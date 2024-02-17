# 2 同态与同构 陪集 正规子群与商群

群与群之间的关系除了子群维系之外还可以通过映射，不过我们天然的希望这个映射可以不破坏群的结构，所以我们更愿意研究称为**同态**(Homomorphism)的映射，其定义如下。

!!! info "定义"
    设 $G$ 和 $H$ 是两个半群，如果映射 $f: G \rightarrow H$ 满足

    $$
    f(ab) = f(a)f(b), \forall a, b \in G. 
    $$

    则称映射 $f$ 是一个从 $G$ 到 $H$ 的同态.

    如果 $f$ 是单射，则称为**单态**(Monomorphism);如果 $f$ 是满射，则称为**满态**(Epimorphism)；如果 $f$ 是双射，则称为**同构**(Isomorphism)，相应的 $G$ 和 $H$ 被称作同构的(Isomorphic)，记作 $G \cong H$. 

    同态 $f: G \rightarrow G$ 被称作 $G$ 的一个**自同态**(Endomorphism)，同构 $f: G \rightarrow G$ 被称作 $G$ 的一个**自同构**(Automorphism).

同态也是一个映射，我们定义其与映射相关的名词。

!!! info "定义"
    设群同态 $f: G \rightarrow H$. $f$ 的**核**(Kernel)是集合 $\{a \in G \mid f(a) = e \in H\}$，记作 $\operatorname{\mathrm{Ker}} f$；设集合 $A$ 是 $G$ 的一个子集，则 $A$ 的**像**(Image) 是集合 $f(A)  = \{b \in H \mid b = f(a), a \in A \}$，$f(G)$ 则是映射 $f$ 的像，记作 $\operatorname{\mathrm{Im}} f$；设集合 $B$ 是 $H$ 的一个子集，则 $B$ 的**原像**(Inverse Image) 是集合 $f^{-1}(B) = \{a \in G \mid f(a) \in B\}$.

以及与映射相应的单满双判定。

!!! success "引理"
    设群同态 $f: G \rightarrow H$.
    
    1. $f$ 是一个单态等价于 $\operatorname{\mathrm{Ker}} f = \{e\}$. 

    2. $f$ 是一个同构等价于存在同态 $g : H \rightarrow G$，使得 $fg = 1_H$ 且 $gf = 1_G$，这样的同态 $g$ 记为 $f^{-1}$.

我们这里便可以补充一下关于循环群的定理. 

!!! success "引理"
    1. 所有无限循环群都同构于整数加法群 $Z$，所有阶数为 $m$ 的有限循环群均同构于模 $m$ 意义下的整数加法群 $Z_m$.

    2. 所有循环群在群同态下的像是循环群，所有循环群的子群也是循环群. 若 $H$ 是循环群 $G = \langle a \rangle$ 的一个非平凡子群，且 $m$ 是满足 $a^m \in H$ 的最小正整数，则 $H = \langle m \rangle$.

为了进一步研究群的结构，我们引进了新的同余关系。

!!! info "定义"
    设 $H$ 是群 $G$ 的一个子群，$a, b \in G$. 若 $ab^{-1} \in H$，则称 $a$ 在模 $H$ (module $H$)意义下**右同余**(Right Congruent)于 $b$，记作 $a \equiv_r b \pmod H$；而若 $a^{-1}b \in H$，则称 $a$ 在模 $H$ 意义下**左同余**(Left Congruent)于 $b$，记作 $a \equiv_l b \pmod H$.

以下便是一些关于左/右同余关系的刻画。

!!! note "定理"
    设 $H$ 是群 $G$ 的一个子群.

    1. 模 $H$ 意义下的左/右同余关系是 $G$ 上的等价关系. 

    2. 设 $a \in G$，则关于元素 $a$ 在模 $H$ 意义下的右同余等价类是集合 $Ha = \{ha | h \in H\}$，相应的左同余等价类是 $aH = \{ah | h \in H\}$. 

    3. $\forall a \in G, \lvert Ha \rvert = \lvert H \rvert = \lvert aH \rvert$. 

