# 阿贝尔群

此讲的研究对象加强为了阿贝尔群，所以我们可以讨论一些普通的群做不到的事情，同时本讲的二元运算也使用 $+$ 记号。

类似于线性空间，在阿贝尔群上我们也可以做所谓的**线性组合**(Linear Combination)，以及找到所谓的**基**(basis)。  

!!! info "定义"
    线性组合：$n_1x_1 + n_2x_2 + \cdots + n_kx_k, n_i \in \mathbf{Z}, x_i \in X$. 事实上，在加法运算下由集合 $X$ 生成的群 $\langle X \rangle$ 就包含了所有的线性组合.  
    基：一个阿贝尔群 $F$ 的基是满足以下条件的子集 $X$：  
        (i) $F = \langle X \rangle$;  
        (ii) 对互异的 $x_1, x_2, \ldots, x_k \in X$ 以及 $n_i \in \mathbf{Z}$，有  
        
    $$
        n_1x_1 + n_2x_2 + \cdots + n_kx_k = 0 \Rightarrow n_i = 0, \forall i.
    $$

基是非常有用的，这点我们在线性代数中就已经意识到了。而注意到循环群 $\langle x \rangle = \{nx \mid n \in \mathbf{Z}\}$，所以我们可以进一步探索基存在的条件。

!!! note "定理"
    对阿贝尔群 $F$ 以下条件等价.  
    (i) $F$ 有一组非空的基；  
    (ii) $F$ 是一族无限循环子群的直和；  
    (iii) $F$ 同构于若干加法群 $Z$ 的直和；  
    (iv) 存在非空集合 $X$ 和函数 $\iota: X \rightarrow F$，满足以下性质：给定一阿贝尔群 $G$ 和一函数 $f: X \rightarrow G$，存在唯一的群同态 $\bar{f}: F \rightarrow G$ 使得 $\bar{f}\iota = f$. 换言之，$F$ 在阿贝尔群的范畴内是**自由**的.

满足以上条件的阿贝尔群被称为（在集合 $X$ 上的）**自由阿贝尔群**(free abelian group). 由定义可知平凡的阿贝尔群 $0$ 是在 $\varnothing$ 上的自由阿贝尔群。

同理，也有些与线性空间的基类似的结论。

!!! note "定理"
    (i) 同一阿贝尔群 $F$ 的任意两个基有相同的基数. 即任一 $F$ 的基 $X$ 的基数是 $F$ 的一个不变量，$\lvert X \rvert$ 被称为 $F$ 的**秩**(rank);  
    (ii) 设 $F_1$ 是集合 $X_1$ 上的自由阿贝尔群，设 $F_2$ 是集合 $X_2$ 上的自由阿贝尔群. 那么 $F_1 \cong F_2$ 等价于二者拥有相同的秩，即 $\lvert X_1 \rvert = \lvert X_2 \rvert$;  
    (iii) 每一个阿贝尔群 $G$ 都是一个秩为 $\lvert X \rvert$ 的自由阿贝尔群的同态像，其中 $X$ 是 $G$ 的生成元的集合. 

下面是一些基的生成方法。

!!! note "定理"
    (i) 若 $\{x_1, \ldots, x_n\}$ 是一自由阿贝尔群 $F$ 的基，$a \in \mathbf{Z}$，那么对于 $\forall i \neq j$，$\{x_1, \ldots, x_{j-1}, x_j + ax_i, x_{j+1}, \ldots, x_n\}$ 也是 $F$ 的一组基.  
    (ii) 如果 $F$ 是一个自由阿贝尔群，其秩为一有限数 $n$，$G$ 是 $F$ 的一个非零子群，那么存在 $F$ 的一组基 $\{x_1, x_2, \ldots, x_n\}$，整数 $r, 1 \leqslant r \leqslant n$，以及正整数 $d_1, d_2, \ldots, d_r$ 使得 $d_1 \mid d_2 \mid \cdots \mid d_r$ 并且 $G$ 是以 $d_1x_1, d_2x_2, \ldots, d_rx_r$ 为基的自由阿贝尔群.

(ii) 其实揭示了一个相当重要的结论，即自由的结构的子结构依然是自由的。

