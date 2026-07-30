# The collision problem

## Problem statement

在碰撞问题中，给定一个黑盒函数 $f: \{1, \ldots, n\} \to \Sigma$，该函数被承诺要么是一对一，要么是二对一，目标是确定属于哪种情况. 为了使问题是良定的，必须有 $\lvert \Sigma \rvert \geq n$. 具体起见，考虑 $\Sigma = \{1, \ldots, n\}$. 以下将给出一个不依赖于 $\lvert \Sigma \rvert$ 的上界，下界则将处理 $\Sigma = \{1, \ldots, n\}$ 的情况.

将碰撞问题纳入形式化定义查询复杂度的框架下. 输入字母表为 $\Sigma$，输入是一个谕示机字符串 $x \in S_0 \cup S_1 \subset \Sigma^n$，其中

\begin{align*}
    S_0 &= \{ x \in \Sigma^n : \forall i \neq j, x_i \neq x_j \}, \\
    S_1 &= \{ x \in \Sigma^n : \forall i, \exists ! j \neq i, x_i = x_j \}.
\end{align*}

为了确定属于何种情况，需要计算函数 $\op{collision}: S_0 \cup S_1 \to \{0, 1\}$，当 $x \in S_b$ 时，$\op{collision}(x) = b$.

量子计算机无法为完全非结构化的问题提供加速，而虽然碰撞问题具有一定的结构，其量子查询复杂度也是 $\Theta(n^{1/3})$，仍然需要很多次查询. 即碰撞问题中的这种结构不足以实现指数级加速. 碰撞问题的结构还出现在 $\op{HSP}$ 中，如果隐藏子群的阶为 $r$，那么 $f$ 是 $r$ 对一的. 但是 $\op{HSP}$ 还具有额外的结构，这也解释了为什么其量子查询复杂度要小很多.

## Classical query complexity

先简要考虑碰撞问题的经典查询复杂度. 在二对一的函数中寻找碰撞的自然算法为随机查询索引，直到观测到一次碰撞为止. 对于两个独立的随机索引 $i, j \in \{1, \ldots, n\}$，有 $\op{Pr}(x_i = x_j) = 1/(n-1)$. 以这种方式查询 $m$ 个索引，就会有 $\binom{m}{2}$ 对索引，期望看到的碰撞次数为 $\binom{m}{2} / (n-1) \approx m^2 / (2n)$. 当 $m = \sqrt{n}$ 时，这个值为 $\Omega(1)$，所以期望能找到一次碰撞. 而使用二阶矩也能证明这种情况以常数概率发生. 

而实际上这就是最优的经典算法，因为在得到碰撞之前除了随机查询索引外没有更好的策略. 而依据并集约束，进行 $m$ 次查询后得到碰撞的概率至多为 $\binom{m}{2} / (n-1) = O(m^2/n)$，所以 $m = \Omega(\sqrt{n})$.

## Quantum algorithm

现在考虑量子算法. 一种是直接应用 Grover 算法，首先查询 $x_1$，然后在 $x_2, \ldots, x_n$ 中搜索与 $x_1$ 相同的元素，这种方法使用 $O(\sqrt{n})$ 次查询，因此不比上述经典算法更好，尽管其以非常不同的方式得到了相同的运行时间.

但是，可以将这种方法和最优经典算法的主要思想相结合来提高性能. 具体而言，首先查询 $m$ 个索引，这里并不在乎选择的方式，并检查其中是否存在碰撞，如果找到则终止；否则在剩下的 $n - m$ 个索引中搜索与前 $m$ 个索引之一相同的元素. 总体而言，这种方法的时间复杂度为 $m + O(\sqrt{(n - m)/m})$，通过取 $m = \Theta(n^{1/3})$，可以最小化该表达式，表明 $Q(\op{collision}) = O(n^{1/3})$.

这类似于之前见过的元素唯一性算法，不同之处在于元素唯一性问题中可能只存在唯一的碰撞，因此基本算法的单次运行只能以很小的概率成功. 解决这一问题的方法是执行振幅放大，而代价是更长的运行时间. 元素唯一性的最终算法运行时间为 $O(n^{3/4})$，结果证明是次优的. 相比之下，上述碰撞问题的算法结果是最优的.

该算法也使用了大量空间来存储最初查询的 $m = n^{1/3}$ 个元素. 而空间受限下碰撞问题的量子查询复杂度仍然是一个开放问题.

## Toward a quantum lower bound

