# 主理想整环上的有限生成模

!!! note "定理"
    (i) 设 $F$ 是主理想整环 $R$ 上的自由模，且 $G$ 是 $F$ 的子模，则 $G$ 也是自由模且 $\operatorname{rank} G \leqslant \operatorname{rank} F$.  
    (ii) 设 $R$ 是主理想整环，$A$ 是由 $n$ 个元素生成的 $R$-模，则 $A$ 的每个子模均可由 $m$ 个元素生成，其中 $m \leqslant n$.

!!! success "推论"
    主理想整环上的幺作用模 $A$ 是自由模当且仅当 $A$ 是投射模.  

下面研究群中元素的阶和阿贝尔群的扭子群到模上的推广。

!!! note "定理"
    设 $A$ 是整环 $R$ 上的左模，对任一 $a \in A$，设 $\mathcal{O}_a = \{r \in R \mid ra = 0\}$，则  
    (i) 对任一 $a \in A$，$\mathcal{O}_a$ 是 $R$ 的理想.  
    (ii) $A_t = \{a \in A \mid \mathcal{O}_a \neq 0\}$ 是 $A$ 的一个子模.  
    (iii) 对任一 $a \in A$ 存在左模同构 $R/\mathcal{O}_a \cong Ra = \{ra \mid r \in R\}$.  
    设 $R$ 是主理想整环且 $p$ 是素数，$p \in R$，则  
    (iv) 若 $p^ia = 0$(等价于 $(p^i) \subset \mathcal{O}_a$)，则存在 $0 \leqslant j \leqslant i$ 使得 $\mathcal{O}_a = (p^j)$.  
    (v) 若 $\mathcal{O}_a = (p^i)$，则对任意 $0 \leqslant j < i$，$p^ja \neq 0$.

设 $A$ 是一整环上的模，上述定理中的理想 $\mathcal{O}_a$ 被称作 $a \in A$ 的**零化理想**(annihilator ideal). 上述定理 (ii) 中的子模 $A_t$ 被称作 $A$ 的**扭子模**(torsion submodule). 若 $A_t = 0$，则称 $A$ 是**无扭模**(torsion-free module). 若 $A_t = A$，则称 $A$ 是**扭模**(torsion module). 每个自由模都是无扭模，但反之不正确.

设 $A$ 是主理想整环 $R$ 上的模，则 $a \in A$ 的零化理想是 $R$ 中的主理想。设 $\mathcal{O}_a = (r)$，则称 $a$ 有**阶 $r$**，元素 $r$ 在不计单位因子的意义下唯一确定。由 $a$ 生成的循环子模 $Ra$ 被称作 **$r$ 阶循环子模**(cyclic submodule of order $r$). 上述定理表明，$a \in A$ 的阶为 0 等价于 $Ra \cong R$. 另一方面，$a \in A$ 有阶 $r$ 且 $r$ 是单位等价于 $a = 0$。(因为 $a = 1_Ra = r^{-1}(ra) = r^{-1}0 = 0$)

!!! example "示例"
    设 $R$ 是主理想整环，$r \in R$，则商环 $R/(r)$ 是以 $a = 1_R + (r)$ 为生成元的循环 $R$-模。显然 $\mathcal{O}_a = (r)$，因此 $a$ 的阶为 $r$ 且 $R/(r)$ 是 $r$ 阶循环子模. 上述定理表明主理想整环上的所有循环子模 $C$ 都同构于 $R/(r)$，其中 $(r) = \mathcal{O}_a$ 而 $a$ 是 $C$ 的生成元.

下面开始是对主理想整环上的有限生成模的结构刻画。

!!! note "定理"
    主理想整环 $R$ 上的有限生成无扭模 $A$ 是自由模.

!!! note "定理"
    若 $A$ 是主理想整环 $R$ 上的有限生成模，则 $A = A_t \oplus F$，其中 $F$ 是秩有限的自由 $R$-模且 $F \cong A/A_t$.

