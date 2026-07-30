# Separating $\mathsf{QMA}$ from $\mathsf{QCMA}$ with a classical oracle

## Preliminaries

### Quantum query complexity

**量子查询算法**

大小为 $n$ 的谕示机指代 $\mathcal{O}: \{0, 1\}^n \mapsto \{0, 1\}$ 的布尔函数，而谕示机本身可以指代将任意字符串映射为一个比特的函数 $\mathcal{O}: \{0, 1\}^* \mapsto \{0, 1\}$.

!!! info "Definition(Quantum query circuit/algorithm)"
    量子查询算法定义为一个和布尔谕示机 $\mathcal{O}: \{0, 1\}^n \mapsto \{0, 1\}$ 交互的无输入量子电路. 谕示机是通过一个相位查询门进行访问的：

    \[
        \ket{b, x} \mapsto (-1)^{b \cdot \mathcal{O}(x)} \ket{b, x},
    \]

    其作用在 $n+1$ 个量子比特上. 该算法由交替出现的酉算子和谕示机门序列描述，$t$ 表示算法进行的谕示机查询次数，$n$ 表示布尔谕示机的大小. 在所有门的作用后，将会在计算基下测量一个指定的输出量子比特，以决定是否接受. 所有量子比特的初态为 $\ket{0}$，且所有酉算子作用于任意但有限数量的量子比特上.

一对函数 $(S, U): \{0, 1\}^{n - 1} \mapsto \{0, 1\}$ 可以通过以下方式表示为 $n$ 个量子比特上的单个函数：

\[
    \mathcal{O}(b, x) = \begin{cases}
        S(x) & \text{if } b = 0, \\
        U(x) & \text{if } b = 1.
    \end{cases}
\]

!!! info "Definition(Quantum query algorithm with witness)"
    量子查询算法也可以带有一个辅助见证（auxiliary witness），主要考虑以下两种见证类型：

    - 量子见证：$q$ 个量子比特的量子态 $\ket{\psi}$.

    - 经典见证：比特串 $w \in \{0, 1\}^q$，被视为一个计算基态.

    除了输入态变为 $\ket{\psi} \otimes \ket{0}^{\otimes (n + 1)}$ 或 $\ket{w} \otimes \ket{0}^{\otimes (n + 1)}$ 外，其他定义保持不变. 该算法的接受概率可能同时取决于谕示机和见证. 

**量子复杂度理论**

!!! info "Definition(Quantum oracle circuits)"
    定义一族量子谕示机电路/算法 $\{\mathcal{A}_n\}_{n \geq 1}$，其中索引 $n$ 对应计算问题显式输入的长度. 每个 $\mathcal{A}_n$ 都可以具体的表示为一个量子电路，包括以下部分：

    - 从固定、完备的量子门集合中抽取的初等量子门；

    - 谕示机相位门，通过以下方式提供对布尔谕示机 $\mathcal{O}_k: \{0, 1\}^k \mapsto \{0, 1\}$ 的相干访问：
    
        \[
            \ket{b, x} \mapsto (-1)^{b \cdot \mathcal{O}_k(x)} \ket{b, x}, x \in \{0, 1\}^k, b \in \{0, 1\}.
        \]

    这可以被视作从各种长度上访问 $\mathcal{O}$ 的电路模型定义.

    如果存在一个确定性多项式时间图灵机 $M$，它在输入 $1^n$ 时输出电路 $\mathcal{A}_n$ 的完整经典描述，那么电路族 $\{\mathcal{A}_n\}$ 是 **$\mathsf{P}$-一致**的. 因为 $M$ 在 $n$ 的多项式时间内运行，所以生成的电路 $\mathcal{A}_n$ 需要满足以下多项式界：

    - 其接受大小为 $n$ 的经典输入，由酉算子门组成，而后对单个量子比特进行测量并得到二进制输出；

    - 其包含最多 $\poly{n}$ 个量子门；

    - 其查询 $\mathcal{O}_k$ 的最大长度 $k$ 也被限制为 $\poly{n}$.

    以上确保了该电路族代表一个在多项式资源内运行、可高效描述的量子算法.

运用 $\mathsf{P}$-一致的量子谕示机算法，便可以定义标准的谕示机量子复杂度类.

!!! info "Definition(Oracle $\mathsf{BQP}$)"
    承诺语言（Promise language）$\mathcal{L}^\mathcal{O} = (\mathcal{L}_\text{yes}, \mathcal{L}_\text{no})^\mathcal{O} \subseteq \{0, 1\}^*$ 属于 **$\mathsf{BQP}^\mathcal{O}$**，如果存在一个 $\mathsf{P}$-一致的量子谕示机算法族 $\{\mathcal{A}_n\}$ 使得对于任意输入 $x$，长度为 $n = \lvert x \rvert$，满足以下条件：

    \begin{align*}
        \text{(Completeness)} \quad & x \in \mathcal{L}_\text{yes} \Rightarrow \Pr{\mathcal{A}_n^\mathcal{O}(x) \text{ accepts}} \geq 2/3, \\
        \text{(Soundness)} \quad & x \in \mathcal{L}_\text{no} \Rightarrow \Pr{\mathcal{A}_n^\mathcal{O}(x) \text{ accepts}} \leq 1/3.
    \end{align*}

类似地，定义 $\mathsf{QCMA}^\mathcal{O}$ 和 $\mathsf{QMA}^\mathcal{O}$.

!!! info "Definition(Oracle $\mathsf{QCMA}$)"
    承诺语言 $\mathcal{L}^\mathcal{O} = (\mathcal{L}_\text{yes}, \mathcal{L}_\text{no})^\mathcal{O} \subseteq \{0, 1\}^*$ 属于 **$\mathsf{QCMA}^\mathcal{O}$**，如果存在一个 $\mathsf{P}$-一致的量子谕示机算法族 $\{\mathcal{A}_n\}$，$\{\mathcal{A}_n\}$ 接受一个长度为 $q(n)$ 的经典见证，使得对于任意输入 $x$，长度为 $n = \lvert x \rvert$，满足以下条件：

    \begin{align*}
        \text{(Completeness)} \quad & x \in \mathcal{L}_\text{yes} \Rightarrow \exists w \in \{0, 1\}^{q(n)} \text{ s.t. } \Pr{\mathcal{A}_n^\mathcal{O}(x, w) \text{ accepts}} \geq 2/3, \\
        \text{(Soundness)} \quad & x \in \mathcal{L}_\text{no} \Rightarrow \forall \tilde{w} \in \{0, 1\}^{q(n)}, \Pr{\mathcal{A}_n^\mathcal{O}(x, \tilde{w}) \text{ accepts}} \leq 1/3.
    \end{align*}

!!! info "Definition(Oracle $\mathsf{QMA}$)"
    承诺语言 $\mathcal{L}^\mathcal{O} = (\mathcal{L}_\text{yes}, \mathcal{L}_\text{no})^\mathcal{O} \subseteq \{0, 1\}^*$ 属于 **$\mathsf{QMA}^\mathcal{O}$**，如果存在一个 $\mathsf{P}$-一致的量子谕示机算法族 $\{\mathcal{A}_n\}$，$\{\mathcal{A}_n\}$ 接受一个长度为 $q(n)$ 的量子见证，使得对于任意输入 $x$，长度为 $n = \lvert x \rvert$，满足以下条件：

    \begin{align*}
        \text{(Completeness)} \quad & x \in \mathcal{L}_\text{yes} \Rightarrow \exists \ket{\psi} \in (\mathbb{C}^2)^{\otimes q(n)} \text{ s.t. } \Pr{\mathcal{A}_n^\mathcal{O}(x, \ket{\psi}) \text{ accepts}} \geq 2/3, \\
        \text{(Soundness)} \quad & x \in \mathcal{L}_\text{no} \Rightarrow \forall \ket{\tilde{\psi}} \in (\mathbb{C}^2)^{\otimes q(n)}, \Pr{\mathcal{A}_n^\mathcal{O}(x, \ket{\tilde{\psi}}) \text{ accepts}} \leq 1/3.
    \end{align*}

### Spectral Forrelation

!!! info "Definition(Spectral Forrelation)"
    称两集合 $S, U \subseteq \{0, 1\}^n$ 为 **$\alpha$-谱相关**（$\alpha$-spectrally forrelated）的，如果

    \[
        \alpha = \lVert \Pi_U \cdot H^{\otimes n} \cdot \Pi_S \rVert^2_{\text{op}} = \max_{\lVert \ket{\psi} \rVert = 1} \lVert \Pi_U \cdot H^{\otimes n} \cdot \Pi_S \ket{\psi} \rVert^2,
    \]

    其中 $\Pi_S$ 和 $\Pi_U$ 分别是投影到 $S$ 和 $U$ 中元素张成的子空间的投影算子.

!!! note "Theorem($\mathsf{QMA}$ containment)"
    对任意 $\alpha > \beta$，存在一个具有 $n$ 量子比特量子见证的 $O(1/(\alpha - \beta)^2)$ 的量子查询算法，给定对谕示机 $S, U: \{0, 1\}^n \mapsto \{0, 1\}$ 的查询访问，如果它们是至少 $\alpha$-谱相关的（Yes 实例），则接受的概率至少为 $2/3$，如果它们是至多 $\beta$-谱相关的（No 实例），则接受的概率至多为 $1/3$. 

    ??? note "Proof"
        存在一个简单的验证器，其以 $\geq \alpha$ 的概率接受 Yes 实例，并以 $\leq \beta$ 的概率接受 No 实例. 设 $\ket{\psi}$ 为 $n$ 量子比特的量子见证，以下量子电路描述了该验证器：

        \qcircuit
            \lstick{\ket{0}} & \qw & \gate{H} & \ctrl{2} & \qw & \qw & \gate{H} & \meter & \cw \\
            \lstick{\ket{0}} & \qw & \gate{H} & \qw & \qw & \ctrl{1} & \gate{H} & \meter & \cw \\
            \lstick{\ket{\psi}} & \qw & \qw & \gate{S} & \gate{H^{\otimes n}} & \gate{U} & \qw & \qw & \qw

        如果两次测量的结果均为 $1$，则接受. 不难验证，两次测量均输出 $1$ 的概率为 $\lVert \Pi_U \cdot H^{\otimes n} \cdot \Pi_S \ket{\psi} \rVert^2$. 依据定义，对于 Yes 实例，存在状态 $\ket{\psi}$ 使得该概率 $\geq \alpha$，而对于 No 实例，对于任意状态 $\ket{\psi}$，该概率 $\leq \beta$. 

        利用 Marriott-Watrous 放大技术，通过进行 $O(1/(\alpha - \beta)^2)$ 此查询，便可以将该验证器转换为一个能以完备性-可靠性为 $(2/3, 1/3)$ 的判定谱相关问题的验证器.

## Constructing samplers from strong yes instances

假设存在一个需要 $t$ 次查询，带有 $q$ 比特经典见证的量子查询算法 $\mathcal{A}^{(S, U)}$，该算法可以解决谱相关问题. 形式化地，假定该量子查询算法具有以下性质：

1. (Completeness) 如果 $(S, U)$ 是至少 $59/100$-谱相关的，则存在一个见证 $w \in \{0, 1\}^q$，使得 $\mathcal{A}^{(S, U)}(w)$ 以至少 $2/3$ 的概率接受.

2. (Soundness) 如果 $(S, U)$ 是至多 $57/100$-谱相关的，则对于任意见证 $\tilde{w} \in \{0, 1\}^q$，$\mathcal{A}^{(S, U)}(\tilde{w})$ 以至多 $1/3$ 的概率接受.

本节中，称至少 $59/100$-谱相关的对 $(S, U)$ 称为谱相关的 Yes 实例，而至多 $57/100$-谱相关的对 $(S, U)$ 称为谱相关的 No 实例. 

对多重集 $S$ 和 $U$ 的谕示机访问可以描述为以下映射的线性扩展

\begin{align*}
    \ket{b, x}\ket{z} & \xrightarrow{\mathcal{O}_S} (-1)^{b \cdot S(x)} \ket{b, x}\ket{z}, \\
    \ket{b, x}\ket{z} & \xrightarrow{\mathcal{O}_U} (-1)^{b \cdot U(x)} \ket{b, x}\ket{z},
\end{align*}

$b$ 是控制比特，$x$ 描述谕示机的输入，$z$ 描述系统其余部分的状态.

### Sampling from $S$

将算法 $\mathcal{A}^{(S, U)}$ 视作 $(\mathcal{A}^U)^S$，即一个由标准酉门和 $U$ 谕示机门构成，并向 $S$ 谕示机发起查询的算法 $\mathcal{A}^U$. 算法 $(\mathcal{A}^U)^S$ 在最终测量前的状态由下式给出：

\[
    V_t \mathcal{O}_S V_{t - 1} \mathcal{O}_S \cdots \mathcal{O}_S V_0 \ket{w, 0}
\]

其中酉变换 $\{V_j\}$ 包含了对 $U$ 的查询. 考虑以下算法，其接受一个见证 $w$ 和子集 $\Delta \subseteq \{0, 1\}^n$ 作为输入. 算法 $\mathsf{Sampler}^U(\Delta, w)$ 是一个采样器，用于在给定已经找到的点的先验子集 $\Delta$ 的情况下，从 $S$ 中生成一个额外样本. 对多重集 $S$ 和集合 $\Delta$，$S \setminus \Delta$ 表示 $S$ 中出现重数至少为 $1$ 且不在 $\Delta$ 中的元素的集合.

\algorithm
    \caption{Query algorithm $\mathsf{Sampler}^U(w, \Delta)$}
    \KwResult{}
    $\text{Sample } j \gets \{0, \ldots, t-1\} \text{ uniformly randomly}$\;
    $\text{Compute the state } V_j \mathcal{O}_\Delta V_{j - 1} \mathcal{O}_\Delta \cdots \mathcal{O}_\Delta V_0 \ket{w, 0}$\;
    $\mathcal{O}_\Delta \text{ is the unitary defined by } \mathcal{O}_\Delta \ket{b, x}\ket{z} \xrightarrow{\mathcal{O}_\Delta} (-1)^{b \cdot \delta(x \in \Delta)} \ket{b, x}\ket{z}$\;
    $\text{Measure the state in the standard basis for output } (b, x, z)$\;
    $\text{If } x \in \Delta \text{, output the alphabetically first symbol not in } \Delta \text{. Else output } x$\;

核心思想是为了让 $\mathcal{A}^U$ 能够区分 $S$ 和 $\Delta$，它必须查询在 $S$ 中但不在 $\Delta$ 中的元素，因为在这类点外 $\mathcal{O}_\Delta$ 和 $S$ 具有完全相同的表现.

!!! success "Lemma"
    设 $(S, U)$ 是谕示机判定问题的一个 Yes 实例. $\Delta \subset S$ 是使得 $(\Delta, U)$ 是一个 No 实例的子集. $w$ 是一个使查询算法 $\mathcal{A}$ 以至少 $2/3$ 的概率接受 $(S, U)$ 的见证. 那么算法 $\mathsf{Sampler}^U(w, \Delta)$ 向谕示机 $U$ 发起 $t$ 次查询，向谕示机 $S$ 发起 $0$ 次查询，并以至少 $\frac{1}{36t^2}$ 的概率产生一个来自 $S \setminus \Delta$ 的样本.

    ???+ success "Proof"
        首先定义一系列**杂交态**（hybrid states）：

        \[
            \ket{h_j(w)} := V_t \mathcal{O}_S \cdots \mathcal{O}_S V_{j} \mathcal{O}_\Delta V_{j - 1} \mathcal{O}_\Delta \cdots V_1 \mathcal{O}_\Delta V_0 \ket{w, 0}, 
        \]

        其中

        \[
            \ket{\psi_j(w)} := V_j \mathcal{O}_S V_{j - 1} \mathcal{O}_S \cdots V_1 \mathcal{O}_S V_0 \ket{w, 0}
        \]

        称为第 $j$ 个**前缀态**（prefix state）. 直观地，前缀态 $\ket{\psi_j(w)}$ 对应于使用谕示机 $(\Delta, U)$ 进行前 $j$ 次查询的算法 $\mathcal{A}^U$ 的状态，而杂交态 $\ket{h_j(w)}$ 对应于将对 $S$ 谕示机的前 $j$ 次查询替换为对 $\Delta$ 谕示机的查询的状态. 因而 $\ket{h_0(w)}$ 对应于在 $(\Delta, U)$ 上运行 $\mathcal{A}$，而 $\ket{h_t(w)}$ 对应于在 $(S, U)$ 上运行 $\mathcal{A}$.

        因为 $(\Delta, U)$ 是一个 No 实例，而 $(S, U)$ 是一个 Yes 实例，所以存在一个测量，在计算基下测量第一个量子比特，其接受 $\ket{h_0(w)}$ 的概率至多为 $1/3$，而接受 $\ket{h_t(w)}$ 的概率至少为 $2/3$. 因此有

        \begin{align*}
            \frac{1}{3} & \leqslant \op{Tr}[\ket{0}\bra{0}(\ket{h_t(w)}\bra{h_t(w)} - \ket{h_0(w)}\bra{h_0(w)})] \\
            & \leqslant \frac{1}{2} \lVert \ket{h_t(w)}\bra{h_t(w)} - \ket{h_0(w)}\bra{h_0(w)} \rVert_1 \\
            & \leqslant \lVert \ket{h_t(w)} - \ket{h_0(w)} \rVert
        \end{align*}

        其中第二行来源于迹距离 $D(\rho, \sigma) = \max_P \op{Tr}[P(\rho - \sigma)]$ 的定义，第三行利用保真度进行转换：

        \begin{align*}
            D(\ket{h_t(w)}, \ket{h_0(w)}) & \leqslant \sqrt{1 - F(\ket{h_t(w)}, \ket{h_0(w)})^2} \\
            & \leqslant \sqrt{2(1 - F(\ket{h_t(w)}, \ket{h_0(w)}))} \\
            & = \sqrt{2(1 - \lvert \innerproduct{h_t(w)}{h_0(w)} \rvert)} \\
            & \leqslant \sqrt{2(1 - \Re \innerproduct{h_t(w)}{h_0(w)})} \\
            & = \lVert \ket{h_t(w)} - \ket{h_0(w)} \rVert.
        \end{align*}

        再依据三角不等式：

        \begin{align*}
            \frac{1}{3} & \leqslant \lVert \ket{h_t(w)} - \ket{h_0(w)} \rVert \\
            & \leqslant \sum_{j = 1}^t \lVert \ket{h_j(w)} - \ket{h_{j - 1}(w)} \rVert \\
            & \leqslant \sum_{j = 0}^{t - 1} \lVert (\mathcal{O}_\Delta - \mathcal{O}_S) \ket{\psi_j(w)} \rVert \\
            & = 2 \sum_{j = 0}^{t - 1} \lVert \Gamma \ket{\psi_j(w)} \rVert.
        \end{align*}

        其中 $\Gamma := \sum_{x \in S \setminus \Delta} \ket{1, x} \bra{1, x} \otimes \mathrm{id}$.

        因为 $S$ 是一个受控相位翻转谕示机，当 $b = 1$ 且 $x \in S$ 时会施加一个 $-1$ 的相位. 而 $\Delta \subseteq S$，$\mathcal{O}_\Delta - \mathcal{O}_S$ 便是向形如 $\ket{1, x}$ 且 $x \in S \setminus \Delta$ 的字符串投影的投影算子的两倍.

        对于 $j \in \{0, \cdots, t - 1\}$，将 $\ket{\psi_j(w)}$ 表示为

        \[
            \ket{\psi_j(w)} = \sum_x \beta_x^{(j)} \ket{x} \otimes \ket{\psi_j(x, w)}, \quad \beta_x^{(j)} \in \mathbb{R}^+.
        \]

        控制比特 $b$ 被包含在状态 $\ket{\psi_j (x, w)}$ 中. 使用 Cauchy-Schwarz 不等式：

        \[
            \frac{1}{6} \leqslant \sum_{j = 0}^{t - 1} \sqrt{\sum_{x \in S \setminus \Delta} (\beta_x^{(j)})^2} \leqslant \sqrt{t} \sqrt{\sum_{j = 0}^{t - 1} \sum_{x \in S \setminus \Delta} (\beta_x^{(j)})^2}.
        \]

        也就有

        \[
            \frac{1}{36t^2} \leqslant \frac{1}{t} \sum_{j = 0}^{t - 1} \sum_{x \in S \setminus \Delta} (\beta_x^{(j)})^2.
        \]

        而右侧就是 $\mathsf{Sampler}^U(w, \Delta)$ 输出来自 $S \setminus \Delta$ 的样本 $x$ 的概率.

### Witness-free sampler

$\mathsf{Sampler}^U(w, \Delta)$ 的运行需要输入见证 $w$. 以 $\mathsf{Sampler}^U(w, \Delta)$ 能够输出一个来自 $S$ 的新元素点为条件，可以迭代该采样器产生多个点，这便产生了一个同样需要见证的**累积采样器**（Cumulative Sampler）. 不过只需付出成功概率降低的代价，便可以换来不需要见证的累积采样器.

\algorithm
    \caption{Query algorithm $\mathsf{CumulativeSampler}^U$}
    \KwResult{}
    $\text{Sample a random } w \in \{0, 1\}^q$\;
    $\text{Initialize } \Delta \gets \varnothing$\;
    $\text{For } v \text{ rounds, run } \mathsf{Sampler}^U(w, \Delta) \text{ with fresh independent randomness.}$\;
    $\text{Append output } x: \Delta \gets \Delta \cup \{x\}$\;
    $\text{Output the resulting } \Delta$\; 

算法 $\mathsf{CumulativeSampler}^U$ 不需要任何见证作为输入，这意味着，对于每个使得 $(\Delta, U)$ 在子集 $\Delta$ 很小时均为 No 实例的 Yes 实例 $(S, U)$，同一个采样器都能以前述的概率产生来自 $S$ 的样本. 接下来在以下定理中形式化这一观察.

!!! note "Theorem(Good samplers from $\mathsf{QCMA}$ algorithm)"
    假设存在一个用于解决谱相关问题的、带有经典见证的量子查询算法 $\mathcal{A}$，使得对于规模为 $n$ 的实例，$\mathcal{A}$ 接受一个大小为 $q$ 的经典见证并进行 $t$ 次谕示机查询. 令 $(S, U)$ 为谱相关问题的一个 Yes 实例，且存在 $v \in \mathbb{N}$ 使得对于所有 $\lvert \Delta \rvert \leqslant v$ 的子集 $\Delta \subseteq S$，$(\Delta, U)$ 都是谱相关问题的 No 实例. 存在一个查询算法 $\mathsf{CumulativeSampler}$（隐式依赖于 $v$）使得 $\mathsf{CumulativeSampler}^U$ 对 $S$ 进行 $0$ 次查询，对 $U$ 进行 $vt$ 次查询，并至少以 $2^{-q} \cdot \left(\frac{1}{36t^2}\right)^v$ 的概率产生来自 $S$ 的 $v$ 个互不相同的样本.

    ??? note "Proof"
        定义 $G$ 为事件“采样得到的见证 $w$ 恰好是针对谕示机对 $(S, U)$ 的一个好见证”，$E_1, \ldots, E_v$ 为事件“对应的各轮猜测确实落在 $S$ 中”. 根据算法构造，这些样本是互不相同的. 它们全部正确的概率为：

        \begin{align*}
            \Pr{E_1, \ldots, E_v} & \geqslant \Pr{G} \cdot \Pr{E_1, \ldots, E_v \mid G} \\
            & \geqslant \Pr{G} \cdot \prod_{j = 1}^v \Pr{E_j \mid E_1, \ldots, E_{j - 1}, G} \\
            & \geqslant 2^{-q} \cdot \left(\frac{1}{36t^2}\right)^v.
        \end{align*}

## Strong yes instances for spectral Forrelation

!!! info "Definition(Strong yes instance)"
    对于任意满足 $t_1 < t_2$ 的 $t_1, t_2, v$，如果一个对 $(S, U)$ 满足以下条件，则称其为 $(t_1, t_2, v)$-强 Yes 实例：

    1. (Completeness) $(S, U)$ 是至少 $t_2$-谱相关的.
    2. (Soundness) 对于所有 $\lvert \Delta \rvert \leqslant v$ 的子集 $\Delta \subseteq S$，$(\Delta, U)$ 是至多 $t_1$-谱相关的.

