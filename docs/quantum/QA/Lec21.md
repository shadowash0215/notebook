# Query complexity and the polynomial method

## Quantum query complexity

已涉及的诸多算法都是在查询复杂度的框架下进行分析的. 该框架中问题的输入由一个“黑盒”提供，其自然地为证明下界提供了一个切入点：通常可以证明，要计算黑盒输入的函数需要多次查询. 相比之下，为计算显式输入的函数证明复杂度下界是著名的困难.

以下简要形式化查询复杂度模型. 考虑计算函数 $f: S \to T$，其中 $S \subseteq \Sigma^n$ 是某个输入字母表 $\Sigma$ 上的字符串集合. 如果 $S = \Sigma^n$，则称 $f$ 为**总函数**（total function），否则称为**部分函数**（partial function）. 输入字符串 $x \in S$ 由一个黑盒提供，其可以计算任何所需的 $i \in \{1, 2, \ldots, n\}$ 对应的 $x_i$ 的值. 

查询算法从一个不依赖于谕示机字符串 $x$ 的初始状态开始，然后其交替进行对黑盒的查询和其他的非查询操作. 目标是在尽可能少的查询次数下，输出 $f(x)$ 的值. 最小查询次数，也就是所谓的 $f$ 的**查询复杂度**，取决于所允许的计算类型，至少存在三种自然模型：

1. $D(f)$ 表示确定性查询复杂度，其中算法是经典的并且必须始终正确工作.

2. $R_\varepsilon$ 表示错误概率至多为 $\varepsilon$ 的随机化查询复杂度，因为可以通过多次重复计算并采取多数表决策略来提高成功率，所以其对 $\varepsilon$ 的依赖性不强. 对于任何常数 $\varepsilon$，有 $R_\varepsilon(f) = \Theta(R_{1/3}(f))$，有时也简记为 $R(f)$.

3. $Q_\varepsilon$ 表示错误概率至多为 $\varepsilon$ 的量子查询复杂度，与随机化查询复杂度类似，对于任何常数 $\varepsilon$，有 $Q_\varepsilon(f) = \Theta(Q_{1/3}(f))$，有时也简记为 $Q(f)$.

已知 $D(\op{OR}) = n$ 且 $R(\op{OR}) = \Theta(n)$，而 Grover 算法表明 $Q(\op{OR}) = \Theta(\sqrt{n})$. 本讲将使用多项式方法证明 $Q(\op{OR}) = \Omega(\sqrt{n})$，这是一个紧的下界.

## Quantum queries

量子查询算法从与 $x$ 无关的态 $\ket{\psi}$ 开始，然后应用一系列酉操作 $U_1, \ldots, U_t$，这些操作与查询 $O_x$ 交替进行，最终得到态

\[
    \ket{\psi_x^{t}} = U_t O_x \cdots U_2 O_x U_1 O_x \ket{\psi}.
\]

而精确的描述这一过程需要说明谕示机 $O_x$ 的使用方式. 简化情况只考虑输入是比特串，即 $\Sigma = \{0, 1\}$ 的情形. 此情况下最自然的模型是比特翻转谕示机 $\hat{O}_x$，其作用如下：

\[
    \hat{O}_x \ket{i, b} = \ket{i, b \oplus x_i}, \quad i \in \{1, 2, \ldots, n\}, b \in \{0, 1\}.
\]

这是自然可逆谕示机映射 $(i, b) \mapsto (i, b \oplus x_i)$ 的线性延拓，只要能高效计算 $i \mapsto x_i$ 即可高效实现.

方便起见，更多考虑的是相位谕示机 $O_x$，其通过对比特翻转谕示机应用 Hadamard 门共轭得到：通过相位反冲技巧，$O_x = (I \otimes H) \hat{O}_x (I \otimes H)$ 满足

\[
    O_x \ket{i, b} = (-1)^{b \cdot x_i} \ket{i, b}, \quad i \in \{1, 2, \ldots, n\}, b \in \{0, 1\}.
\]

