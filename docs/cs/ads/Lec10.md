# $\mathsf{NP}$ 完全性

## 形式语言

!!! info "Definition"
    **字母表**：至多可数的非空集合 $\Sigma$.  
    **字符串**：字母表中元素的有限序列，所有字符串的集合记为 $\Sigma^*$，空串记为 $\varepsilon$.  
    **语言**：字符串的集合，即 $\mathcal{L} \subseteq \Sigma^*$.  
    **Kleene 闭包**：$\mathcal{L}^* = \bigcup_{i=0}^{\infty} \mathcal{L}^i$，其中 $\mathcal{L}^0 = \{\varepsilon\}$，$\mathcal{L}^i$ 指 $\mathcal{L}$ 的 $i$ 次串接.

形式语言在复杂度理论中有着重要的地位，我们此处主要讨论两个问题：  
1. **判定问题**：给定一个字符串 $\omega$ 和一个语言 $\mathcal{L}$，判断 $\omega \in \mathcal{L}$ 是否成立.  
2. **搜索问题**：给定一个语言 $\mathcal{L}$，寻找满足 $\omega \in \mathcal{L}$ 的字符串 $\omega$.

## 计算模型

!!! info "Turing Machine"
    考虑一个双向无限的磁带（tape），将其划分成一个一个的方格（cell），有一个磁头（head），磁头中有一个有限状态机，其中包含有限个状态 $q \in Q$。每个方格要么是空的（$\square$），要么是写有字符 $s \in S$ 的（$S$ 为有限集）. 在每一步操作中，它可以完成：  

    - 磁头内部状态的转变；  
    - 把扫描到的符号 $s$ 改写成 $s' \in S \cup \{\square\}$；  
    - 往左（$L$）或往右（$R$）移动磁头.

    这由一个偏函数（只在定义域的一个子集上有定义的函数）$\delta: Q \times (S \cup \{\square\}) \to Q \times (S \cup \{\square\}) \times \{L, R\}$ 决定（即当我们处于某个状态、读取到某个字符时，这个函数告诉我们下一个状态、应该写下的字符以及应该往哪个方向移动磁头），我们将这个偏函数称为图灵程序（Turing program）.

    每一个计算开始之前，我们都将磁头置于起始方格（starting cell），它是写有内容的最左侧方格，并让其处于起始状态（starting state），然后将输入放在起始方格右侧，并保证纸带其余部分为空。如果磁头抵达状态 $q_h \in Q$，称作停机状态（halting state），则视作计算结束，并将磁带上从起始方格开始的内容视作输出。我们将图灵机的构型（configuration），记作：

    \[
        c = t_mt_{m-1}\cdots t_2t_1\underline{q_i}s_1s_2\cdots s_k.
    \]

    其中 $s_i$ 和 $t_i$ 分别是一直到最右侧（最左侧）的非空格子上的内容，当然，如果没有则可以写个 $\square$；$q_i$ 指当前磁头所处的状态，当前磁头指向 $s_1$ 所在的方格.

    如果磁头进入状态 $q \neq q_h$ 而 $\delta$ 未定义（不移动），则称计算中断，不将其视作停机.

    所谓的图灵计算（Turing computation）就指图灵机的一列构型 $c_0, c_1, \ldots , c_n$，它按照如上的叙述由一个图灵程序所描述.

下面是图灵机的一个例子：

!!! example "Example"
    因为我们需要讨论判定问题，因此图灵机最终应该告诉我们 “是” 或 “否”。实际上就是最终图灵机会在纸带上留下一个 1 或 0 代表 “是” 或 “否”。在有些图灵机的定义中，我们会规定写下 1 时代表一个 $q_{accept}$ 状态表示接收，写下 0 时代表一个 $q_{reject}$ 状态表示拒绝，实际上如果我们在进入接受和拒绝状态后再加一个转移函数到停机状态 $q_h$，就和我们的定义相容了.

以上定义的图灵机称为**确定性图灵机**，我们也可以定义**非确定性图灵机**，其转移函数 $\delta$ 是一个从 $Q \times (S \cup \{\square\})$ 到 $2^{Q \times (S \cup \{\square\}) \times \{L, R\}}$ 的映射，即在某个状态读取某个字符时，可以有多种选择。在判定性问题中，如果有一种选择使得图灵机停机，我们就说这个图灵机接受输入；只有当所有选择都导致图灵机不停机时，我们说这个图灵机拒绝输入。

