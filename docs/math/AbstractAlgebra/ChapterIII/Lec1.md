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
(i) $f$ 是 $R$-模单态 $\Leftrightarrow$ $\ker f = 0$.  
(ii) $f: A \rightarrow B$ 是 $R$-模同构 $\Leftrightarrow$ 存在着 $R$-模同态 $g: B \rightarrow A$，使得 $gf = 1_A, fg = 1_B$.

然后是子结构。

!!! info "定义"
    设 $R$ 是环，$A$ 是 $R$-模，而 $B$ 是 $A$ 的非空子集合。若 $B$ 满足是 $A$ 的加法子群，且 $\forall r \in R, b \in B$，有 $rb \in B$，则称 $B$ 为 $A$ 的**子模**(submodule). 除环上的线性空间上的子模称作**子空间**(subspace).

!!! note "定理"
    若 $X$ 是环 $R$ 上的模 $A$ 的子集，则 $A$ 的所有包含 $X$ 的子模的交被称为 $X$ **生成**(generated)（或**张成**(spanned)）的子模.

如果 $X$ 是有限的，且生成了摸 $B$，则称 $B$ 是**有限生成的**(finitely generated)。若 $X = \varnothing$, 则 $X$ 生成了零模。若 $X = \{a\}$，即 $X$ 只包含一个元素，那么由 $X$ 生成的(子)模称为由 $a$ 生成的**循环(子)模**(cyclic (sub)module)。设 $\{B_i \mid i \in I\}$ 是一族 $A$ 的子模，则由 $X = \cup_{i \in I} B_i$ 生成的子模称为子模 $B_i$ 的**和**(sum)。

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

!!! note "定理"
    $R$ 是一环，$f: A \rightarrow B$ 是 $R$-模同态，$C$ 是 $\ker f$ 的子模，则存在唯一的 $R$-模同态 $\overline{f}: A/C \rightarrow B$，使得对于每个 $a \in A$，$\overline{f}(a+C) = f(a)$