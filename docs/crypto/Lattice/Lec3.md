# CVP 算法

!!! note "Review"
    1. ($\mathsf{CVP}_\gamma$, Search) 给定格基 $B \in \mathbb{Z}^{m \times n}$ 和点 $t \in \mathbb{Z}^m$，求点 $x \in \mathcal{L}(B)$ 使得 $\forall y \in \mathcal{L}(B)$，$\lVert x - t \rVert \leqslant \gamma \cdot \lVert y - t \rVert$.

    2. ($\mathsf{CVP}_\gamma$, Optimization) 给定格基 $B \in \mathbb{Z}^{m \times n}$ 和点 $t \in \mathbb{Z}^m$，求 $r \in \mathbb{Q}$ 使得 $d(t, \mathcal{L}(B)) \leqslant r \leqslant \gamma \cdot d(t, \mathcal{L}(B))$.

    3. ($\mathsf{CVP}_\gamma$, Decision) 给定格基 $B \in \mathbb{Z}^{m \times n}$、点 $t \in \mathbb{Z}^m$ 和 $r \in \mathbb{Q}$，判断 $d(t, \mathcal{L}(B)) \leqslant r$ 或 $d(t, \mathcal{L}(B)) > \gamma \cdot r$.

## 最近平面算法

\algorithm
    \caption{最近平面算法}
    \KwIn{格基 $B \in \mathbb{Z}^{m \times n}$，点 $t \in \mathbb{Z}^m$}
    \KwOut{向量 $x \in \mathcal{L}(B)$ 使得 $\lVert x - t \rVert \leqslant 2^{n/2} \cdot d(t, \mathcal{L}(B))$}
    \KwResult{}
    $\text{对 } B \text{ 运行 } \delta\text{-LLL 算法，取 } \delta = \frac{3}{4}$\;
    $b \gets t$\;
    $\text{for } j = n \text{ down to } 1 \text{ do}$\;
    $\quad b \gets b - c_j b_j, c_j = \lceil \langle b, b_j^* \rangle / \langle b_j^*, b_j^* \rangle \rfloor$\;
    $\text{输出 } t - b$\;

递归步骤：

1. 设 $s$ 为 $t$ 在 $\operatorname{span}(b_1, \ldots, b_n)$ 上的正交投影.

2. 寻找整数 $c$，使得平行超平面 $c b_n^* + \operatorname{span}(b_1, \ldots, b_{n-1})$ 离 $s$ 最近.

3. 令 $s' = s - c b_n$. 以 $s'$ 和 $\mathcal{L}(b_1, \ldots, b_{n-1})$ 为输入递归调用最近平面算法. 设 $x'$ 为答案.

4. 输出 $x = x' + c b_n$.

## 算法正确性

!!! success "Claim"
    1. 对任意 $t \in \operatorname{span}(B)$，最近平面算法输出的 $x \in \mathcal{L}(B)$ 满足 $\lVert x - t \rVert^2 \leqslant \frac{1}{4} \sum_{i=1}^n \lVert b_i^* \rVert^2$.

    2. 因为 $B$ 是 LLL 规约的，所以对任意 $t \in \operatorname{span}(B)$，最近平面算法输出的 $x \in \mathcal{L}(B)$ 满足 $\lVert x - t \rVert \leqslant \frac{1}{2} \cdot 2^{n/2} \lVert b_n^* \rVert$.

以上命题表明，当 $d(t, \mathcal{L}(B)) \geqslant \frac{1}{2} \cdot \lVert b_n^* \rVert$ 时，算法输出的是 $\mathsf{CVP}$ 的一个 $2^{n/2}$ 近似解. 但这并没有解决 $t$ 与格非常接近，或 $t \not \in \operatorname{span}(B)$ 的情况. 

!!! success "Lemma"
    对任意 $t \in \mathbb{Z}^m$，设 $y \in \mathcal{L}(B)$ 为 $t$ 的最近点. 那么以上算法输出的 $x \in \mathcal{L}(B)$ 满足 $\lVert x - t \rVert \leqslant 2^{n/2} \cdot \lVert y - t \rVert$.

    ??? success "Proof"
        在秩 $n$ 上进行数学归纳法. 首先需要归纳证明 $x$ 满足

        \[
            \lVert x - s \rVert \leqslant 2^{n/2} \cdot \lVert y - s \rVert,
        \]

        其中 $s$ 是 $t$ 在 $\operatorname{span}(B)$ 上的正交投影. 这便可以证明命题，因为

        \begin{align*}
            \lVert x - t \rVert^2 &= \lVert s - t \rVert^2 + \lVert x - s \rVert^2 \\
            &\leqslant \lVert s - t \rVert^2 + 2^n \cdot \lVert y - s \rVert^2 \\
            &\leqslant 2^n (\lVert s - t \rVert^2 + \lVert y - s \rVert^2) \\
            &= 2^n \cdot \lVert y - t \rVert^2.
        \end{align*}

        讨论两种情况.

        1. $\lVert s - y \rVert \leqslant \frac{\lVert b_n^* \rVert}{2}$. 这样便有 $y \in c b_n^* + \operatorname{span}(b_1, \ldots, b_{n-1})$，因为其他超平面到 $s$ 的距离至少为 $\frac{\lVert b_n^* \rVert}{2}$. 直观上，这说明第二步中选择的超平面是正确的，所以可以获得 $y' = y - c b_n \in \mathcal{L}(b_1, \ldots, b_{n-1})$. 依据归纳假设，

        \begin{align*}
            \lVert x - s \rVert &= \lVert x' - s' \rVert \\
            &\leqslant 2^\frac{n-1}{2} \cdot \lVert y' - s' \rVert \\
            &= 2^\frac{n-1}{2} \cdot \lVert y - s \rVert \\
            &\leqslant 2^\frac{n}{2} \cdot \lVert y - s \rVert.
        \end{align*}

        2. $\lVert s - y \rVert > \frac{\lVert b_n^* \rVert}{2}$. 这说明第二步中选择的超平面并不正确，但依据命题依然可以得到

        \[
            \lVert s - x \rVert \leqslant \frac{1}{2} \cdot 2^{n/2} \lVert b_n^* \rVert < 2^{n/2} \cdot \lVert s - y \rVert.
        \]