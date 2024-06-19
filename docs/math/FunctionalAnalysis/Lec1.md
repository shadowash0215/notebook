# 度量空间

!!! info "度量空间"
    **度量空间**指对偶 $(X, d)$，其中 $X$ 是一个集合，$d$ 是定义在 $X$ 上的一个**度量**，即 $d$ 定义在 $X \times X$ 上，并且对所有 $x, y, z \in X$ 满足以下四条公理：  
        ($M_1$) $d$ 是实值、有限且非负的；  
        ($M_2$) $d(x, y) = 0$ 当且仅当 $x = y$；  
        ($M_3$) $d(x, y) = d(y, x)$；  
        ($M_4$) $d(x, z) \leq d(x, y) + d(y, z)$（三角不等式）。  
        $X$ 被称作 $(X, d)$ 的基集，$X$ 的元素叫作空间 $(X, d)$ 的点，$d(x, y)$ 被称作 $x$ 和 $y$ 之间的距离。$M_1 \sim M_4$ 被称为**度量公理**。

若取子集 $Y \subset X$ 并将 $d$ 限制在 $Y \times Y$ 上，则可以得到 $(X, d)$ 的一个子空间 $(Y, \tilde{d})$，其中 

\[
    \tilde{d} = d \vert_{Y \times Y}.
\]

$\tilde{d}$ 叫做 $d$ 在 $Y$ 上导出的度量。

## 度量空间的示例

1. 序列空间 $l^\infty$  
    取所有有界的复数序列的集合作为 $X$，也就是说，$X$ 中的每个元素都是形如  

    \[
        x = (\xi_1, \xi_2, \ldots) = (\xi_j)
    \]

    的复数序列，且对于 $j = 1, 2, \ldots$ 有

    \[
        \lvert x \rvert \leqslant c_x,
    \]

    其中 $c_x$ 是依赖于 $x$ 的实数，但是与 $j$ 无关。我们在 $X$ 上用

    \[
        d(x, y) = \sup_{j \in N} \lvert \xi_j - \eta_j \rvert
    \]

    来定义度量，其中 $y = (\eta_j) \in X$ 且 $N = \{1, 2, \ldots\}$. 这样得到的度量空间通常被记作 $l^\infty$。因为 $X$ 中的每个元素都是序列，所以 $l^\infty$ 是一个序列空间。

2. 函数空间 $C[a, b]$  
    我们取定义在闭区间 $J = [a, b]$ 上的所有连续实值函数 $x(t), y(t), \ldots$ 的集合作为基集 $X$，用

    \[
        d(x, y) = \max_{t \in J} \lvert x(t) - y(t) \rvert
    \]

    在 $X$ 上定义度量。这样得到的度量空间记为 $C[a ,b]$。因为 $C[a ,b]$ 的每个点都是 一个函数，所以它是一个函数空间。

