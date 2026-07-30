# Span programs and formula evaluation

生成程序（Span Programs）与量子敌手方法密切相关，并且可以用来证明广义敌手方法实际上在常数因子内刻画了量子查询复杂度. 简单起见，只考虑布尔函数 $f: S \subset \{0, 1\}^n \to \{0, 1\}$ 的情况，这种情况下的许多考量可以推广到其他类型的函数.

## The dual of the adversary method

敌手方法定义了

\[
    \op{Adv}^\pm(f) = \max_{\Gamma} \frac{\lVert \Gamma \rVert}{\max_{i \in [n]} \lVert \Gamma_i \rVert},
\]

使得 $Q(f) = \Omega(\op{Adv}^\pm(f))$. 虽然从上述表达式不能立即看出，但可以证明 $\op{Adv}^\pm(f)$ 实际上是一个**半定规划**（SDP）问题的值，这是一种优化问题，在线性和半正定约束下优化线性目标函数. 

SDP 的一个有用特性是其能被高效求解，所以可以用来找到固定函数的最优敌手下界，但这通常并不能提供确定渐进量子查询复杂度的策略. 

另一个关键特性是 SDP 对偶性：对每一个表述为最大化问题的原始 SDP，都存在一个对偶 SDP，其为最小化问题. 原始 SDP 的可行解给出下界，而对偶 SDP 的可行解给出上界. SDP 满足弱对偶性，即原始问题的最优值小于等于对偶问题的最优值；并且几乎所有的 SDP 都满足强对偶性，即原始问题和对偶问题的最优值相等.

对偶问题的变量可以看作一组向量 $\ket{v_{x, i}} \in \mathbb{C}^d$，其中 $x \in S$ 且 $i \in [n]$. 对于 $b \in \{0, 1\}$，定义 **$b$-复杂度**（$b$-complexity）为

\[
    C_b = \max_{x \in f^{-1}(b)} \sum_{i=1}^n \lVert \ket{v_{x, i}} \rVert^2.
\]

因为强对偶性成立，所以有：

!!! note "Theorem"
    对于任意函数 $f: S \subset \{0, 1\}^n \to \{0, 1\}$，有

    \[
        \op{Adv}^\pm(f) = \min_{\{\ket{v_{x, i}}\}} \max \{ C_0, C_1 \},
    \]

    其中最小化遍历所有满足如下约束的正整数 $d$ 和向量集合 $\{\ket{v_{x, i}} \in \mathbb{C}^d : x \in S, i \in [n]\}$：

    \[
        \sum_{i: x_i \neq y_i} \innerproduct{v_{x, i}}{v_{y, i}} = 1 - \delta_{f(x), f(y)}, \quad \forall x \neq y.
    \]

通过构造敌手对偶问题的解对最佳可能的敌手下界进行上界估计. 但也可以从敌手对偶问题的解构造一个算法，从而给出量子查询复杂度本身的上界. 

观察到，如果对于所有 $x \in f^{-1}(0)$，令 $\ket{v_{x, i}} \to \alpha \ket{v_{x, i}}$，并且对于所有 $y \in f^{-1}(1)$，令 $\ket{v_{y, i}} \to \ket{v_{y, i}} / \alpha$，则约束条件依然成立，但会将 $C_0$ 和 $C_1$ 分别变为 $\alpha^2 C_0$ 和 $C_1 / \alpha^2$. 通过选择 $\alpha = (C_1 / C_0)^{1/4}$，可以使得两个复杂度相等，从而得到

\[
    \op{Adv}^\pm(f) = \min_{\{\ket{v_{x, i}}\}} \sqrt{C_0 C_1}.
\]

$f(x) = f(y)$ 的约束实际上可以被移除，并且不会改变优化问题的值；但对于非布尔函数，类似地松弛会损失一个严格处于 $[1, 2]$ 范围内的常数因子. 松弛的原理如下：假设存在一个向量集合 $\{\ket{v_{x, i}} : x \in S, i \in [n]\}$ 满足 $f(x) \neq f(y)$ 时的约束条件，但不满足 $f(x) = f(y)$ 时的约束，那么只需令 $\ket{v'_{x, i}} = \ket{v_{x, i}} \ket{x_i \oplus f(x)}$. 这样就有 $\lVert \ket{v'_{x, i}} \rVert = \lVert \ket{v_{x, i}} \rVert$，并且对于 $x_i \neq y_i$ 的项，如果 $f(x) \neq f(y)$，则 $\innerproduct{v'_{x, i}}{v'_{y, i}} = \innerproduct{v_{x, i}}{v_{y, i}}$；否则 $\innerproduct{v'_{x, i}}{v'_{y, i}} = 0$. 

