# Verifiable Quantum Advantage without Structure

## Preliminaries

对于随机变量 $X, X'$，$\Delta(X, X')$ 表示它们之间的统计距离. 

对于随机变量 $X$，$H_\infty(X)$ 表示它的最小熵（min-entropy），其定义为 $H_\infty(X) = -\log \max_x \Pr[X=x]$.

对于随机经典算法 $\mathcal{A}$，$y \gets \mathcal{A}(x; r)$ 表示算法 $\mathcal{A}$ 以 $x$ 为输入，使用随机数 $r$ 作为内部随机源，输出 $y$. 

对于未必归一的量子态 $\ket{\psi}, \ket{\phi}$，以及 $\varepsilon \geq 0$，$\ket{\psi} \approx_\varepsilon \ket{\phi}$ 表示 $\lVert \ket{\psi} - \ket{\phi} \rVert \leq \varepsilon$. 简写 $\ket{\psi} \approx \ket{\phi}$ 表示 $\lVert \ket{\psi} - \ket{\phi} \rVert \leq \op{negl}(\lambda)$.

对于未必归一的量子态 $\ket{\psi}, \ket{\phi}$，$\ket{\psi} \propto \ket{\phi}$ 表示 $\ket{\psi} = c \ket{\phi}$，其中 $c \in \mathbb{C} \setminus \{0\}$.

### Finite Fields

对于 $q = p^r$，其中 $p$ 是素数，$\mathbb{F}_q$ 表示阶为 $q$ 的有限域. 对于 $\mathbf{x} = (x_1, \ldots, x_n) \in \mathbb{F}_q^n$，$\mathbf{y} = (y_1, \ldots, y_n) \in \mathbb{F}_q^n$，定义 $\mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n x_i y_i$.

考虑字母表 $\sigma = \mathbb{F}_q^m$，以及 $\mathbf{x} = (\mathbf{x}_1, \ldots, \mathbf{x}_n) \in \sigma^n$，$\mathbf{y} = (\mathbf{y}_1, \ldots, \mathbf{y}_n) \in \sigma^n$，定义 $\mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n \mathbf{x}_i \cdot \mathbf{y}_i$.

迹函数 $\op{Tr}: \mathbb{F}_q \to \mathbb{F}_p$ 定义为

\[
    \op{Tr}(x) = \sum_{i=0}^{r-1} x^{p^i}.
\]

迹函数是 $\mathbb{F}_p$-线性的，即对于任何 $a, b \in \mathbb{F}_p$ 和 $x, y \in \mathbb{F}_q$，有

\[
    \op{Tr}(ax + by) = a \op{Tr}(x) + b \op{Tr}(y).
\]

令 $\omega_p = e^{2\pi i / p}$，对于任何 $\mathbf{x} \in \mathbb{F}_q^n \setminus \{\mathbf{0}\}$，有

\[
    \sum_{\mathbf{y} \in \mathbb{F}_q^n} \omega_p^{\op{Tr}(\mathbf{x} \cdot \mathbf{y})} = 0.
\]

$\mathbb{F}_q$ 的乘法群 $\mathbb{F}_q^*$ 是循环群. 因此存在一个本原元 $\gamma \in \mathbb{F}_q^*$，使得

\[
    \{\gamma^i\}_{i \in [q - 1]} = \mathbb{F}_q^*.
\]

对 $\mathbf{x} \in \mathbb{F}_q^n$，定义 $\mathsf{hw}(\mathbf{x}) = \lvert \{i \in [n] : x_i \neq 0\} \rvert$，即 $\mathbf{x}$ 的 Hamming 重量. 

对于 $\mathbf{x} \in \mathbb{F}_q^n$ 和子集 $S \subseteq [n]$，定义 $\mathbf{x}_S$ 为 $(x_i)_{i \in S}$，即 $\mathbf{x}$ 在 $S$ 上的投影.

### Quantum Fourier Transform over Finite Fields

在基于有限域 $\mathbb{F}_q$ 的量子系统上，量子 Fourier 变换（Quantum Fourier Transform, QFT）为使用 $\op{QFT}_{\mathbb{F}_q}$ 表示的酉算子，对于 $x \in \mathbb{F}_q$，有


\[
    \op{QFT}_{\mathbb{F}_q} \ket{x} = \frac{1}{\sqrt{q}} \sum_{z \in \mathbb{F}_q} \omega_p^{\op{Tr}(x \cdot z)} \ket{z}.
\]

考虑基于字母表 $\Sigma = \mathbb{F}_q^m$ 的量子系统，定义其上的 QFT 为 $\op{QFT}_{\Sigma} = \op{QFT}_{\mathbb{F}_q}^{\otimes m}$. 对于 $\mathbf{x} = (x_1, \ldots, x_m) \in \Sigma$，有

\begin{align*}
    \op{QFT}_\Sigma \ket{\mathbf{x}} &= \op{QFT}_{\mathbb{F}_q}^{\otimes m} \ket{x_1} \otimes \cdots \otimes \ket{x_m} \\
    &= \frac{1}{\sqrt{\lvert \Sigma \rvert}} \sum_{\mathbf{z} \in \Sigma} \omega_p^{\op{Tr}(\mathbf{x} \cdot \mathbf{z})} \ket{\mathbf{z}}.
