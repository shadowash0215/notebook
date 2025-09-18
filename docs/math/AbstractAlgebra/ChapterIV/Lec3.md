# 分裂域 代数闭包 正规性

!!! info "定义"
    设 $F$ 为域，$f \in F[x]$ 是一个正次数多项式，称 $f$ 在 $F$ 上**分裂**(splits over $F$)，也称为在 $F[x]$ 中分裂，若其可以写成 $F[x]$ 中线性因子的乘积，即 $f = u_0(x - u_1) \cdots (x - u_n)$，其中 $u_i \in F$。  
    设 $K$ 是域，$f \in K[x]$ 是一个正次数多项式，$K$ 的一个扩域 $F$ 被称为多项式 $f$ 在 $K$ 上的**分裂域**(splitting field)，若 $f$ 在 $F$ 上分裂，并且 $F = K(u_1, u_2, \ldots, u_n)$，其中 $u_1, \ldots, u_n$ 是 $f$ 在 $F$ 中的全部根。  
    设 $S$ 是一 $K[x]$ 中的正次数多项式集合，$K$ 的一个扩域 $F$ 被称为多项式集合 $S$ 在 $K$ 上的**分裂域**，若 $S$ 中的每个多项式在 $F$ 上分裂，并且 $F$ 是由 $S$ 中所有多项式的根在 $K$ 上生成的域。  

!!! example "示例"
    设 $f = x^2 - 2 \in \mathbb{Q}[x]$，其只有两个根 $u_1 = \sqrt{2}, u_2 = -\sqrt{2}$，所以 $\mathbb{Q}(\sqrt{2}) = \mathbb{Q}(u_1, u_2)$ 是 $f$ 在 $\mathbb{Q}$ 上的分裂域。类似地，$\mathbb{C}$ 是 $x^2 + 1 \in \mathbb{R}[x]$ 在 $\mathbb{R}$ 上的分裂域。  
    但 $u$ 是不可约多项式 $f \in K[x]$ 的根并不代表 $K(u)$ 是 $f$ 在 $K$ 上的分裂域，例如 $f = x^3 - 2 \in \mathbb{Q}[x]$，$u$ 为 $2$ 的实立方根（其余立方根是复数），但 $\mathbb{Q}(u) \subset \mathbb{R}$，不是 $f$ 在 $\mathbb{Q}$ 上的分裂域。

!!! tip "注记"
    若 $F$ 是 $S$ 在 $K$ 上的分裂域，则 $F = K(X)$，其中 $X$ 是 $K[x]$ 的子集合 $S$ 中所有多项式的全部根所组成的集合。所以 $F$ 在 $K$ 上是代数的。如果 $S$ 是有限的，如 $S = \{f_1, f_2, \ldots, f_n\}$，则 $F$ 是 $K$ 的有限扩域，并且 $S$ 的分裂域与 $f = f_1 f_2 \cdots f_n$ 的分裂域相同。

所以关于多项式集合 $S$ 的分裂域，主要关注 $S$ 由一个多项式或者无限多个多项式组成的情况。我们将要证明每个（有限维）Galois 代数扩张事实上都是一个多项式（有限）集合的一种特殊类型的分裂域。不过首先要解决的问题是，是否每个多项式集合都有分裂域？对于一个多项式的情况，我们有如下定理：

!!! note "定理"
    设 $K$ 是域，$f \in K[x]$ 的次数为 $n \geqslant 1$，那么 $f$ 存在分裂域 $F$，且 $[F:K] \leqslant n!$。

    ??? note "证明"
        归纳法证明。当 $n = 1$ 或 $f$ 在 $K$ 上分裂时，$F = K$。  
        当 $n > 1$ 且 $f$ 在 $K$ 上不分裂时，令 $g \in K[x]$ 是 $f$ 的一个次数大于 $1$ 的不可约因子，可知存在一个单扩张 $K(u)$，使得 $u$ 是 $g$ 的一个根，并且 $[K(u):K] = \operatorname{deg} g$。所以 $f = (x - u)h$，其中 $h \in K(u)[x]$ 且次数为 $n - 1$。根据归纳假设，存在 $h$ 的分裂域 $F$，且 $[F:K(u)] \leqslant (n - 1)!$。所以 $[F:K] = [F:K(u)][K(u):K] \leqslant n!$。

