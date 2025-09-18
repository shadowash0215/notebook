# How to Use a Short Basis: Trapdoors for Hard Lattices and New Cryptographic Constructions

## Preliminaries

### Lattices

设 $\mathbf{B} = \{\mathbf{b}_1, \ldots, \mathbf{b}_n\} \subset \mathbb{R}^n$ 由 $n$ 个线性无关向量组成，则基 $B$ 生成的 $n$ 维格 $\Lambda$ 定义为：

\[
    \Lambda = \mathcal{L}(\mathbf{B}) = \{\mathbf{Bc} = \sum_{i \in [n]} c_i \cdot \mathbf{b}_i \mid \mathbf{c} \in \mathbb{Z}^n \}.
\]

格 $\Lambda$ 的最小距离（the minimum distance） $\lambda_1{\Lambda}$ 指的是其中的最短非零向量的长度（默认为 $\mathcal{l}_2$ 范数）：$\lambda_1 (\Lambda) = \min_{0 \neq \mathbf{x} \in \Lambda} \lVert \mathbf{x} \rVert$. 而第 $i$ 个逐次最小距离（the $i$th successive minimum）$\lambda_i(\Lambda)$ 是 $\Lambda$ 中包含 $i$ 个线性无关且范数不超过 $r$ 的最小半径 $r$.

格是 $\mathbb{R}^n$ 中的一个离散加法子群，所以对于任意格 $\Lambda' \subseteq \Lambda$，商群 $\Lambda / \Lambda'$（也记作 $\Lambda \bmod \Lambda'$）是良定义的.

对任何线性无关向量组 $\mathbf{S} = \{\mathbf{s}_1, \ldots, \mathbf{s}_n\} \subseteq \mathbb{R}^n$，定义其 Gram-Schmidt 正交化为：$\tilde{\mathbf{S}} = \{\tilde{\mathbf{s}}_1, \ldots, \tilde{\mathbf{s}}_n\}$.

!!! success "Lemma"
    存在确定的多项式时间算法，其输入为 $n$ 维格 $\Lambda$ 的任意一组基 $\mathbf{B}$ 以及一个满秩格向量集合 $\mathbf{S} \subset \Lambda$，能够输出 $\Lambda$ 的一组基 $\mathbf{T}$，满足 $\forall i \in [n]$，$\lVert \tilde{\mathbf{t}}_i \rVert \leq \lVert \tilde{\mathbf{s}}_i \rVert$.

也就是说，格中任意满秩向量集都可以高效地转为格的一组基，并且不会增加其 Gram-Schmidt 正交化得到的向量的长度.

对偶格 $\Lambda^*$ 定义为：

\[
    \Lambda^* = \{\mathbf{x} \in \mathbb{R}^n \mid \forall \mathbf{v} \in \Lambda, \langle \mathbf{x}, \mathbf{v} \rangle \in \mathbb{Z} \}.
\]

如果 $\mathbf{B}$ 是 $\Lambda$ 的基，则对偶基 $\mathbf{B}^* = (\mathbf{B}^{-1})^\mathrm{T}$ 是 $\Lambda^*$ 的基.

!!! success "Lemma"
    设 $\{\mathbf{b}_1, \ldots, \mathbf{b}_n\}$ 是 $\Lambda$ 的基，而 $\{\mathbf{d}_1, \ldots, \mathbf{d}_n\}$ 是其对应的对偶基，但是逆序排列（即 $\mathbf{d}_i = \mathbf{b}_{n-i+1}^*$），则 $\forall i \in [n]$，$\tilde{\mathbf{d}}_i = \tilde{\mathbf{b}}_i/\lVert \tilde{\mathbf{b}}_i \rVert^2$. 特别地，$\lVert \tilde{\mathbf{d}}_i \rVert = 1/\lVert \tilde{\mathbf{b}}_i \rVert$.

$\gamma = \gamma(n)$ 是随维度变化的近似因子.