3. 序列空间 $s$  
    这个空间的基集 $X$ 是所有（有界的或无界的）复数序列的集合，其度量 $d$ 定义为  

    \[
        d(x, y) = \sum_{j = 1}^{\infty} \dfrac{1}{2^j} \dfrac{\lvert \xi_j - \eta_j \rvert}{1 + \lvert \xi_j - \eta_j \rvert},
    \]

    其中 $x = (\xi_j), y = (\eta_j)$.  
    容易知道公理 $M_1 \sim M_3$ 是满足的，所以我们需要验证 $M_4$. 定义如下取值于 $R$ 的辅助函数  

    \[
        f(t) = \dfrac{t}{1 + t}.
    \]

    对其微分可得 $f'(t) = 1/(1 + t)^2$，而 $\forall t \in \mathbf{R}$ 均有 $f'(t) > 0$，也就是说 $f$ 是单调递增的，从而由

    \[
        \lvert a + b \rvert \leqslant \lvert a \rvert + \lvert b \rvert
    \]

    可以推出

    \[
        f(\lvert a + b \rvert) \leqslant f(\lvert a \rvert + \lvert b \rvert)
    \]

    将上述函数写出并应用关于数的三角不等式，便得到

    \[
        \dfrac{\lvert a + b \rvert}{1 + \lvert a + b \rvert} \leqslant \dfrac{\lvert a \rvert + \lvert b \rvert}{1 + \lvert a \rvert + \lvert b \rvert} = \dfrac{\lvert a \rvert}{1 + \lvert a \rvert + \lvert b \rvert} + \dfrac{\lvert a \rvert}{1 + \lvert a \rvert + \lvert b \rvert} \leqslant \dfrac{\lvert a \rvert}{1 + \lvert a \rvert} + \dfrac{\lvert b \rvert}{1 + \lvert b \rvert}.
    \]

    令 $a = \xi_j - \zeta_j, b = \zeta_j - \eta_j$，其中 $z = (\zeta_j)$，则 $a + b = \xi_j - \eta_j$，并且有

    \[
        \dfrac{\lvert \xi_j - \eta_j \rvert}{1 + \lvert \xi_j - \eta_j \rvert} \leqslant \dfrac{\lvert \xi_j - \zeta_j \rvert}{1 + \lvert \xi_j - \zeta_j \rvert} + \dfrac{\lvert \zeta_j - \eta_j \rvert}{1 + \lvert \zeta_j - \eta_j \rvert}.
    \]

    从而就有

    \[
        \sum_{j = 1}^{\infty} \dfrac{1}{2^j} \dfrac{\lvert \xi_j - \eta_j \rvert}{1 + \lvert \xi_j - \eta_j \rvert} \leqslant \sum_{j = 1}^{\infty} \dfrac{1}{2^j} \dfrac{\lvert \xi_j - \zeta_j \rvert}{1 + \lvert \xi_j - \zeta_j \rvert} + \sum_{j = 1}^{\infty} \dfrac{1}{2^j} \dfrac{\lvert \zeta_j - \eta_j \rvert}{1 + \lvert \zeta_j - \eta_j \rvert}.
    \]

    即所需要证明的三角不等式 $M_4$

    \[
        d(x, y) \leqslant d(x, z) + d(z, y),
    \]

    从而证明了 $s$ 是一个度量空间。

4. 有界函数空间 $B(A)$  
    每个元素 $x \in B(A)$ 都是定义在给定集合 $A$ 上的有界函数。度量定义为

    \[
        d(x, y) = \sup_{t \in A} \lvert x(t) - y(t) \rvert.
    \]

    在集合 $A$ 是区间 $A = [a, b] \subset \mathbf{R}$ 的情况下，$B(A)$ 也写作 $B[a, b]$。  
    易知 $M_1$ 和 $M_3$ 是满足的，$d(x, x) = 0$ 也是显然的。而当 $d(x, y) = 0$ 时，就有 $\forall t \in A$ 满足 $x(t) - y(t) = 0$，所以 $x = y$，因此 $M_2$ 也成立。而对于每个 $t \in A$，均有  

    \[
        \lvert x(t) - y(t) \rvert \leqslant \lvert x(t) - z(t) \rvert + \lvert z(t) - y(t) \rvert \leqslant \sup_{t \in A} \lvert x(t) - z(t) \rvert + \sup_{t \in A} \lvert z(t) - y(t) \rvert.
    \]

    因为右侧给出的上界值与 $t$ 无关，所以对 $\lvert x(t) - y(t) \rvert$ 可以取上界，也就得到 $M_4$。