直观上，为了证伪定理导出的推论，需要构造许多强 Yes 实例，并证明没有任何低查询强度的采样器能在所有这些 Yes 实例上都获得成功. 为了构建这些 Yes 实例希望采样一个大小为 $l$ 的随机多重集 $S$，然后构造以高概率与 $S$ 相关的集合 $U$. 为此，定义：

\[
    \gamma_y(S) := \left(\frac{1}{\sqrt{l}} \sum_{i \in [l]} (-1)^{y \cdot s_i} \right)^2 = \frac{1}{l} \sum_{i, j} (-1)^{y \cdot (s_i + s_j)} = 1 + \frac{1}{l} \sum_{i \neq j} (-1)^{y \cdot (s_i + s_j)}.
\]

注意到 $\gamma_y(S) = 2^n \cdot \lvert \bra{y} H^{\otimes n} \ket{S} \rvert^2$，其中 $\ket{S}$ 为 $S$ 上的叠加态.

以下引理证明了存在一个绝大部分支撑都在强 Yes 实例上的分布，结合先前的定理表明 QCMA 算法蕴含了针对一个特定分布的采样器，在之后的部分将会证明这样的采样器不可能存在.

!!! info "Definition(The $\mathsf{Strong}$ distribution)"
    谕示机对 $(S, U)$ 上的分布 $\mathsf{Strong}_\kappa$ 定义为：

    (a) 通过从 $\{0, 1\}^n$ 中随机均匀采样 $s_i$ 得到一个大小为 $l$ 的多重集 $S$；

    (b) 随后采样集合 $U$：以 $1 - e^{-\kappa \gamma_y(S)/2}$ 的概率将每一个点 $y \in \{0, 1\}^n \setminus \{0^n\}$ 添加进 $U$ 中.

    通过考虑多重集的指示谕示机，分布 $\mathsf{Strong} = \mathsf{Strong}_\kappa$ 也可以看作是谕示机对 $(S, U)$ 上的一个分布.