!!! info "Definition"
    - (Shortest Vector Problem (Decision Version)) $\mathsf{GapSVP}_\gamma$ 的输入是一个 $n$ 维满秩格的基 $\mathbf{B}$，如果 $\lambda_1(\mathcal{L}(\mathbf{B})) \leq 1$，输出 $1$；如果 $\lambda_1(\mathcal{L}(\mathbf{B})) \geq \gamma(n)$，输出 $0$.

    - (Shortest Independent Vectors Problem) $\mathsf{SIVP}_\gamma$ 的输入是一个 $n$ 维满秩格的基 $\mathbf{B}$，目标是输出一个 $n$ 个元素的线性无关向量集合 $\mathbf{S} \subseteq \mathcal{L}(\mathbf{B})$，使得 $\lVert \mathbf{S} \rVert \leq \gamma(n) \cdot \lambda_n(\mathcal{L}(\mathbf{B}))$.

### Gaussians on Lattices

对任意 $s > 0$，定义 Gaussian 函数为：

\[
    \forall \mathbf{x} \in \mathbb{R}^n, \quad \rho_{s, \mathbf{c}} = \exp{(-\pi \lVert \mathbf{x} - \mathbf{c} \rVert^2 / s^2)}.
\]

其中 $\mathbf{c}$ 表示高斯函数的中心. 当下标省略时，默认 $\mathbf{c} = \mathbf{0}, s = 1$.

而对于任意 $\mathbf{c} \in \mathbb{R}^n, s > 0$，以及 $n$ 维格 $\Lambda$，定义 $\Lambda$ 上的离散高斯分布为：

\[
    \forall \mathbf{x} \in \Lambda, D_{\Lambda, s, \mathbf{c}}(\mathbf{x}) = \frac{\rho_{s, \mathbf{c}}(\mathbf{x})}{\rho_{s, \mathbf{c}}(\Lambda)}.
\]

其中分母 $\rho_{s, \mathbf{c}}(\Lambda) = \sum_{\mathbf{x} \in \Lambda} \rho_{s, \mathbf{c}}(\mathbf{x})$ 是归一化常数.

!!! info "Definition"
    对 $n$ 维格以及正实数 $\varepsilon > 0$，平滑参数 $\eta_\varepsilon(\Lambda)$ 指的是满足

    \[
        \rho_{1/s} (\Lambda^*\\ \{0\}) \leq \varepsilon
    \]

    的最小正实数 $s$. 

以下是 $\mathcal{l}_\infty$ 范数下的平滑参数的约束，其将格的平滑参数与其对偶格的最小距离联系起来.

!!! success "Lemma"
    对任意 $n$ 维格 $\Lambda$，以及正实数 $\varepsilon > 0$，

    \[
        \eta_\varepsilon(\Lambda) \leq \dfrac{\sqrt{\log{(2n/(1 + 1/\varepsilon))}/\pi}}{\lambda_1^\infty(\Lambda^*)}
    \]

    所以对于任意 $\omega(\sqrt{\log{n}})$ 函数，总存在可忽略量 $\varepsilon(n)$，使得 $\eta_{\varepsilon(n)}(\Lambda) \leq \omega(\sqrt{\log{n}})/\lambda_1^\infty(\Lambda^*)$.

!!! success "Lemma"
    设 $\Lambda$ 为 $n$ 维格，那么对任意 $\varepsilon \in (0, 1)$，$s > \eta_\varepsilon(\Lambda)$，以及 $\mathbf{c} \in \mathbb{R}^n$，都有

    \[
        \rho_{s, \mathbf{c}}(\Lambda) \in [\frac{1 - \varepsilon}{1 + \varepsilon}, 1] \cdot \rho_{s}(\Lambda).
    \]

这表明当 Gaussian 参数 $s$ 足够大时超过格的平滑参数时，格任意平移的总高斯分布实际上是一致的.

