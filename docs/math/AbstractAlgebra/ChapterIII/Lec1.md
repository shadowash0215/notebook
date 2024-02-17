# 模 模同态 正合列

环上的模实际上是阿贝尔群的推广，我们参照阿贝尔群给出如下定义。

!!! info "定义"
    设 $R$ 是环，一个 **（左）$R$-模**(R-module) 是指一个加法阿贝尔群 $A$ 和一个函数 $R \times A \rightarrow A$，$(r, a) \mapsto ra$，使得对于任意的 $r, s \in R, a, b \in A$，有  
    (i) $r(a+b) = ra + rb$;  
    (ii) $(r+s)a = ra + sa$;  
    (iii) $(rs)a = r(sa)$.  
    若 $R$ 含幺，则  
    (iv) $1_Ra = a, \forall a \in A$.  
    $A$ 被称作**幺作用 （左）$R$-模**(unitary R-module). 若 $R$ 是一除环，则 $A$ 被称作 **（左）线性空间**. 

显然，交换环上的模既可被视作左模，也可被视作右模。  

如果 $R$-模 $A$ 的零元为 $0_A$，$R$ 的零元为 $0_R$，则 $\forall r \in R, a \in A$，有

\[
    r0_A = 0_A, 0_Ra = 0_A.
\]

今后我们将 $0_A, 0_R, 0 \in \mathbf{Z}$ 以及平凡模 $\{0\}$ 均表示成 $0$。

以下是一些模的例子。

!!! example "示例"
    (i) 设 $R$ 和 $S$ 为环，$\varphi: R \mapsto S$ 为环同态，则每个 $S$-模 $A$ 可以形成一个 $R$-模，只要将 $rx$ 定义为 $\varphi(r)x$，$r \in R, x \in A$. 我们称这样的 $R$-模结构是通过 $\varphi$ 的**拉回**(pullback) 实现的.  
    (ii) 设 $A$ 是阿贝尔群，$\mathrm{End} A$ 是 $A$ 的自同态环，则 $A$ 是幺作用 $\mathrm{End} A$-模，其中 $fa := f(a), a \in A, f \in \mathrm{End} A.$

接下去是模同态的定义。

!!! info "定义"
    设 $A$ 和 $B$ 是环 $R$ 上的模，映射 $f: A \rightarrow B$ 被称作 **$R$-模同态**，若对于 $\forall a, c \in A, r \in R$，有

    $$
        f(a + c) = f(a) + f(c), f(ra) = rf(a)
    $$

    若 $R$ 是一除环，则 $f$ 被称为**线性变换**(linear transformation)

注意到 $R$-模同态 $f: A \rightarrow B$ 一定是加法阿贝尔群的同态，所以有类似的描述：若 $f$ 作为集合映射是单射、满射或双射，则分别称 $f$ 为 **$R$-模单态**，**$R$-模满态**或 **$R$-模同构**。$f$ 的核是指作为阿贝尔群同态的核。所以我们可以推出：  
(i) $f$ 是 $R$-模单态 $\Leftrightarrow$ $\operatorname{\mathrm{Ker}} f = 0$.  
(ii) $f: A \rightarrow B$ 是 $R$-模同构 $\Leftrightarrow$ 存在着 $R$-模同态 $g: B \rightarrow A$，使得 $gf = 1_A, fg = 1_B$.

然后是子结构。

!!! info "定义"
    设 $R$ 是环，$A$ 是 $R$-模，而 $B$ 是 $A$ 的非空子集合。若 $B$ 满足是 $A$ 的加法子群，且 $\forall r \in R, b \in B$，有 $rb \in B$，则称 $B$ 为 $A$ 的**子模**(submodule). 除环上的线性空间上的子模称作**子空间**(subspace).

!!! note "定理"
    若 $X$ 是环 $R$ 上的模 $A$ 的子集，则 $A$ 的所有包含 $X$ 的子模的交被称为 $X$ **生成**(generated)（或**张成**(spanned)）的子模.

如果 $X$ 是有限的，且生成了模 $B$，则称 $B$ 是**有限生成的**(finitely generated)。若 $X = \varnothing$, 则 $X$ 生成了零模。若 $X = \{a\}$，即 $X$ 只包含一个元素，那么由 $X$ 生成的(子)模称为由 $a$ 生成的**循环(子)模**(cyclic (sub)module)。设 $\{B_i \mid i \in I\}$ 是一族 $A$ 的子模，则由 $X = \cup_{i \in I} B_i$ 生成的子模称为子模 $B_i$ 的**和**(sum)。

让我们进一步了解生成子模的结构。