正权重敌手方法在此处不足以解决下界问题，这是所谓的**属性测试障碍**（property-testing barrier）的结果：对于一个决策问题，如果其“是”实例输入字符串与“否”实例输入字符串仅在 $\varepsilon$ 比例的字符位置上不同，那么使用正权重敌手方法所能证明的最佳下界约为 $1/\varepsilon$. 对于碰撞问题，这只能证明常数下界. 

所以依然是应用多项式方法. 需要先将方法扩展到非二元输入字母表上，定义变量 $\delta_{ij}, i, j \in \{1, \ldots, n\}$ 满足

\[
    \delta_{ij} = \begin{cases}
        1 & x_i = j \\
        0 & \text{otherwise.}
    \end{cases}
\]

然后声称 $t$ 查询量子算法的接受概率是关于 $\{ \delta_{ij} \}$ 的一个次数至多为 $2t$ 的多重线性多项式. 证明方法类似于二元字母表的情况，假设使用模 $n$ 加法查询，其中 $\ket{i, j} \mapsto \ket{i, j + x_i}$，那么有

\begin{align*}
    \ket{i, j + x_i} &= \sum_k \delta_{i,k} \ket{i, j + k} \\
                     &= \sum_l \delta_{i, l - j} \ket{i, l}.
\end{align*}

所以进行一次查询时，每个振幅的次数增加至多为 $1$.

接下来的目标是得到一个简单的多项式，但又不能直接对 $\delta_{ij}$ 进行对称化，因为这样会破坏问题的结构. Aaronson 的最初想法是将接受概率表示为 $n$ 和 $r$ 的双变量多项式，其中函数是 $r$ 对一的. 但主要问题是需要 $r \mid n$，输入才会有意义. 这种方法给出了 $\Omega(n^{1/5})$ 的下界，Shi 进行改进并得到了 $\Omega(n^{1/3})$ 的最优下界.

## Constructing the functions

本部分描述 Kutin 后来提出的论证，其是目前已知的证明碰撞问题下界的最简方法，给出了紧的下界，且涵盖了值域为 $\{1, \ldots, n\}$ 的情况.

基本思想是考虑在部分定义域上为 $a$ 对一，而在其余定义域上为 $b$ 对一的函数. 称三元组 $(m, a, b)$ **有效**（valid），若 $m \in \{0, \ldots, n\}$，$a \mid m$，$b \mid (n - m)$. 定义输入 $x_i^{m, a, b}$ 如下：

\[
    x_i^{m, a, b} = \begin{cases}
        \lceil i/a \rceil & 1 \leq i \leq m \\
        n - \lfloor (n - i)/b \rfloor & m < i \leq n.
    \end{cases}
\]

在给定这样输入的基础上，可以通过对输入字母表和字符串的字符进行任意排列来获得一个输入族. 具体地说，对于 $\{1, \ldots, n\}$ 上的任意排列 $\sigma, \tau$，定义输入 $x^{\sigma \tau}$ 为 $x^{\sigma \tau}_i = \tau(x^{m, a, b}_{\sigma(i)})$，这便诱导了相应的二元变量 $\delta_{ij}^{\sigma \tau}$，其中 $\delta_{ij}^{\sigma \tau} = 1$ 当且仅当 $x^{\sigma \tau}_i = j$.

声称量子算法在面对这样输入时的接受概率为 $m, a, b$ 的一个多项式. 

