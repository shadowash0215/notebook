# Sylow 定理 有限群分类

!!! success "引理"
    若一群 $H$ 的阶为 $p^n$，$p$ 是素数，其作用在一有限集 $S$ 上. 定义集合 $S_0 = \{x \in S \mid hx = x, \forall h \in H\}$，则 $\lvert S \rvert \equiv \lvert S_0 \rvert \pmod p$.

??? success "证明"
    若 $x \in S_0$，则轨道 $\bar{x}$ 只包含一个元素（与前一节中 $g \in C(G)$ 以及共轭类的关系一致），所以 $S$ 可以被写作一系列集合的无交并：$S = S_0 \cup \bar{x}_1 \cup \bar{x}_2 \cdots \cup \bar{x}_n$，且 $\bar{x}_i > 1, \forall i$. 所以 $\lvert S \rvert = \lvert S_0 \rvert + \lvert \bar{x}_1 \rvert + \lvert \bar{x}_2 \rvert + \cdots + \lvert \bar{x}_n \rvert$. 考虑到 对任一 $i$，因为 $\lvert \bar{x}_i \rvert > 1$ 且 $\lvert \bar{x}_i \rvert = [H : H_{x_i}] \mid \lvert H \rvert = p^n$，所以 $p \mid \lvert \bar{x}_i \rvert$，$\lvert S \rvert \equiv \lvert S_0 \rvert \pmod p$

!!! note "定理"
    (Cauchy) 若 $G$ 是一阶被素数 $p$ 整除的有限群，则 $G$ 中有一元素阶为 $p$.

