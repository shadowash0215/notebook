# Compressed Permutation Oracles

## Preliminaries

### Quantum

给定纯态 $\ket{\psi}$，其密度矩阵为 $\rho(\ket{\psi}) = \ket{\psi}\bra{\psi}$. 密度矩阵的迹范数定义为 $\lVert \rho \rVert_1 = \op{Tr}(\sqrt{\rho^\dagger \rho})$. 

!!! success "Lemma"
    设 $\rho, \tau$ 为 $\mathcal{H}$ 上的密度矩阵，最大区分概率为

    \[
        D(\rho, \tau) = \frac{1}{2} \lVert \rho - \tau \rVert_1.
    \]

Uhlmann 定理通过构建纯化寄存器之间的等距映射来约束两个密度矩阵之间的迹距离.

!!! success "Lemma"
    设 $\ket{\psi}_{AB} \in \mathcal{A} \otimes \mathcal{B}$， $\ket{\phi}_{AC} \in \mathcal{A} \otimes \mathcal{C}$ 是归一化量子态，再设等距映射 $V: \mathcal{C} \to \mathcal{B}$. 记 $\sigma_A = \op{Tr}_B(\rho(\ket{\psi}))$， $\tau_A = \op{Tr}_C(\rho(\ket{\phi}))$ 为敌手寄存器 $A$ 上的约化密度矩阵，则有

    \[
        \frac{1}{2} \lVert \sigma_A - \tau_A \rVert_1 \leq \lVert \ket{\psi}_{AB} - V \ket{\phi}_{AC} \rVert.
    \]

    ???+ success "Proof"
        \begin{align*}
            \lVert \sigma_A - \tau_A \rVert_1 &= \lVert \op{Tr}_B(\rho(\ket{\psi})) - \op{Tr}_C(\rho(\ket{\phi})) \rVert_1 \\
            &= \lVert \op{Tr}_B(\rho(\ket{\psi})) - \op{Tr}_B(\rho(V \ket{\phi})) \\
            &\leq \lVert \rho(\ket{\psi}) - \rho(V \ket{\phi}) \rVert_1 \\
            &\leq 2 \lVert \ket{\psi}_{AB} - V \ket{\phi}_{AC} \rVert.
        \end{align*}

!!! success "Lemma"
    设 $\mathcal{H} = \mathcal{H}_1 \oplus \cdots \oplus \mathcal{H}_k$ 为 Hilbert 空间，$O: \mathcal{H} \to \mathcal{H}$ 可以分解为 $O = O_1 \oplus \cdots \oplus O_k$，其中 $O_i: \mathcal{H}_i \to \mathcal{H}_i$，那么有

    \[
        \lVert O \rVert = \max_{i \in [k]} \lVert O_i \rVert.
    \]

### Notation and definitions

**数据库**：$\mathbf{F}_{M, N}$ 表示从 ${[M]}$ 到 $[N]$ 的所有函数构成的集合，$\mathbf{S}_N$ 表示从 $[N]$ 上所有的置换构成的集合，$\mathbf{D}_{M, N}$ 表示从 $[M]$ 到 $[N]$ 的所有部分函数构成的集合，也可看作所有以下函数：

\[
    D: [M] \to [N] \cup \{\perp\},
\]

所构成的集合，其中 $D(x) = \perp$ 表示 $D$ 在 $x$ 上未定义. $\mathbf{I}_{M, N}$ 表示从 $[M]$ 到 $[N]$ 的所有部分单射，等价的，其由所有以下函数：

\[
    I: [M] \to [N] \cup \{\perp\},
\]

构成，并且除 $\perp$ 外，保持单射性.

本文几乎总是使用 $I_{N, N}$ 和 $D_{\sqrt{N}, \sqrt{N}}$，其中 $N = 4^n$. 完整函数被视为部分函数的特殊情况，因此有 $\mathbf{F}_{M, N} \subseteq \mathbf{D}_{M, N}$，$\mathbf{S}_N \subseteq \mathbf{I}_{N, N}$. 

部分函数和完整函数统称为数据库. 对于 $D \in \mathbf{D}_{M, N}$，其定义域为 $\op{Dom}(D) = \{x \in [M] \mid D(x) \neq \perp\}$，其值域为 $\op{Im}(D) = \{D(x) \mid x \in \op{Dom}(D)\}$. 数据库的大小定义为 $\lvert D \rvert = \lvert \op{Dom}(D) \rvert$.

当 $M, N$ 已从上下文确定时，用 $\mathbf{D}_t := \{D \in \mathbf{D} \mid \lvert D \rvert = t\}$ 表示大小恰为 $t$ 的数据库集合，用 $\mathbf{D}_{\leq t} := \{D \in \mathbf{D} \mid \lvert D \rvert \leq t\}$ 表示大小至多为 $t$ 的数据库集合. 

$\mathbf{\perp}$ 表示空数据库. 给定 $D \in \mathbf{D}_{M, N}$，$D[x \mapsto y]$ 表示数据库：

