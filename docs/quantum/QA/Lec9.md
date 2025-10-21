# Period finding from $\mathbb{Z}$ to $\mathbb{R}$

## Period finding over the integers

寻阶算法本质上也是在寻找满足 $g^x \bmod{L} = g^{x+r} \bmod{L}$ 的最小正整数 $r$，分解 $L$ 也就归约到群 $G = \mathbb{Z}_L$ 上元素 $g \in \mathbb{Z}_L^\times$ 的寻阶问题. 所以最终整个问题规约为如何高效寻找函数 $f(x) = g^x$ 的周期 $r$.

因为 $r$ 通常不整除一个已知的的整数 $N$，所以这不应该视为 $\mathbb{Z}_N$ 上的周期寻找问题，而是 $\mathbb{Z}$ 上的周期寻找问题，或等价的隐藏子群问题. 不过计算机上自然不能表示任意整数，所以只考虑在确定了 $N$ 的情况下函数在 $\{0, 1, \ldots, N-1\}$ 上的取值，并且在 $\mathbb{Z}_N$ 上进行 Fourier 采样，即便函数在 $\mathbb{Z}_N$ 上并非精确周期性的，这个过程也能实现，但这需要周期足够小. 接下来将给出如果已知周期的一个先验上界 $M$ 该如何选取 $N$；如果没有上界便从 $M = 2$ 开始反复加倍直到算法可以工作，而整个过程的开销只是 $\op{poly}(\log r)$.

依然均匀叠加态计算函数起手：

\[
\frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} \ket{x} \mapsto \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} \ket{x, f(x)},
\]

然后经典丢弃第二个寄存器，使得第一个寄存器处于混合态. 因为 $f$ 是一个周期为 $r$ 的函数，所以每个测量结果会得到的是间隔为 $r$ 的点上的叠加态，点的个数 $n$ 取决于第一个点 $x_0 \in \{0, \ldots, r-1\}$ 的位置，因为考虑在 $\{0, \ldots, N-1\}$ 上的函数，其有 $\lfloor N/r \rfloor$ 个完整周期，和 $N - r\lfloor N/r \rfloor$ 个残余的点. 所以若 $x_0 < N - r\lfloor N/r \rfloor$，$n = \lfloor N/r \rfloor + 1$，否则 $n = \lfloor N/r \rfloor$. 因此对应测量结果的叠加态为

\[
    \frac{1}{\sqrt{n}} \sum_{j=0}^{n-1} \ket{x_0 + jr}.
\]

$x_0$ 几乎均匀产生并且未知，运用 $\mathbb{Z}_N$ 上的 $\op{QFT}$ 变换：

\[
    \frac{1}{\sqrt{nN}} \sum_{j=0}^{n-1} \sum_{k \in \mathbb{Z}_N} \omega_N^{k(x_0 + jr)} \ket{k} = \frac{1}{\sqrt{nN}} \sum_{k \in \mathbb{Z}_N} \omega_N^{kx_0} \sum_{j=0}^{n-1} \omega_N^{jkr} \ket{k}.
\]

如果运气很好，选择了满足 $r \mid N$ 的 $N$，那么无论 $x_0$ 是多少，$n = N/r$，且求和为

\[
    \sum_{j=0}^{n - 1} \omega_N^{jkr} = \sum_{j=0}^{n - 1} \omega_n^{jk} = n \delta_{k \bmod{n}, 0},
\]

对应的量子态为

\[
    \frac{n}{\sqrt{nN}} \sum_{k \in \mathbb{Z}_N} \omega_N^{kx_0} \delta_{k \bmod{n}, 0} \ket{k} = \frac{1}{\sqrt{r}} \sum_{k \in n\mathbb{Z}_N} \omega_N^{kx_0} \ket{k}.
\]

并且测量得到的 $k$ 都是 $n = N/r$ 的整数倍，每个倍数的概率均为 $1/r$. 

但更一般的情况下，对 $j$ 的求和实际上是一个几何级数

