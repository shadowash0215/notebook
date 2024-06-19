# 投射摸和内射模

这两个名字其实挺形象的，先看定义。

!!! info "定义"
    环 $R$ 上的模 $P$ 被称为**投射模**(projective module)，是指任意给下面一个 $R$-模同态图表  
    \tikzcd
        & P \arrow[d, "f"] & \\
        A \arrow[r, "g"] & B \arrow[r] & 0
    并且底行都是正合的，也就是说 $g$ 是满射，都存在 $R$-模同态 $h: P \rightarrow A$ 使得 $g \circ h = f$.  

    这个定义就是在说存在 $h$ 使得下面的图表交换。
    \tikzcd
        & P \arrow[ld, swap, "h"] \arrow[d, "f"] & \\
        A \arrow[r, "g"] & B \arrow[r] & 0

这图看着就像投射下了两个映射，$P$ 叫投射摸也 ~~显而易见了~~。

!!! question "问题"
    证明如下命题： 
    (a) 如果 $R$ 是含幺模而 $A$ 是 $R$-模，则 $A$ 有子模 $B$ 和 $C$ 使得 $B$ 是幺作用模，$RC = 0$ 并且 $A = B \oplus C$. (提示：令 $B = \langle 1_Ra \mid a \in A \rangle$，$C = \langle a \in A \mid 1_Ra = 0 \rangle$. 并且注意对于**每个**$a \in A$，$a - 1_Ra \in C$.)  
    (b) 设 $A_1$ 为另一个 $R$-模，且 $A_1 = B_1 \oplus C_1$，其中 $B_1$ 是幺作用模，$RC_1 = 0$. 如果 $f: A \rightarrow A_1$ 是 $R$-模同态，则 $f(B) \subset B_1$，$f(C) \subset C_1$.  
    (c) 如果 (b) 中的映射 $f$ 是满同态或同构，则 $f \mid B: B \rightarrow B_1$ 和 $f \mid C: C \rightarrow C_1$ 也是满同态或同构.

首先，如果 $R$ 是含幺环，$P$ 是幺作用模，则 $P$ 是投射模等价于对于每一对**幺作用**模 $A, B$ 和 $R$-模同态的图表 

\tikzcd
    & P \arrow[d, "f"] & \\
    A \arrow[r, "g"] & B \arrow[r] & 0

其中 $g$ 是满射，都存在 $R$-模同态 $h: P \rightarrow A$ 使得 $g \circ h = f$.  
由上面的问题可知 $A = A_1 \oplus A_2$, $B = B_1 \oplus B_2$，其中 $A_1, B_1$ 是幺作用模，$A_2, B_2$ 是 $R$-模，且 $R(A_2) = 0 = R(B_2)$. $P$ 如果自身是幺作用模就有 $P_1 = P, P_2 = 0$，所以有 $f(P) = f(P_1) \subset B_1$. $g$ 是满同态有 $g \mid A_1: A_1 \rightarrow B_1$ 是满同态。我们可以将原图限制到幺作用模的图表上去：

\tikzcd
    & P \arrow[d, "f"] & \\
    A_1 \arrow[r, "g \mid A_1"] & B_1 \arrow[r] & 0

于是，存在 $R$-模同态 $h: P \rightarrow A$ 使得 $g \circ h = f$ 等价于存在 $R$-模同态 $h: P \rightarrow A_1$ 使得 $(g \mid A_1) \circ h = f$.

!!! note "定理"
    含幺环 $R$ 上的自由模 $F$ 是投射模.

一个显然的推论。

!!! success "推论"
    环 $R$ 上的每个模 $A$ 都是某个投射 $R$-模的同态像.

!!! note "定理"
    （投射摸的等价条件）设 $R$ 是环。关于 $R$-模 $P$ 的下列条件等价：  
    (i) $P$ 是投射模;  
    (ii) 每个短正合序列 $0 \rightarrow A \xrightarrow{f} B \xrightarrow{g} P \rightarrow 0$ 都是分裂正合序列，从而 $B \cong A \oplus P$;  
    (iii) 存在自由 $R$-模 $F$ 和 $R$-模 $K$，使得 $F \cong P \oplus K$.