但对于多项式无限集合的情况，证明要困难的多。这里采用了一种间接证明的方法，即引进此类分裂域的一种特殊情形。在此之前，我们先描述域上的一些等价条件，并引进一些概念。

!!! note "定理"
    下列关于域 $F$ 的条件是等价的：  
    (i) 每个非常数多项式 $f \in F[x]$ 在 $F$ 中都有根；  
    (ii) 每个非常数多项式 $f \in F[x]$ 都在 $F$ 上分裂；  
    (iii) $F[x]$ 中的每个不可约多项式次数均为 $1$；  
    (iv) 除 $F$ 自身外，不存在 $F$ 的代数扩域；  
    (v) 存在 $F$ 的一个子域 $K$，使得 $F$ 在 $K$ 上是代数的，且 $K[x]$ 中的每个多项式均在 $F$ 上分裂。  

    ??? note "证明"
        (i) $\Rightarrow$ (iii)：域上的 $1$ 次多项式都是不可约的。设 $f$ 为 $F[x]$ 中的不可约多项式，其存在一个根 $a$，所以 $f$ 是 $x - a$ 的倍数，而考虑到 $f$ 是不可约的，所以 $f = k(x - a)$，其中 $k \in F - \{0\}$。  
        (iii) $\Rightarrow$ (ii)：域上的多项式都可以分解为不可约多项式的乘积，而不可约多项式次数均为 $1$，所以每个非常数多项式都在 $F$ 上分裂。  
        (ii) $\Rightarrow$ (i)：显然。

满足以上条件的域被称为**代数闭域**(algebraically closed field)。复数域 $\mathbb{C}$ 是一个代数闭域，而实数域 $\mathbb{R}$ 不是代数闭域。以下给出代数闭域、域扩张与分裂域之间的关系：

!!! note "定理"
    设 $F$ 是 $K$ 的一个域扩张，以下条件是等价的：  
    (i) $F$ 在 $K$ 上是代数的，且 $F$ 是代数闭域；  
    (ii) $F$ 是 $K[x]$ 中全体（不可约）多项式所组成的集合的分裂域。 

满足以上条件的域扩张 $F$ 被称为 $K$ 的一个**代数闭包**(algebraic closure)。所以，分裂域的存在性问题可以转化为代数闭包的存在性问题。代数闭包的存在性证明的难点在于集合论，需要运用 Zorn 引理。

!!! success "引理"
    如果 $F$ 是 $K$ 的一个代数扩张，那么 $\lvert F \rvert \leqslant \aleph_0 \cdot \lvert K \rvert$。  

!!! note "定理"
    所有的域 $K$ 都存在代数闭包。$K$ 的任意两个代数闭包是 $K$-自同构的。

!!! success "推论"
    设 $K$ 是域，$S$ 是 $K[x]$ 中的一个正次数多项式集合，那么存在 $S$ 在 $K$ 上的分裂域。

现在便可以将讨论的中心由存在性转移到唯一性。

!!! note "定理"
    设 $\sigma: K \to L$ 是一个域同构，$S = \{f_i\}$ 是 $K[x]$ 中的一个正次数多项式集合，$S' = \{\sigma(f_i)\}$ 是 $L[x]$ 中对应的正次数多项式集合。如果 $F$ 是 $S$ 在 $K$ 上的分裂域，$M$ 是 $S'$ 在 $L$ 上的分裂域，那么 $\sigma$ 可以扩展为一个域同构 $F \cong M$。

!!! success "推论"
    设 $K$ 是域，$S$ 是 $K[x]$ 中的一个正次数多项式集合，则 $S$ 在 $K$ 上的任意两个分裂域是 $K$-同构的。特别地，$K$ 的任意两个代数闭包是 $K$-同构的。

!!! info "定义"
    设 $K$ 是域，$f \in K[x]$ 是不可约多项式，如果 $E$ 是 $f$ 在 $K$ 上的某个分裂域，且 $f$ 在 $E$ 中的根都是单根，那么称 $f$ 为**可分的**（separable）。  
    设 $F$ 是 $K$ 的一个扩域，$u \in F$ 是在 $K$ 上代数的，那么称 $u$ 是可分的，如果其在 $K$ 上的极小多项式是可分的。如果 $F$ 中的每个元素都是可分的，那么称 $F$ 是 $K$ 的一个**可分扩张**（separable extension）。