??? note "证明"
    商模 $A/A_t$ 是无扭的，因为对于任意 $r \neq 0$，$r(a + A_t) = A_t \Rightarrow ra \in A_t \Rightarrow r_1(ra) = 0 \Rightarrow a \in A_t$. 此外，因为 $A$ 是有限生成的，所以 $A/A_t$ 也是有限生成的，因此 $A/A_t$ 是自由模.  
    而由序列 $0 \to A_t \xrightarrow{\iota} A \xrightarrow{\pi} A/A_t \to 0$ 是分裂正合的可知 $A \cong A_t \oplus A/A_t$. 此同构下 $A_t$ 的像是 $A_t$，而 $A/A_t$ 的像是 $A$ 的一个子模 $F$，$F$ 必然是秩有限的自由模，所以 $A = A_t \oplus F$.

这样我们把问题简化到如何刻画清楚主理想整环上的有限生成扭模了。

!!! note "定理"
    设 $A$ 是主理想整环上的扭模，对任一素数 $p \in R$，设 $A(p)$ 为 $A$ 中所有阶为 $p$ 的幂次的元素构成的集合，则  
    (i) 对任一素数 $p$, $A(p)$ 是 $A$ 的子模.  
    (ii) $A = \sum A(p)$，求和对象为 $A$ 中所有素元 $p$. 若 $A$ 是有限生成的，则只有有限个 $A(p)$ 不为零.

??? note "证明"
    (ii) 设 $0 \neq a \in A$ 且 $\mathcal{O}_a = (r)$. 由唯一分解定理，$r = p_1^{n_1}\cdots p_k^{n_k}$，其中 $p_i$ 为 $R$ 中的互异素数，且任一 $n_i > 0$. 对任一 $i$，设 $r_i = p_1^{n_1} \cdot p_{i - 1}^{n_{i-1}}p_{i + 1}^{n_{i+1}} \cdots p_k^{n_k}$，则 $(r_1, \ldots, r_k)$ 是互素的. 由裴蜀定理，存在 $s_1, \ldots , s_k \in R$ 使得 $s_1r_1 + \cdots + s_kr_k = 1_R$. 因而 $a = 1_Ra = (s_1r_1 + \cdots + s_kr_k)a = s_1r_1a + \cdots + s_kr_ka$. 而 $p_i^{n_i}s_ir_ia = s_ira = 0$，所以 $s_ir_ia \in A(p_i)$. 这就证明了当子模 $A(p)$ 中的素元 $p$ 取遍 $R$ 中所有素数时，其生成了 $A$.  
    下面证明是直和. 设 $p$ 是 $R$ 中素元，$A_1$ 是由全部 $A(q)(q \neq p)$ 所生成的 $A$ 的子模. 设 $a \in A(p) \cap A_1$，则存在 $m \geqslant 0$，$p^ma = 0$，且 $a = a_1 + \cdots + a_t$，$a_i \in A(q_i)$，$q_1, \ldots q_t$ 均是与 $p$ 互异的素数. 因为 $a_i \in A(q_i)$，所以存在 $m_i \geqslant 0$ 使得 $q_i^{m_i}a_i = 0$. 从而 $(q_1^{m_1}\cdots q_t^{m_t})a = 0$. 设 $d = q_1^{m_1}\cdots q_t^{m_t}$，则 $d$ 与 $p^m$ 互素，由裴蜀定理存在 $r, s \in R$，$rp^m + sd = 1_R$. 所以，$a = 1_Ra = (rp^m + sd)a = rp^ma + sda = 0$. 所以 $A(p) \cap A_1 = 0$，也就有 $A = \sum A(p)$，其中求和对象为 $R$ 中所有素元 $p$.

这样我们就又把问题简化到如何刻画清楚 $A(p)$ 了，但在此之前我们需要一个引理。对于 $R$-模 $A$ 和 $r \in R$，令 $rA = \{ra \mid a \in A\}$.  

!!! success "引理"
    设 $A$ 是主理想整环 $R$ 上的模，$p \in R$ 是素元，$n$ 为正整数，$p^nA = 0$ 但是 $p^{n-1}A \neq 0$. 设 $a$ 是 $A$ 中阶为 $p^n$ 的元素.  
    (i) 若 $A \neq Ra$，则存在非零元素 $b \in A$ 使得 $Ra \cap Rb = 0$.  
    (ii) 存在 $A$ 的子模 $C$，使得 $A = Ra \oplus C$.

