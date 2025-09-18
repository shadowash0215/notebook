# How to Construct Quantum Random Functions

!!! info "Abstract"
    - 原文链接：[How to Construct Quantum Random Functions](https://eprint.iacr.org/2012/182.pdf)

    - 只对论文主体部分以及影响理解的部分进行了翻译，摘要，总结等部分未翻译.

## Introduction

### Proving Quantum Security

Goldreich, Goldwasser 和 Micali 三人展示了如何从一个倍长的伪随机生成器（$\op{PRG}$）构造一个伪随机函数（$\op{PRF}$），这一构造也因而得名 GGM construction. 而 Johan Håstad 则给出了伪随机生成器可以从任何一个单向函数构造的证明，因为其采用的方法是完全通过黑盒构造的，所以如果支撑的单向函数是量子安全的，那么这个伪随机生成器也是量子安全的. 然而，经典的 GGM construction 的证明在量子情况下并不成立.

GGM Construction 隐含着一个深度为 $n$ 的二叉树，其每个叶子都对应了一个 $\op{PRF}$ 的输入输出对. 为了评估 $\op{PRF}$，应当先从根开始，根据输入构建从根到叶子的路径. 这一安全性证明包含了两个混合论证，第一个是针对树的层与层之间的，第二个是针对同层内的节点的. 第一个的混合论证数量是多项式级别的，因为树的层高是多项式级别的. 第二个的混合论证同样也是多项式级别的，因为经典的敌手只能向 $\op{PRF}$ 查询多项式个节点，所以用于评估 $\op{PRF}$ 的路径的在每一层只会访问多项式数量的节点. 以上两个混合论证允许将任何能以 $\varepsilon$ 的概率攻破 $\op{PRF}$ 的敌手 $A$ 转化为一个能以仅比 $\varepsilon$ 多项式小的概率攻破 $G$ 的敌手 $B$.

但在量子情况下，$A$ 可以用所有输入的叠加态向 $\op{PRF}$ 发起查询，所以即便是单个查询的回复也可能需要访问树中所有节点，而树中每一层的节点数目是指数级的，第二个混合论证就是指数级的. 这就意味着 $B$ 只能以指数小的概率攻破 $G$. 所有现存的从标准假设对 $\op{PRF}$ 的安全性进行证明的方法都有类似的问题.

??? tip "[Hybrid argument](https://en.wikipedia.org/wiki/Hybrid_argument_(cryptography))"
    为了证明两个分布 $D_1$ 和 $D_2$ 是计算上不可区分的，可以定义一个混合分布序列 $D_1 = H_0, H_1, \ldots, H_t = D_2$，其中 $t$ 是安全参数 $n$ 的多项式. 定义任一高效（多项式时间）概率算法 $A$ 的优势为：

    \[
        \op{Adv}_{H_i, H_{i+1}}^{\op{dist}}(A) = \lvert \Pr{x \xleftarrow{$} H_i : A(x) = 1} - \Pr{x \xleftarrow{$} H_{i+1} : A(x) = 1} \rvert
    \]

    其中 \$ 符号表示从分布中随机采样.

    根据三角不等式，可以得到

    \[
        \op{Adv}_{D_1, D_2}^{\op{dist}}(A) \leq \sum_{i=0}^{t-1} \op{Adv}_{H_i, H_{i+1}}^{\op{dist}}(A)
    \]

    因此存在 $k$ 使得 $\op{Adv}_{H_k, H_{k+1}}^{\op{dist}}(A) \geq \op{Adv}_{D_1, D_2}^{\op{dist}}(A) / t$.

    因为 $t$ 是多项式约束的，所以如果能找到一个可忽略的函数 $\varepsilon(n)$ 使得

    \[
        \varepsilon(n) \geq \op{Adv}_{H_k, H_{k+1}}^{\op{dist}}(A) \geq \op{Adv}_{D_1, D_2}^{\op{dist}}(A) / t
    \]

    便可以说明区分 $D_1$ 和 $D_2$ 的优势是可忽略的.

### Are Quantum Oracles Better Than Samples?

在 GGM Construction 的证明中，第一个混合论证将 $\op{PRF}$ 的敌手转变为了区分随机 Oracle 和一个输出来自底层伪随机生成器的随机值的 Oracle 的算法，而第二个混合论证则表明如何运用这一算法区分某个随机值和伪随机生成器的某个输出，从而破坏了 $\op{PRG}$ 的安全性. 

在量子情况下，第一个混合论证仍然成立，但第二个混合论证造成了现在的局面. 因而，为了完成证明，需要证明对于一个具有量子访问的，输出来自某个分布的 Oracle，其并不会并不会比具有单个样本访问权限的，输出来自同一个分布的 Oracle 更有优势. 

!!! note "Theorem"
    设 $D_1$ 和 $D_2$ 是集合 $\mathcal{Y}$ 上的高效可采样分布，并令 $\mathcal{X}$ 是另一个集合. 设 $O_1$ 和 $O_2$ 是 $\mathcal{X}$ 到 $\mathcal{Y}$ 的函数分布，其中对任一 $x \in \mathcal{X}$，$O_i(x)$ 都是依据 $D_i$ 独立选取的. 如果 $A$ 是一个利用量子查询能够高效区分从 $O_1$ 和 $O_2$ 中选取的 Oracle 的量子算法，那么便可以构建一个高效的量子算法 $B$，用以区分来自 $D_1$ 和 $D_2$ 的样本.

经典情况下，任何算法 $A$ 向 Oracle $O$ 发起 $q$ 次查询后只能得到 $q$ 个输出. 因此，给出 $q$ 个来自 $D_1$ 或 $D_2$ 的样本，便可以惰性模拟 Oracle $O_1$ 或 $O_2$，从而得到一个算法，用来区分来自 $D_1$ 的 $q$ 个样本和来自 $D_2$ 的 $q$ 个样本. 再使用一个简单的混合论证，便可以得到一个区分 $D_1$ 和 $D_2$ 的单个样本的算法.

量子情况下，任何量子算法 $A$ 仅向 Oracle $O_i$ 发起一次查询也能够一次性得到所有输出，这意味着需要指数多个样本才能够精确模拟 $O_i$. 然而，尽管无法通过来自 $D_i$ 的 $q$ 个样本来惰性模拟 $O_i$，但可以通过多项式多个样本来近似模拟 $O_i$. 基本地说，对于每个输入，将输出设置为从样本集合中随机选取的一个样本. 尽管这不完全等同于 $O_i$，但足以证明其与 $O_i$ 是不可区分的. 因此，可以通过算法 $A$ 区分来自 $D_1$ 和 $D_2$ 的多项式多个样本，再次借助混合论证，便可以得到一个区分 $D_1$ 和 $D_2$ 的单个样本的算法.

## Preliminaries and Notation

### Functions and Probabilities

给定两个集合 $\mathcal{X}$ 和 $\mathcal{Y}$，定义 $\mathcal{Y}^\mathcal{X}$ 为函数集合 $f: \mathcal{X} \to \mathcal{Y}$. 如果一个函数 $f$ 将 $\mathcal{X}$ 映射到 $\mathcal{Y} \times \mathcal{Z}$，可以将其视作两个函数，一个将 $\mathcal{X}$ 映射到 $\mathcal{Y}$，另一个将 $\mathcal{X}$ 映射到 $\mathcal{Z}$. 换言之，$(\mathcal{Y} \times \mathcal{Z})^\mathcal{X} = \mathcal{Y}^\mathcal{X} \times \mathcal{Z}^\mathcal{X}$.

给定 $f \in \mathcal{Y}^\mathcal{X}$ 和 $g \in \mathcal{Z}^\mathcal{Y}$，可以定义 $g \circ f$ 为 $g(f(x))$，即二者的复合. 对于 $\mathcal{F} \subset \mathcal{Y}^\mathcal{X}$，$g \circ \mathcal{F} = \{g \circ f : f \in \mathcal{F}\}$. 类似地，可以定义 $\mathcal{G} \circ f = \{g \circ f : g \in \mathcal{G}\}$，以及 $\mathcal{G} \circ \mathcal{F} = \{g \circ f : g \in \mathcal{G}, f \in \mathcal{F}\}$.

给定分布 $D$ 和一些事件 $\op{event}$，记 $\op{Pr}_{x \from D}[\op{event}]$ 为从 $D$ 中随机选取 $x$ 后 $\op{event}$ 发生的概率. 而给定集合 $\mathcal{X}$，偶尔也会滥用记号，记 $\mathcal{X}$ 为其本身上的均匀分布.

给定 $\mathcal{Y}^\mathcal{X}$ 上的分布 $D$ 以及函数 $g \in \mathcal{Z}^\mathcal{Y}$，定义 $\mathcal{Z}^\mathcal{X}$ 上的分布 $g \circ D$ 为先从 $D$ 中随机选取 $f$，再输出 $g \circ f$. 类似地，给定 $\mathcal{Z}^\mathcal{Y}$ 上的分布 $E$ 和函数 $f \in \mathcal{Y}^\mathcal{X}$，可以定义 $E \circ f$ 和 $E \circ D$.

给定集合 $\mathcal{Y}$ 上的分布 $D$，和另一集合 $\mathcal{X}$，定义 $D^{\mathcal{X}}$ 为 $\mathcal{Y}^{\mathcal{X}}$ 上的分布，每个输入的输出都依据 $D$ 独立选取. 

集合 $\mathcal{X}$ 上的两分布 $D_1$ 和 $D_2$ 的距离按如下定义：

\[
    \abs{D_1 - D_2} = \sum_{x \in \mathcal{X}} \abs{D_1(x) - D_2(x)}.
\]

如果 $\abs{D_1 - D_2} \leq \varepsilon$，则称 $D_1$ 和 $D_2$ 是 $\varepsilon$-接近的. 而如果 $\abs{D_1 - D_2} \geq \varepsilon$，则称 $D_1$ 和 $D_2$ 是 $\varepsilon$-远离的.

### Quantum Computation

此处只给出这篇论文所需的部分量子计算的基本事实，可以阅读[[NC00]](https://almuhammadi.com/sultan/books_2020/Nielsen_Chuang.pdf)来了解更多.

!!! info "Fact"
    任何一个经典高效可计算函数 $f$ 都可以被量子计算机高效实现. 此外，$f$ 可以被实现为一个 Oracle，并且可以在量子叠加态上进行查询.

以下的事实来自 Zhandry 的工作[[Zha12]](https://eprint.iacr.org/2012/076.pdf)

!!! info "Fact"
    对任意集合 $\mathcal{X}$ 和 $\mathcal{Y}$，可以高效地构建一个从 $\mathcal{X}$ 到 $\mathcal{Y}$ 的能够处理 $q$ 次量子查询的 Oracle，其中 $q$ 是多项式. 更准确地说，任何量子算法对一个 $2q$-wise 独立函数进行至多 $q$ 次查询等同于向随机函数进行查询.

给定一集合 $\mathcal{Y}$ 上的高效可采样分布 $D$，也可以构建一个从 $D^{\mathcal{X}}$ 中抽取元素的随机函数：设 $\mathcal{Z}$ 是用于从 $D$ 中采样的随机值组合，$f(r)$ 是使用随机值 $r \in \mathcal{Z}$ 得到的元素 $y \in \mathcal{Y}$，那么有 $D^{\mathcal{X}}= f \circ \mathcal{Z}^{\mathcal{X}}$. 所以首先构建一个随机函数 $O' \in \mathcal{Z}^{\mathcal{X}}$，然后令 $O(x) = f(O'(x))$.

记能访问经典 Oracle $O$ 的量子算法为 $A^O$，而能访问量子 Oracle $O$ 的量子算法为 $A^\ket{O}$. 

### Cryptographic Primitives

这篇文章中，总假定敌手是量子计算机. 下面给出伪随机函数和两个安全性定义，以及两种分布的不可区分性的定义.

!!! info "Definition"
    **(PRF)** 伪随机函数是指函数 $\op{PRF} : \mathcal{K} \times \mathcal{X} \to \mathcal{Y}$，其中 $\mathcal{K}$ 是密钥空间，$\mathcal{X}$ 和 $\mathcal{Y}$ 分别是定义域和值域. $\mathcal{K}$，$\mathcal{X}$ 和 $\mathcal{Y}$ 都是安全参数 $n$ 的隐式函数. 记 $y = \op{PRF}_k(x)$.

!!! info "Definition"
    **(Standard-Security)** 一伪随机函数称为具有标准安全性，如果不存在高效的量子敌手 $A$ 通过进行经典查询便能够区分一真随机函数和带有随机参数 $k$ 的函数 $\op{PRF}_k$. 也就是说，对于每个这样的 $A$，存在可忽略函数 $\varepsilon = \varepsilon(n)$ 使得

    \[
        \abs{\op{Pr}_{k \from \mathcal{K}}[A^{\op{PRF}_k}(\cdot) = 1] - \op{Pr}_{O \from \mathcal{Y}^\mathcal{X}}[A^O(\cdot) = 1]} < \varepsilon.
    \]

!!! info "Definition"
    **(Quantum-Security)** 一伪随机函数称为具有量子安全性，如果不存在高效的量子敌手 $A$ 通过进行量子查询便能够区分一真随机函数和带有随机参数 $k$ 的函数 $\op{PRF}_k$. 

称这样的量子安全伪随机函数为**量子随机函数（Quantum Random Function）**，或称 $\op{QPRFs}$.

现在给出分布的不可区分性的定义. 不可区分性的标准看法是认为不存在高效的算法能够区分一分布的样本和另一分布的样本. 

!!! info "Definition"
    **(Indistinguishability)** 集合 $\mathcal{Y}$ 上的两分布 $D_1$ 和 $D_2$ 是计算上（统计意义上）不可区分的，如果不存在高效的（计算无界）的量子算法 $A$ 能够区分 $D_1$ 的一个样本和 $D_2$ 的一个样本. 也就是说，对于每个这样的 $A$，存在可忽略函数 $\varepsilon$ 使得

    \[
        \abs{\op{Pr}_{y \from D_1}[A(y) = 1] - \op{Pr}_{y \from D_2}[A(y) = 1]} < \varepsilon.
    \]

而对本文章的工作，还需要一种似乎更强的不可区分性定义，称之为**Oracle 不可区分性**. 想法是不存在高效的算法能够区分输出依据 $D_1$ 或 $D_2$ 分布的 Oracle.

!!! info "Definition"
    **(Oracle-Indistinguishability)** 集合 $\mathcal{Y}$ 上的两分布 $D_1$ 和 $D_2$ 是计算上（统计意义上）Oracle 不可区分的，如果对于任何集合 $\mathcal{X}$，不存在高效的（计算无界）的量子算法 $B$ 能够用多项式次量子查询区分 $D_1^{\mathcal{X}}$ 和 $D_2^{\mathcal{X}}$. 也就是说，对于每个这样的 $B$ 和 $\mathcal{X}$，存在可忽略函数 $\varepsilon$ 使得

    \[
        \abs{\op{Pr}_{O \from \mathcal{Y}^\mathcal{X}}[B^{\ket{O}}(\cdot) = 1] - \op{Pr}_{O \from \mathcal{Y}^\mathcal{X}}[B^{\ket{O'}}(\cdot) = 1]} < \varepsilon.
    \]

本篇文章主要讨论计算有界敌手，所以不可区分性通常指计算不可区分性. 

依据不可区分性的定义，便可以规范化一开始的定理：

!!! note "Theorem"
    设 $D_1$ 和 $D_2$ 是集合 $\mathcal{Y}$ 上的高效可采样分布，那么 $D_1$ 和 $D_2$ 是不可区分的当且仅当它们也是 Oracle 不可区分的.

## Separation Result

这一部分将展示如下的分离结果：

!!! note "Theorem"
    如果安全的 $\op{PRFs}$ 存在，那么存在并非 $\op{QPRFs}$ 的标准安全的 $\op{PRFs}$.

    ???+ note "Proof"
        设 $\op{PRF}$ 为一标准安全的伪随机函数，密钥空间为 $\mathcal{K}$，定义域为 $\mathcal{X}$，陪域为 $\mathcal{Y}$. 接下来将构建一个新的具有周期性的伪随机函数，其周期数值较大，并且被秘密确定. 经典敌手无法探测到这一周期性，自然也就无法将该函数与真正的随机函数进行区分. 但是，量子敌手可以通过量子查询来探测到这一周期性，从而区分这一函数与真正的随机函数.

        记 $\mathcal{X}$ 为 $[N]$，其中 $N$ 是 $\mathcal{X}$ 中的元素个数. 不失一般性，，假定 $\mathcal{Y}$ 包含至少 $N^2$ 个元素（如果不满足，便以标准方式利用更小的定义域和更大的值域构建新的随机函数）. 接下来构建新的伪随机函数 $\op{PRF}'_{(k, a)} (x) = \op{PRF}_k(x \bmod a)$，其中：

        - $\op{PRF}'$ 的密钥空间 $\mathcal{K'} = \mathcal{K} \times \mathcal{A}$，其中 $\mathcal{A}$ 是 $N/2$ 到 $N$ 之间的所有质数组成的集合. 也就是说，$\op{PRF}'$ 的密钥是一个密钥对 $(k, a)$，其中 $k$ 是 $\op{PRF}$ 的密钥，$a$ 是一个在 $(N/2, N]$ 内的质数.

        - 定义域 $\mathcal{X}' = [N']$，其中 $N'$ 是大于 $4N^2$ 的最小的 $2$ 的幂. 

        接下来的两个断言会在附录中证明：

        !!! success "Claim"
            如果 $\op{PRF}$ 是标准安全的，那么 $\op{PRF}'$ 也是标准安全的.

        !!! success "Claim"
            如果 $\op{PRF}$ 是量子安全的，那么 $\op{PRF}'$ 不是量子安全的.

        所以存在一个标准安全的 $\op{PRF}$，其不是量子安全的.

## Pseudorandom Functions from Pseudorandom Generators

以下将给出 GGM construction，以及新的安全性证明方式，其在量子情况下也能使用.

首先定义伪随机生成器：

!!! info "Definition"
    **(PRG)** 伪随机生成器是指函数 $G: \mathcal{X} \to \mathcal{Y}$，其中 $\mathcal{X}$ 和 $\mathcal{Y}$ 都是安全参数 $n$ 的隐式函数. 

!!! info "Definition"
    **(Standard-Security)** 一伪随机生成器 $G$ 被称为是标准安全的，如果分布 $G \circ \mathcal{X}$ 和 $\mathcal{Y}$ 是计算上不可区分的.

!!! tip "Construction"
    **(GGM-PRF)** 设 $G: \mathcal{K} \to \mathcal{K}^2$ 是一个倍长伪随机生成器. 记 $G(x) = (G_0(x), G_1(x))$，其中 $G_0$ 和 $G_1$ 都是将 $\mathcal{K}$ 映射到 $\mathcal{K}$ 的函数. 接下来定义 GGM 伪随机函数 $\op{PRF}: \mathcal{K} \times [2]^n \to \mathcal{K}$，满足

    \[
        \op{PRF}_k(x) = G_{x_1}(G_{x_2}(\cdots G_{x_{n - 1}}(G_{x_n}(k)))\cdots).
    \]

    也就是说，$\op{PRF}$ 接受密钥空间 $\mathcal{K}$ 中的一个密钥 $k$ 和一个 $n$ 位的输入 $x$. 首先对 $k$ 应用 $G$，根据 $x$ 的最后一位是 $0$ 还是 $1$，选择 $G_0$ 或 $G_1$，. 而选择得到的依然是密钥空间中的一个密钥，再次应用 $G$，直到 $x$ 的所有位都被处理完.

正如介绍中所说，GGM Construction 标准的安全性证明在量子情况下失效，所以需要最开始的定理. 接下来将展示其是如何起效的，而定理本身的证明将在后文给出，这里假定定理成立.

首先还是对伪随机生成器定义一个更强的安全性：

!!! info "Definition"
    **(Oracle-Security)** 一伪随机生成器 $G: \mathcal{X} \to \mathcal{Y}$ 被称为是 Oracle 安全的，如果分布 $G \circ \mathcal{X}$ 和 $\mathcal{Y}$ 是 Oracle 不可区分的.

因为可以先从 $\mathcal{X}$ 中采样一个随机值，然后将 $G$ 应用在其上，所以 $G \circ \mathcal{X}$ 是高效可采样的. 因此 $G \circ \mathcal{X}$ 和 $\mathcal{Y}$ 都是高效可采样的. 那么根据定理，有如下的推论：

!!! success "Corollary"
    如果 $G$ 是一个安全的 $\op{PRG}$，那么 $G$ 也是 Oracle 安全的.

接下来便可以证明上述构造的安全性：

!!! note "Theorem"
    如果 $G$ 是一个标准安全的 $\op{PRG}$，那么按上述构建得到的 $\op{PRF}$ 是一个 $\op{QPRF}$.

    ???+ note "Proof"
        还是采用 Goldreich 等人的证明思路，将任意 $\op{PRF}$ 的敌手转变为一个 $G$ 的 Oracle 安全性敌手. 之前的推论表明在 $G$ 是标准安全的情况下，这样的敌手是不存在的.

        假定一量子敌手 $A$ 可以以概率 $\varepsilon$ 区分 $\op{PRF}$ 和随机 Oracle. 按如下定义混合序列中的元素 $H_i$：选取一个随机函数 $P \from \mathcal{K}^{[2]^{n - i}}$（即将 $(n - i)$ 位的输入映射到 $\mathcal{K}$ 的随机函数），并且给 $A$ 如下的 Oracle：

        \[
            O_i(x) = G_{x_1}(G_{x_2}(\cdots G_{x_i}(P(x_{[i+1, n]})))\cdots).
        \]

        $H_0$ 即 $A$ 的 Oracle 是随机的，而当 $i = n$ 时，$P \from \mathcal{K}^{[2]^{n - i}}$ 就是一个只会将空串映射到 $\mathcal{K}$ 的随机函数. 因此 $H_n$ 就对应 $A$ 的 Oracle 是 $\op{PRF}$ 的情况. 设 $\varepsilon_i$ 是 $A$ 可以区分 $H_i$ 和 $H_{i + 1}$ 的概率，也就是说：

        \[
            \varepsilon_i = \Pr{A^{\ket{O_i}}(\cdot) = 1} - \Pr{A^{\ket{O_{i+1}}}(\cdot) = 1}.
        \]

        通过简单的混合论证便可以得到 $\abs{\sum_i \varepsilon_i} = \varepsilon$.

        接下来构建可以攻破 $G$ 的 Oracle 安全性的敌手 $B$. $B$ 被赋予量子访问 Oracle $P: [2]^{n - 1} \to \mathcal{K}^2$ 的权限，并且用来区分 $P \from (\mathcal{K}^2)^{[2]^{n - 1}}$ 和 $P \from G \circ \mathcal{K}^{[2]^{n - 1}}$. 也就是说，$B$ 被给定一个将 $n - 1$ 位输入映射到 $\mathcal{K}^2$ 的随机函数，或是 $G$ 应用上一个将 $n - 1$ 位输入映射到 $\mathcal{K}$ 的随机函数. 其按如下方法区分这两个情况：

        - 从 $\{0, \ldots, n - 1\}$ 中随机选取 $i$.

        - 设 $P^{(i)}: [2]^{n - i - 1} \to \mathcal{K}^2$ 为 Oracle，满足 $P^{(i)}(x) = P(0^ix)$

        - 记 $P^{(i)}$ 为 $(P^{(i)}_0, P^{(i)}_1)$，其中 $P^{(i)}_b: [2]^{n - i - 1} \to \mathcal{K}$ 是 $P^{(i)}$ 的左半或右半部分.

        - 构建 Oracle $O: [2]^n \to \mathcal{K}$，满足：

            \[
                O(x) = G_{x_1}(G_{x_2}(\cdots G_{x_i}(P^{(i)}_{x_{i+1}}(x_{[i+2, n]})))\cdots).
            \]

        - 模拟带有 Oracle $O$ 的 $A$，并输出其输出.

        注意到每个向 $O$ 发起的量子查询都导致了一个向 $P$ 发起的量子查询，所以 $B$ 发起查询的次数和 $A$ 一致.

        固定 $i$，设 $B_i$ 为 使用这一特定 $i$ 的算法 $B$，当 $P$ 是真随机的情况时，$P^{(i)}$ 也是真随机的，$P^{(i)}_0$ 和 $P^{(i)}_1$ 也因而都是真随机的. 所以 $O = O_i$. 而当 $P$ 是从 $G \circ \mathcal{K}^{[2]^{n - 1}}$ 中随机选取的时候，$P^{(i)}$ 的分布遵循 $G \circ \mathcal{K}^{[2]^{n - i - 1}}$，因此 $P_b \from G_b \circ \mathcal{K}^{[2]^{n - i - 1}}$，从而 $O = O_{i+1}$. 对于固定的 $i$，有

        \[
            \op{Pr}_{P \from (\mathcal{K}^2)^{[2]^{n - 1}}}[B_i^{\ket{P}}(\cdot) = 1] - \op{Pr}_{P \from G \circ \mathcal{K}^{[2]^{n - 1}}}[B_i^{\ket{P}}(\cdot) = 1] = \varepsilon_i.
        \]

        对所有 $i$ 求和取平均，并取绝对值，便有

        \[
            \abs{\op{Pr}_{P \from (\mathcal{K}^2)^{[2]^{n - 1}}}[B^{\ket{P}}(\cdot) = 1] - \op{Pr}_{P \from G \circ \mathcal{K}^{[2]^{n - 1}}}[B^{\ket{P}}(\cdot) = 1]} = \abs{\frac{1}{n} \sum_i \varepsilon_i} = \varepsilon/n.
        \]

        因此 $B$ 攻破了 $G$ 的 Oracle 安全性的概率只比 $A$ 区分 $\op{PRF}$ 和随机 Oracle 的概率小多项式倍，说明是不可忽略的.

## Pseudorandom Functions from Synthesizers

这部分将证明依据 Noar 和 Reingold 提出的伪随机合成器构建的伪随机函数是量子安全的.

!!! info "Definition"
    **(Synthesizer)** 伪随机合成器是指函数 $S: \mathcal{X}^2 \to \mathcal{Y}$，其中 $\mathcal{X}$ 和 $\mathcal{Y}$ 都是安全参数 $n$ 的隐式函数.

!!! info "Definition"
    **(Standard-Security)** 一伪随机合成器 $S: \mathcal{X}^2 \to \mathcal{Y}$ 被称为是标准安全的，如果对任何集合 $\mathcal{Z}$，不存在高效的量子敌手 $A$ 通过进行经典查询便能够区分一真随机函数和 $O(z_1, z_2) = S(O_1(z_1), O_2(z_2))$，其中 $O_b \from \mathcal{X}^\mathcal{Z}$ 是随机函数. 也就是说，对于每个这样的 $A$ 和 $\mathcal{Z}$，存在可忽略函数 $\varepsilon$ 使得

    \[
        \abs{\op{Pr}_{O_1, O_2 \from \mathcal{X}^\mathcal{Z}}[A^{S(O_1, O_2)}(\cdot) = 1] - \op{Pr}_{O \from \mathcal{Y}^{\mathcal{Z} \times \mathcal{Z}}}[A^O(\cdot) = 1]} < \varepsilon.
    \]

    其中 $S(O_1, O_2)$ 指将 $(z_1, z_2)$ 映射到 $S(O_1(z_1), O_2(z_2))$.

!!! tip "Construction"
    **(NR-PRF)** 给定伪随机合成器 $S: \mathcal{X}^2 \to \mathcal{X}$，令 $l$ 为一整数，$n = 2^l$. 设 $\op{PRF}_k (x) = \op{PRF}_k^{(l)}(x)$，其中 $\op{PRF}^{(i)}: (\mathcal{X}^{2 \times 2^i}) \times [2]^{2^i} \to \mathcal{X}$ 按如下方式定义：

    \begin{gather*}
        \op{PRF}_{a_{1, 0}, a_{1, 1}}^{(0)} (x) = a_{1, x} \\
        \op{PRF}_{A_1^{(i - 1)}, A_2^{(i - 1)}}^{(i)} = S(\op{PRF}_{A_1^{(i - 1)}}^{(i - 1)}(x_{[1, 2^{i-1}]}), \op{PRF}_{A_2^{(i - 1)}}^{(i - 1)}(x_{[2^{i-1} + 1, 2^i]})).
    \end{gather*}

    其中

    \begin{gather*}
        A_1^{(i-1)} = (a_{1, 0}, a_{1, 1}, \ldots, a_{2^{i-1}, 0}, a_{2^{i-1}, 1}) \\
        A_2^{(i-1)} = (a_{2^{i-1} + 1, 0}, a_{2^{i-1} + 1, 1}, \ldots, a_{2^i, 0}, a_{2^i, 1}).
    \end{gather*}

    也就是说，$\op{PRF}$ 接受一个由 $\mathcal{X}$ 中的 $2 \times 2^l$ 个元素组成的密钥 $k$ 和一个 $n$ 位的输入 $x$. 其使用 $x$ 选取密钥中的 $2^l$ 个元素，并将它们两两配对. 然后其在每对元素上应用 $S$，得到 $\mathcal{X}$ 中的 $2^{l-1}$ 个元素. 接着，其继续对这些元素进行配对，并将 $S$ 应用在每对元素上，直到最后得到一个元素，便是 $\op{PRF}$ 的输出.

下面的定理将在附录中证明：

!!! note "Theorem"
    如果 $S$ 是一个标准安全的伪随机合成器，那么按上述构建得到的 $\op{PRF}$ 是一个 $\op{QPRF}$.

## Direct Construction of Pseudorandom Functions

这部分将呈现 Banerjee, Peikert 和 Rosen 构建伪随机函数的方法，并且证明其是量子安全的.

设 $p, q$ 均为整数，并且 $q > p$. 令 $\lfloor x \rceil_q$ 为 $\mathbb{Z}_q$ 到 $\mathbb{Z}_p$ 的映射，定义方式为将 $x$ 舍入到最接近的 $q/p$ 的倍数，在将其转换为 $\mathbb{Z}_p$ 中的元素. 更准确的说，$\lfloor x \rceil_q = \lfloor (p/q)x \rceil \bmod p$.

!!! tip "Construction"
    设 $p, q, m, l$ 为整数且 $q > p$. 设 $\mathcal{K} = \mathbb{Z}^{n \times m} \times (\mathbb{Z}^{n \times n})^l$. 定义 $\op{PRF}: \mathcal{K} \times [2]^l \to \mathbb{Z}_p^{m \times n}$，满足对任意密钥 $k = (\mathbf{A}, \{\mathbf{S_i}\})$，令

    \[
        \op{PRF}_k(x) = \lfloor \mathbf{A}^t \prod_{i = 1}^l \mathbf{S}_i^{x_i} \rceil_q.
    \]

    函数 $\op{PRF}$ 使用一个由 $n \times m$ 阶的矩阵 $\mathbf{A}$ 和 $l$ 个 $n \times n$ 阶矩阵 $\mathbf{S}_i$ 组成的密钥，其中的元素都是整数模 $q$ 的结果. 其使用一个 $l$ 位的输入来选择 $\mathbf{S}_i$ 的一个子集，并将它们相乘. 这一乘积再左乘 $\mathbf{A}$ 的转置，最后对结果进行模 $p$ 的舍入操作. 
    
接下来是 $\op{PRF}$ 安全性的一个非正规描述，证明将在附录中给出.

!!! note "Theorem"
    设 $\op{PRF}$ 是按上述构建得到的伪随机函数. 对于恰当选取的整数 $p, q, m, l$，以及 $\mathbb{Z}$ 上的分布 $\chi$，如果选取 $\mathbf{A} \from \mathbb{Z}^{n \times m}_q$ 和 $\mathbf{S}_i \from \chi^{n \times n}$，并且 LWE 问题对于模数 $q$ 和分布 $\chi$ 是困难的，那么 $\op{PRF}$ 是一个 $\op{QPRF}$.

## Distinguishing Oracle Distributions

我们描述了一些工具用于论证量子算法无法区分两种 Oracle 分布，并且最终完成一开始的定理的证明. 设 $\mathcal{X}$ 和 $\mathcal{Y}$ 是集合，首先从 Zhandry 的两个定理开始：

!!! note "Theorem"
    设 $A$ 是一个对 Oracle $H: \mathcal{Y}^\mathcal{X}$ 进行 $q$ 次量子查询的量子算法. 如果 $H$ 是从某个分布 $D$ 中抽取的，那么对每个 $z$，概率 $\op{Pr}_{H \from D}[A^{\ket{H}}(\cdot) = z]$ 是所有可能的 $x_i$ 和 $r_i$ 设置下，概率 $\op{Pr}_{H \from D}[H(x_i) = r_i], \forall i \in \{1, \ldots, 2q\}$ 的线性组合.


!!! note "Theorem"
    固定 $q$，令 $D_\lambda$ 为 $\mathcal{Y}^\mathcal{X}$ 上的一族分布，并由 $\lambda \in [0, 1]$ 索引. 假定存在一个整数 $d$ 使得对于每 $2q$ 个对 $(x_i, r_i) \in \mathcal{X} \times \mathcal{Y}$，函数 $p(\lambda) = \op{Pr}_{H \from D_\lambda}[H(x_i) = r_i], \forall i \in \{1, \ldots, 2q\}$ 是一个 $\lambda$ 的至多 $d$ 次多项式. 那么进行 $q$ 次量子查询的量子算法的输出分布在 $D_\lambda$ 和 $D_0$ 下的输出分布是 $2\lambda d^2$-接近的.

接下来展示一个类似的结果：

!!! note "Theorem"
    固定 $q$，令 $E_r$ 为 $\mathcal{Y}^\mathcal{X}$ 上的一族分布，并由 $r \in \mathbb{Z}^+ \cup \{\infty\}$ 索引. 假定存在一个整数 $d$ 使得对于每 $2q$ 个对 $(x_i, r_i) \in \mathcal{X} \times \mathcal{Y}$，函数 $p(\lambda) = \op{Pr}_{H \from E_{1/\lambda}}[H(x_i) = r_i], \forall i \in \{1, \ldots, 2q\}$ 是一个 $\lambda$ 的至多 $d$ 次多项式. 那么进行 $q$ 次量子查询的量子算法的输出分布在 $E_{1/\lambda}$ 和 $E_\infty$ 下的输出分布是 $\pi^2 d^3/3r$-接近的.

    ???+ note "Sketch of Proof"
        令 $D_\lambda = E_{1/\lambda}$. 可见上述两定理的大部分条件是一致的，除了前者要求 $D_\lambda$ 对 $\lambda \in [0, 1]$ 是一个分布族，而后者只要求当 $1/\lambda$ 为整数（或 $\lambda = 0$）时是一个分布族. 证明思路也是类似的，前者使用了一个著名的界约束，其条件为当 $x \in [0, 1]$ 时 $f(x) \in [0, 1]$，而后者只要去当 $1/x$ 为整数时 $f(x) \in [0, 1]$. 这样的函数很少被研究，因此需要在这样的放松下找到合适的界约束. 证明将在附录中给出.

接下来的部分将会把该定理应用到一族新的分布中，从而证明一开始的定理.

### Small-Range Distributions

现在将该定理运用到被称为小值域分布的一个新的 Oracle 上的分布. 给定 $\mathcal{Y}$ 省的一个分布 $D$，定义如下的从 $\mathcal{X}$ 到 $\mathcal{Y}$ 上的函数的分布 $\op{SR}_r^D(x)$：

- 对每个 $i \in [r]$，依据分布 $D$ 从 $\mathcal{Y}$ 中选取一个随机值 $y_i$.

- 对每个 $x \in \mathcal{X}$，随机选取一个 $i \in [r]$，设 $O(x) = y_i$.

在上下文自明的情况下常常省略定义域 $\mathcal{X}$.

以下的引理将在附录中证明：

!!! success "Lemma"
    固定 $k$，对于任意 $\mathcal{X}$，在 $\op{SR}_r^D$ 的每个边际分布中，关于 $k$ 个输入的概率是 $1/r$ 的 $k$ 次多项式.

也可以用如下的视角来理解这个引理：选择 $g \from D^{[r]}$，$f \from [r]^\mathcal{X}$，输出便是 $g \circ f$. 即 $\op{SR}_r^D(\mathcal{X}) = D^{[r]} \circ [r]^\mathcal{X}$. 换而言之，也就是随机选取从 $\mathcal{X}$ 映射到 $[r]$ 的函数 $f$，然后将其与另一个 $[r]$ 到 $\mathcal{Y}$ 的函数 $g$ 组合，而 $g$ 的输出依据 $D$ 来分布. 这一分布被称为小值域分布，因为任何从这一分布中采样的函数的像的集合都被限制在至多 $r$ 个点，而 $r \ll \abs{\mathcal{Y}}$，$[r]$ 便是陪域的一个小子集. 注意到当 $r$ 趋近于无穷时，$f$ 为单射的概率趋近于 $1$. 因此对每个 $x$，$g(f(x))$ 的值将会独立地依据 $D$ 分布，也就有 $\op{SR}_\infty^D(\mathcal{X}) = D^\mathcal{X}$. 因此可以依据上述定理去约束任何量子算法区分 $\op{SR}_r^D$ 和 $\op{SR}_\infty^D = D^\mathcal{X}$ 的能力.

!!! success "Corollary"
    一量子算法向从 $\op{SR}_r^D$ 中抽取的 Oracle 进行 $q$ 次量子查询得到的输出分布与向从 $D^\mathcal{X}$ 中抽取的 Oracle 进行 $q$ 次量子查询得到的输出分布是 $l(q)/r$-接近的，其中 $l(q) = \pi^2 (2q)^3/3 < 27q^3$.

这一约束是紧的，在附录中会展示由 Brassard, Høyer 和 Tapp 提出的量子碰撞寻找算法可以以最优的概率区分 $\op{SR}_r^D$ 和 $D^\mathcal{X}$.

### The Equivalence of Indistinsguishability and Oracle-Indistinguishability

现在可以用以上的技术来探究不可区分性和 Oracle 不可区分性之间的关系，并且证明最初的定理.显然，Oracle 不可区分性意味着不可区分性，因为如果 $A$ 可区分 $D_1$ 和 $D_2$，那么算法 $B^{\ket{O}}(\cdot)$ 以 $x \in \mathcal{X}$ 为输入，返回 $A(O(x))$，便攻破了 Oracle 不可区分性. 

而经典情况下的另一个方向可以通过构建混合序列来证明. 但是在量子情况下，这一方法并不适用，因为量子算法可以查询叠加态，每次查询可能包括指数级的输入. 

在统计意义下，这一问题已经被 Boneh 等人解决. 他们证明了如果一个（潜在无界）的量子敌手通过 $q$ 次查询便可以以 $\varepsilon$ 的概率区分 $D_1^{\mathcal{X}}$ 和 $D_2^{\mathcal{X}}$，那么 $D_1$ 和 $D_2$ 一定是 $\Omega(\varepsilon^2/q^4)$-远离的. 现在便可以通过以上的工具将这一结果扩展到计算意义下，并且在这一过程中提升统计意义下的界限.

???+ note "Proof"
    设 $B$ 是一个高效的量子算法，以不可忽略的概率 $\varepsilon$ 区分 $D_1^{\mathcal{X}}$ 和 $D_2^{\mathcal{X}}$，其中 $D_1$ 和 $D_2$ 是 $\mathcal{Y}$ 上的分布. 也就是说，对某个集合 $\mathcal{X}$，满足

    \[
        \abs{\op{Pr}_{O \from D_1^{\mathcal{X}}}[B^{\ket{O}}(\cdot) = 1] - \op{Pr}_{O \from D_2^{\mathcal{X}}}[B^{\ket{O}}(\cdot) = 1]} = \varepsilon.
    \]

    目标是构建一个高效的量子算法 $A$ 能够区分 $D_1$ 和 $D_2$ 中的样本. 为此，选择 $r$ 使得 $l(q) / r = \varepsilon / 4$. 因而，不存在量子算法可以以高于 $\varepsilon / 4$ 的概率区分 $\op{SR}_r^{D_i}$ 和 $D_i^\mathcal{X}$. 依据三角不等式，有

    \[
        \abs{\op{Pr}_{O \from \op{SR}_r^{D_1}}[B^{\ket{O}}(\cdot) = 1] - \op{Pr}_{O \from \op{SR}_r^{D_2}}[B^{\ket{O}}(\cdot) = 1]} \geq \varepsilon / 2.
    \]

    现在按如下构建 $r + 1$ 个实例的混合序列 $H_i$：对 $j = 0, \ldots, i - 1$，选取 $y_j \from D_1$，对 $j = i, \ldots, r - 1$，选取 $y_j \from D_2$. 然后定义 Oracle $O$ 对每个 $x$，$O(x)$ 随机选取 $y_i$，并且 $B$ 可以查询 $O$ 的输出. 因此 $H_r$ 就是 $O \from \op{SR}_r^{D_1}$ 的情况，而 $H_0$ 就是 $O \from \op{SR}_r^{D_2}$ 的情况. 因此 $H_0$ 和 $H_r$ 需要被以至少 $\varepsilon / 2$ 的概率区分. 令

    \[
        \varepsilon_i = \op{Pr}_{O \from H_{i+1}}[B^{\ket{O}}(\cdot) = 1] - \op{Pr}_{O \from H_i}[B^{\ket{O}}(\cdot) = 1].
    \]

    为 $B$ 区分 $H_i$ 和 $H_{i+1}$ 的概率. 因而就有 $\abs{\sum_{i = 1}^r \varepsilon_i} \geq \varepsilon / 2$. 

    现在构造一算法 $A$ 能够以 $\varepsilon / 2r$ 的概率区分 $D_1$ 和 $D_2$. $A$ 以 $y$ 为输入，按如下工作：

    - 随机选取 $i \in [r]$.

    - 构造一个随机 Oracle $O_0 \from [r]^\mathcal{X}$.

    - 构建随机 Oracle $O_1 \from D_1^{\{0, \ldots, i - 1\}}$ 和 $O_2 \from D_2^{\{i + 1, \ldots, r - 1\}}$.

    - 构建如下的 Oracle $O$：

        - 计算 $j = O_0(x)$.

        - 如果 $j = i$，则输出 $y$.

        - 否则，如果 $j < i$，则输出 $O_1(j)$，如果 $j > i$，则输出 $O_2(j)$.

    - 模拟 $B$ 以 $O$ 为 Oracle 的行为，并输出其输出.

    令 $A_i$ 为 使用 $i$ 的算法 $A$. 如果 $i \from D_1$，那么 $B$ 所见的便是 $H_{i+1}$，而如果 $i \from D_2$，那么 $B$ 所见的便是 $H_i$. 因此

    \[
        \op{Pr}_{y \from D_1}[A_i(y) = 1] - \op{Pr}_{y \from D_2}[A_i(y) = 1] = \varepsilon_i.
    \]

    对所有 $i$ 求和取平均，就能得到 $A$ 的区分概率：

    \[
        \abs{\op{Pr}_{y \from D_1}[A(y) = 1] - \op{Pr}_{y \from D_2}[A(y) = 1]} = \abs{\frac{1}{r} \sum_{i = 1}^r \varepsilon_i} \geq \frac{\varepsilon}{2r} = \frac{\varepsilon^2}{8l(q)}.
    \]

    因此 $A$ 能够以不可忽略的概率区分 $D_1$ 和 $D_2$，这就完成了证明.

注意到如果去除 $B$ 为高效算法的要求，这也就得到了一个统计意义下的证明. 所以如果任何一个进行 $q$ 次查询的计算无界的量子算法能够以 $\varepsilon$ 的概率区分 $D_1$ 和 $D_2$，那么 $D_1$ 和 $D_2$ 一定是 $\Omega(\varepsilon^2/l(q)) = \Omega(\varepsilon^2/q^3)$-远离的，提升了统计意义下的界限.

## Appendix

### Proof of the Separation Result

???+ success "Proof of Claim 1"