!!! note "Theorem"
    任何一个非确定性图灵机都可以被一个确定性图灵机模拟，即它们可以计算的函数是一致的。  
    ??? note "Proof"
        使用带有三条纸带的图灵机模拟非确定性图灵机，其中第一条纸带是输入，第二条纸带模拟非确定性图灵机读到输入的时候的状态和行动，第三条纸带来记录 BFS 的进程，提示第二条纸带下一步应该模拟哪条路径。

## Gödel 数

记 $\mathbb{P} \subset \mathbb{N}$ 为素数集合，对于至多可数集合 $\Sigma$，我们可以定义一个双射 $f: \Sigma \to \mathbb{N}$，然后将每个字符串 $\omega = x_1x_2\cdots x_n$ 映射到 $\mathbb{N}$ 上：
    
\[
    x_1x_2\cdots x_n \mapsto p_1^{f(x_1)}p_2^{f(x_2)}\cdots p_n^{f(x_n)},
\]

其中 $p_n$ 指 $\mathbb{P}$ 中第 $n$ 个素数。这样我们就建立了一个从 $\mathcal{L} \to \mathbb{N}$ 的映射，并且这个映射是单射，这样的对应称为 Gödel 数.

!!! example "Example"
    图灵机是可以被指派 Gödel 数的，因为图灵程序的每一个分量都是可数的，所以只有可数个图灵机。我们记 $M_{\alpha}$ 为编码为 $\alpha$ 的图灵机。不难发现：   

    1. 对于任意计算，都存在无穷多个 $\alpha \in \mathbb{N}$ 对应完成这种计算的图灵程序，这只要通过插入一些无意义状态就能实现。这个结论通常被称为指标集（indice set）的无限性。  
    2. 存在一个图灵机模拟任意编号 $\alpha$ 的图灵机的执行。这个图灵机称为通用图灵机（universial Turingmachine）。可以表明，如果原来的图灵机计算时间是 $f(n)$，那么它花费的时间是 $O(f(n)\log f(n))$.

在此呈现 Tarski 不可定义性定理（Tarski's undefinability theorem），它蕴含了 Gödel 的结果：

!!! info "Definition"
    称 $T: \mathcal{L} \to \mathcal{L}$ 是语言 $\mathcal{L}$ 上的一个谓词（predicate），如果它将字符串 $x$ 映到:

    \[
        s_1 x s_2 x \cdots s_{n - 1} x s_n,
    \]

    其中 $s_i \in \Sigma^*$，且对于任意 $x \in \mathcal{L}$，都有 $T(x) \in \mathcal{L}$.

!!! note "Tarski's undefinability theorem"
    设 $\mathcal{L}$ 是一个形式语言，存在 $\mathbb{N}$ 到 $\Sigma^*$ 的嵌入，记作 $\iota$，其中的字符串可以用 $g: \mathcal{L} \to \mathbb{N}$ 对应到其 Gödel 数，并满足以下条件：

    1. 存在函数 $f: \mathcal{L} \to \{0, 1\}$，称为字符串的**真值**；  
    2. 存在符号 $\neg \in \Sigma$，使得 $f(\neg x) = 1 - f(x)$；  
    3. 对角线引理：对于任意谓词 $B: \mathcal{L} \to \mathcal{L}$，都有一个字符串 $a$ 使得 $a = B(\iota(g(a)))$.

    那么，不存在谓词 $T: \mathcal{L} \to \mathcal{L}$ 满足 $f(T(\iota(g(x)))) = f(x), \forall x \in \mathcal{L}$.

    ??? note "Proof"
        反证法. 根据对角线引理，考虑 $s \in \mathcal{L}$ 使得 $s = \neg T(\iota(g(s)))$（即取 $B = \neg T$），那么 $f(s) = 1 - f(T(\iota(g(s)))) = 1 - f(s)$，矛盾.

这个定理带来了以下的结果：