\end{align*}

类似地，对于任何正整数 $n$ 和 $\mathbf{x} \in \Sigma^n$，有

\[
    \op{QFT}_\Sigma^{\otimes n} \ket{\mathbf{x}} = \frac{1}{\lvert \Sigma \rvert^{n/2}} \sum_{\mathbf{z} \in \Sigma^n} \omega_p^{\op{Tr}(\mathbf{x} \cdot \mathbf{z})} \ket{\mathbf{z}}.
\]

对于函数 $f: \Sigma^n \to \mathbb{C}$，定义其 Fourier 变换为

\[
    \hat{f}(\mathbf{z}) = \frac{1}{\lvert \Sigma \rvert^{n/2}} \sum_{\mathbf{x} \in \Sigma^n} f(\mathbf{x}) \omega_p^{\op{Tr}(\mathbf{x} \cdot \mathbf{z})}.
\]

从而有

\[
    \op{QFT}_\Sigma^{\otimes n} \sum_{\mathbf{x} \in \Sigma^n} f(\mathbf{x}) \ket{\mathbf{x}} = \sum_{\mathbf{z} \in \Sigma^n} \hat{f}(\mathbf{z}) \ket{\mathbf{z}}.
\]

对于函数 $f: \Sigma^n \to \mathbb{C}$ 和 $g: \Sigma^n \to \mathbb{C}$，定义它们的逐点乘积和卷积为

\begin{align*}
    (f \cdot g)(\mathbf{x}) &= f(\mathbf{x}) \cdot g(\mathbf{x}), \\
    (f * g)(\mathbf{x}) &= \sum_{\mathbf{y} \in \Sigma^n} f(\mathbf{y}) g(\mathbf{x} - \mathbf{y}).
\end{align*}

!!! success "Lemma(Parseval's equality)"
    对任意函数 $f: \Sigma^n \to \mathbb{C}$，

    \[
        \sum_{\mathbf{x} \in \Sigma^n} \lvert f(\mathbf{x}) \rvert^2 = \sum_{\mathbf{z} \in \Sigma^n} \lvert \hat{f}(\mathbf{z}) \rvert^2.
    \]

!!! success "Lemma"
    对于 $i \in [n]$，有 $f_i: \Sigma \to \mathbb{C}$，定义 $f: \Sigma^n \to \mathbb{C}$ 为

    \[
        f(\mathbf{x}) = \prod_{i \in [n]} f_i(\mathbf{x}_i),
    \]

    其中 $\mathbf{x} = (\mathbf{x}_1, \ldots, \mathbf{x}_n) \in \Sigma^n$. 则有

    \[
        \hat{f}(\mathbf{z}) = \prod_{i \in [n]} \hat{f}_i(\mathbf{z}_i),
    \]

    其中 $\mathbf{z} = (\mathbf{z}_1, \ldots, \mathbf{z}_n)$.

!!! success "Lemma(Convolution theorem)"
    对任意函数 $f, g, h: \Sigma^n \to \mathbb{C}$，有

    \begin{align*}
        \widehat{f \cdot g} &= \frac{1}{\lvert \Sigma \rvert^{n/2}} (\hat{f} * \hat{g}), \\
        \widehat{f * g} &= \lvert \Sigma \rvert^{n/2} (\hat{f} \cdot \hat{g}), \\
        \widehat{f \cdot (g * h)} &= \hat{f} * (\hat{g} \cdot \hat{h}).
    \end{align*}

### Other Lemmas

!!! success "Lemma(Chernoff bound)"
    设 $X_1, \ldots, X_n$ 为取值于 $\{0, 1\}$ 的独立随机变量，$X := \sum_{i \in [n]} X_i$，$\mu := \mathbb{E}[X]$. 则对于任意 $\delta \geq 0$，有

    \[
        \Pr[X \geq (1 + \delta) \mu] \leq e^{-\frac{\delta^2  \mu}{2 + \delta} }.
    \]

!!! success "Lemma"
    对于任何经典比特串集合 $\mathcal{X}$ 和 $\mathcal{Y}$，以及进行 $q$ 次量子查询的算法 $\mathcal{A}$，有

    \[
        \Pr{\mathcal{A}^\mathcal{H} = 1: H \xleftarrow{\$} \mathsf{Func}(\mathcal{X}, \mathcal{Y})} = \Pr{\mathcal{A}^H = 1: H \xleftarrow{\$} \mathcal{F} },
    \]

    其中 $\mathcal{F}$ 为 $\mathcal{X}$ 到 $\mathcal{Y}$ 的 $2 q$-wise independent 哈希函数族.

## Cryptographic Definitions In The Random Oracle Model

