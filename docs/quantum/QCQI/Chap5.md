# The quantum Fourier transform and its applications

## The quantum Fourier transform

离散傅里叶变换：

\[
    y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{2\pi \i jk/N}.
\]

量子傅里叶变换：

\[
    \ket{j} \to \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi \i jk/N} \ket{k},
\]

也就有

\[
    \sum_{j=0}^{N-1} x_j \ket{j} \to \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} y_k \ket{k} 
\]

以下讨论中取 $N = 2^n$，并且有如下二进制表示法：

\begin{align*}
    j = j_1j_2\ldots j_n & \Rightarrow j = j_1 2^{n-1} + j_2 2^{n-2} + \cdots + j_n 2^0 \\
    j = 0.j_lj_{l+1}\ldots j_m & \Rightarrow = j_l /2 + j_{l+1}/4 + \cdots + j_m/2^{m-l+1}
\end{align*}

通过一些代数变形就能得到量子傅里叶变换的乘积形式：

\[
    \ket{j_1, j_2, \ldots, j_n} \to \frac{\left(\ket{0} + e^{2\pi \i 0.j_n}\ket{1}\right) (\ket{0} + e^{2\pi \i 0.j_{n-1}j_n}\ket{1}) \cdots (\ket{0} + e^{2\pi \i 0.j_1j_2\ldots j_n}\ket{1})}{2^{n/2}} 
\]

变形过程如下：

\begin{align*}
    \ket{j} & \to \frac{1}{2^{n/2}} \sum_{k=0}^{2^n-1} e^{2\pi \i jk/2^n} \ket{k} \\
            & = \frac{1}{2^{n/2}} \sum_{k_1=0}^{1} \cdots \sum_{k_n=0}^{1} e^{2\pi \i j \sum_{l=1}^n k_l 2^{-l}} \ket{k_1, k_2, \ldots, k_n} \\
            & = \frac{1}{2^{n/2}} \sum_{k_1=0}^{1} \cdots \sum_{k_n=0}^{1} \bigotimes_{l=1}^n e^{2\pi \i j k_l 2^{-l}} \ket{k_l} \\
            & = \frac{1}{2^{n/2}} \bigotimes_{l=1}^n \left(\sum_{k_l=0}^{1} e^{2\pi \i j k_l 2^{-l}} \ket{k_l}\right) \\
            & = \frac{1}{2^{n/2}} \bigotimes_{l=1}^n \left(\ket{0} + e^{2\pi \i j 2^{-l}} \ket{1}\right)
\end{align*}

注意到 $j \cdot 2^{-l} = j_1j_2\ldots j_{n-l}.j_{n-l+1} \cdots j_n$，并且 $e^{2\pi \i j 2^{-l}} = e^{2\pi \i 0.j_{n-l+1} \cdots j_n}$，所以有

\[
    \ket{j} \to \frac{\left(\ket{0} + e^{2\pi \i 0.j_n}\ket{1}\right) (\ket{0} + e^{2\pi \i 0.j_{n-1}j_n}\ket{1}) \cdots (\ket{0} + e^{2\pi \i 0.j_1j_2\ldots j_n}\ket{1})}{2^{n/2}}
\]

以下是电路图，其中 $R_k$ 表示这样的酉变换：

\[
    R_k = \begin{pmatrix}
        1 & 0 \\
        0 & e^{2\pi \i /2^k}
    \end{pmatrix}
\]

\qcircuit
    \lstick{\ket{j_1}} & \qw & \gate{H} & \gate{R_2} & \qw & \cdots & & \gate{R_{n-1}} & \gate{R_n} & \qw & \qw & \qw & \qw & \qw & \qw & \qw & \qw & \qw & \qw & \qw & \qw & \qw & \rstick{\ket{0} + e^{2 \pi i 0.j_1 j_2 \cdots j_n} \ket{1}} \\
    \lstick{\ket{j_2}} & \qw & \qw & \ctrl{-1} & \qw & \cdots &  & \qw & \qw & \gate{H} & \qw & \cdots & & \gate{R_{n-2}} & \gate{R_{n-1}} & \qw & \cdots & & \qw & \qw & \qw & \qw & \rstick{\ket{0} + e^{2 \pi i 0. j_2 \cdots j_n} \ket{1}} \\
    \lstick{\vdots} \\
    \lstick{\ket{j_{n-1}}} & \qw & \qw & \qw & \qw & \qw & \qw & \ctrl{-3} & \qw & \qw & \qw & \qw & \qw & \ctrl{-2} & \qw & \qw & \cdots & & \gate{H} & \gate{R_2} & \qw & \qw & \rstick{\ket{0} + e^{2 \pi i 0. j_{n-1} j_n} \ket{1}} \\
    \lstick{\ket{j_n}} & \qw & \qw & \qw & \qw & \qw & \qw & \qw & \ctrl{-4} & \qw & \qw & \qw & \qw & \qw & \ctrl{-3} & \qw & \cdots & & \qw & \ctrl{-1} & \gate{H} & \qw & \rstick{\ket{0} + e^{2 \pi i 0. j_n} \ket{1}} \\

