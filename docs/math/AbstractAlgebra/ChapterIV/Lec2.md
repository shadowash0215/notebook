# Galois 理论基本定理

!!! info "定义"
    设 $E$ 和 $F$ 是 $K$ 的扩张, 则非零映射 $\sigma: E \to F$ 叫做一个 **$K$-同态**(K-homomorphism), 是指 $\sigma$ 是一个域同态同时也是一个 $K$-模同态, 即 $\sigma \mid_K = 1_K$. 类似地, 一个域自同构 $\sigma \in \operatorname{Aut}(F)$ 如果又是一个 $K$-同态, 则称 $\sigma$ 是 $F$ 的一个 **$K$-自同构**(K-automorphism). $F$ 的全体 $K$-自同构所形成的群叫做 $F$ 在 $K$ 上的 **Galois 群**(Galois group), 表示为 $\operatorname{Aut}_K(F)$.

!!! note "定理"
    设 $F$ 是 $K$ 的扩域, $f \in K[x]$. 如果 $u \in F$ 是 $f$ 的根而 $\sigma \in \operatorname{Aut}_K(F)$, 则 $\sigma(u)$ 也是 $f$ 的根.

这一定理的一个重要应用是：如果 $u$ 在 $K$ 上是代数的，且 $u$ 的极小多项式 $f \in K[x]$ 的次数是 $n$，则每个自同构 $\sigma \in \operatorname{Aut}_K K(u)$ 由它在 $u$ 上的作用唯一确定(因为 $\{1_K, u, \ldots, u^{n-1}\}$ 是 $K(u)$ 在 $K$ 上的一组基)。因此，$\operatorname{Aut}_K K(u)$ 的阶数不超过 $m$，其中 $m$ 是 $f$ 在 $K(u)$ 中相异根的个数。

!!! example "示例"
    若 $F = \mathbf{Q}(\sqrt{2}, \sqrt{3}) = \mathbf{Q}(\sqrt{2})(\sqrt{3})$，因为 $x^2 - 3$ 在 $\mathbf{Q}(\sqrt{2})$ 上不可约，所以 $\{1, \sqrt{2}, \sqrt{3}, \sqrt{6}\}$ 是 $F$ 在 $\mathbf{Q}$ 上的一组基。所以，如果 $\sigma \in \operatorname{Aut}_{\mathbf{Q}} F$，则 $\sigma$ 完全由 $\sigma(\sqrt{2})$ 和 $\sigma(\sqrt{3})$ 完全确定。而 $\sigma(\sqrt{2}) = \pm \sqrt{2}$，$\sigma(\sqrt{3}) = \pm \sqrt{3}$，所以 $\operatorname{Aut}_{\mathbf{Q}} F$ 中至多有四个元素，事实上这四种情况都是可能的，所以 $\operatorname{Aut}_{\mathbf{Q}} F$ 有四个元素，且 $\operatorname{Aut}_{\mathbf{Q}} F \cong \mathbf{Z}_2 \oplus \mathbf{Z}_2$.

!!! note "定理"
    设 $F$ 是 $K$ 的一个扩域，$E$ 是一个中间域，$H$ 是 $\operatorname{Aut}_K F$ 的一个子群，则  
    (i) $H' = \{v \in F \mid \sigma(v) = v, \forall \sigma \in H\}$ 是一个中间域；  
    (ii) $E' = \{\sigma \in \operatorname{Aut}_K F \mid \sigma(u) = u, \forall u \in E\} = \operatorname{Aut}_E F$ 是 $\operatorname{Aut}_K F$ 的一个子群.  
    域 $H'$ 被称作 $H$ 在 $F$ 上的**固定域**(fixed field).

!!! info "定义"
    设 $F$ 是 $K$ 的一个扩域，并且 Galois 群 $\operatorname{Aut}_K F$ 的固定域是 $K$ 自身，则称 $F$ 是 $K$ 的一个 **Galois 扩张**(Galois extension)，或称 $F$ 在 $K$ 上是 **Galois 的**.