??? note "证明"
    (i) $\Rightarrow$ (ii) 考虑图表 
    \tikzcd 
        & P \arrow[d, "1_P"] & \\  
        B \arrow[r, "g"] & P \arrow[r] & 0
    由假设可知底部是正合的。由投射模的定义可知存在 $R$-模同态 $h: P \rightarrow B$ 使得 $g \circ h = 1_P$. 从而可知短正合序列 $0 \rightarrow A \xrightarrow{f} B \overset{g}{\underset{h}{\rightleftarrows}} P \rightarrow 0$ 是分裂正合序列，也就有 $B \cong A \oplus P$.  
    (ii) $\Rightarrow$ (iii) 因为每个 $R$-模都是某个自由 $R$-模的同态像，所以存在自由 $R$-模 $F$ 和满同态 $g: F \rightarrow P$. 如果 $K = \operatorname{Ker} g$，则序列 $0 \rightarrow K \rightarrow F \xrightarrow{g} P \rightarrow 0$ 是正合的，从而由假设是分裂正合的，故 $F \cong K \oplus P$.  
    (iii) $\Rightarrow$ (i) 设 $\varphi$ 是复合映射 $F \cong P \oplus K \xrightarrow{\pi} P$, $\psi$ 是复合映射 $P \xrightarrow{\iota} P \oplus K \cong F$. 给出 $R$-模同态图表
    \tikzcd
        & P \arrow[d, "\varphi"] & \\
        A \arrow[r, "f"] & B \arrow[r] & 0
    并且底行是正合的. 考虑图表  
    \tikzcd
        & F \arrow[ldd, swap, "h"] \arrow[d, bend right = 30, "\varphi"] & \\
        & P \arrow[ld, "h'"] \arrow[d, "f"] \arrow[u, bend right = 30, swap, "\psi"]& \\
        A \arrow[r, "g"] & B \arrow[r] & 0
    因为 $F$ 是投射模，从而有 $R$-模同态 $h: F \rightarrow A$，使得 $gh = f\varphi$. 令 $h' = h\psi: P \rightarrow A$，则 $gh' = gh\psi = f\varphi\psi = f(\varphi\psi) = f1_P = f$，从而 $P$ 是投射摸.  

!!! success "命题"
    设 $R$ 是环，$R$-模直和 $\sum_{i \in I} P_i$ 是投射模的充要条件是每个 $P_i$ 都是投射模.

??? success "证明"
    $(\Rightarrow)$ 在上一证明的 (iii) $\Rightarrow$ (i) 中，令 $F = \sum_{i \in I} P_i$，$K = \sum_{i \neq j} P_i$，$P = P_j$，则可以得到 $P_j$ 是投射模.  
    $(\Leftarrow)$ 考虑图表  

    \tikzcd
        & P_j \arrow[ldd, swap, "h_j"] \arrow[d, bend right = 30,"\varphi_j"] & \\
        & \sum P_i \arrow[d, "f"] \arrow[u, bend right = 30, swap, "\psi_j"]& \\
        A \arrow[r, "g"] & B \arrow[r] & 0

    若每个 $P_i$ 都是投射模，则存在 $R$-模同态 $h_j: P_j \rightarrow A$ 使得 $gh_j = f\varphi_j$. 从而存在唯一的 $R$-模同态 $h: \sum P_i \rightarrow A$ 使得 $h\varphi_j = h_j$，从而 $gh = f$，即 $\sum P_i$ 是投射模.

定义投射摸的对偶概念。

!!! info "定义"
    环 $R$ 上的模 $J$ 被称为**内射模**(injective module)，是指任意给下面一个 $R$-模同态图表  
    \tikzcd
        0 \arrow[r] & A \arrow[r, "g"] \arrow[d, "f"] & B \\  
        & J &
    并且顶行都是正合的，也就是说 $g$ 是单射，都存在 $R$-模同态 $h: B \rightarrow J$ 使得 $h \circ g = f$.  
    这个定义就是在说存在 $h$ 使得下面的图表交换。
    \tikzcd
        0 \arrow[r] & A \arrow[r, "g"] \arrow[d, "f"] & B \arrow[ld, "h"] \\  
        & J &

依赖于对偶性，我们也能证明前面部分命题的对偶命题。

!!! success "命题"
    设 $R$ 是环，$R$-模直积 $\prod_{i \in I} P_i$ 是内射模的充要条件是每个 $P_i$ 都是内射模.

因为自由模不存在对偶概念，所以内射模没有类似于投射摸和自由模之间联系的命题。但考虑每个模都是某个投射模的同态像，事实上是对于每个模 $A$，存在一个投射模 $P$ 和正合列 $P \rightarrow A \rightarrow 0$，其对偶应当是，对于每个模 $A$，存在一个内射模 $J$ 和正合列 $0 \rightarrow A \rightarrow J$，也就是说，每个模都能被嵌入某个内射模中。这个命题的证明需要一些准备工作。

