# Appendix

## Group Theory

### Representations

$M_n$ 表示 $n \times n$ 复矩阵集合，群 $G$ 的表示 $\rho$ 为将 $G$ 映射到矩阵群的函数，并且保持乘法结构，即 $\rho(g_1 g_2) = \rho(g_1) \rho(g_2)$ 对于任意 $g_1, g_2 \in G$ 成立. 如果表示 $\rho$ 将元素都映射 $M_n$ 中，则称其有维数 $d_\rho = n$.

#### Equivalence and reducibility

!!! note "Theorem"
    任何矩阵群总和一个酉矩阵群同构.

矩阵群 $G \subset M_n$ 的特征是定义为 $\chi(g) = \op{tr}{g}, g \in G$ 的函数，满足：

- $\chi(I) = n$；

- $\abs{\chi(g)} \leq n$；

- $\chi(g) = n$ 表明 $g = e^{\i \theta} I$；

- $\chi$ 在 $G$ 的任何共轭类上是常数；

- $\chi(g^{-1}) = \chi^*(g)$；

- $\forall g, \chi(g)$ 是代数数.

矩阵群 $G$ 被称为完全可约的，如果其等价于矩阵群 $H$，$H$ 中的每个矩阵都是分块对角形式的. 若不存在，则该矩阵群是不可约的.

!!! success "Schur's Lemma"
    设 $G \subset M_n$ 和 $H \subset M_k$ 有相同的阶. 若存在 $k \times n$ 的矩阵 $S$ 使得 $Sg_i = h_i S$ 对于任意 $g_i \in G, h_i \in H$ 成立，那么要么 $S = O$，要么 $k = n$ 且 $S$ 是可逆方阵.

!!! note "Theorem"
    矩阵群 $G$ 不可约等价于

    \[
        \frac{1}{\lvert G \rvert} \sum_{g \in G} \lvert \chi(g) \rvert^2 = 1.
    \]

#### Orthogonality

!!! note "Fundamental theorem"
    每个群有 $r$ 个不可约表示，其中 $r$ 是 $G$ 的共轭类个数. 若 $\rho^p \in M_{d_\rho}$ 和 $\rho^q$ 是其中两个，那么矩阵元满足正交条件

    \[
        \sum_{g \in G} [\rho^p(g)]^{-1}_{ij} [\rho^q(g)]_{kl} = \frac{\lvert G \rvert}{d_\rho} \delta^{pq} \delta_{il} \delta_{jk}.
    \]

## Number Theory

### Reduction of factoring to order-finding

!!! note "Theorem"
    设 $N$ 是 $L$ 位的合数，$x$ 是 $x^2 = 1 \pmod{N}$ 的非平凡解，且 $1 \leq x \leq N$，那么 $\gcd(x - 1, N)$ 和 $\gcd(x + 1, N)$ 中至少有一个是 $N$ 的非平凡因数，并且可以在 $O(L^3)$ 的时间复杂度内计算出来.

    ???+ note "Proof"
        因为 $x^2 = 1 \pmod{N}$，所以 $N$ 整除 $x^2 - 1 = (x - 1)(x + 1)$，即 $N$ 与 $x - 1$ 或 $x + 1$ 有公因子. 而 $x$ 是非平凡解，所以 $1 < x < N - 1$，$x - 1 < x + 1 < N$，公因子不会是 $N$ 本身. 所以可以使用 Euclid 算法在 $O(L^3)$ 的时间复杂度内计算出 $\gcd(x - 1, N)$ 和 $\gcd(x + 1, N)$，至少其中之一为 $N$ 的非平凡因子.

!!! success "Lemma"
    设 $p$ 为奇素数，$2^d$ 是整除 $\varphi(p^\alpha)$ 的最大的 $2$ 的次幂，那么随机选择 $\mathbb{Z}_{p^\alpha}^*$ 中的元素，其模 $p^\alpha$ 的阶被 $2^d$ 整除的概率恰好为 $1/2$.

    ???+ success "Proof"
        因为 $\varphi(p^\alpha) = p^{\alpha - 1}(p - 1)$ 为偶数，所以 $d \geq 1$. 而 $\mathbb{Z}_{p^\alpha}^*$ 是循环群，设生成元为 $g$，那么每个元素都可以写成 $g^k \pmod{p^\alpha}$ 的形式，其中 $k$ 为 $1$ 到 $\varphi(p^\alpha)$ 的整数. 设 $r$ 为 $g^k$ 模 $p^\alpha$ 的阶，考虑两种情况：

        - $k$ 是奇数：从 $g^{kr} = 1 \pmod{p^\alpha}$ 可以得到 $\varphi(p^\alpha) \mid kr$，进而有 $2^d \mid r$.

        - $k$ 是偶数：可以得到

            \[
                g^{k\varphi(p^\alpha)/2} = (g^{\varphi(p^\alpha)})^{k/2} = 1^{k/2} = 1 \pmod{p^\alpha}.
            \]

            所以 $r \mid \varphi(p^\alpha)/2$，进而 $2^d \not \mid r$.