!!! tip
    1. 不存在谓词 $T$ 使得 $f \circ T \circ \iota \circ g$ 能够判定任意一个字符串的真值；也就是说，$\iota \circ g$ 的“逆”不可完全在 $\mathcal{L}$ 上定义.  
    2. Gödel 不完备性定理：一个包含基本算数（自然数及其等性）的公理系统中，存在一个不可证明也不可证伪的命题：取 $\mathcal{L}$ 为所有可能的逻辑公式，它可以叙述自然数的性质。而一个逻辑公式可以用 $g$ 来编码。所以，对角线引理就是表明，我们有一个谓词 $S(n)$ 表达 $\varphi(n)$ 为假，其中 $\varphi$ 是 Gödel 数为 $n$ 的逻辑公式。然后，将 $S$ 应用于它自身的 Gödel 数 $g(S)$，即可得出矛盾，因为若 $S(g(S))$ 为真，则 $\varphi(g(S))$ 为假，其中 $\varphi$ 是 Gödel 数为 $g(S)$ 的逻辑公式，又 $g$ 是单射，故 $S = \varphi$，所以若 $S(g(S))$ 为真，则 $\varphi(g(S)) = S(g(S))$ 为假，这显然是荒谬的.  
    3. 停机问题：存在一个不可被图灵机计算的问题：判定任意一个图灵机是否会停机。这个问题的证明是通过构造一个图灵机，它会在某个 Gödel 数 $g$ 上停机当且仅当这个 Gödel 数对应的图灵机 $M_g$ 在自己 Gödel 数 $g$ 上不停机，这个图灵机的存在性就是对角线引理的推论.

## 复杂类

### $\mathsf{DTIME}$ 和 $\mathsf{NTIME}$

!!! info "Definition"
    考虑一族函数 $\{f_n\}$. 称一个函数是：  
    1. $\mathsf{DTIME}(f(n))$ 的，如果求解规模为 $n$ 的问题的确定性图灵机在时间 $f(n)$ 步内停机；  
    2. $\mathsf{NTIME}(f(n))$ 的，如果求解规模为 $n$ 的问题的非确定性图灵机在时间 $f(n)$ 步内停机.

一个形式语言 $\mathcal{L}$ 的判定问题的规模指的是输入的长度。这两个类的定义来源于 Hartmanis & Stearns 的论文，这里给出的形式是稍有不同的，忽略了常数的问题，只要注意到他们证明的一个加速定理：

!!! note "Hartmanis-Stearns, 1966"
    如果 $f$ 可以被图灵机 $M$ 在 $T(n)$ 时间内计算，那么对于任意常数 $c \geqslant 1$，都有一个图灵机 $\tilde{M}$ 能够在 $T(n)/c$ 的时间内完成同样的计算.

由此可以定义以下复杂类：

!!! info "Definition"
    1. $\mathsf{P} = \bigcup_{c \geqslant 1} \mathsf{DTIME}(n^c)$，即多项式时间内可解的问题；  
    2. $\mathsf{NP} = \bigcup_{c \geqslant 1} \mathsf{NTIME}(n^c)$，即多项式时间内可验证的问题；  
    3. $\mathsf{EXP} = \bigcup_{c \geqslant 1} \mathsf{DTIME}(2^{n^c})$，即指数时间内可解的问题；  
    4. $\mathsf{NEXP} = \bigcup_{c \geqslant 1} \mathsf{NTIME}(2^{n^c})$，即指数时间内可验证的问题.

以上复杂类的有这样的关系：$\mathsf{P} \subset \mathsf{NP}$，$\mathsf{EXP} \subset \mathsf{NEXP}$，因为确定性图灵机是非确定性图灵机的特例. 同时还有 $\mathsf{NP} \subset \mathsf{EXP}$，这需要注意到用确定性图灵机模拟非确定性图灵机的开销是指数级的，或者使用如下的等价定义：

!!! note "Theorem"
    一个语言 $\mathcal{L}$ 是 $\mathsf{NP}$ 的当且仅当存在一个多项式 $p$ 和一个多项式时间的确定性图灵机 $M$，使得对于任意 $x$，都有

    \[
        x \in \mathcal{L} \Longleftrightarrow \exists u \in \{0, 1\}^{p(|x|)}, s.t. \ M(x, u) = 1.
    \]

    $u$ 被称作 $x$ 关于语言 $\mathcal{L}$ 的证明（certificate）. 故上式的含义为 $x$ 在 $\mathcal{L}$ 中当且仅当存在一个多项式长度的证明使得 $M$ 在多项式时间内接受.

如果 $\mathcal{L}$ 是 $\mathsf{NP}$ 的，那么给出一个非确定性图灵机的选择序列即可作为证明，这个序列长度一定是多项式规模的，因为非确定性图灵机在多项式时间内至多完成多项式次分支。而验证只要通过一个确定性图灵机模拟这个选择序列下的执行即可完成。如果存在这样一个证明，那么非确定性图灵机只要不断分支，一定能在多项式时间内分支多项式次，进而凑出这样的一个证明。