## Span programs

敌手方法的对偶等价于一种称为生成程序的线性代数计算模型. 一个针对函数 $f: \{0, 1\}^n \to \{0, 1\}$ 的生成程序包含：

- 一个目标向量 $\ket{t} \in \mathbb{C}^D$；

- 输入向量集 $I_{i, b} \subset \mathbb{C}^D$，其中 $i \in [n]$ 且 $b \in \{0, 1\}$；

- 一个自由向量集 $I_{\text{free}} \subset \mathbb{C}^D$.

对于输入 $x$，可用的输入向量集合为 $I(x) = I_{\text{free}} \cup \bigcup_{i=1}^n I_{i, x_i}$. 称生成程序计算了 $f$，当且仅当 $\ket{t} \in \op{span}(I(x))$ 成立时 $f(x) = 1$.

生成程序的复杂度由其见证大小衡量. 

- 如果 $f(x) = 1$，则存在 $I(x)$ 中向量的线性组合能够给出 $\ket{t}$；$x$ 的见证大小为任意此类线性组合系数的平方和的最小值.

- 如果 $f(x) = 0$，则存在一个与 $\ket{t}$ 内积为 1 的向量，并且与所有可用输入向量正交；$x$ 的见证大小为该向量与所有输入向量的内积所构成的向量的平方和的最小值.

- 函数 $f$ 的见证大小是 $x \in S$ 的最大见证大小，或者等价地，是 $0$-输入和 $1$-输入的最大见证的几何平均值.

任何计算 $f$ 的生成程序的最小见证大小恰好等于 $\op{Adv}^\pm(f)$，并且生成程序与对偶敌手解有紧密联系. 给定具有向量 $\ket{v_{x, i}}$ 的对偶敌手解，可以构造一个矩阵，其行是向量 $\bigoplus_{i \in [n]} \bra{\bar{x}_i} \bra{v_{x, i}}$. 取该矩阵在块 $i$ 和子块 $b$ 处的列作为 $I_{i, b}$ 的元素，目标向量为全 $1$ 向量，不设置自由向量. 可以证明，这给出了一个见证大小正好是对偶敌手解的复杂度的生成程序.

此外，每个生成程序都可以被转化为一种规范形式，使得这种转换可以被逆转以产生一个对偶敌手解：将规范生成程序的向量视作矩阵的列，其行给出了 $x \in f^{-1}(0)$ 的对偶敌手解向量；而 $x \in f^{-1}(1)$ 的见证向量则给出了其余的对偶敌手解向量.

## Unstructured search

现在给出一个最优对偶敌手解的简单例子，即用于无结构搜索问题. 定义 $f: S \to \{0, 1\}$ 为 $f(x) = \mathrm{OR}(x)$，其中 $S = \{ x \in \{0, 1\}^n : \lvert x \rvert \leq 1 \}$ 为 Hamming 重量最多为 1 的输入集合. 取维度 $d = 1$，对于所有 $i \in [n]$，令 $\ket{v_{0, i}} = 1$ 且 $\ket{v_{x, i}} = x_i$. 约束条件给出：

\[
    \sum_{i: 0 \neq (e_j)_i} \innerproduct{v_{0, i}}{v_{e_j, i}} = \innerproduct{v_{0, j}}{v_{e_j, j}} = 1,
\]

对所有的 $j \in [n]$ 成立，其中 $e_j \in \mathbb{C}^n$ 为第 $j$ 个自然基向量；以及

\[
    \sum_{i: (e_j)_i \neq (e_k)_i} \innerproduct{v_{e_j, i}}{v_{e_k, i}} = \innerproduct{v_{e_j, j}}{v_{e_k, j}} + \innerproduct{v_{e_j, k}}{v_{e_k, k}} = 0,
\]

