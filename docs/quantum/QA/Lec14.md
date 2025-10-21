# The $\op{HSP}$ in the Heisenberg group

## The Heisenberg group

Heisenberg 群有几种不同定义方式. 对于那些熟悉高维系统量子纠错码的人来说，最熟悉的定义可能如下：给定一个质数 $p$，定义作用在一组标准正交态 $\{ \ket{x} : x \in \mathbb{Z}_p \}$ 上的移位算符 $X$ 和相位算符 $Z$ 如下：

\begin{gather*}
    X \ket{x} = \ket{x + 1 \bmod p}, \\
    Z \ket{x} = \omega_p^x \ket{x}.
\end{gather*}

算子满足关系 $ZX = \omega_p XZ$. 所以任何 $X$ 和 $Z$ 的乘积都可以写作 $\omega_p^a X^b Z^c$，其中 $a, b, c \in \mathbb{Z}_p$. 因此算子 $X$ 和 $Z$ 生成了一个 $p^3$ 阶的群，称为 Heisenberg 群. 将群元素写作 $(a, b, c)$，其中 $a, b, c \in \mathbb{Z}_p$，群运算定义为

\[
    (a, b, c) \cdot (a', b', c') = (a + a' + b c', b + b', c + c').
\]

等价地，Heisenberg 群可以表示为 $3 \times 3$ 下三角矩阵的乘法群：

\[
    \left\{ \begin{pmatrix}
        1 & 0 & 0 \\
        b & 1 & 0 \\
        a & c & 1
    \end{pmatrix} : a, b, c \in \mathbb{Z}_p \right\}.
\]

以及半直积 $\mathbb{Z}_p^2 \rtimes_\varphi \mathbb{Z}_p$，其中 $\varphi : \mathbb{Z}_p \to \op{Aut}(\mathbb{Z}_p^2)$ 定义为 $\varphi(c)(a, b) = (a + b c, b)$.

而为了解决 Heisenberg 群上的 $\op{HSP}$，能够区分以下 $p$ 阶循环子群

\[
    H_{a, b} = \langle (a, b, 1) \rangle = \{ (a, b, 1)^x : x \in \mathbb{Z}_p \}
\]

即可. 这种情况的归约本质上与将二面体群 $\op{HSP}$ 归约为隐藏反射情况相同. 通过简单的归纳论证可以得到这类子群中的元素具有以下形式：

\[
    (a, b, 1)^x = (xa + \binom{x}{2} b, xb, x).
\]

容易得到，对于任意 $a, b \in \mathbb{Z}_p$，$p^2$ 个元素 $(l, m, 0)$，其中 $l, m \in \mathbb{Z}_p$，构成了 $H_{a, b}$ 在 Heisenberg 群中的左陪集代表元集合.

## Fourier sampling

设 $f$ 隐藏的子群为 $H_{a, b}$. 那么利用标准方法产生的陪集态为

\[
    \ket{(l, m, 0) H_{a, b}} = \frac{1}{\sqrt{p}} \sum_{x \in \mathbb{Z}_p} \ket{(l + x a + \binom{x}{2} b, m + x b, x)},
\]

其中 $l, m$ 是均匀随机选择的. 目标是通过这些态来确定 $a$ 和 $b$. 类似二面体群中的操作，利用阿贝尔群上的 Fourier 变换去替代整体的非阿贝尔群 Fourier 变换，利用 Heisenberg 群的表示理论就可以证明二者是等价的. 对前两个寄存器在 $\mathbb{Z}_p^2$ 上执行 Fourier 变换，得到

\[
    (F_{\mathbb{Z}_p} \otimes F_{\mathbb{Z}_p} \otimes I) \ket{(l, m, 0) H_{a, b}} = \frac{1}{p^{3/2}} \sum_{x, s, t \in \mathbb{Z}_p} \omega_p^{s (l + x a + \binom{x}{2} b) + t (m + x b)} \ket{s, t, x}.
\]

因为态的密度矩阵是分块对角，且由 $s, t$ 索引，所以可以测量 $s$ 和 $t$ 而不丢失信息. 测量后得到的 $p$ 维量子态为

\begin{align*}
    \ket{\widehat{H_{a, b; s, t}}} &:= \frac{1}{\sqrt{p}} \sum_{x \in \mathbb{Z}_p} \omega_p^{s (x a + \binom{x}{2} b) + t (x b)} \ket{x} \\
    & = \frac{1}{\sqrt{p}} \sum_{x \in \mathbb{Z}_p} \omega_p^{a(s x) + b \left( s \binom{x}{2} + t x \right)} \ket{x}.
\end{align*}

其中 $s, t \in \mathbb{Z}_p$ 是已知且均匀随机获取的. 

## Two states are better than one

如果只有这个态的一个副本，则没有足够的信息来恢复隐藏子群：Holevo 定理保证，对一个 $p$ 维量子态的测量最多能可靠地通信 $p$ 个不同的结果，但有 $p^2$ 个可能的 $(a, b) \in \mathbb{Z}_p^2$ 值，因此需要至少两个态的副本才能可靠地区分这些子群. 虽然可以证明对 $\op{poly}(\log p)$ 个样本进行单寄存器测量就足够恢复 $a$ 和 $b$，并且随机测量以高概率具有这一性质；但尚未知晓是否存在一种单寄存器测量，可以高效地提取 $a$ 和 $b$ 的信息.

然而，通过对两个态副本进行联合测量，便可以恢复相位中二次函数编码的关于 $a$ 和 $b$ 的信息. 

\begin{align*}
    \ket{\widehat{H_{a, b; s, t}}} \otimes \ket{\widehat{H_{a, b; u, v}}} & = \frac{1}{p} \sum_{x, y \in \mathbb{Z}_p} \omega_p^{a (s x + u y) + b \left( s \binom{x}{2} + t x + u \binom{y}{2} + v y \right)} \ket{x, y} \\
    & = \frac{1}{p} \sum_{x, y \in \mathbb{Z}_p} \omega_p^{\alpha a + \beta b} \ket{x, y},
\end{align*}

其中

\begin{align*}
    \alpha & := s x + u y, \\
    \beta & := s \binom{x}{2} + t x + u \binom{y}{2} + v y.
\end{align*}

如果能用 $\ket{\alpha, \beta}$ 来替代 $\ket{x, y}$，那么结果态就是简单的 $\ket{a, b}$ 的 Fourier 变换，从而可以通过逆 Fourier 变换来恢复 $a$ 和 $b$. 所以在辅助寄存器中计算 $\ket{\alpha, \beta}$，得到态

\[
    \frac{1}{p} \sum_{x, y \in \mathbb{Z}_p} \omega_p^{\alpha a + \beta b} \ket{x, y, \alpha, \beta},
\]

并尝试对前两个寄存器取消计算.

对于固定的 $\alpha, \beta, s, t, u, v \in \mathbb{Z}_p$，二次方程组可能具有 $0$、$1$ 或 $2$ 个解 $(x, y)$. 因此，无法期望通过一个基于第三和第四寄存器中的值（以及已知的 $s, t, u, v$）地经典过程来取消计算前两个寄存器. 然而，通过考虑解的全集

\[
    S_{\alpha, \beta}^{s, t, u, v} := \{ (x, y) \in \mathbb{Z}_p^2 : s x + u y = \alpha, \ s \binom{x}{2} + t x + u \binom{y}{2} + v y = \beta \},
\]

依据 $\ket{S} = \sum_{s \in S} \ket{s} / \sqrt{\lvert S \rvert}$，可以将态重写为

\[
    \frac{1}{p} \sum_{\alpha, \beta \in \mathbb{Z}_p} \omega_p^{\alpha a + \beta b} \sqrt{\lvert S_{\alpha, \beta}^{s, t, u, v} \rvert} \ket{S_{\alpha, \beta}^{s, t, u, v}, \alpha, \beta}.
\]

因此，只要能实现酉变换满足

\[
    \ket{S_{\alpha, \beta}^{s, t, u, v}} \mapsto \ket{\alpha, \beta}, \ \lvert S_{\alpha, \beta}^{s, t, u, v} \rvert \neq 0,
\]

就能完成取消计算前两个寄存器的任务，得到态

\[
    \frac{1}{p} \sum_{\alpha, \beta \in \mathbb{Z}_p} \omega_p^{\alpha a + \beta b} \sqrt{\lvert S_{\alpha, \beta}^{s, t, u, v} \rvert} \ket{\alpha, \beta}.
\]

因此实际上也可以直接进行变换而不额外计算 $\alpha$ 和 $\beta$. 称呼 $\ket{S_{\alpha, \beta}^{s, t, u, v}} \mapsto \ket{\alpha, \beta}$ 的逆为**量子采样**（quantum sampling），因为目标是产生解集上的均匀叠加，这是从那些解中随机采样的自然量子模拟. 直接计算表明解可以以封闭解形式给出：

\[
    x = \frac{\alpha s + s v - t u \pm \sqrt{\Delta}}{s(s + u)}, \quad y = \frac{\alpha u + t u - s v \mp \sqrt{\Delta}}{u(s + u)},
\]

其中

\[
    \Delta := (2 \beta s + \alpha s - \alpha^2 - 2 \alpha t) (s + u) u + (\alpha u + t u - s v)^2.
\]

只要  $s u (s + u) \neq 0$，解的数量完全由 $\Delta$ 的值决定. 若 $\Delta$ 是 $\mathbb{Z}_p$ 中的非零平方数，则有两个解；若 $\Delta = 0$，则有一个解；否则没有解. 因为每种情况下都可以高效地计算解的显式表达，因而可以高效地实现变换.

只要解接近于均匀分布，态便接近于 $\ket{a, b}$ 的 Fourier 变换. 因为 $s, t, u, v$ 在 $\mathbb{Z}_p$ 中均匀随机选择，所以 $\Delta$ 也是均匀随机分布在 $\mathbb{Z}_p$ 中的. 因此，$\Delta$ 是非零平方数的概率约为 $1/2$，有两个解的概率也约为 $1/2$；$\Delta = 0$ 的概率为 $1/p$；没有解的概率约为 $1/2$. 这种分布足够接近均匀分布.

应用 $\mathbb{Z}_p \times \mathbb{Z}_p$ 上的逆 Fourier 变换后，得到

\[
    \frac{1}{p^2} \sum_{\alpha, \beta, k, l \in \mathbb{Z}_p} \omega_p^{\alpha (a - k) + \beta (b - l)} \sqrt{\lvert S_{\alpha, \beta}^{s, t, u, v} \rvert} \ket{k, l}.
\]

测量后，得到 $(k, l) = (a, b)$ 的概率为

\[
    \frac{1}{p^4} \left( \sum_{\alpha, \beta \in \mathbb{Z}_p} \lvert S_{\alpha, \beta}^{s, t, u, v} \rvert \right)^2.
\]

由于这些值均匀随机出现，算法的整体成功概率是：

\begin{align*}
    \frac{1}{p^8} \sum_{s, t, u, v \in \mathbb{Z}_p} \left( \sum_{\alpha, \beta \in \mathbb{Z}_p} \sqrt{\lvert S_{\alpha, \beta}^{s, t, u, v} \rvert} \right)^2 & \geq \frac{1}{p^{12}} \left( \sum_{s, t, u, v \in \mathbb{Z}_p} \sum_{\alpha, \beta \in \mathbb{Z}_p} \sqrt{\lvert S_{\alpha, \beta}^{s, t, u, v} \rvert} \right)^2 \\
    & \geq \frac{1}{p^{12}} \left( \sum_{\alpha, \beta \in \mathbb{Z}_p} \frac{p^4}{2 + o(1)} \sqrt{2} \right)^2 \\
    = \frac{1}{2} (1 - o(1)).
\end{align*}

这表明算法以接近 $\frac{1}{2}$ 的概率成功.