# 幂零群和可解群 正规列和次正规列

首先是**升中心列**(ascending central series) 的构造。

!!! info "定义"
    设 $G$ 是一群，其中心 $C(G)$ 是 $G$ 的正规子群. 设 $C_2(G)$ 是 $C(G/C(G))$ 在典范满射下的原像，那么 $C_2(G)$ 也是 $G$ 的正规子群，且包含 $C(G)$. 那么照此进行递归定义：$C_1(G) = C(G)$，$C_i(G)$ 是 $C(G/C_{i-1}(G))$ 在典范满射下的原像. 那么我们得到了 $G$ 的一个正规子群列，称为 $G$ 的升中心列：$\langle e \rangle < C_1(G) < C_2(G) < \cdots$.

??? tip "提示"
    $C_1(G) = C(G) = \{g \mid ag = ga, \forall a \in G\}$ 考虑 $G/C_1(G)$，其中的元素都具有 $gC_1(G)$ 的形式，而且 $C(G/G_1(C))$ 中的元素满足如下性质：$\forall a \in G, gC_1(G) \in C(G/C_1(G))$，则 $(aC_1(G))(gC_1(G)) = agC_1(G) = (gC_1(G))(aC_1(G)) = gaC_1(G)$. 所以 $C_2(G) = \{g \mid (aC_1(G))(gC_1(G)) = (gC_1(G))(aC_1(G)), \forall a \in G\}$. 进而有 $C_{i+1}(G) = \{g \mid (aC_{i}(G))(gC_{i}(G)) = (gC_{i}(G))(aC_{i}(G)), \forall a \in G\}$.

由此导出**幂零群**(nilpotent group)的定义。

!!! info "定义"
    若 $\exists n$ 使得 $C_n(G) = G$，则群 $G$ 是幂零群.

!!! note "定理"
    (i) 所有有限 $p$-群都是幂零的.  
    (ii) 有限个幂零群的直积依然是幂零的.  

??? note "证明"
    (i) $G$ 和它的所有非平凡商群都是 $p$-群，所以它们都有非平凡的中心，也就是说若 $G \neq C_i(G)$，则 $C_i(G)$ 严格包含在 $C_{i+1}(G)$ 中. 因为 $G$ 是有限群，所以必然存在 $n$，使得 $C_n(G) = G$.

!!! success "引理"
    若 $H$ 是幂零群 $G$ 的一个真子群，则 $H$ 是 $N_G(H)$ 的真子群.

!!! note "定理"
    一个有限群是幂零的等价于它是自身 Sylow 子群的直积.

??? note "证明"
    $(\Leftarrow)$ 由所有有限 $p$-群都是幂零的和有限个幂零群的直积依然是幂零的可知.  
    $(\Rightarrow)$ 设 $G$ 是一个有限幂零群，$P$ 是 $G$ 的 Sylow $p$-子群. 要么 $P = G$，此时证毕，要么 $P$ 是 $G$ 的真子群. 对于后者，由引理有 $P$ 是 $N_G(P)$ 的真子群. 而因为 $N_G(N_G(P)) = N_G(P)$，所以 $N_G(P)$ 不是 $G$ 的一个真子群，也就是说 $N_G(P) = G$. 所以 $P$ 是 $G$ 的正规子群，也就是 $G$ 中唯一的 Sylow $p$-子群.  
    对 $G$ 的阶进行唯一素分解，即 $\lvert G \rvert = p_1^{n_1} \cdots p_k^{n_k}$. 令 $P_i$ 是 $G$ 对应的 Sylow $p_i$-子群. $\lvert P_i \rvert = p_i^{n_i}$，且有 $P_i \cap P_j = \langle e \rangle, i \neq j$. 回忆之前关于正规子群性质的介绍，若 $N, K$ 都是正规子群，则有 $NK = KN$. 所以对于 $x \in P_i, y \in P_j(i \neq j)$，有 $xy = yx$. 从而 $P_1P_2 \cdots P_{i-1} P_{i+1} \cdots P_k$ 是 $G$ 的子群，且其中元素的阶都整除 $p_1^{n_1} \cdots p_{i-1}^{n_{i-1}} p_{i+1}^{n_{i+1}} \cdots p_k^{n_k}$. 从而 $P_i \cap P_1P_2 \cdots P_{i-1} P_{i+1} \cdots P_k = \langle e \rangle$，且 $P_1P_2 \cdots P_{k} = P_1 \times P_2 \times \cdots \times P_k$. 而 $\lvert G \rvert = p_1^{n_1} \cdots p_k^{n_k} = \lvert P_1 \times P_2 \times \cdots \times P_k \rvert = \lvert P_1 \cdots P_k \rvert$. 所以 $G = P_1 \times P_2 \times \cdots \times P_k$.

!!! success "推论"
    若 $G$ 是一个有限幂零群，且 $m$ 整除 $\lvert G \rvert$，则 $G$ 有一个阶为 $m$ 的子群.

!!! info "定义"
    设 $G$ 是一群. $G$ 的由集合 $\{aba^{-1}b^{-1} \mid a, b \in G\}$ 生成的子群称为 $G$ 的**交换子群**(commutator subgroup)，记作 $G'$. 元素 $aba^{-1}b^{-1}$ 被称为**交换子**(commutators).

交换子群实际上衡量了原群 $G$ 与阿贝尔群的差距。

!!! note "定理"
    设 $G$ 是一群，则 $G'$ 是 $G$ 的正规子群，且 $G/G'$ 是阿贝尔群. 若 $N$ 是正规子群，则 $G/N$ 可交换等价于 $N$ 包含 $G'$.