对 $j \neq k$ 成立，所以约束满足.

$0$-复杂度和 $1$-复杂度分别为

\begin{align*}
    C_0 & = \sum_{i=1}^n \lVert \ket{v_{0, i}} \rVert^2 = n, \\
    C_1 & = \max_{j \in [n]} \sum_{i=1}^n \lVert \ket{v_{e_j, i}} \rVert^2 = 1.
\end{align*}

因为 $\sqrt{C_0 C_1} = \sqrt{n}$，所以 $\op{Adv}^\pm(f) \leq \sqrt{n}$. 这表明先前讨论的敌手下界是最佳的. 也很容易将此对偶敌手解推广到总 $\mathrm{OR}$ 函数，只需令 $\ket{v_{x, i}} = \delta_{i, j}$，其中 $j$ 是任意一个满足 $x_j = 1$ 的索引位置.

## Formulas and games

无结构搜索可以看作在 $O(\sqrt{n})$ 次查询内计算 $n$ 个比特的逻辑 $\mathrm{OR}$ 问题，很自然地会去思考其他布尔函数的查询复杂度. 接下来将使用生成程序来证明，具有 $n$ 个叶子的平衡二叉 $\mathrm{AND}$-$\mathrm{OR}$ 树的量子查询复杂度为 $O(\sqrt{n})$. 类似地方法表明，任何用 $\mathrm{AND}$, $\mathrm{OR}$, $\mathrm{NOT}$ 门表示的布尔公式的量子查询复杂度都是 $O(\sqrt{n})$.

考虑 Andera 和 Orlando 之间的双人游戏，玩家轮流行动，Andera 先手. 每轮有 $d$ 种可能的移动，一共进行 $k$ 轮. 假设赢家由某个黑盒函数 $f: \{1, \ldots, d\}^k \to \{0, 1\}$ 决定，当 $f$ 的输出为 $0$ 时 Andera 获胜，否则 Orlando 获胜. 若 Andera 和 Orlando 都采用最优策略，那么这个问题等价于计算一个 $\mathrm{AND}$-$\mathrm{OR}$ 公式. 考虑决策树，其为高度为 $k$ 的平衡 $d$ 叉树. 如果 Orlando 能够做出任何导致结果为 $1$ 的移动，他就会获胜，所以其对应的是 $\mathrm{OR}$ 门；而 Andera 如果能做出任何导致结果为 $0$ 的移动，他就会获胜，所以其对应的是 $\mathrm{AND}$ 门. 

那么计算这个平衡 $d$ 叉 $\mathrm{AND}$-$\mathrm{OR}$ 树的量子查询复杂度是多少呢？首先考虑的是随机化经典算法. 因为 $\mathrm{OR}$ 和 $\mathrm{AND}$ 门的特性，所以可以避开对所有叶子节点的查询，如得知某一 $\mathrm{AND}$ 门的一个子节点为 $0$，则不需要查询其他子节点；只有在所有输入均为 $1$ 时，才需要查询所有子节点. 但 $\mathrm{AND}$ 门的输入都由 $\mathrm{OR}$ 门的输出给出，而 $\mathrm{OR}$ 门输出 $1$ 又只需要查询到一个子节点为 $1$ 即可. 

因此一个合理的经典算法为随机猜测一个子节点并且递归的计算它，只在必要时计算其他子节点. 通过分析一个简单的递归式，可以证明该算法使用了

\[
    O\left(\left( \frac{d - 1 + \sqrt{d^2 + 14d + 1}}{4} \right)^k\right) = O(n^{\log_d \frac{d - 1 + \sqrt{d^2 + 14d + 1}}{4}})
\]

次查询，其中 $n = d^k$ 为输入大小. 实际上，可以证明该算法是渐近最优的. 而随着 $d$ 增大，$n$ 保持固定，经典查询复杂度变得更大. 极端情况 $k = 1$，即 $n = d$ 时，这只是在计算 $\mathrm{AND}$ 门，依据 Demorgan 定律等价于计算 $\mathrm{OR}$ 门，且需要 $\Omega(n)$ 次查询.