整个电路使用了 $n$ 个 Hadarmard 门和 $n(n+1)/2$ 个受控门，此外还需要至多 $n/2$ 次交换操作，每次交换操作需要 $3$ 个受控非门，所以这个电路的复杂度是 $\Theta(n^2)$.

应用缺陷：

1. 测量不能直接获得量子计算机中的振幅；

2. 初始态难以制备.

## Phase estimation

假定酉算子 $U$ 有一特征向量 $\ket{u}$ 和对应的特征值 $e^{2\pi \i \varphi}$，但是 $\varphi$ 是未知的. 相位估计算法的目标是估计 $\varphi$ 的值，为了实现相位估计需要假定我们具有能够制备 $\ket{u}$ 和实施受控 $U^{2^j}$ 门的 Oracle. 以下是相位估计算法的第一阶段电路图，使用了两个寄存器. 第一个寄存器位数为 $t$，选取与估计精度和成功率相关；而第二个寄存器用于容纳状态 $\ket{u}$.

\qcircuit
    \lstick{\ket{0}} & \gate{H} & \qw & \qw & \qw & \qw & \cdots & & \qw & \ctrl{6} & \qw & \ket{0} & \rstick{e^{2\pi i(2^{t-1})\varphi}\ket{1}} \\
    \\
    \lstick{\ket{0}} & \gate{H} & \qw & \qw & \ctrl{4} & \qw & \cdots & & \qw & \qw & \qw & \ket{0} & \rstick{e^{2\pi i(2^2)\varphi}\ket{1}} \\
    \lstick{\ket{0}} & \gate{H} & \qw & \ctrl{3} & \qw & \qw & \cdots & & \qw & \qw & \qw & \ket{0} & \rstick{e^{2\pi i(2^1)\varphi}\ket{1}} \\
    \lstick{\ket{0}} & \gate{H} & \ctrl{2} & \qw & \qw & \qw & \cdots & & \qw & \qw & \qw & \ket{0} & \rstick{e^{2\pi i(2^0)\varphi}\ket{1}} \\
    \\
    & \qw & \multigate{2}{U^{2^0}} & \multigate{2}{U^{2^1}} & \multigate{2}{U^{2^2}} & \qw & \cdots & & \qw & \multigate{2}{U^{2^{t-1}}} & \qw \\
    \lstick{\ket{u}} & \qw & \ghost{U^{2^0}} & \ghost{U^{2^1}} & \ghost{U^{2^2}} & \qw & \cdots & & \qw & \ghost{U^{2^{t-1}}} & \qw & \ket{u} \\
    & \qw & \ghost{U^{2^0}} & \ghost{U^{2^1}} & \ghost{U^{2^2}} & \qw & \cdots & & \qw & \ghost{U^{2^{t-1}}} & \qw \\

只需要考虑受控门实际上等价于 $\ket{j}(U^j)^{2^i}\ket{u}$，所以对于 $\frac{1}{\sqrt{2}}(\ket{0} + \ket{1})$，代入后有

\[
    \frac{1}{\sqrt{2}} (\ket{0} + \ket{1}U^{2^i}) \ket{u} = \frac{1}{\sqrt{2}} (\ket{0} + e^{2\pi \i 2^i \varphi} \ket{1}) \ket{u}.
\]

所以整个电路的终态为

\[
    \frac{1}{2^{t/2}} \sum_{k = 0}^{2^t - 1} e^{2\pi \i \varphi k} \ket{k}.
\]

接下来再施加一个逆量子傅里叶变换即可.

### Performance and requirements

