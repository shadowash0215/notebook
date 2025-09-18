# Quantum circuits

## Quantum algorithms

## Single qubit operations

Pauli 矩阵：

\[
    X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad
    Y = \begin{bmatrix} 0 & -\i \\ \i & 0 \end{bmatrix}, \quad
    Z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}.
\]

Hadamard 门，相位门，以及 $\pi/8$ 门：

\[
    H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}, \quad
    S = \begin{bmatrix} 1 & 0 \\ 0 & \i \end{bmatrix}, \quad
    T = \begin{bmatrix} 1 & 0 \\ 0 & e^{\i\pi/4} \end{bmatrix}.
\]

其中有 $H = (X + Z) / \sqrt{2}$，以及 $S = T^2$.

$(a, b)$ 与 Bloch 球面上的 $(\theta, \varphi)$ 之间的关系：

\[
    a = \cos(\theta/2), \quad b = e^{\i\varphi} \sin(\theta/2).
\]

向量 $(\cos(\varphi)\sin(\theta), \sin(\varphi)\sin(\theta), \cos(\theta))$ 被称为 Bloch 向量.

以下是沿着 $\hat{x}$, $\hat{y}$, $\hat{z}$ 方向的旋转门：

\begin{align*}
    R_x(\theta) & = e^{-\i\theta X/2} = \cos(\frac{\theta}{2}) I - \i\sin(\frac{\theta}{2}) X = \begin{bmatrix} \cos(\frac{\theta}{2}) & -\i\sin(\frac{\theta}{2}) \\ -\i\sin(\frac{\theta}{2}) & \cos(\frac{\theta}{2}) \end{bmatrix} \\
    R_y(\theta) & = e^{-\i\theta Y/2} = \cos(\frac{\theta}{2}) I - \i\sin(\frac{\theta}{2}) Y = \begin{bmatrix} \cos(\frac{\theta}{2}) & -\sin(\frac{\theta}{2}) \\ \sin(\frac{\theta}{2}) & \cos(\frac{\theta}{2}) \end{bmatrix} \\
    R_z(\theta) & = e^{-\i\theta Z/2} = \cos(\frac{\theta}{2}) I - \i\sin(\frac{\theta}{2}) Z = \begin{bmatrix} e^{-\i\frac{\theta}{2}} & 0 \\ 0 & e^{\i\frac{\theta}{2}} \end{bmatrix}.
\end{align*}

如果 $\hat{n} = (n_x, n_y, n_z)$ 是一个三维实单位向量，那么沿着 $\hat{n}$ 方向旋转 $\theta$ 的旋转门可以表示为：

\[
    R_{\hat{n}}(\theta) = \exp(-\i\theta \hat{n} \cdot \vec{\sigma}/2) = \cos(\frac{\theta}{2}) I - \i\sin(\frac{\theta}{2}) (n_x X + n_y Y + n_z Z).
\]

!!! note "Theorem"
    ($Z$-$Y$ decomposition for a single qubit) 设 $U$ 是一个单比特门，那么存在实数 $\alpha, \beta, \gamma, \delta$ 使得：

    \[
        U = e^{\i\alpha} R_z(\beta) R_y(\gamma) R_z(\delta).
    \]

!!! success "Corollary"
    设  $U$ 是一个单比特门，那么存在单比特门 $A, B, C$ 满足 $ABC = I$ 使得

    \[
        U = e^{\i\alpha} A X B X C.
    \]

## Controlled operations

假定 $U$ 是一个单比特门，那么受控-$U$ 操作是一个二比特门，如果控制量子比特设置了的话，那么它会对目标量子比特施加 $U$ 操作，即 $\ket{c}\ket{t} \mapsto \ket{c}U^c\ket{t}$.

!!! tip "受控 $U$ 门的实现过程"
    基于 $U = \exp(\i\alpha) A X B X C$ 的分解实现.

    1. 未设置控制比特的情况下，对目标比特施加 $ABC = I$ 操作.

    2. 设置控制比特的情况下，对目标比特施加 $\exp(\i\alpha)A X B X C$ 操作.

    因而只需要实现受控 $X$ 门和受控 $\exp(\i\alpha)$ 相位门. 而受控 $\exp(\i\alpha)$ 相位门的形式等同于控制比特经过矩阵 $\begin{pmatrix} 1 & 0 \\ 0 & e^{\i\alpha} \end{pmatrix}$ 的变换.