!!! success "Lemma"
    设 $p(\{\delta_{ij}\})$ 是一个关于 $\delta_{ij}$ 的多项式，那么对于任意有效的三元组 $(m, a, b)$，令

    \[
        P(m, a, b) = \mathbb{E}_{\sigma, \tau}[ p(\{\delta_{ij}^{\sigma \tau}\}) ],
    \]

    那么 $P(m, a, b)$ 是 $m, a, b$ 的一个多项式，且 $\deg(P) \leq \deg(p)$.

    ???+ success "Proof"
        任何多项式 $p$ 都可以展开为如下形式的单项式之和：

        \[
            I_S(\{\delta_{ij}\}) = \prod_{j=1}^n \prod_{i \in S_j} \delta_{ij},
        \]

        其中 $S_1, \ldots, S_n$ 是 $\{1, \ldots, n\}$ 的不相交子集. 这个单项式只在 $\forall i \in S_j, x_i = j$ 时取值为 $1$，否则取值为 $0$，次数为 $s := \sum_j \lvert S_j \rvert$. 问题规约到处理 $p$ 为任一特定单项式的情况.

        对于任意输入 $x^{\sigma \tau}$，可以识别函数值中属于 $a$ 对一的部分和 $b$ 对一的部分的子集. 给定 $U \subset \{1, \ldots, n\}$，令 $X$ 表示事件：所有在 $U$ 中的函数值属于 $a$ 对一的部分，且所有不在 $U$ 中的函数值属于 $b$ 对一的部分. 更正式地说，对于所有满足 $S_j \neq \varnothing$ 的 $j \in \{1, \ldots, \frac{m}{a}\}$，有 $\tau(j) \in U$，且对于所有满足 $S_j \neq \varnothing$ 的 $j \in \{ n, n - 1, \ldots, n - \frac{n - m}{b} + 1 \}$，有 $\tau(j) \notin U$. 收集对应于事件 $X$ 的输入，有

        \begin{align*}
            P(m, a, b) &= \sum_{U \subset \{1, \ldots, n\}} \op{Pr}_\tau [X] \mathbb{E}_{\sigma, \tau} [ I_S(\{\delta_{ij}^{\sigma \tau}\}) \mid X ] \\
                       &= \sum_{U \subset \{1, \ldots, n\}} \op{Pr}_\tau [X] \op{Pr}_{\sigma, \tau} [\forall j, \forall i \in S_j, \delta_{ij}^{\sigma \tau} = 1 \mid X ].
        \end{align*}

        令 $u := \lvert U \rvert$，$t$ 为满足 $\lvert S_j \rvert \neq 0$ 的 $j$ 的个数，那么有

        \begin{align*}
            \op{Pr}_\tau [X] &= \frac{\frac{m}{a} (\frac{m}{a} - 1) \cdots (\frac{m}{a} - u + 1) \cdot \frac{n - m}{b} (\frac{n - m}{b} - 1) \cdots (\frac{n - m}{b} - (t - u) + 1) \cdot (n - t)!}{n!}, \\
                             &= \frac{\left(\frac{m}{a}\right)_u \left(\frac{n - m}{b}\right)_{t - u}}{(n)_t},
        \end{align*} 

        其中

        \[
            (n)_k := \frac{n!}{(n - k)!} = n (n - 1) \cdots (n - k + 1).
        \]

        这里分子有三部分组成：排列 $a$ 对一的部分中的 $u$ 个函数值，方式数为 $\left(\frac{m}{a}\right)_u$；排列 $b$ 对一的部分中的 $t - u$ 个函数值，方式数为 $\left(\frac{n - m}{b}\right)_{t - u}$；排列剩下的 $n - t$ 个函数值，方式数为 $(n - t)!$. 这是关于 $m, a, b$ 的一个有理函数，分子为 $m^t$，分母为 $a^u b^{t - u}$.

        而只要 $X$ 发生，$\op{Pr}_{\sigma, \tau} [\forall j, \forall i \in S_j, \delta_{ij}^{\sigma \tau} = 1]$ 的值与 $\sigma$ 无关，所以假设 $\sigma$ 是任何满足 $X$ 发生的排列，因此只需要计算索引 $i$ 的一致排列方法数. 对于某个 $j \in U$，排序索引 $i$ 使得 $x_i = j$ 的方法数为

        \[
            a(a - 1) \cdots (a - \lvert S_j \rvert + 1) = (a)_{\lvert S_j \rvert},
        \]

        类似地，对于 $j \notin U$，排序索引 $i$ 使得 $x_i = j$ 的方法数为 $(b)_{\lvert S_j \rvert}$. 而剩下的 $n - s$ 个索引可以任意排列，因此有

        \begin{align*}
            \op{Pr}_{\sigma, \tau} [\forall j, \forall i \in S_j, \delta_{ij}^{\sigma \tau} = 1 \mid X ] &= \frac{(n - s)! \prod_{j \in U} (a)_{\lvert S_j \rvert} \prod_{j \notin U} (b)_{\lvert S_j \rvert}}{n!} \\
            & = \frac{\prod_{j \in U} (a)_{\lvert S_j \rvert} \prod_{j \notin U} (b)_{\lvert S_j \rvert}}{(n)_s}.
        \end{align*}

        这是一个关于 $a, b$ 的次数为 $s$ 的多项式，并且能被 $a^u b^{t - u}$ 整除，所以 $P(m, a, b)$ 是一个关于 $m, a, b$ 的多项式，次数为 $t + s - u - (t - u) = s \leq \deg(p)$.

## Finishing the proof