5. 空间 $l^p$, Hilbert 序列空间 $l^2$  
    令 $p \geqslant 1$ 是一个固定的常数。依据定义，空间 $l^p$ 中的每个元素是使得 $\lvert \xi_1 \rvert^p + \lvert \xi_2 \rvert^p + \ldots$ 收敛的数列 $x = (\xi_1, \xi_2, \ldots) = (\xi_j)$。因此  

    \[
        \sum_{j = 1}^{\infty} \lvert \xi_j \rvert^p < \infty.
    \]

    $l^p$ 上的度量定义为  

    \[
        d(x, y) = \left( \sum_{j = 1}^{\infty} \lvert \xi_j - \eta_j \rvert^p \right)^{1/p},
    \]

    其中 $y = (\eta_j) \in l^p$.  
    在 $p = 2$ 的情况下，便得到了著名的 Hilbert 序列空间 $l^2$，其度量定义为

    \[
        d(x, y) = \sqrt{\sum_{j = 1}^{\infty} \lvert \xi_j - \eta_j \rvert^2}.
    \]

    下面证明 $l^p$ 是一个度量空间，整个过程如下：  
    $(a)$ 建立辅助不等式；  
    $(a) \Rightarrow (b)$ Hölder 不等式；  
    $(b) \Rightarrow (c)$ Minkowski 不等式；  
    $(c) \Rightarrow (d)$ 三角不等式。

    $(a)$ 令 $p > 1$ 并且定义 $q$ 满足

    \[
        \dfrac{1}{p} + \dfrac{1}{q} = 1,
    \]

    则把 $p$ 和 $q$ 称为**共轭指数**。由上可以得到

    \[
        1 = \dfrac{p + q}{pq}, \ pq = p + q, \ (p - 1)(q - 1) = 1.
    \]

    因此 $1/(p - 1) = q - 1$，所以若令 $u = t^{p - 1}$，便有 $t = u^{q - 1}$。令 $\alpha$ 和 $\beta$ 为两个任意的正数，因为 $\alpha \beta$ 为下图中矩形的面积，故通过积分可得不等式

    \[
        \alpha \beta \leqslant \int_0^\alpha t^{p - 1} \mathrm{d} t + \int_0^\beta u^{q - 1} \mathrm{d} u = \dfrac{\alpha^p}{p} + \dfrac{\beta^q}{q}. \enspace (*)
    \]

    当 $\alpha = 0$ 或 $\beta = 0$ 时，上式依然成立。

    \automata
        \node at (2.75, 1.5) {$1$};
        \node at (0.5, 1.25) {$2$};
        \node at (-0.2, -0.2) {$O$};
        \node at (4, -0.2) {$\alpha$};
        \node at (-0.2, 2) {$\beta$};
        \draw[->] (0, 0) -- (0, 4.2);
        \draw[->] (0, 0) -- (5.2, 0);
        \draw[-, very thin,color=gray] (0, 0) grid (5, 4);
        \draw[-, domain=0:5] plot(\x, {\x^0.8}) node[right] {$u = t^{p - 1}$};
        \draw[-, very thick] (4, 0) -- (4, 2) -- (0, 2);
        \draw[-] (0.5, 0) -- (0.5, 0.5^0.8);
        \draw[-] (1, 0) -- (1, 1^0.8);
        \draw[-] (1.5, 0) -- (1.5, 1.5^0.8);
        \draw[-] (2, 0) -- (2, 2^0.8);
        \draw[-] (2.5, 0) -- (2.5, 2.5^0.8);
        \draw[-] (3, 0) -- (3, 3^0.8);
        \draw[-] (3.5, 0) -- (3.5, 3.5^0.8);
        \draw[-] (4, 0) -- (4, 4^0.8);
        \draw[-] (0, 0.5) -- (0.5^1.25, 0.5);
        \draw[-] (0, 1) -- (1^1.25, 1);
        \draw[-] (0, 1.5) -- (1.5^1.25, 1.5);
        \draw[-] (0, 2) -- (2^1.25, 2);

    \automata
        \node at (1.75, 1) {$1$};
        \node at (1.5, 2.25) {$2$};
        \node at (-0.2, -0.2) {$O$};
        \node at (3, -0.2) {$\alpha$};
        \node at (-0.2, 3) {$\beta$};
        \draw[->] (0, 0) -- (0, 4.2);
        \draw[->] (0, 0) -- (5.2, 0);
        \draw[-, very thin,color=gray] (0, 0) grid (5, 4);
        \draw[-, domain=0:5] plot(\x, {\x^0.8}) node[right] {$u = t^{p - 1}$};
        \draw[-, very thick] (3, 0) -- (3, 3) -- (0, 3);
        \draw[-] (0.5, 0) -- (0.5, 0.5^0.8);
        \draw[-] (1, 0) -- (1, 1^0.8);
        \draw[-] (1.5, 0) -- (1.5, 1.5^0.8);
        \draw[-] (2, 0) -- (2, 2^0.8);
        \draw[-] (2.5, 0) -- (2.5, 2.5^0.8);
        \draw[-] (3, 0) -- (3, 3^0.8);
        \draw[-] (0, 0.5) -- (0.5^1.25, 0.5);
        \draw[-] (0, 1) -- (1^1.25, 1);
        \draw[-] (0, 1.5) -- (1.5^1.25, 1.5);
        \draw[-] (0, 2) -- (2^1.25, 2);
        \draw[-] (0, 2.5) -- (2.5^1.25, 2.5);
        \draw[-] (0, 3) -- (3^1.25, 3);

    图中的 $1$ $2$ 分别表示上一式中第一个积分和第二个积分的值。

    $(b)$ 令序列 $(\tilde{\xi}_j)$ 和 $(\tilde{\eta}_j)$ 分别满足

    \[
        \sum_{j = 1}^{\infty} \lvert \tilde{\xi}_j \rvert^p = 1, \ \sum_{j = 1}^{\infty} \lvert \tilde{\eta}_j \rvert^q = 1. \enspace (\Delta)
    \]

    令 $\alpha = \lvert \tilde{\xi}_j \rvert, \ \beta = \lvert \tilde{\eta}_j \rvert$，代入 $(*)$ 式则有

    \[
        \lvert \tilde{\xi}_j \tilde{\eta}_j \rvert \leqslant \dfrac{\lvert \tilde{\xi}_j \rvert^p}{p} + \dfrac{\lvert \tilde{\eta}_j \rvert^q}{q} 
    \]

    对该不等式的两端关于 $j$ 求和，便可以得到

    \[
        \sum_{j = 1}^{\infty} \lvert \tilde{\xi}_j \tilde{\eta}_j \rvert \leqslant \dfrac{1}{p} + \dfrac{1}{q} = 1. \enspace (**)
    \]

    现在取任意非零序列 $x = (\xi_j), y = (\eta_j) \in l^p$，并且令

    \[
        \tilde{\xi}_j = \dfrac{\lvert \xi_j \rvert}{\left( \sum_{k = 1}^{\infty} \lvert \xi_k \rvert^p \right)^{1/p}}, \ \tilde{\eta}_j = \dfrac{\lvert \eta_j \rvert}{\left( \sum_{m = 1}^{\infty} \lvert \eta_m \rvert^q \right)^{1/q}}.
    \]

    其满足 $(\Delta)$ 式，所以可以代入 $(**)$ 式，化简后可以得到

    \[
        \sum_{j = 1}^{\infty} \lvert \xi_j \eta_j \rvert \leqslant \left( \sum_{j = 1}^{\infty} \lvert \xi_j \rvert^p \right)^{1/p} \left( \sum_{j = 1}^{\infty} \lvert \eta_j \rvert^q \right)^{1/q}.
    \]

    这便是 Hölder 不等式。  
    若 $p = 2$ 则 $q = 2$，此时给出 Cauchy-Schwarz 不等式

    \[
        \sum_{j = 1}^{\infty} \lvert \xi_j \eta_j \rvert \leqslant \sqrt{\sum_{j = 1}^{\infty} \lvert \xi_j \rvert^2} \sqrt{\sum_{j = 1}^{\infty} \lvert \eta_j \rvert^2}.
    \]

    $(c)$ 现在证明 Minowski 不等式。其形式如下：

    \[
        \left( \sum_{j = 1}^{\infty} \lvert \xi_j + \eta_j \rvert^p \right)^{1/p} \leqslant \left( \sum_{j = 1}^{\infty} \lvert \xi_j \rvert^p \right)^{1/p} + \left( \sum_{j = 1}^{\infty} \lvert \eta_j \rvert^p \right)^{1/p}.
    \]

    其中 $x = (\xi_j), y = (\eta_j) \in l^p$，且 $p \geqslant 1$。  
    对于 $p = 1$ 的情况，其可以从数的三角不等式推导出来。所以令 $p > 1$，并且定义 $\xi_j + \eta_j = \omega_j$，则由数的三角不等式可得

    \[
        \lvert \omega_j \rvert^p = \lvert \xi_j + \eta_j \rvert \lvert \omega_j \rvert^{p - 1} \leqslant (\lvert \xi_j \rvert + \lvert \eta_j \rvert) \lvert \omega_j \rvert^{p - 1}. 
    \]

    上式两端对 $j$ 从 $1$ 到任一固定的 $n$ 求和，便得

    \[
        \sum \lvert \omega_j \rvert^p \leqslant \sum \lvert \xi_j \rvert \lvert \omega_j \rvert^{p - 1} + \sum \lvert \eta_j \rvert \lvert \omega_j \rvert^{p - 1}.
    \]

    对上式右端第一个和式应用 Hölder 不等式，可得

    \[
        \sum \lvert \xi_j \rvert \lvert \omega_j \rvert^{p - 1} \leqslant \left( \sum \lvert \xi_k \rvert^p \right)^{1/p} \left( \sum \lvert \omega_m \rvert^{(p - 1)q} \right)^{1/q}.
    \]

    因为 $p + q = pq$，所以有 $(p - 1)q = p$，从而上式右端可简化。对右端第二个和式做类似的处理，可得

    \[
        \sum \lvert \eta_j \rvert \lvert \omega_j \rvert^{p - 1} \leqslant \left( \sum \lvert \eta_k \rvert^p \right)^{1/p} \left( \sum \lvert \omega_m \rvert^p \right)^{1/q}.
    \]

    合在一起便得到
    
    \[
        \sum \lvert \omega_j \rvert^p \leqslant \left(\left( \sum \lvert \xi_k \rvert^p \right)^{1/p} + \left( \sum \lvert \eta_k \rvert^p \right)^{1/p}\right) \left( \sum \lvert \omega_m \rvert^p \right)^{1/q}.
    \]

    上式两侧同除 $\left( \sum \lvert \omega_j \rvert^p \right)^{1/q}$，因为 $1 - 1/q = 1/p$，所以可以得到

    \[
        \left(\sum \lvert \omega_j \rvert^p \right)^{1/p} \leqslant \left( \sum \lvert \xi_j \rvert^p \right)^{1/p} + \left( \sum \lvert \eta_j \rvert^p \right)^{1/p}.
    \]

    再令 $n \to \infty$，并且考虑右侧两个级数的收敛性（$x, y \in l^p$），所以左侧级数收敛，便得到了 Minkowski 不等式。

    $(d)$ 最后证明三角不等式。对于 $x = (\xi_j), y = (\eta_j), z = (\zeta_j) \in l^p$，依据数的三角不等式和 Minowski 不等式，可以得到

    \begin{align}
        d(x, y) = \left(\sum \lvert \xi_j - \eta_j \rvert^p \right)^{1/p} &{} \leqslant \left(\sum (\lvert \xi_j - \zeta_j \rvert + \lvert \zeta_j - \eta_j \rvert)^p \right)^{1/p} \\ &{} \leqslant \left(\sum \lvert \xi_j - \zeta_j \rvert^p \right)^{1/p} + \left(\sum \lvert \zeta_j - \eta_j \rvert^p \right)^{1/p} \\ &{} = d(x, z) + d(z, y).
    \end{align}

    这就证明了 $l^p$ 是一个度量空间。