现在假定有 $n + k$ 个比特，$U$ 是一个 $k$ 比特门，那么定义控制门 $C^n(U)$ 为：

\[
    C^n(U) \ket{x_1x_2\cdots x_n} \ket{\psi} = \ket{x_1x_2\cdots x_n} U^{x_1x_2\cdots x_n} \ket{\psi}.
\]

$U$ 上的指数表示乘积，所以这个控制门只在所有控制比特都设置的情况下才会施加 $U$ 操作.

以下电路用于构造一个 $C^2(U)$ 门，其中 $V$ 是酉门并且满足 $V^2 = U$：

\qcircuit
    & \qw & \ctrl{1} & \qw & \ctrl{1} & \ctrl{2} & \qw \\
    & \ctrl{1} & \targ & \ctrl{1} & \targ & \qw & \qw \\
    & \gate{V} & \qw & \gate{V^\dagger} & \qw & \gate{V} & \qw \\

## Measurement

**延迟测量准则(Principle of deferred measurement)**：测量总可以从中间态推迟到最后. 如果使用了测量结果，那么所有经典受控操作都可以更换为量子的受控操作.

**隐式测量准则(Principle of implicit measurement)**：不失一般性，所有未终结的量子导线（没测量过的量子比特）都可以假设其在最后被测量.

## Universal quantum gates

### Two-level unitary gates are universal

只对态的两个或更少部分进行作用的门称为 two-level 的酉门.

首先从 $3 \times 3$ 酉矩阵开始，设 $U$ 具有形式：

\[
    U = \begin{bmatrix} a & d & g \\ b & e & h \\ c & f & j \end{bmatrix}.
\]

接下来去寻找 $U_1, \ldots, U_3$ 这几个 two-level 酉矩阵，满足

\[
    U_3 U_2 U_1 U = I.
\]

从而就有

\[
    U = U_1^\dagger U_2^\dagger U_3^\dagger.
\]

显然 two-level 酉矩阵的共轭转置也是 two-level 酉矩阵. 接下来展示如何构造 $U_1, U_2, U_3$.

1. 如果 $b = 0$，那么 $U_1 = I$，否则 $U_1 = \begin{pmatrix} \frac{a^*}{\sqrt{\lvert a \rvert^2 + \lvert b \rvert^2}} & \frac{b^*}{\sqrt{\lvert a \rvert^2 + \lvert b \rvert^2}} & 0 \\ \frac{b}{\sqrt{\lvert a \rvert^2 + \lvert b \rvert^2}} & -\frac{a}{\sqrt{\lvert a \rvert^2 + \lvert b \rvert^2}} & 0 \\ 0 & 0 & 1 \end{pmatrix}$. 作用就是为了消去 $b$. 设

    \[
        U_1 U = \begin{pmatrix} a' & d' & g' \\ 0 & e' & h' \\ c' & f' & j' \end{pmatrix}.
    \]

2. 如果 $c' = 0$，那么 $U_2 = \begin{pmatrix} a'^* & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$，否则 $U_2 = \begin{pmatrix} \frac{a'^*}{\sqrt{\lvert a' \rvert^2 + \lvert c' \rvert^2}} & 0 & \frac{c'^*}{\sqrt{\lvert a' \rvert^2 + \lvert c' \rvert^2}} \\ 0 & 1 & 0 \\ \frac{c'}{\sqrt{\lvert a' \rvert^2 + \lvert c' \rvert^2}} & 0 & -\frac{a'}{\sqrt{\lvert a' \rvert^2 + \lvert c' \rvert^2}} \end{pmatrix}$. 作用就是为了消去 $c'$，让第一列变为 $(1, 0, 0)$. 设

    \[
        U_2 U_1 U = \begin{pmatrix} 1 & d'' & g'' \\ 0 & e'' & h'' \\ 0 & f'' & j'' \end{pmatrix}.
    \]

    因为 $U, U_1, U_2$ 都是酉矩阵，所以 $U_2 U_1 U$ 也是酉矩阵. 从而有 $d'' = g'' = 0$，所以 $U_2 U_1 U$ 的形式为：

    \[
        U_2 U_1 U = \begin{pmatrix} 1 & 0 & 0 \\ 0 & e'' & h'' \\ 0 & f'' & j'' \end{pmatrix}.
    \]

3. 最后设置 $U_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & e''^* & f''^* \\ 0 & h''^* & j''^* \end{pmatrix}$，这样就有
    
    \[
        U_3 U_2 U_1 U = I.
    \]