!!! success "Lemma(The strong yes property)"
    对于所有 $\kappa \in [0, 1]$, $\rho \geqslant 0$ 使得以下定义的 $t_1 < t_2$，从 $\mathsf{Strong}_\kappa$ 中采样得到的谕示机对 $(S, U)$ 是一个 $(t_1, t_2, v)$-强 Yes 实例，例外概率至多为

    \[
        l^6 2^{-n} + 2 l^2 \exp\left(-\frac{\rho^2 2^n}{2 l^2}\right),
    \]

    其中

    \begin{align*}
        t_1 & = \frac{1 + \kappa}{2} + \frac{v}{l} + \rho, \\
        t_2 & = \frac{1 + 3 \kappa}{2} - \frac{15\kappa^2}{4} - \frac{5 \kappa}{l} - \rho.
    \end{align*}

    特别地，若 $500 \leqslant l \ll 2^{n/6}$，通过设置 $\rho = \sqrt{\frac{2 l^2}{2^n} \ln(\frac{2 \cdot 2^n}{l^4})}$，可以使得 $2 l^2 \exp(-\frac{\rho^2 2^n}{2 l^2}) = l^6 2^{-n}$，从而使得例外概率至多为 $2 l^6 2^{-n}$. 选取 $\kappa = 1/10$，则 $(S, U)$ 是一个 $(57/100, 59/100, l/100)$-强 Yes 实例.

    !!! tip "Remark"
        最重要的是谕示机 $U$ 的构造方式必须使得其包含点 $y$ 的概率是关于 $\gamma_y(S) = 2^n \lvert \bra{y} H^{\otimes n} \ket{S} \rvert^2$ 的函数. 对于 $U$ 的某些其他构造选择，如果将 $y$ 包含在 $U$ 中的概率是关于 $\lvert \bra{y} H^{\otimes n} \ket{S} \rvert$ 本身的函数，那么就会存在一些利用对 $U$ 的谕示机访问来合成量子态 $\ket{S}$ 的方法.

    ???+ success "Proof"
        对于列表 $S = \{s_1, \ldots, s_l\}$ 和正整数 $k$，如果索引的多重集 $\{i_1, \ldots, i_{2k}\}$ 包含每一个索引并且重数为偶数，那么称等式 $s_{i_1} \oplus \cdots \oplus s_{i_{2k}} = 0^n$ 是平凡的. 无论 $s_i$ 的值是什么，平凡等式始终成立. 如果对于 $k = 1, 2, 3$，唯一成立的恒等式 $s_{i_1} \oplus \cdots \oplus s_{i_{2k}} = 0^n$ 仅有这些平凡恒等式，那么称 $S$ 是好的.

        !!! note "Claim"
            在大小为 $l$ 的随机 $S$ 的选择上，除了至多 $l^6/2^n$ 的概率外，$S$ 都是好的.

            ??? note "Proof"
                至多只有 $l^6 + l^4 + l^2$ 个等式需要考虑，而只考虑非平凡等式的话，先消除掉其中所有的偶数次项，得到 2 或 4 或 6 个互异元素的等式，这样等式的总数量便是 $\binom{l}{6} + \binom{l}{4} + \binom{l}{2} \leqslant l^6$. 而对于单个非平凡等式，在随机 $S$ 上的选择，等式 $s_{i_1} \oplus \cdots \oplus s_{i_{2k}}$ 的值就是 $\{0, 1\}^n$ 中的随机元素，所以单个非平凡等式成立的概率为 $2^{-n}$，根据联合界得到该断言.

        因为 $S$ 不是好的概率非常小，所以接下来将仅在 $S$ 是好的条件下计算 $(S, U)$ 为强 Yes 实例的概率. 对于矩阵 $M$ 和子集 $\Delta$，记 $M_{[\Delta]}$ 为将 $M$ 的行和列限制在 $\Delta$ 上的主子矩阵. 令 $M^{S, U} = \Pi_S \cdot H^{\otimes n} \cdot \Pi_U \cdot H^{\otimes n} \cdot \Pi_S$. 注意到 $M^{S, U}$ 中所有由于 $x \not \in S$ 的行和列均为 $0$，所以此处稍微滥用记号，直接将 $M^{S, U}$ 视作 $H^{\otimes n} \cdot \Pi_U \cdot H^{\otimes n}$ 的子矩阵.

        完备性对应于表明 $M^{S, U}$ 的最大特征值 $\geqslant t_2$，为了证明这一点只需要构造状态 $\ket{\psi}$ 使得 $\bra{\psi} M^{S, U} \ket{\psi} \geqslant t_2$，使用的是 $S$ 上的均匀叠加态. 可靠性对应于证明对于任何满足 $\lvert \Delta \rvert \leqslant v$ 的子集 $\Delta \subseteq S$，$\lVert M^{S, U}_{[\Delta]} \rVert \leqslant t_1$.

        令 $M^S = \mathbb{E}_U [M^{S, U}]$，对基于$S$ 采样的 $U$ 求期望. 使用集中不等式来将 $M^{S, U}$ 及其主子矩阵的最大特征值和 $M^S$ 及其主子矩阵的最大特征值联系起来. 

        !!! note "Claim"
            1. 对所有 $S$，$\op{Pr}_U \left[ \max_{x, x'} \lvert M_{x, x'}^S - M_{x, x'}^{S, U} \rvert > \rho \right] \leqslant 2 l^2 e^{-\rho^2 2^n/2}$

            ??? note "Proof"
                固定 $S$，对于 $y \in \{0, 1\}^n$，记 $U_y$ 为 $y \in U$ 值为 $1$ 否则为 $0$ 的随机变量. 对于 $x, x' \in S$：

                \begin{align*}
                    M_{x, x'}^{S, U} & = \bra{x} H^{\otimes n} \Pi_U H^{\otimes n} \ket{x'} = \frac{1}{2^n} \sum_{y \in U} (-1)^{(x \oplus x') \cdot y} = \frac{1}{2^n} \sum_{y \in \{0, 1\}^n} (-1)^{(x \oplus x') \cdot y} U_y, \\
                    M_{x, x'}^S & = \mathbb{E}_U [M_{x, x'}^{S, U}] = \frac{1}{2^n} \sum_{y \in \{0, 1\}^n} (-1)^{(x \oplus x') \cdot y} \mathbb{E}_U[U_y].
                \end{align*}

                因为 $S$ 是固定的，$M_{x, x'}^{S, U}$ 是 $2^n$ 个独立随机变量的和，每个随机变量的范围为 $\{\pm 2^{-n}\}$，所以可以使用 Hoeffding 不等式来得到

                \[
                    \op{Pr}_U \left[\lvert M_{x, x'}^S - M_{x, x'}^{S, U} \rvert \geqslant \rho \right] \leqslant 2 e^{-rho^2 2^n/2}.
                \]

                对 $l^2$ 个对 $(x, x') \in S^2$ 应用联合界得到最终结果.

            2. 对任意 $S$，在选择 $U$ 的随机性上，除了至多 $2 l^2 e^{-\rho^2 2^n/2 l^2}$ 的概率之外，有

            \[
                \lVert M^{S, U} \rVert \geqslant \lVert M^S \rVert - \rho,
            \]

            并且对于任何子集 $\Delta \subseteq S$，

            \[
                \lVert M^{S, U}_{[\Delta]} \rVert \leqslant \lVert M^S_{[\Delta]} \rVert + \rho.
            \]

            ??? note "Proof"
                用 $\rho' = \rho/l$ 带入上述断言，即 $\lvert M_{x, x'}^S - M_{x, x'}^{S, U} \rvert \leqslant \rho' = \rho/l$，例外概率至多为 $2 l^2 e^{-\rho^2 2^n/2 l^2}$. 在此条件下，依据 Gershgorin 圆盘定理，对于任何子集 $\Delta \subseteq S$，$\lVert M^{S, U} - M^S \rVert \leqslant l \rho' = \rho$，且 $\lVert M^{S, U}_{[\Delta]} - M^S_{[\Delta]} \rVert \leqslant \lvert \Delta \rvert \rho' \leqslant l \rho' = \rho$. 接下来再使用三角不等式便可以得到断言.

        剩下的工作是给出 $\lVert M^S \rVert$ 的下界和 $\lVert M^S_{[\Delta]} \rVert$ 的上界. 为此，在正定半定（PSD）偏序下计算近似矩阵. 定义：

        \begin{align*}
            A_S &:= H^{\otimes n} \cdot \mathsf{Diag}\left[ \left(\frac{1}{2} + \frac{\kappa}{2} \gamma_y^{(S)} - \frac{\kappa^2}{4} (\gamma_y^{(S)})^2 \right)_y \right] \cdot H^{\otimes n} \\
            B_S &:= H^{\otimes n} \cdot \mathsf{Diag}\left[ \left(\frac{1}{2} + \frac{\kappa}{2} \gamma_y^{(S)} \right)_y \right] \cdot H^{\otimes n} \\
        \end{align*}

        其中记号 $\mathsf{Diag}[(f(y))_y]$ 表示对角矩阵，对于所有的 $y \in \{0, 1\}^n$，其 $(y, y)$ 对角元为 $f(y)$.

        !!! note "Claim"
            对于任意 $S$ 和任意子集 $\Delta \subseteq \{0, 1\}^n$（包括 $\Delta = \{0, 1\}^n$），有 $A^S_{[\Delta]} \preccurlyeq M^S_{[\Delta]} \preccurlyeq B^S_{[\Delta]}$，特别地，有 $\lVert A^S_{[\Delta]} \rVert \leqslant \lVert M^S_{[\Delta]} \rVert \leqslant \lVert B^S_{[\Delta]} \rVert$.

            ??? note "Proof"
                回忆 $\mathbb{E}_U [\Pi_U] = \mathsf{Diag}[(1 - \frac{1}{2} e^{-\kappa \gamma_y^{(S)}})_y]$. 运用 $e^{-x}$ 的 Taylor 展开，
                
                \[
                    \frac{1}{2} + \frac{\kappa}{2}x - \frac{\kappa^2}{4} x^2 \leqslant 1 - \frac{1}{2} e^{-\kappa x} \leqslant \frac{1}{2} + \frac{\kappa}{2}x.
                \]

                对于对角矩阵而言，由于半正定（PSD）偏序等价于其对角元素的序关系，因此

                \[
                    \mathsf{Diag}\left[ \left(\frac{1}{2} + \frac{\kappa}{2} \gamma_y^{(S)} - \frac{\kappa^2}{4} (\gamma_y^{(S)})^2 \right)_y \right] \preccurlyeq \mathsf{Diag}\left[ \left(1 - \frac{1}{2} e^{-\kappa \gamma_y^{(S)}} \right) \right] \preccurlyeq \mathsf{Diag}\left[ \left(\frac{1}{2} + \frac{\kappa}{2} \gamma_y^{(S)} \right)_y \right].
                \]

                而在变换 $M \mapsto C^\dagger M C$ 下半正定偏序得以保持，所以有 $A^S_{[\Delta]} \preccurlyeq M^S_{[\Delta]} \preccurlyeq B^S_{[\Delta]}$. 由于所有主子矩阵同样也保持半正定偏序，这便证明了断言.
        
        接下来将约束 $A^S$ 和 $B^S$ 以及它们的主子矩阵的最大特征值，进而得到 $M^S$ 的最大特征值. 对于所有好的多重集 $S$，其中的 $l$ 个元素都是互异的，并且对于其和集 $S \oplus S := \{x \oplus y : x, y \in S, x \neq y\}$，其中的元素也都是互异的. 

        **约束 $B^S$ 的最大特征值**：对于 $x \in \{0, 1\}^n$，设 $\delta_x$ 为 $x = 0^n$ 的指示函数. 可以得到

        \begin{align*}
            B^S_{x, x'} & = \frac{1}{2^n} \sum_y (-1)^{(x \oplus x') \cdot y} \left(\frac{1}{2} + \frac{\kappa}{2} \gamma_y^{(S)}\right) \\
            & = \frac{1}{2} \left(\frac{1}{2^n} \sum_y (-1)^{(x \oplus x') \cdot y}\right) + \frac{\kappa}{2 l} \left(\frac{1}{2^n} \sum_y (-1)^{(x \oplus x') \cdot y} \sum_{x_0, x_0' \in S} (-1)^{y \cdot (x_0 \oplus x_0')} \right) \\
            & = \frac{1}{2} \delta_{x \oplus x'} + \frac{\kappa}{2 l} \sum_{x_0, x_0' \in S} \delta_{x \oplus x' \oplus x_0 \oplus x_0'}
        \end{align*}

        对于对角元即 $x = x'$，有 $\delta_{x \oplus x'} = 1$，而 $\delta_{x \oplus x' \oplus x_0 \oplus x_0'} = 1$ 当且仅当 $x_0 = x_0'$，总共有 $l$ 种情况，所以对角元 $B^S_{x, x} = \frac{1}{2} + \frac{\kappa}{2}$. 对于非对角元即 $x \neq x'$，有 $\delta_{x \oplus x'} = 0$，而 $\delta_{x \oplus x' \oplus x_0 \oplus x_0'} = 1$ 当且仅当 $(x_0, x_0') = (x, x')$ 或 $(x_0, x_0') = (x', x)$，总共有 $2$ 种情况，所以非对角元 $B^S_{x, x'} = \frac{\kappa}{l}$. 

        进而可以简化 $B^S_{[\Delta]}$ 的表达形式：

        \[
            B^S_{[\Delta]} = \left(\frac{1}{2} + \frac{\kappa}{2} - \frac{\kappa}{l}\right) \mathrm{id}_\Delta + \frac{\kappa \lvert \Delta \rvert}{l} \ket{\Delta} \bra{\Delta},
        \]

        其中 $\ket{\Delta} := \frac{1}{\sqrt{\lvert \Delta \rvert}} \sum_{x \in \Delta} \ket{x}$ 是 $\Delta$ 上的均匀叠加态. 并且 $\ket{\Delta}$ 是 $B^S_{[\Delta]}$ 的最大特征向量，进而

        \[
            \lVert B^S_{[\Delta]} \rVert = \bra{\Delta} B^S_{[\Delta]} \ket{\Delta} = \frac{1}{2} + \frac{\kappa}{2} - \frac{\kappa}{l} + \frac{\kappa \lvert \Delta \rvert}{l} \leqslant \frac{1 + \kappa}{2} + \frac{\lvert \Delta \rvert \kappa}{l}.
        \]

        **约束 $A^S$ 的最大特征值**：因为存在 $\gamma_y^{(S)}$ 的二次项，计算会更复杂一些.

        \begin{align*}
            A^S_{x, x'} & = \frac{1}{2^n} \sum_y (-1)^{(x \oplus x') \cdot y} \left(\frac{1}{2} + \frac{\kappa}{2} \gamma_y^{(S)} - \frac{\kappa^2}{4} (\gamma_y^{(S)})^2\right) \\
            & = B^S_{x, x'} - \frac{\kappa^2}{4 l^2} \left(\frac{1}{2^n} \sum_y \sum_{x_0, x_0', x_1, x_1'} (-1)^{(x \oplus x') \cdot y} (-1)^{y \cdot (x_0 \oplus x_0')} (-1)^{y \cdot (x_1 \oplus x_1')} \right) \\
            & = B^S_{x, x'} - \frac{\kappa^2}{4 l^2} \sum_{x_0, x_0', x_1, x_1'} \delta_{x \oplus x' \oplus x_0 \oplus x_0' \oplus x_1 \oplus x_1'}.
        \end{align*}

        重点是计算最后一项. 对于对角元 $x = x'$，因为 $S$ 是好的，使得 $\delta_{x \oplus x' \oplus x_0 \oplus x_0' \oplus x_1 \oplus x_1'} = \delta_{x_0 \oplus x_0' \oplus x_1 \oplus x_1'}$ 非零的情况只有以下两种：

        - $x_0 = x_0'$ 且 $x_1 = x_1'$，总共有 $l^2$ 种情况；
        - $x_0 \neq x_0'$，且要么 $(x_0, x_0') = (x_1, x_1')$，要么 $(x_0, x_0') = (x_1', x_1)$，总共有 $2 l (l - 1)$ 种情况.

        所以共计 $3 l^2 - 2 l$ 种情况，对角元为

        \[
            A^S_{x, x} = B^S_{x, x} - \frac{\kappa^2}{4 l^2} (3 l^2 - 2 l) = \frac{1}{2} + \frac{\kappa}{2} - \frac{3 \kappa^2}{4} + \frac{\kappa^2}{2 l}.
        \]

        对于非对角元 $x \neq x'$，使得 $x \oplus x' \oplus x_0 \oplus x_0' \oplus x_1 \oplus x_1' = 0^n$ 的唯一方法是：$x_0, x_0', x_1, x_1'$ 中的一个元素是 $x$，一个元素是 $x'$，其余两个元素是相同的. 有 $ 4 \times 3$ 种方式选择 $x_0, x_0', x_1, x_1'$ 中的两个元素是 $x$ 和 $x'$，并且有 $l$ 种方式选择剩余的一对元素. 但这稍微有点重复计算，例如 $(x, x', x_0, x_0', x_1, x_1') = (x, x', x, x, x, x')$ 会被计算三次（对于 $x_0 = x, x_0' = x, x_1 = x$）. 这种形式的项总共有 $8$ 个，其中 $4$ 个在 $(x_0, x_0', x_1, x_1')$ 中有三个 $x$ 和一个 $x'$，另外 $4$ 个则是三个 $x'$ 和一个 $x$. 每个项都被额外算了两次，所以总项数为 $12 l - 16$，非对角元为

        \[
            A^S_{x, x'} = B^S_{x, x'} - \frac{\kappa^2}{4 l^2} (12 l - 16) = \frac{\kappa}{l} - \frac{3 \kappa^2}{l} + \frac{4 \kappa^2}{l^2}.
        \]

        类似于对 $B^S_{[\Delta]}$ 的分析，有

        \[
            A^S = \left[\frac{1}{2} + \kappa\left(\frac{1}{2} - \frac{1}{l}\right) - \kappa^2\left(-\frac{3}{4} + \frac{7}{2 l } - \frac{4}{l^2}\right)\right] \mathrm{id}_S + \left[\kappa - 3\kappa^2 + \frac{4 \kappa^2}{l}\right] \ket{S} \bra{S}.
        \]

        最大特征向量为 $\ket{S}$，所以

        \begin{align*}
            \lVert A^S \rVert &= \bra{S} A^S \ket{S} \\
            &= \frac{1}{2} + \kappa\left(\frac{3}{2} - \frac{1}{l} \right) + \kappa^2\left(-\frac{15}{4} + \frac{15}{2 l} - \frac{4}{l^2}\right) \\
            & \geqslant \frac{1}{2} + \frac{3 \kappa}{2} - \frac{15 \kappa^2}{4} - \frac{5 \kappa}{l}.
        \end{align*}

        将谱范数界和 Hoeffding 不等式结合便可以证明.

## Quantum mechanics of bosons

### A natural basis

玻色子（位置） Fock 基底是一组形如 $\ket{l_0, l_1, \ldots, l_{2^n - 1}}$ 的正交归一态，其中 $l_x \in \mathbb{Z}_{\geq 0}$ 表示在模式 $x$ 中的粒子数. 玻色子总数为 $\sum_x l_x$.

### The second quantization

定义 $\ket{\text{vac}} := \ket{0, 0, \ldots, 0}$ 为真空态，代表系统中存在 $0$ 个玻色子. 设 $\hat{a}_x$ 和 $\hat{a}_x^\dagger$ 分别为模式 $x$ 的湮灭算子和产生算子，它们对位置 Fock 基底的作用如下：

\begin{align*}
    \hat{a}_x \ket{l_0, l_1, \ldots, l_x, \ldots, l_{2^n - 1}} &= \sqrt{l_x} \ket{l_0, l_1, \ldots, l_x - 1, \ldots, l_{2^n - 1}}, \\
    \hat{a}_x^\dagger \ket{l_0, l_1, \ldots, l_x, \ldots, l_{2^n - 1}} &= \sqrt{l_x + 1} \ket{l_0, l_1, \ldots, l_x + 1, \ldots, l_{2^n - 1}}.
\end{align*}

但这些算子不是酉的.

依据位置产生算子的定义有

\[
    \frac{1}{\sqrt{\prod_{x = 0}^{2^n - 1} l_x!}} \prod_{x = 0}^{2^n - 1} (\hat{a}_x^\dagger)^{l_x} \ket{\text{vac}} = \ket{l_0, l_1, \ldots, l_{2^n - 1}}.
\]

玻色子位置算子的对易关系由下式给出

\[
    [\hat{a}_x, \hat{a}_y^\dagger] = \hat{a}_x \hat{a}_y^\dagger - \hat{a}_y^\dagger \hat{a}_x = \delta_{xy}, \quad [\hat{a}_x, \hat{a}_y] = [\hat{a}_x^\dagger, \hat{a}_y^\dagger] = 0.
\]

### A momentum basis

通过 Hadamard 变换在动量基底中定义湮灭算子和产生算子，但这是计算机科学层面的解读. 通常而言，位置基底到动量基底的变换是由群 $\mathbb{Z}_{2^n}$ 上的 QFT 给出的. 

\begin{align*}
    \tilde{a}_y &:= \frac{1}{\sqrt{2^n}} \sum_{x \in \{0, 1\}^n} (-1)^{x \cdot y} \hat{a}_x, \\
    \tilde{a}_y^\dagger &:= \frac{1}{\sqrt{2^n}} \sum_{x \in \{0, 1\}^n} (-1)^{x \cdot y} \hat{a}_x^\dagger.
\end{align*}

动量算子的对易关系可以从位置算子的推导出：

\[
    [\tilde{a}_x, \tilde{a}_y^\dagger] = \tilde{a}_x \tilde{a}_y^\dagger - \tilde{a}_y^\dagger \tilde{a}_x = \delta_{xy}, \quad [\tilde{a}_x, \tilde{a}_y] = [\tilde{a}_x^\dagger, \tilde{a}_y^\dagger] = 0.
\]

进而便可以推导出存在动量 Fock 基底，其也是形如 $\ket{l_0, l_1, \ldots, l_{2^n - 1}}$ 的正交归一态，其中 $l_y \in \mathbb{Z}_{\geq 0}$ 表示在动量模式 $y$ 中的粒子数. 

### Number operators

定义位置和动量的数量算子 $\hat{n}_x := \hat{a}_x^\dagger \hat{a}_x$ 和 $\tilde{n}_x := \tilde{a}_x^\dagger \tilde{a}_x$. 它们分别在位置 Fock 基底和动量 Fock 基底下为对角矩阵，其作用是将一个 Fock 基底乘以第 $x$ 个模式的粒子数，例如 $\hat{n}_0 \ket{l_0, l_1, \ldots, l_{2^n - 1}} = l_0 \ket{l_0, l_1, \ldots, l_{2^n - 1}}$. 其与产生和湮灭算子的对易关系为

\begin{align*}
    \hat{n}_x \hat{a}_x &= \hat{a}_x^\dagger \hat{a}_x \hat{a}_x = (\hat{a}_x \hat{a}_x^\dagger - 1) \hat{a}_x = \hat{a}_x (\hat{a}_x^\dagger \hat{a}_x - 1) = \hat{a}_x (\hat{n}_x - 1), \\
    \hat{n}_x \hat{a}_x^\dagger &= \hat{a}_x^\dagger \hat{a}_x \hat{a}_x^\dagger = \hat{a}_x^\dagger (1 + \hat{a}_x^\dagger \hat{a}_x) = \hat{a}_x^\dagger (\hat{n}_x + 1).
\end{align*}

总粒子数算子定义为 $\hat{N} := \sum_x \hat{n}_x$，易知 $\hat{N} = \tilde{N}$.

### A random bosonic setup

经典组合学中的一个典型问题可能会以将 $l$ 个不可分辨的球均匀地放入 $N$ 个箱子开始，其量子解释为将 $l$ 个玻色子均匀地放入 $N = 2^n$ 个模式中. 该设定的一种精确纯化是考虑有 $l$ 个玻色子处于 $0$-动量模式，其等于

\[
    \frac{1}{\sqrt{l!}} (\tilde{a}_0^\dagger)^l \ket{\text{vac}} = \frac{1}{\sqrt{l! \cdot 2^{nl}}} \sum_{x_1, \ldots, x_l} \left( \prod_{i = 1}^l \hat{a}_{x_i}^\dagger \right) \ket{\text{vac}}.
\]

因为玻色子是全同的，所以需要引入 $\sqrt{l!}$ 的归一化因子. 假设在位置 Fock 基底下测量该态，并将测量结果解释为一个多重集，那么得到一个包含元素 $x$ 达 $l_x$ 次的特定多重集 $S$ 的概率为

\[
    \Pr{S} = \frac{l!}{2^{nl} \prod_x l_x!},
\]

这恰好是大小为 $l$ 的多重集上的均匀分布.

### Bosonic Hilbert space

$2^n$ 个模式上的玻色子是处于无限维 Hilbert 空间中的状态，因为玻色子系统的玻色子数量并没有限制. 但可以通过限制到固定数量的玻色子，将该 Hilbert 空间表示为有限维 Hilbert 空间的直和：

\[
    \mathcal{H}_{\text{boson}} = \bigoplus_{l = 0}^{\infty} \mathcal{H}_{\text{boson}}^{(l)}, \quad \mathcal{H}_{\text{boson}}^{(l)} := \operatorname{span} \left\{ \ket{l_0, l_1, \ldots, l_{2^n - 1}} : \sum_x l_x = l \right\}.
\]

因为总粒子数算子 $\hat{N} = \tilde{N}$，所以在位置和动量基底下的玻色子数量是相同的；因此，位置 Fock 基底和动量 Fock 基底之间的变换映射，即 Hadamard 变换对于该直和分解是分块对角的.

此工作中讨论的范围为固定拥有 $l$ 个玻色子的玻色子系统，所以状态均处于 $\mathcal{H}_{\text{boson}}^{(l)}$ 中. 该空间的位置和动量 Fock 基底都可以由长度为 $2^n$ 且总和为 $l$ 的非负整数元组进行索引，而这和大小为 $l$ 的多重集 $S$ 的真值表集合是同构的. 在剩余部分中，状态 $\ket{\mathsf{tt}_S}$ 等同于由 $S$ 的元素给出玻色子所处位置的位置 Fock 基底态.

## Sampler upper bound statement and organization

### Theorem statement

主定理如下：

!!! note "Theorem(Sampling probability upper bound)"
    对于所有的 $v$，所有访问谕示机 $U$，输出 $v$ 个互异输出，且每次输出进行 $t$ 次查询的量子算法 $\mathcal{A}^U$，如果谕示机对 $(S, U)$ 按照 Strong 分布进行采样，那么 $\mathcal{A}^U$ 输出的 $v$ 个互异输出均属于 $S$ 的概率至多为

    \[
        2 \left( \frac{4 v ((vt)^{30} + v(vt)^{20}) \sqrt{l} }{2^{n/4} } \right)^v + \left( \left( \frac{(vt)^4}{l^{1/32} } \right)^v + e^{-5vt} \right)^2.
    \]

    !!! tip "Remark"
        本定理中各项指数并不重要，只是粗略放缩的结果. 关键是对于 $v, t = \op{poly}(n)$，且 $l = 2^{cn}$，分子是显著小于分母的. 因此随着 $v$ 的增长，该数值呈指数级迅速递减.

        实际上会证明一个稍强的命题，即为“首先向谕示机 $U$ 进行 $T$ 次查询，然后输出 $v$ 个猜测”的任意算法给出界. 在 $T = vt$ 的情况下，这是一类比“每次猜测进行 $t$ 次查询”的算法严格更广泛的算法类. 研究这种更强模型的合理性在于，它能自然地处理算法在不同猜测之间的记忆的复杂度.

### Proof overview and intuition

证明将定义一族由正整数 $r$ 和 $o$ 索引的子空间 $\{\mathsf{QEC}_{(r, o)}\}$，其满足如下性质：如果进行 $T$ 次查询后的状态大部分包含在 $\mathsf{QEC}_{(r, o)}$ 中（其中 $r \leqslant \op{poly}(n)$ 且 $o \leqslant v/4$），那么猜测算法的成功概率界就足以证明定理. 一旦确立了支撑在子空间 $\mathsf{QEC}_{(r, o)}$ 上的状态具有较低的采样成功概率，接下来便将证明，所有对纯化后的 $(S, U)$ 谕示机进行 $T$ 次查询的查询算法，其状态几乎完全支撑在 $\mathsf{QEC}_{(r, o)}$ 上（其中 $r$ 关于 $T$ 呈多项式阶关系）. 将这些结合起来，便得到了采样概率的上界.

记号 $\mathsf{QEC}_{(r, o)}$ 指代称为 **$(r, o)$-准偶凝聚态** 的空间. 非正式地说，$(r, o)$-准偶凝聚态是动量 Fock 态生成的空间中的一个状态，其中奇数数量算子的数量 $\leqslant o$，且非零的动量模式的数量至多为 $r$.

## Sampler upper bounds for quasi-even condensates

回想一下，更宏观的目标是证明查询算法在源自 Strong 分布的随机实例上的成功概率上界，可以设想该查询算法被分为了两个步骤：

1. 与谕示机 $U$ 进行交互的 $T$ 次查询；
2. 对猜测结果与 $S$ 关系的测量.

与 $(S, U) \sim \mathsf{Strong}$ 的交互可以通过纯化谕示机上的分布，并在叠加态中与每个对 $(S, U)$ 进行相干交互来进行研究. 这里的纯化是指对谕示机 $U$ 的查询被替换为以下酉变换的线性扩展：

\[
    \ket{b, x, y} \ket{\mathsf{tt}_S} \ket{\mathsf{tt}_U} \mapsto (-1)^{b \cdot U(y)} \ket{b, x, y} \ket{\mathsf{tt}_S} \ket{\mathsf{tt}_U}.
\]

其中 $\mathsf{tt}_{(\cdot)}$ 是相对应谕示机的真值表的记号. 检查算法输出的 $v$ 个猜测等价于测量算法与谕示机的最终纠缠状态，所采用的投影测量算子为：

\[
    \Pi_{\mathrm{succ} } := \sum_{z_1, \ldots, z_v \in (\{0, 1\}^n)^v \text{ and distinct} } \ket{z_1, \ldots, z_v} \bra{z_1, \ldots, z_v} \otimes \sum_{S: z_1, \ldots, z_v \in S} \ket{\mathsf{tt}_S} \bra{\mathsf{tt}_S}.
\]

该采样器在随机谕示机 $(S, U)$ 的分布上的成功概率等于在纯化后的谕示机上运行采样器后，使用 $\Pi_{\mathrm{succ}}$ 对后查询状态进行测量时被接受的概率. 接下来定义 $(r, o)$-准偶凝聚态.

!!! info "Definition(Quasi-even condensates)"
    令 $u = (u_x)_{x \in \{0, 1\}^n}$ 为一个满足 $\sum_x u_x = l$ 的非负整数元组，其代表一个包含 $l$ 个玻色子的动量 Fock 态. 如果满足以下条件，则称 $u$ 描述了一个 $(r, o)$-准偶凝聚态：

    1. (Condensate): $u_0 \geqslant l - r$，即绝大多数玻色子都处于 $0$-动量模式；
    2. (Quasi-even): 除 $u_0$ 外，至多有 $o$ 个 $u_x$ 是奇数.

    定义 $(r, o)$-准偶凝聚态为处于与准偶凝聚态元组相对应的由动量 Fock 态生成的空间中的任意状态，即 $\op{span}\{\ket{u} : u \text{ 是 } (r, o)\text{-准偶凝聚态元组}\}$. 定义 $\mathsf{QEC}_{(r, o)}$ 为指向该空间的投影算子. 此外，定义 $\mathsf{Con}_r$ 和 $\mathsf{QE}_o$ 分别为指向 $r$-凝聚态和 $o$-准偶态的投影算子. $\mathsf{QE}_{=o}$ 和 $\mathsf{QE}_{\geqslant o}$ 分别为指向恰好 $o$ 个奇数 $u_x$ 和至少 $o$ 个奇数 $u_x$ 的状态的投影算子. 所有这些投影算子在动量 Fock 态基底下都是对角矩阵，因此它们相互对易，依据定义有

    \[
        \mathsf{QEC}_{(r, o)} = \mathsf{Con}_r \cdot \mathsf{QE}_o = \mathsf{QE}_o \cdot \mathsf{Con}_r.
    \]

    !!! tip "Remark"
        所有先前定义的投影算子都要求状态中正好有 $l$ 个玻色子. 在此子空间下，$\mathsf{Con}_0$ 指向“所有 $l$ 个玻色子均处于 $0$-动量模式”的状态（即 $\ket{l, 0, \ldots, 0}$），$\mathsf{Con}_l$ 指向所有包含 $l$ 个玻色子的状态.

!!! note "Theorem(Quasi-even condensate probability upper bound)"
    令 $\Pi_\mathrm{succ}$ 为前文定义的成功测量算子，且 $\mathsf{QEC}_{(r, v/4)}$ 是指向 $(r, v/4)$-准偶凝聚态的投影算子，其仅作用在 $S$ 寄存器上. 则

    \[
        \lVert \mathsf{QEC}_{(r, v/4)} \cdot \Pi_\mathrm{succ} \cdot \mathsf{QEC}_{(r, v/4)} \rVert \leqslant 2 \left( \frac{4 v (r^3 + vr^2) \sqrt{l} }{2^{n/4} } \right)^v.
    \]

    ???+ note "Proof"
        证明该定理所需的关键引理如下，它给出了一个处于准偶凝聚态的系统在进行 $v$ 个互异的猜测 $z_1, \ldots, z_v$ 时成功概率的上界. 直观上，该引理有些奇怪，因为它计算的是准偶凝聚态空间上数量算子之积的最大特征值，但接下来会证明其足以用于在准偶凝聚态空间中证明 $\Pi_\mathrm{succ}$ 的最大特征值上界. 该证明依赖于引理中证明的上界与猜测位置的选择无关这一事实.

        !!! success "Lemma"
            对互异的坐标 $z_1, \ldots, z_v \in \{0, 1\}^n$，有

            \[
                \lVert \mathsf{QEC}_{(r, v/4)} \cdot \hat{n}_{z_1} \cdots \hat{n}_{z_v} \cdot \mathsf{QEC}_{(r, v/4)} \rVert \leqslant 2 \left( \frac{4 (r^3 + vr^2) \sqrt{l} }{2^{n/4} } \right)^v.
            \]

            ???+ success "Proof"
                Hermitian 矩阵的谱范数的一个上界是所有行中最大的 $1$-范数. 目标是在准偶凝聚态空间中研究 $\hat{n}_{z_1} \cdots \hat{n}_{z_v}$，所以着重考虑动量 Fock 基底中由 $u$ 索引的行，其中 $u$ 是一个 $(r, o)$-准偶凝聚态元组. 目标是约束

                \begin{align*}
                    & \sum_{(r, o)\text{-QEC tuple } w} \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert \\ &= \sum_{d \geqslant 0} \left( \sum_{(r, o)\text{-QEC tuple } w \text{ and } \lvert w - u \rvert = 2d} \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert \right) \\
                    & \leqslant \sum_{d \geqslant 0} \left( \max_{(r, o)\text{-QEC tuple } w \text{ and } \lvert w - u \rvert = 2d} \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert \right) \cdot \text{#} \{w: (r, o)\text{-QEC tuple and } \lvert w - u \rvert = 2d\}. \\
                \end{align*}

                将利用另外两个断言来约束上述方程中的各项. 第一个是对与固定元组 $u$ 的距离为 $2d$ 的元组 $w$ 所对应的矩阵元的估计.

                !!! note "Claim"
                    固定两个 $(r, o)$-准偶凝聚态元组 $u$ 和 $w$，满足 $\lvert w - u \rvert = 2d$ 且 $l \geqslant 2d$，那么对于所有互异的 $z_1, \ldots, z_v$，以下结论成立：

                    \[
                        \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert \leqslant \begin{cases}
                        v!(2 r)^{v + d/2} \frac{l^{v - d/2}}{2^{n v}} & \text{if } d \leqslant v, \\
                        0 & \text{if } d > v.
                        \end{cases}
                    \]

                    ??? note "Proof"
                        回忆 $\hat{a}_{z_i} = \frac{1}{\sqrt{2^n}} \sum_w (-1)^{z_i \cdot w} \tilde{a}_w$，所以

                        \begin{align*}
                            \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert &= \lvert \bra{w} \hat{a}_{z_1}^\dagger \cdots \hat{a}_{z_v}^\dagger \hat{a}_{z_1} \cdots \hat{a}_{z_v} \ket{u} \rvert \\
                            &= \left\lvert \frac{1}{(2^n)^v} \sum_{\alpha_1, \ldots, \alpha_v} \sum_{\beta_1, \ldots, \beta_v} \left( \prod_{i = 1}^v (-1)^{z_i \cdot (\alpha_i \oplus \beta_i)} \right) \bra{w} \tilde{a}_{\alpha_1}^\dagger \cdots \tilde{a}_{\alpha_v}^\dagger \tilde{a}_{\beta_1} \cdots \tilde{a}_{\beta_v} \ket{u} \right\rvert \\
                            & \leqslant \frac{1}{(2^n)^v} \sum_{\alpha_1, \ldots, \alpha_v} \sum_{\beta_1, \ldots, \beta_v} \lvert \bra{w} \tilde{a}_{\alpha_1}^\dagger \cdots \tilde{a}_{\alpha_v}^\dagger \tilde{a}_{\beta_1} \cdots \tilde{a}_{\beta_v} \ket{u} \rvert.
                        \end{align*}

                        首先，如果 $d > v$，那么式子中的每一项对应于：从准偶凝聚态开始，在动量模式 $\beta_1, \ldots, \beta_v$ 上各减 $1$，然后在动量模式 $\alpha_1, \ldots, \alpha_v$ 上各加 $1$. 此外，当且仅当它们能够对应于一系列将 $u$ 映射到 $w$ 的相继加减操作时，该项才不为 $0$. 而 $u$ 和 $w$ 相差 $2d > 2v$，因此不存在 $v$ 次相继加操作 $\alpha_1, \ldots, \alpha_v$ 和 $v$ 次相继减操作 $\beta_1, \ldots, \beta_v$ 能够将 $u$ 映射到 $w$. 因此求和中的每一项都严格为 $0$.

                        现在考虑 $d \leqslant v$ 的情况. 固定一组 $\alpha_1, \ldots, \alpha_v$ 和 $\beta_1, \ldots, \beta_v$，并考虑以下这一项
                        
                        \[
                            \lvert \bra{w} \tilde{a}_{\alpha_1}^\dagger \cdots \tilde{a}_{\alpha_v}^\dagger \tilde{a}_{\beta_1} \cdots \tilde{a}_{\beta_v} \ket{u} \rvert.
                        \]

                        只有当从 Fock 态 $u$ 湮灭模式 $\beta_1, \ldots, \beta_v$ 中的玻色子，并在模式 $\alpha_1, \ldots, \alpha_v$ 中产生玻色子时，才能得到 $w$，否则该项为 $0$. 将湮灭算子作用于模式 $z$ 时，状态的模长在乘性上增加至多 $\sqrt{u_z}$，$u_z$ 为 $\ket{u}$ 中 $z$ 模式的粒子数. 并且，只要 $z \neq 0$，就有 $u_z \leqslant r$.

                        而 $u$ 和 $w$ 都是包含 $l$ 个玻色子的状态，所以它们的 $0$-动量模式的差异至多为总差异的一半. 因为 $w$ 和 $u$ 的差异为 $2d$，所以它们在非 $0$-动量模式的差异至少为 $d$，也就是说在 $\{\tilde{a}_{\beta_i}\}_i$ 和 $\{\tilde{a}_{\alpha_i}^\dagger\}_i$ 中至少有 $d$ 个算子是作用在非 $0$-动量模式上的，至多有 $2v - d$ 个算子是作用在 $0$-动量模式上的. 因此该项的模长限制为

                        \[
                            \lvert \bra{w} \tilde{a}_{\alpha_1}^\dagger \cdots \tilde{a}_{\alpha_v}^\dagger \tilde{a}_{\beta_1} \cdots \tilde{a}_{\beta_v} \ket{u} \rvert \leqslant l^{v - d/2} r^{d/2}.
                        \]

                        最终需要约束求和中非零项的项数. 首先注意到对求和式中对应非零项的 $\beta_1, \ldots, \beta_v$ 的选择数量约束在 $(r + 1)^v$ 上，因为若 $\tilde{a}_{\beta_i}$ 作用在 $u$ 未占据的模式上，就会将其映射为 $0$，而 $u$ 至多占据 $r + 1$ 个动量模式.

                        而对于固定的 $u, w$ 以及 $\{\tilde{a}_{\beta_i}\}_i$，存在唯一的产生算子多重集 $\{\tilde{a}_{\alpha_i}^\dagger\}_i$，使得 $\lvert \bra{w} \tilde{a}_{\alpha_1}^\dagger \cdots \tilde{a}_{\alpha_v}^\dagger \tilde{a}_{\beta_1} \cdots \tilde{a}_{\beta_v} \ket{u} \rvert \neq 0$. 而 $\{\alpha_1, \ldots, \alpha_v\}$ 的排列数量至多为 $v!$，进而有

                        \begin{align*}
                            \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert & \leqslant \frac{1}{2^{nv} } \sum_{\alpha_1, \ldots, \alpha_v} \sum_{\beta_1, \ldots, \beta_v} \lvert \bra{w} \tilde{a}_{\alpha_1}^\dagger \cdots \tilde{a}_{\alpha_v}^\dagger \tilde{a}_{\beta_1} \cdots \tilde{a}_{\beta_v} \ket{u} \rvert \\
                            & \leqslant \frac{1}{2^{nv} } l^{v - d/2} r^{d/2} \sum_{\alpha_1, \ldots, \alpha_v} \sum_{\beta_1, \ldots, \beta_v} \delta(\lvert \bra{w} \tilde{a}_{\alpha_1}^\dagger \cdots \tilde{a}_{\alpha_v}^\dagger \tilde{a}_{\beta_1} \cdots \tilde{a}_{\beta_v} \ket{u} \rvert \neq 0) \\
                            & \leqslant \frac{1}{2^{nv} } l^{v - d/2} r^{d/2} v! (r + 1)^v \\
                            & \leqslant v! (2 r)^{v + d/2} \frac{l^{v - d/2}}{2^{nv}}.
                        \end{align*}


                第二个是对所有 $d$ 值下，与初始准偶凝聚态 $u$ 的距离恰好为 $2d$ 的准偶凝聚态 $w$ 的数量的上界估计.

                !!! note "Claim"
                    对于每个 $(r, o)$-准偶凝聚态元组 $u$ 和 $d \geqslant 0$，与 $u$ 的距离恰好为 $2d$ 的 $(r, o)$-准偶凝聚态元组 $w$ 的数量被以下上界所控制：

                    \[
                        (2^{n + 1})^{d/2 + o} (r + 1 + d/2 + o)^{d/2 + o}.
                    \]

                    ??? note "Proof"
                        首先定义一个有关带约束的放球入箱的计数问题，然后表明该问题的答案给出了于 $u$ 距离为 $d$ 的 $(r, o)$ 准偶凝聚态数量的一个上界，并进一步证明其被断言给出的上界所约束.

                        **定义计数问题**：对于每个元组 $u$，定义 $\op{pos}(u)$ 为 $u$ 中具有非零分量的索引. 考虑的计数问题是将球分配到 $2^n$ 个箱子的方法数，并需要满足以下条件：

                        1. 每个球标有整数 $\red{-2}, \red{-1}, \blue{+1}, \blue{+2}$ 中的一个，且相同标签的球是全同的.
                        2. 恰好有 $\lfloor d/2 \rfloor$ 个 $\blue{+2}$ 球和 $\lfloor d/2 \rfloor$ 个 $\red{-2}$ 球，以及 $o$ 个 $\blue{+1}$ 球和 $o$ 个 $\red{-1}$ 球.
                        3. 对于 $\op{pos}(u)$ 之外的任何箱子，放置在该箱子中的球的标签之和必须 $\geqslant 0$.

                        通过构造一个从准偶凝聚态到分配方案的单射，来证明球到箱子的分配方案数是与给定准偶凝聚态 $u$ 的距离为 $2d$ 的准偶凝聚态数量的一个上界.

                        **构造单射映射**：固定一个与 $u$ 距离为 $2d$ 的准偶凝聚态 $w$，定义 $e = w - u$ 为 $w$ 和 $u$ 之间的逐分量之差，因为 $u$ 和 $w$ 具有相同数量的玻色子，所以 $e$ 各分量之和为 $0$. 将 $e$ 分解为正负分量：

                        \[
                            e = e^+ - e^-, \quad e^+ \geqslant 0, e^- \geqslant 0.
                        \]

                        定义 $e_\mathrm{even} := 2(\lfloor e^+/2 \rfloor - \lfloor e^-/2 \rfloor)$，$e_\mathrm{odd} := e - e_\mathrm{even}$. 对于任何分量 $e_x$，有

                        \[
                            (e_\mathrm{odd})_x = \begin{cases}
                            0, & \text{ if} x \text{ is even,} \\
                            \op{sgn}(e_x), & \text{ if} x \text{ is odd.}
                            \end{cases}
                        \]

                        因为是从两个准偶凝聚态开始的，所以 $e_\mathrm{odd}$ 中的非零分量数至多为 $2 o$. 而 $\lvert e_\mathrm{even} \rvert \leqslant 2 \lfloor d/2 \rfloor$，所以如果 $d$ 不是偶数，那么 $e_\mathrm{even}$ 对 $u$ 和 $w$ 之间距离的贡献仅仅为 $d - 1$.

                        现在考虑以下将球分配到箱子的方案. 不失一般性，假设 $e_\mathrm{even}$ 的各分量之和 $\leqslant 0$.

                        1. 对于每个箱子 $x$，如果 $(e_\mathrm{even})_x \geqslant 0$，则将 $(e_\mathrm{even})_x / 2$ 个 $\blue{+2}$ 球放入该箱子；如果 $(e_\mathrm{even})_x < 0$，则将 $(e_\mathrm{even})_x / 2$ 个 $\red{-2}$ 球放入该箱子.

                        2. 令 $b_+$ 和 $b_-$ 为前一步分配的 $\blue{+2}$ 和 $\red{-2}$ 球的总数，有 $b_+ \leqslant b_-$. 将剩余的 $\lfloor d/2 \rfloor - b_-$ 个 $\blue{+2}$ 球和相同数量的 $\red{-2}$ 球放入第 $0$ 个箱子中，这分配了所有的 $\red{-2}$ 球.

                        3. $b_\mathrm{rem} := b_- - b_+$ 为尚未分配的 $\blue{+2}$ 球，向 $e_\mathrm{odd}$ 中前 $b_\mathrm{rem}$ 个 $+1$ 分量对应的箱子中放置一个 $\blue{+2}$ 球，然后将对应分量改为 $-1$，这样得到的新向量称为 $e_\mathrm{balanced}$.

                        4. 此时 $e_\mathrm{balanced}$ 是一个分量仅为 $\{-1, 0, +1\}$，分量和为 $0$ 并且至多有 $2 o$ 个非零分量的向量. 所以 $e_\mathrm{balanced}$ 含有至多 $o' \leqslant o$ 个 $+1$ 分量以及 $o'$ 个 $-1$ 分量. 将每个 $+1$ 分量对应的箱子中放置一个 $\blue{+1}$ 球，将每个 $-1$ 分量对应的箱子中放置一个 $\red{-1}$ 球. 剩余的 $o - o'$ 个 $\blue{+1}$ 球和 $o - o'$ 个 $\red{-1}$ 球放入第 $0$ 个箱子中.

                        可以验证这是一个有效的分配方案，并且利用每个箱子中球的标签之和便可以恢复出误差向量 $e = w - u$. 而对于任意两个不同的准偶凝聚态 $w, w'$，这一误差向量不可能相同，所以分配方案和准偶凝聚态之间是单射关系.

                        **约束组合恒等式**：使用隔板法来约束分配数，可以采取以下方法进行放大估算：

                        (a) 将 $\blue{+2}$ 球和 $\blue{+1}$ 球放入 $2^n - 1$ 个箱子中；

                        (b) 将 $\red{-2}$ 球和 $\red{-1}$ 球放入对应于 $\op{pos}(u)$ 的 $r + 1$ 个箱子，以及 (a) 中 $\blue{+2}$ 和 $\blue{+1}$ 球所在的至多 $d/2 + o$ 个箱子中.

                        \begin{align*}
                            (a) & \leqslant \binom{d/2 + k + 2^n}{d/2, k, 2^n} = \frac{(d/2 + k + 2^n)!}{(d/2)! k! (2^n)!} \leqslant (2^{n + 1})^{d/2 + k} \leqslant (2^{n + 1})^{d/2 + o}, \\
                            (b) & \leqslant \binom{r + 1 + d/2 + o}{r + 1, d/2, o} \leqslant (r + 1 + d/2 + o)^{d/2 + o}.
                        \end{align*}

                        将二者相乘便得到了上界.

                从而有

                \begin{align*}
                    & \sum_{(r, o)\text{-QEC tuple } w} \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert \\ 
                    &\leqslant \sum_{d \geqslant 0} \left( \max_{(r, o)\text{-QEC tuple } w \text{ and } \lvert w - u \rvert = 2d} \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert \right) \cdot \text{#} \{w: (r, o)\text{-QEC tuple and } \lvert w - u \rvert = 2d\} \\
                    &\leqslant v! (2 r)^v \sum_{d = 0}^{v} (2 r)^{d/2} \frac{l^{v - d/2}}{(2^n)^v} ((2^{n + 1})^{d/2 + o} (r + 1 + d/2 + o)^{d/2 + o}) \\
                    & \leqslant v! (2 r)^{3v/2} \left( \frac{l}{2^n} \right)^v (2^{n + 1})^o \sum_{d = 0}^{v} \left( \sqrt{\frac{2^{n + 1} }{l} } \right)^d (r + 1 + v/2 + o)^{d/2 + o} \\
                    & \leqslant v! (2 r)^{3v/2} \left( \frac{l}{2^n} \right)^v (2^{n + 1})^o (r + 1 + v/2 + o)^o \sum_{d = 0}^{v} \left( \frac{2^{n + 1} }{l} (r + 1 + v/2 + o) \right)^{d/2} \\
                    & \leqslant \frac{v! (2 r)^{3v/2} }{2^{o - 1} } \frac{l^v}{(2^n)^{v - o} } \left( \frac{2^{n + 1} }{l} (r + 1 + v/2 + o) \right)^{v/2} \\
                    & = 2^{2v - o + 1} v! r^{3v/2} (r + 1 + v/2 + o)^{v/2 + o} \frac{l^{v/2} }{(2^n)^{v / 2 - o} } \\
                \end{align*}

                因为 $\frac{2^{n + 1} }{l} (r + 1 + v/2 + o) \geqslant 2$，所以这个几何级数求和不会超过其最大项的 $2$ 倍.

                设置 $o = v/4$，便可以得到

                \begin{align*}
                    \lVert \mathsf{QEC}_{(r, o)} \cdot \hat{n}_{z_1} \cdots \hat{n}_{z_v} \cdot \mathsf{QEC}_{(r, o)} \rVert &\leqslant \max_{(r, o)\text{-QEC tuple } u} \sum_{(r, o)\text{-QEC tuple } w} \lvert \bra{w} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{u} \rvert \\
                    &\leqslant 2^{7v/4 + 1} v! r^{3v/2} (r + 1 + 3v/4)^{3v/4} \frac{l^{v/2} }{(2^n)^{v/4} } \\
                    &\leqslant 2 \left( \frac{4 v (r^3 + vr^2) \sqrt{l} }{2^{n/4} } \right)^v.
                \end{align*}

                使用了粗略的上界缩放，如 $r^{3/2} \leqslant r^2$ 和 $3v/4 + 1 \leqslant v$ 消去了表达式中的常数因子.

        证明该引理蕴含定理. 重写成功投影算子为

        \[
            \Pi_\mathrm{succ} = \sum_{z_1, \ldots, z_v \in (\{0, 1\}^n)^v \text{ and distinct} } \ket{z_1, \ldots, z_v} \bra{z_1, \ldots, z_v} \otimes \Pi_{z_1, \ldots, z_v},
        \]

        其中 $\Pi_{z_1, \ldots, z_v}$ 定义为指向“在位置模式 $z_1, \ldots, z_v$ 中至少有一个玻色子”的状态 $\ket{\mathsf{tt}_S}$ 的投影算子. 注意到对于互异的 $z_1, \ldots, z_v$，因为湮灭算子是对易的，所以有

        \[
            \hat{a}_{z_1}^\dagger \cdots \hat{a}_{z_v}^\dagger \hat{a}_{z_1} \cdots \hat{a}_{z_v} = \hat{n}_{z_1} \cdots \hat{n}_{z_v} \succcurlyeq \Pi_{z_1, \ldots, z_v}.
        \]

        这一命题在概念上等价于应用 Markov 不等式，即对于非负随机变量 $X$，有 $\Pr{X \geqslant 1} \leqslant \mathbb{E}[X]$. 因此有

        \[
            \lVert \mathsf{QEC}_{(r, v/4)} \cdot \Pi_\mathrm{succ} \cdot \mathsf{QEC}_{(r, v/4)} \leqslant \lVert \mathsf{QEC}_{(r, v/4)} \cdot \Lambda_\mathrm{succ} \cdot \mathsf{QEC}_{(r, v/4)} \rVert,
        \]

        其中 $\Lambda_{\mathrm{succ} } := \sum_{z_1, \ldots, z_v \in (\{0, 1\}^n)^v \text{ and distinct} } \ket{z_1, \ldots, z_v} \bra{z_1, \ldots, z_v} \otimes (\hat{a}_{z_1}^\dagger \cdots \hat{a}_{z_v}^\dagger \hat{a}_{z_1} \cdots \hat{a}_{z_v})$.

        接下来应用引理证明上界：

        \[
            \lVert \mathsf{QEC}_{(r, v/4)} \cdot \Lambda_\mathrm{succ} \cdot \mathsf{QEC}_{(r, v/4)} \rVert \leqslant 2 \left( \frac{4 v (r^3 + vr^2) \sqrt{l} }{2^{n/4} } \right)^v.
        \]

        考虑支撑在 $\mathsf{QEC}_{(r, v/4)}$ 上的任意归一化态 $\ket{\varphi}$，将其写作基于猜测的展开式

        \[
            \ket{\varphi} = \sum_{z_1, \ldots, z_v} \alpha_{z_1, \ldots, z_v} \ket{z_1, \ldots, z_v} \otimes \ket{\varphi_{z_1, \ldots, z_v}},
        \]

        其中 $\ket{\varphi_{z_1, \ldots, z_v}}$ 是系统其余部分的归一化状态. 那么有

        \begin{align*}
            \bra{\varphi} \Lambda_{\mathrm{succ}} \ket{\varphi} &= \sum_{z_1, \ldots, z_v \text{ and distinct} } \lvert \alpha_{z_1, \ldots, z_v} \rvert^2 \bra{\varphi_{z_1, \ldots, z_v}} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{\varphi_{z_1, \ldots, z_v}} \\
            &\leqslant \max_{z_1, \ldots, z_v \text{ and distinct} } \bra{\varphi_{z_1, \ldots, z_v}} \hat{n}_{z_1} \cdots \hat{n}_{z_v} \ket{\varphi_{z_1, \ldots, z_v}} \\
            & \leqslant 2 \left( \frac{4 v(r^3 + vr^2) \sqrt{l} }{2^{n/4} } \right)^v.
        \end{align*}

## A bosonic compressed oracle technique

### Initial bosonic state

首先计算对多重集 $S$ 的选择的纯化. 均匀随机采样一个大小为 $l$ 的多重集的一种技术是：制备初始处于 $0$-动量模式下的 $l$ 个玻色子，然后在位置基底下测量. 所以谕示机 $S$ 的纯化态简单来说就是处于 $0$-动量模式下的 $l$ 个玻色子态：

\[
    \frac{1}{\sqrt{l!} } (\tilde{a}_0^\dagger)^l \ket{\text{vac} }.
\]

!!! note "Claim"
    上述状态等于所有 $l$ 元多重集上的均匀叠加态，其中每一个元素都是相互独立地随机均匀采样的.

    ??? note "Proof"
        可以将一个均匀随机的 $l$ 元多重集的纯化在 Fock 基底中写作：

        \[
            \sum_{l_0, \ldots, l_{2^n - 1} \in \mathbb{Z}_{\geqslant 0} \text{ and } \sum_x l_x = l} \sqrt{p_{l_0, \ldots, l_{2^n - 1}}} \ket{l_0, \ldots, l_{2^n - 1}},
        \]

        其中 $p_{l_0, \ldots, l_{2^n - 1}} = \frac{1}{2^{nl}} \frac{l!}{\prod_{x \in \{0, 1\}^n} l_x!}$ 是采样 $l$ 个均匀随机字符串时，测量得到每一个 $x$ 恰好有 $l_x$ 个副本的概率.

        接下来写出 $0$-动量模式下施加 $l$ 个玻色子产生算子的状态在 Fock 基底中的展开式：

        \begin{align*}
            \frac{1}{\sqrt{l!} } (\tilde{a}_0^\dagger)^l \ket{\text{vac} } &= \frac{1}{\sqrt{l! 2^{nl}} } \sum_{x_1, \ldots, x_l \in \{0, 1\}^n} \left( \prod_{i = 1}^l \hat{a}_{x_i}^\dagger \right) \ket{\text{vac} } \\
            & = \frac{1}{\sqrt{l! 2^{nl}} } \sum_{l_0, \ldots, l_{2^n - 1} \in \mathbb{Z}_{\geqslant 0} \text{ and } \sum_x l_x = l} \frac{l!}{\prod_{x \in \{0, 1\}^n} l_x!} \left( \prod_{i = 1}^l (\hat{a}_x^\dagger)^{x_i} \right) \ket{\text{vac} } \\
            & = \frac{1}{\sqrt{2^{nl}} } \sum_{l_0, \ldots, l_{2^n - 1} \in \mathbb{Z}_{\geqslant 0} \text{ and } \sum_x l_x = l} \sqrt{\frac{l!}{\prod_{x \in \{0, 1\}^n} l_x!}} \ket{l_0, \ldots, l_{2^n - 1}}.
        \end{align*}

        第二行是因为特定 Fock 基底 $\ket{l_0, \ldots, l_{2^n - 1}}$ 的出现次数恰为 $\frac{l!}{\prod_{x \in \{0, 1\}^n} l_x!}$；第三行是产生算子的作用.

### Purified state of algorithm and oracle registers

接下来引入对谕示机 $U$ 进行查询的查询算法的状态纯化. 为了构造压缩谕示机，写出以下针对 $S$ 和 $U$ 的系统初始状态的纯化；假设该状态是在纯化寄存器 $\mathsf{S}$ 和 $\mathsf{U}$ 上表示的：

\[
    \ket{\text{init} }_{\mathsf{S}, \mathsf{U}} := \frac{1}{\sqrt{l!} } (\tilde{a}_0^\dagger)^l \ket{\text{vac} }_{\mathsf{S}} \otimes \ket{\perp}_\mathsf{U}^{\otimes 2^n}.                
\]

此处的 $\mathsf{U}$ 寄存器被划分为 $\otimes_{y \in \{0, 1\}^n} \mathsf{U}_y$，每个 $\mathsf{U}_y$ 寄存器的初始状态为 $\ket{\perp}$. 分别针对 $\mathsf{S}$ 和 $\mathsf{U}$ 单个寄存器的初始状态的纯化可以写作

\[
    \ket{\text{init} }_{\mathsf{S}} := \frac{1}{\sqrt{l!} } (\tilde{a}_0^\dagger)^l \ket{\text{vac} }_{\mathsf{S}}, \quad \ket{\text{init} }_{\mathsf{U}} := \ket{\perp}_\mathsf{U}^{\otimes 2^n}.
\]

定义以下作用于寄存器 $\mathsf{US}$ 的等距同构：

\begin{align*}
    \mathcal{V}_1 &:= \sum_S \ket{\mathsf{tt}_S} \bra{\mathsf{tt}_S}_\mathsf{S} \otimes \\ 
    &\bigotimes_{y \in \{0, 1\}^n} \left(\left( \sqrt{1 - \frac{1}{2} e^{-\kappa \gamma_y^{(S)} } } \ket{0} + \sqrt{\frac{1}{2} e^{-\kappa \gamma_y^{(S)} } } \ket{1} \right) \bra{\perp}_{\mathsf{U}_y} + \left( \sqrt{\frac{1}{2} e^{-\kappa \gamma_y^{(S)} } } \ket{0} + \sqrt{1 - \frac{1}{2} e^{-\kappa \gamma_y^{(S)} } } \ket{1} \right) \bra{\top}_{\mathsf{U}_y} \right)
\end{align*}

这是一个只作用在 $\mathsf{US}$ 上的酉算子. 再定义作用在寄存器 $\mathsf{AU}$ 上的等距同构，其中 $\mathsf{A}$ 寄存器是算法的查询寄存器：

\[
    \mathcal{V}_2 := \sum_{y \in \{0, 1\}^n} \sum_{b \in \{0, 1\}} \sum_U (-1)^{b \cdot U(y)} \ket{b, y} \bra{b, y}_\mathsf{A} \otimes \ket{\mathsf{tt}_U} \bra{\mathsf{tt}_U}_\mathsf{U}.
\]

有如下引理：

!!! success "Lemma"
    对任意查询算法 $\mathcal{A}$，有

    \[
        \op{Tr}_\mathsf{US} \left[ \mathcal{A}^{\mathcal{V}_1^\dagger \mathcal{V}_2 \mathcal{V}_1} (\ket{0, \text{init} } \bra{0, \text{init} }) \right] = \mathbb{E}_{S, U} \left[ \mathcal{A}^U (\ket{0} \bra{0}) \right].
    \]

    ??? success "Proof"
        因为 $\mathcal{V}_1$ 只作用于 $\mathsf{US}$，所以其和 $\mathcal{A}$ 施加的其他酉算子是对易的，即单次查询中的 $\mathcal{V}_1^\dagger$ 会与下次查询的 $\mathcal{V}_1$ 抵消. 因此有

        \begin{align*}
            & \mathcal{A}^{\mathcal{V}_1^\dagger \mathcal{V}_2 \mathcal{V}_1} \ket{0, \text{init} } \\
            &= U_t (\mathcal{V}_1^\dagger \mathcal{V}_2 \mathcal{V}_1) U_{t - 1} \cdots U_1 (\mathcal{V}_1^\dagger \mathcal{V}_2 \mathcal{V}_1) U_0 \ket{0, \text{init} } \\
            &= \mathcal{V}_1^\dagger U_t \mathcal{V}_2 U_{t - 1} \cdots U_1 \mathcal{V}_2 U_0 \mathcal{V}_1 \ket{0, \text{init} } \\
            &= \mathcal{V}_1^\dagger \mathcal{A}^{\mathcal{V}_2} \mathcal{V}_1 \ket{0, \text{init} }.
        \end{align*}

        从而

        \begin{align*}
            \op{Tr}_\mathsf{US} \left[ \mathcal{A}^{\mathcal{V}_1^\dagger \mathcal{V}_2 \mathcal{V}_1} (\ket{0, \text{init} } \bra{0, \text{init} }) \right]
            &= \op{Tr}_\mathsf{US} \left[ \mathcal{V}_1^\dagger \mathcal{A}^{\mathcal{V}_2} \mathcal{V}_1 (\ket{0, \text{init} } \bra{0, \text{init} }) \right] \\
            &= \op{Tr}_\mathsf{US} \left[ \mathcal{A}^{\mathcal{V}_2} (\ket{0} \bra{0} \otimes (\mathcal{V}_1 \ket{\text{init} } \bra{\text{init} } \mathcal{V}_1^\dagger)) \right] \\
        \end{align*}

        而将 $\mathcal{V}_1$ 作用在 $\ket{\text{init} }$ 上的结果是

        \[
            \mathcal{V}_1 \ket{\text{init} } = \frac{1}{\sqrt{l! \cdot 2^{n l}}} \sum_{s_1, \ldots, s_l \in \{0, 1\}^n} \bigotimes_{y \in \{0, 1\}^n} \left( \sqrt{1 - \frac{1}{2} e^{-\kappa \gamma_y^{(S)} } } \ket{0} + \sqrt{\frac{1}{2} e^{-\kappa \gamma_y^{(S)} } } \ket{1} \right)_{\mathsf{U}_y}\otimes \hat{a}_{s_1}^\dagger \cdots \hat{a}_{s_l}^\dagger \ket{\text{vac} }.   
        \]

        所以对 $\mathcal{A}$ 的 $\mathsf{US}$ 寄存器求偏迹，将会产生按照 $\mathsf{Strong}$ 分布采样的随机 $U$ 和 $S$，并且 $\mathcal{A}$ 查询 $\mathcal{V}_2$ 所得到的混合态和 $\mathcal{A}$ 查询 $U$ 所得到的混合态是相同的.

!!! success "Corollary"
    定义作用在 $\mathsf{S}$ 上的关于参数 $y$ 的 Kraus 算子为

    \begin{align*}
        E_0^{(y)} &:= \sum_S (1 - e^{-\kappa \gamma_y^{(S)} }) \ket{\mathsf{tt}_S} \bra{\mathsf{tt}_S}_\mathsf{S}, \\
        E_1^{(y)} &:= \sum_S \sqrt{e^{-\kappa \gamma_y^{(S)} } (2 - e^{-\kappa \gamma_y^{(S)} }) } \ket{\mathsf{tt}_S} \bra{\mathsf{tt}_S}_\mathsf{S}
    \end{align*}

    然后定义作用于寄存器 $\mathsf{AUS}$ 的酉算子 $\mathcal{O}$ 为

    \[
        \mathcal{O} := \sum_{y \in \{0, 1\}^n} \sum_{b \in \{0, 1\}} \ket{b, y} \bra{b, y}_\mathsf{A} \otimes \left( \tilde{Z}_{\mathsf{U}_y} \otimes (E_0^{(y)})_\mathsf{S} + \tilde{X}_{\mathsf{U}_y} \otimes (E_1^{(y)})_\mathsf{S} \right)^b.  
    \]

    其中 $\tilde{Z}$ 和 $\tilde{X}$ 是以 $\{\ket{\perp}, \ket{\top}\}$ 为基底的 Pauli $Z$ 和 $X$ 算子，并且注意作用在 $\mathsf{US}$ 寄存器上的指数 $b$. 然后有

    \[
        \op{Tr}_\mathsf{US} \left[ \mathcal{A}^{\mathcal{O}} (\ket{0, \text{init} } \bra{0, \text{init} }) \right] = \mathbb{E}_{S, U} \left[ \mathcal{A}^U (\ket{0} \bra{0}) \right].
    \]

    ??? success "Proof"
        注意到 $(E_0^{(y)})^2 + (E_1^{(y)})^2 = \mathrm{id}$，且 $0 \preccurlyeq E_0^{(y)} \preccurlyeq \mathrm{id}$，$0 \preccurlyeq E_1^{(y)} \preccurlyeq \mathrm{id}$. 
        
        只需要证明 $\mathcal{O} = \mathcal{V}_1^\dagger \mathcal{V}_2 \mathcal{V}_1$，然后应用引理即可.

        \begin{align*}
            & \mathcal{V}_1^\dagger \mathcal{V}_2 \mathcal{V}_1 \\
            &= \sum_{S, y} \ket{1, y} \bra{1, y}_\mathsf{A} \otimes \big( \left( (1 - e^{-\kappa \gamma_y^{(S)} }) \ket{\perp} + \sqrt{e^{-\kappa \gamma_y^{(S)} } (2 - e^{-\kappa \gamma_y^{(S)} }) } \ket{\top} \right) \bra{\perp}_{\mathsf{U}_y} \\
            &+ (\sqrt{e^{-\kappa \gamma_y^{(S)} } (2 - e^{-\kappa \gamma_y^{(S)} }) } \ket{\perp} + (1 - e^{-\kappa \gamma_y^{(S)} }) \ket{\top} ) \bra{\top}_{\mathsf{U}_y} \big) \otimes \ket{\mathsf{tt}_S} \bra{\mathsf{tt}_S}_\mathsf{S} \\
            &+ \sum_y \ket{0, y} \bra{0, y}_\mathsf{A} \otimes \mathrm{id}_\mathsf{US} \\
            &= \sum_{S, y} \ket{1, y} \bra{1, y}_\mathsf{A} \otimes \left( (1 - e^{-\kappa \gamma_y^{(S)} }) \tilde{Z} + \sqrt{e^{-\kappa \gamma_y^{(S)} } (2 - e^{-\kappa \gamma_y^{(S)} }) } \tilde{X} \right)_{\mathsf{U}_y} \otimes \ket{\mathsf{tt}_S} \bra{\mathsf{tt}_S}_\mathsf{S} \\
            &+ \sum_y \ket{0, y} \bra{0, y}_\mathsf{A} \otimes \mathrm{id}_\mathsf{US}.
        \end{align*}

        $\tilde{Z} = \ket{\perp} \bra{\perp} - \ket{\top} \bra{\top}$，$\tilde{X} = \ket{\perp} \bra{\top} + \ket{\top} \bra{\perp}$. 利用 Kraus 算子改写即可验证两者相等.

所以 $\mathcal{A}^\mathcal{O}$ 的操作序列如下：

\[
    \underbrace{A \mathcal{O} A \mathcal{O} \cdots A \mathcal{O}}_{T \text{ times}} A \ket{0}_\mathsf{A}\ket{\text{init} }_{\mathsf{US}}.
\]

对受控 $U$ 的查询访问可以进一步缩写为

\[
    \mathcal{O} = \sum_{y \in \{0, 1\}^n} \sum_{b \in \{0, 1\}} \ket{b, y} \bra{b, y}_\mathsf{A} \otimes \left( \sum_{x \in \{0 ,1\}} (K^x)_{\mathsf{U}_y} \otimes (E_x^{(y)})_\mathsf{S} \right)^b,
\]

其中 $K^x := \tilde{Z}^{1 - x} + \tilde{X}^x$.

给定 $\mathbf{y} = (y_1, \ldots, y_T)$，$\mathbf{b} = (b_1, \ldots, b_T)$，令 $\mathbf{y^b} = (y_i: b_i = 1)$，其长度为 $\lvert \mathbf{b} \rvert = \sum_{i} b_i$，第 $i$ 个分量记为 $y^b_i$，那么给定 $\mathbf{x} = (x_1, \ldots, x_{\lvert \mathbf{b} \rvert})$，定义以下缩写：

\[
    (K^\mathbf{x})_{\mathbf{y}, \mathbf{b}} := \prod_{i = 1}^{\lvert \mathbf{b} \rvert} (K^{x_i})_{\mathsf{U}_{y^b_i}}, \quad E_\mathbf{x}^{(\mathbf{y}, \mathbf{b})} := \prod_{i = 1}^{\lvert \mathbf{b} \rvert} (E_{x_i}^{(y^b_i)}), \quad A_{\mathbf{y}, \mathbf{b}} := \prod_{i = T}{1} A \cdot \ket{b_i, y_i} \bra{b_i, y_i}.
\]

从而，后查询态为

\[
    \ket{\psi_\mathrm{PQ}} := \sum_{\mathbf{y} \in (\{0, 1\}^n)^T} \sum_{\mathbf{b} \in \{0, 1\}^T} \left( (A_{\mathbf{y}, \mathbf{b}})_\mathsf{A} \otimes \left( \sum_{\mathbf{x} \in \{0, 1\}^{\lvert \mathbf{b} \rvert}} (K^\mathbf{x})_{\mathbf{y}, \mathbf{b}} \otimes E_\mathbf{x}^{(\mathbf{y}, \mathbf{b})} \right) \right) A \ket{0}_\mathsf{A} \ket{\text{init} }_{\mathsf{US}}.
\]

### Action of the oracle in the momentum basis

定义“单 $y$-动量跃迁算子” $\tilde{\mathbf{G}}_y$ 和“双 $y$-动量跃迁算子” $\tilde{\mathbf{H}}_y$ 为

\begin{align*}
    \tilde{\mathbf{G}}_y &:= \frac{1}{\sqrt{l}} \sum_{x \in \{0, 1\}^n} \tilde{a}_{x \oplus y}^\dagger \tilde{a}_x, \\
    \tilde{\mathbf{H}}_y &:= \frac{1}{l} \sum_{x, x' \in \{0, 1\}^n} \tilde{a}_{x \oplus y}^\dagger \tilde{a}_{x' \oplus y}^\dagger \tilde{a}_x \tilde{a}_{x'}.
\end{align*}

通过 $\tilde{\mathbf{H}}_y$ 的作用下，整个系统的动量增加了 $2y$，而这在按位异或域 $\mathbb{F}_2^n$ 下就是增加了 $0$ 动量，所以系统的总动量在 $\tilde{\mathbf{H}}_y$ 的作用下是守恒的. 并且，单动量跃迁算子和双动量跃迁算子之间是相互关联的：

\begin{align*}
    \tilde{\mathbf{G}}_y^2 &= \frac{1}{l} \sum_{x, x' \in \{0, 1\}^n} \tilde{a}_{x \oplus y}^\dagger \tilde{a}_x \tilde{a}_{x' \oplus y}^\dagger \tilde{a}_{x'} \\
    &= \frac{1}{l} \sum_{x, x' \in \{0, 1\}^n} \tilde{a}_{x \oplus y}^\dagger (\tilde{a}_{x' \oplus y}^\dagger \tilde{a}_x + \delta_{x, x' \oplus y}) \tilde{a}_{x'} \\
    &= \frac{1}{l} \sum_{x, x' \in \{0, 1\}^n} \tilde{a}_{x \oplus y}^\dagger \tilde{a}_{x' \oplus y}^\dagger \tilde{a}_x \tilde{a}_{x'} + \frac{1}{l} \sum_{x \in \{0, 1\}^n} \tilde{a}_x^\dagger \tilde{a}_x \\
    &= \tilde{\mathbf{H}}_y + \frac{\tilde{N}}{l}.
\end{align*}

在 $l$ 个玻色子的子空间中，便是

\[
    \tilde{\mathbf{G}}_y^2 = \tilde{\mathbf{H}}_y + \mathrm{id}.
\]

接下来将建立将跃迁算子和映射 $\ket{\mathsf{tt}_S} \mapsto \gamma_y^{(S)} \ket{\mathsf{tt}_S}$ 的联系.

!!! success "Lemma(Single hopping twice applies $\gamma_y^{(S)}$)"
    对任意 $y \in \{0, 1\}^n$，有

    \[
        \tilde{\mathbf{G}}_y^2 \hat{a}_{s_1}^\dagger \cdots \hat{a}_{s_l}^\dagger \ket{\text{vac} } = \gamma_y^{(S)} \hat{a}_{s_1}^\dagger \cdots \hat{a}_{s_l}^\dagger \ket{\text{vac} }.
    \]

    ??? success "Proof"
        直接计算 $\tilde{\mathbf{G}}_y$ 在位置基底上的作用：

        \begin{align*}
            \tilde{\mathbf{G}}_y \hat{a}_{s_1}^\dagger \cdots \hat{a}_{s_l}^\dagger \ket{\text{vac} } &= \frac{1}{\sqrt{l}} \sum_{x \in \{0, 1\}^n} \tilde{a}_{x \oplus y}^\dagger \tilde{a}_x \hat{a}_{s_1}^\dagger \cdots \hat{a}_{s_l}^\dagger \ket{\text{vac} } \\
            &= \frac{1}{\sqrt{l N^l} } \sum_{x \in \{0, 1\}^n} \sum_{t_1, \ldots, t_l} (-1)^{t_1 \cdot s_1 + \cdots + t_l \cdot s_l} \tilde{a}_{x \oplus y}^\dagger \tilde{a}_x \tilde{a}_{t_1}^\dagger \cdots \tilde{a}_{t_l}^\dagger \ket{\text{vac} } \\
            &= \frac{1}{\sqrt{l N^l} } \sum_{i = 1}^l \sum_{t_1, \ldots, t_l} (-1)^{t_1 \cdot s_1 + \cdots + t_l \cdot s_l} \tilde{a}_{t_i \oplus y}^\dagger \left( \prod_{k: k \neq i} \tilde{a}_{t_k}^\dagger \right) \ket{\text{vac} } \\
            &= \frac{1}{\sqrt{l N^l} } \sum_{i = 1}^l \sum_{t_1, \ldots, t_l} (-1)^{y \cdot s_i} (-1)^{t_1 \cdot s_1 + \cdots + t_l \cdot s_l} \tilde{a}_{t_1}^\dagger \cdots \tilde{a}_{t_l}^\dagger \ket{\text{vac} } \\
            &= \left( \frac{1}{\sqrt{l}} \sum_{i = 1}^l (-1)^{y \cdot s_i} \right) \hat{a}_{s_1}^\dagger \cdots \hat{a}_{s_l}^\dagger \ket{\text{vac} }.
        \end{align*}

        而因为 $\tilde{\mathbf{G}}_y$ 在位置基底下是对角的，平方作用只需要将产生的系数平方即可，依据定义二者相等.
    
!!! note "Fact(Hopping operators preserve condensates)"
    对任意 $r \geqslant 0$ 以及 $k \geqslant 0$，有

    \[
        (\mathrm{id} - \mathsf{Con}_{r + 2k}) \cdot \tilde{\mathbf{H}}_{y_k} \cdots \tilde{\mathbf{H}}_{y_1} \cdot \mathsf{Con}_r = 0.
    \]

    其次，对于任何多项式 $p: \mathbb{R^{2^n} \to \mathbb{R}}$，设 $M_p$ 为算子 $p(\gamma_0^{(S)}, \ldots, \gamma_{2^n - 1}^{(S)})$，有

    \[
        (\mathrm{id} - \mathsf{Con}_{r + 2 \deg(p)}) \cdot M_p \cdot \mathsf{Con}_r = 0.
    \]

    ??? note "Proof"
        第一个等式成立是因为 $\tilde{\mathbf{H}}_y$ 最多只能将 $2$ 个玻色子从 $0$-动量模式中移出.

        第二个等式成立是因为

        \begin{align*}
            p(\gamma_0^{(S)}, \ldots, \gamma_{2^n - 1}^{(S)}) &= p(\tilde{\mathbf{G}}_0^2, \ldots, \tilde{\mathbf{G}}_{2^n - 1}^2) \\
            &= p(\tilde{\mathbf{H}}_0 + \mathrm{id}, \ldots, \tilde{\mathbf{H}}_{2^n - 1} + \mathrm{id}).
        \end{align*}

        展开后便是形如 $\tilde{\mathbf{H}}_{y \leqslant \deg(p)}, \ldots, \tilde{\mathbf{H}}_{y_1}}$ 的线性组合，结合第一个等式便可得出.

!!! note "Fact(Norm of hopping operators for condensates)"
    对于 $y \neq 0$ 以及所有 $r \geqslant 0$，单动量跃迁算子和双动量跃迁算子的作用在 $r$-凝聚态空间上具有较小的范数，具体来说：

    \begin{align*}
        \lVert \tilde{\mathbf{G}}_y \cdot \mathsf{Con}_r \rVert &\leqslant \sqrt{r} + \sqrt{2 + 4r} \\
        \lVert \tilde{\mathbf{H}}_y \cdot \mathsf{Con}_r \rVert &\leqslant 9r + 9.
    \end{align*}

    ??? note "Proof"
        定义 

        \[
            \tilde{M}_y := \frac{1}{\sqrt{l}} (\tilde{a}_y^\dagger \tilde{a}_0 + \tilde{a}_0^\dagger \tilde{a}_y), \quad \tilde{M}_y' := \frac{1}{\sqrt{l}} \sum_{x \not \in \{0, y\}} \tilde{a}_{x \oplus y}^\dagger \tilde{a}_x.
        \]

        因此，约束 $\lVert \tilde{\mathbf{G}}_y \cdot \mathsf{Con}_r \rVert$ 可以通过三角不等式分解为约束 $\lVert \tilde{M}_y \cdot \mathsf{Con}_r \rVert$ 和 $\lVert \tilde{M}_y' \cdot \mathsf{Con}_r \rVert$. 根据构造，$\tilde{M}_y$ 只依赖于 $0$-动量模式和 $y$-动量模式的玻色子数，而 $\tilde{M}_y'$ 只依赖于其余动量模式. 

        观察到 $\tilde{\mathbf{G}}_y$ 和 $\tilde{M}_y$ 都与 $\tilde{n}_0 + \tilde{n}_y$ 对易，即 $\tilde{M}_y$ 保持 $0$-动量模式和 $y$-动量模式的玻色子数之和不变. 如果依据 $\tilde{n}_0 + \tilde{n}_y$ 对 $l$ 个玻色子的子空间进行正交划分，那么 $\tilde{M}_y$ 相对于这一直和分解是分块对角的.

        所以可以将分析限制在满足以下条件的状态下：在 $0$-动量模式和 $y$-动量模式中共有 $L$ 个玻色子，并且满足 $l - L \leqslant r$. $\tilde{M}_y$ 完全依赖于 $0$-动量模式和 $y$-动量模式的玻色子数，所以可以将分析限制在完全由 $0$-动量模式和 $y$-动量模式的玻色子中的总共 $L$ 个玻色子所组成的状态上，即 $\ket{L - j, j}$ 的叠加. 而后计算 $\tilde{M}_y$ 的作用：

        \begin{align*}
            \sqrt{l} \cdot \tilde{M}_y \ket{\phi} &= \sum_{j = 0}^L (\tilde{a}_y^\dagger \tilde{a}_0 + \tilde{a}_0^\dagger \tilde{a}_y) \alpha_j \ket{L - j, j} \\
            &= \sum_{j = 0}^L \alpha_j \left( \sqrt{(L - j)(j + 1)} \ket{L - j - 1, j + 1} + \sqrt{(L - j + 1) j} \ket{L - j + 1, j - 1} \right) \\
            &= \left( \sum_{j' = 1}^L \alpha_{j' - 1} \sqrt{(L - j' + 1) j'} \ket{L - j', j'} \right) + \left( \sum_{j'' = 0}^{L - 1} \alpha_{j'' + 1} \sqrt{(L - j'') (j'' + 1)} \ket{L - j'', j''} \right) \\
            &= \sum_{j = 0}^L \left( \alpha_{j - 1} \sqrt{(L - j + 1) j} + \alpha_{j + 1} \sqrt{(L - j) (j + 1)} \right) \ket{L - j, j}.
        \end{align*}

        由此便可以约束 $\lVert \tilde{M}_y \cdot \mathsf{Con}_r \rVert$.

        \begin{align*}
            \lVert \tilde{M}_y \ket{\phi} \rVert^2 &= \frac{1}{l} \sum_{j = 0}^L \left\lvert \alpha_{j - 1} \sqrt{(L - j + 1) j} + \alpha_{j + 1} \sqrt{(L - j) (j + 1)} \right\rvert^2 \\
            & \leqslant \frac{2}{l} \sum_{j = 0}^L (\lvert \alpha_{j - 1} \sqrt{(L - j + 1) j} \rvert^2 + \left\lvert \alpha_{j + 1} \sqrt{(L - j) (j + 1)} \right\rvert^2) \\
            &= \frac{2}{l} \sum_{j = 0}^L (\lvert \alpha_{j - 1} \rvert^2 (L - j + 1) j + \lvert \alpha_{j + 1} \rvert^2 (L - j) (j + 1)) \\
            &= \frac{2}{l} (\sum_{j' = 0}^L \lvert \alpha_{j'} \rvert^2 (L - j') (j' + 1)) + \frac{2}{l} (\sum_{j'' = 0}^L \lvert \alpha_{j''} \rvert^2 (L - j'' + 1) j'') \\
            &= \frac{2}{l} \sum_{j = 0}^L \lvert \alpha_j \rvert^2 (L + 2 j L - 2 j^2) \\
            & \leqslant \frac{2}{l} \sum_{j = 0}^L \lvert \alpha_j \rvert^2 (L + 2 r L) \\
            & = 2L(1 + 2r)/l \\
            & \leqslant 2 + 4r.
        \end{align*}

        类似地，为了估计 $\lVert \tilde{M}_y' \cdot \mathsf{Con}_r \rVert$，因为 $\tilde{M}_y'$ 只依赖于除 $0$-动量模式和 $y$-动量模式之外的动量模式，且这些模式种至多有 $r$ 个玻色子，依据平方根函数的凹性，当 $r \leqlsant l$ 时，范数至多为 $r/\sqrt{l} \leqlsant r / \sqrt{r} \leqlsant \sqrt{r}$. 而当 $r > l$ 时，使用 $\lVert \tilde{\mathbf{G}}_y \rVert \leqlsant \sqrt{l} \leqlsant \sqrt{r}$ 即可.

        而为了约束 $\lVert \tilde{\mathbf{H}}_y \cdot \mathsf{Con}_r \rVert$，注意到 $\tilde{\mathbf{G}}_y \ket{\phi}$ 是一个 $r + 1$-凝聚态，所以

        \begin{align*}
            \lVert \tilde{\mathbf{H}}_y \ket{\phi} \rVert & \leqslant 1 + \lVert \tilde{\mathbf{G}}_y^2 \ket{\phi} \rVert \\
            & \leqslant 1 + (\sqrt{r} + \sqrt{2 + 4r})(\sqrt{r + 1} + \sqrt{2 + 4(r + 1)}) \\
            & \leqslant 9r + 9.
        \end{align*}

## Proving the condensate property

在本节中将证明对于任何 $T$ 次的查询算法，该算法纯化后的查询后状态大部分支撑在凝聚态上. 算法 $\mathcal{A}$ 的纯化查询后状态为

\[
    \ket{\psi_\mathrm{PQ}} := \sum_{\mathbf{y}, \mathbf{b}} \left( (A_{\mathbf{y}, \mathbf{b}})_\mathsf{A} \otimes \left( \sum_{\mathbf{x}} (K^\mathbf{x})_{\mathbf{y}, \mathbf{b}} \otimes e_\mathrm{x} \left( \tilde{\mathbf{G}}_{y^b_1}, \ldots, \tilde{\mathbf{G}}_{y^b_{\lvert \mathbf{b} \rvert}} \right) \right) \right) A \ket{0}_\mathsf{A} \ket{\text{init} }_{\mathsf{US}}.
\]

首要目标是证明对某个适量大（但是和 $n$ 呈多项式阶关系）的 $R$，$\lVert \ket{\psi_\mathrm{PQ}}$ - $\mathsf{Con}_R \ket{\psi_\mathrm{PQ}} \rVert$ 是非常小的. 然而事实表明可以证明一个更强的命题：将算子 $\tilde{\mathbf{G}}$ 限制在 $\mathsf{Con}_R$ 并不会显著改变状态. 形式上，定义凝聚态夹心查询后状态（condensate sandwiched post-query state）如下.

!!! info "Definition(Condensate sandwiched post-query states)"
    对于整数 $R, r \geqslant 0$，以及对谕示机发起了 $T$ 次查询的量子敌手 $\mathcal{A}$，定义 $(R, r)$-夹心态为

    \[
        \ket{\tilde{\psi}_{R, r}} := \sum_{\mathbf{y}, \mathbf{b}} \left( (A_{\mathbf{y}, \mathbf{b}})_\mathsf{A} \otimes \left( \sum_{\mathbf{x}} (K^\mathbf{x})_{\mathbf{y}, \mathbf{b}} \otimes \prod_{i = 1}^{\lvert \mathbf{b} \rvert} \mathsf{Con}_r \cdot e_{x_i} \left(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_{y^b_i} \cdot \mathsf{Con}_R) \right) \right) \cdot \mathsf{Con}_r \right) A \ket{0}_\mathsf{A} \ket{\text{init} }_{\mathsf{US}}.
    \]

将 $\ket{\tilde{\psi}_{R, r}}$ 限制在 $\mathsf{Con}_r$ 子空间中不会改变其状态本身，因此只需表明 $\ket{\tilde{\psi}_{R, r}}$ 接近于 $\ket{\psi_\mathrm{PQ}}$ 即可. 主定理如下：

!!! note "Theorem(Sandwiching theorem)"
    对每个 $\iota > 0$，存在整数 $r = O(n^2 T^5 \ln^3 (T) \ln^2 (1/\iota))$ 和 $R = O(n^3 T^6 \ln^4 (T) \ln^3 (1/\iota))$，使得

    \[
        \lVert \ket{\psi_\mathrm{PQ}} - \ket{\tilde{\psi}_{R, r}} \rVert \leqslant \iota.
    \]

证明中使用的主要技术是对指数函数进行多项式近似，为了明确在此背景下“多项式近似”的含义，定义**函数查询后状态**（function post-query state）如下：

!!! info "Definition(Function post-query states)"
    设 $\mathcal{A}$ 是一个在查询间应用酉算子 $A$ 的 $T$ 次量子查询算法，给定一族函数 $f_\mathrm{x} = f_(x_1, \ldots, x_T)$，定义 $f$-查询后状态为

    \[
        \ket{\psi_f} := \sum_{\mathbf{y}, \mathbf{b}} \left( (A_{\mathbf{y}, \mathbf{b}})_\mathsf{A} \otimes \left( \sum_{\mathbf{x}} (K^\mathbf{x})_{\mathbf{y}, \mathbf{b}} \otimes f_\mathrm{x}(\tilde{\mathbf{G}}_{y^b_1}, \ldots, \tilde{\mathbf{G}}_{y^b_{\lvert \mathbf{b} \rvert}}) \right) \right) A \ket{0}_\mathsf{A} \ket{\text{init} }_{\mathsf{US}}.
    \]

通过对角化 $X$，并将 $f$ 作用在对角元上，便实现对对角化矩阵计算 $f(X)$. 直观上，如果 $U_y$ 是根据 $f(\gamma_y(S))$ 采样得到的，那么函数查询后状态就对应于查询 $U$ 谕示机后的算法纯化状态. 为了将这些状态与原始的查询后状态联系起来，可以写出对应于 $\ket{\psi_\mathrm{PQ}}$ 的函数.

!!! info "Definition(Kraus operator eigenvalue functions)"
    定义如下的函数对 $e_0, e_1$：

    \begin{align*}
        e_0(\gamma) &:= 1 - e^{-\kappa \gamma}, \\
        e_1(\gamma) &:= \sqrt{e^{-\kappa \gamma} (2 - e^{-\kappa \gamma})} = \sqrt{2} e^{-\kappa \gamma / 2} \sqrt{1 - e^{-\kappa \gamma} / 2}.
    \end{align*}

    可以将 Kraus 算子 $E_x^{(y)}$ 表示为 $\sum_S e_x(\gamma_y^{(S)}) \ket{\mathsf{tt}_S} \bra{\mathsf{tt}_S}$.

而对于所有 $B \in \mathbb{Z}_{\geqslant 0}$，以及 $\mathbf{x} = (x_1, \ldots, x_B)$，也可以使用 $e_\mathbf{x}(\gamma_1, \ldots, \gamma_B)$ 简写 $\prod_{i = 1}^B e_{x_i}(\gamma_i)$.

因此有

\[
    \ket{\psi_\mathrm{PQ}} = \ket{\psi_e}.
\]

!!! note "Theorem(Polynomial approximation of post-query state)"
    对于每个 $\iota > 0$，存在一族关于算子 $\tilde{\mathbf{G}}^2_{y_i}$ 的多项式 $\text{AKraus}_\mathbf{x}$（隐式依赖于 $\iota$），其次数满足

    \[
        \deg(\text{AKraus}_\mathbf{x}) = O(n^2 T^5 \ln (T) \ln^2 (1/\iota)),
    \]

    使得通过以下方式可以约束真实的查询后状态和多项式近似之间的距离：

    \[
        \lVert \ket{\psi_\mathrm{PQ}} - \ket{\psi_{\text{AKraus}}} \rVert \leqslant \iota.
    \]

### Polynomial approximations to the Kraus operators

本节中将引入两种多项式近似，第一种是指数函数的截断 Taylor 展开：

\[
    \text{Taylor}_d (z) := \sum_{j = 0}^d \frac{z^j}{j!}.
\]

有如下引理：

!!! success "Lemma(Truncated Taylor condensate approximation)"
    设 $W$ 为一个算子，存在一个常数 $M > 0$ 使得对于任意整数 $m > 0$，$W$ 作用 $m$-凝聚态子空间上的算子范数由 $Mm$ 控制. 此外，假设对于所有的 $m$，$W$ 都会将 $m$-凝聚态子空间映射到 $(m + 2)$-凝聚态子空间. 即对于所有的 $m > 0$，$W$ 满足以下两个条件：

    \begin{gather*}
        \lVert W \cdot \mathsf{Con}_m \rVert \leqslant M m, \\
        W \cdot \mathsf{Con}_m = \mathsf{Con}_{m + 2} \cdot W \cdot \mathsf{Con}_m = \mathsf{Con}_{m + 2} \cdot W \cdot \mathsf{Con}_{m + 2} \cdot \mathsf{Con}_m.
    \end{gather*}

    那么对于 $r \geqslant 0$，$s \geqslant 3M$，$1/e \geqslant \varepsilon > 0$，以及 $d \geqslant 4 \ln (1/\varepsilon) + r$, 有

    \[
        \lVert (\text{Taylor}_d(-W / s) - \exp(-W / s)) \cdot \mathsf{Con}_r \rVert \leqslant \varepsilon.
    \]

    ??? success "Proof"
        展开 $e^{-W / s}$ 的 Taylor 级数，有

        \begin{align*}
            \lVert (\text{Taylor}_d(-W / s) - \exp(-W / s)) \cdot \mathsf{Con}_r \rVert &= \left\lVert \sum_{j = d + 1}^\infty \frac{1}{j!} s^{-j} (-W)^j \cdot \mathsf{Con}_r \right\rVert \\
            &\leqslant \sum_{j = d + 1}^\infty \frac{1}{j!} s^{-j} \lVert W^j \cdot \mathsf{Con}_r \rVert \\
            &= \sum_{j = d + 1}^\infty \frac{1}{j!} s^{-j} \left\lVert \left( \prod_{k = j}^1 \mathsf{Con}_{2k + r} W \mathsf{Con}_{2k + r} \right) \cdot \mathsf{Con}_r \right\rVert \\
            &\leqslant \sum_{j = d + 1}^\infty \frac{1}{j!} s^{-j} \prod_{k = j}^1 \lVert \mathsf{Con}_{2k + r} W \mathsf{Con}_{2k + r} \rVert \\
            &\leqslant \sum_{j = d + 1}^\infty \frac{1}{j!} \left(\prod_{k = j}^1 (k + r/2) \right) \left(\frac{M}{s}\right)^j \\
            &= \sum_{j = 1}^\infty \binom{r/2 + j}{j} \left(\frac{M}{s}\right)^j.
        \end{align*}

        定义 $w_j = \binom{r/2 + j}{j} \left(\frac{M}{s}\right)^j$，问题转为约束 $S(d) := \sum_{j = d + 1}^\infty w_j$. 考虑 $w_j$ 的比值：

        \[
            \frac{w_{j + 1}}{w_j} = \left(\frac{M}{s}\right) \frac{\binom{r/2 + j + 1}{j + 1}}{\binom{r/2 + j}{j}} = \left(\frac{M}{s}\right) \frac{r/2 + j + 1}{j + 1} = \left(\frac{M}{s}\right) \left(1 + \frac{r}{2(j + 1)}\right).
        \]

        对于 $j \geqslant d$，该值至多为

        \[
            Q := \left(\frac{M}{s}\right) \left(1 + \frac{r}{2(d + 1)}\right).
        \]

        因为 $M/s \leqslant 1/3$，且 $r/2(d + 1) \leqslant 1/2$，所以 $Q \leqslant 1/2$. 因此有

        \[
            S(d) = \sum_{j = d + 1}^\infty w_j \leqslant w_{d + 1} \sum_{k = 0}^\infty Q^k = 2 w_{d + 1} = 2 \binom{r/2 + d + 1}{d + 1} \left(\frac{M}{s}\right)^{d + 1} \leqslant 2^(r/2 + d + 2) \cdot 3^{-(d + 1)}.
        \]

        对于 $d \geqslant 4 \ln (1/\varepsilon) + r$，该值可以被 $\varepsilon$ 上界约束.

第二种是第一类 Chebyshev 多项式：

\[
    \text{Cheby}_k (z) = \cos (k \arccos(z)), \quad z \in [-1, 1].
\]

Chebyshev 多项式构成了多项式空间的一组基，因此存在系数 $a_k^{(s)}$，使得在 Chebyshev 多项式基底下，函数 $z \mapsto z^s$ 可以表示为

\[
    z^s = \sum_{k = 0}^s a_k^{(s)} \text{Cheby}_k(z).
\]

将 $z^s$ 的截断 Chebyshev 展开式记为

\[
    \text{TCheby}_{s, d} (z) := \sum_{k = 0}^d a_k^{(s)} \text{Cheby}_k(z).
\]

将应用以下关于 Chebyshev 多项式的事实：

!!! note "Fact"
    1. 对于所有 $k \geqslant 0$，有 $\lvert a_k^{(s)} \rvert \leqslant 1$. 并且对于所有 $z \in [-1, 1]$，有 

    \[
        \lvert z^s - \text{TCheby}_{s, d} (z) \rvert \leqslant 2 \cdot \exp \left(- \frac{d^2}{2s} \right).
    \]

    2. 对于所有 $k \geqslant 0$，$\text{Cheby}_k$ 在单项式基底下的各项系数被 $(1 + \sqrt{2})^k$ 所控制.

!!! success "Lemma(Flat approximations of exponential functions)"
    设 $W$ 是满足先前引理条件的半正定算子 $W \succcurlyeq 0$，那么对于任意 $\varepsilon > 0$ 和 $r \geqslant 0$，存在一个次数至多为 $100 M \ln(1 / \varepsilon)(r + 1)$ 的多项式，称为 $\mathrm{Flat}_\varepsilon = \mathrm{Flat}_{\varepsilon, M, r}$，使得

    \[
        \lVert (\exp(-W) - \mathrm{Flat}_\varepsilon (W) ) \cdot \mathsf{Con}_r \rVert \leqslant \varepsilon.
    \]

    ??? success "Proof"
        利用 $W \succcurlyeq 0$ 这一事实来确保 $\exp(-W/w)$ 的谱被包含在 $[0, 1]$.

        为了应用引理，固定 $w := 36 M^2 \ln(2 / \varepsilon)$，以及 $d' := \left\lceil \sqrt{72 M^2 \ln^2 (2 / \varepsilon)} \right\rceil$. 依据先前的事实，对于所有满足 $d' \geqslant \sqrt{2 w \ln(2 / \varepsilon)}$ 的 $d'$，有

        \[
            \exp(-W) \cdot \mathsf{Con}_r = (\exp(-W / w))^w \cdot \mathsf{Con}_r \approx_{\varepsilon / 2} (\text{TCheby}_{w, d'}(\exp(-W / w))) \cdot \mathsf{Con}_r.
        \]

        其中符号 $X \approx_\varepsilon X'$ 表示 $\lVert X - X' \rVert \leqslant \varepsilon$. 

        现在令 $b_k$ 为多项式 $\text{TCheby}_{w, d'} (z)$ 在单项式展开式中单项式 $z^k$ 的系数，即

        \[
            \text{TCheby}_{w, d'} (z) = \sum_k b_k z^k.
        \]

        因为选择的 $w, d'$ 满足

        \[
            d' = \sqrt{2 w \ln(2 / \varepsilon)},
        \]

        所以对于所有 $k \leqslant d'$，可以进行以下放缩：

        \[
            \frac{k}{w} \leqslant \frac{d'}{w} \leqslant \frac{\sqrt{4 w \ln {2 / \varepsilon}}}{w}.
        \]

        固定 $d := (4 ((9 M + 1) \ln(1 / \varepsilon) + \ln (2)) + r). 依据引理，只需要满足以下两个条件

        \[
            d \geqslant 4 \ln (2 \cdot (\max_k \lvert b_k \rvert) \cdot d' / \varepsilon) + r, \quad s:= \sqrt{\frac{w}{4 \ln (2 / \varepsilon)}} \geqslant 3 M,
        \]

        就会有

        \begin{align*}
            \text{TCheby}_{w, d'} (\exp(-W/w)) \cdot \mathsf{Con}_r &= \sum_{k = 1}^{d'} b_k \cdot \exp(-W/w)^k \cdot \mathsf{Con}_r \\
            &= \sum_{k = 1}^{d'} b_k \cdot \exp(- \frac{k}{w} W ) \cdot \mathsf{Con}_r \\
            & \approx_{\varepsilon / 2} \sum_{k = 1}^{d'} b_k \cdot \text{Taylor}_d(-\frac{k}{w} W) \cdot \mathsf{Con}_r.
        \end{align*}

        这里的 $s$ 实际上就是 $w / k$，其条件较容易证明. 接下来需要证明 $d$ 满足所需的下界. 对于足够小的 $\varepsilon$，可以对 $d'$ 进行放缩：

        \[
            d' = \left\lceil \sqrt{72 M^2 \ln^2 (2 / \varepsilon)} \right\rceil \leqslant 9 M \ln(1 / \varepsilon).
        \]

        依据定义，观察到

        \[
            b_k = \sum_{k' = k}^{d'} a_{k'}^{(s)} \cdot [\text{Coefficient of } z^{k'} \text{ in } \text{Cheby}_k(z)].
        \]

        依据事实，对于所有的 $k$，$b_k$ 都可以被以下上界控制：

        \[
            \lvert b_k \rvert \leqslant (\lvert a_1^{(s)} \rvert + \cdots + \lvert a_{d'}^{(s)} \rvert) (1 + \sqrt{2})^{d'} \leqslant d' (2.5)^{d'}.
        \]

        两侧取对数，对于 $d' \geqslant 10$ 应用之前的放缩，便可得出

        \begin{align*}
            \ln (\lvert b_k \rvert) + \ln (d') & \leqslant 2 \ln (d') + d' \ln (2.5) \\
            & \leqslant 2 \ln (d') + 9 M \ln(1 / \varepsilon) \cdot 0.89 \\
            & \leqslant 9 M \ln(1 / \varepsilon).
        \end{align*}

        定义 $\mathrm{Flat}_\varepsilon (z)$ 为

        \[
            \mathrm{Flat}_\varepsilon (z) := \sum_{k = 1}^{d'} b_k \cdot \text{Taylor}_d(-\frac{k}{w} z).
        \]

        因此 $\mathrm{Flat}_\varepsilon (z)$ 是一个次数 $\leqslant d$ 的多项式，其次数至多为

        \[
            \deg(\mathrm{Flat}_\varepsilon) \leqslant d \leqslant (4 ((9 M + 1) \ln(1 / \varepsilon) + \ln (2)) + r) \leqslant 100 M \ln(1 / \varepsilon)(r + 1).
        \]

        带入即有

        \[
            \text{TCheby}_{w, d'} (\exp(-W/w)) \cdot \mathsf{Con}_r \approx_{\varepsilon / 2} \mathrm{Flat}_\varepsilon (W) \cdot \mathsf{Con}_r.
        \]

        利用三角不等式即可得到所需结果.

!!! success "Lemma"
    设 $W_1, \ldots, W_T \succcurlyeq 0$ 为满足 Truncated Taylor condensate approximation 引理条件且两两可对易的半正定算子. 对任意 $r \geqslant 0$ 以及 $\mathbf{x} \in \{0, 1\}^T$，存在一个多元多项式 $\text{AKraus}_{\varepsilon, \mathbf{x}}$ 使得

    \[
        \left\lVert \left(\prod_{i = 0}^T e_{x_i} (W_i) - \text{AKraus}_{\varepsilon, \mathbf{x}}(W_1, \ldots, W_T) \right) \cdot \mathsf{Con}_r \right\rVert \leqslant \varepsilon
    \]

    此外，$\text{AKraus}_{\varepsilon, \mathbf{x}}$ 的次数至多为 $O(M T^3 \ln(T) \ln^2(1 / \varepsilon)(r + 1))$.

    ???+ success "Proof"
        首先考虑一个算子 $W$ 的情况. 将 $e_1$ 定义中的函数 $z \mapsto \sqrt{1 - z / 2}$ 替换为以下截断二项式展开

        \[
            \text{TSqrt} (z) := \sum_{k = 0}^{d''} \binom{1/2}{k} (-1 / 2)^k z^k,
        \]

        其中 $d'' := 4 + \frac{3}{2}(\ln(T) + \ln(1 / \varepsilon))$. 因为平方根函数在 $0$ 附近没有很好的 Taylor 展开式，所以需要以 $z \mapsto \sqrt{1 - z / 2}$ 的截断二项式展开来近似它.
        
        定义如下的多项式近似：

        \begin{align*}
            p_0(z) &:= 1 - z^2 \\
            p_1(z) &:= \sqrt{2} z \cdot \text{TSqrt}(z^2).
        \end{align*}

        因为 $\text{TSqrt}$ 是对 $\sqrt{1 - z / 2}$ 的良好近似，所以 $p_x(e^{-\kappa z/2})$ 是对 $e_x(z)$ 的良好近似.  

        !!! note "Claim"
            \[
                \left \lVert \prod_{i = 1}^T e_{x_i}(W_i) - \prod_{i = 1}^T p_{x_i}(e^{-\kappa W_i / 2}) \right\rVert \leqslant \varepsilon / 2.
            \]

            ??? note "Proof"
                根据构造有

                \[
                    p_0(\exp (-\kappa z / 2)) = e_0(W), 
                \]

                因而关键在于 $p_1$ 和 $e_1$ 的近似. 实现如下近似：

                \begin{align*}
                    & \lVert p_1(\exp(-\kappa W / 2)) - e_1(W) \rVert \\
                    &= \left \lVert \sqrt{2} \exp(-\kappa W / 2) \left( \sqrt{1 - \frac{1}{2} \exp(-\kappa W)} - \text{TSqrt}(\exp(-\kappa W)) \right) \right\rVert \\
                    &\leqslant \sqrt{2} \left\lVert \exp(-\kappa W / 2) \right\rVert \sum_{k = d''}^\infty \left\lvert \binom{1/2}{k} \right\rvert \frac{1}{2^k} \left\lVert \exp(-\kappa W)^k \right\rVert \\
                    &\leqslant \frac{\sqrt{2}}{2^{d''}} \sum_{k = 0}^\infty \frac{1}{2^k} \\
                    &\leqslant \frac{\varepsilon}{4 T}.
                \end{align*}

                以上放缩中使用了 $\left\lvert \binom{1/2}{k} \right\rvert \leqslant 1$，以及 $\lVert \exp(-\kappa W)^k \rVert \leqslant 1$.

                接下来将使用混合论证将这些单项近似提升为多项乘积近似. 定义混合算子 $B_j$ 为

                \[
                    B_j := \prod_{k = T - j + 1}^T e_{x_k}(W_k) \prod_{i = 1}^{T - j} p_{x_i}(\exp(-\kappa W_i / 2)).
                \]

                利用三角不等式，有

                \begin{align*}
                    & \left\lVert \prod_{i = 1}^T e_{x_i}(W_i) - \prod_{i = 1}^T p_{x_i}(\exp(-\kappa W_i / 2)) \right\rVert \\
                    &\leqslant \sum_{j = 1}^T \lVert B_j - B_{j - 1} \rVert \\
                    &= \sum_{j = 1}^T \left\lVert \prod_{k = T - j + 2}^T e_{x_k}(W_k) \left( e_{x_{T - j + 1}}(W_{T - j + 1}) - p_{x_{T - j + 1}}(\exp(-\kappa W_{T - j + 1} / 2)) \right) \prod_{i = 1}^{T - j} p_{x_i}(\exp(-\kappa W_i / 2)) \right\rVert \\
                    &\leqslant \sum_{j = 1}^T \left\lVert e_{x_{T - j + 1}}(W_{T - j + 1}) - p_{x_{T - j + 1}}(\exp(-\kappa W_{T - j + 1} / 2)) \prod_{i = 1}^{T - j} p_{x_i}(\exp(-\kappa W_i / 2)) \right\rVert \\
                    &\leqslant T \cdot \frac{\varepsilon}{4 T} \cdot (1 + \frac{\varepsilon}{4 T})^T \\
                    &\leqslant \varepsilon / 2.
                \end{align*}

                其中利用了 $\lVert e_{x_k} W_k \rVert \leqslant 1$，$e_0(W_i) = p_0(\exp(-\kappa W_i / 2))$，$\lVert e_1 (W_i) - p_1(\exp(-\kappa W_i / 2)) \rVert \leqslant \varepsilon / 4 T$，并由此推广的

                \[
                    \lVert p_{x_k}(\exp(-\kappa W_k / 2)) \rVert \leqslant \frac{\varepsilon}{4 T} + \lVert e_{x_k}(W_k) \rVert \leqslant 1 + \frac{\varepsilon}{4 T},
                \]

                以及

                \[
                    (1 + \frac{\varepsilon}{4 T})^{T - j} \leqslant (1 + \frac{\varepsilon}{4 T})^T \leqslant e^{\frac{\varepsilon}{4T} T} \leqslant e^{1/4} \leqslant 2.
                \]

        接下来观察到 $\prod_{i = 1}^T p_{x_i}(\exp(-\kappa W_i / 2))$ 是一个关于 $\exp(-\kappa W_i / 2)$ 的多项式，次数至多为 $3 d'' T$，因为存在 $T$ 个形如 $z \text{TSqrt}(z^2)$ 的项，每一项会产生 $1 + 2d'' \leqslant 3d''$ 的次数. 

        因为假设了 $W_i$ 两两可对易，所以对任意 $J$ 个算子的集合 $W_{i_j}$，可以写出

        \[
            \prod_{j = 1}^J \exp(-\kappa W_{i_j} / 2) = \exp(-\kappa \sum_{j = 1}^J W_{i_j} / 2).
        \]

        而 $\sum_{j = 1}^J W_{i_j}$ 也依然将 $m$-凝聚态子空间映射到 $(m + 2)$-凝聚态子空间，并且依据三角不等式，有

        \[
            \left \lVert \mathsf{Con}_m \cdot \left(\frac{\kappa}{2} \sum_{j = 1}^J W_{i_j} \right) \cdot \mathsf{Con}_m \right\rVert \leqslant \kappa J M m \leqslant J M m.
        \]

        接下来将 $p_x (z)$ 在单项式基底上展开，得到

        \[
            p_x(z) = \sum_{k = 0}^{3 d''} c_k^{(x)} z^k.
        \]

        这便可以利用 $\text{Flat}_\varepsilon$ 多项式来构建多元多项式 $\text{AKraus}_{\varepsilon, \mathbf{x}}$. 对于 $\mathbf{x} = (x_1, \ldots, x_T)$，其定义为

        \[
            \text{AKraus}_{\varepsilon, \mathbf{x}}(z_1, \ldots, z_T) := \sum_{k_1, \ldots, k_T = 0}^{3 d''} \left( \prod_{i = 1}^T c_{k_i}^{(x_i)} \cdot \mathrm{Flat}_{\frac{\varepsilon}{2 \cdot 2^T}} \left( -\kappa \sum_{i = 1}^T k_i z_i / 2 \right) \right).
        \]

        !!! note "Claim"
            \[
                \left\lVert \left(\prod_{i = 1}^T p_{x_i}(\exp(-\kappa W_i / 2)) - \text{AKraus}_{\varepsilon, \mathbf{x}}(W_1, \ldots, W_T) \right) \cdot \mathsf{Con}_r \right\rVert \leqslant \varepsilon / 2.
            \]

            ??? note "Proof"
                对于任何单项式 $\prod_{i = 1}^J x_{i_j}$，应用 Flat approximations 定理，得到

                \[
                    \prod_{j = 1}^J \exp(-\kappa W_{i_j} / 2) \cdot \mathsf{Con}_r \approx_{\frac{\varepsilon}{2 \cdot 2^T}} \mathrm{Flat}_{\frac{\varepsilon}{2 \cdot 2^T}} \left( \sum_{j = 1}^J \kappa W_{i_j} / 2 \right) \cdot \mathsf{Con}_r.
                \]

                此外，$\prod_{i = 1}^T p_{x_i}$ 展开后各项系数绝对值之和至多为 $2^T$. 首先观察到 $p_0$ 的系数绝对值之和为 $2$；而在 $\text{TSqrt}(z^2)$ 中，除了第一项为 $1$ 外，其余项的系数都是负数，所以 $p_1$ 的系数绝对值之和至多为

                \[
                    \sum_{k_i = 0}^{3d''} \lvert c_{k_i}^{(x_i)} \rvert = \sqrt{2}(2 - \text{TSqrt}(1)) \leqslant \sqrt{2} \cdot (2 - \sqrt{1 - 1/2}) \leqslant 2.
                \]

                最后应用三角不等式

                \begin{align*}
                    & \left\lVert \left(\prod_{i = 1}^T p_{x_i}(\exp(-\kappa W_i / 2)) - \text{AKraus}_{\varepsilon, \mathbf{x}}(W_1, \ldots, W_T) \right) \cdot \mathsf{Con}_r \right\rVert \\
                    &\leqslant \sum_{k_1, \ldots, k_T = 0}^{3 d''} \left \lvert \prod_{i = 1}^T c_{k_i}^{(x_i)} \right\rvert \left\lVert \left(\text{Flat}_{\frac{\varepsilon}{2 \cdot 2^T}} \left( -\kappa \sum_{i = 1}^T k_i W_i / 2 \right) - \exp(-\kappa \sum_{i = 1}^T k_i W_i / 2) \right) \cdot \mathsf{Con}_r \right\rVert \\
                    &\leqslant \sum_{k_1, \ldots, k_T = 0}^{3 d''} \left \lvert \prod_{i = 1}^T c_{k_i}^{(x_i)} \right\rvert \cdot \frac{\varepsilon}{2 \cdot 2^T} \\
                    &\leqslant \sum_{k_1, \ldots, k_T = 1}^{3 d''} \frac{\varepsilon}{2 \cdot 2^T} \\
                    = \prod_{i = 1}^T \sum_{k_i = 0}^{3 d''} \lvert c_{k_i}^{(x_i)} \rvert \cdot \frac{\varepsilon}{2 \cdot 2^T} \\
                    &\leqslant 2^T \cdot \frac{\varepsilon}{2 \cdot 2^T} \\
                    &\leqslant \varepsilon / 2.
                \end{align*}

        应用三角不等式即可得到所需结果. 而 $\text{AKraus}_{\varepsilon, \mathbf{x}}$ 的次数至多为

        \begin{align*}
            \deg(\text{AKraus}_{\varepsilon, \mathbf{x}}) &\leqslant T \cdot \deg(\mathrm{Flat}_{\frac{\varepsilon}{2 \cdot 2^T}, J}) \\
            &\leqslant 100 J M T (\ln(1 / \varepsilon) + T + 1)(r + 1) \\
            &\leqslant 300 d'' M T^3 \ln(1 / \varepsilon) (r + 1) \\
            &\leqslant O(M T^3 \ln(T) \ln^2(1 / \varepsilon)(r + 1)).
        \end{align*}

!!! success "Lemma"
    设 $B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}$ 和 $B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}'$ 为作用在 $S$ 寄存器的两族算子，定义

    \[
        \ket{\psi_B} := \sum_{\mathbf{y}, \mathbf{b}} \left((A_\mathbf{y}, \mathbf{b})_\mathsf{A} \otimes \left(\sum_{\mathbf{x}} (K^\mathbf{x})_{\mathsf{y}, \mathbf{b}} \otimes B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} \right) \right) A \ket{0}_\mathsf{A} \ket{\text{init}}_\mathsf{US},
    \]

    并类似地定义 $\ket{\psi_B'}$. 那么对于所有足够大的 $n$，有

    \[
        \lVert \ket{\psi_B} - \ket{\psi_B'} \rVert \leqslant 2^{2nT} \max_{\mathbf{x}, \mathbf{y}, \mathbf{b}} \lVert B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}' \ket{\text{init}}_\mathsf{US} \rVert.
    \]

    ??? success "Proof"
        应用两次三角不等式，一次针对 $\mathbf{y}$ 的求和，一次针对 $\mathbf{x}$ 的求和. 并且利用 $\lVert K^{x_i} \rVert \leqslant 2$，$\lVert \ket{y_i} \bra{y_i} \cdot A \rVert \leqslant 1$，以及 Schatten $\infty$-范数的次可乘性，得到

        \begin{align*}
            & \lVert \ket{\psi_B} - \ket{\psi_B'} \rVert \\
            &= \left\lVert \sum_{\mathbf{y} \in (\{0, 1\}^n)^T} \sum_{\mathbf{b} \in \{0, 1\}^T} \left((A_\mathbf{y}, \mathbf{b})_\mathsf{A} \otimes \left(\sum_{\mathbf{x} \in \{0, 1\}^{\lvert \mathbf{b}\rvert}} (K^\mathbf{x})_{\mathsf{y}, \mathbf{b}} \otimes (B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}') \right) \right) A \ket{0}_\mathsf{A} \ket{\text{init}}_\mathsf{US} \right\rVert \\
            &\leqslant \sum_{\mathbf{y} \in (\{0, 1\}^n)^T} \sum_{\mathbf{b} \in \{0, 1\}^T} \left\lVert A_\mathbf{y}, \mathbf{b} \cdot A \ket{0} \otimes \left(\sum_{\mathbf{x} \in \{0, 1\}^{\lvert \mathbf{b}\rvert}} (K^\mathbf{x})_{\mathsf{y}, \mathbf{b}} \ket{\perp}^{\otimes 2^n} \otimes (B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}') \ket{\text{init}_S} \right) \right\rVert \\
            &= \sum_{\mathbf{y} \in (\{0, 1\}^n)^T} \sum_{\mathbf{b} \in \{0, 1\}^T} \lVert A_\mathbf{y}, \mathbf{b} \cdot A \ket{0} \rVert \cdot \left \lVert \left(\sum_{\mathbf{x} \in \{0, 1\}^{\lvert \mathbf{b}\rvert}} (K^\mathbf{x})_{\mathsf{y}, \mathbf{b}} \ket{\perp}^{\otimes 2^n} \otimes (B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}') \ket{\text{init}_S} \right) \right \rVert \\
            &\leqslant \sum_{\mathbf{y} \in (\{0, 1\}^n)^T} \sum_{\mathbf{b} \in \{0, 1\}^T} \lVert A_\mathbf{y}, \mathbf{b} \cdot A \ket{0} \rVert \cdot \sum_{\mathbf{x} \in \{0, 1\}^{\lvert \mathbf{b}\rvert}} \lVert (K^\mathbf{x})_{\mathsf{y}, \mathbf{b}} \ket{\perp}^{\otimes 2^n} \otimes (B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}') \ket{\text{init}_S} \rVert \\
            &= \sum_{\mathbf{y} \in (\{0, 1\}^n)^T} \sum_{\mathbf{b} \in \{0, 1\}^T} \lVert A_\mathbf{y}, \mathbf{b} \cdot A \ket{0} \rVert \cdot \sum_{\mathbf{x} \in \{0, 1\}^{\lvert \mathbf{b}\rvert}} \lVert (K^\mathbf{x})_{\mathsf{y}, \mathbf{b}} \ket{\perp}^{\otimes 2^n} \rVert \cdot \lVert (B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}') \ket{\text{init}_S} \rVert \\
            &\leqslant 2^{T} \sum_{\mathbf{y} \in (\{0, 1\}^n)^T} \sum_{\mathbf{b} \in \{0, 1\}^T} \sum_{\mathbf{x} \in \{0, 1\}^{\lvert \mathbf{b}\rvert}} \lVert (B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}') \ket{\text{init}_S} \rVert \\
            &\leqslant 2^{3T + nT} \max_{\mathbf{x}, \mathbf{y}, \mathbf{b}} \lVert (B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}') \ket{\text{init}_S} \rVert \\
            &\leqslant 2^{2nT} \max_{\mathbf{x}, \mathbf{y}, \mathbf{b}} \lVert (B_{\mathbf{x}, \mathbf{y}, \mathbf{b}} - B_{\mathbf{x}, \mathbf{y}, \mathbf{b}}') \ket{\text{init}_S} \rVert.
        \end{align*}

最后证明主定理.

因为初始状态满足 $\ket{\text{init}_S} = \mathsf{Con}_0 \ket{\text{init}_S}$，所以可以在 $r = 0$ 的情况下对算子 $W_i = \tilde{\mathbf{G}}_{y_i}^2$ 应用 AKraus lemma. 注意到 $\tilde{\mathbf{G}}_{y_i}^2$ 在位置基底下全都是对角的，且均半正定两两对易. 依据 Norm of hopping operators for condensates 的事实，其也满足相关的条件. 所以只需在以上引理中选择 $\varepsilon := \iota / 2^{2nT}$，便可以证明.

### Extending the approximation to the sandwiched operator

!!! note "Proof(Sandwiching theorem)"
    证明包含了对于 $\mathsf{S}$ 寄存器的两次混合论证，并且都使用了 AKraus lemma. 

    第一步混合论证从 $0$-凝聚态开始应用 AKraus lemma，以获取限制在 $\mathsf{Con}_0$ 上的算子乘积 $\prod_{i = 1}^{T - j} e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2)$ 的近似多项式 $\text{AKraus}_{\varepsilon, \mathbf{x}_{T - j} } (\tilde{\mathbf{G}}_{y_1}^2, \ldots, \tilde{\mathbf{G}}_{y_{T - j} }^2)$. 这里定义子串为 $\mathsf{x}_k = (x_k, \ldots, x_1)$. 这些近似针对的是具有不同长度的 $e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2)$ 的乘积. 根据 AKraus lemma，设置误差为 $\varepsilon / 2T$ 时，对于所有的 $j$，$\text{AKraus}_{\varepsilon / 2T, \mathbf{x}_{T - j} }$ 的次数被以下上界控制：

    \[
        \deg(\text{AKraus}_{\varepsilon / 2T, \mathbf{x}_{T - j} }) = O(T^3 \ln(T) \ln^2(2T / \varepsilon)) = O(T^3 \ln^3(T) \ln^2(1 / \varepsilon)).
    \]

    设置 $r = 2 \deg(\text{AKraus}_{\varepsilon / 2T, \mathbf{x}}) \geqslant 2 \max_j \deg(\text{AKraus}_{\varepsilon / 2T, \mathbf{x}_{T - j} })$，并定义以下的混合状态：

    \[
        D_j := \prod_{i = T}^{T - j + 1} \mathsf{Con}_r \cdot e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \prod_{i = 1}^{T - j} e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \ket{\text{init}_S}.
    \]

    前 $T - j$ 个算子是两两对易的，展开顺序并不影响结果. 因为初始状态是一个 $0$-凝聚态，所以有

    \[
        \left \lVert \left(\prod_{i = T}^1 \mathsf{Con}_r \cdot e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \cdot \mathsf{Con}_r - \prod_{i = 1}^T e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \right) \ket{\text{init}_S} \right\rVert = \lVert D_0 - D_T \rVert \leqslant \sum_{j = 1}^T \lVert D_j - D_{j - 1} \rVert.
    \]

    从而有

    \begin{align*}
        \lVert D_j - D_{j - 1} \rVert &= \left\lVert \prod_{i = T}^{T - j + 2} \mathsf{Con}_r \cdot e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \cdot \left( \mathsf{Con}_r \cdot e_{x_{T - j + 1}}(\tilde{\mathbf{G}}_{y_{T - j + 1}}^2) - e_{x_{T - j + 1}}(\tilde{\mathbf{G}}_{y_{T - j + 1}}^2) \right) \prod_{i = 1}^{T - j} e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \ket{\text{init}_S} \right\rVert \\
        &\leqslant \left\lVert (\mathrm{id} - \mathsf{Con}_r) \cdot \prod_{i = 1}^{T - j} e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \ket{\text{init}_S} \right\rVert \\
        &\leqslant \frac{\varepsilon}{2T} + \left\lVert (\mathrm{id} - \mathsf{Con}_r) \cdot \text{AKraus}_{\varepsilon / 2T, \mathbf{x}_{T - j}} (\tilde{\mathbf{G}}_{y_1}^2, \ldots, \tilde{\mathbf{G}}_{y_{T - j}}^2) \ket{\text{init}_S} \right\rVert \\
        &\leqslant \frac{\varepsilon}{2T} + \left\lVert (\mathrm{id} - \mathsf{Con}_r) \cdot \mathsf{Con}_r \cdot \text{AKraus}_{\varepsilon / 2T, \mathbf{x}_{T - j}} (\tilde{\mathbf{G}}_{y_1}^2, \ldots, \tilde{\mathbf{G}}_{y_{T - j}}^2) \ket{\text{init}_S} \right\rVert \\
        &\leqslant \frac{\varepsilon}{2T}.
    \end{align*}

    因为 $\text{AKraus}_{\varepsilon / 2T, \mathbf{x}_{T - j}}$ 是一个关于 $\tilde{\mathbf{G}}_{y_i}^2$ 的次数至多为 $r / 2$ 的多项式，所以至多只会将 $r$ 个玻色子从 $0$-动量空间中移除，即作用于初始态后会得到一个严格的 $r$-凝聚态，从而添加 $\mathsf{Con}_r$ 不会改变结果，但 $(\mathrm{id} - \mathsf{Con}_r) \mathsf{Con}_r = 0$，所以最后一项为零. 

    因为凝聚态投影算子是相互对易的，所以对于所有的 $m \geqslant 0$，都有

    \[
        \lVert \mathsf{Con}_m \cdot \mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R \cdot \mathsf{Con}_m \rVert = \lVert \mathsf{Con}_R \cdot \mathsf{Con}_m \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_m \cdot \mathsf{Con}_R \rVert \leqslant \lVert \mathsf{Con}_m \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_m \rVert.
    \]

    而依据 Norm of hopping operators for condensates 的事实，夹心算子 $W = \mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R$ 以 $M = O(1)$ 满足 Truncated Taylor condensate approximation 的第一个条件，并且也容易验证 $W$ 是半正定算子，且满足第二个条件. 因此可以在 $W$ 上应用 AKraus lemma，在 $T = 1$ 以及 $M = O(1)$ 的情况下，得到一个多项式 $\text{AKraus}_{\varepsilon / 4T, x}$ 使得

    \begin{align*}
        \text{AKraus}_{\varepsilon / 4T, x}(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) \cdot \mathsf{Con}_r & \approx_{\varepsilon / 4T} e_x(\tilde{\mathbf{G}}_y^2) \cdot \mathsf{Con}_r \\
        \text{AKraus}_{\varepsilon / 4T, x}(\tilde{\mathbf{G}}_y^2) \cdot \mathsf{Con}_r & \approx_{\varepsilon / 4T} e_x(\tilde{\mathbf{G}}_y^2) \cdot \mathsf{Con}_r.
    \end{align*}

    其中 $\deg(\text{AKraus}_{\varepsilon / 4T, x}) = O((r + 1) \ln (4T / \varepsilon))$. 因为这对所有 $R \geqslant r$ 都成立，所以对于 $R = r + 2 \deg(\text{AKraus}_{\varepsilon / 4T, x}) = r + O((r + 1) \ln (4T / \varepsilon))$ 也成立.

    现在进行第二步混合论证，定义 $C_j$ 为

    \[
        C_j := \prod_{i = T}^{T - j + 1} \mathsf{Con}_r \cdot e_{x_i}(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_{y_i}^2 \cdot \mathsf{Con}_R) \cdot \mathsf{Con}_r \prod_{i = T - j}^0 \mathsf{Con}_r \cdot e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \cdot \mathsf{Con}_r.
    \]

    从而有

    \[
        \left \lVert \left(\prod_{i = T}^1 \mathsf{Con}_r \cdot e_{x_i}(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_{y_i}^2 \cdot \mathsf{Con}_R) \cdot \mathsf{Con}_r - \prod_{i = T}^1 \mathsf{Con}_r \cdot e_{x_i}(\tilde{\mathbf{G}}_{y_i}^2) \cdot \mathsf{Con}_r \right) \right\rVert = \lVert C_0 - C_T \rVert \leqslant \sum_{j = 1}^T \lVert C_j - C_{j - 1} \rVert.
    \]

    限制 $\lVert C_j - C_{j - 1} \rVert$：

    \begin{align*}
        & \lVert C_j - C_{j - 1} \rVert \\
        &\leqslant \left\lVert \mathsf{Con}_r \cdot e_{x_{T - j + 1}}(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_{y_{T - j + 1}}^2 \cdot \mathsf{Con}_R) \cdot \mathsf{Con}_r - \mathsf{Con}_r \cdot e_{x_{T - j + 1}}(\tilde{\mathbf{G}}_{y_{T - j + 1}}^2) \cdot \mathsf{Con}_r \right\rVert \\
        &\leqslant \left\lVert \left(e_{x_{T - j + 1}}(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_{y_{T - j + 1}}^2 \cdot \mathsf{Con}_R) - \text{AKraus}_{\varepsilon / 4T, x_{T - j + 1}}(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_{y_{T - j + 1}}^2 \cdot \mathsf{Con}_R) \right) \cdot \mathsf{Con}_r \right\rVert \\
        &+ \left\lVert \left(e_{x_{T - j + 1}}(\tilde{\mathbf{G}}_{y_{T - j + 1}}^2) - \text{AKraus}_{\varepsilon / 4T, x_{T - j + 1}}(\tilde{\mathbf{G}}_{y_{T - j + 1}}^2) \right) \cdot \mathsf{Con}_r \right\rVert \\
        &+ \left\lVert \left(\text{AKraus}_{\varepsilon / 4T, x_{T - j + 1}}(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_{y_{T - j + 1}}^2 \cdot \mathsf{Con}_R) - \text{AKraus}_{\varepsilon / 4T, x_{T - j + 1}}(\tilde{\mathbf{G}}_{y_{T - j + 1}}^2) \right) \cdot \mathsf{Con}_r \right\rVert \\
        &\leqslant \frac{\varepsilon}{4T} + \frac{\varepsilon}{4T} + 0 \\
        &\leqslant \frac{\varepsilon}{2T}.
    \end{align*}

    因为整个状态都保持在 $r + 2 \deg(\text{AKraus}_{\varepsilon / 4T, x}) \leqslant R$-凝聚态子空间中，所以 $\mathsf{Con}_R$ 的添加不会改变结果，第三项的结果为 $0$.

    最终选择误差为 $\varepsilon := \iota / 2^{2nT}$，并且利用 $\mathsf{S}$ 寄存器上两族算子作用下的状态距离即可完成论证.

## Proving the quasi-even property

在本节中将证明向谕示机 $U$ 进行 $T$ 次查询的任何验证算法，其纯化后的状态也极其接近 $v/4$ 准偶态.

### The double-hopping operator is almost always paired on condensates

在本小节中将表明：将一个双动量跃迁算子作用于准偶凝聚态会产生另一个奇数占据度极难发生改变的准偶凝聚态.

首先定义元组 $w$ 的 $y$-双差分集合，并证明其元素数量的一个界. 简便起见使用以下符号：

\[
    \Delta_{x, x'}^{(y)} := 1_{x \oplus y} + 1_{x' \oplus y} - 1_x - 1_{x'} \in \mathbb{Z}^{2^n}.
\]

!!! info "Definition(Double difference set)"
    给定 $y \in \{0, 1\}^n$，以及 $y \neq 0^n$，定义元组 $w$ 的 $y$-双差分集合为

    \[
        \mathrm{diff}_y^2(w) := \{u \in \mathbb{Z}_{\geqslant 0}^{2^n} : \exists (x, x') \text{ 满足 } x \not \in \{x', x' \oplus y\} \text{ 且 } w = u + \Delta_{x, x'}^{(y)} \}.
    \]

    此外，当 $u \in \mathrm{diff}_y^2(w)$ 时，用 $(x, x') = \mathrm{diff}_y^2(u, w)$ 表示能将 $w$ 映射为 $u$ 的这组 $(x, x')$ 的选择. 不失一般性，令 $x$ 为字典序较小的那个.

!!! note "Claim"
    对于每个 $(R, o)$-准偶凝聚态 $u$，以及任意 $y \in \{0, 1\}^n$，$y \neq 0^n$，有

    \[
        \lvert \mathrm{diff}_y^2(u) \rvert \leqslant (R + 1)^2.
    \]

    ??? note "Proof"
        因为 $u$ 是一个凝聚态，其非 $0$-动量模式下的玻色子数至多为 $R$，因此至多有 $R + 1$ 中选择 $x$ 的方式，以及 $R + 1$ 种选择 $x'$ 的方式，使得加上 $\Delta_{x, x'}^{(y)}$ 后仍然得到一个非负的元组. 对于足够大的 $R$，通常会使用粗略的上界 $2R^2$.

!!! success "Lemma"
    对任意 $R \in [l]$，以及任意 $y \in \{0, 1\}^n$，$y \neq 0^n$，以下成立

    \[
        \left \lVert \sum_{o \in [R]} (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{H}}_y \cdot \mathsf{QEC}_{(R, =o)} \right\rVert \leqslant \frac{R^5}{\sqrt{l}}.
    \]

    ???+ success "Proof"
        通过表明对于每个输入态 $\ket{\psi}$，状态的模长都会缩小一个适当的因子，来论证其算子范数很小. 因为 $o$ 的选择至多有 $R$ 个，因此只需对处于 $\mathsf{QEC}_{(R, =o)}$ 的态 $\ket{\psi}$ 控制 $(\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{H}}_y \ket{\psi}$ 的范数，最后应用三角不等式即可. 将 $\ket{\psi}$ 展开为动量 Fock 态 $\ket{u}$ 的叠加，其中 $u$ 是一个 $(R, =o)$-准偶凝聚态：

        \[
            \ket{\psi} = \sum_{u \in \mathsf{QEC}_{(R, =o)}} \alpha_u \ket{u}.
        \]

        展开双动量跃迁算子，在施加 $\tilde{\mathbf{H}}_y$ 后，得到

        \[
            \tilde{\mathbf{H}}_y \ket{\psi} = \sum_{u \in \mathsf{QEC}_{(R, =o)}} \alpha_u \left(\frac{1}{l} \sum_{x, x' \in \{0, 1\}^n} \sqrt{u_x u_{x'}} (u_{x \oplus y} + 1)(u_{x' \oplus y} + 1) \ket{u + \Delta_{x, x'}^{(y)}} \right).
        \]

        应用投影算子到具有 $o' \neq o$ 个奇数分量的状态上，将会消除求和中所有对应于 $x = x'$ 或 $x = x' \oplus y$ 的项，因为这两种情况的状态的奇数分量数不会发生改变. 因此可以重新分组，并且利用双差分集合的定义，得到

        \begin{align*}
            & (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{H}}_y \ket{\psi} \\
            &= \sum_{u \in \mathsf{QEC}_{(R, =o)}} \left(\frac{\alpha_u}{l} \sum_{x, x' \in \{0, 1\}^n} \delta(u + \Delta_{x, x'}^{(y)} \not \in \mathsf{QE}_{=o}) \sqrt{u_x u_{x'} (u_{x \oplus y} + 1)(u_{x' \oplus y} + 1)} \ket{u + \Delta_{x, x'}^{(y)}} \right) \\
            &= \sum_{u \in \mathsf{QEC}_{(R, =o)}} \frac{\alpha_u}{l} \sum_{x, x' \in \{0, 1\}^n} \sum_{x \not \in \{x', x' \oplus y\}} \delta(u + \Delta_{x, x'}^{(y)} \not \in \mathsf{QE}_{=o}) \sqrt{u_x u_{x'} (u_{x \oplus y} + 1)(u_{x' \oplus y} + 1)} \ket{u + \Delta_{x, x'}^{(y)}} \\
            &= \frac{1}{l} \sum_{w \in \mathsf{QEC}_{(R + 2, o + 4})} \delta(w \not \in \mathsf{QE}_{=o}) \left(\sum_{u \in \mathsf{QEC}_{(R, =o)}} \sum_{u \in \mathrm{diff}_y^2(w)} \sum_{(x, x') = \mathrm{diff}_y^2(u, w)} 2 \alpha_u \sqrt{u_x u_{x'} (u_{x \oplus y} + 1)(u_{x' \oplus y} + 1)} \ket{w} \right).
        \end{align*}

        利用 $\ket{w}$ 的正交性以及 $\mathrm{diff}_y^2(w)$ 中 $u$ 的数量上界，得到

        \begin{align*}
            & \lVert (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{H}}_y \ket{\psi} \rVert^2 \\
            &= \frac{1}{l^2} \left\lVert \sum_{w \in \mathsf{QEC}_{(R + 2, o + 4})} \delta(w \not \in \mathsf{QE}_{=o}) \left(\sum_{u \in \mathsf{QEC}_{(R, =o)}} \sum_{u \in \mathrm{diff}_y^2(w)} \sum_{(x, x') = \mathrm{diff}_y^2(u, w)} 2 \alpha_u \sqrt{u_x u_{x'} (u_{x \oplus y} + 1)(u_{x' \oplus y} + 1)} \ket{w} \right) \right\rVert^2 \\
            &= \frac{4}{l^2} \sum_{w \in \mathsf{QEC}_{(R + 2, o + 4})} \delta(w \not \in \mathsf{QE}_{=o}) \left\lvert \sum_{u \in \mathsf{QEC}_{(R, =o)}} \sum_{u \in \mathrm{diff}_y^2(w)} \sum_{(x, x') = \mathrm{diff}_y^2(u, w)} \alpha_u \sqrt{u_x u_{x'} (u_{x \oplus y} + 1)(u_{x' \oplus y} + 1)} \right\rvert^2 \\
            &\leqslant \frac{4}{l^2} \sum_{w \in \mathsf{QEC}_{(R + 2, o + 4})} \sum_{u \in \mathsf{QEC}_{(R, =o)}} \sum_{u \in \mathrm{diff}_y^2(w)} 2 R^2 \cdot u_x u_{x'} (u_{x \oplus y} + 1)(u_{x' \oplus y} + 1) \cdot \lvert \alpha_u \rvert^2 \\
            &\leqslant \frac{8}{l^2} \sum_{w \in \mathsf{QEC}_{(R + 2, o + 4})} \sum_{u \in \mathrm{diff}_y^2(w)} l R^5 \cdot \lvert \alpha_u \rvert^2 \\
            &\leqslant \frac{8}{l^2} \sum_u \lvert \alpha_u \rvert^2 l R^5 \cdot \lvert \mathrm{diff}_y^2(u) \rvert \\
            &\leqslant \frac{16 R^7}{l}.
        \end{align*}

        开方即可获得

        \[
            \lVert (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{H}}_y \ket{\psi} \rVert \leqslant \frac{4 R^{7 / 2}}{\sqrt{l}}.
        \]

        因为 $o$ 最多只能和 $R$ 一样大，运用三角不等式就可以将从 $0$ 到 $R$ 的所有 $o$ 的求和范数控制在 $4 R^{9 / 2} / \sqrt{l} \leqslant R^5 / \sqrt{l}$.

    上述约束对 $\tilde{\mathbf{H}}_y$ 成立，但是希望将其推广到 $\tilde{\mathbf{G}}_y^2 = \tilde{\mathbf{H}}_y + \mathrm{id}$ 上.

    !!! success "Corollary"
        对任意 $R \in [l]$，以及任意 $y \in \{0, 1\}^n$，$y \neq 0^n$，以下成立

        \[
            \left \lVert \sum_{o \in [R]} (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{QEC}_{(R, =o)} \right\rVert \leqslant \frac{R^5}{\sqrt{l}}.
        \]

        ??? success "Proof"
            因为 $\tilde{\mathbf{G}}_y^2 = \tilde{\mathbf{H}}_y + \mathrm{id}$，所以直接应用引理即可得到

            \begin{align*}
                & \left \lVert \sum_{o \in [R]} (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{QEC}_{(R, =o)} \right\rVert \\
                &= \left \lVert \sum_{o \in [R]} (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{H}}_y \cdot \mathsf{QEC}_{(R, =o)} + \sum_{o \in [R]} (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \mathsf{QE}_{=o} \cdot \mathsf{Con}_R \right\rVert \\
                &= \left \lVert \sum_{o \in [R]} (\mathrm{id} - \mathsf{QE}_{=o}) \cdot \tilde{\mathbf{H}}_y \cdot \mathsf{QEC}_{(R, =o)} + 0 \right\rVert \\
                &\leqslant \frac{R^5}{\sqrt{l}}.
            \end{align*}

### Dyson series expansion of the exponential

本节将展示如何应用指数函数的 Dyson 级数，将以上引理提升到关于双动量跃迁算子某些函数上.

!!! note "Fact"
    1. (Application of Duhamel's principle). 以下恒等式对所有矩阵 $A$，$V$ 和 $t \geqslant 0$ 均成立：

        \[
            \exp(-t \cdot (A + V)) = \exp(-t \cdot A) - \int_{0 \leqslant s \leqslant t} \mathrm{d}s \exp(-(t - s) \cdot (A + V)) \cdot V \cdot \exp(-s \cdot A).
        \]

        通过在最外层将该恒等式对自变量进行代换，即可得到如下针对 $A$ 的微扰的 Dyson 级数.

    2. (Dyson's formula for the exponential function). 对于任意矩阵 $A$，$V$ 和 $\kappa \geqslant 0$，将 $\exp{-\kappa \cdot (A + V)} - \exp{-\kappa \cdot A}$ 表示为：

        \[
            \sum_{k = 1}^{\infty} \int_{0 \leqslant s_1 \leqslant \ldots \leqslant s_k \leqslant \kappa} \mathrm{d} \mathbf{s} \exp(-(\kappa - s_k)A) \cdot \underbrace{V \cdot \exp(-(s_k - s_{k - 1}) A) \cdot V \cdots V}_{k \text{ times}} \exp(-s_1 A).
        \]

        Dyson 公式的目的是按如下方式展开指数 $\exp(-\kappa \cdot (A + V))$：展开式中只包含项 $V$ 的乘积和 $A$ 的指数函数. 使用场景是当 $V$ 是一个与 $A$ 共同施加的微小扰动时，Dyson 公式允许展开指数并应用已知的关于 $V$ 的界.

将应用其证明双动量跃迁算子的指数只会以极低概率改变奇数分量的数量.

!!! success "Lemma"
    对于所有满足 $\kappa \leqslant 1$，$R \leqslant l^{1/10} / 2$，以及 $1 \leqslant d \leqslant R$ 的参数，以下成立：

    \[
        \left \lVert \sum_{o \in [R]} \mathsf{QE}_{\geqslant o + d} \cdot \exp(-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)) \cdot \mathsf{QE}_o \right\rVert \leqslant \left( \frac{2 R^5}{\sqrt{l}} \right)^{d / 4}.
    \]

    ??? success "Proof"
        对 $\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R$ 进行如下展开以应用 Dyson 公式：

        \[
            \mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R = \underbrace{\sum_{o \in [R]} \mathsf{QEC}_{(R, =o)} \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{QEC}_{(R, =o)}}_{A} + \underbrace{\sum_{o, o' \in [R], o \neq o'} \mathsf{QEC}_{(R, =o)} \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{QEC}_{(R, =o')}}_{V}. 
        \]

        注意到 $V = \mathsf{Con}_R \cdot \sum_{o'} (\mathrm{id} - \mathsf{QE}_{=o'}) \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{QE}_{=o'}$，其范数可以被以上推论控制. 而利用 $\tilde{\mathbf{G}}_y^2$ 至多只能移动 $2$ 个玻色子的事实，以及 $A$ 的定义，有
        
        \[
            V \cdot \mathsf{QE}_o = \mathsf{QE}_{o + 4} \cdot V \cdot \mathsf{QE}_o, \quad A \cdot \mathsf{QE}_o = \mathsf{QE}_o \cdot A \cdot \mathsf{QE}_o.
        \]

        因为 $\mathsf{QE}_o$ 和 $A$ 对易，所以其和 $e^{-\kappa A}$ 也对易. 从而有 $\mathsf{QE}_{\geqslant o + d} \cdot e^{-\kappa A} \cdot \mathsf{QE}_o = 0$，这样便可以丢弃掉 Dyson 公式中的第一项 $\exp(-\kappa A)$. 并且因为 $V$ 只能增加最多 $4$ 个奇数分量，所以对于 $d' < d/4$，以及 $0 \leqslant s_1 \leqslant \ldots \leqslant s_{d'} \leqslant \kappa$，有

        \[
            \mathsf{QE}_{\geqslant o + d} \cdot \exp(-(\kappa - s_{d'})A) \cdot \underbrace{V \cdots V}_{d' \text{ times}} \cdot \exp(-s_1 A) \cdot \mathsf{QE}_o = 0.
        \]

        最终应用 Dyson 公式，得到

        \begin{align*}
            & \left \lVert \mathsf{QE}_{\geqslant o + d} \cdot \exp(-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)) \cdot \mathsf{QE}_o \right\rVert \\
            &= \left \lVert \sum_{k \geqslant d / 4} \int_{0 \leqslant s_1 \leqslant \ldots \leqslant s_k \leqslant \kappa} \mathrm{d} \mathbf{s} \ \mathsf{QE}_{\geqslant o + d} \cdot \exp(-(\kappa - s_k)A) \cdot V \cdots V \cdot \exp(-s_1 A) \cdot \mathsf{QE}_o \right\rVert \\
            &\leqslant \sum_{k \geqslant d / 4} \int_{0 \leqslant s_1 \leqslant \ldots \leqslant s_k \leqslant \kappa} \mathrm{d} \mathbf{s} \left\lVert \mathsf{QE}_{\geqslant o + d} \cdot \exp(-(\kappa - s_k)A) \cdot V \cdots V \cdot \exp(-s_1 A) \cdot \mathsf{QE}_o \right\rVert \\
            &\leqslant \sum_{k \geqslant d / 4} \int_{0 \leqslant s_1 \leqslant \ldots \leqslant s_k \leqslant \kappa} \mathrm{d} \mathbf{s} \lVert V \rVert^k \\
            &\leqslant \sum_{k \geqslant d / 4} \left(\frac{R^5}{\sqrt{l}}\right)^k = \frac{1}{1 - R^5 / \sqrt{l}} \cdot \left(\frac{R^5}{\sqrt{l}}\right)^{\lceil d / 4 \rceil} \\
            &\leqslant 2 \cdot \left(\frac{R^5}{\sqrt{l}}\right)^{d / 4} \\
            & \leqslant \left(\frac{2 R^5}{\sqrt{l}}\right)^{d / 4}.
        \end{align*}

        因为 $A$ 不会改变奇数分量的数量，所以其指数函数也不会改变奇数分量的数量，非零输出便需要至少 $d / 4$ 个 $V$ 的作用. 积分项的消去利用了当 $\kappa \leqslant 1$ 时，$\int_{0 \leqslant s_1 \leqslant \ldots \leqslant s_k \leqslant \kappa} \mathrm{d} \mathbf{s} = \frac{\kappa^k}{k!} \leqslant 1$. 

### Recursive bounds on the oddness of products of operators

本小节通过组合方法证明多次施加双动量跃迁算子后，仍然不会显著增加奇数分量的数量. 

!!! success "Lemma"
    令 $\Pi_0 \preccurlyeq \Pi_1 \preccurlyeq \ldots$ 为 Hilbert 空间 $\mathcal{H}$ 上的一族投影算子. 设 $A_1, \ldots, A_t$ 为 $\mathcal{H}$ 上的一族算子，满足 $\lVert A_i \rVert \leqslant 1$. 假设对于所有整数 $a, b \geqslant 0$，都有 $\lVert (\mathrm{id} - \Pi_{a + b}) \cdot A_i \cdot \Pi_a \rVert \leqslant \varepsilon^{b + 1}$，则对于所有整数 $\lambda \geqslant 0$ 以及满足 $\Pi_0 \ket{\psi} = \ket{\psi}$ 的态 $\ket{\psi}$，都有

    \[
        \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_t \cdots A_1 \ket{\psi} \rVert \leqslant \binom{t + \lambda}{t - 1} \varepsilon^{\lambda + 1}.
    \]

    ??? success "Proof"
        当 $t = 1$ 时，结论显然成立. 接下来定义 $\Pi_{-1} := 0$，并且对 $j = 0, \ldots, \lambda$，令 $\Delta_j := \Pi_j - \Pi_{j - 1}$，因为投影算子的偏序性，所以有 $\Delta_j = \Pi_j \cdot (\mathrm{id} - \Pi_{j - 1})$. 进而

        \begin{align*}
            \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_{t + 1} \cdots A_1 \ket{\psi} \rVert &\leqslant \underbrace{\sum_{j = 0}^\lambda \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_{t + 1} \cdot \Delta_j \cdot A_t \cdots A_1 \Pi_0 \ket{\psi} \rVert}_{(A)} \\
            &+ \underbrace{\lVert (\mathrm{id} - \Pi_\lambda) \cdot A_{t + 1} \cdot (\mathrm{id} - \Pi_\lambda) \cdot A_t \cdots A_1 \Pi_0 \ket{\psi} \rVert}_{(B)} \\
        \end{align*}

        为了约束 $(B)$ 项，使用数学归纳法：

        \begin{align*}
            \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_{t + 1} \cdot (\mathrm{id} - \Pi_\lambda) \cdot A_t \cdots A_1 \Pi_0 \ket{\psi} \rVert &\leqslant \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_{t + 1} (\mathrm{id} - \Pi_\lambda) \rVert \cdot \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_t \cdots A_1 \Pi_0 \ket{\psi} \rVert \\
            &\leqslant \underbrace{\lVert A_{t + 1} \rVert}_{\leqslant 1} \cdot \binom{t + \lambda}{t - 1} \varepsilon^{\lambda + 1}
        \end{align*}

        而对于 $(A)$ 项，根据归纳法

        \begin{align*}
            \sum_{j = 0}^\lambda \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_{t + 1} \cdot \Delta_j \cdot A_t \cdots A_1 \Pi_0 \ket{\psi} \rVert &= \sum_{j = 0}^\lambda \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_{t + 1} \cdot \Pi_j(\mathrm{id} - \Pi_{j - 1}) \cdot A_t \cdots A_1 \Pi_0 \ket{\psi} \rVert \\
            &\leqslant \sum_{j = 0}^\lambda \lVert (\mathrm{id} - \Pi_\lambda) \cdot A_{t + 1} \cdot \Pi_j \rVert \cdot \lVert (\mathrm{id} - \Pi_{j - 1}) \cdot A_t \cdots A_1 \Pi_0 \ket{\psi} \rVert \\
            &\leqslant \sum_{j = 0}^\lambda \varepsilon^{\lambda - j + 1} \cdot \binom{t + j - 1}{t - 1} \varepsilon^{j} \\
            &= \binom{t + \lambda}{t} \varepsilon^{\lambda + 1}.
        \end{align*}

        相加得到

        \[
            (A) + (B) \leqslant \left(\binom{t + \lambda}{t} + \binom{t + \lambda}{t - 1}\right) \varepsilon^{\lambda + 1} = \binom{t + 1 + \lambda}{t} \varepsilon^{\lambda + 1}.
        \]

        归纳证明完成.

### Wrapping up the proof

本小节中将证明对 $U$ 进行关于 $n$ 的多项式次查询的算法，其状态在几何距离上与 $\mathsf{QE}_{v / 4}$ 子空间为指数级接近.

!!! success "Lemma"
    对于所有的 $y \in \{0, 1\}^n$，$y \neq 0^n$，$\kappa \leqslant 1$，$R \leqslant l^{1/10} / 2$，以及 $1 \leqslant d \leqslant R$，有

    \[
        \left \lVert \sum_{o \in [R]} \mathsf{QE}_{\geqslant o + d} \cdot \sqrt{1 - \frac{1}{2} \exp (-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R))} \cdot \mathsf{QE}_o \right\rVert \leqslant \left( \frac{64 R^5}{\sqrt{l}} \right)^{d / 4}.
    \]

    ??? success "Proof"
        将前两个引理应用到平方根的二项式展开来实现证明.

        \[
            \sqrt{1 + x} = \sum_{k = 0}^{\infty} \binom{1/2}{k} x^k.
        \]

        从而有

        \[
            \sqrt{1 - \frac{1}{2} \exp (-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R))} = \sum_{k = 0}^{\infty} \binom{1/2}{k} \left(-\frac{1}{2}\right)^k \exp(-k \kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)).
        \]

        取 $\lambda = d - 1$，$\Pi_0 = \mathsf{QE}_o \preccurlyeq \Pi_1 = \mathsf{QE}_{o + 1} \preccurlyeq \ldots \preccurlyeq \Pi_{o + d - 1}$，$A_1 = \cdots = A_t = \exp(-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R))$.

        \begin{align*}
            & \left \lVert \mathsf{QE}_{\geqslant o + d} \cdot \sqrt{1 - \frac{1}{2} \exp (-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R))} \cdot \mathsf{QE}_o \right\rVert \\
            &= \left\lVert \sum_{k = 0}^{\infty} \binom{1/2}{k} \left(-\frac{1}{2}\right)^k \mathsf{QE}_{\geqslant o + d} \cdot \exp(-k \kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)) \cdot \mathsf{QE}_o \right\rVert \\
            &\leqslant \sum_{k = 1}^{\infty} \left\lvert \binom{1/2}{k} \right\rvert \left(\frac{1}{2}\right)^k \left\lVert \mathsf{QE}_{\geqslant o + d} \cdot \exp(-k \kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)) \cdot \mathsf{QE}_o \right\rVert \\
            &\left(\frac{2 R^5}{\sqrt{l}}\right)^{d / 4} \sum_{k = 1}^{\infty} \left\lvert \binom{1/2}{k} \right\rvert \left(\frac{1}{2}\right)^k \binom{k + d}{k - 1} \\
            &\leqslant \left(\frac{2 R^5}{\sqrt{l}}\right)^{d / 4} \cdot 2^{d + 1} \\
            &\leqslant \left(\frac{64 R^5}{\sqrt{l}}\right)^{d / 4}.
        \end{align*}

        其中

        \begin{align*}
            \sum_{k = 1}^{\infty} \left\lvert \binom{1/2}{k} \right\rvert \left(\frac{1}{2}\right)^k \binom{k + d}{k - 1} &\leqslant \sum_{k = 1}^{\infty} \left(\frac{1}{2}\right)^k \binom{k + d}{k - 1} \\
            &=\frac{1}{2} \sum_{k = 0}^{\infty} \left(\frac{1}{2}\right)^k \binom{(d + 2) + k - 1}{k} \\
            &= \frac{1}{2} \cdot \sum_{k = 0}^{\infty} \left(-\frac{1}{2}\right)^k \binom{-(d + 2)}{k} \\
            &= \frac{1}{2} \cdot \left(1 - \frac{1}{2}\right)^{-(d + 2)} \\
            &= 2^{d + 1}.
        \end{align*}

        首先利用了对于 $k \geqslant 1$，$\lvert \binom{1/2}{k} \rvert \leqslant 1$，然后使用了二项式系数的恒等式 $\binom{-a}{b} = (-1)^b \binom{a + b - 1}{b}$，最后使用了二项式定理 $\sum_{k = 0}^{\infty} \binom{n}{k} x^k = (1 + x)^n$.

!!! success "Lemma(Single query preserves quasi-evenness)"
    对于所有 $o, R \leqslant l^{1/10} / 2$，$1 \leqslant d \leqslant R$，作用在 $\mathsf{A}$ 寄存器上且满足 $\lVert A \rVert \leqslant 1$ 的算子 $A$，以下不等式成立

    \[
        \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\sum_y A \cdot \ket{y} \bra{y} \otimes \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right)\right) \mathsf{QE}_o \right\rVert \leqslant \left(\frac{2^{14} R^5}{\sqrt{l}}\right)^{d / 4}.
    \]

    ??? success "Proof"
        按如下展开范数

        \begin{align*}
            & \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\sum_y A \cdot \ket{y} \bra{y} \otimes \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right)\right) \mathsf{QE}_o \right\rVert \\
            &= \left\lVert \sum_y A \cdot \ket{y} \bra{y} \otimes \mathsf{QE}_{\geqslant o + d} \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right) \mathsf{QE}_o \right\rVert \\
            &\leqslant \sum_y \left\lVert \ket{y} \bra{y} \otimes \mathsf{QE}_{\geqslant o + d} \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right) \mathsf{QE}_o \right\rVert \\
            &\leqslant \max_y \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right) \mathsf{QE}_o \right\rVert \\
            &\leqslant \max_y \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right) \mathsf{QE}_o \right\rVert \\
            &+ \max_y \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right) \mathsf{QE}_o \right\rVert \\
            &\leqslant \underbrace{\max_y \left\lVert \mathsf{QE}_{\geqslant o + d} \cdot e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) \cdot \mathsf{QE}_o \right\rVert}_{(A)} \\
            &+ \underbrace{\max_y \left\lVert \mathsf{QE}_{\geqslant o + d} \cdot e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) \cdot \mathsf{QE}_o \right\rVert}_{(B)}.
        \end{align*}

        对 $(A)$ 和 $(B)$ 项分别应用引理进行约束.

        \begin{align*}
            (A) &= \max_y \sqrt{2} \left\lVert \mathsf{QE}_{\geqslant o + d} \cdot e^{(-\kappa / 2) \cdot (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)} \sqrt{1 - \frac{1}{2} e^{-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)}} \cdot \mathsf{QE}_o \right\rVert \\
            &\leqslant \sqrt{2} (d + 1) \left(\frac{64 R^5}{\sqrt{l}}\right)^{d / 4}.
        \end{align*}

        此处取 $\lambda = d - 1$，$\Pi_0 = \mathsf{QE}_o \preccurlyeq \Pi_{d - 1} = \mathsf{QE}_{o + d - 1}$，$A_1 = \sqrt{1 - \frac{1}{2} e^{-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)}}$，$A_2 = \cdots = A_{d + 1} = e^{(-\kappa / 2) \cdot (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)}$.

        \begin{align*}
            (B) &\leqslant \max_y \left\lVert \mathsf{QE}_{\geqslant o + d} \cdot (\mathrm{id} - e^{-\kappa (\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)}) \cdot \mathsf{QE}_o \right\rVert \\
            &\leqslant \left(\frac{2 R^5}{\sqrt{l}}\right)^{d / 4}.
        \end{align*}

        从而

        \[
            (A) + (B) \leqslant 2d \left(\frac{64 R^5}{\sqrt{l}}\right)^{d / 4} \leqslant \left(\frac{2^{14} R^5}{\sqrt{l}}\right)^{d / 4}.
        \]

    !!! success "Corollary(Single controlled query preserves quasi-evenness)"
        对于所有 $o, R \leqslant l^{1/10} / 2$，$1 \leqslant d \leqslant R$，作用在 $\mathsf{A}$ 寄存器上且满足 $\lVert A \rVert \leqslant 1$ 的算子 $A$，以下不等式成立

        \[
            \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\sum_{y, b} A \cdot \ket{b, y} \bra{b, y} \otimes \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right)\right)^b \mathsf{QE}_o \right\rVert \leqslant \left(\frac{2^{14} R^5}{\sqrt{l}}\right)^{d / 4}.
        \]

        ??? success "Proof"
            简单的三角不等式应用：

            \begin{align*}
                & \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\sum_{y, b} A \cdot \ket{b, y} \bra{b, y} \otimes \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right)\right)^b \mathsf{QE}_o \right\rVert \\
                &\leqslant \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\sum_{y} A \cdot \ket{1, y} \bra{1, y} \otimes \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right) \right) \mathsf{QE}_o \right\rVert \\
                &+ \left\lVert \mathsf{QE}_{\geqslant o + d} \left(\sum_{y} A \cdot \ket{0, y} \bra{0, y} \otimes \mathrm{id} \right) \mathsf{QE}_o \right\rVert \\
                &\leqslant \left(\frac{2^{14} R^5}{\sqrt{l}}\right)^{d / 4} + 0.
            \end{align*}


!!! note "Theorem"
    设 $\mathcal{A}$ 为向谕示机 $U$ 发起 $T$ 次查询的任意算法，且 $v \in \mathbb{Z}_{\geqslant 0}$ 是 $4$ 的倍数. 那么存在常数 $c$，使得对于足够大的 $n$，算法纯化后的状态与 $(c \cdot T^10, v/4)$-准偶凝聚态子空间的补空间的投影的重叠度被如下约束：

    \[
        \left\lVert (\mathrm{id} - \mathsf{QEC}_{(c \cdot T^{10}, v / 4)}) \ket{\psi_{\mathrm{PQ} } } \right\rVert ^2 \leqslant \left( \left(\frac{T^4}{l^{1/32} } \right)^v + e^{-5T} \right)^2.
    \]

    ??? note "Proof"
        不失一般性，假设 $T \geqslant n$. 应用 Sandwiching theorem，取 $\iota = e^{-5T}$，这样便存在整数 $r = O(T^{10})$，$R = O(T^{13})$，使得

        \[
            \left\lVert \ket{\psi_{\mathrm{PQ}}} - \ket{\psi_{R, r}} \right\rVert \leqslant e^{-5T}.
        \]

        接下来取 $\lambda = v / 4$，$\Pi_0 = \mathsf{QEC}_{(r, 0)} \preccurlyeq \cdots \preccurlyeq \Pi_{v / 4} = \mathsf{QEC}_{(r, v / 4)}$，$A_i$ 为

        \[
            A_i = \left(\sum_{y, b} A \cdot \ket{b, y} \bra{b, y} \otimes \left(\tilde{X}_{\mathsf{U}_y} \otimes e_1(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R) + \tilde{Z}_{\mathsf{U}_y} \otimes e_0(\mathsf{Con}_R \cdot \tilde{\mathbf{G}}_y^2 \cdot \mathsf{Con}_R)\right)\right)^b.
        \]

        总共有 $T \leqslant l^{1/10}/2$ 个算子 $A_i$，并且初始状态处于 $\mathsf{QE}_0$ 中，所以有

        \begin{align*}
            \left\lVert (\mathrm{id} - \mathsf{QEC}_{(c \cdot T^{10}, v / 4)}) \ket{\psi_{R, r}} \right\rVert &\leqslant \binom{T + v / 4}{T - 1} \left(\frac{2^{14} R^5}{\sqrt{l}}\right)^{(v / 4 + 1)/4} \\
            &\leqslant (2T)^{v / 4} \left(\frac{2^{14} R^5}{\sqrt{l}}\right)^{v / 16} \\
            &\leqslant \left(\frac{2^(18) R^5 T^4}{\sqrt{l}}\right)^{v / 16}.
        \end{align*}

        二者结合得到

        \begin{align*}
            \left\lVert (\mathrm{id} - \mathsf{QEC}_{(c \cdot T^{10}, v / 4)}) \ket{\psi_{\mathrm{PQ}}} \right\rVert &\leqslant \left(\frac{2^(18) R^5 T^4}{\sqrt{l}}\right)^{v / 16} + e^{-5T} \\
            &\leqslant \left(\left(\frac{4 R^{5/16} T^{1/4}}{l^{1/32}}\right)^v + e^{-5T}\right).
        \end{align*}

        因为 $R = c \cdot T^{13}$，$r = c \cdot T^{10}$，所以对于足够大的 $T$，有 $4R^{5/16} T^{1/4} \leqslant T^4$，从而得到最终的约束.

!!! note "Proof(Sampling probability upper bound)"
    设 $\ket{\psi_{\mathrm{PQ}}}$ 为算法对 $U$ 进行 $vt$ 次查询后得到的状态，那么对于 $\Pi_\mathrm{succ}$，有

    \begin{align*}
        \lVert \Pi_\mathrm{succ} \ket{\psi_{\mathrm{PQ}}} \rVert^2 &\leqslant \lVert \Pi_\mathrm{succ} \mathsf{QEC}_{(c \cdot T^{10}, v / 4)} \ket{\psi_{\mathrm{PQ}}} \rVert^2 + \lVert (\mathrm{id} - \mathsf{QEC}_{(c \cdot T^{10}, v / 4)}) \ket{\psi_{\mathrm{PQ}}} \rVert^2 \\
        &\leqslant 2 \left( \frac{4 v ((vt)^{30} + v(vt)^{20}) \sqrt{l} }{2^{n/4} } \right)^v + \left( \left( \frac{(vt)^4}{l^{1/32} } \right)^v + e^{-5vt} \right)^2.
    \end{align*}

## Property-testing and oracle separations

!!! note "Theorem"
    考虑任意选择常数 $a \geqslant 0$ 以及所有 $n \geqslant n_0$ 下满足 $t(n) \leqslant a n^a$ 和 $q(n) \leqslant a n^a$ 的函数 $t(n)$ 和 $q(n)$. 令 $n_0$ 为 Good samplers from $\mathsf{QCMA}$ algorithms 和 Sampling probability upper bound 在代入 $t = t(n)$，$q = q(n)$ 以及 $v = 1000q$ 时成立的最小整数. 那么对于任意 $n \geqslant n_0$，以及对大小为 $n$ 的谕示机对 $(S, U)$ 进行 $t(n)$ 次查询，具有长度为 $q(n)$ 的经典见证的二进制输出量子查询算法 $\mathcal{A}$，必然存在一对大小为 $n$ 的谕示机 $(S^*, U^*)$ 满足以下条件之一：

    1. $(S^*, U^*)$ 至少是 $59/100$-谱相关的，但对于长度为 $q(n)$ 的所有经典见证 $w$，其接受概率满足

        \[
            \Pr{\mathcal{A}^{(S^*, U^*)}(w) = 1} \leqslant \frac{2}{3}.
        \]
    
    2. $(S^*, U^*)$ 至多是 $57/100$-谱相关的，但存在一个长度为 $q(n)$ 的经典见证 $\tilde{w}$，使得其接受概率满足

        \[
            \Pr{\mathcal{A}^{(S^*, U^*)}(\tilde{w}) = 1} \geqslant \frac{1}{3}.
        \]

    ???+ note "Proof"
        如果上述结论不成立，则算法 $\mathcal{A}$ 就可以正确分类所有保证为至少 $59/100$-谱相关或至多 $57/100$-谱相关的规模为 $n$ 的实例. 但是，设置 $l = 2^{n / 10}$ 以及 $v = 1000q$，代入 $\kappa = 1/10$ 和 $\rho = 2 l^2 / (2^n \ln(2^n / 2l^4))$，并且使用 Good samplers from $\mathsf{QCMA}$ algorithms 和 The strong yes property 引理，就能够产生一个当 $(S, U)$ 采样自 $\mathsf{Strong}$ 分布时，以 $O(t^{-1000q})$ 的概率输出 $v$ 个点的采样器.

        另一方面，只要 $t, q \leqslant a n^a$，应用 Sampling probability upper bound 定理会对 $\mathsf{Strong}$ 分布给出一个至多为 $O((\op{poly}(n) 2^{-n/160})^{1000q})$ 的采样概率上界. 对于足够大的 $n$，有 $(\op{poly}(n) 2^{-n/160})^{1000q} \ll t^{-1000q}$，从而产生矛盾.