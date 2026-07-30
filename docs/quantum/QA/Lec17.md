# Continuous-time quantum walk

## Continuous-time quantum walk

随机游走有离散时间和连续时间两种形式. 先考虑连续时间随机游走的量子类比. 给定图 $G = (V, E)$，$A$ 为其邻接矩阵，对于 $j, k \in V$，其元素定义为

\[
    A_{j, k} = \begin{cases}
        1, & (j, k) \in E, \\
        0, & (j, k) \notin E.
    \end{cases}
\]

特别地，不允许自环的话 $A$ 的对角线元素均为 $0$. 另一个同等重要的矩阵是 $G$ 的 Laplacian $L$，定义为

\[
    L_{j, k} = \begin{cases}
        -\deg(j), & j = k, \\
        1, & (j, k) \in E, \\
        0, & \text{otherwise}.
    \end{cases}
\]

其中 $\deg(j)$ 是顶点 $j$ 的度数. 使用这个定义是因为此时 $L$ 是连续统下的拉普拉斯算子 $\Delta = \nabla^2$ 的离散近似.

$G$ 上的连续时间随机游走定义为以下的微分方程的解：

\[
    \frac{\mathrm{d} }{\mathrm{d} t} p_j(t) = \sum_{k \in V} L_{j, k} p_k(t),
\]

其中 $p_j(t)$ 是在时间 $t$ 时刻位于顶点 $j$ 的概率. 这可以看作是扩散方程的一个离散类比. 注意到

\[
    \frac{\mathrm{d} }{\mathrm{d} t} \sum_{j \in V} p_j(t) = \sum_{j, k \in V} L_{j, k} p_k(t) = 0,
\]

这表明初始归一化的分布保持归一化，连续时间随机游走在任何时间 $t$ 的演化都是一个随机过程. 该微分方程的闭合解为

\[
    p(t) = e^{L t} p(0).
\]

注意到该微分方程实际上和量子力学中的 Schrödinger 方程类似：

\[
    \i \frac{\mathrm{d} }{\mathrm{d} t} \ket{\psi} = H \ket{\psi},
\]

只是其缺少因子 $\i$. 如果插入因子 $\i$，并将概率 $p_j(t)$ 重命名为量子振幅 $q_j(t) = \innerproduct{j}{\psi(t)}$，便可以得到方程

\[
    \i \frac{\mathrm{d} }{\mathrm{d} t} q_j(t) = \sum_{k \in V} L_{j, k} q_k(t).
\]

这就是以图 $G$ 的 Laplacian $L$ 作为 Hamiltonian 的 Schrödinger 方程. 因为 $L$ 是 Hermitian 矩阵，所以动力学在 $\frac{\mathrm{d} }{\mathrm{d} t} \sum_j \lvert q_{j \in V}(t) \rvert^2 = 0$ 下保持归一化. 同样可以给出其闭合解，此处为 $\ket{\psi(t)} = e^{-\i L t} \ket{\psi(0)}$.

也可以使用任何与 $G$ 的结构相关的 Hermitian Hamiltonian 来定义连续时间量子游走，如 $G$ 的邻接矩阵 $A$，尽管其不能作为连续时间经典随机游走的生成元. 

## Random and quantum walks on the hypercube

考虑布尔超立方体，顶点集 $V = \{0, 1\}^n$，边集为所有 Hamming 距离为 1 的顶点对，即 $E = \{(x, y) \in V^2 : \delta(x, y) = 1\}$. $n = 1$ 时，超立方体是一个包含两个顶点和一条边的图，对应的邻接矩阵为

\[
    \sigma_x = \begin{pmatrix}
        0 & 1 \\
        1 & 0
    \end{pmatrix}.
\]

对于一般的 $n$，这个图为 $1$-维超立方体的 $n$ 重笛卡尔积，其邻接矩阵为

\[
    A = \sum_{j=1}^n \sigma_x^{(j)},
\]

其中 $\sigma_x^{(j)}$ 表示 $\sigma_x$ 作用在第 $j$ 个比特上，而对其他比特作用单位矩阵. 简单起见考虑以邻接矩阵 $A$ 作为 Hamiltonian 的量子游走. 因为上式各项相互对易，所以描述该游走演化的酉算子为

\begin{align*}
    e^{-\i A t} & = \prod_{j=1}^n e^{-\i \sigma_x^{(j)} t} \\
                & = \bigotimes_{j=1}^n \begin{pmatrix}
                    \cos t & -\i \sin t \\
                    -\i \sin t & \cos t
                \end{pmatrix}.
\end{align*}

在时间 $t = \pi / 2$，该算子将翻转态的每个比特，将任何输入状态 $\ket{x}$ 映射到对顶点 $\ket{\bar{x}}$. 而考虑从顶点 $x$ 开始的离散时间或连续时间经典随机游走，因为游走迅速达到超立方体所有 $2^n$ 个顶点上的均匀分布，所以在任何时刻到达对顶点 $\bar{x}$ 的概率都是指数级小的. 这个简单的例子表明，随机游走和量子游走可以表现出截然不同的行为.

## Random and quantum walks in one dimension

最著名的随机游走例子是在无限路径上的情况，顶点集 $V = \mathbb{Z}$，$(j, k) \in E$ 当且仅当 $\lvert j - k \rvert = 1$. 从原点开始的随机游走在时间 $t$ 内移动的距离通常正比于 $\sqrt{t}$，无论连续时间还是离散时间的随机游走都是如此. 接下来考虑相应的量子游走. 