接下来进行推广，设 $U$ 作用在 $d$-维 Hilbert 空间上，那么可以构造 two-level 酉矩阵 $U_1, \ldots, U_{d-1}$ 使得 $U_{d-1} U_{d-2} \cdots U_1 U$ 的第一个主对角元为 $1$，并且第一行和第一列的其他元素为 $0$，即：

\[
    U_{d-1} U_{d-2} \cdots U_1 U = \begin{pmatrix} 1 & 0 \\ 0 & U' \end{pmatrix}.
\]

接下来继续对 $U'$ 进行类似的操作，进而得到：

\[
    U = V_1 \ldots V_k,
\]

其中 $k \leq (d-1) + (d-2) + \cdots + 1 = \frac{d(d-1)}{2}$.

### Single qubit and CNOT gates are universal

接下来就是证明单比特门和 CNOT 门可以构建任意的 two-level 酉矩阵. 设 $U$ 是一个作用在 $n$ 个量子比特上的 two-level 酉矩阵，并且非平凡作用的空间由计算基 $\ket{s}, \ket{t}$ 生成，其中 $s = s_1 \ldots s_n$，$t = t_1 \ldots t_n$，$s_i, t_i \in \{0, 1\}$. 设 $\tilde{U}$ 是 $U$ 的非平凡 $2 \times 2$ 子矩阵，其可以认为是一个单比特门. 

设 $g_1, \ldots, g_m$ 是连接 $s$ 和 $t$ 的格雷码路径，其中 $g_1 = s$，$g_m = t$. 因为 $s$ 和 $t$ 至多有 $n$ 处不同，所以 $m \leq n + 1$. 

具体的原理是首先实现 $g_1$ 到 $g_{m - 1}$ 的循环移位，也就是

\begin{align*}
    \ket{g_1} & \mapsto \ket{g_{m - 1}} \\
    \ket{g_2} & \mapsto \ket{g_1} \\
    & \cdots \\
    \ket{g_{m - 1}} & \mapsto \ket{g_{m - 2}} \\
\end{align*}

这种交换都可以使用 CNOT 门实现. 假设 $g_1$ 和 $g_2$ 是在第 $i$ 位不同，那么目标位便是 $i$，条件是其他的比特都相同. 

接下来设 $g_{m - 1}$ 和 $g_m$ 在第 $j$ 位不同，对其应用受控-$\tilde{U}$ 门. 注意这时的 $g_{m - 1}$ 实际上可以认为是 $g_1$，因为之后会利用移位门将其移回去，这就达成了对 $g_1$ 和 $g_m$ 的操作，而不会影响到其他比特. 最后再移位回去就可以了.

实现 $U$ 门至多需要 $2(n - 1)$ 个受控交换门和 $1$ 个受控-$\tilde{U}$ 门，而它们都需要 $O(n)$ 个单比特门和 CNOT 门. 因而总的复杂度为 $O(n^2)$. 而任意一个 $2^n$ 维的酉矩阵都可以分解为 $O(2^{2n}) = O(4^n)$ 个 two-level 酉矩阵，因而总的复杂度为 $O(n^2 \cdot 4^n)$. 这种构造方式并不高效，但是已经接近最优了，因为之后可以证明存在酉操作需要使用指数级别的单比特门和 CNOT 门. 因此，要找到快速的量子算法，显然需要采用与通用性构造不同的思路.

### A discrete set of universal operations

尽管已经证明单比特门和 CNOT 门共同构成了一个通用的量子门集，但是它们的抗噪性并不好. 接下来便会描述一组离散的量子门集，这些门集可以用来构造任意的量子算法，并且可以利用量子纠错来实现抗噪性.

#### Approximating unitary operators

显然一组离散门并不能用于准确实现任意的酉操作，因为酉操作是连续的. 所以便转向了如何去进行近似实现，那么如何衡量近似的好坏呢？设 $U$ 是需要实现的酉操作，$V$ 是实际实现的酉操作，定义误差为：

\[
    E(U, V) = \max_{\ket{\psi}} \lVert (U - V) \ket{\psi} \rVert.
\]