??? note "证明"
    (ii) 若 $n = 1$，则 $F = \langle x_1 \rangle \cong \mathrm{Z}$，且 $G = \langle d_1x_1 \rangle \cong \mathrm{Z}, d_1 \in N^*$. 然后采用归纳法.  
    假设结论对所有秩小于 $n$ 的自由阿贝尔群均成立，则设集合 $S$ 表示满足以下条件的整数 $s$：存在 $F$ 的一组基 $\{y_1, \ldots, y_n\}$，且 $sy_1 + k_2y_2 + \cdots + k_ny_n \in G, k_i \in \mathrm{Z}$. 注意到 $\{y_2, y_1, y_3, \ldots, y_n\}$ 也是 $F$ 的一组基，所以 $k_2 \in S$. 同理对 $j = 3, 4, \ldots n, k_j \in S$. 因为 $G \neq 0$，所以 $S \neq \varnothing$，从而 $S$ 中存在最小正整数 $d_1$，并且对 $F$ 的某一组基 $\{y_1, y_2, \ldots, y_n\}$，存在 $v \in G$，使得 $v = d_1y_1 + k_2y_2 + \cdots + k_ny_n$. 利用带余除法，可以得到，对于 $i = 2, 3, \ldots, n$，均有 $k_i = d_1q_i + r_i$，所以 $v = d_1(y_1 + q_2y_2 + \cdots + q_ny_n) + r_2y_2 + r_3y_3 + \cdots + r_ny_n$，令 $x = y_1 + q_2y_2 + \cdots + q_ny_n$，由 (i) 可知 $W = \{x, y_2, \ldots, y_n\}$ 是 $F$ 的一组基. 而 $v \in G$，$r_i < d_1$，且将 $W$ 中的元素以任意顺序重新排列均是 $F$ 的基，故 $r_i \in S, i = 2, 3 \ldots, n$. 考虑到 $d_1$ 是 $S$ 中的最小正整数，有 $r_i = 0, i = 2, 3, \ldots, n$. 所以 $v = d_1x_1 \in G$.  
    设 $H = \langle y_2, \ldots, y_n \rangle$，则 $H$ 是秩为 $n-1$ 的自由阿贝尔群，且 $F = \langle x_1 \rangle \oplus H$，我们进一步证明 $G = \langle v \rangle \oplus (G \cap H)$. 因为 $\{x_1, y_2, \ldots, y_n\}$ 是 $F$ 的一组基，故 $\langle v \rangle \cap (G \cap H) = 0$. 设 $u = t_1x_1 + t_2y_2 + \cdots + t_ny_n \in G, t_i \in \mathrm{Z}$，带余除法有 $t_1 = d_1q_1 + r_1$，所以 $u - q_1v = r_1x + t_2y_2 + \cdots + t_ny_n \in G$. 而 $d_1$ 是 $S$ 中的最小正整数，有 $r_1 = 0$. 所以 $t_2y_2 + \cdots + t_ny_n \in G \cap H$ 且 $u = q_1v + (t_2y_2 + \cdots + t_ny_n)$，$G = \langle v \rangle + (G \cap H)$. 也就有 $G = \langle v \rangle \oplus (G \cap H)$.  
    若 $G \cap H = 0$，则 $G = \langle d_1x_1 \rangle$，从而定理成立. 否则有 $C \cap H \neq 0$，由归纳假设，存在 $H$ 的一组基 $\{x_2, x_3, \ldots, x_n\}$ 和正整数 $r, d_2, \ldots, d_r$，使得 $d_2 \mid d_3 \mid \cdots \mid d_r$，且 $G \cap H$ 是以 $\{d_2x_2, \ldots, d_nx_n\}$ 为基的自由阿贝尔群. 由于 $F = \langle x_1 \rangle \oplus H$ 且 $G = \langle v \rangle \oplus (G \cap H)$，完成归纳仅需要再证明 $d_1 \mid d_2$. 由带余除法，$d_2 = qd_1 + r_0$. 由 (i) 有 $\{x_2, x_1 + qx_2, x_3, \ldots, x_n\}$ 是 $F$ 的一组基，而 $r_0x_2 + d_1(x_1+qx_2) = d_1x_1 + d_2x_2 \in G$，所以 $r_0 \in S$，而 $d_1$ 是 $S$ 中的最小正整数，所以有 $r_0 = 0$，即 $d_1 \mid d_2$.
      
!!! success "推论"
    如果 $G$ 是由 $n$ 个元素有限生成的阿贝尔群，那么 $G$ 的每个子群 $H$ 都是可由 $m$ 个元素生成，其中 $m \leqslant n$.

我们接下来开始研究有限生成的阿贝尔群。

!!! note "定理"
    (i) 任一有限生成的阿贝尔群 $G$ 都是（同构于）一些循环群的有限直和，并且这些循环群中如果有一些是有限的，总可以使它们的阶为 $m_1, \ldots, m_t$，满足 $m_1 > 1$ 且 $m_1 \mid m_2 \mid \cdots \mid m_t$;  
    (ii) 任一有限生成阿贝尔群 $G$ 都是（同构于）循环群的有限直和，这些循环群要么是无限的，要么阶是一个素数. 

!!! success "引理"
    若 $m$ 是一正整数，并且可被素分解为以下形式：$m = p_1^{n_1}p_2^{n_2}\cdots p_t^{n_t}, p_1, p_2, \ldots, p_t$ 是互异素数，且 $n_i > 0$，则有 $Z_m \cong Z_{p_1^{n_1}} \oplus Z_{p_2^{n_2}} \oplus \cdots \oplus Z_{p_t^{n_t}}$

!!! success "推论"
    若 $G$ 是一有限生成的阿贝尔群，阶为 $n$ ，那么对于任意 $m \mid n$，$G$ 都有阶为 $m$ 的子群. 