设 $b$ 是 $[0, 2^t - 1]$ 中的整数，并且满足 $b/2^t = 0.b_1b_2 \cdots b_t$ 是小于 $\varphi$ 的最佳 $t$ 位近似值，也就有差值 $\delta = \varphi - b/2^t$ 应当满足 $0 \leq \delta < 2^{-t}$. 

对第一阶段终态施加逆量子傅里叶变换后的状态为

\[
    \frac{1}{2^t} \sum_{k, l = 0}^{2^t - 1} e^{\frac{-2\pi \i k l}{2^t}} e^{2\pi \i \varphi k} \ket{l}.
\]

设 $\alpha_l$ 是 $\ket{(b + l) \pmod{2^t}}$ 的振幅，注意到 $((b + l) \pmod{2^t}) /2^t = (b + l)/2^t$，进而有

\[
    \alpha_l = \frac{1}{2^t} \sum_{k = 0}^{2^t - 1} (e^{2\pi \i (\varphi - (b + l)/2^t)})^k.
\]

这是一个几何级数，所以

\begin{align*}
    \alpha_l & = \frac{1}{2^t} \left(\frac{1 - e^{2\pi \i (2^t\varphi - (b + l))}}{1 - e^{2\pi \i (\varphi - (b + l)/2^t)}}\right) \\
             & = \frac{1}{2^t} \left(\frac{1 - e^{2\pi \i (2^t\delta - l)}}{1 - e^{2\pi \i (\delta - l/2^t)}}\right) \\
\end{align*}

设最终的测量结果为 $m$，那么期望的便是限制住测量得到使得 $\lvert m - b \rvert > e$ 的 $m$ 的概率，其中 $e$ 表示我们对错误的容忍度. 

\[
    p(\lvert m - b \rvert > e) = \sum_{-2^{t-1} < l \leq -(e + 1)} \lvert \alpha_l \rvert^2 + \sum_{(e + 1) \leq l < 2^{t-1}} \lvert \alpha_l \rvert^2.
\]

因为对于任意实数 $\theta$，都有 $\lvert 1 - e^{\i \theta} \rvert \leq 2$，所以有

\[
    \lvert \alpha_l \rvert \leq \frac{2}{2^t \lvert 1 - e^{2\pi \i (\delta - l/2^t)} \rvert}.
\]

而当 $-\pi \leq \theta \leq \pi$ 时，$\lvert 1 - e^{\i \theta} \rvert \geq 2\lvert \theta \rvert/\pi$，并且当 $-2^{t-1} < l \leq 2^{t-1}$ 时有 $-\pi \leq 2\pi(\delta - l/2^t) \leq \pi$，所以有

\[
    \lvert \alpha_l \rvert \leq \frac{2}{2^{t + 1}(\delta - l/2^t)}.
\]

代入得到

\[
    p(\lvert m - b \rvert > e) \leq \frac{1}{4}\left(\sum_{l = -2^{t-1} + 1}^{-(e + 1)} \frac{1}{(l - 2^t \delta)^2} + \sum_{l = (e + 1)}^{2^{t-1}} \frac{1}{(l - 2^t \delta)^2}\right).
\]

而因为 $0 \leq 2^t \delta \leq 1$，所以进一步放缩

\begin{align*}
    p(\lvert m - b \rvert > e) & \leq \frac{1}{4}\left(\sum_{l = -2^{t-1} + 1}^{-(e + 1)} \frac{1}{l^2} + \sum_{l = (e + 1)}^{2^{t-1}} \frac{1}{(l - 1)^2}\right) \\
                               & = \frac{1}{2} \sum_{l = e}^{2^{t-1} - 1} \frac{1}{l^2} \\
                               & \leq \frac{1}{2} \int_{e-1}^{2^{t-1}-1} \mathrm{d} l \frac{1}{l^2} \\
                               & \leq \frac{1}{2(e - 1)}.
\end{align*}

因为希望以 $2^{-n}$ 的误差概率来估计 $\varphi$，所以取 $e = 2^{t-n} - 1$. 使用了 $t = n + p$ 个量子比特用于相位估计，所以得到正确近似的概率至少为 $1 - \frac{1}{2(2^p - 1)}$.

所以，如果想要以 $1 - \varepsilon$ 的概率获得 $\varphi$ 的 $n$ 位近似值，需要

\[
    t = n + \left \lceil \log (2 + \frac{1}{2\varepsilon}) \right \rceil.
\]

