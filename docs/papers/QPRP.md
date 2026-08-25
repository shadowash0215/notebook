# A Note on Quantum-Secure PRPs

## Preliminaries

本文中所讨论的密码学原语都将通过高效的经典算法来实现，使用 $\mathsf{ClassicComp}$ 和 $\mathsf{QuantComp}$ 来区分经典敌手和量子敌手，并使用 $\mathsf{ClassicQuery}$ 和 $\mathsf{QuantQuery}$ 来区分进行经典查询或量子查询的敌手.

### Cryptographic Primitives

!!! info "Definition"
    一个 $\mathsf{ClassicComp}$-（resp. $\mathsf{QuantComp}$-）单向函数是一个高效的经典函数 $\mathsf{OWF}: \{0, 1\}^\lambda \to \{0, 1\}^*$，使得对于任何高效的经典（resp. 量子）敌手 $\mathcal{A}$，其在随机输入上对 $\mathsf{OWF}$ 进行求逆的概率是可忽略的，即

    \[
        \Pr{\mathsf{OWF}(\mathcal{A}(\lambda, \mathsf{OWF}(x))) = \mathsf{OWF}(x): x \gets \{0, 1\}^\lambda} < \op{negl}(\lambda).
    \]

!!! info "Definition"
    对于双元组 $(\mathsf{Comp}, \mathsf{Query}) \in \{(\mathsf{ClassicComp}, \mathsf{ClassicQuery}), (\mathsf{QuantComp}, \mathsf{ClassicQuery}), (\mathsf{QuantComp}, \mathsf{QuantQuery})\}$，一个 $(\mathsf{Comp}, \mathsf{Query})$-伪随机函数族（PRF）是一个高效的经典函数族 $\mathsf{PRF}_{m, n}: \{0, 1\}^\lambda \times \{0, 1\}^m \to \{0, 1\}^n$，满足以下性质：对于任何多项式有界的 $m = m(\lambda)$ 和 $n = n(\lambda)$，以及任何高效的敌手 $\mathcal{A}$，$\mathcal{A}$ 无法将针对随机密钥 $k \gets \{0, 1\}^\lambda$ 的 $\mathsf{PRF}_{m, n}(k, \cdot)$ 与一个真正的随机函数 $O: \{0, 1\}^m \to \{0, 1\}^n$ 区分开来，即

    \[
        \left\lvert \Pr{\mathcal{A}^{\mathsf{PRF}_{m, n}(k, \cdot)}(\lambda) = 1: k \gets \{0, 1\}^\lambda} - \Pr{\mathcal{A}^{O(\cdot)}(\lambda) = 1} \right\rvert < \op{negl}(\lambda).
    \]

$\mathsf{PRF}$ 的定义域和陪域是单调（monotone）的，即如果 $m_1 \leq m_2$ 和 $n_1 \leq n_2$，则 $\mathsf{PRF}_{m_1, n_1}$ 可以通过截断 $\mathsf{PRF}_{m_2, n_2}$ 的输出和输入来实现.

!!! note "Theorem"
    如果存在 $\mathsf{ClassicComp}$-单向函数，则同样存在 $(\mathsf{ClassicComp}, \mathsf{ClassicQuery})$-$\mathsf{PRF}$. 如果存在 $\mathsf{QuantComp}$-单向函数，则同样存在 $(\mathsf{QuantComp}, \mathsf{ClassicQuery})$-$\mathsf{PRF}$.

## Pseudorandom Permutations