??? note "证明"
    仅证明 2.

    易知关于元素 $a$ 在模 $H$ 意义下的右同余等价类是集合

    $$
    \{x \in G | x \equiv_r a\} = \{x \in G | xa^{-1} = h \in H\} = \{x \in G | x = ha, h \in H\} = \{ha | h \in H\} = Ha. 
    $$ 
    
    左同余同理. 

集合 $Ha$ 被称作 $G$ 上关于 $H$ 的**右陪集**(Right Coset)，集合 $aH$ 被称作 $G$ 上关于 $H$ 的**左陪集**(Left Coset). 虽然被叫做陪集，但它们实际上就是等价类，自然有一些与等价类相应的性质。

!!! success "引理"
    设 $H$ 是群 $G$ 的一个子群.  
    1. $G$ 是所有关于 $H$ 的左/右陪集的并.  
    2. 关于 $H$ 的两个左/右陪集要么相等，要么不交.  
    3. $\forall a, b \in G, Ha = Hb \Leftrightarrow  ab^{-1} \in H, aH = bH \Leftrightarrow a^{-1}b \in H$.  
    4. 设集合 $\mathfrak{R}$ 中的元素是所有关于 $H$ 的互异的右陪集，集合 $\mathfrak{L}$ 中的元素是所有关于 $H$ 的互异的左陪集，那么有 $\lvert \mathfrak{R} \rvert = \lvert \mathfrak{L} \rvert$.

第 4 条定理表明关于同一子群的互异左右陪集数量是相等的，也就确保了下面这个定义的合理性。

!!! info "定义"
    设 $H$ 是群 $G$ 的一个子群. 定义 $H$ 在 $G$ 中的**指标**(index) 为上一引理第四条中的集合$\mathfrak{R}$ 或 $\mathfrak{L}$ 的基数，即互异左/右陪集的数量，记作 $[G:H]$.

指标的引入给群的刻画带来了新的方法，以下是一些相关的定理。

!!! note "定理"
    1. 设 $K, H, G$ 均为群且满足 $K < H < G$，那么 $[G:K] = [G:H][H:K]$. 其中任意两个是有限的话，第三个也是有限的. 

    2. (Lagrange) 设 $H$ 是群 $G$ 的一个子群，则 $\lvert G \rvert = [G:H]\lvert H \rvert$. 由此有，若 $G$ 是有限群，$a \in G$，则 $a$ 的阶 $\lvert a \rvert$ 整除群 $G$ 的阶 $\lvert G \rvert$. 

    3. 设 $H$ 和 $K$ 均是群 $G$ 的有限子群，定义 $HK = \{hk | h \in H, k \in K\}$. 易知 $HK$ 和 $G$ 上的乘法构成群，且有 $\lvert HK \rvert = \lvert H \rvert \lvert K \rvert / \lvert H \cap K \rvert$. 

    4. 设 $H$ 和 $K$ 均是群 $G$ 的子群，则 $[H:H \cap K] \leqslant [G:K]$. 若 $[G:K]$ 是有限的，那么等号成立当且仅当 $G = KH$.

    5. $HK = KH$ 等价于 $HK$ 是 $G$ 的子群.

    6. 设 $H$ 和 $K$ 均是群 $G$ 的子群，且指标有限，则 $[G:H \cap K]$ 是有限的，并且 $[G:H \cap K] \leqslant [G:H][G:K]$，等号成立当且仅当 $G = HK$.