相位估计需要输入 $U$ 的特征态 $\ket{u}$ 才能精确测量相位，但是如果制备特定特征态可能十分困难，替代的方法是制备任意态 $\ket{\psi}$，其可以被 $U$ 的特征态线性表示为 $\ket{\psi} = \sum_u c_u \ket{u}$，设 $\ket{u}$ 对应的特征值为 $e^{2\pi \i \varphi_u}$，那么其演化后所输出的态应当很接近于 $\sum_u c_u \ket{\tilde{\varphi}_u} \ket{u}$，其中 $\ket{\tilde{\varphi}_u}$ 是相位 $\varphi_u$ 的极佳近似. 因而测量得到 $\tilde{\varphi}_u$ 的概率为 $\lvert c_u \rvert^2$.

## Applications: order-finding and factoring

### Application: order-finding

量子寻阶算法实际上就是在如下的酉算子上进行相位估计

\[
    U \ket{y} = \ket{xy \pmod{N}},
\]

其中 $y \in {0, 1}^L$，约定当 $N \leq y \leq 2^N - 1$ 时 $xy \pmod{N} = y$.

定义 

\[
    \ket{u_s} = \frac{1}{\sqrt{r}} \sum_{k=0}^{r-1} \exp\left(\frac{-2\pi \i s k}{r}\right) \ket{x^k \pmod{N}},
\]

其中 $r$ 为 $x$ 的阶. 当 $0 \leq s \leq r - 1$ 时，$\ket{u_s}$ 是 $U$ 的特征态，可以通过如下计算验证：

\begin{align*}
    U \ket{u_s} & = \frac{1}{\sqrt{r}} \sum_{k=0}^{r-1} \exp\left(\frac{-2\pi \i s k}{r}\right) U \ket{x^{k+1} \pmod{N}} \\
    & = \frac{1}{\sqrt{r}} \sum_{k=1}^{r} \exp\left(\frac{-2\pi \i s (k-1)}{r}\right) \ket{x^k \pmod{N}} \\
    & = \frac{1}{\sqrt{r}} \sum_{k=1}^{r} \exp\left(\frac{2\pi \i s}{r}\right) \exp\left(\frac{-2\pi \i s k}{r}\right) \ket{x^k \pmod{N}} \\
    & = e^{2\pi \i s / r} \ket{u_s}.
\end{align*}

使用相位估计有两个重要的要求：

- 对任意整数 $j$，都能够高效地实现受控 $U^{2^j}$ 门；

- 能够高效制备非平凡特征值的特征态 $\ket{u_s}$，或至少是这些特征态的叠加态.

第一个要求可以利用模幂运算实现，并且实现相位估计阶段的整个受控 $U^{2^j}$ 操作序列使用了 $O(L^3)$ 个门，其中 $L = \lceil \log N \rceil$ 为 $N$ 的二进制位数.

!!! success "Modular exponentiation"
    希望计算如下的变换

    \begin{align*}
        \ket{z} \ket{y} & \to \ket{z} U^{z_t 2^{t - 1}} \cdots U^{z_1 2^0} \ket{y} \\
                        & = \ket{z} \ket{x^{z_t 2^{t - 1}} \times \cdots \times x^{z_1 2^0} y \pmod{N}} \\
                        & = \ket{z} \ket{x^z y \pmod{N}}
    \end{align*}

    所以结果等价于第二个寄存器乘以模幂 $x^z \pmod{N}$，其中 $z$ 是第一个寄存器的内容. 这一操作可以利用可逆计算轻松完成，基本的想法是在第三个寄存器中可逆计算关于 $z$ 的函数 $x^z \pmod{N}$，然后将结果与第二个寄存器的内容相乘，最后利用取消计算的方式将第三个寄存器的内容清除.

    模幂运算分为两个阶段：

    1. 利用模平方算法计算 $x^{2^j} \pmod{N}$，$j$ 取 $0, 1, \ldots, t - 1$. 令 $t = 2L + 1 + \lceil \log (2 + 1/(2\varepsilon)) \rceil = O(L)$，所以需要 $t - 1 = O(L)$ 次模平方运算. 每次模平方运算需要 $O(L^2)$ 个门，所以总的复杂度为 $O(tL^2) = O(L^3)$.

    2. 基于先前的观察

    \[
        x^z \pmod{N} = (x^{z_t 2^{t - 1}} \pmod{N}) (x^{z_{t-1} 2^{t - 2}} \pmod{N}) \cdots (x^{z_1 2^0} \pmod{N}),
    \]

    采取 $t - 1 = O(L)$ 次模乘运算，每次模乘运算需要 $O(L^2)$ 个门，所以总的复杂度为 $O(tL^2) = O(L^3)$.

    因此可以构建含 $t$ 位寄存器和 $L$ 位寄存器的电路，输入 $(z, y)$，输出 $(z, x^z y \pmod{N})$，总的复杂度为 $O(L^3)$，转换为量子电路后实现 $\ket{z} \ket{y} \to \ket{z} \ket{x^z y \pmod{N}}$ 的量子门数为 $O(L^3)$.