\[
    \sum_{j=0}^{n-1} \omega_N^{jkr} = \frac{\omega_N^{nkr} - 1}{\omega_N^{kr} - 1} = \omega_N^{(n-1)kr/2} = \omega_N^{(n-1)kr/2} \frac{\sin(\pi n kr / N)}{\sin(\pi kr / N)}.
\]

得到 $k$ 的概率即为

\[
    \op{Pr}(k) = \frac{1}{nN} \frac{\sin^2(\pi n kr / N)}{\sin^2(\pi kr / N)}.
\]

从 $n = N/r$ 的情况分析，期望这个分布强烈集中接近于 $N/r$ 的整数倍的 $k$ 值附近. 记 $\lfloor x \rceil$ 为最接近 $x$ 的整数，得到 $k = \lfloor jN/r \rceil = jN/r + \epsilon$ 的概率为

\[
    \op{Pr}(k = \lfloor jN/r \rceil) = \frac{1}{nN} \frac{\sin^2(\pi jn + \pi n r \epsilon / N)}{\sin^2(\pi j + \pi r \epsilon / N)} = \frac{1}{nN} \frac{\sin^2(\pi n r \epsilon / N)}{\sin^2(\pi r \epsilon / N)}.
\]

分析这个概率的下界，分母利用 $\sin^2 x \leq x^2$ 约束上界；而对于分子，观察到 $\lvert \varepsilon \rvert \leq 1/2$，且 $rn/N \leq 1 + O(1/n)$，所以有 $\lvert \pi n r \epsilon / N \rvert \leq \pi/2 + O(1/n)$，因此存在一个常数 $c > 0$ 使得 $\sin^2(\pi n r \epsilon / N) \geq c(\pi n r \epsilon / N)^2$，当 $n$ 较大时，可以选择 $c = 4/\pi^2$. 因此有

\[
    \op{Pr}(k = \lfloor jN/r \rceil) \geq \frac{1}{nN} \frac{c(\pi n r \epsilon / N)^2}{(\pi r \epsilon / N)^2} = \frac{c n}{N} \approx \frac{c}{r}.
\]

该下界表明 Fourier 采样以不低于某个常数的概率产生一个 $k$ 值，该值是最接近 $N/r$ 的 $r$ 个整数倍之一的整数.

最后就是利用 $\lfloor j r / N \rceil$ 来恢复 $r$，可以通过除以 $N$ 产生一个与 $j/r$ 相差不超过 $1/2N$ 的有理近似，然后利用连分数展开：

\[
    \frac{\lfloor j r / N \rceil}{N} = \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}}.
\]

