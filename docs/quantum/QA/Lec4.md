# The abelian quantum Fourier transform and phase estimation

## Quantum Fourier transform

阿贝尔群 $G$ 上的量子傅里叶变换（quantum Fourier transform, $\op{QFT}$）定义为

\[
    F_G := \frac{1}{\sqrt{\lvert G \rvert}} \sum_{x \in G} \sum_{y \in \hat{G}} \chi_y(x) \ket{y}\bra{x}.
\]

$\hat{G}$ 是 $G$ 的一个完全特征标集，$\chi_y(x)$ 表示 $G$ 的第 $y$ 个特征标在 $x$ 处的取值.

最简单的 $\op{QFT}$ 情形对应 $G = \mathbb{Z}_2^n$，因为其上的特征标为 $\chi_y(x) = (-1)^{x \cdot y}$，所以

\[
    F_{\mathbb{Z}_2^n} = \frac{1}{\sqrt{2^n}} \sum_{x, y \in \mathbb{Z}_2^n} (-1)^{x \cdot y} \ket{y}\bra{x} = H^{\otimes n}.
\]

## $\op{QFT}$ over $\mathbb{Z}_{2^n}$

$G = \mathbb{Z}_{2^n}$ 时 情况稍微复杂些：

\[
    F_{\mathbb{Z}_{2^n}} = \frac{1}{\sqrt{2^n}} \sum_{x, y \in \mathbb{Z}_{2^n}} \omega_{2^n}^{xy} \ket{y}\bra{x}.
\]

其中 $\omega_m = e^{2\pi \i / m}$ 是 $m$ 次单位根. 接下来将 $x, y$ 写作二进制串来进行分析：

\begin{align*}
    \ket{x} & \mapsto \frac{1}{\sqrt{2^n}} \sum_{y \in \mathbb{Z}_{2^n}} \omega_{2^n}^{xy} \ket{y} \\
            & = \frac{1}{\sqrt{2^n}} \sum_{y \in \mathbb{Z}_{2^n}} \omega_{2^n}^{x\left(\sum_{k=0}^{n-1} 2^k y_k\right)} \ket{y_{n-1} \ldots y_1y_0} \\
            & = \frac{1}{\sqrt{2^n}} \sum_{y \in \mathbb{Z}_{2^n}} \prod_{k=0}^{n-1} \omega_{2^n}^{x y_k 2^k} \ket{y_{n-1} \ldots y_1y_0} \\
            & = \frac{1}{\sqrt{2^n}} \bigotimes_{k=0}^{n-1} \sum_{y_k \in \mathbb{Z}_2} \omega_{2^n}^{x y_k 2^k} \ket{y_k} \\
            & = \bigotimes_{k=0}^{n-1} \ket{z_k},
\end{align*}

其中

\begin{align*}
    \ket{z_k} & := \frac{1}{\sqrt{2}} \sum_{y_k \in \mathbb{Z}_2} \omega_{2^n}^{x y_k 2^k} \ket{y_k} \\
              & = \frac{1}{\sqrt{2}} \left( \ket{0} + \omega_{2^n}^{x 2^k} \ket{1} \right) \\
              & = \frac{1}{\sqrt{2}} \left( \ket{0} + \omega_{2^n}^{\left(\sum_{j=0}^{n-1} x_j 2^{j+k}\right)} \ket{1} \right) \\
              & = \frac{1}{\sqrt{2}} \left( \ket{0} + e^{2\pi \i \left(x_0 2^{k-n} + x_1 2^{k+1-n} + \cdots + x_{n-1-k} 2^{-1}\right)} \ket{1} \right).
\end{align*}

也可写作 $\ket{z_k} = \frac{1}{\sqrt{2}} \left( \ket{0} + \omega_{2^{n-k}}^x \ket{1} \right)$，第一种写法便于理解其电路实现. 所以 $F\ket{x}$是单比特态 $\ket{z_k}$ 的张量积，第 $k$ 个量子比特只由 $x$ 的低 $n-k$ 位决定. 定义