但这实际上有点浪费，因为有 $O_x \ket{i, 0} = \ket{i, 0}, \forall i$. 可以等价的考虑一个相位谕示机 $O_x'$，定义为 $O_x' \ket{0} = \ket{0}$ 以及 $\forall i \in \{1, 2, \ldots, n\}, O_x' \ket{i} = (-1)^{x_i} \ket{i}$. 但也必须包含通过输入一个已知特征值的特征态来不查询输入的能力. 如果只能执行相位翻转 $\ket{i} \mapsto (-1)^{x_i} \ket{i}$ 的话，就无法区分字符串 $x$ 以及其按位取反 $\bar{x}$.

推广到 $d$ 元输入字母表 $\Sigma = \mathbb{Z}_d$ 的情形，可以定义如下谕示机 $\hat{O}_x$：

\[
    \hat{O}_x \ket{i, b} = \ket{i, b + x_i}, \quad i \in \{1, 2, \ldots, n\}, b \in \mathbb{Z}_d.
\]

对第二个寄存器进行 Fourier 变换可得到相位谕示机 $O_x = (I \otimes F_{\mathbb{Z}_d}) \hat{O}_x (I \otimes F_{\mathbb{Z}_d}^\dagger)$，其满足

\[
    O_x \ket{i, b} = \omega^{b \cdot x_i} \ket{i, b}, \quad i \in \{1, 2, \ldots, n\}, b \in \mathbb{Z}_d.
\]

## Quantum algorithms and polynomials

!!! success "Lemma"
    对于一个输入为 $x \in \{0, 1\}^n$ 的黑盒问题，进行 $t$ 次查询的量子算法的接受概率是变量 $x_1, x_2, \ldots, x_n$ 的一个次数至多为 $2t$ 的多项式.

    ???+ success "Proof"
        断言任何基态的振幅是一个次数至多为 $t$ 的多项式，因此得到任何基态的概率，也包括了接受概率，是一个次数至多为 $2t$ 的多项式.

        证明通过对 $t$ 的归纳进行. 如果一个算法不对输入进行任何查询，那么其接受概率与输入无关，因此是常数，一个次数为 $0$ 的多项式.

        而对于归纳步骤，一次查询进行如下的映射操作：

        \begin{align*}
            \ket{i, b} & \overset{O_x}{\mapsto} (-1)^{b \cdot x_i} \ket{i, b} \\
                       & = (1 - 2 b x_i) \ket{i, b}.
        \end{align*}

        因此它将每个振幅的次数增加了至多 $1$. 

考虑布尔函数 $f: \{0, 1\}^n \to \{0, 1\}$，若对于所有 $x \in \{0, 1\}^n$，有一个多项式 $p \in \mathbb{R}[x_1, \ldots, x_n]$ 满足 $p(x) = f(x)$，则称 $p$ 表示 $f$. 记 $\deg(f)$ 为表示 $f$ 的最小次数多项式的次数，有 $Q_0(f) \geq \deg(f)/2$.

为了处理有界误差算法，引入**近似次数**（approximate degree）概念. 若对于所有 $x \in \{0, 1\}^n$，有一个多项式 $p$ 满足 $\lvert p(x) - f(x) \rvert \leq 1/\varepsilon$，则称 $p$ $\varepsilon$-近似 $f$. $f$ 的 $\varepsilon$-近似次数 $\widetilde{\deg}_\varepsilon(f)$ 定义为 $\varepsilon$-近似 $f$ 的最小次数多项式的次数. 显然 $Q_\varepsilon(f) \geq \widetilde{\deg}_\varepsilon(f)/2$. 而先前提到过误差有界查询复杂度并不强烈依赖于特定的错误概率 $\varepsilon$，所以可以定义 $\widetilde{\deg}(f) = \widetilde{\deg}_{1/3}(f)$. 所以若要为布尔函数的量子查询复杂度约束下界，只需要为其近似次数约束下界即可.

## Symmetrization

