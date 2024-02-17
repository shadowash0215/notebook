# 域扩张

!!! info "定义"
    如果域 $K$ 是域 $F$ 的子域，则称 $F$ 是 $K$ 的**扩域**(extension field)，或者叫做 $K$ 的**域扩张**(field extension).

如果 $F$ 是 $K$ 的扩域，不难看出 $1_K = 1_F$。此外 $F$ 是 $K$ 的向量空间，本章我们将 $K$-向量空间 $F$ 的维数表示为 $[F:K]$。按照 $[F:K]$ 是否有限，我们称 $F$ 是 $K$ 的**有限维扩张**(finite extension)或者**无限维扩张**(infinite extension)。

!!! note "定理"
    设 $F$ 是 $E$ 的扩域，$E$ 是 $K$ 的扩域，则 $[F:K] = [F:E][E:K]$. 此外，如果 $[F:E]$ 和 $[E:K]$ 都是有限的等价于 $[F:K]$ 也是有限的.  

!!! note "定理"
    设 $F$ 是域 $K$ 的扩域，$u, u_i \in F$，而 $X \subset F$, 则  
    (i) 子环 $K[u]$ 是 $\{f(u) \mid f \in K[x]\}$.  
    (ii) 子环 $K[u_1, \cdots, u_m]$ 是 $\{g(u_1, \cdots, u_m) \mid g \in K[x_1, \cdots, x_m]\}$.  
    (iii) 子环 $K[X]$ 是 $\{h(u_1, \cdots, u_n) \mid u_i \in X, n \in N^*, h \in K[x_1, \cdots, x_n]\}$.  
    (iv) 子域 $K(u)$ 是 $\left\{\frac{f(u)}{g(u)} = f(u)g(u)^{-1} \mid f, g \in K[x], g(u) \neq 0 \right\}$.  
    (v) 子域 $K(u_1, \cdots, u_m)$ 是 $\left\{\frac{h(u_1, \cdots, u_m)}{k(u_1, \cdots, u_m)} = h(u_1, \cdots, u_m)k(u_1, \cdots, u_m)^{-1} \mid h, k \in K[x_1, \cdots, x_m], h(u_1, \cdots, u_m) \neq 0 \right\}$.  
    (vi) 子域 $K(X)$ 是 $\left\{\frac{p(u_1, \cdots, u_n)}{q(u_1, \cdots, u_n)} = p(u_1, \cdots, u_n)q(u_1, \cdots, u_n)^{-1} \mid u_i \in X, n \in N^*, p, q \in K[x_1, \cdots, x_n], q(u_1, \cdots, u_n) \neq 0 \right\}$.  
    (vii) 对于每个 $v \in K(X)$(或 $v \in K[x]$)，均存在 $X$ 的有限子集 $X'$，使得 $v \in K(X')$(或 $v \in K[X']$).  

!!! info "定义"
    设 $F$ 是 $K$ 的扩域，$F$ 中的元素 $u$ 叫做在 $K$ 上是**代数的**(algebraic over $K$)，如果存在 $K[x]$ 的非零多项式 $f(x)$，使得 $f(u) = 0$. 否则，$u$ 叫做在 $K$ 上是**超越的**(transcendental over $K$). 如果 $F$ 中的每个元素都是在 $K$ 上是代数的，则称 $F$ 是 $K$ 的**代数扩张**(algebraic extension)，否则称 $F$ 是 $K$ 的**超越扩张**(transcendental extension).

下面的两个定理不计同构的刻画了所有单扩张。

!!! note "定理"
    (i) 设 $F$ 是 $K$ 的扩域，$u \in F$ 在 $K$ 上超越，则 $K(u) \cong K(x)$，且此同构在 $K$ 上的限制是恒等自同构.  
    (ii) 设 $F$ 是 $K$ 的扩域，$u \in F$ 在 $K$ 上代数，则  
    (a) $K(u) = K[u]$.  
    (b) $K(u) \cong K[x]/(f)$，其中 $f \in K[x]$ 是 $n$ 次首一多项式，其由条件 $f(u) = 0$ 和 $g(u) = 0(g \in K[x]) \Leftrightarrow f \mid g$ 所唯一确定.  
    (c) $[K(u):K] = n$.  
    (d) $\{1_K, u, u^2, \ldots, u^{n-1}\}$ 是 $K$ 上的向量空间 $K(u)$ 的一组基.  
    (e) $K(u)$ 中的每个元素都可以唯一的写成 $a_0 + a_1u + \cdots + a_{n-1}u^{n-1}(a_i \in K)$.  

!!! note "定理"
    设 $F$ 是 $K$ 的扩域，$u \in F$ 在 $K$ 上代数，则上述定理中的首一多项式 $f$ 称作 $u$ 的**不可约多项式**(irreducible polynomial)或者**极小多项式**(minimal polynomial). 而 $\operatorname{deg} f = [K(u):K]$ 称作 $u$ 在 $K$ 上的**次数**(degree).  

!!! example "示例"
    多项式 $x^3 - 3x - 1$ 在 $\mathbf{Q}$ 上是不可约的，且它有实数根 $u$. 由上述定理，$u$ 在 $\mathbf{Q}$ 上的次数是 $3$，且 $\{1, u, u^2\}$ 是 $\mathbf{Q}$ 上的向量空间 $\mathbf{Q}(u)$ 的一组基. 元素 $u^4 + 2u^3 + 3 \in \mathbf{Q}(u) = \mathbf{Q}[u]$ 可以表示为基元素的线性组合，方法是利用带余除法.  

    \[
        x^4 + 2x^3 + 3 = (x + 2)(x^3 - 3x - 1) + (3x^2 + 7x + 5).
    \]

    从而 

    \begin{align}
        u^4 + 2u^3 + 3 & = (u + 2)(u^3 - 3u - 1) + (3u^2 + 7u + 5). \\
                       & = (u + 2) \cdot 0 + (3u^2 + 7u + 5). \\
                       & = 3u^2 + 7u + 5.
    \end{align}

    $3u^2 + 7u + 5$ 的乘法逆元可以按下面的方法计算：因为 $x^3 - 3x - 1$ 在 $\mathbf{Q}$ 上是不可约的，从而多项式 $x^3 - 3x - 1$ 和 $3x^2 + 7x + 5$ 互素，所以存在多项式 $f(x), g(x) \in \mathbf{Q}[x]$，使得 $g(x)(x^3 - 3x - 1) + h(x)(3x^2 + 7x + 5) = 1$. 令 $x = u$，则 $g(u)(u^3 - 3u - 1) + h(u)(3u^2 + 7u + 5) = g(u) \cdot 0 + h(u)(3u^2 + 7u + 5) = h(u)(3u^2 + 7u + 5) = 1$. 从而 $3u^2 + 7u + 5$ 的乘法逆元是 $h(u)$. 多项式 $g(x)$ 和 $h(x)$ 可以用扩展的欧几里得算法计算出来：$g(x) = -\frac{7}{37}x + \frac{29}{111}, h(x) = \frac{7}{111}x^2 - \frac{26}{111}x + \frac{28}{111}$.

接下来就域同构的扩充进行一些讨论。考虑以下问题：

!!! question
    设 $E$ 是 $K$ 的扩域，$F$ 是 $L$ 的扩域，且 $\sigma: K \rightarrow L$ 是域同构，则在什么条件下可以将 $\sigma$ 扩充为域同构 $\tau: E \rightarrow F$?

下面就单扩张给出解答。回忆有关环的知识，若 $\sigma: R \rightarrow S$ 是一环同态，则映射 $R[x] \rightarrow S[x]$，$\sum_i r_ix^i \mapsto \sum_i \sigma(r_i)x^i$ 也是环同态，其是 $\sigma$ 的扩充。我们将此同态依然记作 $\sigma$，并且用 $\sigma f$ 表示 $f \in R[x]$ 的像元素。

!!! note "定理"
    设 $\sigma: K \rightarrow L$ 是域同构，$u$ 是 $K$ 的某扩域 $E$ 中的元素，$v$ 是 $L$ 的某扩域 $F$ 中的元素. 设以下两个条件中有一个是成立的：  
    (i) $u$ 在 $K$ 上超越，且 $v$ 在 $L$ 上超越.  
    (ii) $u$ 是不可约多项式 $f \in K[x]$ 的根，$v$ 是 $\sigma f \in L[x]$ 的根.  
    则 $\sigma$ 可以扩充为域同构 $\tau: K(u) \rightarrow L(v)$，且 $\tau u = v$.

!!! success "推论"
    设 $E$ 和 $F$ 都是 $K$ 的扩域，$u \in E$ 和 $v \in F$ 都在 $K$ 上代数. 则 $u$ 和 $v$ 是同一个不可约多项式的根当且仅当存在域同构 $\sigma: K(u) \rightarrow K(v)$，使得 $\sigma u = v$，且在 $K$ 上的限制是恒等自同构.

目前为止，我们都是预先给出扩域，讨论多项式在扩域中的根。下面的定理表明我们其实不需要预先给出扩域。  

!!! note "定理"
    若 $K$ 是域，$f \in K[x]$ 是 $n$ 次多项式，则存在 $K$ 的单扩张 $F = K(u)$，使得：  
    (i) $u \in F$ 是 $f$ 的根.  
    (ii) $[F:K] \leqslant n$，等号成立当且仅当 $f$ 在 $K[x]$ 中是不可约的.  
    (iii) 如果 $f$ 在 $K[x]$ 中是不可约的，则在不计 $K$-同构意义下，$F$ 是唯一的.

根据 (iii)，我们也称 $F$ 是将不可约多项式 $f$ 的一个根**添加**(adjoin) 到 $K$ 上得到的域。

!!! note "定理"
    若 $F$ 是 $K$ 的有限维扩张，则 $F$ 是 $K$ 上有限生成的代数扩张.

??? note "证明"
    设 $[F:K] = n$，$u \in F$，则 $n + 1$ 元集合 $\{1_K, u, u^2, \ldots, u^n\}$ 在 $K$ 上线性相关，从而存在 $a_i \in K$，使得 $a_0 + a_1u + \cdots + a_nu^n = 0$，且至少有一个 $a_i \neq 0$. 从而 $u$ 在 $K$ 上代数. 因为 $u$ 是 $F$ 中的任意一个元素，所以 $F$ 是 $K$ 上的代数扩张. 如果 $\{v_1, \ldots, v_m\}$ 是 $F$ 的一组基，则易见 $F = K(v_1, \ldots, v_m)$.  

!!! note "定理"
    若 $F$ 是 $K$ 的扩域，$X$ 是 $F$ 的子集，使得 $F = K(X)$，且 $X$ 中的每个元素都在 $K$ 上代数，则 $F$ 是 $K$ 上的代数扩张. 又若 $X$ 是有限集合，则 $F$ 是 $K$ 上的有限维扩张.

!!! note "定理"
    若 $F$ 是 $E$ 的代数扩张，$E$ 是 $K$ 的代数扩张，则 $F$ 是 $K$ 的代数扩张.

!!! note "定理"
    设 $F$ 是 $K$ 的扩域，$E$ 是 $F$ 中所有在 $K$ 上代数的元素构成的集合，则 $E$ 是 $F$ 的子域，且 $E$ 是 $K$ 在 $F$ 中的唯一最大代数扩张.