!!! success "引理"
    设 $G$ 是一阿贝尔群，$m$ 是一整数且 $p$ 是一素数，那么以下集合均为 $G$ 的子群：  
    (i) $mG = \{mu \mid u \in G\}$;  
    (ii) $G[m] = \{u \in G \mid mu = 0\}$;  
    (iii) $G(p) = \{u \in G \mid \lvert u \rvert = p^n, \exists n \geqslant 0\}$;  
    (iv) $G_t = \{u \in G \mid \lvert u \rvert \in \mathbf{Z}\}$.  
    特别地，存在着以下的一些同构： 
    (v) $Z_{p^n}[p] \cong Z_p(n \leqslant 1), p^mZ_{p_n} \cong Z_{p^{n-m}}(m < n)$.  
    设 $H$ 和 $G_i(i \in I)$ 都是阿贝尔群，则：  
    (vi) 若 $g: G \rightarrow \sum_{i \in I} G_i$ 是一同构，则 $g$ 在 $mG$ 和 $G[m]$ 上的限制分别是同构 $mG \cong \sum_{i \in I} mG_i, G[m] \cong \sum_{i \in I} G_i[m]$.  
    (vii) 若 $f: G \rightarrow H$ 是同构，则 $f$ 在 $G_t$ 和 $G_p$ 上的限制分别是同构 $G_t \cong H_t, G(p) \cong H(p)$.

若 $G$ 是阿贝尔群，则 $G_t$ 被称为 $G$ 的**扭子群**(torsion subgroup)，若 $G_t = G$，则群 $G$ 叫做**扭群**(torsion group)，若 $G_t = 0$，则称 $G$ 是**无扭的**(torsion-free).

下面便是本节最重要的定理。

!!! note "定理"
    （有限生成阿贝尔群结构定理）设 $G$ 是有限生成阿贝尔群，则  
    (i) 存在唯一的非负整数 $s$，使得将 $G$ 任意分解为循环群直和时，其无限循环群直和部分的个数恰好为是 $s$.  
    (ii) 要么 $G$ 是自由阿贝尔群，要么存在唯一的一组（不必互异）正整数 $m_1, \ldots, m_t$，使得 $m_1 > 1$，$m_1 \mid m_2 \mid \cdots \mid m_t$，并且 

    $$
        G \cong Z_{m_1} \oplus Z_{m_2} \oplus \cdots \oplus Z_{m_t} \oplus F,
    $$

    其中 $F$ 是自由阿贝尔群.  
    (iii) 要么 $G$ 是自由阿贝尔群，要么存在一组正整数 $p_1^{s_1}, \ldots, p_k^{s^k}$，其不计次序意义下是唯一的，使得 $p_1, \ldots, p_k$ 是素数（不必互异），$s_1, \ldots, s_k$ 是正整数（不必互异），并且

    $$
        G \cong Z_{{p_1}^{s_1}} \oplus Z_{{p_2}^{s_2}} \oplus \cdots \oplus Z_{{p_k}^{s_k}} \oplus F,
    $$

    其中 $F$ 是自由阿贝尔群.

若 $G$ 是有限生成阿贝尔群，则 (ii) 中唯一决定的整数 $m_1, \ldots, m_t$ 被称为 $G$ 的**不变因子**(invariant factors)，(iii) 中唯一决定的素数幂被称为 $G$ 的**初等因子**(elementary divisors)。

!!! example "示例"
    (i) 全体 $1500$ 阶的有限阿贝尔群可由下述方法完全决定（不计同构）. 有限群 $G$ 的初等因子之积为 $\lvert G \rvert$，而 $1500 = 2^2 \cdot 3 \cdot 5^3$，所以初等因子只有以下六种可能：$\{2, 2, 3, 5^3\},$ $\{2, 2, 3, 5, 5^2\},$ $\{2, 2, 3, 5, 5, 5\},$ $\{2^2, 3, 5^3\},$ $\{2^2, 3, 5, 5^2\},$ $\{2^2, 3, 5, 5, 5\}.$ 这六种初等因子每组决定了一个 $1500$ 阶的阿贝尔群.  
    (ii) 如果 $G = Z_5 \oplus Z_{15} \oplus Z_{25} \oplus Z_{36} \oplus Z_{54}$. 则 $G \cong Z_5 \oplus (Z_{3} \oplus Z_{5}) \oplus Z_{25} \oplus (Z_{4} \oplus Z_{9}) \oplus (Z_{2} \oplus Z_{27})$. 从而 $G$ 的初等因子是 $2, 2^2, 3, 3^2, 3^3, 5, 5, 5^2$，其可排列为

    $$
        \begin{matrix} 2^0 & 3^1 & 5^1 \\ 2^1 & 3^2 & 5^1 \\ 2^2 & 3^3 & 5^2 \end{matrix}
    $$

    所以 $G$ 的不变因子是 $2^0 \cdot 3^1 \cdot 5^1 = 15, 2^1 \cdot 3^2 \cdot 5^1 = 90, 2^2 \cdot 3^3 \cdot 5^2 = 2700$，因此 $G \cong Z_{15} \oplus Z_{90} \oplus Z_{2700}$.