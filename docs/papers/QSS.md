# Quantum Secret Sharing and Error Correction vs No-Cloning

## Preliminaries

### Quantum Secret Sharing

量子秘密分享（Quantum Secret Sharing, QSS）方案包含有 $n$ 个参与者和一个访问结构 $\Gamma \subseteq 2^{[n]}$. $\Gamma$ 是单调的，对于任意 $S \in \Gamma$，如果 $S \subseteq T$，则 $T \in \Gamma$. 本文中考虑多拷贝变体，即方案同时包含 $k$ 个秘密的复制. 一个 $(n, \Gamma, k)$-QSS 方案由以下算法组成：

- $\mathsf{Deal}(\ket{\psi}^{\otimes k})$: 该算法接收 $\ket{\psi}$ 的 $k$ 个副本，输出 $n$ 个系统 $R_1, \ldots, R_n$ 上的联合量子态 $\rho_{R_1, \ldots, R_n}$，$R_i$ 与 Hilbert 空间 $\mathcal{H}_i$ 相关联.

- $\mathsf{Recon}(S, \rho'_{\{R_i\}_{i \in S}})$: 该算法接收一个集合 $S \subseteq [n]$ 和 $\{R_i\}_{i \in S}$ 上的量子态 $\rho'_{\{R_i\}_{i \in S}}$，输出一个量子态 $\ket{\psi'}$.

如果 $S \in \Gamma$，则称 $S$ 是一个授权集合，否则称为未授权集合. 

!!!+ definition "QSS Correctness and Security"
    1. (QSS Correctness) 对于任意授权集合 $S \in \Gamma$，以及任意纯态 $\ket{\psi}$，如果执行 $\rho_{R_1, \ldots, R_n} \gets \mathsf{Deal}(\ket{\psi}^{\otimes k})$，$\ket{\psi'} \gets \mathsf{Recon}(S, \rho_{\{R_i\}_{i \in S}})$，有 $\ket{\psi'} = \ket{\psi}$，那么称该 QSS 方案是正确的.

    2. (QSS Security) 对于任意未授权集合 $S \notin \Gamma$，以及任意一对纯态 $\ket{\psi^0}$ 和 $\ket{\psi^1}$，如果执行 $\rho^b_{R_1, \ldots, R_n} \gets \mathsf{Deal}((\ket{\psi^b})^{\otimes k})$，则有 $\rho^0_{\{R_i\}_{i \in S}} = \rho^1_{\{R_i\}_{i \in S}}$，那么称该 QSS 方案是安全的.

    3. $(n, \Gamma, k)$-QSS 方案是一个以 $n$ 个参与者、访问结构 $\Gamma$ 和秘密副本数 $k$ 为输入的，满足正确性和安全性的 QSS 方案.

接下来考虑阈限量子秘密分享方案，其带有阈限访问结构 $\Gamma_{t, n}$，定义为 $\Gamma_{t, n} = \{S \subseteq [n] : \lvert S \rvert \geq t\}$. 

!!!+ definition "Quantum Threshold Secret Sharing"
    $(n, t, k)$-QTSS 方案是一个以 $n$ 个参与者、阈限访问结构 $\Gamma_{t, n}$ 和秘密副本数 $k$ 为输入的，满足正确性和安全性的 QSS 方案.

**$k = 1$ 时的量子秘密分享的完整刻画**

!!!+ theorem
    $(n, \Gamma, 1)$-QSS 方案存在当且仅当 $\Gamma$ 中不存在两个不相交的集合.

    !!!+ corollary
        $(n, t, 1)$-QTSS 方案存在当且仅当 $n < 2t$.

**不可克隆定理的多副本推广**

!!!+ corollary
    若 $\Gamma$ 中存在 $k+1$ 个两两不相交的集合，则不存在 $(n, \Gamma, k)$-QSS 方案. 对于阈限情形，若 $n \geq (k+1)t$，则不存在 $(n, t, k)$-QTSS 方案.

### Graph Theory

!!!+ definition
    1. (Vertex Coloring) 给定一个图 $G = (V, E)$，一个顶点着色是一个函数 $c: V \to [k]$，使得对于任意边 $(u, v) \in E$，有 $c(u) \neq c(v)$.

    2. (Chromatic Number) 图 $G$ 的色数 $\chi(G)$ 是使得 $G$ 可着色的最小整数 $k$.

$\chi(G) \leq 2$ 的图称为二分图. 

!!!+ theorem
    图 $G$ 是二分图当且仅当 $G$ 中不存在奇数长度的环.

!!!+ definition
    1. (Access Structure Graph) 给定一个访问结构 $\Gamma \subseteq 2^{[n]}$，其访问结构图 $G_\Gamma$ 的每个顶点对应 $\Gamma$ 中的一个极小授权集合，两个顶点之间有一条边当且仅当它们对应的极小授权集合不相交.

    2. (Kneser Graph) Kneser 图 $K(m, l)$ 的每个顶点对应于一个 $m$ 元集合的 $l$ 元子集，两个顶点之间有一条边当且仅当它们对应的子集不相交.

对于阈限访问结构 $\Gamma_{t, n}$，其访问结构图 $G_{\Gamma_{t, n}}$ 是 Kneser 图 $K(n, t)$.

!!!+ theorem "Lovász's Theorem"
    对于任意整数 $m \geq 2l$，有 $\chi(K(m, l)) = m - 2l + 2$.

## Positive Results

### The Dual-Copy Case（$k = 2$）

!!!+ theorem
    $(n, \Gamma, 2)$-QSS 方案可以通过访问结构并集(union of 
    access structures)方式实现当且仅当访问结构图 $G_\Gamma$ 是二分图. 

### Generalizing to Arbitrary $k$

!!!+ theorem
    $(n, \Gamma, k)$-QSS 方案可以通过访问结构并集方式实现当且仅当访问结构图 $G_\Gamma$ 是 $k$-可着色的.

!!!+ theorem
    $(n, t, k)$-QTSS 方案可以通过访问结构并集方式实现当且仅当 $n \leq 2t - 2 + k$.

## Negative Results

### Canonical Form

!!!+ lemma "Purified dealer"
    任意 $(n, \Gamma, k)$-QSS 方案都可以假设其 $\mathsf{Deal}$ 由如下等距映射给出：

    \[
        \hat{U}_D: \mathcal{H}^{\otimes k} \to \mathcal{H}_1 \otimes \cdots \otimes \mathcal{H}_n \otimes \mathcal{H}_E,
    \]

    其中 $\mathcal{H} \cong \mathbb{C}^d$ 是秘密空间，$\mathcal{H}_E$ 是环境空间. 定义全局纯态 $\ket{\Psi_\psi} = \hat{U}_D \ket{\psi}^{\otimes k}$，因而 $\op{Tr}_E(\ket{\Psi_\psi}\bra{\Psi_\psi}) = \rho_{R_1, \ldots, R_n}$.

!!!+ lemma "Unitary reconstruction"
    设 $S \in \Gamma$ 是一个授权集合，$\mathcal{H}_S = \bigotimes_{i \in S} \mathcal{H}_i$，那么存在一个 $\mathcal{H}_S$ 上的酉算子 $\hat{U}_S$，以及一个分解 $\mathcal{H}_S \cong \mathcal{K}_S \otimes \mathcal{R}_S$，其中 $\dim(\mathcal{K}_S) = d$，使得对于任意纯态 $\ket{\psi}$，有

    \[
        (\hat{U}_S \otimes I) \ket{\Psi_\psi} = \ket{\psi}_{\mathcal{K}_S} \otimes \ket{\Theta_\psi^S},
    \]

    其中 $\ket{\Theta_\psi^S}$ 是一个定义在 $\mathcal{R}_S \otimes \mathcal{H}_{\bar{S}} \otimes \mathcal{H}_E$ 上的纯态.

### Labeled Cliques and the Residual State

!!!+ definition "Labeled Clique"
    带有标签的 $k$-团是一个有序元组 $\vec{A} = (A_1, \ldots, A_k)$，其中 $A_i \in \Gamma$，并且 $A_i \cap A_j = \varnothing, \forall i \neq j$. 称 $i$ 是 $A_i$ 在 $\vec{A}$ 中的索引，其可以被理解为颜色，即 $c(A_i) = i$. 

    
只有当 $G_\Gamma$ 中包含一个 $k$-团时，才存在带有标签的 $k$-团. 因为 $A_i$ 都是两两不相交的授权集合，所以可以同时施加重建酉算子.

!!!+ lemma "Constant residue"
    设 $\vec{A} = (A_1, \ldots, A_k)$ 是一个带有标签的 $k$-团，令 $\hat{U}_{\vec{A}} = \hat{U}_{A_1} \hat{U}_{A_2} \cdots \hat{U}_{A_k}$，那么存在一个与秘密态无关的固定单位向量 $\ket{\mathrm{Rem}}$，使得对于任意纯态 $\ket{\psi}$，有

    \[
        \hat{U}_{\vec{A}} \ket{\Psi_\psi} = \ket{\psi}_{\mathcal{K}_{A_1}} \otimes \cdots \otimes \ket{\psi}_{\mathcal{K}_{A_k}} \otimes \ket{\mathrm{Rem}}.
    \]

    $\ket{\mathrm{Rem}}$ 称为残余态(residual state)，它定义在 $\mathcal{R}_{A_1} \otimes \cdots \otimes \mathcal{R}_{A_k} \otimes \mathcal{H}_{\overline{A_1 \cup \cdots \cup A_k}} \otimes \mathcal{H}_E$ 上.

    ???+ success "Proof"
        因为 $V := \hat{U}_{\vec{A}} \hat{U}_D$ 是一个等距映射，所以其保持内积. 考虑两个不正交的输入 $\ket{\psi^0}$ 和 $\ket{\psi^1}$，输入前与输入后的状态的内积满足

        \[
            \innerproduct{\psi^0}{\psi^1}^k = \innerproduct{\psi^0}{\psi^1}^k \innerproduct{\mathrm{Rem}^0}{\mathrm{Rem}^1},
        \]

        而 $\innerproduct{\psi^0}{\psi^1} \neq 0$，所以 $\innerproduct{\mathrm{Rem}^0}{\mathrm{Rem}^1} = 1$，两个单位向量的内积为 1 当且仅当它们相等，所以 $\ket{\mathrm{Rem}^0} = \ket{\mathrm{Rem}^1}$，即残余态与秘密态无关.

!!!+ definition "Alternate dealer"
    设 $\vec{A} = (A_1, \ldots, A_k)$ 是一个带有标签的 $k$-团，定义替代处理者 $\mathcal{D}'_{\vec{A}}$ 为如下的线性映射：

    \[
        \mathcal{D}'_{\vec{A}}: \mathcal{H}^{\otimes k} \to \mathcal{H}_1 \otimes \cdots \otimes \mathcal{H}_n \otimes \mathcal{H}_E, \quad \mathcal{D}'_{\vec{A}}(\ket{\phi_1} \otimes \cdots \otimes \ket{\phi_k}) = \hat{U}_{\vec{A}}^\dagger (\ket{\phi_1} \otimes \cdots \otimes \ket{\phi_k} \otimes \ket{\mathrm{Rem}}), 
    \]

    其中 $\ket{\phi_i}$ 位于输出寄存器 $\mathcal{K}_{A_i}$ 上.

!!!+ lemma "Properties of the alternate dealer" {#lem:alternate-dealer-properties}
    对于每个带有标签的 $k$-团 $\vec{A}$：

    1. (Agreement on the diagonal) $\mathcal{D}'_{\vec{A}}(\ket{\psi}^{\otimes k}) = \ket{\Psi_\psi}, \forall \ket{\psi}$，即所有 $\mathcal{D}'_{\vec{A}}$ 在对角线输入上都与原始处理者 $\mathcal{D}$ 一致.

    2. (Index extraction) 对于任意 $i$ 以及输入 $\ket{\phi_1}, \ldots, \ket{\phi_k}$，有

        \[
            \hat{U}_{A_i} \mathcal{D}'_{\vec{A}}(\ket{\phi_1} \otimes \cdots \otimes \ket{\phi_k}) = \ket{\phi_i}_ \otimes (\cdots),
        \]

        省略的部分位于 $\mathcal{R}_{A_i} \otimes \mathcal{H}_{\bar{A_i}} \otimes \mathcal{H}_E$ 上. 换言之，索引 $i$ 与 $A_i$ 绑定，$A_i$ 会恢复输入中的第 $i$ 个副本，这个性质即使在输入态不相同的时候也成立.

### The Substitution Lemma

!!!+ definition
    设 $\vec{A} = (A_1, \ldots, A_k)$ 是一个带有标签的 $k$-团，$i_0 \in [k]$，$A'$ 是一个与任意 $A_j, j \neq i_0$ 不相交的授权集合. 带有标签的 $k$-团 $\vec{B}$ 是通过将 $\vec{A}$ 中的 $A_{i_0}$ 替换为 $A'$ 得到的，即 $\vec{B} = (A_1, \ldots, A_{i_0 - 1}, A', A_{i_0 + 1}, \ldots, A_k)$，称 $\vec{B}$ 是在 $i_0$ 处替换 $\vec{A}$ 的结果.

!!!+ lemma "Substitution"
    如果 $\vec{B}$ 是 $\vec{A}$ 的一个替换，那么 $\mathcal{D}'_{\vec{A}} = \mathcal{D}'_{\vec{B}}$.

    ???+ success "Proof"
        考虑 $\Delta := \mathcal{D}'_{\vec{A}} - \mathcal{D}'_{\vec{B}}$，我们需要证明 $\Delta = 0$. 设 $i_0$ 是被替换的索引. 依据\adref{lem:alternate-dealer-properties}，对于任意单位态 $\ket{\phi}$，有 $\Delta(\ket{\phi}^{\otimes k}) = 0$，因而对于任意 $\ket{v} \in \mathcal{H}$，依据齐次性，有 $\Delta(\ket{v}^{\otimes k}) = 0$. 

        固定一组单位正交基 $\{\ket{e_1}, \ldots, \ket{e_d}\}$，并考虑 $\vec{z} \in \mathbb{C}^d$，定义 $\ket{v_\vec{z}} = \sum_{a = 1}^d z_a \ket{e_a}$，依据多重线性性展开 $\Delta(\ket{v_\vec{z}}^{\otimes k}) = 0$，得到以下多项式等式：

        \[
            \sum_{w \in [d]^k} z_{w_1} \cdots z_{w_k} \Delta(\ket{e_{w_1}} \otimes \cdots \otimes \ket{e_{w_k}}) = 0.
        \]

        对字 $w = (w_1, \ldots, w_k)$ 定义其类型 $\mathrm{type}(w) = (m_1, \ldots, m_d) \in \mathbb{N}^d$，$m_a$ 是 $w$ 中等于 $a$ 的元素的数量. 显然具有同样类型的字在多项式展开中对应同一个单项式 $z_1^{m_1} \cdots z_d^{m_d}$，所以比较系数得到

        \[
            \sum_{\mathrm{type}(w) = \vec{m}} \Delta(\ket{e_{w_1}} \otimes \cdots \otimes \ket{e_{w_k}}) = 0, \quad \forall \vec{m} \in \mathbb{N}^d, \sum_{a = 1}^d m_a = k. \label{eq:substitution}
        \]

        定义 $C_j := A_j = B_j, \forall j \neq i_0$ 为两个团共享的 $k - 1$ 个授权集合，并定义 $W:= \bigotimes_{j \neq i_0} \hat{U}_{C_j}$. 而对 $\mathcal{D}'_{\vec{A}}$ 和 $\mathcal{D}'_{\vec{B}}$ 施加 $W$ 后，依据\adref{lem:alternate-dealer-properties}，除了 $i_0$ 处的输入外，其他所有输入都被恢复到输出中. 因此对任意 $w \in [d]^k$，有

        \[
            W \Delta(\ket{e_{w_1}} \otimes \cdots \otimes \ket{e_{w_k}}) = \bigotimes_{j \neq i_0} \ket{e_{w_j}} \otimes \ket{\delta_w},
        \]

        其中 $\ket{\delta_w}$ 是剩余寄存器的残余状态. 对 $\eqref{eq:substitution}$ 施加 $W$，得到

        \[
            \sum_{\mathrm{type}(w) = \vec{m}} \bigotimes_{j \neq i_0} \ket{e_{w_j}} \otimes \ket{\delta_w} = 0.
        \]

        接下来考虑 $w_{-i_0} := (w_1, \ldots, w_{i_0 - 1}, w_{i_0 + 1}, \ldots, w_k)$，在固定 $\vec{m}$ 的情况下，$w_{i_0}$ 的取值是唯一的. 所以在固定类型的情况下，每个字给出的限制字也是唯一的，由此进行索引提取得到的 $\bigotimes_{j \neq i_0} \ket{e_{w_j}}$ 是线性无关的，这可以通过内积得到验证. 因此 $\ket{\delta_w} = 0$，也就有 $\Delta(\ket{e_{w_1}} \otimes \cdots \otimes \ket{e_{w_k}}) = 0, \forall w \in [d]^k$. 而 $\{\ket{e_{w_1}} \otimes \cdots \otimes \ket{e_{w_k}} : w \in [d]^k\}$ 是 $\mathcal{H}^{\otimes k}$ 的一组基，所以 $\Delta = 0$，即 $\mathcal{D}'_{\vec{A}} = \mathcal{D}'_{\vec{B}}$.

### Clique Path obstruction

!!!+ definition "Clique Path"
    团路径指带有标签的 $k$-团序列 $P = (\vec{A}^{(0)}, \ldots, \vec{A}^{(l)})$，其中 $\vec{A}^{(m+1)}$ 是 $\vec{A}^{(m)}$ 的一个替换.

    !!!+ corollary
        一个团路径上的所有带有标签的 $k$-团都有相同的替代处理者 $\mathcal{D}'_{\vec{A}^{(0)}} = \cdots = \mathcal{D}'_{\vec{A}^{(l)}}$.

团路径可以给授权集染色，但这种染色可能不是良定义的.

!!!+ definition "Inconsistent Clique Path"
    称团路径 $P$ 将授权集 $S$ 染色为 $i$，如果存在一个带有标签的 $k$-团 $\vec{A}^{(m)}$，使得 $S = A^{(m)}_i$. 如果 $P$ 将授权集 $S$ 染色为两个不同的索引，即存在 $i \neq i'$，以及 $m, m'$，使得 $A^{(m)}_i = S = A^{(m')}_{i'}$，则称 $P$ 是不一致的.

!!!+ theorem "Clique-Path obstruction"
    令 $\Gamma$ 是一个单调访问结构，$k \geq 2$，如果 $\Gamma$ 中存在一个不一致的团路径，则不存在 $(n, \Gamma, k)$-QSS 方案.

### The Clique Path Obstruction Applied to Threshold Structures

!!!+ lemma 
    设 $n = kt + 1$. $G_{\Gamma_{t, n}}$ 中的任意带标签的 $k$-团都可以通过团路径到达另一个带标签的 $k$-团.

!!!+ theorem
    对于 $n \geq kt + 1$，$k \geq 2$，不存在 $(n, t, k)$-QTSS 方案.