!!! note "Theorem"
    设 $N = p_1^{\alpha_1} \cdots p_m^{\alpha_m}$ 是一个正奇合数的质因数分解，$x$ 是随机选择的满足 $1 \leq x \leq N - 1$ 且与 $N$ 互质的整数，设 $r$ 为 $x$ 模 $N$ 的阶，那么

    \[
        p(r \text{ is even and } x^{r/2} \neq -1 \pmod{N}) \geq 1 - \frac{1}{2^{m - 1}}.
    \]

    ???+ note "Proof"
        将证明

        \[
            p(r \text{ is odd or } x^{r/2} = -1 \pmod{N}) \leq \frac{1}{2^{m - 1}}.
        \]

        依据中国剩余定理，从 $\mathbb{Z}_N^*$ 中随机选取 $x$ 等价于独立随机的从每个 $\mathbb{Z}_{p_j^{\alpha_j}}$ 中选取 $x_j$，并且对每个 $j$ 都有 $x = x_j \pmod{p_j^{\alpha_j}}$. 设 $r_j$ 为 $x_j$ 模 $p_j^{\alpha_j}$ 的阶，$2^{d_j}$ 是整除 $r_j$ 的最大的 $2$ 的次幂，而 $2^d$ 是整除 $r$ 的最大的 $2$ 的次幂. 接下来将证明如果 $r$ 是奇数或 $x^{r/2} = -1 \pmod{N}$，就需要所有的 $d_j$ 取相同的值. 

        1. 考虑 $r$ 是奇数，因为 $r_j \mid r$，所以有 $d_j = 0$.

        2. 考虑 $r$ 为偶数且 $x^{r/2} = -1 \pmod{N}$，所以 $x^{r/2} = -1 \pmod{p_j^{\alpha_j}}$ 对所有 $j$ 都成立. 进而有 $r_j \not \mid r/2$，且 $r_j \mid r$，所以 $d_j = d$.

        引理的作用实际上是 $d_j$ 等于任何值的概率都小于等于 $1/2$，所以两种情况的概率都不会超过 $\frac{1}{2^m}$，而两种情况是独立的，所以概率不会超过为 $\frac{1}{2^{m - 1}}$，完成证明.

### Continued fractions

实数连续统和整数之间存在诸多联系，其中一个精彩示例便是连分数理论. 连分数的核心思想便是只用整数描述实数. 

有限简单连分数由正整数序列 $a_0, a_1, \ldots, a_N$ 描述，

\[
    [a_0, \ldots, a_N] \equiv a_0 + \cfrac{1}{a_1 + \cfrac{1}{\cdots + \cfrac{1}{a_N}}}.
\]

并定义其第 $n$ 个渐进分数为 $[a_0, \ldots, a_n]$.

!!! note "Theorem"
    设 $x$ 是大于等于 $1$ 的有理数，那么其有连分数表示 $x = [a_0, a_1, \ldots, a_N]$，可通过连分数算法求得.

而通过放宽对 $a_0$ 的限制，可以消除 $x \geq 1$ 的限制. 连分数算法唯一的歧义出现在整数的拆分，即 $a_n = a_n$ 或 $a_n = (a_n - 1) + \frac{1}{1}$ 两种等效表示，这便允许我们自由选择收敛项数是奇数还是偶数.