!!! note "定理"
    设 $A$ 是主理想整环 $R$ 上的有限生成模，并且 $A$ 中的每个元素的阶均是 $R$ 中素元 $p$ 的幂次，则 $A$ 是阶分为 $p^{n_1}, \ldots, p^{n_k}$ 的循环 $R$-模的直和，其中 $n_1 \geqslant n_2 \geqslant \cdots \geqslant n_k \geqslant 1$.

!!! success "引理"
    设 $A, B, A_i(i \in I)$ 均是主理想整环 $R$ 上的模，$r \in R, p \in R$，其中 $p$ 是素元.  
    (i) $rA = \{ra \mid a \in A\}$ 和 $A[r] = \{a \in A \mid ra = 0\}$ 都是 $A$ 的子模.  
    (ii) $R/(p)$ 是域，$A[p]$ 是 $R/(p)$ 上的向量空间.  
    (iii) 对于每个正整数 $n$，均有 $R$-模同构 

    \[
        (R/(p^n))[p] \cong R/(p), \quad p^m(R/(p^n)) \cong R/(p^{n-m}), \quad 0 \leqslant m \leqslant n.
    \]

    (iv) 若 $A \cong \sum_{i \in I} A_i$，则 $rA \cong \sum_{i \in I} rA_i$，$A[r] \cong \sum_{i \in I} A_i[r]$.  
    (v) 如果 $f: A \to B$ 是 $R$-模同构，则 $f$ 诱导同构 $A_t \cong B_t$，$A(p) \cong B(p)$.   

!!! success "引理"
    设 $R$ 是主理想整环，如果 $r \in R$ 可以分解成 $r = p_1^{n_1}\cdots p_k^{n_k}$，其中 $p_i$ 是 $R$ 中互异的素元，$n_i$ 是正整数，则 $R/(r) \cong R/(p_1^{n_1}) \oplus \cdots \oplus R/(p_k^{n_k})$. 于是，每个 $r$ 阶循环子模均是阶数分别为 $p_1^{n_1}, \ldots, p_k^{n_k}$ 的 $k$ 个循环子模的直和.  

然后来到了主定理。

!!! note "$\star$定理"
    设 $A$ 是主理想整环 $R$ 上的有限生成模.  
    (i) $A$ 是一个秩有限的自由子模 $F$ 和有限个循环扭模的直和. 进而，如果存在循环扭模直和成分，则可以使它们的阶分别为 $r_1, \ldots, r_t$，其中 $r_1, \ldots, r_t$ 是 $R$ 中(不必两两互异)的非零非单位元素，并且 $r_1 \mid r_2 \mid \cdots \mid r_t$. $F$ 的秩和理想 $(r_1) \cdots (r_t)$ 由 $A$ 唯一确定.  
    (ii) $A$ 是一个秩有限的自由子模 $E$ 和有限个循环扭模的直和. 进而，如果存在循环扭模直和成分，则可以使它们的阶分别为 $p_1^{s_1}, \ldots, p_t^{s_t}$，其中 $p_1, \ldots, p_t$ 是 $R$ 中(不必两两互异)的素元，而 $s_1, \ldots, s_t$ 是(不必两两互异的)正整数. $E$ 的秩和理想 $(p_1^{s_1}) \cdots (p_t^{s_t})$ 由 $A$ 唯一确定.

$r_1, \ldots, r_t$ 称为 $A$ 的**不变因子**(invariant factors)，$p_1^{s_1}, \ldots, p_t^{s_t}$ 称为 $A$ 的**初等因子**(elementary factors)。

!!! success "推论"
    主理想整环上的两个有限生成模 $A$ 和 $B$ 是同构的当且仅当 $A/A_t$ 和 $B/B_t$ 有相同的秩，且 $A$ 和 $B$ 有相同的不变因子(或者初等因子).