- **经典随机谕示机模型（Classical Random Oracle Model, CROM）**：在该模型中，会选择一个均匀随机函数 $H: \{0, 1\}^n \to \{0, 1\}^m$，其中 $n = n(\lambda)$ 和 $m = m(\lambda)$ 均是关于安全参数 $\lambda$ 的多项式函数，并且允许敌手对 $H$ 进行经典查询. 除非另有说明，否则认为 $H$ 产生的概率是从 $\{0, 1\}^n$ 到 $\{0, 1\}^m$ 的函数集合中均匀随机选择的. CROM 中的敌手通常称为均匀经典敌手.
- **量子随机谕示机模型（Quantum Random Oracle Model, QROM）**：该模型与 CROM 类似，但允许敌手对随机函数 $H$ 进行量子查询. 即系统提供了一个应用酉变换 $\ket{x}\ket{y} \mapsto \ket{x}\ket{y \oplus H(x)}$ 的量子谕示机. QROM 中的敌手通常称为均匀量子敌手.
- **带有辅助输入的经典随机谕示机模型（Classical Random Oracle Model with Auxiliary Input, AI-CROM）**：该模型与 CROM 类似，但允许敌手获取依赖于该随机谕示机的、多项式大小的经典辅助信息. AI-CROM 中的敌手通常称为非均匀经典敌手.
- **带有（经典）辅助输入的量子随机谕示机模型（Quantum Random Oracle Model with (Classical) Auxiliary Input, AI-QROM）**：该模型与 QROM 类似，但允许敌手获取依赖于该随机谕示机的、多项式大小的经典辅助信息. AI-QROM 中的敌手通常称为非均匀量子敌手.

!!! info "Definition(Family of Oracle-aided Functions)"
    对于函数 $l_\mathsf{key} = l_\mathsf{key}(\lambda)$，$l_\mathsf{in} = l_\mathsf{in}(\lambda)$ 和 $l_\mathsf{out} = l_\mathsf{out}(\lambda)$，一族关于谕示机 $H: \{0, 1\}^n \to \{0, 1\}^m$ 的可高效计算的带有谕示机辅助的有密钥函数族 $\{f_\lambda: \{0, 1\}^{l_\mathsf{key} } \times \{0, 1\}^{l_\mathsf{in}} \to \{0, 1\}^{l_\mathsf{out}}\}_{\lambda \in \mathbb{N}}$ 是指一族可以通过（确定性）多项式时间经典机器并借助对谕示机 $H$ 的访问来实现的函数族 $f_\lambda$. 如果 $l_\mathsf{key} = 0$，则称该函数族为无密钥函数族. 默认认为是无密钥函数族，除非另有说明. $f_\lambda^H$ 表示关于谕示机 $H$ 的函数族 $f_\lambda$.

*单向函数*：现在定义带有谕示机辅助的函数对于随机谕示机呈单向性的含义. 仅考虑无密钥函数，因为无密钥和有密钥的单向函数在表达能力上是等价的.