??? note "证明"
    设 $S = \{(a_1, a_2, \ldots, a_p) \mid a_i \in G, a_1a_2\cdots a_p = e\}$. 因为 $a_p = (a_1a_2\cdots a_{p-1})^{-1}$，所以 $\lvert S \rvert = n^{p-1}$，其中 $n = \lvert G \rvert$. 因为 $p \mid n$，所以 $\lvert S \rvert \equiv 0 \pmod p$. 设群 $Z_{p}$ 在集合 $S$ 上的作用为循环置换，即 $k \in Z_p, k(a_1, a_2, \ldots, a_p) = (a_{k+1}, a_{k+2}, \ldots, a_p, a_1, \ldots, a_k)$.  
    验证 $(a_{k+1}, a_{k+2}, \ldots, a_p, a_1, \ldots, a_k) \in S$. 令 $(a_1a_2\cdots a_k) = a, (a_{k+1}a_{k+2}\cdots a_p) = b$，则 $ab = e$. 而 $ba = (a^{-1}a)(ba) = a^{-1}(ab)a = e$，所以 $(a_{k+1}, a_{k+2}, \ldots, a_p, a_1, \ldots, a_k) \in S$.  
    验证对于 $0, k, k' \in Z_p, x \in S$，有 $0x = x, (k + k')x = k(k'x)$. 所以群作用是良定义的.  
    所以 $(a_1, a_2, \ldots, a_n) \in S_0$ 表明 $a_1 = a_2 = \cdots a_n$. 显然 $(e, e, \ldots, e) \in S_0$，所以 $\lvert S_0 \rvert \neq 0$. 而由上可知 $0 \equiv \lvert S \rvert \equiv \lvert S_0 \rvert \pmod p$. 故 $S_0$ 中至少存在 $p$ 个元素，也就是 $\exists a \neq e$，使得 $(a, a, \ldots, a) \in S_0$，从而 $a^p = e.$ 因为 $p$ 是素数，所以 $\lvert a \rvert = p$.

由此衍生出 **$p$-群**(p-group)的定义.

!!! info "定义"
    若群 $G$ 中的所有元素的阶都是某一固定素数 $p$ 的幂次，则称群 $G$ 为 $p$-群.  
    若 $H$ 是 $G$ 的子群且为一 $p$-群，则称 $H$ 为 $G$ 的 **$p$-子群**(p-subgroup).

!!! success "推论"
    (i) 有限群 $G$ 是 $p$-群等价于 $\lvert G \rvert$ 是 $p$ 的幂次.  
    (ii) 非平凡有限 $p$-群 $G$ 的中心 $C(G)$ 含有不止一个元素.

??? success "证明"
    (ii) 考虑类方程 

    $$
        \lvert G \rvert = \lvert C(G) \rvert + \sum_{i = 1}^m [G : C_G(x_i)],
    $$

    $[G : C_G(x_i)] > 1$，且 $[G : C_G(x_i)] \mid \lvert G \rvert = p^n$，所以 $p \mid [G : C_G(x_i)]$，且 $p \mid \lvert G \rvert$. 进而 $\lvert C(G) \rvert \equiv 0 \pmod p$. 由于 $\lvert C(G) \rvert \geqslant 1$，所以 $C(G)$ 中至少有 $p$ 个元素.

!!! success "引理"
    (i) 若 $H$ 是有限群 $G$ 的一个 $p$-子群，那么 $[N_G(H) : H] \equiv [G : H] \pmod p$.  
    (ii) 若 $H$ 是有限群 $G$ 的一个 $p$-子群，且 $p$ 整除 $[G : H]$，则 $N_G(H) \neq H$.

??? success "证明"
    (i) 考虑 $S$ 是 $H$ 在 $G$ 中全体左陪集构成的集合，且 $H$ 在 $S$ 上的作用是左平移，则 $\lvert S \rvert = [G : H]$，且 

    $$
        xH \in S_0 \Leftrightarrow hxH = xH(\forall h \in H) \Leftrightarrow x^{-1}hxH = H(\forall h \in H) \Leftrightarrow x^{-1}hx \in H(\forall h \in H).
    $$
    
    进而 $x^{-1}Hx = H$，也就有 $xHx^{-1} = H$，所以 $x \in N_G(H)$. $\lvert S_0 \rvert$ 是陪集 $xH(x \in N_G(H))$ 的个数，即 $\lvert S_0 \rvert = [N_G(H) : H]$. 进而 $[N_G(H) : H] = \lvert S_0 \rvert \equiv \lvert S \rvert  = [G : H] \pmod p$.  
    (ii) 是 (i) 的直接推论.

!!! note "$\star$定理"
    (First Sylow Theorem) 设 $G$ 是一阶为 $p^nm$ 的群，$n \geqslant 1$，$p$ 是一素数，且 $(p, m) = 1$. 则对任一 $1 \leqslant i \leqslant n$，$G$ 均包含 $p^i$ 阶子群，并且 $G$ 的每个 $p^i(i < n)$ 阶子群均是某个 $p^{i+1}$ 阶子群的正规子群.

??? note "证明"
    因为 $p \mid \lvert G \rvert$，所以由 Cauchy 可知 $G$ 包含一个 $p$ 阶元素 $a$，也就包含 $p$ 阶子群 $\langle a \rangle$.  
    现归纳假设 $H$ 是 $G$ 的 $p^i$ 阶子群，$1 \leqslant i < n$. 所以 $p \mid [G : H]$. 而 $H$ 是 $N_G(H)$ 的正规子群. 由上述两引理可知 $H \neq N_G(H)$ 且 $1 < \lvert N_G(H)/H \rvert = [H_G(H) : H] \equiv [G : H] \equiv 0 \pmod p$. 所以 $p \mid \lvert N_G(H)/H \rvert$.  
    由 Cauchy 可知 $N_G(H)/H$ 包含一 $p$ 阶子群，此子群具有形式 $H_1/H$，其中 $H_1$ 是 $N_G(H)$ 的子群并且 $H_1$ 包含 $H$. 因为 $H \triangleleft N_G(H)$，所以 $H \triangleleft H_1$. 最终 $\lvert H_1 \rvert = \lvert H \rvert \lvert H_1/H \rvert = p^ip = p^{i+1}$. 

进而，$G$ 的一个子群 $P$ 被称为 **Sylow $p$-子群**(Sylow p-subgroup)，若其是 $G$ 中最大的 $p$-子群. 进而每个 $p$-子群均包含在某个 Sylow $p$-子群中. 上一定理表明，对于任一素数 $p \mid \lvert G \rvert$，有限群 $G$ 必有非平凡的 Sylow $p$-子群.

!!! success "推论"
    设 $G$ 是一阶为 $p^nm$ 的群，$n \geqslant 1$，$p$ 是一素数，且 $(p, m) = 1$. 设 $H$ 是 $G$ 的一个 $p$-子群，则  
    (i) $H$ 是 $G$ 的一个 Sylow $p$-子群等价于 $\lvert H \rvert = p^n$.  
    (ii) Sylow $p$-子群的每个共轭也是 Sylow $p$-子群.  
    (iii) 如果 $G$ 只有一个 Sylow $p$-子群 $P$，则 $P \triangleleft G$.

??? success "证明"
    (ii) 引理：若 $H < G$，$a \in G$，则 $aHa^{-1}$ 是 $G$ 的子群，且 $aHa^{-1} \cong H$.

考虑上一推论的第二条的逆，我们可以得到如下定理：

!!! note "$\star$定理"
    (Second Sylow Theorem) 设 $H$ 是有限群 $G$ 的一个 $p$-子群，$P$ 是 $G$ 的任意 Sylow $p$-子群，那么存在  $x \in G$，使得 $H < xPx^{-1}$. 特别地，$G$ 的任意两个 Sylow $p$-子群均互为共轭.

??? note "证明"
    设 $S$ 是 $P$ 在 $G$ 上的全体左陪集构成的集合，$H$ 在 $S$ 上的作用是左平移. 由引理 $\lvert S_0 \rvert \equiv \lvert S \rvert = [G : P] \pmod p.$ 但 $p \not \mid [G : P],$ 所以 $\lvert S_0 \rvert \neq 0$. 即存在 $xP \in S_0$.  
    从而有 $xP \in S_0 \Leftrightarrow hxP = xP(\forall h \in H) \Leftrightarrow x^{-1}hxP = P(\forall h \in H) \Leftrightarrow x^{-1}Hx < P \Leftrightarrow H < xPx^{-1}$.   
    特别地，如果 $H$ 是 Sylow $p$-子群，则 $\lvert H \rvert = \lvert P \rvert = \lvert xPx^{-1} \rvert$. 所以 $H = xPx^{-1}$.

接下来是一些定量的刻画.

!!! note "$\star$定理"
    (Third Sylow Theorem) 设 $G$ 是一有限群，$p$ 是一素数，那么 $G$ 的 Sylow $p$-子群的个数整除 $\lvert G \rvert$，且模 $p$ 余 1.

??? note "证明"
    由 Second Sylow Theorem, Sylow $p$-子群的个数是他们之中任一个（设为 $P$）的共轭子群个数，其为 $[G : N_G(P)],$ 是 $\lvert G \rvert$ 的因子. 令 $S$ 为 $G$ 的全体 Sylow $p$-子群所组成的集合，$P$ 在 $S$ 上的作用是共轭，则 $Q \in S_0 \Leftrightarrow xQx^{-1} = Q(\forall x \in P)$，其又等价于 $P < N_G(Q)$. 而 $P, Q$ 都是 $G$ 的 Sylow $p$-子群，$N_G(Q) < G$，$Q < N_G(Q)$，故 $P, Q$ 均是 $N_G(Q)$ 的 Sylow $p$-子群，二者在 $N_G(Q)$ 中共轭. 但 $Q$ 在 $N_G(Q)$ 中正规，所以 $Q = P$，$S_0 = \{P\}$. 而 $\lvert S \rvert \equiv \lvert S_0 \rvert = 1 \pmod p$，所以 $\lvert S \rvert = kp+1$.

!!! note "定理"
    若 $P$ 是有限群 $G$ 的一个 Sylow $p$-子群，则 $N_G(N_G(P)) = N_G(P)$.

??? note "证明"
    设 $N = N_G(P)$，有 $P \triangleleft N$. 因为 $P$ 是 $G$ 的一个 Sylow $p$-子群，所以 $P$ 也是 $N$ 的 Sylow $p$-子群. 而 $P \triangleleft N$，所以 $P$ 是 $N$ 中唯一的 Sylow $p$-子群.  
    设 $g \in N_G(N)$，则 $gPg^{-1} < gNg^{-1} = N$. 因为 Sylow $p$-子群的共轭也是 Sylow $p$-子群，所以 $gPg^{-1}$ 是 $G$ 的 Sylow $p$-子群，也是 $N$ 的 Sylow $p$-子群. 而 $P$ 是 $N$ 中唯一的 Sylow $p$-子群，故 $gPg^{-1} = P$，$g \in N$.  
    $g \in N_G(N) \rightarrow g \in N$，故 $N_G(N) < N$. 而 $N < N_G(N)$ 是显然的，故 $N = N_G(N)$，也就是 $N_G(N_G(P)) = N_G(P)$.

以下是对小阶数群和阶与素数相关的群的分类。

!!! success "推论"
    (i)设 $p$ 和 $q$ 均为素数，且 $p>q$. 若 $q \nmid p-1$，则所有阶为 $pq$ 的群均同构于循环群 $Z_{pq}$. 若 $q \mid p-1$，则阶为 $pq$ 的群存在（同构于）以下两种群：循环群 $Z_{pq}$ 和由满足以下条件的元素 $c, d$ 生成的非阿贝尔群 $K$，

    $$
        \lvert c \rvert = p, \lvert d \rvert = q, dc = c^sd,
    $$

    其中 $s \not \equiv 1 \pmod p$ 且 $s^q \equiv 1 \pmod p.$

    (ii) 若 $p$ 是奇素数，那么所有阶为 $2p$ 的群要么同构于循环群 $Z_{2p}$，要么同构于二面体群 $D_p$.

    (iii) 8 阶非阿贝尔群是（同构于）以下两种群：四元群 $Q_8$ 和二面体群 $D_4$.

    (iv) 12 阶非阿贝尔群是（同构于）以下三种群：二面体群 $D_6$，置换群 $A_4$，和 $T = \langle a, b \rangle$，其中 $\lvert a \rvert = 6, b^2 = a^3$，且 $ba = a^{-1}b$.

??? success "证明"
    给定 $pq$ 阶群 $G$，由 Cauchy 可知 $G$ 包含元素 $a, b$，$\lvert a \rvert = p, \lvert b \rvert = q$. 

(i) 中的第二种群被称为**亚循环群**(metacyclic group)