!!! tip "注记"
    $F$ 在 $K$ 上是 Galois 的等价于对于任一 $u \in F - K$，均存在 $\sigma \in \operatorname{Aut}_K F$ 使得 $\sigma(u) \neq u$. 如果 $F$ 是 $K$ 的任意扩张，而 $K_0$ 是 $\operatorname{Aut}_K F$ 的固定域，则 $F$ 在 $K_0$ 上是 Galois 的，且 $K \subset K_0$，$\operatorname{Aut}_{K_0} F = \operatorname{Aut}_K F$.

如果 $L$ 和 $M$ 是某个扩张的两个中间域，且 $L \subset M$，则称维数 $[M:L]$ 是 $L$ 和 $M$ 的 **相对维数**(relative degree)。类似地，如果 $H$ 和 $J$ 是该扩张的 Galois 群的两个子群，且 $H < J$，则称 $[J:H]$ 是 $H$ 和 $J$ 的相对指数(relative index)。

!!! note "Galois 理论基本定理"
    如果 $F$ 是 $K$ 的一个有限维 Galois 扩张，则在该扩张的全部中间域所构成的集合和 Galois 群 $\operatorname{Aut}_K F$ 的全部子群所构成的集合之间存在一个一一对应(由 $E \mapsto E' = \operatorname{Aut}_E F$ 给出)，并且  
    (i) 两个中间域的相对维数等于它们所对应的子群的相对指数，特别地，$[F:K] = \lvert \operatorname{Aut}_K F \rvert$；  
    (ii) $F$ 在每个中间域 $E$ 上都是 Galois 的. 另一方面，$E$ 在 $K$ 上是 Galois 的当且仅当对应的子群 $E' = \operatorname{Aut}_E F$ 是 $G = \operatorname{Aut}_K F$ 的正规子群，此时 $\operatorname{Aut}_K E \cong \operatorname{Aut}_K F / E'$.

以下两张图是 Galois 理论基本定理的示意图：

\tikzcd
    F \arrow[d] & M \arrow[l, "\supset"] \arrow[d] & L \arrow[l, "\supset"] \arrow[d] & K \arrow[l, "\supset"] \arrow[d] \\
    1 & M' \arrow[l, "<"] & L' \arrow[l, "<"] & G \arrow[l, "<"]

\tikzcd
    F & H' \arrow[l, "\supset"] & J' \arrow[l, "\supset"] & K \arrow[l, "\supset"] \\
    1 \arrow[u] & H \arrow[l, "<"] \arrow[u] & J \arrow[l, "<"] \arrow[u] & G \arrow[l, "<"]

以下是对其形式化的阐述：

!!! success "引理"
    设 $F$ 是 $K$ 的扩域，$L$ 和 $M$ 是 $F$ 的两个中间域，$H$ 和 $J$ 是 $\operatorname{Aut}_K F$ 的两个子群，则  
    (i) $F' = 1$，$K' = G$;  
    (i') $1' = F$;  
    (ii) $L \subset M \Rightarrow M' < L'$;  
    (ii') $H < J \Rightarrow J' \subset H'$;  
    (iii) $L \subset L'', H < H''$;  
    (iv) $L' = L'''$，$H' = H'''$. 

设 $X$ 是一个中间域或者是 Galois 群的一个子群，若 $X = X''$，则称 $X$ 是**闭的**(closed)。所以 $F$ 在 $K$ 上是 Galois 的等价于 $K$ 是闭的。

!!! note "定理"
    如果 $F$ 是 $K$ 的一个扩域，则在该扩张的闭中间域所构成的集合和其 Galois 群的闭子群所构成的集合之间存在一个由 $E \mapsto E' = \operatorname{Aut}_E F$ 给出的一一对应.

上面这个定理是我们证明 Galois 理论基本定理第 (i) 条的关键。但想让它发挥作用我们还需要证明在有限维 Galois 代数扩张中所有的中间域和 Galois 群的子群都是闭的。以下先证明一些技术型的引理，它们能让我们估计各种相对维数：

!!! success "引理"
    设 $F$ 是 $K$ 的一个扩域，$L$ 和 $M$ 是 $F$ 的两个中间域，且 $L \subset M$. 如果 $[M:L]$ 有限，则 $[L':M'] \leqslant [M:L]$. 特别地，如果 $[F:K]$ 有限，则 $\lvert \operatorname{Aut}_K F \rvert \leqslant [F:K]$.

    ??? success "证明"
        对 $[M:L] = n$ 进行归纳。$n = 1$ 时结论显然成立。设 $n > 1$ 并且当 $i < n$ 时结论都成立，那么存在 $u \in M - L$，因为 $[M:L]$ 是有限的，所以 $u$ 在 $L$ 上是代数的，设 $f \in L[x]$ 是 $u$ 的极小多项式，$\operatorname{deg} f = k > 1$，那么有 $[L(u):L] = k, [M: L(u)] = n/k$.  
        (1) 若 $k < n$，则有 $1 < n/k < n$，由归纳假设，$[L':L(u)'] \leqslant k, [L(u)':M'] \leqslant n/k$，所以 $[L':M'] = [L':L(u)'][L(u)':M'] \leqslant n$.  
        (2) 若 $k = n$，则 $[M: L(u)] = 1$，即 $M = L(u)$。设 $M'$ 关于 $L'$ 的全体左陪集构成的集合为 $S$，$f$ 在 $F$ 中的所有的根构成的集合为 $T$，我们希望构建一个从 $S$ 到 $T$ 的单射，那么就会有 $\lvert S \rvert \leqslant \lvert T \rvert$。因为 $\lvert S \rvert = [L':M']$，并且 $\lvert T \rvert < n$，所以就能得到 $[L':M'] \leqslant [M:L]$.  
        设 $\tau M'$ 是 $M'$ 关于 $L'$ 的一个左陪集，对于 $\sigma \in M' = \operatorname{Aut}_M F$，因为 $u \in M$，所以 $\sigma(u) = u$，也就有 $\tau \sigma(u) = \tau(u)$。这也就表明 $\tau M'$ 中的所有元素对 $u$ 的作用都是相同的，即 $u \mapsto \tau(u)$. 而注意到 $\tau \in L'$，$u$ 是 $f \in L[x]$ 的根，所以 $\tau(u)$ 也是 $f$ 的根，这表明 $\tau M' \mapsto \tau(u)$ 是良定义的。以下证明其是单射：设 $\tau M' = \tau_0 M'(\tau, \tau_0 \in L')$，所以 $\tau_0^{-1}\tau(u) = u$，即 $\tau_0^{-1}\tau$ 固定 $u$，从而有 $\tau_0^{-1}\tau$ 逐元素地固定 $L(u) = M$（代数扩张与基的关系），所以 $\tau_0^{-1}\tau \in M'$，即 $\tau M' = \tau_0 M'$，所以 $\tau M' \mapsto \tau(u)$ 是单射。  
        特别地，$\lvert \operatorname{Aut}_K F \rvert = [\operatorname{Aut}_K F : 1] = [K':F'] \leqslant [F:K]$.

!!! success "引理"
    设 $F$ 是 $K$ 的一个扩域，$H$ 和 $J$ 是 $\operatorname{Aut}_K F$ 的两个子群，且 $H < J$. 如果 $[J:H]$ 有限，则 $[H':J'] \leqslant [J:H]$.  

    ??? success "证明"
        反证法。设 $[J:H] = n$，$[H':J'] = m > n$，则存在 $u_1, u_2, \ldots, u_{n + 1} \in H'$ 并且在 $J'$ 上是线性无关的。设 $J$ 关于 $H$ 的轨道分解为 $J = \bigsqcup_{i = 1}^n \tau_i H$，并且考虑域 $F$ 上如下的 $n$ 个系数为 $\tau_i (u_j)$ 的 $n + 1$ 元齐次线性方程组

        \begin{align}
            \tau_1 (u_1) x_1 + \tau_1 (u_2) x_2 + & \cdots + \tau_1 (u_{n + 1}) x_{n + 1} = 0 \\
            \tau_2 (u_1) x_1 + \tau_2 (u_2) x_2 + & \cdots + \tau_2 (u_{n + 1}) x_{n + 1} = 0 \\
            & \cdots \\
            \tau_n (u_1) x_1 + \tau_n (u_2) x_2 + & \cdots + \tau_n (u_{n + 1}) x_{n + 1} = 0
        \end{align}

        显然其一定有非平凡解，设为 $x_1 = a_1, \ldots, x_r = a_r, x_{r + 1} = \cdots = x_{n + 1} = 0 (a_i \neq 0)$，其使得不为零的 $a_i$ 个数最少。而考虑到解的倍数同样也是解，不妨设 $a_1 = 1_F$. 反证的出发点便是能够在此基础上构造出使得不为零的 $a_i$ 个数更少的解。  
        下证存在 $\sigma \in J$，使得 $x_1 = \sigma a_1, x_2 = \sigma a_2, \ldots, x_r = \sigma a_r, x_{r + 1} = \cdots = x_{n + 1} = 0$ 也是上述方程组的解，并且满足 $\sigma a_2 \neq a_2$。  
        根据轨道分解，诸 $\tau_i$ 中恰好存在一个（设为 $\tau_1$）是 $H$ 的代表元，即 $\tau_1 \in H$. 而 $u_1, u_2, \ldots, u_{n + 1} \in H'$，所以 $\tau_1(u_i) = u_i$，所以方程组的第一个方程表明 
        
        \[
            u_1 a_1 + u_2 a_2 + \cdots + u_{n + 1} a_{n + 1} = 0
        \]

        但是 $u_1, u_2, \ldots, u_{n + 1}$ 在 $J'$ 上是线性无关的，并且 $\{a_i\}$ 并不全为零，所以必然存在某个 $a_i$（设为 $a_2$）不属于 $J'$。于是存在 $\sigma \in J$ 使得 $\sigma a_2 \neq a_2$。  
        而后考虑如下的方程组

        \begin{align}
            \sigma \tau_1 (u_1) x_1 + \sigma \tau_1 (u_2) x_2 + & \cdots + \sigma \tau_1 (u_{n + 1}) x_{n + 1} = 0 \\
            \sigma \tau_2 (u_1) x_1 + \sigma \tau_2 (u_2) x_2 + & \cdots + \sigma \tau_2 (u_{n + 1}) x_{n + 1} = 0 \\
            & \cdots \\
            \sigma \tau_n (u_1) x_1 + \sigma \tau_n (u_2) x_2 + & \cdots + \sigma \tau_n (u_{n + 1}) x_{n + 1} = 0
        \end{align}

        因为 $\sigma$ 是一个自同构，所以 $x_1 = \sigma a_1, x_2 = \sigma a_2, \ldots, x_r = \sigma a_r, x_{r + 1} = \cdots = x_{n + 1} = 0$ 也是上述方程组的解。下面需要说明这两个方程组本质上是等价的，也就是要说明如下两点：  
        (1) $J = \bigsqcup_{i = 1}^n \sigma \tau_i H$;  
        (2) 若 $\xi$ 与 $\theta$ 是 $H$ 关于 $J$ 的同一个左陪集的两个元素，那么 $\xi(u_i) = \theta(u_i), i = 1, 2, \ldots, n + 1$。  
        考虑 $\varphi_\sigma: J \to J, \varphi_\sigma(\tau_i H) = \sigma \tau_i H$，证明 (1) 只需说明 $\varphi_\sigma$ 为双射即可。若 $\sigma \tau_i H = \sigma \tau_j H$，则 $(\sigma \tau_j)^{-1} \sigma \tau_i \in H$，即 $\tau_j^{-1} \tau_i \in H$，而考虑到 $J = \bigsqcup_{i = 1}^n \tau_i H$，即 $\tau_j^{-1} \tau_i \in H$ 等价于 $i = j$，所以 $\varphi_\sigma$ 是单射。而两个集合的元素个数相等，所以 $\varphi_\sigma$ 是满射。又 $\xi, \theta \in \tau_i H$，所以 $\xi = \tau_i \xi_0, \theta = \tau_i \theta_0$，其中 $\xi_0, \theta_0 \in H$，而 $u_i \in H'$，所以 $\xi(u_i) = \tau_i \xi_0(u_i) =  \tau_i u_i = \tau_i \theta_0(u_i) = \theta(u_i)$。  
        所以 $x_1 = \sigma a_1, x_2 = \sigma a_2, \ldots, x_r = \sigma a_r, x_{r + 1} = \cdots = x_{n + 1} = 0$ 也是第一个方程组的解。而解的差也是解，所以 $x_1 = a_1 - \sigma a_1, x_2 = a_2 - \sigma a_2, \ldots, x_r = a_r - \sigma a_r, x_{r + 1} = \cdots = x_{n + 1} = 0$ 也是第一个方程组的解。而 $a_1 = 1_F$，所以 $x_1 = 0$，且 $x_2 = a_2 - \sigma a_2 \neq 0$，所以这与第一个解使得不为零的 $a_i$ 个数最少相矛盾。所以 $[H':J'] \leqslant [J:H]$.

!!! success "引理"
    设 $F$ 是 $K$ 的一个扩域，$L$ 和 $M$ 是 $F$ 的两个中间域，且 $L \subset M$；$H$ 和 $J$ 是 $\operatorname{Aut}_K F$ 的两个子群，且 $H < J.$   
    (i) 如果 $L$ 是闭的且 $[M:L]$ 有限，则 $M$ 是闭的并且 $[L':M'] = [M:L]$；  
    (ii) 如果 $H$ 是闭的且 $[J:H]$ 有限，则 $J$ 是闭的并且 $[H':J'] = [J:H]$；  
    (iii) 如果 $F$ 是 $K$ 的一个有限维 Galois 扩张，那么所有的中间域以及对应的 Galois 群的子群都是闭的，且 $\lvert \operatorname{Aut}_K F \rvert = [F:K]$.  

    !!! tip "注记"
        注意到对 (ii) 而言令 $H = 1$ 便可以得到所有 Galois 群的有限子群都是闭的。

    ??? success "证明"
        (i) 注意到 $M \subset M'', L = L''$，并且运用前两个引理，可以得到 

        \[
            [M: L] \leqslant [M'': L] = [M'': L''] \leqslant [L': M'] \leqslant [M: L],
        \]

        也就是说 $M = M''$ 并且 $[L': M'] = [M: L].$  
        (ii) 同理，$J \subset J'', H = H''$，运用前两个引理，便有  

        \[
            [J: H] \leqslant [J'': H] = [J'': H''] \leqslant [H': J'] \leqslant [J: H],
        \]

        即 $J = J''$ 且 $[H': J'] = [J: H].$  
        (iii) 设 $E$ 是一个中间域，显然 $[E:K]$ 有限；因为 $F$ 是 Galois 扩张，所以 $K$ 是闭的，由 (i) 可知 $E$ 是闭的，并且 $[K':E'] = [E:K]$. 考虑 $E = F$，则 $\lvert \operatorname{Aut}_K F \rvert = [\operatorname{Aut}_K F : 1] = [K':F'] = [F:K]$ 是有限的。从而可知所有 $\operatorname{Aut}_K F$ 的子群$J$ 都是有限的，所以 $J$ 是闭的。

那么结合上闭中间域和 Galois 群的闭子群的一一对应，我们就能得到 Galois 理论基本定理的第 (i) 条。接下来我们来做 Galois 理论基本定理的第 (ii) 条的准备工作。设 $F$ 是 $K$ 的一个扩域，$E$ 是一个中间域，$E$ 被称为（关于 $K$ 和 $F$）**稳定的**(stable)，如果对于任意 $K$-自同态 $\sigma \in \operatorname{Aut}_K F$，$\sigma(E) = E$。显然 $\sigma^{-1}(E) = E$，这也就表明 $\sigma \mid_E$ 实际上是 $E$ 的一个 $K$-自同态，逆为 $\sigma^{-1} \mid_E$。接下来会证明对于有限维的情况来说，$E$ 是稳定的当且仅当 $E$ 是 $K$ 上 Galois 的。首先将正规子群与稳定中间域联系起来：

!!! success "引理"
    设 $F$ 是 $K$ 的一个扩域。  
    (i) 若 $E$ 是一个稳定中间域，则 $E' = \operatorname{Aut}_E F$ 是 $\operatorname{Aut}_K F$ 的正规子群；  
    (ii) 若 $H$ 是 $\operatorname{Aut}_K F$ 的一个正规子群，则 $H'$ 是一个稳定中间域.  

    ??? success "证明"
        (i) 考虑 $u \in E, \sigma \in \operatorname{Aut}_K F$，根据稳定性有 $\sigma (u) \in E$。对于任意的 $\tau \in E' = \operatorname{Aut}_E F$，有 $\tau \sigma (u) = \sigma (u)$，所以 $\sigma^{-1} \tau \sigma (u) = u$，即 $\sigma^{-1} \tau \sigma \in \operatorname{Aut}_E F$，从而 $E'$ 是 $\operatorname{Aut}_K F$ 的正规子群。  
        (ii) 考虑 $\sigma \in \operatorname{Aut}_K F, \tau \in H$，根据正规性有 $\sigma^{-1} \tau \sigma \in H$，所以对于任意的 $u \in H'$，有 $\sigma^{-1} \tau \sigma (u) = u$，即 $\tau \sigma (u) = \sigma (u)$。所以 $\sigma (u) \in H', \forall u \in H'$，即 $H'$ 是一个稳定中间域。

接下来的三条引理着重于稳定中间域，Galois 扩张和 Galois 群的关系：

!!! success "引理"
    设 $F$ 是 $K$ 的一个 Galois 扩张，$E$ 是一个稳定中间域，则 $E$ 在 $K$ 上是 Galois 的.  

    ??? success "证明"
        考虑 $u \in E - K$，因为 $F$ 在 $K$ 上是 Galois 的，所以存在 $\sigma \in \operatorname{Aut}_K F$ 使得 $\sigma(u) \neq u$，但是根据稳定性有 $\sigma \mid_E \in \operatorname{Aut}_E F$，从而 $E$ 在 $K$ 上是 Galois 的。

!!! success "引理"
    设 $F$ 是 $K$ 的一个扩域，$E$ 是一个中间域，并且 $E$ 在 $K$ 上是代数的且 Galois 的，那么 $E$ 是稳定的。  

    ??? success "证明"
        考虑 $u \in E$，因为 $E$ 在 $K$ 上是代数的，所以设 $f \in K[x]$ 是 $u$ 的极小多项式，并且令 $u = u_1$. $u_1, u_2, \ldots, u_r$ 是 $f$ 在 $E$ 中的所有互异的根，易知 $r \leqslant n = \operatorname{deg} f$。设 $\tau \in \operatorname{Aut}_K E$，则 $\tau$ 对 $\{u_i\}$ 的作用是一个置换，所以首一多项式 $g = \prod_{i = 1}^r (x - u_i)$ 的系数都被 $\tau$ 固定。又因为 $E$ 在 $K$ 上是 Galois 的，所以 $g \in K[x]$。而 $u = u_1$ 是 $g$ 的一个根，因此 $f \mid g$。又因为 $g$ 是首一的并且 $\operatorname{deg} g \leqslant \operatorname{deg} f$，所以 $f = g$，从而 $f$ 的所有根是互不相同并且全部落在 $E$ 中的。现在考虑 $\sigma \in \operatorname{Aut}_K F$，$\sigma(u)$ 也是 $f$ 的根，有 $\sigma (u) \in E$ ，所以 $E$ 是稳定的。

设 $F$ 是 $K$ 的一个扩域，$E$ 是一个中间域。考虑 $K$-自同态 $\tau \in \operatorname{Aut}_K E$，则 $\tau$ 被称为**可延拓**到 $F$ 上的，如果存在 $\sigma \in \operatorname{Aut}_K F$ 使得 $\sigma \mid_E = \tau$。显然所有可延拓的 $K$-自同态构成了 $\operatorname{Aut}_K E$ 的一个子群。接下来的引理说明稳定中间域和可延拓的关系：  

!!! success "引理"
    设 $F$ 是 $K$ 的一个扩域，$E$ 是一个稳定中间域，则商群 $\operatorname{Aut}_K F / \operatorname{Aut}_E F$ 同构于 $E$ 的所有可延拓的 $K$-自同态所构成的群.  

    ??? success "证明"
        因为 $E$ 是稳定的，所以 $\sigma \mapsto \sigma \mid_E$ 是一个 $\operatorname{Aut}_K F \to \operatorname{Aut}_K E$ 的群同态，并且像是所有 $E$ 的可延拓到 $F$ 上的 $K$-自同态组成的群，核是 $\operatorname{Aut}_E F$，根据群的第一同构定理可以得到结论。

有了这些引理的准备，我们便可以完成 Galois 理论基本定理的全部证明了。

!!! note "Galois 理论基本定理的证明"  
    (i) 已知闭中间域和 Galois 群的闭子群之间有一个一一对应，而且 Galois 扩张的中间域和对应 Galois 群的子群都是闭的，指数之间的关系也已证明过，所以 (i) 得证。  
    (ii) 因为 $E$ 是闭的，所以 $F$ 在 $E$ 上是 Galois 的。因为 $E$ 是 $K$ 的一个有限维扩张，所以也是一个代数扩张。从而，如果 $E$ 同时也是 $K$ 上 Galois 的，那么便可以得到 $E$ 是稳定的，对应有 $E' = \operatorname{Aut}_E F$ 是 $\operatorname{Aut}_K F$ 的正规子群。而如果 $E' = \operatorname{Aut}_E F$ 是 $\operatorname{Aut}_K F$ 的正规子群，那么 $E''$ 是一个稳定中间域，而又知道 Galois 扩张的中间域都是闭的，所以 $E'' = E$，即 $E$ 是稳定中间域，进而 $E$ 是 $K$ 上 Galois 的。  
    而考虑 $E$ 是一个 $K$ 上 Galois 的中间域，所以会有 $E'$ 在 $\operatorname{Aut}_K F$ 中是一个正规子群。由于 $E$ 和 $E'$ 是闭的，并且 $G' = K$，所以可以得到 $\lvert G/E' \rvert = [G:E'] = [E'':G'] = [E:K]$。而又知道 $G/E' = \operatorname{Aut}_K F / \operatorname{Aut}_E F$ 同构于 $\operatorname{Aut}_K E$ 的一个 $[E:K]$ 阶子群，但第一部分已经证明了 $\lvert \operatorname{Aut}_K E \rvert = [E:K]$，所以 $\operatorname{Aut}_K F / \operatorname{Aut}_E F \cong \operatorname{Aut}_K E$，即 (ii) 得证。

Galois 理论的现代发展主要归功于 Emil Artin，包括上面对于基本定理的证明思路也依赖于他，但他的基本对象是给定的域 $F$ 以及 $F$ 的一个自同构群 $G$，然后构建 $K$ 作为 $G$ 的固定域。  

!!! note "定理"
    (Artin) 设 $F$ 为域，$G$ 为 $F$ 的一个自同构群，$K$ 是 $G$ 在 $F$ 上的固定域，那么 $F$ 在 $K$ 上是 Galois 的。如果 $G$ 是有限的，则 $F$ 是 $K$ 的一个有限维 Galois 扩张，并且 $G$ 是对应的 Galois 群.  

    ??? note "证明"
        显然 $G$ 一定是 $\operatorname{Aut}_K F$ 的子群，如果 $u \in F - K$，则存在 $\sigma \in G$ 使得 $\sigma(u) \neq u$，所以 $\operatorname{Aut}_K F$ 的固定域实际上也就是 $K$，所以 $F$ 在 $K$ 上是 Galois 的。当 $G$ 是有限的时候，有 $[F:K] = [1':G'] \leqslant [G:1] = \lvert G \rvert$，因此 $F$ 是 $K$ 的一个有限维 Galois 扩张，此时对应有 $G = G''$。 而 $G' = K$，所以 $\operatorname{Aut}_K F = K' = G'' = G$，即 $G$ 是对应的 Galois 群。