考虑 $x \in {0, 1}$ 有 $x^2 = x$，因此所谓的多元多项式其实可以降次为多重线性多项式，再利用对称化便可以得到一个相关的单变量多项式. 考虑 $x \in \{0, 1\}^n$，记 $\lvert x \rvert = \sum_{i=1}^n x_i$ 为 $x$ 的 Hamming 重量. 

!!! success "Lemma"
    给定任意 $n$ 元多重线性多项式 $p$，令 $P(k) = \mathbb{E}_{\lvert x \rvert = k} [p(x)]$，即所有 Hamming 重量为 $k$ 的输入 $x$ 上 $p(x)$ 的均值. 那么 $P$ 是一个满足 $\deg(P) \leq \deg(p)$ 的单变量多项式.

    ???+ success "Proof"
        因为 $p$ 是多重线性的，所以可以写作单项式的和，即对于某些系数 $c_S$，有

        \[
            p(x) = \sum_{S \subset \{1, \ldots, n\}} c_S \prod_{i \in S} x_i.
        \]

        因此 $P(k)$ 也可以写作

        \[
            P(k) = \sum_{S \subset \{1, \ldots, n\}} c_S \mathbb{E}_{\lvert x \rvert = k} \left[ \prod_{i \in S} x_i \right].
        \]
        
        而每个单项式的均值可以计算为

        \begin{align*}
            \mathbb{E}_{\lvert x \rvert = k} \left[ \prod_{i \in S} x_i \right] & = \Pr_{ \lvert x \rvert = k} \left[ \forall i \in S, x_i = 1 \right] \\
            & = \frac{\binom{n - \lvert S \rvert}{k - \lvert S \rvert}}{\binom{n}{k}} \\
            & = \frac{(n - \lvert S \rvert)! k! (n - k)!}{(k - \lvert S \rvert)! (n - k)! n!} \\
            & = \frac{(n - \lvert S \rvert)!}{n!} \cdot k (k - 1) \cdots (k - \lvert S \rvert + 1).
        \end{align*}

        这是 $k$ 的 $\lvert S \rvert$ 次多项式，而当 $\lvert S \rvert > \deg(p)$ 时，其系数 $c_S = 0$，因此 $\deg(P) \leq \deg(p)$.

因此，多项式方法对于对称函数来说是一种自然的研究途径.

## Parity

设奇偶函数 $\op{PARITY}: \{0, 1\}^n \to \{0, 1\}$ 定义为 $\op{PARITY}(x) = \oplus_{i=1}^n x_i$. Deutsch 问题为计算两个比特输入的奇偶函数，只使用了一次查询. 通过每次查询一对比特，并且获取结果的奇偶，可以得到 $Q_0(\op{PARITY}) \leq n/2$. 

接下来讨论下界. 对称化奇偶函数得到的单变量多项式 $P: \{0, 1, \ldots, n\} \to \mathbb{R}$ 满足

\[
    P(k) = \begin{cases}
        0, & \text{if } k \text{ is even}, \\
        1, & \text{if } k \text{ is odd}.
    \end{cases}   
\]

因为 $P$ 变换了 $n$ 次方向，所以 $\deg(P) \geq n$. 因此 $Q_0(\op{PARITY}) \geq n/2$, Deutsch 算法在确定性查询复杂度意义下是最优的.

而对于有界误差情形，需要约束 $\op{PARITY}$ 的近似次数下界. 若 $\lvert p(x) - f(x) \rvert \leq \varepsilon$，$\forall x \in \{0, 1\}^n$，则相应的单变量多项式 $P$ 满足

\[
    \lvert P(k) - F(k) \rvert = \lvert \mathbb{E}_{\lvert x \rvert = k} [p(x) - f(x)] \rvert \leq \varepsilon, \forall k \in \{0, 1, \ldots, n\},
\]

$P$ 和 $F$ 分别为 $p$ 和 $f$ 的对称化多项式. 因此 $\op{PARITY}$ 的 $\varepsilon$-近似多重线性多项式 $p$ 意味着存在一个单变量多项式 $P$ 满足：