!!! success "Paturi"
    设 $f \in \mathbb{R}[x]$，$a, b \in \mathbb{Z}$，$a < b$，$\xi \in [a, b]$. 如果存在常数 $c, d$ 使得

    - $\lvert f(i) \rvert \leq c$ 对所有整数 $i \in [a, b]$ 成立，
    - $\lvert f(\xi) - f(\lfloor \xi \rfloor) \rvert \geq d$，

    那么 $\deg(f) = \Omega(\sqrt{(\xi - a + 1)(b - \xi + 1)})$.

注意对任意 $\xi$，只要条件成立，都有 $\deg(f) = \Omega(\sqrt{b - a})$；而如果 $\xi$ 接近于中点，那么结果会更好，为 $\Omega(b - a)$. 并且依据连续性，可以使用

\[
    \lvert f(\xi - 1) - f(\xi) \rvert \geq d, \text{ for some } \xi \in [a + 1, b]
\]

替换第二个条件.

接下来证明碰撞问题的量子查询复杂度为 $\Omega(n^{1/3})$. 设 $p(\{\delta_{ij}\})$ 为 $t$-查询量子算法的接受概率多项式，该算法以最多 $1/3$ 的错误率解决碰撞问题，并定义 $P(m, a, b)$ 如上所述. 那么有 $t \geq \deg(P)/2$. 且 $P$ 有如下性质：

- $0 \leq P(m, 1, 1) \leq 1/3$
- $2/3 \leq P(m, 2, 2) \leq 1$
- 对所有有效的 $(m, a, b)$，$0 \leq P(m, a, b) \leq 1$

现在考虑一半为一对一，另一半为二对一的函数. 具体起见，令 $m = 2 \lfloor n/4 \rfloor$，因为 $n - m$ 也是偶数，所以 $(m, 1, 2)$ 是有效的. 考虑两种情况，取决于算法更可能将其称为“是”输入还是“否”输入.

首先假设 $P(m, 1, 2) \geq 1/2$. 令 $r$ 为满足 $\lvert P(m, 1, r) \rvert \geq 2$ 的最小正整数. 考虑多项式 $f(x) = P(m, 1, x)$，对于所有 $x \in \{1, \ldots, r - 1\}$，有 $-2 \leq f(x) \leq 2$，而 $\lvert f(1) - f(2) \rvert \geq 1/6$. 依据 Paturi 引理，取 $a = 1, b = r - 1, \xi = 2, c = 2, d = 1/6$，得到 $\deg(f) = \Omega(\sqrt{r})$. 而 $\deg(f) \leq \deg(P)$，所以 $\deg(P) = \Omega(\sqrt{r})$.

另一方面，考虑多项式 $f(x) = P(n-rx, 1, r)$，当 $x \in \mathbb{Z}$ 且 $rx \in \{0, \ldots, n\}$ 时，三元组 $(n-rx, 1, r)$ 也是有效的. 因此对于所有的整数 $x \in [0, \lfloor n/r \rfloor]$，都有 $0 \leq f(x) \leq 1$. 而 $\lvert f(\frac{(n - m)}{r}) \rvert = P(m, 1, r) \geq 2$，且 $\frac{(n - m)}{r}$ 大约在 $0$ 和 $\lfloor n/r \rfloor$ 的中点处. 依据 Paturi 引理，取 $a = 0, b = \lfloor n/r \rfloor, \xi = (n - m)/r, c = 1, d = 1$，得到 $\deg(f) = \Omega(n/r)$，所以 $\deg(P) = \Omega(n/r)$.

现在考虑 $P(m, 1, 2) < 1/2$ 的情况. 令 $r$ 为满足 $\lvert P(m, r, 2) \rvert \geq 2$ 的最小正整数. 与之前类似，依据 Paturi 引理，取 $a = 1, b = r - 1, \xi = 2, c = 2, d = 1/6$，得到 $\deg(P) = \Omega(\sqrt{r})$. 另一方面，考虑多项式 $f(x) = P(2rx, r, 2)$，对 $x \in \{0, \ldots, \lfloor n/2r \rfloor\}$，三元组 $(2rx, r, 2)$ 是有效的，所以 $0 \leq f(x) \leq 1$. 而 $\lvert P(m, r, 2) \rvert \geq 2$，$f(x)$ 从 $x = \lfloor m/2r \rfloor$ 到 $x = m/2r$ 跳变了至少 $1$，取 $a = 0, b = \lfloor n/2r \rfloor, \xi = m/2r, c = 1, d = 1$，得到 $\deg(P) = \Omega(n/r)$.

因为 $\deg(P) = \Omega(\sqrt{r})$ 且 $\deg(P) = \Omega(n/r)$，所以 $\deg(P) = \Omega(n/\deg(P)^2)$，解出 $\deg(P) = \Omega(n^{1/3})$.