为了计算量子游走的行为，需要对角化相应的 Hamiltonian. 该图的 Laplacian 的特征态为动量态 $\ket{\hat{p}}$，诸分量为

\[
    \innerproduct{j}{\hat{p}} = e^{\i p j},
\]

其中 $p \in [-\pi, \pi]$. 而

\begin{align*}
    \bra{j} L \ket{\hat{p}} & = \innerproduct{j + 1}{\hat{p}} + \innerproduct{j - 1}{\hat{p}} - 2 \innerproduct{j}{\hat{p}} \\
                            & = (e^{\i (p (j + 1))} + e^{\i (p (j - 1))} - 2 e^{\i (p j)}) \\
                            & = e^{\i (p j)} (e^{\i p} + e^{-\i p} - 2) \\
                            & = 2 ( \cos p - 1 ) \innerproduct{j}{\hat{p}}.
\end{align*}

所以对应的特征值为 $\lambda_p = 2 ( \cos p - 1 )$. 因此在时间 $t$ 内从 $j$ 游走到 $k$ 的振幅为

\begin{align*}
    \bra{k}e^{-\i L t}\ket{j} & = \frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{-2\i t ( \cos p - 1 )} \innerproduct{k}{\hat{p}} \innerproduct{\hat{p}}{j} \mathrm{d} p \\
    & = \frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{\i p (k - j) - 2\i t ( \cos p - 1 )} \mathrm{d} p \\
    & = e^{2\i t} (-\i)^{k - j} J_{k - j}(2 t),
\end{align*}

其中 $J_\nu$ 是阶为 $\nu$ 的第一类 Bessel 函数. 当 $\nu \gg t$ 时，$J_\nu(t)$ 是指数级小的；$\nu \approx t$ 时，为 $\nu^{-1/3}$ 量级；$\nu \ll t$ 时，为 $\nu^{-1/2}$ 量级. 因此这实际描述了一个传播速度为 $2$ 的波.

可以使用类似的计算来精确描述相应的连续时间经典随机游走，其只是在量子情况下将 $t $ 替换为 $\i t$ 的解析延拓. 时间 $t$ 内从 $j$ 游走到 $k$ 的概率为

\[
    [e^{L t}]_{k, j} = e^{-2 t} I_{k - j}(2 t),
\]

其中 $I_\nu$ 是阶为 $\nu$ 的修正第一类 Bessel 函数. 对于较大的 $t$，该表达式近似于 $\frac{1}{\sqrt{4 \pi t}} \exp\left(-(k - j)^2/4t\right)$，一个宽度为 $\sqrt{2 t}$ 的高斯分布，符合经典随机游走的扩散行为.

## Black-box traversal of the glued trees graph

量子游走的行为可能与经典游走的行为截然不同. 接下来是一个可以展示量子游走能力的例子，其可以比任何经典算法指数级更快地解决这一黑盒问题.

考虑一个图，由两棵高度为 $n$ 的平衡二叉树开始，然后通过一个长度为 $2 \cdot 2^n$ 的随机环交替地将两棵树的叶子连接起来. 如果从某棵树的根开始随机游走，那么其会迅速在叶子连接部分迷失，到达对侧树的根的概率很小. 事实上，通过以仅支持局部探索的方式定义该图的结构，可以确保从某棵树的根节点出发的任何经典算法都无法高效地抵达对侧树的根节点. 但量子游走会在上界为 $\op{poly}(n)$ 的时间内在对侧树的根节点生成一个下界为 $1/\op{poly}(n)$ 的重叠度的量子态.

为了建立经典和量子策略之间可证明的分离，将以查询复杂度的方式表述图遍历问题. 设 $G = (V, E)$ 是一个顶点为 $N$ 的图，令 $m$ 为满足 $2^m \geq N$ 的整数，并令 $k$ 至少为 $G$ 的最大度数. 对每个顶点 $a \in V$，分配一个不同的 $m$ 位字符串 $\op{name}(a)$ 作为其名称，并且不将 $11\cdots1$ 分配给任何顶点. 对于每个 $b \in V$ 且 $(a, b) \in E$，为有序对 $(a, b)$ 分配 $\{1, 2, \ldots, k\}$ 中的一个唯一标签 $\op{label}(a, b)$. 对于 $a \in \{0, 1\}^m$ 和 $c \in \{1, 2, \ldots, k\}$，定义 $v_c(a)$ 为跟随 $a$ 的标号为 $c$ 的出边所到达的顶点的名称；而如果没有名为 $a$ 或没有从 $a$ 出发的标号为 $c$ 的出边，则令 $v_c(a) = 11\cdots1$. $G$ 的黑盒函数以 $a \in \{0, 1\}^m$ 和 $c \in \{1, 2, \ldots, k\}$ 作为输入，并输出 $v_c(a)$. 

设 $G$ 是一个图，$\op{ENTRANCE}$ 和 $\op{EXIT}$ 是 $G$ 的两个顶点，给定如上所述的 $G$ 的黑盒，并额外承诺 $\op{name}(\op{ENTRANCE}) = 00\cdots0$，目标是输出 $\op{EXIT}$ 的名称. 如果一个算法的运行时间是 $m$ 的多项式，那么称其为高效的.

随机游走问题不一定是这个问题的最佳经典策略. 即便随机游走不行，也存在一个遍历 $n$ 维超立方体的高效经典算法. 然而，没有经典算法可以