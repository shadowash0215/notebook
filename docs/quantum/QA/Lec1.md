# Preliminaries

## Quantum data

对于 $n$ 个量子比特的系统，其状态可以表示为如下形式

\[
    \ket{\psi} = \sum_{x \in \{0,1\}^n} a_x \ket{x},
\]

其中 $a_x \in \mathbb{C}$，并且满足归一化条件 $\sum_x \lvert a_x \rvert^2 = 1$. 基态 $\ket{x}$ 被称作计算基（Computational basis）.

更抽象地，考虑群 $G$，基态 $\ket{g}$ 对应群元素 $g \in G$，则群上的任意量子态可以表示为

\[
    \ket{\phi} = \sum_{g \in G} b_g \ket{g}.
\]

## Quantum circuits

对量子态的操作需要保持归一化，酉算子（unitary operator）是最常用的操作. 酉算子 $U$ 满足 $U^\dagger U = U U^\dagger = I$.

为了高效计算，酉算子都是由量子电路实现的.

## Universal gate sets

任何 $n$ 量子比特的酉算子都可以由 1 量子比特门和 2 量子比特门组合而成. 全部的 1 量子比特门和 2 量子比特门便被称为通用门集（Universal gate set）. 

在实际情况下，某些酉算子可能是较为复杂的，这个时候进行一些近似是必要的. 称带有门 $U_1, U_2, \ldots, U_t$ 的量子电路为 $U$ 的 $\epsilon$-近似，如果

\[
    \lVert U - U_t U_{t-1} \cdots U_1 \rVert \leq \epsilon,
\]

$\lVert \cdot \rVert$ 是算子范数，当 $\lVert U - V \rVert$ 很小时， $U$ 和 $V$ 应当难以区分. 一个自然的选择是谱范数

\[
    \lVert A \rVert := \max_\ket{\psi} \frac{\lVert A \ket{\psi} \rVert}{\lVert \ket{\psi} \rVert}.
\]

其中 $\lVert \ket{\psi} \rVert := \sqrt{\innerproduct{\psi}{\psi}}$ 是 2-范数. 谱范数实际上就是 $A$ 的最大奇异值.

$\{H, T, C \}$ 是一个通用门集，其中

\[
    H := \frac{1}{\sqrt{2}} \begin{pmatrix}
        1 & 1 \\
        1 & -1
    \end{pmatrix}, \quad
    T := \begin{pmatrix}
        e^{\i \pi/8} & 0 \\
        0 & e^{-\i \pi/8}
    \end{pmatrix}, \quad
    C := \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 0 & 1 \\
        0 & 0 & 1 & 0
    \end{pmatrix}.
\]