!!! info "Definition(One-way Functions with Random Oracles)"
    称一族关于谕示机 $H: \{0, 1\}^n \to \{0, 1\}^m$ 的可高效计算的带有谕示机辅助的无密钥函数族 $\{f_\lambda: \{0, 1\}^{l_\mathsf{in}} \to \{0, 1\}^{l_\mathsf{out}}\}_{\lambda \in \mathbb{N}}$ 在 CROM（resp., QROM）中是单向的，如果对于所有向 $H$ 进行 $\op{poly}(\lambda)$ 次经典（resp., 量子）查询的计算无界敌手 $\mathcal{A}$，存在可忽略函数 $\op{negl}$，使得

    \[
        \op{Pr}_H[y = f_\lambda^H(x'): x \xleftarrow{\$} \{0, 1\}^{l_\mathsf{in}}, y = f_\lambda^H(x), x' \xleftarrow{\$} \mathcal{A}^{H}(1^\lambda, y)] \leq \op{negl}(\lambda).
    \]

    称 $\{f_\lambda: \{0, 1\}^{l_\mathsf{in}} \to \{0, 1\}^{l_\mathsf{out}}\}_{\lambda \in \mathbb{N}}$ 在 AI-CROM（resp., AI-QROM）中是单向的，如果对于所有向 $H$ 进行 $\op{poly}(\lambda)$ 次经典（resp., 量子）查询的计算无界敌手 $\mathcal{A}$，存在可忽略函数 $\op{negl}$，使得

    \[
        \op{Pr}_H[y = f_\lambda^H(x'): x \xleftarrow{\$} \{0, 1\}^{l_\mathsf{in}}, y = f_\lambda^H(x), x' \xleftarrow{\$} \mathcal{A}^{H}(a(H), 1^\lambda, y)] \leq \op{negl}(\lambda),
    \]

*碰撞抗性*：现在定义碰撞哈希.

!!! info "Definition(Collision-resistance with Random Oracles)"
    称一族关于谕示机 $H: \{0, 1\}^n \to \{0, 1\}^m$ 的可高效计算的带有谕示机辅助的有密钥函数族 $\{f_\lambda: \{0, 1\}^{l_\mathsf{key}} \times \{0, 1\}^{l_\mathsf{in}} \to \{0, 1\}^{l_\mathsf{out}}\}_{\lambda \in \mathbb{N}}$ 在 CROM（resp., QROM）中是碰撞抗性的，如果对于所有向 $H$ 进行 $\op{poly}(\lambda)$ 次经典（resp., 量子）查询的计算无界敌手 $\mathcal{A}$，存在可忽略函数 $\op{negl}$，使得

    \[
        \op{Pr}_H[f_\lambda^H(k, x_0) = f_\lambda^H(k, x_1) \wedge x_0 \neq x_1: k \xleftarrow{\$} \{0, 1\}^{l_\mathsf{key}}, (x_0, x_1) \xleftarrow{\$} \mathcal{A}^{H}(k)] \leq \op{negl}(\lambda).
    \]

    AI-CROM 和 AI-QROM 中的碰撞抗性可以类似地定义.

无密钥哈希函数不能抵御非均匀敌手，因为具体的碰撞信息可能被硬编码在辅助信息中.

*量子性证明*：现在定义量子性证明，其允许量子证明者向经典验证者证明自己确实具有量子计算能力.

!!! info "Definition"
    一个关于随机谕示机，且密钥长度为 $\mathsf{key} = \op{poly}(\lambda)$ 的（有密钥非交互式公开可验证）量子性证明由算法 $\op{Prove}, \op{Verify}$ 组成：

    - $\op{Prove}^H(1^\lambda, k)$：这是 QPT 算法，以安全参数 $1^\lambda$ 和密钥 $k \in \{0, 1\}^{\mathsf{key}}$ 为输入，向随机谕示机 $H$ 进行 $\op{poly}(\lambda)$ 次量子查询，并输出一个经典证明 $\pi$.

    - $\op{Verify}^H(1^\lambda, k, \pi)$：这是确定性经典多项式时间算法，以安全参数 $1^\lambda$、密钥 $k \in \{0, 1\}^{\mathsf{key}}$ 和证明 $\pi$ 为输入，向随机谕示机 $H$ 进行 $\op{poly}(\lambda)$ 次经典查询，并输出 $\top$ 表示接受，或 $\perp$ 表示拒绝.

    量子性证明需要满足以下性质：

    - 正确性（Correctness）：有
    
        \[
            \op{Pr}_{H, k}[\op{Verify}^H(1^\lambda, k, \pi) = \perp: \pi \xleftarrow{\$} \op{Prove}^H(1^\lambda, k)] \leq \op{negl}(\lambda).
        \]

    - 可靠性（Soundness）：如果在 CROM 中，对于任何向 $H$ 进行 $Q(\lambda)$ 次经典谕示机查询的计算无界敌手 $\mathcal{A}$，满足

        \[
            \op{Pr}_{H, k}[\op{Verify}^H(1^\lambda, k, \pi) = \top: \pi \xleftarrow{\$} \mathcal{A}^{H}(1^\lambda, k)] \leq \varepsilon(\lambda),
        \]

        那么称该量子性证明是 $(Q(\lambda), \varepsilon(\lambda))$-可靠的. 在不指定 $Q$ 和 $\varepsilon$ 的情况下，要求是对于任何进行 $\op{poly}(\lambda)$ 次经典查询的计算无界敌手 $\mathcal{A}$，上述概率均为 $\op{negl}(\lambda)$.

与碰撞抗性类似，不存在能够抵御非均匀敌手的无密钥量子性证明.

*随机性证明*：现在定义（最小）熵证明和随机性证明，后者也被称为可认证随机性. 这些协议允许一个本身只有极少熵的经典验证者，在一个可能不可信的单个量子设备的辅助下产生大量的熵.

!!! info "Definition"
    一个关于随机谕示机，且密钥长度为 $\mathsf{key} = \op{poly}(\lambda)$ 的（有密钥非交互式公开可验证）最小熵证明由算法 $\op{Prove}, \op{Verify}$ 组成：

    - $\op{Prove}^H(1^\lambda, k, 1^h)$：这是 QPT 算法，以安全参数 $1^\lambda$、密钥 $k \in \{0, 1\}^{\mathsf{key}}$ 和最小熵阈值 $1^h$ 为输入，向随机谕示机 $H$ 进行 $\op{poly}(\lambda, h)$ 次量子查询，并输出一个经典证明 $\pi$.

    - $\op{Verify}^H(1^\lambda, k, 1^h, \pi)$：这是确定性经典多项式时间算法，以安全参数 $1^\lambda$、密钥 $k \in \{0, 1\}^{\mathsf{key}}$、最小熵阈值 $1^h$ 和证明 $\pi$ 为输入，向随机谕示机 $H$ 进行 $\op{poly}(\lambda, h)$ 次经典查询，并输出一个字符串 $x$，或 $\perp$ 表示拒绝.

    最小熵证明需要满足以下性质：

    - 正确性（Correctness）：对于任何 $h = h(\lambda)$，有
    
        \[
            \op{Pr}_{H, k}[\op{Verify}^H(1^\lambda, k, 1^h, \pi) = \perp: \pi \xleftarrow{\$} \op{Prove}^H(1^\lambda, k, 1^h)] \leq \op{negl}(\lambda).
        \]

    - 最小熵（Min-entropy）：对于任何多项式有界的 $h = h(\lambda)$，任何对 $H$ 进行 $\op{poly}(\lambda)$ 次量子查询的计算无界敌手 $\mathcal{A}$，以及任何多项式的逆函数 $\delta$，存在可忽略函数 $\op{negl}$ 满足以下条件，其中用 $\mathcal{A}^H (1^\lambda, k, 1^h)$ 表示在输出不为 $\perp$ 的条件下，$\op{Verify}^H(1^\lambda, k, 1^h, A^H(1^\lambda, k, 1^h))$ 的输出分布：

    \[
        \op{Pr}_{H, k}[\Pr{\op{Verify}^H(1^\lambda, k, 1^h, \mathcal{A}^H(1^\lambda, k, 1^h)) \neq \perp } \geq \delta(\lambda) \wedge H_\infty(\mathcal{A}_\top^H (1^\lambda, k, 1^h)) \leq h(\lambda)] \leq \op{negl}(\lambda).
    \]

    AI-QROM 中的最小熵证明可以类似地定义.

最小熵性质和正确性结合在一起蕴含了：在与诚实的 $\op{Prove}$ 算法交互时，对于绝大多是谕示机 $H$ 和密钥 $k$，$\op{Verify}$ 算法的输出所具有的最小熵至少为 $h$.

!!! info "Definition"
    一个关于随机谕示机的（有密钥非交互式公开可验证）随机性证明具有与最小熵证明相同的语法，不同之处在于允许 $\op{Verify}$ 算法是随机化的，并且要求 $\op{Verify}$ 算法的输出在不为 $\perp$ 时恰好为 $h$ 比特. 
    
    随机性证明需要满足以下性质：

    - 正确性（Correctness）：对于任何 $h = h(\lambda)$，有
    
        \[
            \op{Pr}_{H, k}[\op{Verify}^H(1^\lambda, k, 1^h, \pi; r) = \perp: \pi \xleftarrow{\$} \op{Prove}^H(1^\lambda, k, 1^h)] \leq \op{negl}(\lambda).
        \]

    - 简明随机性（Succinct Randomness）：$\op{Verify}$ 算法使用的随机数 $r$ 的长度为 $\op{poly}(\lambda, \log h)$ 比特.

    - 真实随机性（True Randomness）：对于任何多项式有界的 $h = h(\lambda)$，任何对 $H$ 进行 $\op{poly}(\lambda)$ 次量子查询的计算无界敌手 $\mathcal{A}$，以及任何多项式的逆函数 $\delta$，存在可忽略函数 $\op{negl}$，使得对于 $(1 - \op{negl}(\lambda))$ 比例的谕示机和密钥对 $(H, k)$，满足：如果满足 $\Pr{\op{Verify}^H(k, h, \mathcal{A}^H(k, h; r)) \neq \perp} \geq \delta$，则有：

        \[
            \Delta((r, U), (r, \mathcal{A}_\top^H(1^\lambda, k, 1^h; r))) \leq \op{negl}(\lambda),
        \]

        其中 $\mathcal{A}^H(1^\lambda, k, 1^h; r)$ 表示在输出不为 $\perp$ 的条件下，$\op{Verify}^H(1^\lambda, k, 1^h, \mathcal{A}^H(1^\lambda, k, 1^h); r)$ 的输出分布，$U$ 表示 $h$ 比特字符串上的均匀分布.

        换言之，只要 $\op{Verify}$ 算法能够以多项式的逆级别的概率输出一个字符串，那么对于绝大多数的 $H, k$，该字符串在统计上都极其接近于真正的随机数.

AI-QROM 中的随机性证明可以类似地定义.

*从最小熵到真实随机性*：现在讨论最小熵证明如何蕴含随机性证明. 这是提取器的一个直接应用.

!!! note "Theorem"
    如果 QROM（resp., AI-QROM）中存在最小熵证明，那么 QROM（resp., AI-QROM）中同样存在随机性证明. 如果最小熵证明是无密钥的，那么随机性证明也是无密钥的.

    ??? note "Proof"
        只需设计一个新的验证算法 $\op{Verify}'$，它为强提取器选择一个随机种子，并将该提取器作用在原 $\op{Verify}$ 算法的输出上，并直接输出该提取器的输出. 依据提取器的参数，将最小熵阈值 $h$ 选择得显著高于期望的输出长度，$\op{Verify}'$ 算法的输出将在统计上极接近所需长度得真正随机数.

### From Uniform to Non-Uniform Security

显然，抵御非均匀敌手的安全性可以蕴含抵御均匀敌手的安全性. 而另一个方向的证明利用了“盐”（salt）技术. 存在一些已有的结果，但要求敌手何时获胜是高效可验证的，这适用于单向函数、碰撞抗性和量子性证明，但不适用于最小熵证明和随机性证明. 

!!! note "Theorem"
    如果 $\{f_\lambda\}_\lambda$ 在 CROM（resp., QROM）中是单向的，那么 $\{g_\lambda\}_\lambda$ 在 AI-CROM（resp., AI-QROM）中也是单向的，其中 $g_\lambda^H(s, x) = s \Vert f_\lambda^{H(s \Vert \cdot)}(x)$，$s \in \{0, 1\}^\lambda$.

!!! note "Theorem"
    如果 $\{f_\lambda\}_\lambda$ 在 CROM（resp., QROM）中是可能有密钥的碰撞抗性的函数族，那么有密钥的函数族 $\{g_\lambda\}_\lambda$ 在 AI-CROM（resp., AI-QROM）中也是具有碰撞抗性的，其中 $g_\lambda^H(k_0 \Vert k_1, x) = f_\lambda^{H(k_1 \Vert \cdot)}(k_0, x)$，$k_1 \in \{0, 1\}^\lambda$.

!!! note "Theorem"
    如果 $(\op{Prove}_0, \op{Verify}_0)$ 是在 CROM 中具有可靠性的量子性证明，那么 $(\op{Prove}, \op{Verify})$ 是在 AI-CROM 中具有可靠性的量子性证明，其中 $\op{Prove}^H(1^\lambda, k_0 \Vert k_1) = \op{Prove}^{H(k_1 \Vert \cdot)}(1^\lambda, k_0)$，$\op{Verify}^H(1^\lambda, k_0 \Vert k_1, \pi) = \op{Verify}^{H(k_1 \Vert \cdot)}(1^\lambda, k_0, \pi)$，$k_1 \in \{0, 1\}^\lambda$.

“盐”技术也是可以将最小熵证明和随机性证明从均匀敌手情况提升至非均匀敌手情况的. 过往的结果运用了大尺寸的“盐”，但如此庞大的“盐”本身就可以作为一个真正的随机数源. 这里给出了小尺寸的“盐”也是可行的结果.

!!! note "Theorem"
    如果 $(\op{Prove}_0, \op{Verify}_0)$ 是在 QROM 中的最小熵证明（resp., 随机性证明），那么 $(\op{Prove}, \op{Verify})$ 是在 AI-QROM 中的最小熵证明（resp., 随机性证明），其中 $\op{Prove}^H(1^\lambda, k_0 \Vert k_1, 1^h) = \op{Prove}^{H(k_1 \Vert \cdot)}(1^\lambda, k_0, 1^{h+1})$，$\op{Verify}^H(1^\lambda, k_0 \Vert k_1, 1^h, \pi) = \op{Verify}^{H(k_1 \Vert \cdot)}(1^\lambda, k_0, 1^{h+1}, \pi)$，$k_1 \in \{0, 1\}^\lambda$.

## Error Correcting Codes

### Definitions

在字母表 $\Sigma$ 上，长度为 $n \in \mathbb{N}$ 的码是指子集 $C \subseteq \Sigma^n$. 

*线性码*：如果码 $C$ 的字母表为 $\Sigma = \mathbb{F}_q$，并且 $C \subseteq \mathbb{F}_q^n$ 是 $\mathbb{F}_q^n$ 的线性子空间，则称 $C$ 为线性码. 

*折叠线性码*：如果码 $C$ 的字母表为 $\Sigma = \mathbb{F}_q^m$，并且 $C \subseteq \Sigma^n$ 是 $\mathbb{F}_q^{mn}$ 的线性子空间，则称 $C$ 为折叠线性码.

线性码是折叠线性码在 $m = 1$ 时的特例. 对于线性码 $C \subseteq \mathbb{F}_q^n$ 以及整除 $n$ 的 $m \in \mathbb{N}$，定义如下的 $m$ 重折叠版本 $C^{(m)}$：

\[
    C^{(m)} = \{((x_1, \ldots, x_m), (x_{m+1}, \ldots, x_{2m}), \ldots, (x_{n-m+1}, \ldots, x_n)) : (x_1, \ldots, x_n) \in C\}.
\]

显然 $C^{(m)}$ 是折叠线性码. 反之，任何折叠线性码都可以表示为某个线性码 $C$ 和 $m \in \mathbb{N}$ 的 $C^{(m)}$ 形式.

*对偶码*：设 $C$ 是在 $\mathbb{F}_q$ 上长度为 $n$，维度为 $k$ 的线性码. 定义 $C$ 的对偶码为 $C$ 作为 $\mathbb{F}_q$ 线性空间时的正交补，即

\[
    C^\perp = \{\mathbf{z} \in \mathbb{F}_q^n : \mathbf{z} \cdot \mathbf{x} = 0, \forall \mathbf{x} \in C\}.
\]

$C^\perp$ 是在 $\mathbb{F}_q$ 上长度为 $n$，维度为 $n - k$ 的线性码. 

以类似地方式定义折叠线性码的对偶码. 对于折叠线性码 $C \subseteq \Sigma^n$，其中 $\Sigma = \mathbb{F}_q^m$，定义其对偶码为

\[
    C^\perp = \{\mathbf{z} \in \Sigma^n : \mathbf{z} \cdot \mathbf{x} = 0, \forall \mathbf{x} \in C\}.
\]

依据定义，对于任何长度为 $n$ 的线性码以及整除 $n$ 的 $m \in \mathbb{N}$，有 $(C^{(m)})^\perp = (C^\perp)^{(m)}$.

!!! success "Lemma"
    对于折叠线性码 $C \subseteq \Sigma^n$，如果定义

    \[
        f(\mathbf{x}) = \begin{cases}
            \frac{1}{\sqrt{\lvert C \rvert}} & \mathbf{x} \in C, \\
            0 & \text{otherwise}.
        \end{cases}
    \]

    那么有

    \[
        \hat{f}(\mathbf{z}) = \begin{cases}
            \frac{1}{\sqrt{\lvert C^\perp \rvert}} & \mathbf{z} \in C^\perp, \\
            0 & \text{otherwise}.
        \end{cases}
    \]

    ??? success "Proof"
        对于 $\mathbf{z} \in C^\perp$，有

        \begin{align*}
            \hat{f}(\mathbf{z}) &= \frac{1}{\lvert \Sigma \rvert^{n/2}} \sum_{\mathbf{x} \in C} f(\mathbf{x}) \omega_p^{\op{Tr}(\mathbf{x} \cdot \mathbf{z})} \\
            &= \frac{1}{\lvert \Sigma \rvert^{n/2}} \sum_{\mathbf{x} \in C} \frac{1}{\sqrt{\lvert C \rvert}} \\
            &= \frac{1}{\sqrt{\lvert C^\perp \rvert}}.
        \end{align*}

*列表恢复*：称码 $C \subseteq \Sigma^n$ 是 $(\zeta, \ell, L)$-列表可恢复的，如果对于任何满足 $\lvert S_i \rvert \leq \ell$ 的子集 $S_i \subseteq \Sigma$，$i \in [n]$，有

\[
    \lvert \{(x_1, \ldots, x_n) \in C : \lvert \{i \in [n] : x_i \in S_i\} \rvert \geq (1 - \zeta) n\} \rvert \leq L.
\]

列表可恢复性通常还要求满足 $\lvert \{i \in [n] : x_i \in S_i\} \rvert \geq (1 - \zeta) n$ 的所有码字 $(x_1, \ldots, x_n)$ 构成的列表可以从输入 $\{S_i\}_{i \in [n]}$ 在关于 $\lvert \Sigma \rvert, n, \ell$ 的多项式时间内计算出来，但本方案中不要求.

### Suitable Codes

以下引理表明存在满足目的的纠错码.

!!! success "Lemma"
    对任何常数 $0 < c < c' < 1$，存在一族显式定义的折叠线性码 $\{C_\lambda\}_{\lambda \in \mathbb{N}}$，其在字母表 $\Sigma = \mathbb{F}_q^m$ 上，长度为 $n$. 其中字母表大小 $\lvert \Sigma \rvert = 2^{\lambda^{\Theta(1)}}$，码长 $n = \Theta(\lambda)$，码空间大小满足 $\lvert C_\lambda \rvert \geq 2^{n + \lambda}$. 该码族满足以下性质：

    1. $C_\lambda$ 是 $(\zeta, \ell, L)$-列表可恢复的，其中 $\zeta = \Omega(1)$，$\ell = 2^{\lambda^c}$，且列表大小 $L = 2^{\tilde{O}(\lambda^{c'})}$.

    2. 存在一个针对对偶码的高效确定性解码算法 $\op{Decode}_{C_\lambda^\perp}$，满足以下性质. 设 $\mathcal{D}$ 为字母表 $\Sigma$ 上的概率分布，其以 $1/2$ 的概率取 $0$，以 $1/2$ 的概率在 $\Sigma \setminus \{0\}$ 上随机均匀取值，那么
    
        \[
            \mathop{Pr}\limits_{\mathbf{e} \xleftarrow{\$} \mathcal{D}^n}[\forall \mathbf{x} \in C_\lambda^\perp, \op{Decode}_{C_\lambda^\perp}(\mathbf{x} + \mathbf{e}) = \mathbf{x}] \geq 1 - 2^{-\Omega(\lambda)}.
        \]

    3. 对于所有的 $j \in [n - 1]$，有

        \[
            \mathop{Pr}\limits_{\mathbf{x} \xleftarrow{\$} C_\lambda}[\mathsf{hw}(\mathbf{x}) = n - j] \leq \left(\frac{n}{\lvert \Sigma \rvert}\right)^j.
        \]

对 $C_\lambda$ 的实例化是基于合适参数选择下的折叠 Reed-Solomon 码.

## Technical Lemmas

!!! success "Lemma"
    令 $\ket{\psi}$ 和 $\ket{\phi}$ 是基于字母表 $\Sigma = \mathbb{F}_q^m$ 的量子系统上的量子态，写作

    \begin{gather*}
        \ket{\psi} = \sum_{\mathbf{x} \in \Sigma^n} V(\mathbf{x}) \ket{\mathbf{x}}, \\
        \ket{\phi} = \sum_{\mathbf{e} \in \Sigma^n} W(\mathbf{e}) \ket{\mathbf{e}},
    \end{gather*}

    设函数 $F: \Sigma^n \to \Sigma^n$. 令 $\op{GOOD} \subseteq \Sigma^n \times \Sigma^n$ 为一个子集，满足对于任何 $(\mathbf{x}, \mathbf{e}) \in \op{GOOD}$，有 $F(\mathbf{x} + \mathbf{e}) = \mathbf{x}$. 令 $\op{BAD}$ 为 $\op{GOOD}$ 的补集. 

    假设满足

    \begin{gather*}
        \sum_{(\mathbf{x}, \mathbf{e}) \in \op{BAD} } \lvert \hat{V}(\mathbf{x}) \hat{W}(\mathbf{e}) \rvert^2 \leq \varepsilon, \\
        \sum_{\mathbf{z} \in \Sigma^n} \left \lvert \sum_{(\mathbf{x}, \mathbf{e}) \in \op{BAD} : \mathbf{x} + \mathbf{e} = \mathbf{z}} \hat{V}(\mathbf{x}) \hat{W}(\mathbf{e}) \right \rvert^2 \leq \delta.
    \end{gather*}

    定义 $U_\op{add}$ 和 $U_F$ 为以下酉变换：

    \[
        \ket{\mathbf{x}}\ket{\mathbf{e}} \xrightarrow{U_\op{add}} \ket{\mathbf{x}}\ket{\mathbf{x} + \mathbf{e}} \xrightarrow{U_F} \ket{\mathbf{x} - F(\mathbf{x} + \mathbf{e})}\ket{\mathbf{x} + \mathbf{e}}.    
    \]

    那么有

    \[
        (I \otimes (\op{QFT}_\Sigma^{\otimes n})^{-1}) U_F U_\op{add} (\op{QFT}_\Sigma^{\otimes n} \otimes \op{QFT}_\Sigma^{\otimes n}) \ket{\psi}\ket{\phi} \approx_{\sqrt{\varepsilon} + \sqrt{\delta}} \lvert \Sigma \rvert^{n/2} \sum_{\mathbf{z} \in \Sigma^n} (V \cdot W)(\mathbf{z}) \ket{0}\ket{\mathbf{z}}. 
    \]

## Proof of Quantumness

本节中给出了 QROM 中量子性证明的构造. 

!!! note "Theorem"
    存在一个关于随机谕示机的无密钥量子性证明，其在 CROM 中满足可靠性.

通过先前的定理，可以直接得到以下推论.

!!! success "Corollary"
    存在一个关于随机谕示机的有密钥量子性证明，其在 AI-CROM 中满足可靠性.

*构造*：令 $\{C_\lambda\}_\lambda$ 为字母表 $\Sigma = \mathbb{F}_q^m$ 上的折叠线性码族，其对于任意的 $0 < c < c' < 1$，满足引理中的性质.

令 $H: \Sigma \to \{0, 1\}^n$ 为随机谕示机. 对于 $i \in [n]$，定义 $H_i: \Sigma \to \{0, 1\}$ 为 $H_i(x) = H(x)_i$. 按如下方式在 QROM 中构造量子性证明协议 $\Pi = (\op{Prove}, \op{Verify})$：

- $\op{Prove}^H(1^\lambda)$：对于 $i \in [n]$，其生成状态

    \[
        \ket{\psi_i} \propto \sum_{\mathbf{e}_i \in \Sigma: H_i(\mathbf{e}_i) = 1} \ket{\mathbf{e}_i}.
    \]

    实现方式如下：其首先在 $\Sigma$ 上生成均匀叠加态，相干地评估 $H$，然后测量其输出比特，如果结果为 $1$，则成功生成了上述状态. 重复上述过程，直到成功或失败 $\lambda$ 次. 如果对于某个 $i$，在 $\lambda$ 次尝试中都未能成功生成 $\ket{\psi_i}$，则直接终止并放弃，否则设置张量积状态

    \[
        \ket{\psi} = \ket{\psi_1} \otimes \cdots \otimes \ket{\psi_n}.
    \]

    现在便得到了

    \[
        \ket{\psi} \propto \sum_{\substack{\mathbf{e} = (\mathbf{e}_1, \ldots, \mathbf{e}_n) \in \Sigma^n, \\ H_i(\mathbf{e}_i) = 1, \forall i \in [n]}} \ket{\mathbf{e}}.
    \]

    接着生成 $\ket{\phi} \propto \sum_{\mathbf{x} \in C} \ket{\mathbf{x}}$. 同时对 $\ket{\psi}$ 和 $\ket{\phi}$ 进行 $\op{QFT}$，得到

    \[
        \ket{\eta} = \op{QFT} \ket{\psi} \otimes \op{QFT} \ket{\phi}.
    \]

    设 $U_\op{add}$ 为加法酉变换，$U_\op{Decode}$ 为对偶码的解码酉变换，按照如下方式计算：

    \[
        \ket{\mathbf{x}} \ket{\mathbf{e}} \xrightarrow{U_\op{add}} \ket{\mathbf{x}} \ket{\mathbf{x} + \mathbf{e}} \xrightarrow{U_\op{Decode}} \ket{\mathbf{x} - \op{Decode}_{C^\perp}(\mathbf{x} + \mathbf{e})} \ket{\mathbf{x} + \mathbf{e}}.
    \]

    此处的解码算法也需要满足引理要求. 最后对状态应用 $(I \otimes \op{QFT}^{-1})$，并测量第二个寄存器，将结果 $x \in \Sigma^n$ 作为证明 $\pi$ 输出.

- $\op{Verify}^H(1^\lambda, \pi)$：将 $\pi$ 解析为 $\mathbf{x} = (\mathbf{x}_1, \ldots, \mathbf{x}_n) \in \Sigma^n$，如果 $\mathbf{x} \in C$ 且 $H_i(\mathbf{x}_i) = 1$ 对所有 $i \in [n]$ 成立，则输出 $\top$，否则输出 $\perp$.