!!! note "定理"
    设 $F$ 是 $K$ 的一个扩域，那么以下条件是等价的：  
    (i) $F$ 是 $K$ 上的一个代数 Galois 扩张；  
    (ii) $F$ 是 $K$ 上的一个可分扩张，且 $F$ 是 $K[x]$ 中某个正次数多项式集合 $S$ 在 $K$ 上的分裂域；  
    (iii) $F$ 是 $K[x]$ 中某个可分正次数多项式集合 $T$ 在 $K$ 上的分裂域。

    !!! tip "注记"
        如果 $F$ 在 $K$ 上还是有限维的，那么 (ii) 和 (iii) 还可以进一步加强，如 (iii) 可以加强为 $F$ 是某个多项式 $f \in K[x]$ 在 $K$ 上的分裂域，且 $f$ 的每个不可约因子都是可分的。

    ??? note "证明"
        (i) $\Rightarrow$ (ii) and (iii): 设 $u \in F$ 对应的极小多项式为 $f \in K[x]$，则可使用如下的证明（取 $E = F$）：
        > 考虑 $u \in E$，因为 $E$ 在 $K$ 上是代数的，所以设 $f \in K[x]$ 是 $u$ 的极小多项式，并且令 $u = u_1$. $u_1, u_2, \ldots, u_r$ 是 $f$ 在 $E$ 中的所有互异的根，易知 $r \leqslant n = \operatorname{deg} f$。设 $\tau \in \operatorname{Aut}_K E$，则 $\tau$ 对 $\{u_i\}$ 的作用是一个置换，所以首一多项式 $g = \prod_{i = 1}^r (x - u_i)$ 的系数都被 $\tau$ 固定。又因为 $E$ 在 $K$ 上是 Galois 的，所以 $g \in K[x]$。而 $u = u_1$ 是 $g$ 的一个根，因此 $f \mid g$。又因为 $g$ 是首一的并且 $\operatorname{deg} g \leqslant \operatorname{deg} f$，所以 $f = g$，从而 $f$ 的所有根是互不相同并且全部落在 $E$ 中的。  

        来证明 $f$ 在 $F$ 上分裂成了互异的一次因子的乘积，也就说明了 $u$ 是可分的。而设 $\{v_i \mid i \in I\}$ 是 $F$ 在 $K$ 上的一组基，令 $f_i \in K[x]$ 是 $v_i$ 的极小多项式（$i \in I$），可知 $f_i$ 在 $F[x]$ 中均是可分的，并且分裂。所以 $F$ 是 $S = \{f_i \mid i \in I\}$ 在 $K$ 上的分裂域。  
        (ii) $\Rightarrow$ (iii): 设 $f \in S$，而 $g \in K[x]$ 是 $f$ 的一个首一不可约因子。因为 $f$ 在 $F$ 上分裂，所以 $g$ 是某个 $u \in F$ 的极小多项式。而 $f$ 在 $F$ 上是可分的，所以 $g$ 也是可分的。设 $S = \{f_i\}$，按照如上构造对应获得的多项式集合为 $T = \{g_i\}$，则 $F$ 是 $T$ 在 $K$ 上的分裂域，并且 $T$ 中的每个多项式都是可分的。  
        (iii) $\Rightarrow$ (i): $F$ 在 $K$ 上是代数的，因为 $K$ 上的任何分裂域都是代数扩张。考虑 $u \in F - K$，根据分裂域的定义以及  
        > (vii) 对于每个 $v \in K(X)$(或 $v \in K[X]$)，均存在 $X$ 的有限子集 $X'$，使得 $v \in K(X')$(或 $v \in K[X']$).   

        可知 $u \in K(v_1, \ldots, v_n)$，其中 $v_i$ 是某个 $f_i \in T$ 的根。因此 $u \in E = K(u_1, \ldots, u_r)$，其中 $u_i$ 是 $f_1, \ldots, f_n$ 在 $F$ 中的所有根，进而 $[E:K]$ 是有限的。因为每个 $f_i$ 都在 $F$ 上分裂，所以 $E$ 是有限集合 $\{f_1, \ldots, f_n\}$ 在 $K$ 上的分裂域。若假定定理对有限维是成立的，那么 $E$ 在 $K$ 上便是 Galois 的，从而存在 $\tau \in \operatorname{Aut}_K E$，使得 $\tau u \neq u$。而  
        > 如果 $F$ 是 $S$ 在 $K$ 上的分裂域，而 $E$ 是中间域，则 $F$ 也是 $S$ 在 $E$ 上的分裂域。  

        所以 $F$ 也是 $T$ 在 $E$ 上的分裂域，所以 $\tau$ 可以扩充为一个自同构 $\sigma \in \operatorname{Aut}_K F$，使得 $\sigma u = \tau u \neq u$。因此 $u (\in F - K) \notin G'$，所以 $F$ 是 $K$ 的一个 Galois 扩张。  
        这表明我们只需要在 $[F:K]$ 有限的情况下证明定理即可。此时存在有限多个多项式 $g_1, \ldots, g_n \in T$，使得 $F$ 是 $\{g_1, \ldots, g_t\}$ 在 $K$ 上的分裂域，并且有 $\operatorname{Aut}_K F$ 是有限的。设 $K_0$ 是 $\operatorname{Aut}_K F$ 的固定域，那么根据 Artin 定理与 Galois 基本定理，$F$ 是 $K_0$ 的 Galois 扩张，并且 $[F:K_0] = \lvert \operatorname{Aut}_K F \rvert$。所以，为了证明 $F$ 是 $K$ 的 Galois 扩张，只需要证明 $[F:K] = \lvert \operatorname{Aut}_K F \rvert$。  
        这部分证明采用归纳法。设 $[F:K] = n$，$n = 1$ 是平凡的。若 $n > 1$，则必有某个 $g_i$（设为 $g_1$）的次数 $s > 1$。设 $u \in F$ 是 $g_1$ 的根，所以 $[K(u):K] = \operatorname{deg} g_1 = s$。因为 $g_1$ 是可分的，所以 $g_1$ 共有 $s$ 个根。使用如下的证明（取 $L = K, M = K(u), f = g_1$）：  
        > 设 $\tau M'$ 是 $M'$ 关于 $L'$ 的一个左陪集，对于 $\sigma \in M' = \operatorname{Aut}_M F$，因为 $u \in M$，所以 $\sigma(u) = u$，也就有 $\tau \sigma(u) = \tau(u)$。这也就表明 $\tau M'$ 中的所有元素对 $u$ 的作用都是相同的，即 $u \mapsto \tau(u)$. 而注意到 $\tau \in L'$，$u$ 是 $f \in L[x]$ 的根，所以 $\tau(u)$ 也是 $f$ 的根，这表明 $\tau M' \mapsto \tau(u)$ 是良定义的。以下证明其是单射：设 $\tau M' = \tau_0 M'(\tau, \tau_0 \in L')$，所以 $\tau_0^{-1}\tau(u) = u$，即 $\tau_0^{-1}\tau$ 固定 $u$，从而有 $\tau_0^{-1}\tau$ 逐元素地固定 $L(u) = M$（代数扩张与基的关系），所以 $\tau_0^{-1}\tau \in M'$，即 $\tau M' = \tau_0 M'$，所以 $\tau M' \mapsto \tau(u)$ 是单射。

        存在从 $H = \operatorname{Aut}_{K(u)} F$ 关于 $\operatorname{Aut}_K F$ 的全体左陪集组成的集合到 $g_1$ 在 $F$ 中的 $s$ 个根所组成的集合的一个单射 $\sigma H \mapsto \sigma(u)$。所以 $[\operatorname{Aut}_K F : H] \leqslant s$。若 $v \in F$ 是 $g_1$ 的另外一个根，则存在同构 $\tau: K(u) \cong K(v)$，使得 $\tau(u) = v$ 且 $\tau \mid_K = \operatorname{id}_K$。因为 $F$ 是 $\{g_1, \ldots, g_t\}$ 在 $K(u)$ 和 $K(v)$ 上的分裂域，所以 $\tau$ 可以扩充为一个自同构 $\sigma \in \operatorname{Aut}_K F$，使得 $\sigma(u) = v$。所以，$g_1$ 的每个根都是 $H$ 的某个左陪集的像，所以 $[\operatorname{Aut}_K F : H] = s$。进一步，  
        > 如果 $F$ 是 $S$ 在 $K$ 上的分裂域，而 $T$ 是 $S$ 中多项式的全部不可约因子所组成的集合，则 $F$ 也是 $T$ 在 $K$ 上的分裂域。

        所以 $F$ 是多项式集合 $\{g_i\}$ 在 $K(u)[x]$ 中的全部不可约因子 $h_j$ 组成的集合在 $K(u)$ 上的分裂域。显然 $h_j$ 是可分的，因为 $h_j$ 整除某个 $g_i$。因为 $[F:K(u)] = n/s < n$，所以由归纳假设有 $[F: K(u)] = \lvert \operatorname{Aut}_{K(u)} F \rvert = \lvert H \rvert$。所以有  

        \[
            [F:K] = [F:K(u)][K(u):K] = \lvert H \rvert \cdot s = \lvert H \rvert \cdot \lvert \operatorname{Aut}_K F : H \rvert = \lvert \operatorname{Aut}_K F \rvert.
        \]

        命题得证。

由此，我们可以将 Galois 理论基本定理推广到无限维的情况：

!!! note "推广 Galois 理论基本定理"
    设 $F$ 是 $K$ 的一个代数 Galois 扩张，则在该扩张的全部中间域所构成的集合和 Galois 群 $\operatorname{Aut}_K F$ 的全部闭子群所构成的集合之间存在一个一一对应(由 $E \mapsto E' = \operatorname{Aut}_E F$ 给出)，并且满足 $F$ 在每个中间域 $E$ 上都是 Galois 的。另一方面，$E$ 在 $K$ 上是 Galois 的当且仅当对应的子群 $E' = \operatorname{Aut}_E F$ 是 $G = \operatorname{Aut}_K F$ 的正规子群，此时 $\operatorname{Aut}_K E \cong \operatorname{Aut}_K F / E'$.  

    !!! tip "注记"
        如果 $[F:K]$ 是无限的，则 $\operatorname{Aut}_K F$ 永远存在一个不闭的子群。

    ??? note "证明"
        首先证明所有中间域都是闭的。因为 $F$ 是 $K$ 上的代数 Galois 扩张，所以 $F$ 是 $K[x]$ 中某个可分正次数多项式集合 $T$ 在 $K$ 上的分裂域。设 $E$ 是 $F$ 的一个中间域，则有 $F$ 也是 $T$ 在 $E$ 上的分裂域。所以 $F$ 在 $E$ 上是 Galois 的，从而 $E$ 是闭的。  
        因为 $F$ 是 $K$ 上的代数扩张，所以 $E$ 在 $K$ 上也是代数的。由如下证明：  
        > 从而，如果 $E$ 同时也是 $K$ 上 Galois 的，那么便可以得到 $E$ 是稳定的，对应有 $E' = \operatorname{Aut}_E F$ 是 $\operatorname{Aut}_K F$ 的正规子群。而如果 $E' = \operatorname{Aut}_E F$ 是 $\operatorname{Aut}_K F$ 的正规子群，那么 $E''$ 是一个稳定中间域，而又知道 Galois 扩张的中间域都是闭的，所以 $E'' = E$，即 $E$ 是稳定中间域，进而 $E$ 是 $K$ 上 Galois 的。

        便可得到 $E$ 在 $K$ 上是 Galois 的 等价于 $E' = \operatorname{Aut}_E F$ 是 $\operatorname{Aut}_K F$ 的正规子群。  
        因为 $E$ 在 $K$ 上是 Galois 的，并且 $E'$ 是 $\operatorname{Aut}_K F$ 的正规子群，所以 $E$ 是稳定的，也就有 $G/E' = \operatorname{Aut}_K F / \operatorname{Aut}_E F$ 同构于 $E$ 的所有可延拓的 $K$-自同构所构成的群，其是 $\operatorname{Aut}_K E$ 的子群。因为 $F$ 是 $K$ 上的分裂域，所以 $F$ 也是 $E$ 上的分裂域，也就是说 $\operatorname{Aut}_K E$ 中的每个自同构都是可以延拓到 $F$ 上的。所以 $G/E' = \operatorname{Aut}_K F / \operatorname{Aut}_E F$ 同构于 $\operatorname{Aut}_K E$。

接下来，我们要对分裂域进行刻画。

!!! info "定义"
    设 $F$ 是 $K$ 的一个代数扩张，称 $F$ 是 $K$ 的一个**正规扩张**（normal extension），或 $K$ 上正规的，若 $K[x]$ 中的每个不可约多项式只要有根在 $F$ 中，那么其在 $F$ 上分裂。

!!! note "定理"
    设 $F$ 是 $K$ 的一个代数扩张，那么以下条件等价：  
    (i) $F$ 在 $K$ 上正规；  
    (ii) $F$ 是 $K[x]$ 的某个多项式集合 $S$ 在 $K$ 上的分裂域；  
    (iii) 若 $\overline{K}$ 是 $K$ 的某个包含 $F$ 的代数闭包，则对于任意一个域的 $K$-单态 $\sigma: F \to \overline{K}$，必然有 $\operatorname{Im} \sigma = F$，也就是说 $\sigma$ 是 $F$ 上的 $K$-自同构。

    ??? note "证明"
        (i) $\Rightarrow$ (ii): 设 $\{u_i \mid i \in I\}$ 是 $F$ 在 $K$ 上的一组基，设 $S = \{f_i\}$，其中 $f_i \in K[x]$ 是 $u_i$ 的极小多项式。因为 $F$ 在 $K$ 上正规，所以 $f_i$ 在 $F$ 上分裂，所以 $F$ 是 $S$ 在 $K$ 上的分裂域。  
        (ii) $\Rightarrow$ (iii): 设 $F$ 是 $S = \{f_i \mid i \in I\}$ 在 $K$ 上的分裂域，$\sigma: F \to \overline{K}$ 是一个域的 $K$-单态。若 $u$ 是 $f_j$ 的一个根，那么 $\sigma(u)$ 也是 $f_j$ 的一个根。因为 $f_j$ 在 $F$ 上分裂，所以设 $f_j = c(x - u_1) \cdots (x - u_n), u_i \in F, c \in K$。因为 $\overline{K}[x]$ 是唯一分解整环，所以对于任意 $i = 1, \ldots, n$，$\sigma(u_i)$ 一定落在 $u_1, \ldots, u_n$ 中的某一个上。因为 $\sigma$ 是单射，所以其也只是一个置换。但 $F$ 是由所有 $f_j$ 的所有根在 $K$ 上生成的，所以 $\sigma(F) = F$，也就有 $\sigma \in \operatorname{Aut}_K F$。  
        (iii) $\Rightarrow$ (i): 设 $\overline{K}$ 是 $F$ 的一个代数闭包，所以 $\overline{K}$ 是 $K$ 的一个代数扩张，进而是 $K$ 的一个包含 $F$ 的代数闭包。设 $f \in K[x]$ 是一个不可约多项式，其有一个根 $u \in F$，根据之前的构造方法可知 $\overline{K}$ 包含 $f$ 的全部根。设 $v \in \overline{K}$ 是 $f$ 的任意一个根，那么存在着域的 $K$-同构 $\sigma: K(u) \cong K(v)$，使得 $\sigma(u) = v$，其可以延拓为 $\overline{K}$ 的 $K$-自同构。从而 $\sigma \mid_F$ 是单态 $F \to \overline{K}$，并且有 $\sigma(F) = F$。因此 $v = \sigma(u) \in F$，所以 $f$ 在 $F$ 上分裂，从而 $F$ 在 $K$ 上正规。

!!! success "推论"
    设 $F$ 是 $K$ 的一个代数扩张，那么 $F$ 在 $K$ 上是 Galois 的当且仅当 $F$ 是 $K$ 的一个正规且可分扩张。如果 $\operatorname{char} K = 0$，那么 $F$ 在 $K$ 上是 Galois 的当且仅当 $F$ 是 $K$ 的一个正规扩张。

!!! note "定理"
    设 $E$ 是 $K$ 的一个代数扩张，则存在 $E$ 的一个扩张 $F$，使得  
    (i) $F$ 是 $K$ 的一个正规扩张；  
    (ii) $F$ 没有包含 $E$ 并且在 $K$ 上正规的真子域；  
    (iii) 如果 $E$ 在 $K$ 上是可分的，那么 $F$ 在 $K$ 上是 Galois 的；  
    (iv) $[F:K]$ 是有限的当且仅当 $[E:K]$ 是有限的。  
    (v) $F$ 在不计 $E$-同构的意义下是唯一的。

该定理中的 $F$ 被称为 $E$ 在 $K$ 上的一个**正规闭包**（normal closure）。