!!! info "Definition"
    对于双元组 $(\mathsf{Comp}, \mathsf{Query}) \in \{(\mathsf{ClassicComp}, \mathsf{ClassicQuery}), (\mathsf{QuantComp}, \mathsf{ClassicQuery}), (\mathsf{QuantComp}, \mathsf{QuantQuery})\}$，以及定义域类型 $\mathsf{Dom} \in \{\mathsf{LargeDom}, \mathsf{AnyDom}\}$，一个 $(\mathsf{Comp}, \mathsf{Query}, \mathsf{Dom})$-伪随机置换族（PRP）是一族高效的经典函数对 $\mathsf{PRP}_o: \{0, 1\}^\lambda \times \{0, 1\}^o \to \{0, 1\}^o$，$\mathsf{PRP}_o^{-1}: \{0, 1\}^\lambda \times \{0, 1\}^o \to \{0, 1\}^o$，满足以下性质：

    - 对于每个密钥 $k$ 和整数 $o$，$\mathsf{PRP}_o(k, \cdot)$ 和 $\mathsf{PRP}_o^{-1}(k, \cdot)$ 互为逆函数，即对于所有的 $o, k, x$，均有 $\mathsf{PRP}_o^{-1}(k, \mathsf{PRP}_o(k, x)) = x$. 这蕴含了 $\mathsf{PRP}_o(k, \cdot)$ 是一个排列.

    - 对于任何多项式有界的 $o = o(\lambda)$，以及任何高效的敌手 $\mathcal{A}$，$\mathcal{A}$ 无法将针对随机密钥 $k \gets \{0, 1\}^\lambda$ 的 $\mathsf{PRP}_o(k, \cdot)$ 与一个真正的随机置换 $P: \{0, 1\}^o \to \{0, 1\}^o$ 区分开来. 考虑其强变体，其中 $\mathcal{A}$ 可以访问 $P$，也可以访问 $P^{-1}$，即

        \[
            \left\lvert \Pr{\mathcal{A}^{\mathsf{PRP}_o(k, \cdot), \mathsf{PRP}_o^{-1}(k, \cdot)}(\lambda) = 1: k \gets \{0, 1\}^\lambda} - \Pr{\mathcal{A}^{P(\cdot), P^{-1}(\cdot)}(\lambda) = 1} \right\rvert < \op{negl}(\lambda).  
        \]

    - 如果 $\mathsf{Dom} = \mathsf{LargeDom}$，则只要求 $o$ 足够大时成立. 但如果 $\mathsf{Dom} = \mathsf{AnyDom}$，则要求对于所有多项式有界的 $o$ 都成立，此时 $o$ 可以是对数级的. 定义域为 $\{0 ,1\}^o$ 的 $\mathsf{PRP}$ 并不能直接给出一个定义域为 $\{0, 1\}^{o'}$ 的 $\mathsf{PRP}$，其中 $o' < o$，因为无法保证其在 $\{0, 1\}^{o'}$ 上仍然是一个排列. 

### Function to Permutation Converters

!!! info "Definition"
    设 $\mathsf{Query} \in \{\mathsf{ClassicQuery}, \mathsf{QuantQuery}\}$，$\mathsf{Dom} \in \{\mathsf{LargeDom}, \mathsf{AnyDom}\}$，固定一个在 $o, \lambda$ 上的函数族 $\mathcal{Q}$. 一个 $(\mathsf{Query}, \mathsf{Dom}, Q)$-函数到置换转换器（FPC）是一个由高效经典谕示机算法对 $$\mathsf{F}_o, $\mathsf{R}_o$，满足：

    - $\mathsf{F}_o, $\mathsf{R}_o$ 接收 $\lambda$ 和字符串 $x \in \{0, 1\}^o$ 作为输入，输出字符串 $y \in \{0, 1\}^o$.

    - 存在多项式 $m(o, \lambda)$，$n(o, \lambda)$，$\mathsf{F}_o$ 和 $\mathsf{R}_o$ 可以向谕示机 $O: \{0, 1\}^m \to \{0, 1\}^n$ 发起查询.

    - $\mathsf{F}_o$ 和 $\mathsf{R}_o$ 是高效的，运行时间为 $\op{poly}(o, \lambda)$. 特别地，它们对 $O$ 的查询次数至多为 $\op{poly}(o, \lambda)$.

    - $\mathsf{F}_o$ 和 $\mathsf{R}_o$ 互为逆函数，即对于所有的 $x \in \{0, 1\}^o$ 和谕示机 $O$，均有 $$\mathsf{R}_o^O(\lambda, $\mathsf{F}_o^O(\lambda, x)) = x$.

    - 在给定查询权限的情况下，$\mathsf{F}_o$ 和 $\mathsf{R}_o$ 与一个随机排列及其逆函数是不可区分的. 设 $o(\lambda)$ 是一个多项式有界的函数，如果 $\mathsf{Dom} = \mathsf{LargeDom}$，则同时限制 $o$ 被某个多项式下界约束. 设 $q(\lambda) = q(o(\lambda), \lambda)$ 是 $\mathcal{Q}$ 中的任意函数，$\mathcal{A}$ 是**任意**（可能非高效，即计算能力无限）敌手，其对谕示机查询次数至多为 $q$，其中如果 $\mathsf{Query} = \mathsf{QuantQuery}$，则 $\mathcal{A}$ 可以发起量子查询. 则有

        \[
            \left\lvert \Pr{\mathcal{A}^{$\mathsf{F}_o^O(\lambda, \cdot), $\mathsf{R}_o^O(\lambda, \cdot)}(\lambda) = 1} - \Pr{\mathcal{A}^{P(\cdot), P^{-1}(\cdot)}(\lambda) = 1} \right\rvert < \op{negl}(\lambda),
        \]

### The Main Lemma

本节证明 $\mathsf{FPC}$ 足以构造 $\mathsf{PRP}$.

!!! success "Lemma"
    设 $\mathcal{Q}$ 是所有多项式的集合，如果存在 $(\mathsf{Comp}, \mathsf{Query})$-$\mathsf{PRF}$ 且存在 $(\mathsf{Query}, \mathsf{Dom}, \mathcal{Q})$-$\mathsf{FPC}$，则同样存在 $(\mathsf{Comp}, \mathsf{Query}, \mathsf{Dom})$-$\mathsf{PRP}$.

    ???+ success "Proof"
        证明 $(\mathsf{QuantComp}, \mathsf{QuantQuery}, \mathsf{AnyDom})$-$\mathsf{PRP}$ 的存在性，其他情况类似. 构造如下：

        \begin{gather*}
            \mathsf{PRP}_o(k, x) = $\mathsf{F}_o^{\mathsf{PRF}_{m, n}(k, \cdot)}(\lambda, x), \\
            \mathsf{PRP}_o^{-1}(k, x) = $\mathsf{R}_o^{\mathsf{PRF}_{m, n}(k, \cdot)}(\lambda, x).
        \end{gather*}

        其中 $\lvert k \rvert = \lambda$. 安全性通过混合论证证明.

        **Hybrid 0**: $\mathcal{A}$ 被赋予谕示机 $P(x) = $\mathsf{F}_o^{\mathsf{PRF}_{m, n}(k, \cdot)}(\lambda, x)$ 和 $P^{-1}(x) = $\mathsf{R}_o^{\mathsf{PRF}_{m, n}(k, \cdot)}(\lambda, x)$，其中 $k \gets \{0, 1\}^\lambda$. 这就是真实的构造场景.

        **Hybrid 1**: 将 $\mathsf{PRF}$ 替换为真实的随机函数 $O: \{0, 1\}^m \to \{0, 1\}^n$，$\mathcal{A}$ 被赋予谕示机 $P(x) = $\mathsf{F}_o^{O(\cdot)}(\lambda, x)$ 和 $P^{-1}(x) = $\mathsf{R}_o^{O(\cdot)}(\lambda, x)$. 
        
        假设 $\mathcal{A}$ 以不可忽略的概率区分 Hybrid 0 和 Hybrid 1，则可以构造一个 $\mathsf{PRF}$ 对手 $\mathcal{B}^O(\lambda) = A^{\mathsf{F}_o^O(\lambda, \cdot), \mathsf{R}_o^O(\lambda, \cdot)}(\lambda)$. 如果 $O(\cdot) = \mathsf{PRF}_{m, n}(k, \cdot)$，则 $\mathcal{A}$ 的行为与 Hybrid 0 相同；如果 $O(\cdot)$ 是一个真正的随机函数，则 $\mathcal{A}$ 的行为与 Hybrid 1 相同. 此外，对于 $\mathcal{A}$ 发起的任何量子查询，$\mathcal{B}$ 可以通过向其自身的谕示机发起多项式个量子查询予以回答. 因此 $\mathcal{B}$ 是一个高效的量子算法，其在攻破 $\mathsf{PRF}$ 安全性上的优势和 $\mathcal{A}$ 在区分 Hybrid 0 和 Hybrid 1 上的优势相同，这与 $\mathsf{PRF}$ 具备 $(\mathsf{QuantComp}, \mathsf{QuantQuery})$-安全性相矛盾. 因此 Hybrid 0 和 Hybrid 1 是不可区分的.

        **Hybrid 2**：$\mathcal{A}$ 被赋予了真实的随机排列谕示机 $P$ 和 $P^{-1}$. Hybrid 1 和 Hybrid 2 的不可区分性由 $\mathsf{F}$，$\mathsf{R}$ 的 $(\mathsf{QuantQuery}, \mathsf{AnyDom}, \mathcal{Q})$-安全性保证. 这就完成了证明.

### Constructions of FPCs