??? note "证明"
    考虑 $f: G \rightarrow G$ 是任一自同构，则有 $f(aba^{-1}b^{-1}) = f(a)f(b)f(a)^{-1}f(b) \in G'$. 从而 $f(G') < G'$. 特别地，若 $f$ 是由 $a \in G$ 共轭作用给出的自同构，则 $aG'a^{-1} = f(G') < G'$，所以 $G'$ 是 $G$ 的正规子群.  
    因为 $ab(ba)^{-1} = aba^{-1}b^{-1} \in G'$，所以 $abG' = baG'$，即 $G/G'$ 是阿贝尔群.   
    如果 $G/N$ 是阿贝尔群，则 $\forall a, b \in G, abN = baN$，也就有 $ab(ba)^{-1} = aba^{-1}b^{-1} \in N$，即 $N$ 包含全部换位子，从而 $G' < N$. 反方向是平凡的.

!!! info "定义"
    设 $G$ 是一群，$G^{(1)}$ 定义为 $G'$，继续递归定义：$G^{(i)}$ 为 $(G^{(i-1)})'$，$G^{(i)}$ 被称为 $G$ 的 $i$ 阶**导群**(derived subgroup)，其生成了一个降序列：$G > G^{(1)} > G^{(2)} > \cdots$. 且任意导群都是 $G$ 的正规子群.

!!! info "定义"
    群 $G$ 被称为**可解的**(solvable)，若存在 $n$ 使得 $G^{(n)} = \langle e \rangle$.

!!! note "定理"
    所有幂零群都是可解群.

??? note "证明"
    考虑 $C_i(G)$ 的定义，$C_i(G) = \{g \mid (aC_{i-1}(G))(gC_{i-1}(G)) = (gC_{i-1}(G))(aC_{i-1}(G)), \forall a \in G\}$，从而 $C_{i}(G)/C_{i-1}(G) = C(G/C_{i-1}(G))$ 是阿贝尔群，由上一定理可知 $C_{i}(G)' < C_{i-1}(G), \forall i > 1$，且 $C_1(G) = C(G)$ 是阿贝尔群，其导群为 $\langle e \rangle$. 因为 $G$ 是幂零群，所以存在 $n \in N$，使得 $G = C_n(G)$. 从而，$C(G/C_{n-1}(G)) = C_n(G)/C_{n-1}(G) = G/C_{n-1}(G)$ 是阿贝尔群，所以有 $G^{(1)} = G' < C_{n-1}(G)$. 考虑子群的导群是原群导群的子群，所以 $G^{(2)} = {G^{(1)}}' < C_{n-1}(G)' < C_{n-2}(G)$，$G^{(3)} < C_{n-2}(G)' < C_{n-3}(G)$，以此类推，$G^{(n)} < C_1(G) = C(G) = \langle e \rangle$，所以 $G^{(n)} = \langle e \rangle$.

!!! note "定理"
    (i) 可解群的子群和同态像也是可解的.  
    (ii) 若 $N$ 是 $G$ 的正规子群，且 $N$ 和 $G/N$ 均是可解的，则 $G$ 是可解的.

!!! success "推论"
    若 $n \geqslant 5$，则对称群 $S_n$ 不可解. 

??? tip "提示"
    考虑交错群 $A_n$，$n \geqslant 5$ 时其是单群.

在定义幂零群和可解群的时候我们利用了正规列，下面我们来研究它们。

!!! info "定义"
    (i) 群 $G$ 的**次正规列**(subnormal series) 是一串满足 $G_{i+1}$ 在 $G_i$ 中正规的子群：$G = G_0 > G_1 > \cdots > G_n, 0 \leqslant i < n$. 列的**因子**(factor) 是商群 $G_i/G_{i+1}$，列的**长度**(length) 是其非平凡因子的个数. 若 $G_i$ 均是 $G$ 的正规子群，则此列称为**正规列**(normal series).  
    (ii) 设 $G = G_0 > G_1 > \cdots > G_n$ 是一次正规列，则形如 $G = G_0 > G_1 > \cdots > G_i > N > G_{i+1} > \cdots > G_n$ 或 $G = G_0 > G_1 > \cdots > G_n > N$ 的列称为 $G = G_0 > G_1 > \cdots > G_n$ 的 **一步加细**(one-step refinement)，其中 $N$ 是 $G_i$ 的正规子群且 $G_{i+1} 是 N$ 的正规子群. 次正规列 $S$ 通过有限次一步加细得到的任一次正规列，都称作 $S$ 的**细化**(refinement). 若 $S$ 的一个细化的长度大于 $S$ 的长度，则称其为 $S$ 的**真细化**(proper refinement).  
    (iii) 次正规列 $G = G_0 > G_1 > \cdots > G_n = \langle e \rangle$ 被称为**合成列**(composition series)，若其因子 $G_i/G_{i+1}$ 都是单群；若 $G_i/G_{i+1}$ 都是阿贝尔群，则称其为**可解列**(solvable series).

!!! note "定理"
    (i) (a) 每个有限群 $G$ 均有合成列；  
        (b) 可解列的任一细化仍是可解列；  
        (c) 一个次正规列是合成列当且仅当它没有真细化.  
    (ii) 群 $G$ 是可解的等价于 $G$ 有可解列.  
    (iii) 有限群 $G$ 是可解的等价于 $G$ 有合成列，且其因子都是素阶循环群.

!!! info "定义"
    群 $G$ 的两个次正规列 $S$ 和 $T$ 被称作**等价的**(equivalent)，若它们的非平凡因子之间存在一一对应，使得相应的因子同构.

显然，如果 $S$ 是群 $G$ 的合成列，则 $S$ 的每个加细均与 $S$ 等价。

!!! note "定理"
    (Jordan-Hölder) 群 $G$ 任意两个合成列都是等价的. 所以，每个群的合成列都唯一决定了一串单群.