第二个要求如果要制备 $\ket{u_s}$，就必须要知道阶 $r$ 的值. 但是有个方法可以绕过：

\[
    \frac{1}{\sqrt{r}} \sum_{k=0}^{r-1} \ket{u_s} = \ket{1},
\]

因此在相位估计阶段，如果第一个寄存器使用 $t = 2L + 1 + \lceil \log (2 + 1/(2\varepsilon)) \rceil$ 个量子比特，并且第二个寄存器制备为 $\ket{1}$，那么对于每个 $s \in \{0, 1, \ldots, r - 1\}$，算法有 $(1 - \varepsilon)/r$ 的概率测量得到相位估计值 $\varphi \approx s/r$，精确度为 $2L + 1$ 位.

#### The continued fraction expansion

虽然只有 $\varphi$ 前 $2L + 1$ 位的精确度，但有其为有理数的先验知识，如果能计算最接近 $\varphi$ 的分数，便可以得到 $r$. 连分数算法便可以高效的做到这点.

!!! note "Theorem"
    设 $s/r$ 是有理数，并且满足

    \[
        \lvert s/r - \varphi \rvert \leq \frac{1}{2r^2},
    \]

    那么 $s/r$ 是 $\varphi$ 的一个连分数近似，并且可以用连分数算法使用 $O(L^3)$ 的操作计算出来.

因为 $\varphi$ 是 $s/r$ 的前 $2L + 1$ 位近似，且 $r \leq N \leq 2^L$，所以有 $\abs{s/r - \varphi} \leq 2^{-2L + 1} \leq \frac{1}{2r^2}$. 因而如果给定 $\varphi$，连分数算法可以高效得到无公共因子的 $s'$ 和 $r'$ 满足 $s'/r' = s/r$，$r'$ 便是阶的候选值，验证 $x^{r'} \equiv 1 \pmod{N}$ 即可.

#### Performance

寻阶算法有两种可能性失败. 第一是相位估计阶段没有得到预期的结果，这种情况发生的概率至多为 $\varepsilon$，并且可以通过略微增加电路规模来降低这种情况发生的概率. 第二种情况更严重些，即 $s$ 和 $r$ 是有公因子的，此时连分数算法返回的 $r'$ 只是 $r$ 的一个因子. 不过有三种方法解决该问题：

1. 最直接的方法是注意到 $0$ 到 $r - 1$ 范围内随机选择的 $s$ 很有可能与 $r$ 互质. 注意到小于 $r$ 的素数数量至少为 $r / 2 \log r$，所以 $s$ 是素数的概率至少为 $1/2\log r > 1/2\log N$. 重复算法 $2 \log N$ 次便会以高概率观察到 $s/r$ 中 $s$ 和 $r$ 互质，从而得到 $r$.

2. 而注意到如果 $r' \neq r$，那么除非 $s = 0$，都有 $r'$ 是 $r$ 的因子. $s = 0$ 的概率为 $1/r \leq 1/2$，几次重复便可以消除这种可能. 假如用 $a' \equiv a^{r'} \pmod{N}$ 替代 $a$，那么其阶便是 $r/r'$. 接着便重复此算法，直到得到 $r$，至多进行 $\log(r) = O(L)$ 次迭代.

3. 这一方法比前两个方法都要好，因为其只需要常数次尝试. 核心思想是重复两次相位估计-连分数算法过程，分别得到 $r_1', s_1'$ 和 $r_2', s_2'$. 如果 $s_1'$ 和 $s_2'$ 没有公因子，便可以通过取 $r_1'$ 和 $r_2'$ 的最小公倍数来提取 $r$. $s_1'$ 和 $s_2'$ 没有公因子的概率为