!!! note "Approximating quantum circuits"
    假定量子系统的初态为 $\ket{\psi}$，然后施加一个酉操作 $U$ 或者 $V$，最后进行测量. 设 $M$ 是该测量的一个 POVM 算子，$P_U$ 和 $P_V$ 分别是施加 $U$ 和 $V$ 后得到相应测量结果的概率. 那么有：

    \[
        \lvert P_U - P_V \rvert = \lvert \bra{\psi} U^\dagger M U \ket{\psi} - \bra{\psi} V^\dagger M V \ket{\psi}.
    \]

    定义 $\ket{\Delta} = (U - V) \ket{\psi}$，那么有：

    \begin{align*}
        \lvert P_U - P_V \rvert & = \lvert \bra{\psi} U^\dagger M (U - V) \ket{\psi} + \bra{\psi} (U^\dagger - V^\dagger) M V \ket{\psi} \rvert \\
        & = \lvert \bra{\psi} U^\dagger M \ket{\Delta} + \bra{\Delta} M V \ket{\psi} \rvert \\
        & \leq \lvert \bra{\psi} U^\dagger M \ket{\Delta} \rvert + \lvert \bra{\Delta} M V \ket{\psi} \rvert \\
        & \leq \lVert \bra{\psi} U^\dagger M \rVert \cdot \lVert \ket{\Delta} \rVert + \lVert \bra{\Delta} \cdot \rVert \lVert M V \ket{\psi} \rVert \\
        & \leq \lVert \ket{\Delta} \rVert + \lVert \ket{\Delta} \rVert \\
        & \leq 2 E(U, V).
    \end{align*}

    接下来考虑用一组门序列 $V_1, \ldots, V_m$ 来近似实现另一组门 $U_1, \ldots, U_m$，整个序列的误差满足：

    \[
        E(U_m U_{m-1} \cdots U_1, V_m V_{m-1} \cdots V_1) \leq \sum_{i=1}^m E(U_i, V_i).
    \]

    从 $m = 2$ 开始进行归纳，注意到存在 $\ket{\psi}$ 满足

    \begin{align*}
        E(U_2 U_1, V_2 V_1) & = \lVert (U_2 U_1 - V_2 V_1) \ket{\psi} \rVert \\
        & = \lVert (U_2 U_1 - V_2 U_1 + V_2 U_1 - V_2 V_1) \ket{\psi} \rVert \\
        & \leq \lVert (U_2 U_1 - V_2 U_1) \ket{\psi} \rVert + \lVert (V_2 U_1 - V_2 V_1) \ket{\psi} \rVert \\
        & \leq \lVert (U_2 - V_2) U_1 \ket{\psi} \rVert + \lVert V_2 (U_1 - V_1) \ket{\psi} \rVert \\
        & \leq E(U_2, V_2) + E(U_1, V_1).
    \end{align*}

    归纳部分不再赘述.

#### Universality of Hadamard + phase + CNOT + $\pi/8$ gates

首先 Hadamard 门和 $\pi/8$ 门可以以任意精度实现任意的单比特门. 考虑 $T$ 和 $HTH$ 门的组合，前者沿着 $\hat{z}$ 轴旋转 $\pi/4$，后者沿着 $\hat{x}$ 轴旋转 $\pi/4$，那么它们的复合如下：

\begin{align*}
    \exp(-\i \frac{\pi}{8} Z) \exp(-\i \frac{\pi}{8} X) & = (\cos(\frac{\pi}{8}) I - \i \sin(\frac{\pi}{8}) Z) (\cos(\frac{\pi}{8}) I - \i \sin(\frac{\pi}{8}) X) \\
    & = \cos^2(\frac{\pi}{8}) I - \i (\cos(\frac{\pi}{8}) (X + Z) + \sin(\frac{\pi}{8}) Y) \sin(\frac{\pi}{8}) 
\end{align*}

这是一个沿着轴 $\vec{n} = (\cos(\frac{\pi}{8}), \sin(\frac{\pi}{8}), \cos(\frac{\pi}{8}))$ 旋转 $\theta$ 的门，其中 $\cos(\theta/2) = \cos^2(\frac{\pi}{8})$，注意这里的 $\vec{n}$ 未归一化. 所以只使用 Hadamard 门和 $\pi/8$ 门就构建出了 $R_{\hat{n}}(\theta)$ 门，并且 $\theta$ 可以被证明为 $2\pi$ 的无理数倍.

