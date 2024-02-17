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
    域 $H'$ 被称作 $H$ 在 $F$ 上的**不动域**(fixed field).

!!! info "定义"
    设 $F$ 是 $K$ 的一个扩域，并且 Galois 群 $\operatorname{Aut}_K F$ 的不动域是 $K$ 自身，则称 $F$ 是 $K$ 的一个 **Galois 扩张**(Galois extension)，或称 $F$ 在 $K$ 上是 **Galois 的**.

!!! tip "注记"
    $F$ 在 $K$ 上是 Galois 的等价于对于任一 $u \in F - K$，均存在 $\sigma \in \operatorname{Aut}_K F$ 使得 $\sigma(u) \neq u$. 如果 $F$ 是 $K$ 的任意扩张，而 $K_0$ 是 $\operatorname{Aut}_K F$ 的不动域，则 $F$ 在 $K_0$ 上是 Galois 的，且 $K \subset K_0$，$\operatorname{Aut}_{K_0} F = \operatorname{Aut}_K F$.

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

上面这个定理是我们证明 Galois 理论基本定理的关键。但想让它发挥作用我们还需要证明在有限维 Galois 代数扩张中所有的中间域和 Galois 群的子群都是闭的。以下先证明一些技术型的引理，它们能让我们估计各种相对维数：

!!! success "引理"
    设 $F$ 是 $K$ 的一个扩域，$L$ 和 $M$ 是 $F$ 的两个中间域，且 $L \subset M$. 如果 $[M:L]$ 有限，则 $[L':M'] \leqslant [M:L]$. 特别地，如果 $[F:K]$ 有限，则 $\lvert \operatorname{Aut}_K F \rvert \leqslant [F:K]$.