\[
    D[x \mapsto y](x') = \begin{cases}
        y, & x' = x, \\
        D(x'), & x' \neq x.
    \end{cases}
\]

对于部分单射可以类似地定义 $I[x \mapsto y]$，但如果已经存在另一个输入映射到 $y$，则需要将其条目删除：

\[
    I[x \mapsto y](x') = \begin{cases}
        y, & x' = x, \\
        \perp, & x' \neq x, y \neq \perp, I(x') = y, \\
        I(x'), & x' \neq x, y = \perp \text{ or } I(x') \neq y.
    \end{cases}
\]

给定 $D \in \mathbf{D}$，定义

\[
    D \vert^x := \{D[x \mapsto y] \mid y \in [N] \cup \{\perp\}\},
\]

其表示所有与 $D$ 在 $x$ 以外完全相同的数据库. 定义 $\mathbf{D} \vert^x := \{D \in \mathbf{D} \mid x \not \in \op{Dom}(D)\}$，其表示所有在 $x$ 上未定义的数据库. 对于任何固定的 $x$，集合族 $\{D \vert^x \mid D \in \mathbf{D} \vert^x\}$ 构成 $\mathbf{D}$ 的划分.

对于单射数据库，维持其单射性质是必不可缺的，因此有

\[
    I \vert^x := \{I[x \mapsto y] \mid y \in (N \setminus \op{Im}(I)) \cup \{I(x)\} \cup \{\perp\}\}.
\]

给定集合 $S$，$x \sim S$ 表示从 $S$ 中均匀随机选择一个元素 $x$. 对于 $x \in \{0, 1\}^{2n}$，用 $x_L$ 表示 $x$ 的前 $n$ 位，用 $x_R$ 表示 $x$ 的后 $n$ 位. 

**空间**：给定集合 $S$，$\mathcal{H}(S)$ 表示由 $S$ 中元素标记的单位正交基张成的 Hilbert 空间. 即 $\mathcal{H}(S) = \op{span}\{\ket{x} \mid x \in S\}$，$\innerproduct{x}{x'} = \delta_{x, x'}$.

对于任意集合 $A \subseteq S$，

\[
    \ket{+_A} = \frac{1}{\sqrt{\lvert A \rvert}} \sum_{x \in A} \ket{x},
\]

表示 $A$ 中所有元素的均匀叠加态. 若 $A_1, \ldots, A_l$ 两两不交并且 $\bigcup_{i = 1}^l A_i = S$，则他们构成 $S$ 的一个划分，此时 $\mathcal{H}(S) = \bigoplus_{i = 1}^l \mathcal{H}(A_i)$.

本文经常使用数据库空间 $\mathcal{H}(\mathbf{D})$ 以及其单射数据库子空间 $\mathcal{H}(\mathbf{I}) \leq \mathcal{H}(\mathbf{D})$. 在此基础上定义数据库大小投影算子

\[
    \Pi^t := \sum_{D \in \mathbf{D}_t} \ket{D}\bra{D}, \quad \Pi^{\leq t} := \sum_{k = 0}^t \Pi^k.
\]

$\lVert \cdot \rVert$ 表示标准 $L_2$ 范数，对算子则表示相应的诱导范数. $\lVert \cdot \rVert_1$ 表示迹范数. 对于 Hilbert 空间 $\mathcal{H}_\mathsf{A} \otimes \mathcal{H}(\mathbf{D})$ 或 $\mathcal{H}_\mathsf{A} \otimes \mathcal{H}(\mathbf{I})$，$\lVert \cdot \rVert_{\leq t}$ 表示将数据库大小限制到至多为 $t$ 的标准 $L_2$ 范数. 具体而言，对空间 $\mathcal{H}_{\mathsf{AI}} = \mathcal{H}_\mathsf{A} \otimes \mathcal{H}(\mathbf{I})$ 上的状态 $\ket{\psi}$ 或算子 $O$，有

\[
    \lVert \ket{\psi}_{\mathsf{A I}} \rVert_{\leq t} = \lVert \Pi_\mathsf{I}^{\leq t} \ket{\psi}_{\mathsf{A I}} \rVert, \quad \lVert O_{\mathsf{A I}} \rVert_{\leq t} = \lVert O_{\mathsf{A I}} \Pi_\mathsf{I}^{\leq t} \rVert.
\]

定义数据库的一致性投影，对于 $\mathcal{H}(\mathbf{F}_{M, N})$ 上的数据库以及输入-输出对 $(x, y) \in [M] \times [N]$，定义

\[
    \Pi^{(x, y) \in \mathsf{db}} := \sum_{D \in \mathbf{D}: D(x) = y} \ket{D}\bra{D}.
\]

### Compressed oracles

设 $M$ 和 $N$ 都是 $2$ 的幂次，并将 $[M]$ 和 $[N]$ 中的元素通过自然映射表示为比特串. 从 $\mathbf{F}_{M, N}$ 中均匀随机选择函数，并考虑如下的谕示机：

\[
    \mathcal{O}_f \ket{x, y}_\mathsf{X Y} := \ket{x, y \oplus f(x)}_\mathsf{X Y}.
\]

设量子算法 $\mathcal{A}^{\mathcal{O}_f}$ 对 $\mathcal{O}_f$ 进行 $q$ 次查询，算法内部的工作空间和查询寄存器统一记为 Hilbert 空间 $\mathcal{H}_\mathsf{A}$，算法在各次谕示机查询之间执行的酉变换记为 $A_0, \ldots, A_q$，查询寄存器 $X, Y$ 均被视作 $A$ 的一部分. 算法得到的最终混合态为

\[
    \rho_\mathcal{A}^{(\mathcal{O}_f)} = \mathbb{E}_{f \sim \mathbf{F}_{M, N}} [\rho(A_q \mathcal{O}_f \cdots A_1 \mathcal{O}_f A_0 \ket{0})].
\]

不过也可以考虑纯化整个实验，引入函数真值表寄存器 $\mathcal{H}_\mathsf{F} = \mathcal{H}(\mathbf{F})$，并定义纯化谕示机：

\[
    \mathsf{P}_\mathsf{X Y F} \ket{x, y}_\mathsf{X Y} \ket{f}_{F} := \ket{x, y \oplus f(x)}_\mathsf{X Y} \ket{f}_{F}.
\]

将纯化寄存器初始化为所有函数的均匀叠加：

\[
    \ket{+_\mathbf{F}} = \frac{1}{\sqrt{\lvert \mathbf{F}_{M, N} \rvert}} \sum_{f \in \mathbf{F}_{M, N}} \ket{f},
\]

而后运行纯化谕示机，并利用偏迹去除掉纯化寄存器，得到的攻击者视图为

\[
    \rho_\mathcal{A}^{(\mathcal{O}_f)} = \op{Tr}_F(\rho(A_{q, \mathsf{A}} \mathsf{P}_\mathsf{A F} \cdots A_{1, \mathsf{A}} \mathsf{P}_\mathsf{A F} A_{0, \mathsf{A}} \ket{0}_\mathsf{A} \ket{+_\mathbf{F}}_\mathsf{F})).
\]

压缩谕示机提供了另一种分析可量子访问随机函数的表示. 在此情况下，纯化寄存器是一张初始化为空的数据库，每次查询只修改数据库中与查询点相对应的位置，类似于经典的懒采样.

固定一个在 $x$ 上未定义的数据库 $D \in \mathbf{D}_{M, N}, x \not \in \op{Dom}(D)$，考虑局部子空间 $\mathcal{H}(D \vert^x) \leq \mathcal{H}(\mathbf{D})$，即所有只在 $x$ 上与 $D$ 不同的数据库所张成的空间. 定义：

\[
    \ket{+_{x, D}} = \frac{1}{\sqrt{N}} \sum_{y \in [N]} \ket{D[x \mapsto y]},
\]

这便是在 $x$ 处填入一个均匀随机输出的量子叠加. 在 $\mathcal{H}(D \vert^x)$ 上定义函数压缩算子 $\mathsf{fC}$，其由 $x, D$ 索引：

\[
    \mathsf{fC}_{x, D} := \mathrm{id} - \ket{+_{x, D}}\bra{+_{x, D}} - \ket{D}\bra{D} + \ket{+_{x, D}}\bra{D} + \ket{D}\bra{+_{x, D}}.
\]

换言之，该算子交换状态 $\ket{D}$ 和 $\ket{+_{x, D}}$. 因为 $\{D \vert^x \mid D \in \mathbf{D} \vert^x\}$ 构成 $\mathbf{D}$ 的划分，因此可以定义全局压缩算子，以及由查询寄存器控制的受控操作：

\[
    \mathsf{fC}_x := \bigoplus_{D \in \mathbf{D} \vert^x} \mathsf{fC}_{x, D}, \quad \mathsf{fC}_\mathsf{X D} \ket{x}_\mathsf{X} := \ket{x}_\mathsf{X} \otimes \mathsf{fC}_{x, \mathsf{D}}.
\]

接下来扩展纯化谕示机 $\mathsf{P}$，定义为

\[
    \mathsf{P} \ket{x, y} \ket{D} := \begin{cases}
        \ket{x, y \oplus D(x)} \ket{D}, & x \in \op{Dom}(D) \\
        \ket{x, y} \ket{D}, & x \not \in \op{Dom}(D)
    \end{cases}.
\]

而后就可以得到压缩函数谕示机

\[
    \mathsf{cfO}_\mathsf{X Y P} := \mathsf{fC}_\mathsf{X P} \cdot \mathsf{P}_\mathsf{X Y P} \cdot \mathsf{fC}_\mathsf{X P}^\dagger,
\]

纯化寄存器允许包含部分函数，$\mathcal{H}_D = \mathcal{H}(\mathbf{D})$，该寄存器初始化为空数据库，所有的纯化谕示机调用都替换为 $\mathsf{cfO}$，对应的最终状态为

\[
    \ket{\psi_\mathcal{A}^\mathsf{cfO}}_\mathsf{A D} = A_{q, \mathsf{A}} \mathsf{cfO}_\mathsf{A D} \cdots A_{1, \mathsf{A}} \mathsf{cfO}_\mathsf{A D} A_{0, \mathsf{A}} \ket{0}_\mathsf{A} \ket{\perp}_\mathsf{D}.
\]

!!! success "Lemma"
    1. (Soundness) 查询压缩谕示机的算法的视图和查询真随机函数的算法的视图一致,

        \[
            \rho_{\mathcal{A}, \mathsf{A}}^{(\mathcal{O}_f)} = \op{Tr}_D[\ket{\psi_\mathcal{A}^\mathsf{cfO}}\bra{\psi_\mathcal{A}^\mathsf{cfO}}_\mathsf{A D}].
        \]

    2. (Bounded growth) 经过 $q$ 次查询后，压缩谕示机的最终状态完全支撑在定义域大小之多为 $q$ 的部分函数上,

        \[
            \ket{\psi_\mathcal{A}^\mathsf{cfO}} \in \mathcal{H}_\mathsf{A} \otimes \mathcal{H}(\mathbf{D}_{\leq q}).
        \]

    3. (Fundamental lemma) 敌手找到 $l$ 对谕示机的输入-输出对的概率指数级接近这 $l$ 个对就位于压缩数据库中的概率.

        \[
            \lVert \Pi^{(\mathcal{O}_f)}_\mathsf{A D} \ket{\psi_\mathcal{A}^\mathsf{cfO}} \rVert \leq \lVert \Pi^{(\mathsf{cfO})}_\mathsf{A D} \ket{\psi_\mathcal{A}^\mathsf{cfO}} \rVert + \sqrt{\frac{l}{N}}.
        \]

        两个投影算子分别代表这些点是否和真正的随机函数一致，以及是否出现在压缩谕示机的数据库中.

        \begin{align*}
            \Pi^{(\mathsf{cfO})}_\mathsf{A D} &:= \sum_{\{(x_1, y_1), \ldots, (x_l, y_l)\} \in ([M] \times [N])^{\times l}} (\Pi^{(x_1, y_1) \in \mathsf{db}} \cdots \Pi^{(x_l, y_l) \in \mathsf{db}})_\mathsf{D} \\ 
            & \otimes (\ket{x_1, y_1, \ldots, x_l, y_l}\bra{x_1, y_1, \ldots, x_l, y_l} \otimes \mathrm{id})_\mathsf{A}, \\
            \Pi^{(\mathcal{O}_f)}_\mathsf{A D} &:= \sum_{\{(x_1, y_1), \ldots, (x_l, y_l)\} \in ([M] \times [N])^{\times l}} (\mathsf{fC}_{x_1} \Pi^{(x_1, y_1) \in \mathsf{db}} \mathsf{fC}_{x_1}^\dagger \cdots \mathsf{fC}_{x_l} \Pi^{(x_l, y_l) \in \mathsf{db}} \mathsf{fC}_{x_l}^\dagger)_\mathsf{D} \\ 
            & \otimes (\ket{x_1, y_1, \ldots, x_l, y_l}\bra{x_1, y_1, \ldots, x_l, y_l} \otimes \mathrm{id})_\mathsf{A}.
        \end{align*}

如果考虑对空数据库 $\ket{\perp}_\mathsf{D}$ 施加解压算子 $\mathsf{fC}_x^\dagger$，则得到

\[
    \mathsf{fC}_x^\dagger \ket{\perp}_\mathsf{D} = \frac{1}{\sqrt{N}} \sum_{y \in [N]} \ket{(x, y)}_\mathsf{D},
\]

显然 $x$ 处的输出是良定的. 这一性质在压缩谕示机查询中也得以保留.

更正式地说，定义压缩子空间和解压子空间. 向前者的投影定义为 $\Xi$，后者定义为 $\Gamma$. 对于固定的输入 $x$，定义为

\[
    \Gamma_x := \sum_{D \in \mathsf{D} \ \mathrm{s.t.} \ x \in \op{Dom}(D)} \ket{D}\bra{D}, \quad \Xi_x := \mathsf{fC}_x^\dagger \Gamma_x \mathsf{fC}_x.
\]

因为不同位置上的投影算子是可交换的，所以定义

\[
    \Gamma = \prod_{x \in [M]} \Gamma_x, \quad \Xi = \prod_{x \in [M]} \Xi_x.
\]

标准纯化谕示机保持 $\Gamma$ 不变，而压缩谕示机保持 $\Xi$ 不变. 

!!! success "Lemma"
    1. 对任意 $\ket{\psi} \in \Xi$，有 $\mathsf{cfO} \ket{\psi} \in \Xi$.

    2. 固定输入 $x \in [M]$，对于 $D \in D \vert^x$，选择集合 $S_{x, D} \subset [N]$ 使得 $\lvert S_{x, D} \rvert \geq N - t$. 令 $\ket{S_{x, D}} = \frac{1}{\sqrt{\lvert S_{x, D} \rvert}} \sum_{y \in S_{x, D}} \ket{D[x \mapsto y]}$，定义算子

        \begin{align*}
            G_{x, D} &:= 1 - \ket{D}{\bra{D}} - \ket{S_{x, D}}\bra{S_{x, D}} + \ket{D}\bra{S_{x, D}} + \ket{S_{x, D}}\bra{D}, \\
            G_x &:= \bigoplus_{D \in \mathbf{D} \vert^x} G_{x, D},
        \end{align*}

        则有

        \[
            \lVert \mathsf{fC}_x - G_x \rVert = O\left(\sqrt{\frac{t}{N}}\right).
        \]

    3. 固定输入 $x \in [M]$，令 $R$ 为辅助寄存器，设 $\ket{\phi_y}_R$ 为一族由 $y \in [N]$ 索引，两两正交的量子态，考虑如下形式的量子态：

        \[
            \ket{\psi}_{D R} = \sum_{D \in \mathbf{D}, D(x) \neq \perp} \alpha_D \ket{D}_D \ket{\phi_{D(x)}}_R,
        \]

        这意味着数据库外部存在一份关于 $x$ 的输出值的正交记录. 那么对于 $G_{x, D}$，有

        \[
            \lVert (\mathrm{id}_{R D} - G_{x, D}) \ket{\psi}_{D R} \rVert = O\left(\sqrt{\frac{1}{N - t}}\right).
        \]

## Compressed permutation oracles

设 $\varphi \sim \mathbf{S}_N$ 为均匀随机选择的置换，考虑如下的谕示机：

\[
    \mathcal{O}_\varphi \ket{b, x}_\mathsf{X} \ket{y}_\mathsf{Y} := \ket{b, x}_\mathsf{X} \ket{y \oplus \varphi^(1 - 2b)(x)}_\mathsf{Y}.
\]

设 $\mathcal{A}^{\mathcal{O}_\varphi}$ 为对 $\mathcal{O}_\varphi$ 进行 $q$ 次查询的量子算法，算法内部状态空间为 Hilbert 空间 $\mathcal{H}_\mathsf{A}$，在查询之间执行的酉变换为 $A_0, \ldots, A_q$，则算法的最终混合态为

\[
    \rho_\mathcal{A}^{(\mathcal{O}_\varphi)} = \mathbb{E}_{\varphi \sim \mathbf{S}_N} [\rho(A_q \mathcal{O}_\varphi \cdots A_1 \mathcal{O}_\varphi A_0 \ket{0})].
\]

固定 $I \in \mathbf{I}$，以及 $x \in [N] \setminus \op{Dom}(I)$，考虑局部子空间 $\mathcal{H}(I \vert^x) \leq \mathcal{H}(\mathbf{I})$，定义状态：

\[
    \ket{+_{x, I}} = \frac{1}{\sqrt{N - \lvert I \rvert}} \sum_{y \in [N] \setminus \op{Im}(I)} \ket{I[x \mapsto y]},
\]

接下来便可以在此子空间上定义置换压缩谕示机 $\mathsf{pC}$，其由 $x, I$ 索引：

\[
    \mathsf{pC}_{x, I} := \mathrm{id} - \ket{+_{x, I}}\bra{+_{x, I}} - \ket{I}\bra{I} + \ket{+_{x, I}}\bra{I} + \ket{I}\bra{+_{x, I}}.
\]

因为 $\{I \vert^x \mid I \in \mathbf{I} \vert^x\}$ 构成 $\mathbf{I}$ 的划分，因此可以定义全局压缩算子，以及由查询寄存器控制的受控操作：

\[
    \mathsf{pC}_x := \bigoplus_{I \in \mathbf{I} \vert^x} \mathsf{pC}_{x, I}, \quad \mathsf{pC}_\mathsf{X I} \ket{x}_\mathsf{X} := \ket{x}_\mathsf{X} \otimes \mathsf{pC}_{x, \mathsf{I}}.
\]

接下来扩展纯化谕示机 $\mathsf{P}$，定义为

\[
    \mathsf{P} \ket{x, y} \ket{I} := \begin{cases}
        \ket{x, y \oplus I(x)} \ket{I}, & x \in \op{Dom}(I) \\
        \ket{x, y} \ket{I}, & x \not \in \op{Dom}(I)
    \end{cases}.
\]

还需要定义反转算子 $\mathsf{F}$，用以反转整个数据库. 因为 $I^{-1}(y) = x \neq \perp$ 当且仅当 $I(x) = y$，否则 $I^{-1}(y) = \perp$，因此可以定义反转算子 $\mathsf{F}$：

\[
    \mathsf{F} \ket{I} := \ket{I^{-1}}.
\]

整个过程都需要维护数据库的单射性. 全局压缩置换谕示机定义为

\[
    \mathsf{cpO} \ket{b} := \ket{b} \otimes \begin{cases}
        \mathsf{pC} \cdot \mathsf{P} \cdot \mathsf{pC}^\dagger, & b = 0, \\
        \mathsf{F} \cdot \mathsf{pC} \cdot \mathsf{P} \cdot \mathsf{pC}^\dagger \cdot \mathsf{F}^\dagger, & b = 1.
    \end{cases}
\]

取纯化寄存器 $\mathcal{H}_\mathsf{I} = \mathcal{H}(\mathbf{I})$，初始化为空数据库 $\ket{\perp}_\mathsf{I}$，所有的纯化谕示机调用都替换为 $\mathsf{cpO}$，对应的最终状态为

\[
    \ket{\psi_\mathcal{A}^\mathsf{cpO}}_\mathsf{A I} = A_{q, \mathsf{A}} \mathsf{cpO}_\mathsf{A I} \cdots A_{1, \mathsf{A}} \mathsf{cpO}_\mathsf{A I} A_{0, \mathsf{A}} \ket{0}_\mathsf{A} \ket{\perp}_\mathsf{I}.
\]

### Properties

!!! success "Lemma"
    1. (Soundness) 查询压缩置换谕示机的高效算法的视图和查询真随机置换的算法的视图的距离是可忽略的,

        \[
            \rho_{\mathcal{A}, \mathsf{A}}^{(\mathcal{O}_\varphi)} \overset{\mathrm{negl}}{\approx} \op{Tr}_\mathsf{I}[\rho(\ket{\psi_\mathcal{A}^\mathsf{cpO}}_\mathsf{A I})].
        \]
        
    2. (Bounded growth) 经过 $q$ 次查询后，压缩置换谕示机的最终状态完全支撑在定义域大小之多为 $q$ 的部分单射上,

        \[
            \Pi_{\leq q, \mathsf{I}} \ket{\psi_\mathcal{A}^\mathsf{cpO}}_\mathsf{A I} = \ket{\psi_\mathcal{A}^\mathsf{cpO}}_\mathsf{A I}.
        \]

    3. (Fundamental Lemma) $t$ 次查询后，敌手找到 $l$ 对谕示机的输入-输出对的概率指数级接近这 $l$ 个对就位于压缩数据库中的概率.

        \[
            \lVert \Pi^{(\mathcal{O}_\varphi)}_\mathsf{A I} \ket{\psi_\mathcal{A}^\mathsf{cpO}}_\mathsf{A I} \rVert \leq \lVert \Pi^{(\mathsf{cpO})}_\mathsf{A I} \ket{\psi_\mathcal{A}^\mathsf{cpO}}_\mathsf{A I} \rVert + O\left(\frac{l}{\sqrt{N - t - l}}\right).
        \]

        两个投影算子分别代表这些点是否和真正的随机置换一致，以及是否出现在压缩谕示机的数据库中.

        \begin{align*}
            \Pi^{(\mathsf{cpO})}_\mathsf{A I} &:= \left(\sum_{\{(x_1, y_1), \ldots, (x_l, y_l)\} \in [N]^{2l}} \Pi^{(x_1, y_1) \in \mathsf{db}} \cdots \Pi^{(x_l, y_l) \in \mathsf{db}}\right)_\mathsf{I} \\
            &\otimes \left(\ket{x_1, y_1, \ldots, x_l, y_l}\bra{x_1, y_1, \ldots, x_l, y_l} \otimes \mathrm{id}\right)_\mathsf{A}, \\
            \Pi^{(\mathcal{O}_\varphi)}_\mathsf{A I} &:= \left(\sum_{\{(x_1, y_1), \ldots, (x_l, y_l)\} \in [N]^{2l}} \mathsf{pC}_{x_1} \Pi^{(x_1, y_1) \in \mathsf{db}} \mathsf{pC}_{x_1}^\dagger \cdots \mathsf{pC}_{x_l} \Pi^{(x_l, y_l) \in \mathsf{db}} \mathsf{pC}_{x_l}^\dagger\right)_\mathsf{I} \\
            &\otimes \left(\ket{x_1, y_1, \ldots, x_l, y_l}\bra{x_1, y_1, \ldots, x_l, y_l} \otimes \mathrm{id}\right)_\mathsf{A}.
        \end{align*}

## Purified permutations

考虑两个随机置换 $\pi, \omega \in \mathsf{S}_N$，二者称为外层置换；以及三个随机函数 $h, k, f: \{0, 1\}^n \to \{0, 1\}^n$，称为内层 Feistel 网络. $h, k, f$ 为均匀随机函数，但是 $(\pi, \omega)$ 的分布不做要求. 元组定义了置换 $\varphi_{(\pi, \omega, h, k, f)}$，作用为 $\varphi_{(\pi, \omega, h, k, f)}(x) = y$，其中的内部结构为：

\begin{align*}
    \pi(x) &= u, \\
    u_R \oplus h(u_L) &= m, \\
    u_L \oplus k(m) &= v_L, \\
    m \oplus f(v_L) &= v_R, \\
    y &= \omega(v).
\end{align*}

整个系统称为掩码 Feistel 网络. 纯化空间为 $\mathcal{H}_\mathsf{P} = \mathcal{H}(\mathbf{S}_N)^{\otimes 2} \otimes \mathcal{H}(\mathbf{F}_{\sqrt{N}, \sqrt{N}})^{\otimes 3}$，五个寄存器分别记为 $\mathsf{\Pi}, \mathsf{\Omega}, \mathsf{H}, \mathsf{K}, \mathsf{F}$. 

### Query analysis

定义纯化查询算子 $\mathsf{mfP}$，其作用为

\[
    \mathsf{mfP} \ket{x, y}_\mathsf{X Y} \ket{\pi, \omega, h, k, f}_\mathsf{P} := \ket{x, y \oplus \varphi_{(\pi, \omega, h, k, f)}(x)}_\mathsf{X Y} \ket{\pi, \omega, h, k, f}_\mathsf{P}.
\]

设 $\mathcal{D}$ 为 $\mathbf{S}_N^{\times 2}$ 上的分布，外层置换从 $\mathcal{D}$ 中采样，初始纯化态可以写作：

\[
    \ket{\psi_0}_\mathsf{P} = \sum_{\pi, \omega \in \mathbf{S}_N} \sqrt{p_\mathcal{D}(\pi, \omega)} \ket{\pi, \omega}_\mathsf{\Pi \Omega} \otimes \frac{1}{\sqrt{(2^n)^{3 \cdot 2^n}}} \sum_{h, k, f \in \mathbf{F}_{2^n, 2^n}} \ket{h, k, f}_\mathsf{H K F}.
\]

解压序列被称作掩码 Feistel 解压操作，记为 $\mathsf{mfC}^\dagger$，$\mathsf{mfC}$ 自然指掩码 Feistel 压缩操作. 记 $D_h, D_k, D_f$ 分别为寄存器 $\mathsf{H}, \mathsf{K}, \mathsf{F}$ 中的数据库，进行以下操作：

1. 在输入 $u_L$ 处解压 $D_h$，其中 $u = \pi(x)$；
2. 在输入 $u_R \oplus D_h(u_L)$ 处解压 $D_k$；
3. 在输入 $u_L \oplus D_k(u_R \oplus D_h(u_L))$ 处解压 $D_f$.

接下来便可以正式定义压缩算子 $\mathsf{mfC}$，定义

\begin{align*}
    U_{u, \mathsf{H}}^{(H)} &:= \mathsf{fC}_{u_L, \mathsf{H}} \\
    U_{u, \mathsf{H K}}^{(K)} \ket{D_h}_\mathsf{H} &:= \ket{D_h}_\mathsf{H} \otimes \begin{cases}
        \mathrm{id}_\mathsf{K}, & u_L \not \in \op{Dom}(D_h), \\
        \mathsf{fC}_{u_R \oplus D_h(u_L), \mathsf{K}}, & u_L \in \op{Dom}(D_h),
    \end{cases} \\
    U_{u, \mathsf{H K F}}^{(F)} \ket{D_h, D_k}_\mathsf{H K} &:= \ket{D_h, D_k}_\mathsf{H K} \otimes \begin{cases}
        \mathrm{id}_\mathsf{F}, & u_L \not \in \op{Dom}(D_h) \\
        \mathrm{id}_\mathsf{F}, & u_R \oplus D_h(u_L) \not \in \op{Dom}(D_k) \\
        \mathsf{fC}_{u_L \oplus D_k(u_R \oplus D_h(u_L)), \mathsf{F}}, & u_L \in \op{Dom}(D_h), u_R \oplus D_h(u_L) \in \op{Dom}(D_k).
    \end{cases} \\
    U_{u, \mathsf{H K F}} & := U_{u, \mathsf{H}}^{(H)} U_{u, \mathsf{H K}}^{(K)} U_{u, \mathsf{H K F}}^{(F)}.
\end{align*}

接下来加上外层置换：

\begin{align*}
    \mathsf{mfC}_{x, \mathsf{\Pi H K F}} &:= \ket{\pi}_\mathsf{\Pi} \otimes U_{\pi(x), \mathsf{H K F}} \\
    \mathsf{mfC}_\mathsf{X \Pi H K F} \ket{x}_\mathsf{X} &:= \ket{x}_\mathsf{X} \otimes \mathsf{mfC}_{x, \mathsf{\Pi H K F}}.
\end{align*}

类似反转算子 $\mathsf{F}$，定义外层置换反转算子 $\mathsf{mfF}$，其作用为

\[
    \mathsf{mfF}_\mathsf{P} \ket{\pi}_\mathsf{\Pi} \ket{\omega}_\mathsf{\Omega} \ket{D_h}_\mathsf{H} \ket{D_k}_\mathsf{K} \ket{D_f}_\mathsf{F} := \ket{\omega^{-1}}_\mathsf{\Pi} \ket{\pi^{-1}}_\mathsf{\Omega} \ket{D_f}_\mathsf{H} \ket{D_k}_\mathsf{K} \ket{D_h}_\mathsf{F}.
\]

该算子逆向整条路径，并且交换了两个外层置换，以及寄存器 $\mathsf{H}$ 和 $\mathsf{F}$ 的数据库. 如果纯化 $P$ 代表置换 $\varphi_P$，则其反转纯化 $P'$ 满足 $\mathsf{mfF} \ket{P} = \ket{P'}$，并且其代表的置换为 $\varphi_{P'} = \varphi_P^{-1}$. 于是可以定义压缩掩码 Feistel 谕示机：

\[
    \mathsf{cmfO} \ket{b} = \ket{b} \otimes \begin{cases}
        \mathsf{mfC} \cdot \mathsf{mfP} \cdot \mathsf{mfC}^\dagger, & b = 0, \\
        \mathsf{mfF} \cdot \mathsf{mfC} \cdot \mathsf{mfP} \cdot \mathsf{mfC}^\dagger \cdot \mathsf{mfF}^\dagger, & b = 1.
    \end{cases}
\]

记 $D = (D_h, D_k, D_f) \in \mathbf{F}_{2^n, 2^n}^{\times 3}$ 为纯化寄存器 $\mathsf{H K F}$ 中的数据库，记 $P = (\pi, \omega, D)$ 为纯化寄存器的可能状态，$\mathbf{P}$ 为所有可能状态的集合. 可能状态的大小由其中最大的数据库大小定义，即 $\lvert P \rvert := \max\{\lvert D_h \rvert, \lvert D_k \rvert, \lvert D_f \rvert\}$. 

### Internal Feistel

!!! info "Definition"
    固定 $D = (D_h, D_k, D_f)$，如果存在 $m$，使得 $u_R \oplus D_h(u_L) = v_R \oplus D_f(v_L) = m$，且 $u_L \oplus v_L = D_k(m)$，则称存在从 $u$ 到 $v$ 的**链**（chain），$(u, m, v)$ 定义了整条链，且 $(u_L, m, v_L)$ 为链的输入端.

从输入 $u$ 向右求解的时候，如果遇到未定义的数据库值，则链会被截断，称为**半链**（semi-chain）. 半链的长度依据最近未定义值的距离而定义，如果 $D_h(u_L) = \perp$，则半链长度为 $0$；如果 $D_k(D_h(u_L) \oplus u_R) = \perp$，则半链长度为 $1$；如果 $D_f(D_k(D_h(u_L) \oplus u_R) \oplus u_L) = \perp$，则半链长度为 $2$；链是特殊的半链，长度为 $3$.

在固定 $D$ 的情况下，如果存在 $u$ 到 $v$ 的链，则称 $D$ 支撑输入输出对 $(u, v)$，所有被 $D$ 支撑的输入输出对构成了一个部分单射，记为 $\mathsf{supp}(D)$，并简写 $\mathsf{Dom}(D) := \mathsf{Dom}(\mathsf{supp}(D))$，$\mathsf{Im}(D) := \mathsf{Im}(\mathsf{supp}(D))$. $D(u)$ 表示 $\mathsf{supp}(D)(u)$，$D^{-1}(v)$ 也是类似的. 如果 $u \in \mathsf{Dom}(D)$，那么 $D[u \mapsto \perp]$ 表示将 $D$ 中的链删除所得到的数据库.

如果两条链在同一轮函数中的输入相同，则称它们碰撞.

!!! info "Definition"
    $(u, m, v) \neq (u', m', v')$ 是 $D$ 中的两条链，如果 $u_L = u'_L$、$m = m'$ 或 $v_L = v'_L$，则称它们碰撞.

数据库三元组 $D = (D_h, D_k, D_f)$ 中如果没有碰撞的链，且三个数据库的每个表项都恰好参与了一条链，则称 $D$ 是**典则的**（canonical），所有典则数据库的集合记作 $\mathbf{C} \subset \mathbf{D}_{2^n, 2^n}^{\times 3}$，$\mathbf{C}_t$ 表示数据库大小均为 $t$ 的典则数据库的集合. 

!!! success "Lemma"
    令 $D = (D_h, D_k, D_f) \in \mathbf{C}_t$，则其包含 $t$ 条链 $u_1 \to v_1, \ldots, u_t \to v_t$，且 $u_i$ 和 $v_i$ 内两两互异；包含 $t(t - 1)$ 条长度为 $2$ 的右向半链；包含 $t(2^n - t)$ 条长度为 $1$ 的右向半链；包含 $(2^n - t)2^n$ 条长度为 $0$ 的右向半链. 左向半链的数量与右向半链的数量相同. 

给定包含 $t$ 个输入输出对的部分单射 $I$，用 $\mathbf{D}(I)$ 表示支撑 $I$ 的典则数据库的集合. 当以下条件之一成立时，该集合为空集：

!!! info "Definition"
    1. 输入左侧碰撞：存在互异的 $x, x' \in \mathsf{Dom}(I)$，使得 $x_L = x'_L$；
    2. 输出左侧碰撞：存在互异的 $y, y' \in \mathsf{Im}(I)$，使得 $y_L = y'_L$；
    3. 内部状态左侧碰撞：存在 $(x, y) \in I$，$x' \in \mathsf{Dom}(I)$，$y' \in \mathsf{Im}(I)$，$(x, y) \neq (x', y')$，使得 $x_L \oplus y_L = x'_L \oplus y'_L$.

如果以上事件均未发生，即 $\mathbf{D}(I) \neq \varnothing$，则称 $I$ 是**可行的**（allowable）. 记所有的 $\mathbf{A}_t \subset \mathbf{I}_t$ 为可行数据库的集合.

!!! success "Lemma"
    以上条件刻画了所有不可行数据库.

    ???+ success "Proof"
        $(\Leftarrow)$ 如果 $I$ 可行，那么可以构造一个恰好支撑 $I$ 的典则数据库 $D$，将 $I$ 表示为 $I = (u_1, v_1), \ldots, (u_t, v_t)$，从空数据库 $D = (D_h, D_k, D_f)$ 开始，依照以下算法构造数据库：

        \algorithm
            \caption{数据库扩展算法}
            \KwResult{}
            $\text{对每个 } j \in [t]$;
            $\enspace \text{选择满足 } (u_j)_R \oplus z_j \not \in \operatorname{Dom}(D_k) \text{ 的 } z_j, \text{ 添加 } ((u_j)_L, z_j) \text{ 到 } D_h$;
            $\enspace \text{添加 } ((u_j)_R \oplus z_j, (u_j)_L \oplus (v_j)_L) \text{ 到 } D_k$;
            $\enspace \text{添加 } ((v_j)_L, (v_j)_R \oplus z_j \oplus (u_j)_R) \text{ 到 } D_f$;

        经过了 $j - 1$ 次迭代后，第 $1$ 步的 $z_j$ 还有 $2^n - (j - 1)$ 个可选项. 所有形如 $u = (u_j)_L \Vert z_R, z_R \in \{0, 1\}^n$ 的输入在 $D_h$ 中都映射到了 $z_j$，此时产生了 $2^n$ 个长度为 $1$ 的半链；计算 $z_R \oplus z_j$ 会得到 $D_k$ 的输入，其中的 $j - 1$ 个输入映射到了 $m_i, i \in [j - 1]$，被扩展成了长度为 $2$ 的半链；但这些半链不会被扩展为长度为 $3$ 的链，假设其映射到了 $m_i$，那么 $D_k(m_i) = (u_i)_L \oplus (v_i)_L$，此时的 $(v_j)_L = (u_j)_L \oplus (u_j)_L \oplus (v_j)_L$，可行性保证该值不等于任何已存在的 $(v_p)_L, p \in [t]$，因此不会产生长度为 $3$ 的链. 

        第 $2$ 步会衔接先前的长度为 $1$ 的半链中的一条，即以 $u_j = (u_j)_L \Vert (u_j)_R$ 为输入，$z_j$ 为中间值的半链；但其也会扩展输入形如 $(u_i)_L \Vert (z_i \oplus (u_j)_R \oplus z_j), i \in [j - 1]$ 的半链，将长度扩展为 $2$，但依然不会产生长度为 $3$ 的链，因为不存在内部状态左侧碰撞. 

        所以每次迭代都会增加一条从 $u_j$ 到 $v_j$ 的链，且不会引入新的链，并且得到的数据库显然是极小的. 因此最终得到的数据库 $D$ 是支撑 $I$ 的典则数据库.

!!! success "Lemma"
    对任意 $I \in \mathbf{A}_t$，有 $\lvert \mathbf{D}(I) \rvert = (2^n)_t = \frac{2^n!}{(2^n - t)!}$.

!!! info "Definition"
    设 $A \in \mathbf{A}_t$，且 $u \not \in \mathsf{Dom}(A)$，称 $A$ 允许输入 $u$，若存在 $v \in \{0, 1\}^{2n}$，使得 $A[u \mapsto v] \in \mathbf{A}_{t + 1}$，记为 $A \heartsuit u$. 如果 $A[u \mapsto v]$ 依然保持可行性，那么记 $A \heartsuit (u, v)$，并称 $(u, v)$ 是可行的.

    !!! tip "Remark"
        如果 $A \heartsuit u$，且 $2t^2 < 2^n$，那么对于任何满足 $u'_L = u_L$ 的 $u' \not \in \mathsf{Dom}(A)$，都有 $A \heartsuit u'$，至少有 $2^n - t^2$ 个这样的 $u'$.

!!! info "Definition"
    固定 $A \in \mathbf{A}_t$，以及 $u \in \{0, 1\}^{2n}$，并且 $A \heartsuit u$，定义集合 $\mathbf{V}_{u, A}$ 为所有满足 $A \heartsuit (u, v)$ 的 $v \in \{0, 1\}^{2n}$ 的集合，以及 $\mathbf{L}_{u, A}$ 为 $\mathbf{V}_{u, A}$ 中所有 $v$ 的左侧部分的集合，即

    \begin{align*}
        \mathbf{V}_{u, A} &:= \{v \in \{0, 1\}^{2n} \mid A \heartsuit (u, v)\}, \\
        \mathbf{L}_{u, A} &:= \{v_L \in \{0, 1\}^n \mid v \in \mathbf{V}_{u, A}\}.
    \end{align*}

    而显然对于满足 $u'_L = u_L$ 的 $u' \not \in \mathsf{Dom}(A)$，都有 $\mathbf{V}_{u, A} = \mathbf{V}_{u', A}$，所以可以只使用 $u_L$ 来索引 $\mathbf{V}_{u, A}$，将其记为 $l$，那么以上集合可以记作 $\mathbf{V}_{l, A}$ 和 $\mathbf{L}_{l, A}$.

!!! success "Lemma"
    对任意 $A \in \mathbf{A}_t$，以及 $u \in [N] \setminus \mathsf{Dom}(A)$ 满足 $A \heartsuit u$，有

    \[
        \lvert \mathbf{L}_{u, A} \rvert \geq 2^n - 2t^2 - 2t.
    \]

    并且对于任意 $l \in \mathbf{L}_{u, A}$，以及 $r \in \{0, 1\}^n$，都有 $l \Vert r \in \mathbf{V}_{x, A}$.

    ???+ success "Proof"
        $A[u \mapsto v]$ 可能会导致从以下两种方面导致内部状态左侧碰撞：

        1. 存在 $u' \in \mathsf{Dom}(A) \cup \{u\}$，$v' \in \mathsf{Im}(A) \cup \{v\}$，且 $(u', v') \neq (u, v)$，使得

            \[
                u_L' \oplus v_L' = u_L \oplus v_L.
            \]

        2. 存在 $u' \in \mathsf{Dom}(A) \cup \{u\}$，$(u'', v'') \in A$，使得

            \[
                u_L‘ \oplus v_L = u_L’‘ \oplus v_L’‘.
            \]

        对于情况 1，当 $v = v'$ 时方程便会规约为 $u_L' = u_L$，此时与 $A$ 允许输入 $u$ 的假设矛盾. 所以 $u'$ 有 $t + 1$ 种选择，$v'$ 有 $t$ 种选择，因此最多有 $t(t + 1)$ 个 $v_L$ 会导致碰撞. 对于情况 2，同样是 $t(t + 1)$ 个 $v_L$ 会导致碰撞. 因此最多有 $2t(t + 1)$ 个 $v_L$ 会导致碰撞，因此至少有 $2^n - 2t(t + 1) = 2^n - 2t^2 - 2t$ 个 $v_L$ 不会导致碰撞. 

!!! info "Definition"
    (1) 称元组 $D$ 是一个一阶扩展，如果存在：

    1. 某个典则数据库 $D' = (D_h', D_k', D_f')$，

    2. 某个 $l \in \{0, 1\}^n$ 使得对于某个 $r$，$D'$ 允许输入 $l \Vert r$，且对于任意 $r$ 都有 $l \Vert r \not \in \mathsf{Dom}(D')$，

    3. 某个 $z \in \{0, 1\}^n$，

    使得 $D = (D_h'[l \mapsto z], D_k', D_f')$.

    称 $D$ 是 $D'$ 带有 $(l, z)$ 的一阶扩展. 记 $\mathbf{E}(\mathbf{C}_t)$ 为大小为 $t$ 的典则数据库的所有一阶扩展的集合，$\mathbf{E}(D)$ 为 $D$ 的所有一阶扩展的集合.

    (2) 称元组 $D$ 是一个二阶扩展，如果存在：

    1. 某个典则数据库 $D'$ 是 $D''$ 带有 $(l, z)$ 的一阶扩展，

    2. 某个 $m \in \{0, 1\}^n$ 使得 $m \not \in \mathsf{Dom}(D'_k)$，

    3. 某个 $w \in \{0, 1\}^n$，使得 $l \oplus w \in \mathbf{L}_{l, \mathsf{supp}(D'')}$，

    使得 $D = (D_h', D_k'[m \mapsto w], D_f')$.

    称 $D$ 是 $D''$ 带有 $(l, z), (m, w)$ 的二阶扩展，$D'$ 带有 $(m, w)$ 的一阶扩展. 记 $\mathbf{E}^2(\mathbf{C}_t)$ 为大小为 $t$ 的典则数据库的所有二阶扩展的集合，$\mathbf{E}^2(D)$ 为 $D$ 的所有二阶扩展的集合.

    (3) 称元组 $D$ 是一个三阶扩展，如果存在：

    1. 某个典则数据库 $D'$ 是 $D''$ 带有 $(l, z), (m, w)$ 的二阶扩展，
    
    2. 某个 $z' \in \{0, 1\}^n$，

    使得 $D = (D_h', D_k', D_f'[l \oplus m \mapsto z'])$.

    记 $\mathbf{E}^3(\mathbf{C}_t)$ 为大小为 $t$ 的典则数据库的所有三阶扩展的集合，$\mathbf{E}^3(D)$ 为 $D$ 的所有三阶扩展的集合.

!!! success "Lemma"
    固定 $u \in [N]$，对任意 $t \geq 0$，典则数据库 $D \in \mathbf{C}_{t + 1}$ 满足 $u \in \mathsf{Dom}(D)$，存在唯一的 $D' \in \mathbf{C}_t$，使得 $u \not \in \mathsf{Dom}(D')$，且 $D = \mathbf{E}^3(D')$. 此外，所有典则数据库的三阶扩展也都是典则的.

接下来的定义将用到 $\uparrow$ 和 $\downarrow$ 符号，前者表示正向计算路径，后者表示反向计算路径. 

!!! info "Definition"
    固定 $D \in \mathbf{C}_t$，以及 $u \in [N] \setminus \mathsf{Dom}(D)$，并且 $D$ 允许输入 $u$，定义 

    \[
        D \uparrow^u_h := \{D\} \cup \{(D_h[u_L \mapsto z], D_k, D_f) \mid z \in \{0, 1\}^n \setminus \{u_R \oplus \op{Dom}(D_k)\}\}.
    \]

    对于带有扩展 $(u_L, z)$ 的一阶扩展 $D' \in D \uparrow^u_h \subset \mathbf{E}(D)$，以及 $z \in \{0, 1\}^n \setminus \{u_R \oplus \op{Dom}(D_k)\}$，定义

    \[
        D' \uparrow^u_k := \{D'\} \cup \{(D'_h, D_k[u_R \oplus z \mapsto w], D_f) \mid w \in \{u_L \oplus \mathbf{L}_{u_L, \mathsf{supp}(D)}\}\}.
    \]

    对于带有扩展 $(u_L, z), (u_R \oplus z, w)$ 的二阶扩展 $D'' \in D' \uparrow^u_k \subset \mathbf{E}^2(D)$，定义

    \[
        D'' \uparrow^u_f := \{D''\} \cup \{(D''_h, D''_k, D_f[u_L \oplus w \mapsto z']) \mid z' \in \{0, 1\}^n\}
    \]

对数据库集合应用以上记号时，指的是对集合中每个数据库应用该记号，并简记 $(D \uparrow^u_h) \uparrow^u_k := D \uparrow^u_{h, k}$，$((D \uparrow^u_h) \uparrow^u_k ) \uparrow^u_f := D \uparrow^u_{h, k, f}$. 

!!! success "Lemma"
    对于任意 $D \neq D' \in \mathbf{C}$，以及 $u \in [N]$，其被 $D$ 和 $D'$ 允许输入，但不被二者支撑，即 $u \not \in \mathsf{Dom}(D) \cup \mathsf{Dom}(D')$，则有

    \[
        D \uparrow^u_h \cap D' \uparrow^u_h = \varnothing, \quad
        D \uparrow^u_{h, k} \cap D' \uparrow^u_{h, k} = \varnothing, \quad
        D \uparrow^u_{h, k, f} \cap D' \uparrow^u_{h, k, f} = \varnothing.
    \]

!!! info "Definition"
    设 $D \in \mathbf{C}$，以及 $u \in \op{Dom}(D)$，定义

    \begin{align*}
        D \downarrow^u_h &:= \{(D_h[u_L \mapsto z], D_k, D_f) \mid z \in \{0, 1\}^n \cup \{\perp\} \setminus \{u_R \oplus \op{Dom}(D_k)\}\}, \\
        D \downarrow^u_k &:= \{(D_h, D_k[u_R \oplus D_h(u_L) \mapsto w], D_f) \mid w \in \{u_L \oplus \mathbf{L}_{u_L, D[u \mapsto \perp]}\} \cup \{\perp\}\}, \\
        D \downarrow^u_f &:= \{(D_h, D_k, D_f[D(u)_L \mapsto z']) \mid z' \in \{0, 1\}^n \cup \{\perp\}\}.
    \end{align*}

!!! success "Lemma"
    对于任意 $D \neq D' \in \mathbf{C}$，以及 $u \in \op{Dom}(D) \cap \op{Dom}(D')$，有

    \[
        D \downarrow^u_h \cap D' \downarrow^u_h = \varnothing, \quad
        D \downarrow^u_k \cap D' \downarrow^u_k = \varnothing,
    \]

    当 $D[u \mapsto \perp] \neq D'[u \mapsto \perp]$ 时，有

    \[
        D \downarrow^u_f \cap D' \downarrow^u_f = \varnothing. 
    \]
    