接下来证明重复迭代 $R_{\hat{n}}(\theta)$ 门可以任意近似 $R_{\hat{n}}(\alpha)$. 设 $\delta > 0$ 为需要的精度，取整数 $N > \frac{2\pi}{\delta}$，定义 $\theta_k \in [0, 2\pi)$ 为 $\theta_k = k \theta \pmod 2\pi$. 根据鸽巢原理，存在互异的 $j, k$ 使得 $\lvert \theta_k - \theta_j \rvert \leq \frac{2\pi}{N} < \delta$. 不失一般性，假设 $j < k$，那么有 $\lvert \theta_{k - j} \rvert < \delta$. 因为 $j \neq k$ 并且 $\theta$ 是 $2\pi$ 的无理数倍，所以 $\theta_{k - j} \neq 0$. 考虑序列 $\theta_{l(k - j)}$，随着 $l$ 变换其将覆盖区间 $[0, 2\pi)$，并且相邻角度的差值小于 $\delta$. 

从而对于任意的 $\varepsilon > 0$，都存在 $n$ 使得 

\[
    E(R_{\hat{n}}(\alpha), R_{\hat{n}}(\theta)^n) < \frac{\varepsilon}{3}
\]

!!! note "Exercise"
    1. For arbitrary $\alpha$ and $\beta$ show that

        \[
            E(R_{\hat{n}}(\alpha), R_{\hat{n}}(\alpha + \beta)) = \lvert 1 - \exp(\i \beta/2) \rvert.
        \]

    2. Suppose $\hat{m}$ and $\hat{n}$ are non-parallel real unit vectors in three dimensions. Use $Z$-$Y$ decomposition to show that an arbitrary single qubit unitary $U$ may be written

        \[
            U = e^{\i\alpha} R_{\hat{n}}(\beta) R_{\hat{m}}(\gamma) R_{\hat{n}}(\delta).
        \]

再就是证明任意单比特门都可以用 Hadamard 门和 $\pi/8$ 门来实现. 对于任意 $\alpha$，可以验证：

\[
    H R_{\hat{n}}(\alpha) H = R_{\hat{m}}(\alpha),
\]

其中 $\hat{m}$ 是方向 $(\cos(\frac{\pi}{8}), -\sin(\frac{\pi}{8}), \cos(\frac{\pi}{8}))$ 的单位向量，并且同样有

\[
    E(R_{\hat{m}}(\alpha), R_{\hat{m}}(\theta)^n) < \frac{\varepsilon}{3}.
\]

而根据前面的练习，对任意的单比特门，其都可以表示为

\[
    U = e^{\i\alpha} R_{\hat{n}}(\beta) R_{\hat{m}}(\gamma) R_{\hat{n}}(\delta).
\]

从而可以得出

\[
    E(U, R_{\hat{n}}(\theta)^{n_1} H R_{\hat{n}}(\theta)^{n_2} H R_{\hat{m}}(\theta)^{n_3}) < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.
\]

依赖于 $\theta_k$ 的近似均匀分布，如果实现单比特门的允许误差为 $\delta$，那么其所需要的门的数量为 $\Omega(\frac{1}{\delta})$，而实现 $m$ 个门的允许误差为 $\varepsilon$，那么所需要的门的数量为 $\Omega(\frac{m^2}{\varepsilon})$. 不过，根据 Solovay–Kitaev 定理，以 $\delta$ 的精度实现单比特门的所需门数量为 $O(\log^c(\frac{1}{\delta}))$，其中 $c$ 是一个近似等于 $2$ 的常数，所以实现允许误差为 $\varepsilon$ 的 $m$ 个单比特门的所需门数量为 $O(m \log^c(\frac{m}{\varepsilon}))$.

#### Approximating arbitrary unitary gates is generically hard

首先考虑这样一个问题：需要多少个门才能生成任意 $n$ 量子比特的态？假定有 $g$ 种不同的门，并且每个门最多作用在 $f$ 位输入上，$f$ 和 $g$ 都是常数. 那么假定电路中包括 $m$ 个门，并且从计算基 $\ket{0}^{\otimes n}$ 开始，电路中的每个门有至多 ${\binom{n}{f}}^g = O(n^{fg})$ 种可能性，因而电路最多产生 $O(n^{fgm})$ 种不同的态. 

如果希望以 $\varepsilon$ 的精度去逼近 $\ket{\psi}$，想法便是有限覆盖，但是需要考虑的便是覆盖所需要的态数目. 首先观察到 $n$ 比特的态空间可以被认为是一个 $2^{n + 1} - 1$ 维的单位球体. 