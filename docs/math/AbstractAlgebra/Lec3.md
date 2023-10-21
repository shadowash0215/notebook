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
    (iv) 存在非空集合 $X$ 和函数 $l: X \rightarrow F$，满足以下性质：给定一阿贝尔群 $G$ 和一函数 $f: X \rightarrow G$，存在唯一的群同态 $\overline{f}: F \rightarrow G$ 使得 $\overline{f}l = f$. 换言之，$F$ 在阿贝尔群的范畴内是**自由**的.

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

!!! success "推论"
    如果 $G$ 是由 $n$ 个元素有限生成的阿贝尔群，那么 $G$ 的每个子群 $H$ 都是由 $m, m \leqslant n$ 个元素生成的.

我们接下来开始研究有限生成的阿贝尔群。

!!! note "定理"
    (i) 任一有限生成的阿贝尔群 $G$ 都是（同构于）一些循环群的有限直和，由高到低记循环群指数为 $m_1, \ldots, m_t$，满足 $m_1 > 1$ 且 $m_1 \mid m_2 \mid \cdots \mid m_t$;  
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