??? note "证明"
    1. 对 $G$ 作陪集分解，$G = \bigcup_{i \in I} Ha_i, a_i \in G$，所以 $\lvert I \rvert = [G:H]$ 且 $Ha_i$ 不交. 同理对 $H$ 作陪集分解，$H = \bigcup_{j \in J} Kb_j, b_j \in J$，所以 $J = [H:K]$ 且 $Kb_j$ 不交. 从而 $G = \bigcup_{i \in I} Ha_i = \bigcup_{i \in I} \left(\bigcup_{j \in J} Kb_j\right)a_i = \bigcup_{(i, j) \in I \times J} Kb_ja_i$.   
    下面只需要证明 $Kb_ja_i$ 不交，这样就会有 $[G:K] = \lvert I \times J \rvert = \lvert I \rvert \lvert J \rvert = [G:H][H:K]$. 若 $Kb_ja_i = Kb_ra_t$，则 $b_ja_i = kb_ra_t, k \in K$. 因为 $b_j, b_r, k \in H$，从而有 $Hb_ja_i = Hkb_ra_t \Rightarrow Ha_i = Ha_t$，从而 $i = t, b_ja_i = kb_ra_t \Rightarrow b_j = kb_r$，进而 $Kb_j = Kkb_r \Rightarrow Kb_j = Kb_r$，所以 $j = r$，也就是说 $Kb_ja_i$ 不交，得证. 

    2. 取 $K = \langle e \rangle$，有 $\lvert G \rvert = [G:H] \lvert H \rvert$. 再取 $H = \langle a \rangle$ 即证. 

    3. 设 $C = H \cap K$，$C$ 在 $K$ 中的指标 $n = \lvert K \rvert / \lvert H \cap K \rvert$，且有陪集分解 $K = \cup_{i = 1}^{n} Ck_i, k_i \in K$. 而 $HC = H$，所以 $HK = H(\cup_{i = 1}^{n} Ck_i) = \cup_{i = 1}^{n} HCk_i = \cup_{i = 1}^{n} Hk_i, \lvert HK \rvert = \lvert H \rvert * n = \lvert H \rvert \lvert K \rvert / \lvert H \cap K \rvert$. 

    4. 设 $A$ 是 $H \cap K$ 在 $H$ 中的所有互异右陪集构成的集合，$B$ 是 $K$ 在 $G$ 中所有互异右陪集构成的集合. 定义映射 $\varphi: A \rightarrow B$，对应法则为 $(H \cap K)h \mapsto K(i(h)), h \in H, i: H \rightarrow G, i(h) \mapsto h$. 易见其是良定义的，因为若 $(H \cap K)h' = (H \cap K)h$，则有 $h'h^{-1} \in (H \cap K) \subset K$，进而 $Kh' = K(i(h')) = K(i(h)) = Kh$. 而若 $K(i(h')) = Kh' = Kh = K(i(h))$，则有 $h'h^{-1} \in K$，又 $h, h' \in H$ 必有 $h'h^{-1} \in H$，所以 $h'h^{-1} \in (H \cap K)$，即 $(H \cap K)h' = (H \cap K)h$，$\varphi$ 是单的，所以 $[H:H \cap K] = \lvert A \rvert \leqslant \lvert B \rvert = [G:K]$. 若 $[G:K]$ 是有限的，则 $[H:H \cap K] = [G:K]$等价于 $\varphi$ 是满的. 即 $\forall Kg, g \in G, \exists (H \cap K)h, h \in H, s.t. \varphi((H \cap K)h) = Kg$，为保证满射，必有 $Kg= Kh, h \in H$，从而 $\forall g \in G, g = Kh, h \in H$，即 $G = KH$. 
 
    5. ($\Leftarrow$) 因为 $HK$ 是 $G$ 的一个子群，所以 $\forall x \in HK, \exists h \in H, k \in K, s.t. x = hk$. 而 $x^{-1} \in HK$，且 $x^{-1} = (hk)^{-1} = k^{-1}h^{-1} \in KH$，所以 $HK \subseteq KH$. 而我们也知道 $k \in K, h \in H$ 有 $k \in HK, h \in HK$，而 $HK$ 是 $G$ 的子群，所以 $kh \in HK$，从而有 $KH \subseteq HK$，进而 $HK = KH$.   
    ($\Rightarrow$) 根据子群的定义证明.  
    i. $e \in H, e \in K \Rightarrow e \in HK.$  
    ii. $\forall x \in HK, x = hk, h \in H, k \in K$，$x^{-1} = (hk)^{-1} = k^{-1}h^{-1} \in KH = HK$.  
    iii. 设 $x, y \in HK, \exists h_x, h_y \in H, k_x, k_y \in K, s.t. x = h_xk_x, y = h_yk_y$，所以 $xy = h_xk_xh_yk_y$. 而 $HK = KH$，所以 $\exists h \in H, k \in K, s.t. k_xh_y = hk$，所以 $xy = h_xhkk_y \in HK$.  
    综上 $HK$ 是 $G$ 的一个子群. 

    6. 由 4 有 $[H:H \cap K] \leqslant [G:K]$，两侧同乘 $[G:H]$ 有 $[G:H][H:H \cap K] \leqslant [G:H][G:K]$，而 $[G:H][H:H \cap K] = (\lvert G \rvert / \lvert H \rvert)(\lvert H \rvert / (H \cap K)) = \lvert G \rvert / \lvert (H \cap K) \rvert = [G:H \cap K]$，所以 $[G:H \cap K] \leqslant [G:H][G:K]$，$[G:H], [G:K]$ 均有限，所以 $[G:H \cap K]$ 有限. 等号成立条件与 4 相同，即  $G = KH$，而由 5 可知，$G = KH = HK$. 

从陪集继续出发，我们能得到一些性质更好的子群。

!!! note "定理"
    设 $N$ 是 $G$ 的一个子群，那么以下条件等价：  
    1. 左同余模 $N$ 关系与右同余模 $N$ 关系是一致的.  
    2. $N$ 的每个左陪集都是 $N$ 的一个右陪集.  
    3. $\forall a \in G, aN = Na$.  
    4. $\forall a \in G$，定义 $aNa^{-1} = \{ana^{-1} | n \in N\}$，则 $aNa^{-1} \subset N$.  
    5. $\forall a \in G, aNa^{-1} = N$.  

??? note "证明"
    仅证明一部分等价性. 

    (2 $\Rightarrow$ 3) 对部分 $b \in G$ 有 $aN = Nb$，那么 $a \in aN = Nb$，且 $a \in Na$，所以 $a \in Na \cap Nb$，而陪集要么不交，要么相等，所以 $aN = Nb = Na$. 

    (4 $\Rightarrow$ 5) $\forall a \in G, aNa^{-1} \subset N$，而 $a^{-1} \in G$，同样有 $a^{-1}N(a^{-1})^{-1}  = a^{-1}Na \subset N$. 所以 $\forall n \in N, n = a(a^{-1}na)a^{-1} \in aNa^{-1}$，所以 $aNa^{-1} = N$. 

满足上述定理的子群 $N$ 被称作 $G$ 的一个**正规子群**(Normal Subgroup)，记作 $N \triangleleft G$. 注意这种性质不具有传递性，即 $N \triangleleft M, M \triangleleft G \nRightarrow N \triangleleft G$. 但是有这样的一个定理。

!!! success "引理"
    设 $N$ 是 $G$ 的一个正规子群，则 $N$ 是 $G$ 的任一包含 $N$ 的子群的正规子群. 即 
    
    $$
        N \triangleleft G, \forall M < G, N < M \Rightarrow N \triangleleft M
    $$

正规子群的优秀之处还在于其与其他子群结合时仍然保有良好的性质。

!!! note "定理"
    设 $K$ 和 $N$ 均是群 $G$ 的子群且 $N$ 是 $G$ 的正规子群，则  
    1. $N \cap K$ 是 $K$ 的正规子群.  
    2. $N$ 是 $N \vee K$ 的正规子群.  
    3. $NK = N \vee K = KN$.  
    4. 若 $K$ 也是 $N$ 的一个正规子群且 $N \cap K = \langle e \rangle$，那么 $\forall k \in K, n \in N, nk = kn$.

??? note "证明"
    1. 设 $n \in N \cap K, a \in K$. $N \triangleleft G \Rightarrow ana^{-1} \in N, K < G \Rightarrow ana^{-1} \in K$，所以 $a(N \cap K)a^{-1} \subset N \cap K \Rightarrow N \cap K \triangleleft K$. 

    2. 显然，因为 $N < N \vee K$.

    3. 显然 $NK \subset N \vee K$. $\forall x \in N \vee K$ 都有如下的形式: 
    
    $$
        n_1k_1n_2k_2 \cdots n_rk_r, n_i \in N, k_i \in K. 
    $$

    因为 $N \triangleleft G$，所以 $n_ik_j = k_jn_i', n_i' \in N$. 从而 $x$ 可被写作如下的形式 $x = n(k_1k_2 \cdots k_r)$. 所以 $N \vee K \subset NK$，有 $NK = N \vee K$. 同理 $N \vee K = KN$.

    4.  设 $k \in K, n \in N$. 因为 $K \triangleleft G$，所以 $nkn^{-1} \in K$；因为 $N \triangleleft G$，所以 $kn^{-1}k^{-1} \in N$. 进而 $(nkn^{-1})k^{-1} = n(kn^{-1}k^{-1}) \in N \cap K = \langle e \rangle$，从而 $nk = kn$.

由此出发，我们可以生成一个新的重要的群。

!!! info "定义"
    设 $N$ 是群 $G$ 的一个正规子群，$G/N$ 是 $N$ 的所有陪集构成的集合，则 $G/N$ 与如下的二元运算构成一群，阶为 $[G:N]$ ：$(aN)(bN) = abN$. 称 $G/N$ 为 $N$ 关于 $G$ 的**商群**(Quotient Group)

??? note "证明"
    我们需要证明此定义是良定义的，即若 $a_1 \equiv a \pmod N, b_1 \equiv b \pmod N$，有 $a_1b_1 \equiv ab \pmod N$. 由条件有 $a_1a^{-1} = n_1 \in N, b_1b^{-1} = n_2 \in N$. 因此 $(a_1b_1)(ab)^{-1} = a_1b_1b^{-1}a^{-1} = a_1n_2a^{-1}$. 因为 $N$ 是正规的，所以 $a_1N = Na_1$，进而 $\exists n_3 \in N, a_1n_2 = n_3a_1$. 所以 $(a_1b_1)(ab)^{-1} = (a_1n_2)a^{-1} = n_3a_1a^{-1} = n_3n_1 \in N$，也就有 $a_1b_1 \equiv ab \pmod N$.

可以发现，模 $n$ 剩余群 $\mathbf{Z}_n = \mathbf{Z} / \langle n \rangle$.

下面我们给出群同态与正规子群以及商群的联系。

!!! note "定理"
    若 $f: G \rightarrow H$ 是一个群同态，那么 $f$ 的核 $\operatorname{\mathrm{Ker}} f$ 是 $G$ 的一个正规子群.  
    而若 $N$ 是 $G$ 的一个正规子群，那么映射 $\pi : G \rightarrow G/N, \pi(a) = aN$ 是一个核为 $N$ 的满同态，被称为**典范满射**(Canonical Epimorphism). 每个正规子群都可以诱导一个典范满射.

??? note "证明"
    设 $x \in \operatorname{\mathrm{Ker}} f, a \in G$，则 

    $$
        f(axa^{-1}) = f(a)f(x)(f(a))^{-1} = f(a)e(f(a))^{-1} = f(a)(f(a))^{-1} = e.
    $$ 

    且 $axa^{-1} \in \operatorname{\mathrm{Ker}} f$. 因此 $a(\operatorname{\mathrm{Ker}} f)a^{-1} \subset Ker f$，进而 $\operatorname{\mathrm{Ker}} f \triangleleft G$. 映射 $\pi : G \rightarrow G/N$ 显然是满的，且 $\pi(ab) = abN = aNbN = \pi(a)\pi(b)$，所以 $\pi$ 是一个满同态. $\operatorname{\mathrm{Ker}} \pi = \{a \in G \mid \pi(a) = eN = N\} = \{a \in G \mid aN = N\} = \{a \in G \mid a \in N\} = N$.

由此可以得到一个关键的引理。

!!! success "引理"
    若 $f: G \rightarrow H$ 是一个群同态，$N$ 是 $G$ 的一个正规子群，且是 $f$ 的核的子集，那么存在唯一的一个群同态 $\bar{f} : G/N \rightarrow H$，满足 $\bar{f}(aN) = f(a), \forall a \in G$，且 $\operatorname{\mathrm{Im}} f = \operatorname{\mathrm{Im}} \bar{f}, \operatorname{\mathrm{Ker}} \bar{f} = (\operatorname{\mathrm{Ker}} f)/N$. $\bar{f}$ 是一个群同构等价于 $f$ 是一个满同态且 $N = \operatorname{\mathrm{Ker}} f$.(*)

本质上就是存在唯一的同态 $\bar{f} : G/N \rightarrow H$ 使得下图是交换的。

\tikzcd
    G \arrow[r, "f"] \arrow[d, "\pi"swap] & H \\
    G/N \arrow[ru, "\bar{f}"swap]

??? note "证明"
    首先证明 $\bar{f}$ 是良定义的.  
    设 $b \in aN$，则 $b = an, n \in N$. 注意到 $N < \operatorname{\mathrm{Ker}} f$，有 $f(b) = f(an) = f(a)f(n) = f(a)e =f(a)$. 所以对于 $f$ 对于陪集 $aN$ 中的每个元素的作用效果都是等同的，从而 $\bar{f}: G/N \rightarrow H, \bar{f}(aN) = f(a)$ 是良定义的. 而 $\bar{f}(abN) = f(ab) = f(a)f(b) = \bar{f}(aN)\bar{f}(bN)$，所以 $\bar{f}$ 是一个群同态. 显然 $\operatorname{\mathrm{Im}} \bar{f} = \operatorname{\mathrm{Im}} f$.对于 $\operatorname{\mathrm{Ker}} \bar{f}$，我们有  

    $$
        aN \in \operatorname{\mathrm{Ker}} \bar{f} \Leftrightarrow f(a) = e \Leftrightarrow a \in \operatorname{\mathrm{Ker}} f.
    $$

    从而 $\operatorname{\mathrm{Ker}} \bar{f} = \{aN \mid a \in \operatorname{\mathrm{Ker}} f\} = (\operatorname{\mathrm{Ker}} f)/N$.  
    由上可见 $\bar{f}$ 是一个满态等价于 $f$ 是一个满态，$\bar{f}$ 是一个单态等价于 $\operatorname{\mathrm{Ker}} \bar{f} = \operatorname{\mathrm{Ker}} f/N$ 是 $G/N$ 的平凡子群，也有 $\operatorname{\mathrm{Ker}} f = N$.

这也就得出了著名的**群同态基本定理**，又称第一同构定理(First Isomorphism Theorem)。

!!! note "$\star$定理"
    若 $f: G \rightarrow H$ 是一个群同态，那么其诱导一同构 $G/\operatorname{\mathrm{Ker}} f \cong \operatorname{\mathrm{Im}} f$.

??? note "证明"
    引理(*)中取 $N = \operatorname{\mathrm{Ker}} f$ 即可. 

不过我们不满足于此，我们还希望寻找更多的性质更好的同构，为此我们要先证明一引理。

!!! success "引理"
    若 $f: G \rightarrow H$ 是一群同态， $N \triangleleft G, M \triangleleft H$，且 $f(N) < M$，那么 $f$ 诱导一个如下的群同态 $\bar{f}: G/N \rightarrow H/M$，映射方式为 $aN \mapsto f(a)M$.  
    $\bar{f}$ 是一个群同构等价于 $\operatorname{\mathrm{Im}} f \vee M = H$ 且 $f^{-1}(M) \subset N$. 若 $f$ 是一满同态使得 $f(N) = M$ 且 $\operatorname{\mathrm{Ker}} f \subset N$，则 $\bar{f}$ 是一个群同构. 

其也就是等同于下图是交换的。

\tikzcd
    G \arrow[r, "f"] \arrow[d, "\pi"] & H \arrow[d, "\pi'"] \\
    G/N \arrow[r, "\bar{f}"] &H/M  

??? note "证明"
    定义 $\pi, \pi'$ 分别为 $N, M$ 诱导的典范满射，即 $\pi : G \rightarrow G/N, \pi' : H \rightarrow H/M$. 考虑 $f$ 与 $\pi'$ 的复合 $\pi'f : G \rightarrow H/M, (\pi'f)(a) = f(a)M$. 如果 $a \in \operatorname{\mathrm{Ker}} \pi'f$，那么 $(\pi'f)(a) = f(a)M = M$. 也就是说 $f(a) \in M, \exists m \in M$ 使得 $f(a) = m$，也就是说 $\exists m \in M$，使得 $m$ 关于 $f$ 的原像是 $a$，所以 $a \in f^{-1}(M)$. 而如果 $a \in f^{-1}(M)$，则 $f(a) \in M$，进而 $f(a)M = M = (\pi'f)(a)$，$\operatorname{\mathrm{Ker}} \pi'f = f^{-1}(M)$. 又 $f(N) < M$，所以 $N \subset f^{-1}(M)$.  
    对 $\pi'f$ 应用引理(*)，$\exists \bar{f}: G/N \rightarrow H/M, \bar{f}(aN) = (\pi'f)(a) = f(a)M$ 其为一群同态，其为群同构等价于 $\pi'f$ 是满同态且 $N = \operatorname{\mathrm{Ker}} \pi'f$. 考虑 $\pi'f$ 是满同态，则 $\operatorname{\mathrm{Im}} f$ 经 $\pi'$ 后能映满商群 $H/M$，也就是说 $\operatorname{\mathrm{Im}} f$ 和 $M$ 能够生成群 $H$，$\operatorname{\mathrm{Im}} f \vee M = H$；考虑 $N = \operatorname{\mathrm{Ker}} \pi'f = f^{-1}(M)$，因为 $N \subset f^{-1}(M)$，所以有 $f^{-1}(M) \subset N$.  
    如果 $f$ 是一个满同态，显然有 $H = \operatorname{\mathrm{Im}} f = \operatorname{\mathrm{Im}} f \vee M$. 若 $f(N) = M$，$\operatorname{\mathrm{Ker}} f \subset N$，则 $f^{-1}(M) \subset N$，$\bar{f}$ 是一个同构. 

由此我们也有了第二同构定理(Second Isomorphism Theorem)和第三同构定理(Third Isomorphism Theorem).

!!! note "$\star$定理"
    1. 如果 $N$ 和 $K$ 是群 $G$ 的两子群，且 $N \triangleleft G$，那么 $K/(N \cap K) \cong NK/N$;  
    2. 若 $H$ 和 $K$ 是群 $G$ 的两个正规子群，且 $K < H$，那么 $H/K$ 是 $G/K$ 的一个正规子群且 $(G/K)/(H/K) \cong G/H$.

??? note "证明"
    1. $N \triangleleft NK = N \vee K$. 考虑如下映射链 $K \stackrel{\subset}{\rightarrow} NK \stackrel{\pi}{\rightarrow} NK/N$. 其复合 $\pi \subset := f$ 是一群同态. $f(k) = kN, \forall k \in K$，从而 $\operatorname{\mathrm{Ker}} f = K \cap N$. 由第一同构定理，存在群同构 $\bar{f}: K/K \cap N \rightarrow \operatorname{\mathrm{Im}} f$. 而 $\forall \alpha \in NK/N$，有 $\alpha = nkN, \exists n \in N, k \in K$. 而 $N$ 是正规的，进而 $\exists n_1 \in N, nk = kn_1, \alpha = nkN = kn_1N = kN = f(k)$，所以 $\operatorname{\mathrm{Im}} f = NK/N$.  
    2. 考虑 $\mathrm{id}_G$，有 $\mathrm{id}_G(K) < H$. 其诱导了一个满同态 $I: G/K \rightarrow G/H, I(ak) = aH$. 而 $H = I(aK)$ 等价于 $a \in H$，所以 $\operatorname{\mathrm{Ker}} I = \{aK \mid a \in H\} = H/K$. 进而 $H/K \triangleleft G/K$ 且 $G/H = \operatorname{\mathrm{Im}} I \cong (G/K)/(\operatorname{\mathrm{Ker}} I) = (G/K)/(H/K)$.

如下定理表明满同态是保持正规子群的。

!!! note "$\star$定理"
    设 $f: G \rightarrow H$ 是一个群的满同态, 则 $K \mapsto f(K)$ 给出了一个 $G$ 的全体包含 $\operatorname{\mathrm{Ker}} f$ 的子群 $K$ 所构成的集合 $S_f(G)$ 和 $H$ 的全体子群组成的集合 $S(H)$ 之间的一一对应, 且正规子群对应正规子群.

下面是一个自然推论。

!!! success "推论"
    若 $N$ 是 $G$ 的正规子群, 则 $G/N$ 的每个子群都有形式 $K/N$, 其中 $K$ 是 $G$ 的一个包含 $N$ 的子群. 进而 $K/N \triangleleft G/N$ 等价于 $K \triangleleft G$.