\[
    1 - \sum_q p(q \mid s_1') p(q \mid s_2'),
\]

求和遍历所有素数 $q$，$p(x \mid y)$ 表示 $x$ 整除 $y$ 的概率. 如果 $q$ 整除 $s_1'$，那么便也会整除约分前的 $s_1$，所以可以用 $p(q \mid s_1)$ 约束 $p(q \mid s_1')$. 易知 $p(q \mid s_1') \leq p(q \mid s_1) \leq 1/q$. 类似地，$p(q \mid s_2') \leq 1/q$. 所以 $s_1'$ 和 $s_2'$ 没有公因子的概率满足

\[
    1 - \sum_q p(q \mid s_1') p(q \mid s_2') \geq 1 - \sum_q \frac{1}{q^2}.
\]

通过如下的技术，便可以约束以上概率：

!!! note "exercise"
    对所有 $x \geq 2$ 证明 $\int_x^{x + 1} 1/y^2 \mathrm{d}y \geq 2/3x^2$，进而证明

    \[
        \sum_q \frac{1}{q^2} \leq \frac{3}{2} \int_2^\infty \frac{1}{y^2} \mathrm{d}y = \frac{3}{4}.
    \]

所以有

\[
     1 - \sum_q p(q \mid s_1') p(q \mid s_2') \geq \frac{1}{4}.
\]

即获得正确的 $r$ 的概率至少为 $1/4$.

### Application: factoring

因数分解问题实际上和寻阶问题是等价的，接下来将展示如何将因数分解归约到寻阶.

规约分为两步：

1. 证明如果能找到方程 $x^2 = 1 \pmod{N}$ 的非平凡解 $x \neq \pm 1 \pmod{N}$，那么就可以计算出 $N$ 的一个因子；

2. 证明随机选择的与 $N$ 互质的 $y$ 其阶为偶数并且满足 $y^{r/2} \neq \pm 1 \pmod{N}$ 的概率相当高，所以 $x \equiv y^{r/2} \pmod{N}$ 就是 $x^2 = 1 \pmod{N}$ 的一个非平凡解.

!!! note "Theorem"
    设 $N$ 是 $L$ 位的合数，$x$ 是 $x^2 = 1 \pmod{N}$ 的非平凡解，且 $1 \leq x \leq N$，那么 $\gcd(x - 1, N)$ 和 $\gcd(x + 1, N)$ 中至少有一个是 $N$ 的非平凡因数，并且可以在 $O(L^3)$ 的时间复杂度内计算出来.

!!! note "Theorem"
    设 $N = p_1^{\alpha_1} \cdots p_m^{\alpha_m}$ 是一个正奇合数的质因数分解，$x$ 是随机选择的满足 $1 \leq x \leq N - 1$ 且与 $N$ 互质的整数，设 $r$ 为 $x$ 模 $N$ 的阶，那么

    \[
        p(r \text{ is even and } x^{r/2} \neq -1 \pmod{N}) \geq 1 - \frac{1}{2^{m-1}}.
    \]

    !!! bug "原定理有误，可见[勘误](https://yingzhouli.com/posts/2022-06/probability-bound-in-factoring-order-finding.html)"
        

!!! note "Exercise"
    设 $N$ 为 $L$ 位，该练习的目的是给出一个高效的经典算法来决定是否存在 $a \geq 1, b \geq 2$ 使得 $N = a^b$.

    1. 证明如果存在满足条件的 $b$，则 $b \leq L$；

    2. 证明至多需要 $O(L^2)$ 次操作来计算 $\log_2 N$，$x = y/b, b \leq L$，以及最接近 $2^x$ 的两个整数 $u_1$ 和 $u_2$；

    3. 证明至多需要 $O(L^2)$ 次操作来使用重复平方法计算 $u_1^b$ 和 $u_2^b$，以及检查其是否与 $N$ 相等；

    4. 结合先前的结论给出一个 $O(L^3)$ 的算法来决定是否存在满足条件的 $a, b$.

## General applications of the quantum Fourier transform

### Period-finding

设 $f$ 是一个产生单比特输出的周期函数，即 $f(x + r) = f(x)$，其中 $0 < r < 2^L$ 是未知的，$x, r \in \{0, 1, 2, \ldots\}$. 给定黑盒 $U$ 进行酉操作 $U\ket{x}\ket{y} \to \ket{x}\ket{y \oplus f(x)}$. 问题是需要多少次查询和其他操作才能确定 $r$.