!!! note "定理"
    设 $R$ 是环，$A$ 是一 $R$-模，$X$ 是 $A$ 的一个子集，$\{B_i \mid i \in I\}$ 是 $A$ 的一族子模，$a \in A$. 定义 $Ra = \{ra \mid r \in R\}$，则  
    (i) $Ra$ 是 $A$ 的一个子模，映射 $R \rightarrow Ra$，$r \mapsto ra$ 是一$R$-模满态.  
    (ii) 由 $a$ 生成的循环子模 $C$ 是 $\{ra+na \mid r \in R, n \in \mathrm{Z}\}$. 若 $R$ 是含幺环，$A$ 是幺作用模，则 $C = Ra$.  
    (iii) 由 $X$ 生成的子模 $D$ 是

    $$
        \left\{\sum_{i = 1}^s r_ia_i + \sum_{j = 1}^t n_jb_j \mid s, t \in N^*, a_i, b_j \in X, r_i \in R, n_j \in \mathrm{Z}\right\}.
    $$

    若 $R$ 是含幺环，$A$ 是幺作用模，则 

    $$
        D = RX = \left\{\sum_{i = 1}^s r_ia_i \mid s\in N^*, a_i \in X, r_i \in R\right\}.
    $$

    (v) 子模族 $\{B_i \mid i \in I\}$ 的和是 $\{b_{i_1}+ \cdots + b_{i_n} \mid b_{i_k} \in B_{i_k}\}$.

然后是商结构的一些性质。

!!! note "定理"
    设 $B$ 是环 $R$ 上模 $A$ 的子模，则商群 $A/B$ 是$R$-模，其中 $R$ 在 $A/B$ 上的作用定义为 $r(a+B) = ra + B, \forall r \in R, a \in A$. 进而映射 $\pi: A \rightarrow A/B$, $a \mapsto a + B$ 是一$R$-模满态，核为 $B$. 这是模结构中的典范满射.

由此，我们可以从群的同构定理推理到模的同构定理. 

!!! note "$\star$定理"
    (i) $R$ 是一环，$f: A \rightarrow B$ 是 $R$-模同态，$C$ 是 $\operatorname{\mathrm{Ker}} f$ 的子模，则存在唯一的 $R$-模同态 $\bar{f}: A/C \rightarrow B$，使得对于每个 $a \in A$，$\bar{f}(a+C) = f(a)$. 其次，$\operatorname{Im} \bar{f} = \operatorname{Im} f$, $\operatorname{\mathrm{Ker}} \bar{f} = \operatorname{\mathrm{Ker}} f/C$. 最后，$\bar{f}$ 是 $R$-模同构 $\Leftrightarrow$ $f$ 是 $R$-模满同态且 $\operatorname{\mathrm{Ker}} f = C$. 特别地，$A/\operatorname{\mathrm{Ker}} f \cong \operatorname{Im} f$.  
    (ii) 如果 $R$ 是环，$A'$ 和 $B'$ 分别是 $R$-模 $A$ 和 $B$ 的子模，$f: A \rightarrow B$ 是 $R$-模同态，且 $f(A') \subset B'$，则存在唯一的 $R$-模同态 $\bar{f}: A/A' \rightarrow B/B'$，使得对于每个 $a \in A$，$\bar{f}(a+A') = f(a) + B'$. 进而，$\bar{f}$ 是 $R$-模同构 $\Leftrightarrow$ $\operatorname{\mathrm{Im}} f + B' = B$ 且 $f^{-1}(B') \subset A'$. 特别地，如果 $f$ 是 $R$-模满同态，且 $f(A') = B'$，$\operatorname{\mathrm{Ker}} f \subset A'$，则 $\bar{f}$ 是 $R$-模同构.   
    (iii) 设 $B$ 和 $C$ 是环 $R$ 上模 $A$ 的子模，则  
    (a) 存在 $R$-模同构 $B/(B \cap C) \cong (B+C)/C$.  
    (b) 如果 $C \subset B$，则 $B/C$ 是 $A/C$ 的子模，且存在 $R$-模同构 $(A/C)/(B/C) \cong A/B$.  
    (iv) 如果 $R$ 是环，$B$ 是 $R$-模 $A$ 的子模，则在集合 $\{C \mid C \subset A, C \supset B\}$ 和集合 $\{D \mid D \subset A/B\}$ 之间存在一一对应，$C \mapsto C/B$. 也就是说 $A/B$ 的子模都有形式 $C/B$，其中 $C$ 是 $A$ 包含 $B$ 的子模.

!!! note "定理"
    设 $R$ 是环，$\{A_i \mid i \in I\}$ 是一族非空 $R$-模，$\prod_{i \in I} A_i$ 是阿贝尔群 $A_i$ 的直积，$\sum_{i \in I} A_i$ 是 $A_i$ 的直和。则  
    (i) $\prod_{i \in I} A_i$ 是 $R$-模，其中 $R$ 在 $\prod_{i \in I} A_i$ 上的作用定义为 $r\{a_i\}_{i \in I} = \{ra_i\}_{i \in I}, \forall r \in R, \{a_i\}_{i \in I} \in \prod_{i \in I} A_i$.  
    (ii) $\sum_{i \in I} A_i$ 是 $\prod_{i \in I} A_i$ 的子模.  
    (iii) 对于每个 $k \in I$，典范投影 $\pi_k: \prod_{i \in I} A_i \rightarrow A_k$，$\{a_i\}_{i \in I} \mapsto a_k$ 是 $R$-模满同态.  
    (iv) 对于每个 $k \in I$，典范嵌入 $\iota_k: A_k \rightarrow \sum_{i \in I} A_i$，$a_k \mapsto \{a_i\}_{i \in I}$ 是 $R$-模单同态.