在有限项截断后得到该展开的一个渐进分数. 具体参照 [Quantum-Quantum Computation and Quantum Information-Appendix](https://note.shad0wash.cc/quantum/QCQI/Appendix/#continued-fractions). 而任意满足

\[
    \left\lvert \frac{p}{q} - \frac{\lfloor j r / N \rceil}{N} \right\rvert < \frac{1}{2q^2}
\]

的分数 $p/q$ 都是 $\lfloor j r / N \rceil / N$ 的某个渐进分数，且 $j/r$ 与 $\lfloor j r / N \rceil / N$ 的距离不超过 $1/2N$，所以只要 $r^2 < N$，就能确保 $j/r$ 是某个渐进分数. 通过取足够大的 $N$，便提供了一个高效恢复周期 $r$ 的方法.

## Period finding over the reals

现在讨论函数 $f: \mathbb{R} \to S$，其满足 $f(x) = f(x + r), r \in \mathbb{R}$. 假定 $f$ 在每个最小周期内都是单射，接下来调整 Shor 算法过程来得到 $r$ 的近似值，即使其是无理数. 为了进行周期寻找离散化是必要的，但是不恰当的离散化可能会完全破坏周期性结构. 为此需要先定义**伪周期**（pseudoperiodic）. 称函数 $f: \mathbb{Z} \to S$ 在 $k \in \mathbb{Z}$ 处是伪周期的，且周期为 $r \in \mathbb{R}$，如果对于任意整数 $l \in \mathbb{Z}$，都有 $f(k) = f(k + \lfloor l r \rceil)$ 或 $f(k) = f(k + \lceil l r \rceil)$. 称 $f$ 是 **$\varepsilon$-伪周期**的，如果 $f$ 在 $k = 0, 1, \ldots, \lfloor r \rfloor$ 中至少 $\varepsilon$ 比例的点处是伪周期的. 假定存在常数 $\varepsilon$ 使得 $f$ 是 $\varepsilon$-伪周期的，并且在伪周期的输入点上 $f$ 是单射的. 

现在考虑对伪周期函数施加 Fourier 采样. 依然在 $\mathbb{Z}_N$ 上均匀叠加态计算函数：

\[
    \sum_{x=0}^{N-1} \ket{x} \mapsto \sum_{x=0}^{N-1} \ket{x, f(x)},
\]

测量第二个寄存器会以常数概率得到伪周期点，假设这个值为 $f(x_0)$，$0 \leq x_0 \leq r$. 和先前一样，若 $x_0 < N - r \lfloor N/r \rfloor$，则 $n = \lfloor N/r \rfloor + 1$，否则 $n = \lfloor N/r \rfloor$. 使用 $[\ell]$ 表示可能是 $\lfloor \ell \rfloor$ 或 $\lceil \ell \rceil$ 的整数，得到测量结果对应的态为

\[
    \frac{1}{\sqrt{n}} \sum_{j=0}^{n-1} \ket{x_0 + [j r]}.
\]

接下来施加 $\mathbb{Z}_N$ 上的 $\op{QFT}$ 变换：

\[
    \frac{1}{\sqrt{nN}} \sum_{j=0}^{n-1} \sum_{k \in \mathbb{Z}_N} \omega_N^{k(x_0 + [j r])} \ket{k} = \frac{1}{\sqrt{nN}} \sum_{k \in \mathbb{Z}_N} \omega_N^{k x_0} \sum_{j=0}^{n-1} \omega_N^{k [j r]} \ket{k}.
\]

而 $[j r] = j r + \delta_j$，其中 $-1 < \delta_j < 1$. 因此对 $j$ 的求和为

\[
    \sum_{j=0}^{n-1} \omega_N^{k [j r]} = \sum_{j=0}^{n-1} \omega_N^{k j r} \omega_N^{k \delta_j}. 
\]

显然如果不考虑 $\delta_j$ 项，就会退化成稍早分析过的几何级数，其归一化后为 $\Omega(1/\sqrt{r})$，因而很自然的期望这个求和和原先的几何级数接近. 具体地，考虑两者之差：

\begin{align*}
    \left\lvert \sum_{j=0}^{n-1} \omega_N^{k j r} \omega_N^{k \delta_j} - \sum_{j=0}^{n-1} \omega_N^{k j r} \right\rvert & \leq \sum_{j=0}^{n-1} \left\lvert \omega_N^{k j r} \right\rvert \cdot \left\lvert \omega_N^{k \delta_j} - 1 \right\rvert \\
    & = \sum_{j=0}^{n-1} \left\lvert \omega_N^{k \delta_j} - 1 \right\rvert \\
    & = 2 \sum_{j=0}^{n-1} \left\lvert \sin \frac{\pi k \delta_j}{N} \right\rvert \\
    & \leq 2 \sum_{j=0}^{n-1} \left\lvert \frac{\pi k \delta_j}{N} \right\rvert \\
    & \leq \frac{2 \pi n k}{N}.
\end{align*}

单纯考虑这个上界，振幅并非对所有 $k$ 都足够小. 但可以限制 $k$，如只考虑小于 $N / \log r$ 的 $k$ 值，获得的概率为 $1 / \log r$，这是一个多项式开销，可以接受. 在这种情况下，有

\begin{align*}
    \left\lvert \frac{1}{\sqrt{nN}} \sum_{j=0}^{n-1} \omega_N^{k [j r]} \right\rvert & = \Omega\left( \frac{1}{\sqrt{r}} \right) - O\left( \frac{1}{\sqrt{nN}} \cdot \frac{n}{\log r} \right) \\
    & = \Omega\left( \frac{1}{\sqrt{r}} \right) - O\left( \frac{1}{\sqrt{r} \log r} \right) \\
    & = \Omega\left( \frac{1}{\sqrt{r}} \right).
\end{align*}

因而 Fourier 采样仍然允许我们从一个 $k = \lfloor j N / r \rceil$ 以相当大的概率出现的分布中采样，不过这一概率现在为 $\Omega(1 / \op{poly} (\log r))$ 而非 $\Omega(1)$. 

最终便是使用 $k$ 去获取 $r$ 的近似值. 因为 $r$ 不是整数，Shor 算法中的技术不能直接使用，但可以执行足够多次 Fourier 采样，直到得到 $\lfloor j N / r \rceil$ 和 $\lfloor j' N / r \rceil$，其中 $j$ 和 $j'$ 互质，这同样只需要多项式开销. 下面证明，如果 $N \geq 3r^2$，那么 $j/j'$ 是 $\lfloor j N / r \rceil / \lfloor j' N / r \rceil$ 的某个渐进分数. 进而可以得到 $j$，进一步计算 $jr / \lfloor j N / r \rceil$，因为 $\lvert r - \lfloor j N / \lfloor j N / r \rceil \rceil \rvert \leq 1$，便可以得到 $r$ 的一个良好近似.

!!! success "Lemma"
    若 $N \geq 3r^2$，那么 $j/j'$ 是 $\lfloor j N / r \rceil / \lfloor j' N / r \rceil$ 的某个渐进分数，并且 $\lvert r - \lfloor j N / \lfloor j N / r \rceil \rceil \rvert \leq 1$.

    ???+ success "Proof"
        关于渐进分数只需证明

        \[
            \left\lvert \frac{\lfloor j N / r \rceil}{\lfloor j' N / r \rceil} - \frac{j}{j'} \right\rvert < \frac{1}{2 {j'}^2}.
        \]

        令 $\lfloor j N / r \rceil = j N / r + \mu$，$\lfloor j' N / r \rceil = j' N / r + \nu$，其中 $\lvert \mu \rvert, \lvert \nu \rvert \leq 1/2$. 所以有

        \begin{align*}
            \left\lvert \frac{\lfloor j N / r \rceil}{\lfloor j' N / r \rceil} - \frac{j}{j'} \right\rvert & = \left\lvert \frac{(j N / r + \mu) }{(j' N / r + \nu)} - \frac{j}{j'} \right\rvert \\
            & = \left\lvert \frac{j N + \mu r}{j' N + \nu r} - \frac{j}{j'} \right\rvert \\
            & = \left\lvert \frac{r(\mu j' - \nu j)}{(j' N + \nu r) j'} \right\rvert \\
            & \leq \frac{r(j + j')}{2 j'^2 N - j' r} \\
            & \leq \frac{r}{j' N - r/2}
        \end{align*}

        最后一步不失一般性地假设 $j \leq j'$. 因为 $j' < r$，而 $N \geq 3 r^2$，所以 $j' N \geq r/2 + 2 j'^2 r$，上式被 $\frac{1}{2 j'^2}$ 所约束.

        最终

        \begin{align*}
            r - \frac{j N}{\lfloor j N / r \rceil} & = r - \frac{j N}{j N / r + \mu} \\
                                                   & = r - \frac{j N r}{j N + \mu r} \\
                                                   & = \frac{r^2 \mu}{j N + \mu r}. 
        \end{align*}

        因为 $N \geq 3 r^2, \lvert \mu \rvert \leq 1/2, j \geq 1$，所以上式最多为 $1$.

## Other algorithms for number fields

Hallgren 关于 Pell 方程的原始论文还解决了主理想问题：整数分解可以规约到求解 Pell 方程，其又可以规约到主理想问题，但反向规约尚未可知. Buchmann 和 Williams 设计了一个基于主理想问题的密钥交换协议，Hallgren 的算法表明这是可以被量子计算机破解的.

Hallgren 以及 Schmidt 和 Vollmer 独立地发现了针对代数数论中问题的进一步相关算法，具体来说，他们找到了在常数次数数域中计算单位群和类群的多项式时间算法. 这些算法需要将 $\mathbb{R}$ 上的周期寻找问题推广到 $\mathbb{R}^d$ 上的类似问题. 最近，其中一些算法已被扩展到任意次数数域的情况.