\algorithm
    \caption{Period-finding}
    \KwIn{执行 $U\ket{x}\ket{y} \to \ket{x}\ket{y \oplus f(x)}$ 的黑盒 \\ 储存函数结果的寄存器，初始化为 $\ket{0}$ \\ $t = O(L + \log(1/\varepsilon))$ 个初始化为 $\ket{0}$ 的量子比特}
    \KwOut{最小正周期 $r$}
    \KwData{一次查询，$O(L^2)$ 次其他操作，成功概率 $O(1)$}
    \KwResult{}
    $\ket{0} \ket{0} \quad \text{初始态}$\;
    $\to \frac{1}{\sqrt{2^t}} \sum_{x=0}^{2^t-1} \ket{x} \ket{0} \quad \text{叠加态}$\;
    $\to \frac{1}{\sqrt{2^t}} \sum_{x=0}^{2^t-1} \ket{x} \ket{f(x)} \quad \text{施加 } U $\;
    $\approx \frac{1}{\sqrt{r2^t}} \sum_{l=0}^{r-1} \sum_{x=0}^{2^t-1} e^{2\pi \mathrm{i} l x/r} \ket{x} \ket{\hat{f}(l)}$\;
    $\to \frac{1}{\sqrt{r}} \sum_{l=0}^{r-1} \ket{\widetilde{l/r}}\ket{\hat{f}(l)} \quad \text{施加 } \operatorname{QFT}^\dagger$\;
    $\to \widetilde{l/r} \quad \text{测量}$\;
    $\to r \quad \text{连分数算法}$\;

第 3 行中的 $\ket{\hat{f}(l)}$ 定义为

\[
    \ket{\hat{f}(l)} = \frac{1}{\sqrt{r}} \sum_{x=0}^{r-1} e^{-2\pi \i l x/r} \ket{f(x)}
\]

其为 $\ket{f(x)}$ 的傅里叶变换. 而因为 $\sum_{l=0}^{r-1} e^{2\pi \i l x/r} = \begin{cases}
r, & r \mid x \\
0, & \text{otherwise}
\end{cases}$，所以第 3 行成立. 第 4 行的近似是因为 $2^t$ 可能不是 $r$ 的倍数，不过也不需要是倍数，这在相位估计中通过误差边界处理，已经能确保估计值足够精确.

接下来介绍傅里叶变换的平移不变性. 用如下的符号描述量子傅里叶变换：

\[
    \sum_{h \in H} \alpha_h \ket{h} \to \sum_{g \in G} \tilde{\alpha}_g \ket{g},
\]

其中 $\tilde{\alpha}_g = \sum_{h \in H} \alpha_h e^{2\pi \i gh/\lvert G \rvert}$，$H$ 是 $G$ 的某个子集，而 $G$ 索引了 Hilbert 空间中的某组单位正交基. 假设对初始状态应用酉变换 $U_k$，其作用为

\[
    U_k\ket{g} = \ket{g + k}.
\]

然后应用傅里叶变换，结果为

\[
    U_k \sum_{h \in H} \alpha_h \ket{h} = \sum_{h \in H} \alpha_h \ket{h + k} \to \sum_{g \in G} e^{2\pi \i g k/\lvert G \rvert} \tilde{\alpha}_g \ket{g}.
\]

而无论 $k$ 取何值，都有

\[
    \lvert e^{2\pi \i g k/\lvert G \rvert} \tilde{\alpha}_g \rvert = \lvert \tilde{\alpha}_g \rvert.
\]

即 $\ket{g}$ 的振幅大小不会改变. 用群论的语言表述的话，$G$ 是群，$H$ 是其子群，如果 $G$ 上的函数 $f$ 在 $H$ 的陪集上是常数的话，$f$ 的傅里叶变换就在 $H$ 的陪集上是不变.

### Discrete logarithms

考虑一个更复杂的函数 $f(x_1, x_2) = a^{sx_1 + x_2} \bmod{N}$，所有的参数均为整数，并且 $r$ 是 $a$ 模 $N$ 的阶. 这个函数也具有周期性，因为 $f(x_1 + l, x_2 - ls) = f(x_1, x_2)$，但这里的周期实际上是个二元组 $(l, -ls)$，其中 $l$ 是整数. 如果能确定 $s$ 便可以解决离散对数问题：给定 $a$ 和 $b = a^s$，求 $s$. 黑盒 $U$ 进行酉变换 $U\ket{x_1}\ket{x_2}\ket{y} \to \ket{x_1}\ket{x_2}\ket{y \oplus f(x_1, x_2)}$. 以下给出了解决该问题的量子算法，这里假设 $r$ 已知，因为可以用寻阶算法确定.