1. $k$ 为偶数时，$P(k) \leq \varepsilon$；

2. $k$ 为奇数时，$P(k) \geq 1 - \varepsilon$.

对于 $\varepsilon < 1/2$，该函数依然改变了 $n$ 次方向，因此 $\deg(P) \geq n$. 也就是说 $\widetilde{\deg}_\varepsilon(\op{PARITY}) \geq n$，从而 $Q_\varepsilon(\op{PARITY}) \geq n/2$. 这表明即使包含了允许的错误概率，Deutsch 算法仍然是最优的. 这也是一个量子计算机无法获得任何显著加速的例子. 相比之下，尽管敌手方法可以证明奇偶函数的下界为 $\Omega(n)$，但其所确定的常数因子是依赖于 $\varepsilon$ 的.

注意，这也表明在无结构搜索问题中，精确计算标记项的数量需要 $\Omega(n)$ 次查询，因为精确确定 $1$ 的个数实际上也确定了奇偶性.

## Unstructured search

接下来将利用多项式方法证明计算 $n$ 个比特的逻辑或的下界为 $\Omega(\sqrt{n})$. $\op{OR}$ 的对称化函数为 $F(k)$，其中 $F(0) = 0$，$F(1) = 1$. 其实还有 $F(k) = 1, k > 1$，但实际上不需要使用这个性质. 这个函数是单调的，所以不能利用奇偶函数的方法来约束. 不过有如下来自 Markov 不等式的结果来证明 $\widetilde{\deg}(\op{OR}) = \Omega(\sqrt{n})$.

!!! success "Lemma"
    设 $P: \mathbb{R} \to \mathbb{R}$ 是一个多项式，那么

    \[
        \max_{x \in [0, n]} \frac{\mathrm{d}P(x)}{\mathrm{d}x} \leq \frac{(\deg(P))^2}{n} \left( \max_{x \in [0, n]} P(x) - \min_{x \in [0, n]} P(x) \right).
    \]

换言之，令

\[
    h := \max_{x \in [0, n]} P(x) - \min_{x \in [0, n]} P(x),
\]

为 $P$ 在区间 $[0, n]$ 上的“高度”，以及

\[
    d = \max_{x \in [0, n]} \frac{\mathrm{d}P(x)}{\mathrm{d}x},
\]

为 $P$ 在区间 $[0, n]$ 上的最大导数值，那么有 $\deg(P) \geq \sqrt{nd/h}$.


设 $P$ 为 $\op{OR}$ 的 $\varepsilon$-近似多项式，那么 $P(0) \leq \varepsilon$ 且 $P(1) \geq 1 - \varepsilon$. $P$ 从 $0$ 到 $1$ 的变化量至少为 $1 - 2\varepsilon$，因此 $d \geq 1 - 2\varepsilon$. $h$ 是不可控的，因为无法控制 $P$ 在非整数点的行为，函数可能在这些点上振荡得很厉害. 但对于 $k \in \{0, 1, \ldots, n\}$，有 $P(k) \in [0, 1]$，如果 $h$ 非常大，那么 $d$ 也就会很大，因为 $P$ 必须足够快的变化以从 $[0, 1]$ 内的值开始并返回到 $[0, 1]$ 内. 特别地，$P$ 在宽度至多为 $1/2$ 的区间上至少需要变化 $(h - 1)/2$，因此 $d \geq (h - 1)$. 综上，有

\[
    \deg(P) \geq \sqrt{\frac{n \max{(1 - 2\varepsilon, h - 1)}}{h}} = \Omega(\sqrt{n}).
\]

所以 $Q(\op{OR}) = \Omega(\sqrt{n})$.

对于任意的 $w$，上述论证同样适用于 $\lvert x \rvert = w$ 时取值为 $0$，$\lvert x \rvert = w + 1$ 时取值为 $1$ 的函数；特别地，其适用于任何非常值对称函数. 当然，对于某些对称函数，如奇偶函数和多数函数等，可以得到更好的下界.