6. 离散度量空间  
    任意取一集合 $X$，并且定义其上的离散度量为

    \[
        d(x, x) = 0, \ d(x, y) = 1(x \neq y).
    \]

    空间 $(X, d)$ 便被称为离散度量空间。虽然其很少被应用，但我们会用其来说明一些概念。

## 开集、闭集和邻域

首先考虑度量空间 $X = (X, d)$ 中的一些重要类型的子集。

!!! info "球和球面"
    给定点 $x_0 \in X$ 和 $r > 0$，定义如下三种类型的子集：  
    1. 开球 $B(x_0, r) = \{x \in X \vert d(x, x_0) < r\}$；  
    2. 闭球 $\tilde{B}(x_0, r) = \{x \in X \vert d(x, x_0) \leqslant r\}$；  
    3. 球面 $S(x_0, r) = \{x \in X \vert d(x, x_0) = r\}$.  
    由定义也可以得到 $S(x_0, r) = \tilde{B}(x_0, r) - B(x_0, r)$。
    !!! warning
        虽然我们在这里使用了欧几里得空间的术语，但其余度量空间的球和球面的性质并不是如同欧几里得空间的，比如离散度量空间，当 $r \neq 1$ 时，$S(x_0, r) = \varnothing$。

!!! info "开集和闭集"
    $M$ 为度量空间 $X$ 的一个子集，如果以 $M$ 中的每个点为球心，都可以作一个开球将 $M$ 完全包含在内，则称 $M$ 为**开集**。如果 $M$ 在 $X$ 中的余集是开集，则称 $M$ 为**闭集**。