而如果 $k$ 足够小，量子计算机便可以更快的计算此类游戏. $k = 1$ 的情况可以通过 Grover 算法在 $O(\sqrt{n})$ 次查询内完成. 而通过递归地应用 Grover 算法，并适当放大成功概率，可以在 $\sqrt{n} O(\log n)^{k-1}$ 次查询内完成该公式的计算，这对常数 $k$ 是近乎最优的. 使用允许噪声输入的 Grover 算法变体，可以略微改进为 $O(\sqrt{n} c^k)$，其中 $c$ 是某个常数. 但这两种算法只在 $k$ 是常数是接近紧的，对于非常低的度数（如 $d = 2$, $k = \log_2 n$）时，直到 2007 年才提出了比经典算法更好的量子算法.

以下将描述如何仅用 $O(\sqrt{n})$ 次量子查询解决该问题，利用生成程序的组合性质来进行分析.

## Function composition

敌手方法的一个良好性质是其在函数复合下的行为. 给定 $f: \{0, 1\}^n \to \{0, 1\}$ 和 $g: \{0, 1\}^m \to \{0, 1\}$，定义复合函数 $f \circ g: \{0, 1\}^{nm} \to \{0, 1\}$ 为

\[
    (f \circ g)(x) = f(g(x_1, \ldots, x_m), g(x_{m+1}, \ldots, x_{2m}), \ldots, g(x_{(n-1)m+1}, \ldots, x_{nm})).
\]

这里关注上界，有如下结果：

!!! note "Theorem"
    $\op{Adv}^\pm(f \circ g) \leq \op{Adv}^\pm(f) \cdot \op{Adv}^\pm(g)$.

    ???+ note "Proof"
        设 $\{\ket{v_{x, i}} : x \in \{0, 1\}^n, i \in [n]\}$ 是 $f$ 的一个最优对偶敌手解，$\{\ket{u_{y, j}} : y \in \{0, 1\}^m, j \in [m]\}$ 是 $g$ 的一个最优对偶敌手解. 令 $y = (y^1, \ldots, y^n)$，其中 $y^i \in \{0, 1\}^m$，并且定义

        \[
            \ket{w_{y, (i, j)}} = \ket{v_{g(y), i}} \otimes \ket{u_{y^i, j}},
        \]

        其中 $g(y) = (g(y^1), \ldots, g(y^n))$. 宣称这就是 $f \circ g$ 的一个对偶敌手解. 验证约束条件：

        \begin{align*}
            \sum_{(i, j): y_j^i \neq z_j^i} \innerproduct{w_{y, (i, j)}}{w_{z, (i, j)}} & = \sum_{i \in [n]} \innerproduct{v_{g(y), i}}{v_{g(z), i}} \sum_{j: y_j^i \neq z_j^i} \innerproduct{u_{y^i, j}}{u_{z^i, j}} \\
            & = \sum_{i \in [n]} \innerproduct{v_{g(y), i}}{v_{g(z), i}} (1 - \delta_{g(y^i), g(z^i)}) \\
            & = \sum_{i: g(y^i) \neq g(z^i)} \innerproduct{v_{g(y), i}}{v_{g(z), i}} \\
            & = 1 - \delta_{(f \circ g)(y), (f \circ g)(z)}.
        \end{align*}

        又因为 $\lVert \ket{w_{y, (i, j)}} \rVert = \lVert \ket{v_{g(y), i}} \rVert \cdot \lVert \ket{u_{y^i, j}} \rVert$，所以

        \begin{align*}
            \op{Adv}^\pm(f \circ g) & \leq \max_y \sum_i \lVert \ket{v_{g(y), i}} \rVert^2 \sum_j \lVert \ket{u_{y^i, j}} \rVert^2 \\
            & \leq \op{Adv}^\pm(f) \cdot \op{Adv}^\pm(g).
        \end{align*}

所以将 $\mathrm{AND}$ 和 $\mathrm{OR}$ 的对偶敌手解相结合，就能得到平衡二叉 $\mathrm{AND}$-$\mathrm{OR}$ 树的 $O(\sqrt{n})$ 上界.

## An algorithm from a dual adversary solution

对偶敌手法不仅给出了 $\op{Adv}^\pm(f)$ 的上界，还直接给出了一个查询复杂度为 $O(\op{Adv}^\pm(f))$ 的计算 $f$ 的量子算法. 