!!! note "Theorem"
    设 $a_0, \ldots, a_N$ 是正整数序列，那么

    \[
        [a_0, \ldots, a_n] = \frac{p_n}{q_n},
    \]

    其中 $p_n, q_n$ 是满足如下条件产生的实数：

    \begin{gather*}
        p_0 \equiv a_0, q_0 \equiv 1; \\
        p_1 \equiv 1 + a_1 a_0, q_1 \equiv a_1; \\
        p_n \equiv a_n p_{n-1} + p_{n-2}, q_n \equiv a_n q_{n-1} + q_{n-2}, \quad 2 \leq n \leq N.
    \end{gather*}

    ???+ note "Proof"
        采用数学归纳法. $n = 0, 1, 2$ 的情况自行验证. 依据定义，$n \geq 3$ 时有

        \[
            [a_0, \ldots, a_n] = [a_0, \ldots, a_{n - 2}, a_{n - 1} + \frac{1}{a_n}].
        \]

        运用归纳假设，设右侧连分数的渐进分数序列表示为 $\tilde{p}_j/\tilde{q}_j$，则有

        \[
            [a_0, \ldots, a_{n - 2}, a_{n - 1} + \frac{1}{a_n}] = \frac{\tilde{p}_{n - 1}}{\tilde{q}_{n - 1}}.
        \]

        而显然有 $\tilde{p}_{n - 3} = p_{n - 3}, \tilde{q}_{n - 3} = q_{n - 3}, \tilde{p}_{n - 2} = p_{n - 2}, \tilde{q}_{n - 2} = q_{n - 2}$，因此有

        \begin{align*}
            \frac{\tilde{p}_{n - 1}}{\tilde{q}_{n - 1}} & = \frac{(a_{n - 1} + \frac{1}{a_n}) \tilde{p}_{n - 2} + \tilde{p}_{n - 3}}{(a_{n - 1} + \frac{1}{a_n}) \tilde{q}_{n - 2} + \tilde{q}_{n - 3}} \\
            & = \frac{(a_{n - 1} p_{n - 2} + p_{n - 3}) + \frac{p_{n - 2}}{a_n}}{(a_{n - 1} q_{n - 2} + q_{n - 3}) + \frac{q_{n - 2}}{a_n}} \\
            & = \frac{a_n p_{n - 1} + p_{n - 2}}{a_n q_{n - 1} + q_{n - 2}} \\
            & = \frac{p_n}{q_n}.
        \end{align*}

        所以

        \[
            [a_0, \ldots, a_n] = \frac{p_n}{q_n}.
        \]

对于有理数 $x = p/q > 1$，需要多少个 $a_n$ 的值才能确定其连分数展开？设 $a_0, \ldots, a_N$ 为正整数序列，从 $p_n$ 和 $q_n$ 的定义可知，$\{p_n\}$ 和 $\{q_n\}$ 都是递增序列，所以 $p_n = a_n p_{n - 1} + p_{n - 2} \geq 2 p_{n - 2}$，同理 $q_n = a_n q_{n - 1} + q_{n - 2} \geq 2 q_{n - 2}$，因此有 $p_n, q_n \geq 2^{\lfloor n/2 \rfloor}$，进而 $p \geq q \geq 2^{\lfloor N/2 \rfloor}$，$N = O(\log (p))$. 所以如果 $x = p/q$ 是有理数，且 $p, q$ 都是 $L$ 位整数，那么 $x$ 的连分数展开可以在 $O(L^3)$ 的时间复杂度内完成.

!!! note "Theorem"
    设 $x$ 为有理数，且 $p/q$ 也是有理数，满足

    \[
        \abs{\frac{p}{q} - x} \leq \frac{1}{2q^2},
    \]

    则 $p/q$ 是 $x$ 的连分数的一个渐进分数.

    ???+ note "Proof"
        设 $[a_0, \ldots, a_n]$ 是 $p/q$ 的连分数展开，$[a_0, \ldots, a_j] = \frac{p_j}{q_j}$，显然 $p/q = p_n/q_n$. 定义 $\delta$ 为

        \[
            x \equiv \frac{p}{q} + \frac{\delta}{2q_n^2},
        \]

        所以 $\abs{\delta} < 1$. 定义 $\lambda$ 为

        \[
            \lambda \equiv 2\left(\frac{q_np_{n - 1} - p_nq_{n - 1}}{\delta}\right) - \frac{q_{n - 1}}{q_n}.
        \]

        其满足

        \[
            x = \frac{\lambda p_n + p_{n - 1}}{\lambda q_n + q_{n - 1}}.
        \]

        所以 $x = [a_0, \ldots, a_n, \lambda]$. 选择 $n$ 为偶数的表示形式，则有

        \[
            \lambda = \frac{2}{\delta} - \frac{q_{n - 1}}{q_n}.
        \]

        依据 $\{q_n\}$ 的递增性，有

        \[
            \lambda \geq 2 - 1 = 1.
        \]

        所以 $\lambda$ 是一个大于 $1$ 的有理数，其有简单有限连分数表示形式 $[b_0, b_1, \ldots, b_m]$，所以 $[a_0, \ldots, a_n, b_0, b_1, \ldots, b_m]$ 是 $x$ 的一个简单有限连分数表示形式，且 $p/q$ 为渐进分数.