半径为 $\varepsilon$ 的开球 $B(x_0, \varepsilon)$ 也被称为 $x_0$ 的 $\varepsilon$-邻域。所谓 $x_0$ 的**邻域**，是指 $X$ 含有 $x_0$ 的一个 $\varepsilon$-邻域的任意子集。

若 $M \subset X$ 是 $x_0$ 的一个邻域，则称 $x_0$ 是 $M$ 的**内点**。$M$ 的所有内点构成的集合称为 $M$ 的**内部**，记作 $\operatorname{Int}(M).$ $M$ 的内部是 $M$ 的最大开子集。

若把 $X$ 的所有开子集构成的集族记为 $\mathscr{T}$，则不难证明 $\mathscr{T}$ 满足以下性质：

$(T_1)$ $\varnothing \in \mathscr{T}, \ X \in \mathscr{T}$；  
$(T_2)$ $\mathscr{T}$ 中任意个成员之并仍在 $\mathscr{T}$ 中；  
$(T_3)$ $\mathscr{T}$ 中任意两个成员之交仍在 $\mathscr{T}$ 中。

$T_1 \sim T_3$ 是非常根本的性质，所以我们可以期待在推广到一般的情况下，这些性质仍然成立。所以，我们定义：给定集合 $X$ 和 $X$ 的满足公理 $T_1 \sim T_3$ 的子集族 $\mathscr{T}$，则称 $(X, \mathscr{T})$ 为**拓扑空间**，集合 $\mathscr{T}$ 叫做 $X$ 的一个**拓扑**。