\[
    R_k := \begin{pmatrix}
        1 & 0 \\
        0 & \omega_{2^k}
    \end{pmatrix},
\]

电路图与复杂度不多赘述.

## Phase estimation

相位估计也是基于 $\mathbb{Z}_{2^n}$ 上的 $\op{QFT}$. 给定酉算子 $U$ 及其本征态 $\ket{\phi}$，满足 $U\ket{\phi} = e^{\i \phi} \ket{\phi}$. $U$ 要么是白盒形式，要么是允许进行受控 $U^j$ 操作的黑盒形式. 目标是在合适的精度下估计 $\phi$. 为了得到 $\phi$ 的 $n$ 位二进制近似，需要先制备状态

\[
    \frac{1}{\sqrt{2^n}} \sum_{x \in \mathbb{Z}_{2^n}} \ket{x, \phi},
\]

然后应用算子

\[
    \sum_{x \in \mathbb{Z}_{2^n}} \ket{x}\bra{x} \otimes U^x,
\]

得到

\[
    \frac{1}{\sqrt{2^n}} \sum_{x \in \mathbb{Z}_{2^n}} e^{\i \phi x} \ket{x, \phi}.
\]

对第一个寄存器应用逆 $\op{QFT}$ 并进行测量. 如果 $\phi/2\pi$ 的二进制展开在至多 $n$ 位后终止（即 $\phi = 2\pi y/2^n$），那么之前的状态便可以写作 $F_{\mathbb{Z}_{2^n}} \ket{y} \otimes \ket{\phi}$，得到的 $y$ 就是 $\phi/2\pi$ 的精确二进制表示. 一般情况下是高概率得到较好的近似，特别地，获得 $y$ 的概率为

\[
    \op{Pr}(y) = \frac{1}{2^{2n}} \frac{\sin^2(2^{n-1} \phi)}{\sin^2(\phi/2 - \pi y / 2^n)}.
\]

## $\op{QFT}$ over $\mathbb{Z}_N$ and over general finite abelian groups

可以进一步利用相位估计来实现任意循环群 $\mathbb{Z}_N$ 上的 $\op{QFT}$：

\[
    F_{\mathbb{Z}_N} = \frac{1}{\sqrt{N}} \sum_{x, y \in \mathbb{Z}_N} \omega_N^{xy} \ket{y}\bra{x}.
\]

目标是 $\ket{x} \mapsto \ket{\tilde{x}}$，其中 $\ket{\tilde{x}} := F_{\mathbb{Z}_N} \ket{x}$ 是一个 Fourier 基态. 而直接执行 $\ket{x, 0} \mapsto \ket{x, \tilde{x}}$ 是相对简单的，所以问题转变为如何擦除 $\ket{x}$. 考虑模 $N$ 加 $1$ 的酉算子

\[
    U := \sum_{x \in \mathbb{Z}_N} \ket{x+1}\bra{x}.
\]

该算子的特征态正是傅里叶基态 $\ket{\tilde{x}}$，因为

\[
    F_{\mathbb{Z}_N}^\dagger U F_{\mathbb{Z}_N} = \sum_{x \in \mathbb{Z}_N} \omega_N^{-x} \ket{x}\bra{x},
\]

也就有

\[
    U \ket{\tilde{x}} = \omega_N^{-x} \ket{\tilde{x}}.
\]

所以通过 $U$ 上的相位估计可以得到 $x$ 的近似值，也就可以实现

\[
    \ket{\tilde{x}, 0} \mapsto \ket{\tilde{x}, x}.
\]

逆向操作便可以擦除 $\ket{x}$.

而有限阿贝尔群可以被分解为循环群的直积，群直积的 $\op{QFT}$ 可以通过各个循环群的 $\op{QFT}$ 的张量积来实现.