此外，如果 $s > \eta_\varepsilon(\Lambda')$，其中 $\Lambda'$ 是 $\Lambda$ 的子格，那么 $\Lambda$ 上的高斯分布在模去 $\Lambda'$ 后是近似均匀分布的.

!!! success "Corollary"
    设 $\Lambda, \Lambda'$ 是 $n$ 维格，且 $\Lambda' \subset \Lambda$，那么对于任意 $\varepsilon \in (0, \frac{1}{2})$，任意 $s > \eta_\varepsilon(\Lambda')$，以及 $\mathbf{c} \in \mathbb{R}^n$，分布 $D_{\Lambda, s, \mathbf{c}} \bmod \Lambda'$ 与 $\Lambda \bmod \Lambda'$ 上的均匀分布之间的距离不超过 $2\varepsilon$.

    ???+ success "Proof"
        考虑 $\mathbf{z} \bmod \Lambda'$ 上的边际分布，其中 $\mathbf{z} \from D_{\Lambda, s, \mathbf{c}}$，那么对任意陪集 $\mathbf{v} + \Lambda' \in \Lambda / \Lambda'$，$\mathbf{z} \in \mathbf{v} + \Lambda'$ 的概率与如下的值成比例：

        \[
            \rho_{s, \mathbf{c}}(\mathbf{v} + \Lambda') = \rho_{s, \mathbf{c} - \mathbf{v}}(\Lambda') \in [\frac{1 - \varepsilon}{1 + \varepsilon}, 1] \cdot \rho_{s}(\Lambda').
        \]

!!! success "Lemma"
    对任意 $n$ 维格 $\Lambda$，$\mathbf{c} \in \op{span}(\Lambda)$，正实数 $\varepsilon \in (0, 1)$，以及 $s > \eta_\varepsilon(\Lambda)$，都有

    \[
        \op{Pr}_{\mathbf{x} \sim D_{\Lambda, s, \mathbf{c}}}[\lVert \mathbf{x} - \mathbf{c} \rVert > s\sqrt{n}] \leq \frac{1+\varepsilon}{1 - \varepsilon} \cdot 2^{-n}.
    \]

这个引理表明从参数为 $s$ 的离散高斯分布中采样的向量 $\mathbf{x}$，其与高斯函数中心 $\mathbf{c}$ 的距离不会超过 $s\sqrt{n}$.

!!! success "Lemma"
    对任意 $n$ 维格 $\Lambda$，中心 $\mathbf{c} \in \mathbb{R}^n$，正实数 $\varepsilon > 0$，$s > 2\eta_\varepsilon(\Lambda)$，那么对于任意 $\mathbf{x} \in \Lambda$，都有

    \[
        D_{\Lambda, s, \mathbf{c}}(\mathbf{x}) \leq \frac{1 + \varepsilon}{1 - \varepsilon} \cdot 2^{-n}.
    \]

    当 $\varepsilon < \frac{1}{3}$ 时，$D_{\Lambda, s, \mathbf{c}}$ 的最小熵至少为 $n - 1$.

### Learning with Errors

对 $x \in \mathbb{R}$，$\lfloor x \rceil = \lfloor x + 1/2 \rfloor$ 指距离 $x$ 最近的整数. 记 $\mathbb{T} = \mathbb{R} / \mathbb{Z}$ 为模 $1$ 加法下的实数群，元素为 $[0, 1)$ 的实数.

- **Probability distributions** 均值为 $0$，方差为 $\sigma^2$ 的正态（高斯）分布是实数集 $\mathbb{R}$ 上的概率分布，密度函数为 $\frac{1}{\sigma \cdot \sqrt{2\pi}} \exp{(-x^2/2\sigma^2)}$. 两个独立的均值为 $0$，方差分别为 $\sigma_1^2$，$\sigma_2^2$ 的正态分布变量的和满足均值为 $0$，方差为 $\sigma_1^2 + \sigma_2^2$ 的正态分布. 尾不等式则是对于方差为 $\sigma^2$ 的正态分布变量，其值偏离均值 $t$ 个标准差 $t \cdot \sigma$ 的概率至多为 $\frac{1}{t} \exp{(-\frac{t^2}{2})}$.

    对 $\alpha \in \mathbb{R}^+$，$\Psi_\alpha$ 定义为 $\mathbb{T}$ 上的分布，其由均值为 $0$，标准差为 $\alpha/\sqrt{2\pi}$ 的正态分布模 $1$ 得到. 而对于 $\mathbb{T}$ 上的任意概率分布 $\phi$ 和正整数 $q \in \mathbb{Z}^+$，其离散化分布 $\bar{\phi}$ 是定义在 $\mathbb{Z}_q$ 上的离散分布，对应随机变量为 $\lfloor q \cdot X_\psi \rceil \bmod q$，其中 $X_\phi$ 满足分布 $\phi$.

    对整数 $q \geq 2$，$\mathbb{Z}_q$ 上的概率分布 $\chi$，维度 $n \in \mathbb{Z}^+$ 以及向量 $\mathbf{s} \in \mathbb{Z}_q^n$，定义 $A_{\mathbf{s}, \chi}$ 为 $\mathbb{Z}_q^n \times \mathbb{Z}_q$ 上的分布，对应随机变量 $(\mathbf{a}, \mathbf{a}^\mathrm{T} \mathbf{s} + x)$，其中 $\mathbf{a} \from \mathbb{Z}_q$ 是均匀随机向量，$x \from \chi$ 是独立随机变量，所有运算在 $\mathbb{Z}_q$ 下进行.

- **Learning with errors** 对于整数 $q = q(n)$ 和定义在 $\mathbb{Z}_q$ 上的分布 $\chi$，带误差学习问题 $\mathsf{LWE}_{q ,\chi}$ 的目标是借助 Oracle 以不可忽略的概率区分以下两种分布：

    1. $A_{\mathbf{s}, \chi}$，其中 $\mathbf{s} \from \mathbb{Z}_q^n$ 是均匀随机向量.

    2. $\mathbb{Z}_q^n \times \mathbb{Z}_q$ 上的均匀分布.


    换而言之，如果 $\mathbf{LWE}$ 是困难的，那么 $A_{\mathbf{s}, \chi}$ 就是一个伪随机分布.

!!! note "Proposition"
    设 $\alpha = \alpha(n) \in (0 ,1)$，并且 $q = q(n)$ 是一个满足 $\alpha \cdot q > 2 \sqrt{n}$ 的素数. 如果存在能够高效解决 $\mathsf{LWE}_{q, \bar{\Psi}_\alpha}$ 的算法，那么存在量子算法，最坏情况下能够以 $\tilde{O}(n/\alpha)$ 的近似因子，在 $\mathcal{l}_2$ 范数下逼近 $\mathsf{SIVP}$ 和 $\mathsf{GapSVP}$ 问题.

该结果后续被扩展至任意 $\mathcal{l}_p$ 范数，$2 \leq p \leq \infty$，并且保持近似因子为 $\tilde{O}(n/\alpha)$.

## New Smoothing Parameter Bound

对格 $\Lambda$ 定义 Gram-Shmidt 最小距离为：

\[
    \tilde{bl}(\Lambda) = \min_{\mathbf{B}} \lVert \tilde{\mathbf{B}} \rVert = \min_{\mathbf{B}} \max_{i \in [n]} \lVert \tilde{\mathbf{b}}_i \rVert.
\]

因为此前定理证明了对于任意满秩集合 $S \subset \Lambda$，都存在基 $\mathbf{T}$，使得 $\lVert \tilde{\mathbf{T}} \rVert \leq \lVert \tilde{\mathbf{S}} \rVert \leq \lVert \mathbf{S} \rVert$，所以只限制在基上也是良定的.

!!! success "Lemma"
    对任意 $n$ 维格 $\Lambda$ 和实数 $\varepsilon > 0$，有：

    \[
        \eta_{\varepsilon}(\Lambda) \leq \tilde{bl}(\Lambda) \cdot \sqrt{\frac{\log{(2n/(1 + 1/\varepsilon))}}{\pi}}.
    \]

    所以对于任意 $\omega(\sqrt{\log{n}})$ 函数，总存在可忽略量 $\varepsilon(n)$，使得 $\eta_{\varepsilon(n)}(\Lambda) \leq \tilde{bl}(\Lambda) \cdot \omega(\sqrt{\log{n}})$.

!!! success "Lemma"
    对任意 $n$ 维格 $\Lambda$，

    \[
        \lambda_1(\Lambda) \leq \tilde{bl}(\Lambda) \leq \lambda_n(\Lambda) \leq 2 \mu(\Lambda) \leq \sqrt{n} \cdot \tilde{bl}(\Lambda).
    \]

    其中 $\mu(\Lambda)$ 是 $\Lambda$ 的覆盖半径. 此外，最后一个不等式在常数因子意义下是紧的，即存在格族 $\{\Lambda_n\}_{n \in N}$ 使得 $\Lambda_n$ 是 $n$ 维格，并且 $\lambda_n(\Lambda_n) \geq \Omega(\sqrt{n}) \cdot \tilde{bl}(\Lambda_n)$.

## Sampling from Discrete Gaussians

接下来将展示如何使用任意的基 $\mathbf{B}$ 来从满足 $s > \lVert \tilde{\mathbf{B}} \rVert$ 的离散高斯分布 $D_{\Lambda, s, \mathbf{c}}$ 中高效采样.

!!! note "Theorem"
    存在概率多项式算法，输入为 $n$ 维格 $\Lambda$ 的基 $\mathbf{B}$，正实数 $s > \lVert \tilde{\mathbf{B}} \rVert \cdot \omega(\sqrt{\log{n}})$，以及中心 $\mathbf{c} \in \mathbb{R}^n$，可以从一个与 $D_{\Lambda, s, \mathbf{c}}$ 统计接近的分布中输出一个样本.

### Sampling Integers

首先定义 $\mathsf{Sample}\mathbb{Z}$，其从一维格 $\mathbb{Z}$ 上的离散高斯分布 $D_{\mathbb{Z}, s, c}$ 中采样整数. 设 $t(n) > \omega(\sqrt{\log{n}})$，为某个固定的函数，如 $t(n) = \log{n}$. $\mathsf{Sample}\mathbb{Z}$ 使用的是拒绝采样算法，具体来说，输入 $(s, c)$，算法从 $Z = \mathbb{Z} \cap [c - s \cdot t(n), c + s \cdot t(n)]$ 中均匀随机采样一个整数 $x$，然后以 $\rho_s(x - c) \in (0, 1]$ 的概率输出 $x$，否则重复采样.

$\mathsf{Sample}\mathbb{Z}$ 的正确性依赖于 $D_{\mathbb{Z}, s, c}$ 的尾不等式.

!!! success "Lemma"
    对任意 $\varepsilon > 0$，$s \geq \eta_\varepsilon(\mathbb{Z})$，以及 $t > 0$，都有

    \[
        \op{Pr}_{x \sim D_{\mathbb{Z}, s, c}}[\lvert x - c \rvert > s \cdot t] \leq 2e^{-\pi t^2} \cdot \frac{1 + \varepsilon}{1 - \varepsilon}.
    \]

    特别地，当 $\varepsilon \in (0, \frac{1}{2})$，$t > \omega(\sqrt{\log{n}})$ 时，$\lvert x - c \rvert \geq s \cdot t$ 的概率是可忽略的.

    ???+ success "Proof"
        设 $\mathcal{B} = (-1, 1) \subset R$ 为一维单位开球，首先有如下的不等式：

        \[
            \rho_s((\mathbb{Z} - c) \setminus t \cdot s \cdot \mathcal{B}) \leq 2 e^{-\pi t^2} \cdot \rho_s(\mathbb{Z}).
        \]

        接下来考虑 $D_{\mathbb{Z}, s, c}$ 中所有落在 $t \cdot s \cdot (\mathcal{B} + c)$ 外的点的总概率：

        \[
            D_{\mathbb{Z}, s, c}(\mathbb{Z} \setminus (t \cdot s \cdot (\mathcal{B} + c))) = \frac{\rho_s((\mathbb{Z} - c) \setminus t \cdot s \cdot \mathcal{B})}{\rho_{s, c}(\mathbb{Z})} \leq \frac{2 e^{-\pi t^2} \cdot \rho_s(\mathbb{Z})}{\rho_{s, c}(\mathbb{Z})} \leq \frac{2 e^{-\pi t^2} \cdot \rho_s(\mathbb{Z})}{\frac{1 - \varepsilon}{1 + \varepsilon} \cdot \rho_s(\mathbb{Z})}.
        \]

        得证.

!!! success "Lemma"
    对任意 $0 < \varepsilon < \exp{-\pi}$，$s \geq \eta_\varepsilon(\mathbb{Z})$，以及任意 $\omega(\log{n})$ 函数，$\mathsf{Sample}\mathbb{Z}$ 会以极大的概率在 $t(n) \cdot \omega(\log{n})$ 轮迭代中终止，并且输出一个与 $D_{\mathbb{Z}, s, c}$ 统计接近的分布.（注意迭代次数与 Gaussian 参数 $s$ 无关）

    ???+ success "Proof"
        首先定义 $\mathbb{Z}$ 上的一个概率分布 $D$，其中 $D(x)$ 正比于 $\rho_s(x - c), \forall x \in Z$，否则 $D(x) = 0$. 而 $\mathsf{Sample}\mathbb{Z}$ 的输出分布就是 $D$，并且根据上一引理，$D$ 和 $D_{\mathbb{Z}, s, c}$ 之间的距离是可忽略的.

        接下来分析运行时间.