$\prod_{i \in I} A_i$ 被称为 $A_i$ 的(外)**直积**(direct product)，$\sum_{i \in I} A_i$ 被称为 $A_i$ 的(外)**直和**(direct sum). 如果下标集合是有限的，则直积和直和是相同的，并且记作 $A_1 \oplus A_2 \oplus \cdots \oplus A_n$.

下面讨论**正合列**(exact sequence)的概念。

!!! info "定义"
    一对模同态 $A \xrightarrow{f} B \xrightarrow{g} C$ 被称为在 $B$ 处 **正合**(exact)，是指 $\operatorname{\mathrm{Ker}} g = \operatorname{\mathrm{Im}} f$. 模同态有限序列 $A_0 \xrightarrow{f_1} A_1 \xrightarrow{f_2} \cdots \xrightarrow{f_n} A_n$ 被称为 **正合的**，是指 $\forall i \in \{1, 2, \cdots, n-1\}$，$\operatorname{\mathrm{Ker}} f_{i+1} = \operatorname{\mathrm{Im}} f_i$. 模同态无限序列 $\cdots \xrightarrow{f_{i-1}} A_{i-1} \xrightarrow{f_i} A_i \xrightarrow{f_{i+1}} A_{i+1} \xrightarrow{f_{i+2}}\cdots$ 被称为 **正合的**，是指 $\forall i \in \mathrm{N}^*$，$\operatorname{\mathrm{Ker}} f_{i+1} = \operatorname{\mathrm{Im}} f_i$.

!!! tip "提示"
    $0 \rightarrow A \xrightarrow{f} B$ 是正合的 $\Leftrightarrow$ $f$ 是模的单同态. $B \xrightarrow{g} C \rightarrow 0$ 是正合的 $\Leftrightarrow$ $g$ 是模的满同态. 如果 $A \xrightarrow{f} B \xrightarrow{g} C$ 是正合的，则 $g \circ f = 0$. 形如 $0 \rightarrow A \xrightarrow{f} B \xrightarrow{g} C \rightarrow 0$ 的正合列被称为 **短正合列**(short exact sequence).

!!! success "引理"
    设 $R$ 是环，且 

    \tikzcd
        0 \arrow[r] & A \arrow[r, "f"] \arrow[d, "\alpha"] & B \arrow[r, "g"] \arrow[d, "\beta"] & C \arrow[r] \arrow[d, "\gamma"] & 0 \\  
        0 \arrow[r] & A' \arrow[r, "f'"] & B' \arrow[r, "g'"] & C' \arrow[r] & 0

    是 $R$-模和 $R$-模同态组成的交换图表，且两行都是正合的，则  
    (i) $\alpha$ 和 $\gamma$ 是单同态 $\Leftrightarrow$ $\beta$ 是单同态.  
    (ii) $\alpha$ 和 $\gamma$ 是满同态 $\Leftrightarrow$ $\beta$ 是满同态.  
    (iii) $\alpha$ 和 $\gamma$ 是同构 $\Leftrightarrow$ $\beta$ 是同构.

两个短正合序列被称作**同构的**，是指存在下面形式的模交换图表

\tikzcd
    0 \arrow[r] & A \arrow[r] \arrow[d, "f"] & B \arrow[r] \arrow[d, "g"] & C \arrow[r] \arrow[d, "h"] & 0 \\  
    0 \arrow[r] & A' \arrow[r] & B' \arrow[r] & C' \arrow[r] & 0

并且 $f, g, h$ 都是同构. 同时不难证明图表

\tikzcd
    0 \arrow[r] & A \arrow[r] & B \arrow[r] & C \arrow[r] & 0 \\
    0 \arrow[r] & A \arrow[r] \arrow[u, "f^{-1}"] & B \arrow[r] \arrow[u, "g^{-1}"] & C \arrow[r] \arrow[u, "h^{-1}"] & 0 

也是交换的。事实上，短正合序列的同构关系是等价关系。

!!! note "定理"
    设 $R$ 是环，$0 \rightarrow A_1 \xrightarrow{f} B \xrightarrow{g} A_2 \rightarrow 0$ 是 $R$-模同态组成的短正合列，则下列三个条件彼此等价：  
    (i) 存在 $R$-模同态 $h: A_2 \rightarrow B$，使得 $g \circ h = 1_{A_2}$.  
    (ii) 存在 $R$-模同态 $k: B \rightarrow A_1$，使得 $k \circ f = 1_{A_1}$.  
    (iii) 所给的序列同构于短正合序列 $0 \rightarrow A_1 \xrightarrow{\iota_1} A_1 \oplus A_2 \xrightarrow{\pi_2} A_2 \rightarrow 0$，并且从 $A_1$ 到 $A_1$ 和从 $A_2$ 到 $A_2$ 的垂直同构均是恒等映射. 特别地，$A_1 \oplus A_2 \cong B$.

满足上述条件的短正合序列被称为**分裂的**(split)。