!!! success "Collary"
    度量空间是拓扑空间。

在研究连续映射时，开集也起着重要的作用，而这里的连续性是微积分中连续性概念的一个自然推广，定义如下：

!!! info "连续映射"
    令 $X = (X, d)$ 和 $Y = (Y, \tilde{d})$ 是两个度量空间。若对于任意正数 $\varepsilon > 0$，存在一个正数 $\delta > 0$，使得对于任意 $x \in X$，只要 $d(x, x_0) < \delta$，就有 $\tilde{d}(Tx, Tx_0) < \varepsilon$，则称映射 $T: X \to Y$ 在点 $x_0$ 处是**连续的**。若 $T$ 在 $X$ 的每一点都是连续的，则称 $T$ 是**连续的**。

连续映射也可以用开集的术语表征如下：

!!! note "Theorem"
    度量空间 $X$ 到 $Y$ 的映射 $T: X \to Y$ 是连续的，当且仅当对于 $Y$ 的每个开集 $V$，其原像 $T^{-1}(V)$ 是 $X$ 的开集。

令 $M$ 是度量空间 $X$ 的一个子集，若点 $x_0 \in X$ 的每个邻域至少含有一个异于 $x_0$ 的点 $y \in M$，则 $x_0$ 叫作 $M$ 的**聚点**。$M$ 的所有点和所有聚点构成的集合称为 $M$ 的**闭包**，记作 $\overline{M}$. $M$ 的闭包是包含 $M$ 的最小闭集。

下面给出度量空间中的球的另一个不同寻常的性质：

!!! warning
    开球 $B(x_0, r)$ 的闭包 $\overline{B}(x_0, r)$ 不一定是闭球 $\tilde{B}(x_0, r)$。

!!! info "稠密集 可分空间"
    度量空间 $X$ 的子集 $M$ 称为 $X$ 的**稠密集**，如果 $\overline{M} = X$。若 $X$ 含有可数个稠密集，则称 $X$ 为**可分空间**。

!!! example
    $l^\infty$ 是不可分空间，$l^p(1 \leqslant p < \infty)$ 是可分空间。  
    ??? question "证明"
        令 $y = (\eta_j)$ 是 $l^\infty$ 中的一个序列，且 $\eta_j \in \{0, 1\}$。用 $y$ 来构造一个二进制表示的实数

        \[
            \hat{y} = \dfrac{\eta_1}{2^1} + \dfrac{\eta_2}{2^2} + \ldots.
        \]

        而区间 $[0, 1]$ 中的点集是不可数的，每个 $\hat{y} \in [0, 1]$ 皆有一个二进制表示，且不同的数有不同的二进制表示。再由 $y$ 与 $\hat{y}$ 的一一对应关系可知，形如 $y$ 的序列集合在 $l^\infty$ 中构成了一个不可数子集 $S$。有 $l^\infty$ 中的度量可知，$S$ 中的两个元素是不同的当且仅当它们的距离是 $1$。所以可以以 $S$ 中不同的元素 $y$ 为中心，半径为 $1/3$ 作多到不可数的互不相交的球。若 $M$ 是 $l^\infty$ 的任一稠密子集，则所作的每个不相交小球都将含有 $M$ 的点，从而说明 $M$ 是不可数的。因为 $M$ 是任意的稠密集，所以 $l^\infty$ 是不可分空间。