!!! example "Example"
    \[
        \mathcal{L} = \{(m, r) \mid \exists s < r, s \mid m\}
    \]

    这个语言是 $\mathsf{NP}$ 的，因为 $s$ 就是我们所需要的证明。问题的输入是 $m$ 和 $r$，输入的长度就是 $\log m + \log r$。而 $s$ 是一个小于 $r$ 的数，所以 $s$ 的长度是 $O(\log r)$ 的，其作为证明首先是多项式长度的，然后可以在 $\log r$ 的多项式时间内进行除法验证，所以这样就能验证给出的证明是否正确。

    如果用非确定性图灵机，直观而言我们直接在第一步尝试所有可能的 $s$ 即可。因为这些尝试只要有一个成功，那么我们就能得到一个正确的分解。 

### $\mathrm{co} \text{-} \mathsf{NP}$ 类

形式语言 $\mathcal{L}$ 的补集记作 $\overline{\mathcal{L}} = \Sigma^* \setminus \mathcal{L}$，而对于复杂类，我们也可以定义补类：

!!! info "Definition"
    设 $\mathsf{C}$ 是一个复杂类，则 $\mathrm{co} \text{-} \mathsf{C}$ 称为 $\mathsf{C}$ 的补类，其中的语言定义为：

    \[
        \mathrm{co} \text{-} \mathsf{C} = \{ \mathcal{L} \mid \overline{ \mathcal{L} } \in \mathsf{C} \}.
    \]

$\mathrm{co} \text{-} \mathsf{C}$ 并不意味着在所有问题意义上的补，而是其中所有语言的补。所以有如下的结果：

!!! note "Theorem"
    $\mathsf{P} = \mathrm{co} \text{-} \mathsf{P}$.  
    ??? note "Proof"
        调换确定性图灵机回答的 “是” 和 “否” 的含义即可.

但这对于 $\mathsf{NP}$ 来说，如果使用的是非确定性图灵机的定义，就相对难以处理。所以我们使用证明的方式来描述 $\mathrm{co} \text{-} \mathsf{NP}$：

!!! note "theorem"
    一个语言 $\mathcal{L}$ 是 $\mathrm{co} \text{-} \mathsf{NP}$ 的当且仅当存在一个多项式 $p$ 和一个多项式时间的确定性图灵机 $M$，使得对于任意 $x$，都有

    \[
        x \in \mathcal{L} \Longleftrightarrow \forall u \in \{0, 1\}^{p(|x|)}, s.t. \ M(x, u) = 0.
    \]

进一步，我们可以证明 $\mathsf{P} \subset \mathsf{NP} \cap \mathrm{co} \text{-} \mathsf{NP}$，以及 $\mathsf{P} = \mathsf{NP} \Rightarrow \mathsf{NP} = \mathrm{co} \text{-} \mathsf{NP}$.

以下给出一个关于 $\mathrm{co} \text{-} \mathsf{NP}$ 的例子：

!!! example
    在布尔公式中，所有永真式的集合是 $\mathrm{co} \text{-} \mathsf{NP}$ 的，这是因为我们可以用确定性图灵机在多项式时间内完成一个布尔公式的求值。如果它是永真式，那么任意求值的结果都是 1，然后翻转 0 和 1 即可匹配我们上面的定义。

### 空间复杂度类 $\mathsf{PSPACE}$

在这里，我们需要考虑的是图灵机的纸带花费多大的空间。

!!! info "Definition"
    我们同样定义一个问题是：  
    1. $\mathsf{DSPACE}(f(n))$ 的，如果求解规模为 $n$ 的问题的确定性图灵机花费 $f(n)$ 长度的纸带；  
    2. $\mathsf{NSPACE}(f(n))$ 的，如果求解规模为 $n$ 的问题的非确定性图灵机花费 $f(n)$ 长度的纸带.

非确定图灵机花费的纸带长度是最多的那个分支花费的长度。而此处的“加速定理”是不言自明的，只需要“几步并成一步”，也就是在一格纸带里多填充一些东西，扩充字母表即可。

以下的定理给出了 $\mathsf{DSPACE}$ 和 $\mathsf{NSPACE}$ 的关系：

!!! note "Savitch's theorem"
    对于任意函数 $f(n) \geqslant \log n$，都有 $\mathsf{NSPACE}(f(n)) \subset \mathsf{DSPACE}(f^2(n))$.