!!! success "引理"
    设 $R$ 是含幺环. 则幺作用 $R$-模 $J$ 是内射模的充要条件是对于 $R$ 的每个左理想 $L$，$R$ 模同态 $L \rightarrow J$ 均可以被扩张到 $R$-模同态 $R \rightarrow J$.  

!!! info "定义"
    阿贝尔群 $D$ 被称作**可除的**(divisible)，是指对于任意给定的 $y \in D$ 和 $0 \neq n \in \mathbf{Z}$，都存在 $D$ 中的元素 $x$ 使得 $nx = y$. 不难证明，阿贝尔群的直和是可除群当且仅当每个直和分量都是可除群. 同时可以证明，每个可除群的同态像都是可除群.

!!! success "引理"
    阿贝尔群 $D$ 是可除群等价于 $D$ 是内射(幺作用) $\mathbf{Z}$-模.

??? success "证明"
    $(\Rightarrow)$ 设 $D$ 是可除群，注意到 $\mathbf{Z}$ 的左理想均是循环群 $\langle n \rangle$, $n \in \mathbf{Z}$. 设 $f: \langle n \rangle \rightarrow D$ 是同态，则存在 $x \in D$ 使得 $nx = f(n)$. 定义 $h: \mathbf{Z} \rightarrow D$, $1 \mapsto x$，则 $h$ 是同态，且 $h(n) = nx = f(n)$，从而 $h$ 是扩张. 所以 $D$ 是内射 $\mathbf{Z}$-模.  
    $(\Leftarrow)$ 设 $D$ 是内射 $\mathbf{Z}$-模，$y \in D$, $0 \neq n \in \mathbf{Z}$，定义 $f: \langle n \rangle \rightarrow D$, $n \mapsto y$，则 $f$ 是同态. 因为 $D$ 是内射 $\mathbf{Z}$-模，所以存在 $h: \mathbf{Z} \rightarrow D$ 使得下图交换

    \tikzcd
        0 \arrow[r] & \langle n \rangle \arrow[r, "\subset"] \arrow[d, "f"] & \mathbf{Z} \arrow[ld, "h"] \\
        & D & 

    若 $h(1) = x$，则 $h(n) = nx = f(n) = y$，从而 $D$ 是可除群.

!!! success "引理"
    每个阿贝尔群均可以嵌入可除阿贝尔群中.  

若 $R$ 是含幺环，而 $J$ 是阿贝尔群，则 $\operatorname{Hom}_{\mathbf{Z}}(R, J)$ 也是阿贝尔群，并可以验证，$\operatorname{Hom}_{\mathbf{Z}}(R, J)$ 是幺作用左 $R$-模，其中 $R$ 作用为 $(rf)(x) = f(xr)$.  

!!! success "引理"
    如果 $J$ 是可除阿贝尔群，$R$ 是含幺环，则 $\operatorname{Hom}_{\mathbf{Z}}(R, J)$ 是内射左 $R$-模.

??? success "证明"
    我们只需要证明，对于 $R$ 的每一个左理想 $L$，任意 $R$-模同态 $f: L \rightarrow \operatorname{Hom}_{\mathbf{Z}}(R, J)$ 都可以扩张到 $R$-模同态 $h: R \rightarrow \operatorname{Hom}_{\mathbf{Z}}(R, J)$. 由 $g(a) = [f(a)](1_R)$ 给出的映射 $g: L \rightarrow J$ 是同态. 因为 $J$ 是可除群，所以 $J$ 是内射 $\mathbf{Z}$-模，并且有图表  
    \tikzcd
        0 \arrow[r] & L \arrow[r, "\subset"] \arrow[d, "g"] & R \\
        & J &
    从而有群同态 $\bar{g}: R \rightarrow J$ 使得 $\bar{g} \mid L = g$. 定义 $h: R \rightarrow \operatorname{Hom}_{\mathbf{Z}}(R, J)$, $r \mapsto h(r)$，其中 $[h(r)](x) = \bar{g}(xr)$. 验证 $h$ 的良定义性，验证 $h$ 是群同态.  

!!! success "命题"
    (i) 含幺环 $R$ 上的每个幺作用模 $A$ 均可以嵌入某个内射 $R$-模中.  
    (ii) 设 $R$ 是含幺环，则关于幺作用 $R$-模 $J$ 的下列条件等价：  
    (a) $J$ 是内射模;  
    (b) 每个短正合序列 $0 \rightarrow J \xrightarrow{f} B \xrightarrow{g} C \rightarrow 0$ 都是分裂正合序列，从而 $B \cong J \oplus C$;  
    (c) 如果 $J$ 是某个 $R$-模 $B$ 的子模，则 $J$ 是 $B$ 的直和因子.