\algorithm
    \caption{Discrete logarithm}
    \KwIn{执行 $U\ket{x_1}\ket{x_2}\ket{y} \to \ket{x_1}\ket{x_2}\ket{y \oplus f(x_1, x_2)}$ 的黑盒 \\ 储存函数结果的寄存器，初始化为 $\ket{0}$ \\两个拥有 $t = O(\lceil \log r \rceil + \log(1/\varepsilon))$ 个量子比特的寄存器，初始化为 $\ket{0}$}
    \KwOut{使得 $a^s = b$ 的最小正整数 $s$}
    \KwData{一次查询，$O(\lceil \log r \rceil^2)$ 次其他操作，成功概率 $O(1)$}
    \KwResult{}
    $\ket{0} \ket{0} \ket{0} \quad \text{初始态}$\;
    $\to \frac{1}{2^t} \sum_{x_1=0}^{2^t-1} \sum_{x_2=0}^{2^t-1} \ket{x_1} \ket{x_2} \ket{0} \quad \text{叠加态}$\;
    $\to \frac{1}{2^t} \sum_{x_1=0}^{2^t-1} \sum_{x_2=0}^{2^t-1} \ket{x_1} \ket{x_2} \ket{f(x_1, x_2)} \quad \text{施加 } U $\;
    $\approx \frac{1}{2^t\sqrt{r}} \sum_{l_2=0}^{r-1} \sum_{x_1=0}^{2^t-1} \sum_{x_2=0}^{2^t-1} e^{2\pi\mathrm{i} (sl_2x_1+l_2x_2)/r} \ket{x_1} \ket{x_2} \ket{\hat{f}(sl_2, l_2)}$\;
    $= \frac{1}{2^t\sqrt{r}} \sum_{l_2=0}^{r-1} \left[\sum_{x_1=0}^{2^t-1} e^{2\pi\mathrm{i} (sl_2x_1)/r} \ket{x_1} \right] \left[\sum_{x_2=0}^{2^t-1} e^{2\pi\mathrm{i} (l_2x_2)/r} \ket{x_2} \ket{\hat{f}(sl_2, l_2)}\right]$\;
    $\to \frac{1}{\sqrt{r}} \sum_{l_2=0}^{r-1} \ket{\widetilde{sl_2/r}} \ket{\widetilde{l_2/r}} \ket{\hat{f}(sl_2, l_2)} \quad \text{施加 } \operatorname{QFT}^\dagger$\;
    $\to (\widetilde{sl_2/r}, \widetilde{l_2/r}) \quad \text{测量}$\;
    $\to s \quad \text{推广连分数算法}$\;

第 3 行引入状态

\[
    \ket{\hat{f}(l_1, l_2)} = \sum_{x_1=0}^{r-1} \sum_{x_2=0}^{r-1} e^{-2\pi \i (l_1x_1+l_2x_2)/r} \ket{f(x_1, x_2)} = \frac{1}{\sqrt{r}} \sum_{j=0}^{r-1} e^{-2\pi \i (l_2j)/r} \ket{f(0, j)}.
\]

$l_1$ 和 $l_2$ 必须满足

\[
    \sum{k = 0}^{r - 1} e^{2\pi\i k(l_1/s - l_2)/r} = r,
\]

否则 $\ket{\hat{f}(l_1, l_2)}$ 几乎为 $0$.

### The hidden subgroup problem

以上两个问题其实都是隐藏子群问题的特例，隐藏子群问题可以表述为

!!! question "隐藏子群问题"
    设函数 $f$ 从有限生成群 $G$ 映射到有限集合 $X$，满足其在子群 $K$ 的陪集上是常数，并且在不同的赔集上是不同的. 给定一个量子黑盒，其可以执行酉变换 $U \ket{g} \ket{x} = \ket{g} \ket{x \oplus f(g)}$，其中 $g \in G$，$x \in X$，$\oplus$ 是 $X$ 上良定义的二元运算. 问题是找到子群 $K$ 的生成集合.