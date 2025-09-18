# Introduction to quantum mechanics

## Linear algebra

### Inner products

定义外积为如下形式：

\[
    (\ket{w} \bra{v}) (\ket{v'}) = \ket{w} \innerproduct{v}{v'} = \innerproduct{v}{v'} \ket{w}
\]

外积可以用来证明正交基的完备性，设 $\ket{i}$ 是一组正交基，那么对于任意的 $\ket{v}$ 有 $\ket{v} = \sum_i v_i \ket{i}$，且 $\innerproduct{i}{v} = v_i$，那么

\[
    \left(\sum_i \ket{i} \bra{i}\right) \ket{v} = \sum_i \ket{i} \innerproduct{i}{v} = \sum_i v_i \ket{i} = \ket{v}.
\]

因为对任意的 $\ket{v}$ 均成立，所以 $\sum_i \ket{i} \bra{i} = I$，即正交基的完备性. 

应用之一便是给出所有线性算子的外积表示. 设 $A: V \to W$ 是一个线性算子，$\ket{v_i}$ 和 $\ket{w_i}$ 分别是 $V$ 和 $W$ 的一组正交基，那么 $A$ 可以表示为

\begin{align*}
    A & = I_W A I_V \\
      & = \left(\sum_i \ket{w_i} \bra{w_i}\right) A \left(\sum_j \ket{v_j} \bra{v_j}\right) \\
        & = \sum_{i,j} \ket{w_i} \bra{w_i} A \ket{v_j} \bra{v_j} \\
        & = \sum_{i,j} \bra{w_i} A \ket{v_j} \ket{w_i} \bra{v_j}.
\end{align*}

这便是 $A$ 的外积表示，而其中的 $\bra{w_i} A \ket{v_j}$ 便是 $A$ 第 $i$ 行第 $j$ 列的矩阵元.

第二个应用是 Cauchy-Schwarz 不等式. 考虑任意的 $\ket{v}$ 和 $\ket{w}$，利用 $\ket{w}$ 构建一组正交基 $\ket{i}$，其中第一项为 $\ket{w}/\sqrt{\innerproduct{w}{w}}$，那么

\begin{align*}
    \innerproduct{v}{v} \innerproduct{w}{w} & = \sum_i \innerproduct{v}{i} \innerproduct{i}{w} \innerproduct{w}{w} \\
                                            & \geq \dfrac{\innerproduct{v}{w} \innerproduct{w}{v}}{\innerproduct{w}{w}} \innerproduct{w}{w} \\
                                            & = \innerproduct{v}{w} \innerproduct{w}{v} = \norm{\innerproduct{v}{w}}^2.
\end{align*}

### Eigenvectors and eigenvalues

空间 $V$ 上的线性算子 $A$ 的对角化表示为 $A = \sum_i \lambda_i \ket{i} \bra{i}$，其中 $\ket{i}$ 组成了一组 $A$ 的正交的特征向量，对应的特征值为 $\lambda_i$.

当一个特征空间的维数大于 $1$ 时，便称其为退化（degenerate）的. 

### Adjoints and Hermitian operators

设 $A$ 是 Hilbert 空间 $V$ 上的一个线性算子，那么 $A$ 的伴随算子 $A^\dagger$ 定义为满足对于任意 $\ket{v}, \ket{w} \in V$ 有

\[
    (\ket{v}, A\ket{w}) = (A^\dagger \ket{v}, \ket{w})
\]

的算，并且约定 $\ket{v}^\dagger = \bra{v}$.

如果 $A$ 的伴随算子是其自身，那么称 $A$ 是自伴算子（Hermitian operator）. 一类重要的自伴算子是投影算子. 设 $W$ 是 $d$-维空间 $V$ 的一个 $k$-维子空间，利用 Gram-Schmidt 正交化方法可以构造一组正交基 $\ket{1}, \cdots, \ket{d}$，其中 $\ket{1}, \cdots, \ket{k}$ 是 $W$ 的一组基，那么投影到 $W$ 上的投影算子 $P$ 可以表示为

\[
    P = \sum_{i=1}^k \ket{i} \bra{i}.
\]

由定义可知 $\ket{v} \bra{v}$ 是自伴算子，因此 $P$ 也是自伴算子. $P$ 的正交补是算子 $Q = I - P$，其投影到 $W$ 的正交补上，即由 $\ket{k+1}, \cdots, \ket{d}$ 构成的空间.

算子 $A$ 被称为是正规的（normal）如果 $A A^\dagger = A^\dagger A$. 正规算子的一个重要的表示定理是谱分解定理，其表明正规算子的充要条件是其可以被对角化.

一个矩阵 $U$ 被称为是酉矩阵（unitary matrix）如果 $U U^\dagger = U^\dagger U = I$. 几何意义上，酉矩阵保持内积不变，即

\[
    (U\ket{v}, U\ket{w}) = \bra{v} U^\dagger U \ket{w} = \bra{v} I \ket{w} = \innerproduct{v}{w}.
\]

设 $\ket{v_i}$ 为任意一组正交基，令 $\ket{w_i} = U \ket{v_i}$，因为 $U$ 保持内积不变，所以 $\ket{w_i}$ 也是正交的. 进而 $U$ 可以被表示为

\[
    U = \sum_i \ket{w_i} \bra{v_i}.
\]

而对于两组正交基 $\ket{v_i}$ 和 $\ket{w_i}$，也可以相应地构造酉矩阵 $U = \sum_i \ket{w_i} \bra{v_i}$.

!!! example
    (Basis changes) Suppose $A'$ and $A''$ are matrix representations of an operator $A$ on a vector space $V$ with respect to two different orthonormal bases, $\ket{v_i}$ and $\ket{w_i}$. Then the elements of $A'$ and $A''$ are $A'_{ij} = \bra{v_i} A \ket{v_j}$ and $A''_{ij} = \bra{w_i} A \ket{w_j}$. Characterize the relationship between $A'$ and $A''$.

    ??? solution
        \[
            A'' = U^\dagger A' U,
        \]

        因而有 $\ket{w_i} = \sum_k U_{ki} \ket{v_k}$，$U_{ij} = \innerproduct{v_i}{w_j}$.

    
自伴算子中一类重要的算子是正算子，对于任意的 $\ket{v}$ 有 $(\ket{v}, A\ket{v}) \geq 0$. 而如果 $\forall \ket{v} \neq 0$，$(\ket{v}, A\ket{v}) > 0$，则称 $A$ 是正定的.

### Tensor products

张量积满足以下性质：

1. 对任意标量 $z$ 以及元素 $\ket{v} \in V$ 和 $\ket{w} \in W$，有

    \[
        z (\ket{v} \otimes \ket{w}) = (z \ket{v}) \otimes \ket{w} = \ket{v} \otimes (z \ket{w}).
    \]

2. 对任意 $\ket{v_1}, \ket{v_2} \in V$ 和 $\ket{w} \in W$，有

    \[
        (\ket{v_1} + \ket{v_2}) \otimes \ket{w} = \ket{v_1} \otimes \ket{w} + \ket{v_2} \otimes \ket{w}.
    \]

3. 对任意 $\ket{v} \in V$ 和 $\ket{w_1}, \ket{w_2} \in W$，有

    \[
        \ket{v} \otimes (\ket{w_1} + \ket{w_2}) = \ket{v} \otimes \ket{w_1} + \ket{v} \otimes \ket{w_2}.
    \]

设 $\ket{v} \in V$ 和 $\ket{w} \in W$，$A$ 和 $B$ 分别是 $V$ 和 $W$ 上的线性算子，那么 $A \otimes B$ 是 $V \otimes W$ 上的线性算子，其作用为

\[
    (A \otimes B) (\ket{v} \otimes \ket{w}) = A\ket{v} \otimes B\ket{w}.
\]

那么该作用便可以自然地推广到张量积空间上的任意向量：

\[
    (A \otimes B) \left(\sum_i a_i \ket{v_i} \otimes \ket{w_i}\right) = \sum_i a_i A\ket{v_i} \otimes B\ket{w_i}.
\]

而考虑 $A: V \to V'$ 和 $B: W \to W'$，那么 $C: V \otimes W \to V' \otimes W'$ 可以表示为

\[
    C = \sum_i c_i A_i \otimes B_i.
\]

作用为

\[
    \left(\sum_i c_i A_i \otimes B_i\right) \ket{v} \otimes \ket{w} = \sum_i c_i A_i \ket{v} \otimes B_i \ket{w}.
\]

$V$ 和 $W$ 上的内积可以自然地推广到张量积空间上的内积：

\[
    (\sum_i a_i \ket{v_i} \otimes \ket{w_i}, \sum_j b_j \ket{v_j'} \otimes \ket{w_j'}) = \sum_{i,j} a_i^* b_j \innerproduct{v_i}{v_j'} \innerproduct{w_i}{w_j'}.
\]

$A \otimes B$ 的矩阵表示实际上是 $A$ 和 $B$ 的 Kronecker 积. 设 $(A)_{mn}$ 和 $(B)_{pq}$ 的矩阵表示分别为 $A_{ij}$ 和 $B_{kl}$，那么 $A \otimes B$ 的矩阵表示为

\[
    A \otimes B = \begin{pmatrix}
        A_{11} B & A_{12} B & \cdots & A_{1n} B \\
        A_{21} B & A_{22} B & \cdots & A_{2n} B \\
        \vdots & \vdots & \ddots & \vdots \\
        A_{m1} B & A_{m2} B & \cdots & A_{mn} B
    \end{pmatrix}.
\]

其中 $A_{ij} B$ 都是一个 $p \times q$ 的矩阵.

### Operator functions

设 $A = \sum_a a \ket{a} \bra{a}$ 是一个正规算子的谱分解，那么 $f(A)$ 定义为

\[
    f(A) = \sum_a f(a) \ket{a} \bra{a}.
\]

另一个重要的矩阵函数便是矩阵的迹，定义为矩阵对角元素之和. 

\[
    \op{Tr} (A) = \sum_i A_{ii}.
\]

易见迹是循环且线性的，即 $\op{Tr} (AB) = \op{Tr} (BA)$ 以及 $\op{Tr} (A + B) = \op{Tr} (A) + \op{Tr} (B)$，$z \op{Tr} (A) = \op{Tr} (zA)$，其中 $A$ 和 $B$ 是任意的矩阵，$z \in \mathbb{C}$. 通过循环性，也能得到矩阵的迹在酉相似变换下不变，所以迹是一个矩阵的不变量.

假定 $\ket{\psi}$ 是一个单位向量，$A$ 是任意一个算子，为了计算 $\op{Tr} (A \ket{\psi} \bra{\psi})$，利用 Gram-Schmidt 正交化方法可以构造一组正交基 $\ket{i}$，其中第一项为 $\ket{\psi}$，那么

\begin{align*}
    \op{Tr} (A \ket{\psi} \bra{\psi}) & = \sum_i \bra{i} A \ket{\psi} \innerproduct{\psi}{i} \\
                                      & = \bra{\psi} A \ket{\psi}.
\end{align*}

这一结果在用来计算算子的迹时非常有用.

### The commutator and anti-commutator

两算子 $A$ 和 $B$ 的对易子定义为 $[A, B] = AB - BA$，而反对易子定义为 $\{A, B\} = AB + BA$. 如果 $[A, B] = 0$，那么称 $A$ 和 $B$ 对易. 相应的，如果 $\{A, B\} = 0$，那么称 $A$ 和 $B$ 反对易.

!!! note "Theorem"
    (Simultaneous diagonalization theorem) 设 $A$ 和 $B$ 都是自伴算子，那么 $A$ 和 $B$ 可以被同时对角化当且仅当 $[A, B] = 0$.

!!! example
    (Exponential of the Pauli matrices)Let $\vec{v}$ be any real, three-dimensional unit vector and $\theta$ a real number. Prove that 
    
    \[
        \op{exp} (\i \theta \vec{v} \cdot \vec{\sigma}) = \cos (\theta) I + \i \sin (\theta) \vec{v} \cdot \vec{\sigma}, 
    \]

    where $\vec{v} \cdot \vec{\sigma} = \sum_{i = 1}^3 v_i \sigma_i$.

Pauli 矩阵的对易子和反对易子如下：

\begin{gather*}
    [\sigma_a, \sigma_b] = 2 \i \epsilon_{abc} \sigma_c, \\
    \{\sigma_a, \sigma_b\} = 2 \delta_{ab} I.
\end{gather*}

而根据对易子和反对易子的定义，有：

\begin{align*}
    [\sigma_a, \sigma_b] + \{\sigma_a, \sigma_b\} & = (\sigma_a\sigma_b - \sigma_b\sigma_a) + (\sigma_a\sigma_b + \sigma_b\sigma_a) \\
    2 \i \epsilon_{abc} \sigma_c + 2 \delta_{ab} I & = 2\sigma_a\sigma_b \\
    \sigma_a\sigma_b & = \delta_{ab} I + \i \epsilon_{abc} \sigma_c.
\end{align*}

在此基础上考虑向量乘法 $(\vec{v} \cdot \vec{\sigma})(\vec{u} \cdot \vec{\sigma})$，其中 $\vec{v}$ 和 $\vec{u}$ 是任意的三维实向量，那么展开后即为

\begin{align*}
    (\vec{v} \cdot \vec{\sigma})(\vec{u} \cdot \vec{\sigma}) & = (v_a \sigma_a + v_b \sigma_b + v_c \sigma_c)(u_a \sigma_a + u_b \sigma_b + u_c \sigma_c) \\
    & = v_a u_a \sigma_a^2 + v_b u_b \sigma_b^2 + v_c u_c \sigma_c^2 \\ 
    & + v_a u_b \sigma_a \sigma_b + v_a u_c \sigma_a \sigma_c + v_b u_a \sigma_b \sigma_a + v_b u_c \sigma_b \sigma_c + v_c u_a \sigma_c \sigma_a + v_c u_b \sigma_c \sigma_b \\
    & = (v_a u_a + v_b u_b + v_c u_c) I \\
    & + \i (v_a u_b - v_b u_a) \sigma_c + \i (v_a u_c - v_c u_a) \sigma_b + \i (v_b u_c - v_c u_b) \sigma_a \\
    & = (\vec{v} \cdot \vec{u}) I + \i (\vec{v} \times \vec{u}) \cdot \vec{\sigma}.
\end{align*}

如果令 $\vec{u} = \vec{v}$，那么便有

\[
    (\vec{v} \cdot \vec{\sigma})^2 = I.
\]

进而可以得到

\begin{gather*}
    (\vec{v} \cdot \vec{\sigma})^{2n} = I, \\
    (\vec{v} \cdot \vec{\sigma})^{2n+1} = \vec{v} \cdot \vec{\sigma}.
\end{gather*}

将指数式进行 Taylor 展开，便有

\begin{align*}
    \op{exp} (\i \theta \vec{v} \cdot \vec{\sigma}) & = \sum_{n=0}^\infty \dfrac{(\i \theta )^n}{n!} (\vec{v} \cdot \vec{\sigma})^n \\
    & = \sum_{n=0}^\infty \dfrac{(\i \theta )^{2n}}{(2n)!} (\vec{v} \cdot \vec{\sigma})^{2n} + \sum_{n=0}^\infty \dfrac{(\i \theta )^{2n+1}}{(2n+1)!} (\vec{v} \cdot \vec{\sigma})^{2n+1} \\
    & = \sum_{n=0}^\infty \dfrac{(-1)^n \theta^{2n}}{(2n)!} I + \sum_{n=0}^\infty \dfrac{\i (-1)^n \theta^{2n+1}}{(2n+1)!} \vec{v} \cdot \vec{\sigma} \\
    & = \cos (\theta) I + \i \sin (\theta) \vec{v} \cdot \vec{\sigma}.
\end{align*}

### The polar and singular value decompositions

!!! note "Theorem"
    (Polar decomposition) 设 $A$ 是线性空间 $V$ 上的一个算子，那么存在一个酉算子 $U$ 和正算子 $J$ 以及 $K$，使得
    
    \[
        A = U J = K U.
    \]

    其中 $J$ 和 $K$ 满足 $J = \sqrt{A^\dagger A}$ 和 $K = \sqrt{A A^\dagger}$. 如果 $A$ 是可逆的，那么 $U$ 是唯一的.

!!! success "Corollary"
    (Singular value decomposition) 设 $A$ 是一个方阵，那么存在酉矩阵 $U$ 以及 $V$，还有元素为非负实数的对角矩阵 $D$，使得

    \[
        A = U D V.
    \]

    其中 $D$ 的对角元素为 $A$ 的奇异值.

## The postulates of quantum mechanics

### State space

!!! success "Postulate 1"
    任何孤立的物理系统都与一个带有内积的复线性空间相关联，称为该系统的状态空间. 系统完全由状态向量描述，其是状态空间中的一个单位向量.

最简单的量子力学系统，也是我们最为关心的系统，便是量子比特. 量子比特的状态空间是一个二维复线性空间，设 $\ket{0}$ 和 $\ket{1}$ 是一组正交基，那么空间中任意的状态向量可以表示为

\[
    \ket{\psi} = a \ket{0} + b \ket{1},
\]

其中 $a$ 和 $b$ 是复数，满足 $\lvert a \rvert^2 + \lvert b \rvert^2 = 1$. $\innerproduct{\psi}{\psi} = 1$ 也被称为归一化条件.

称线性组合 $\sum_i a_i \ket{\psi_i}$ 为 $\ket{\psi_i}$ 的叠加态，其中对应概率幅为 $a_i$.

### Evolution

!!! success "Postulate 2"
    一个封闭量子系统的演化由一个酉变换描述，即 $t_1$ 时刻的状态向量 $\ket{\psi}$ 和 $t_2$ 时刻的状态向量 $\ket{\psi'}$ 通过仅依赖于 $t_1$ 和 $t_2$ 的酉算子 $U$ 相关联，即

    \[
        \ket{\psi'} = U \ket{\psi}.
    \]

下面给出一个更加精细的公设，可以用来描述连续时间的演化. 

!!! success "Postulate 2'"
    一个封闭量子系统的演化由 Schrödinger 方程描述，即

    \[
        \i \hbar \dfrac{\mathrm{d} \ket{\psi}}{\mathrm{d} t} = H \ket{\psi},
    \]

    其中 $\hbar$ 是约化 Planck 常数，$H$ 是系统的哈密顿算子.

因为 $H$ 是一个自伴算子，所以其有一个谱分解

\[
    H = \sum_E E \ket{E} \bra{E},
\]

特征值为 $E$，对应的特征向量为 $\ket{E}$. $\ket{E}$ 被称为能量本征态，也被称为定态. $E$ 便是 $\ket{E}$ 对应的能量. 最小的能量被称为基态能量，对应的态被称为基态. $\ket{E}$ 被称为定态的原因是其随着时间变化只会获得一个因子，即

\[
    \ket{E} \to \op{exp} (-\i E t / \hbar) \ket{E}.
\]

那么连续时间的演化算子和离散时间的演化算子之间有何联系呢？只需写出 Schrödinger 方程的解即可：

\[
    \ket{\psi(t_2)} = \op{exp} (-\i H (t_2 - t_1) / \hbar) \ket{\psi(t_1)} = U(t_2, t_1) \ket{\psi(t_1)}.
\]

便可定义 $U(t_1, t_2) = \op{exp} (-\i H (t_2 - t_1) / \hbar)$.

### Quantum measurement

!!! success "Postulate 3"
    量子测量由一组测量算子 $\{M_m\}$ 描述，其作用在被测量系统的状态空间上. 下标 $m$ 对应测量可能的结果. 若测量前系统处于状态 $\ket{\psi}$，那么结果 $m$ 出现的概率为

    \[
        p(m) = \bra{\psi} M_m^\dagger M_m \ket{\psi}.
    \]

    测量后，系统的状态变为

    \[
        \dfrac{M_m \ket{\psi}}{\sqrt{p(m)}}.
    \]

    测量算子满足完备性条件，即

    \[
        \sum_m M_m^\dagger M_m = I.
    \]

### Distinguishing quantum states

以下证明非正交量子态不能被可靠地区分.

假定存在某个测量能够可靠地区分非正交态 $\ket{\psi_1}$ 和 $\ket{\psi_2}$，如果量子态 $\ket{\psi_1}$（$\ket{\psi_2}$）被制备出来，那么测量结果 $f(j) = 1$（$f(j) = 2$）的概率必然为 $1$. 定义 $E_i = \sum_{j: f(j) = i} M_j^\dagger M_j$，则有

\[
    \bra{\psi_1} E_1 \ket{\psi_1} = 1, \quad \bra{\psi_2} E_2 \ket{\psi_2} = 1.
\]

而因为 $\sum_i E_i = I$，且 $\bra{\psi_1} E_1 \ket{\psi_1} = 1$，故 $\bra{\psi_1} E_2 \ket{\psi_1} = 0$，进而有 $\sqrt{E_2} \ket{\psi_1} = 0$. 又因为 $\ket{\psi_1}$ 和 $\ket{\psi_2}$ 是非正交的，所以 $\ket{\psi_2}$ 可以被分解为 $\ket{\psi_2} = \alpha \ket{\psi_1} + \beta \ket{\psi_1^\perp}$，其中 $\ket{\psi_1^\perp}$ 是与 $\ket{\psi_1}$ 正交的态，$\lvert \alpha \rvert^2 + \lvert \beta \rvert^2 = 1$，且 $\lvert \beta \rvert < 1$. 进而有 $\sqrt{E_2} \ket{\psi_2} = \beta \sqrt{E_2} \ket{\psi_1^\perp}$，代入得到

\[
    \bra{\psi_2} E_2 \ket{\psi_2} = \lvert \beta \rvert^2 \bra{\psi_1^\perp} E_2 \ket{\psi_1^\perp} \leq \lvert \beta \rvert^2 < 1.
\]

这与测量结果为 $2$ 的概率为 $1$ 矛盾，因此非正交态不能被可靠地区分.

### Projective measurements

投影测量由一个可观测量 $M$ 描述，其是一个作用在被观测系统的状态空间上的自伴算子. 该被观测量有如下的谱分解：

\[
    M = \sum_m m P_m,
\]

其中 $P_m$ 是投影到 $M$ 对应特征值 $m$ 的特征空间的投影算子. 测量的可能结果对应于 $M$ 的特征值，测量状态 $\ket{\psi}$ 得到结果 $m$ 的概率为

\[
    p(m) = \bra{\psi} P_m \ket{\psi}.
\]

如果测量结果为 $m$，那么测量后系统的状态为

\[
    \dfrac{P_m \ket{\psi}}{\sqrt{p(m)}}.
\]

测量结果的期望值如下：

\begin{align*}
    \mathbf{E} (M) & = \sum_m m p(m) \\
                   & = \sum_m m \bra{\psi} P_m \ket{\psi} \\
                   & = \bra{\psi} \sum_m m P_m \ket{\psi} \\
                   & = \bra{\psi} M \ket{\psi}.
\end{align*}

其也经常用符号 $\langle M \rangle$ 表示.

而方差也就可以表示为

\begin{align*}
    [\Delta (M)]^2 & = \langle M - \langle M \rangle \rangle^2 \\
                   & = \langle M^2 \rangle - \langle M \rangle^2.
\end{align*}

!!! note "The Heisenberg uncertainty principle"
    设 $A$ 和 $B$ 都是自伴算子，$\ket{\psi}$ 是任意的态. 假定 $\bra{\psi} AB \ket{\psi} = x + \i y$，那么

    \begin{align*}
        \bra{\psi} BA \ket{\psi} & = (B^\dagger \ket{\psi})^\dagger A \ket{\psi} \\
                                 & = ((A \ket{\psi})^\dagger (B^\dagger \ket{\psi}))^\dagger \\
                                 & = ((\bra{\psi} A^\dagger) (B^\dagger \ket{\psi}))^\dagger \\
                                 & = (\bra{\psi} AB \ket{\psi})^\dagger \\
                                 & = x - \i y.
    \end{align*}

    所以 $\bra{\psi} [A, B] \ket{\psi} = 2 \i y$，$\bra{\psi} \{A, B\} \ket{\psi} = 2 x$. 这也就有

    \[
        \lvert \bra{\psi} [A, B] \ket{\psi} \rvert^2 + \lvert \bra{\psi} \{A, B\} \ket{\psi} \rvert^2 = 4 \lvert \bra{\psi} AB \ket{\psi} \rvert^2.
    \]

    而根据 Cauchy-Schwarz 不等式，有

    \[
        \lvert \bra{\psi} AB \ket{\psi} \rvert^2 \leq \bra{\psi} A^2 \ket{\psi} \bra{\psi} B^2 \ket{\psi},
    \]

    从而可以得到

    \[
        \lvert \bra{\psi} [A, B] \ket{\psi} \rvert^2 \leq 4 \bra{\psi} A^2 \ket{\psi} \bra{\psi} B^2 \ket{\psi}.
    \]

    设 $C$ 和 $D$ 是两个可观测量，将 $A = C - \langle C \rangle$ 和 $B = D - \langle D \rangle$ 代入.

    \begin{align*}
        4 \langle A^2 \rangle \langle B^2 \rangle & = 4 \langle (C - \langle C \rangle)^2 \rangle \langle (D - \langle D \rangle)^2 \rangle \\
                                                  & = 4 [\Delta (C)]^2 [\Delta (D)]^2.
    \end{align*}

    以及

    \begin{align*}
        [A, B] & = AB - BA \\
               & = (C - \langle C \rangle)(D - \langle D \rangle) - (D - \langle D \rangle)(C - \langle C \rangle) \\
               & = CD - \langle C \rangle D - C \langle D \rangle + \langle C \rangle \langle D \rangle - DC + \langle D \rangle C + D \langle C \rangle - \langle D \rangle \langle C \rangle \\
               & = CD - DC \\
               & = [C, D].
    \end{align*}

    故有

    \[
        \Delta (C) \Delta (D) \geq \dfrac{\lvert \bra{\psi} [C, D] \ket{\psi} \rvert}{2}.
    \]

    这便是 Heisenberg 不确定性原理.

    关于不确定性原理，需警惕一种常见误解：认为测量可观测量 $C$ 的精度 $\Delta (C)$ 会导致 $D$ 的值被扰动了 $\Delta (D)$，从而满足如上的不等式. 尽管量子测量确实会扰动系统，但这绝非不确定性原理的内涵。正确解释是：若制备大量相同量子态 $\ket{\psi}$，对部分系统测量 $C$，对另一部分测量 $D$，那么 $C$ 结果的标准差 $\Delta (C)$ 与 $D$ 结果的标准差 $\Delta (D)$ 之间存在如上的关系.

假定 $\vec{v}$ 是一个实三维单位向量，那么可以定义可观测量

\[
    \vec{v} \cdot \vec{\sigma} = v_1 \sigma_1 + v_2 \sigma_2 + v_3 \sigma_3,
\]

对这一可观测量的测量有时也被称为沿着 $\vec{v}$ 方向测量自旋. 

### POVM measurements

假定对一个处于 $\ket{\psi}$ 的系统进行一次由算子 $M_m$ 描述的测量. 那么结果 $m$ 出现的概率为 $p(m) = \bra{\psi} M_m^\dagger M_m \ket{\psi}$. 定义

\[
    E_m = M_m^\dagger M_m,
\]

可知 $E_m$ 是一个正算子，且满足完备性条件 $\sum_m E_m = I$. $E_m$ 便被称为 POVM 元素，整个 POVM 便被描述为 $\{E_m\}$. 

### Phase

考虑量子态 $e^{\i \theta} \ket{\psi}$ 和 $\ket{\psi}$，其中 $\theta$ 是实数. 这两个态被称作在忽略全局相位的情况下等价的. 有趣的是，这两个态的测量统计结果是相同的. 假定 $M_m$ 是与某个量子测量关联的测量算子，那么二者的测量结果为 $m$ 的概率分别为

\begin{gather*}
    p(m) = \bra{\psi} M_m^\dagger M_m \ket{\psi}, \\
    p'(m) = \bra{\psi} e^{-\i \theta} M_m^\dagger M_m e^{\i \theta} \ket{\psi} = \bra{\psi} M_m^\dagger M_m \ket{\psi}.
\end{gather*}

因此，从观测角度看，这两个态是等价的. 基于此，全局相位因子可被视为与物理系统的可观测性质无关.

另一种相位被称为相对相位. 考虑如下两个态：

\[
    \ket{\psi} = \dfrac{1}{\sqrt{2}} (\ket{0} + \ket{1}), \quad \ket{\psi'} = \dfrac{1}{\sqrt{2}} (\ket{0} - \ket{1}).
\]

$\ket{\psi}$ 关于 $\ket{1}$ 的振幅是 $\dfrac{1}{\sqrt{2}}$，而 $\ket{\psi'}$ 关于 $\ket{1}$ 的振幅是 $-\dfrac{1}{\sqrt{2}}$. 二者大小一致，但是符号不同. 更广义地，如果振幅 $a$ 和 $b$ 满足 $a = \op{exp} (\i \theta) b$，那么称 $a$ 和 $b$ 相差一个相对相位. 再一般些，如果两个量子态在某一组正交基下的振幅分量均通过一个相位因子关联，那么称这两个态在该组基下具有相对相位差.

### Composite systems

!!! success "Postulate 4"
    复合物理系统的状态空间是各个组成部分的状态空间的张量积. 如果组成部分的编号从 $1$ 到 $n$，并且第 $i$ 个系统位于状态 $\ket{\psi_i}$，那么整个系统的状态为 $\ket{\psi_1} \otimes \ket{\psi_2} \otimes \cdots \otimes \ket{\psi_n}$.

以下证明投影变化结合酉矩阵可以实现任何一般的量子测量.

假定存在一个量子系统，其状态空间为 $Q$，并且希望在其上进行由 $\{M_m\}$ 描述的一般测量. 为了实现这一测量，需要引入一个辅助系统（ancilla system），其状态空间为 $M$，并且有一组正交基 $\{\ket{m}\}$，其中 $m$ 对应测量结果. 

设 $\ket{0}$ 是 $M$ 的任意一个定态，定义算子 $U$ 对 $\ket{\psi} \ket{0}$ 的作用为

\[
    U (\ket{\psi} \ket{0}) = \sum_m M_m \ket{\psi} \ket{m}.
\]

利用 $\ket{m}$ 的正交性和 $M_m$ 的完备性，可以得到 $U$ 对形如 $\ket{\psi} \ket{0}$ 的态保持内积. 

\begin{align*}
    \bra{\varphi} \bra{0} U^\dagger U \ket{\psi} \ket{0} & = \sum_{m, m'} \bra{\varphi} M_m^\dagger M_{m'} \ket{\psi} \innerproduct{m}{m'} \\
                                                          & = \sum_m \bra{\varphi} M_m^\dagger M_m \ket{\psi} \\
                                                          & = \innerproduct{\varphi}{\psi}.
\end{align*}

再根据如下的例子便可以将 $U$ 扩展为 $Q \otimes M$ 上的酉算子，也记为 $U$.

!!! example
    设 $V$ 是一个 Hilbert 空间，有子空间 $W$. 设 $U: W \to V$ 是一个保持内积的线性算子，也就是说，对于任意的 $\ket{w_1}, \ket{w_2} \in W$，有

    \[
        \bra{w_1} U^\dagger U \ket{w_2} = \innerproduct{w_1}{w_2}.
    \]

    证明存在一个酉算子 $U': V \to V$ 扩展了 $U$，即 $U' \ket{w} = U \ket{w}$ 对任意的 $\ket{w} \in W$ 都成立，但 $U'$ 定义在整个 $V$ 上.

接下来假定在整个系统上进行一个由投影算子 $P_m = I_Q \otimes \ket{m} \bra{m}$ 描述的投影测量. 那么测量结果 $m$ 出现的概率为

\begin{align*}
    p(m) & = \bra{\psi} \bra{0} U^\dagger P_m U \ket{\psi} \ket{0} \\
         & = \sum_{m', m''} \bra{\psi} M_{m'}^\dagger \ket{m'} (I_Q \otimes \ket{m} \bra{m}) M_{m''} \ket{\psi} \ket{m''} \\
         & = \bra{\psi} M_m^\dagger M_m \ket{\psi}.
\end{align*}

与一般测量的概率公式一致. 测量结果为 $m$ 后，系统 $QM$ 的状态为

\[
    \dfrac{P_m U \ket{\psi} \ket{0}}{\sqrt{\bra{\psi} U^\dagger P_m U \ket{\psi}}} = \dfrac{M_m \ket{\psi} \ket{m}}{\sqrt{\bra{\psi} M_m^\dagger M_m \ket{\psi}}}.
\]

也就是说 $M$ 的状态为 $\ket{m}$，而 $Q$ 的状态为

\[
    \dfrac{M_m \ket{\psi}}{\sqrt{\bra{\psi} M_m^\dagger M_m \ket{\psi}}}.
\]

如果一个复合系统的某个态不能够写作其组成系统的态的张量积，那么称该态为纠缠态. 

## Application: superdense coding

假定 Alice 有 2 经典比特的信息，想要传递给 Bob，但只允许传输 1 个量子比特，该如何实现？

首先假设 Alice 和 Bob 初始共享一个纠缠态

\[
    \ket{\psi} = \dfrac{1}{\sqrt{2}} (\ket{00} + \ket{11}).
\]

Alice 持有第一个量子比特，Bob 持有第二个量子比特. 如果 Alice 希望传递的信息和施加操作的关系如下：

\begin{align*}
    00 & \to I, \\
    01 & \to X, \\
    10 & \to Z, \\
    11 & \to \i Y.
\end{align*}

施加后的态为

\begin{align*}
    00: \ket{\psi} & \to \dfrac{1}{\sqrt{2}} (\ket{00} + \ket{11}), \\
    01: \ket{\psi} & \to \dfrac{1}{\sqrt{2}} (\ket{00} - \ket{11}), \\
    10: \ket{\psi} & \to \dfrac{1}{\sqrt{2}} (\ket{10} + \ket{01}), \\
    11: \ket{\psi} & \to \dfrac{1}{\sqrt{2}} (\ket{01} - \ket{10}).
\end{align*}

而这四个态是 Bell 态，它们是正交的. Alice 只需将自己的量子比特传递给 Bob，Bob 便能够通过测量得到 Alice 想要传递的信息.

## The density operator

### Ensembles of quantum states

密度算子为描述状态并非完全确定的量子系统提供了一种方法. 更准确地说，假定量子系统处于 $\ket{\psi_i}$ 的概率为 $p_i$，那么称 $\{p_i, \ket{\psi_i}\}$ 为一个量子系综. 而该系统的密度算子定义为

\[
    \rho = \sum_i p_i \ket{\psi_i} \bra{\psi_i}.
\]

密度算子也常称为密度矩阵. 之前提到的量子力学的公设都可以用密度算子的语言重新表述.

假定某个封闭量子系统的演化由一个酉算子 $U$ 描述，那么系综的密度算子在演化后的形式为

\[
    \rho = \sum_i p_i \ket{\psi_i} \bra{\psi_i} \xrightarrow{U} \sum_i p_i U \ket{\psi_i} \bra{\psi_i} U^\dagger = U \rho U^\dagger.
\]

测量也很容易用密度算子的语言描述. 假定在系统上施加由 $\{M_m\}$ 描述的一般测量，初始状态为 $\ket{\psi}$，那么测量结果 $m$ 出现的概率为

\[
    p(m \mid i) = \bra{\psi_i} M_m^\dagger M_m \ket{\psi_i} = \op{Tr} (M_m^\dagger M_m \ket{\psi_i} \bra{\psi_i}).
\]

第二个等号来源于 $\op{Tr} (A \ket{\psi} \bra{\psi}) = \bra{\psi} A \ket{\psi}$. 那么整个系综的测量结果为 $m$ 的概率为

\begin{align*}
    p(m) & = \sum_i p_i p(m \mid i) \\
         & = \sum_i p_i \op{Tr} (M_m^\dagger M_m \ket{\psi_i} \bra{\psi_i}) \\
         & = \op{Tr} (M_m^\dagger M_m \sum_i p_i \ket{\psi_i} \bra{\psi_i}) \\
         & = \op{Tr} (M_m^\dagger M_m \rho).
\end{align*}

那么测量结果为 $m$ 后，系统的状态是什么呢？如果初始状态为 $\ket{\psi_i}$，那么测量后系统的状态为

\[
    \ket{\psi_i^m} = \dfrac{M_m \ket{\psi_i}}{\bra{\psi_i} M_m^\dagger M_m \ket{\psi_i}}.
\]

对应的系综是 $\{p(i \mid m), \ket{\psi_i^m}\}$，其密度算子为

\[
    \rho_m = \sum_i p(i \mid m) \ket{\psi_i^m} \bra{\psi_i^m} = \sum_i p(i \mid m) \dfrac{M_m \ket{\psi_i} \bra{\psi_i} M_m^\dagger}{\bra{\psi_i} M_m^\dagger M_m \ket{\psi_i}}.
\]

根据基本的概率论知识，$p(i \mid m) = p(m \mid i) p_i / p(m)$，代入得到

\begin{align*}
    \rho_m & = \sum_i \dfrac{p(m \mid i) p_i}{p(m)} \dfrac{M_m \ket{\psi_i} \bra{\psi_i} M_m^\dagger}{\bra{\psi_i} M_m^\dagger M_m \ket{\psi_i}} \\
              & = \sum_i p_i \dfrac{M_m \ket{\psi_i} \bra{\psi_i} M_m^\dagger}{\op{Tr} (M_m^\dagger M_m \rho)} \\
              & = \dfrac{M_m \rho M_m^\dagger}{\op{Tr} (M_m^\dagger M_m \rho)}.
\end{align*}

至此，演化公设和测量公设都可以用密度算子的语言重新表述.

接下来再介绍一些量子力学的基本概念. 如果一个量子系统的态 $\ket{\psi}$ 是确切知道的，那么称为纯态，这种情况下其密度算子为 $\rho = \ket{\psi} \bra{\psi}$. 否则 $\rho$ 为混合态. 纯态和混合态的密度算子的区别在于，纯态的密度算子满足 $\op{Tr} (\rho^2) = 1$，而混合态的密度算子满足 $\op{Tr} (\rho^2) < 1$.

如果一个量子系统处于状态 $\rho_i$ 的概率为 $p_i$，那么不难得到其密度算子为 $\sum_i p_i \rho_i$. 可以通过展开 $\rho_i = \sum_{j} p_{ij} \ket{\psi_{ij}} \bra{\psi_{ij}}$，代入得到

\[
    \rho = \sum_{i, j} p_i p_{ij} \ket{\psi_{ij}} \bra{\psi_{ij}} = \sum_i p_i \rho_i.
\]

$\rho$ 被称为 $\rho_i$ 的混合. 

假设因某些原因，$m$ 的测量结果丢失了，此时系统会以 $p(m)$ 的概率处于 $\rho_m$ 的状态. 此时系统的状态可以用如下的密度算子描述：

\begin{align*}
    \rho & = \sum_m p(m) \rho_m \\
         & = \sum_m \op{Tr} (M_m^\dagger M_m \rho) \dfrac{M_m \rho M_m^\dagger}{\op{Tr} (M_m^\dagger M_m \rho)} \\
        & = \sum_m M_m \rho M_m^\dagger.
\end{align*}

### General properties of the density operator

密度算子的特征由如下定理给出.

!!! note "Theorem"
    (Characterization of density operators) 算子 $\rho$ 为一个与某些系综 $\{p_i, \ket{\psi_i}\}$ 对应的密度算子的充要条件是

    1. (Trace condition) $\op{Tr} (\rho) = 1$,
    2. (Positivity condition) $\rho$ 是正算子.

    ??? note "Proof"
        $(\Rightarrow)$ 假定 $\rho = \sum_i p_i \ket{\psi_i} \bra{\psi_i}$ 是一个密度算子. 那么

        \[
            \op{Tr} (\rho) = \sum_i p_i \op{Tr} (\ket{\psi_i} \bra{\psi_i}) = \sum_i p_i = 1.
        \]

        假定 $\ket{\varphi}$ 是空间中的任意态，那么

        \begin{align*}
            \bra{\varphi} \rho \ket{\varphi} & = \sum_i p_i \innerproduct{\varphi}{\psi_i} \innerproduct{\psi_i}{\varphi} \\
                                             & = \sum_i p_i \lvert \innerproduct{\varphi}{\psi_i} \rvert^2 \\
                                             & \geq 0.
        \end{align*}

        $(\Leftarrow)$ 假定 $\rho$ 满足上述两个条件. 因为 $\rho$ 是正算子，所以可以对其进行谱分解

        \[
            \rho = \sum_j \lambda_j \ket{j} \bra{j},
        \]

        其中 $\lambda_j$ 是正实数，$\ket{j}$ 是正交归一的. 从迹条件可知 $\sum_j \lambda_j = 1$. 那么系综 $\{\lambda_j, \ket{j}\}$ 便对应了 $\rho$.

!!! success "Postulta in density operator language"
    (Postulate 1) 任何孤立的物理系统都与一个带有内积的复线性空间相关联，称为该系统的状态空间. 系统完全由密度算子描述，其是正算子，满足 $\op{Tr} (\rho) = 1$，并且作用在状态空间上. 如果一个量子系统处于状态 $\rho_i$ 的概率为 $p_i$，那么系统的密度算子为 $\rho = \sum_i p_i \rho_i$.

    (Postulate 2) 一个封闭量子系统的演化由一个酉算子 $U$ 描述，即 $t_1$ 时刻的密度算子 $\rho$ 和 $t_2$ 时刻的密度算子 $\rho'$ 通过仅依赖于 $t_1$ 和 $t_2$ 的酉算子 $U$ 相关联，即

    \[
        \rho' = U \rho U^\dagger.
    \]

    (Postulate 3) 量子测量由一组测量算子 $\{M_m\}$ 描述，其作用在被测量系统的状态空间上，下标 $m$ 对应测量可能的结果. 如果量子系统测量前处于状态 $\rho$，那么结果 $m$ 出现的概率为

    \[
        p(m) = \op{Tr} (M_m^\dagger M_m \rho).
    \]

    并且在此次测量后，系统的状态变为

    \[
        \dfrac{M_m \rho M_m^\dagger}{\op{Tr} (M_m^\dagger M_m \rho)}.
    \]

    测量算子满足完备性条件，即

    \[
        \sum_m M_m^\dagger M_m = I.
    \]

    (Postulate 4) 一个量子系统的状态空间是各个组成部分的状态空间的张量积. 如果组成部分的编号从 $1$ 到 $n$，并且第 $i$ 个系统位于状态 $\rho_i$，那么整个系统的状态为 $\rho_1 \otimes \rho_2 \otimes \cdots \otimes \rho_n$.

!!! tip
    如下给出一密度矩阵

    \[
        \rho = \dfrac{3}{4} \ket{0} \bra{0} + \dfrac{1}{4} \ket{1} \bra{1}.
    \]

    很自然地，有人会认为其以 $\dfrac{3}{4}$ 的概率处于 $\ket{0}$，以 $\dfrac{1}{4}$ 的概率处于 $\ket{1}$. 但事实上并非如此，考虑如下两个态

    \begin{gather*}
        \ket{a} = \sqrt{\dfrac{3}{4}} \ket{0} + \sqrt{\dfrac{1}{4}} \ket{1}, \\
        \ket{b} = \sqrt{\dfrac{3}{4}} \ket{0} - \sqrt{\dfrac{1}{4}} \ket{1}.
    \end{gather*}

    并且该系统处于 $\ket{a}$ 的概率为 $\dfrac{1}{2}$，处于 $\ket{b}$ 的概率也为 $\dfrac{1}{2}$. 计算密度算子可以得到

    \[
        \rho = \dfrac{1}{2} \ket{a} \bra{a} + \dfrac{1}{2} \ket{b} \bra{b} = \dfrac{3}{4} \ket{0} \bra{0} + \dfrac{1}{4} \ket{1} \bra{1}.
    \]

    也就是说，两个不同的系综关联了同一个密度算子. 事实上，特征值和特征向量只是一个密度算子关联的诸多系综中的一个，其并不特殊.

那么自然而然地，我们会想到，满足什么条件的系综能生成同一个密度算子呢？接下来会使用未规范化的状态向量 $\ket{\tilde{\psi}_i}$ 来描述密度算子. 称 $\ket{\tilde{\psi}_i}$ 生成了算子 $\rho$，如果 $\rho = \sum_i \ket{\tilde{\psi}_i} \bra{\tilde{\psi}_i}$. 因而 $\ket{\tilde{\psi}_i}$ 与常见系综的关联由表达式 $\ket{\tilde{\psi}_i} = \sqrt{p_i} \ket{\psi_i}$ 给出. 接下来便是考虑 $\ket{\tilde{\psi}_i}$ 和 $\ket{\tilde{\varphi}_j}$ 何时生成同一个密度算子.

!!! note "Theorem"
    (Unitary freedom in the ensemble for density matrices) 集合 $\ket{\tilde{\psi}_i}$ 和 $\ket{\tilde{\varphi}_j}$ 生成了同一个密度算子当且仅当

    \[
        \ket{\tilde{\psi}_i} = \sum_j u_{ij} \ket{\tilde{\varphi}_j},
    \]

    其中 $u_{ij}$ 构成一个酉矩阵，下标为 $i$ 和 $j$. 如果两个集合元素数量不同，那么对较小的集合进行零向量填充.

    ??? note "Proof"

        $(\Leftarrow)$ 假定 $\ket{\tilde{\psi}_i} = \sum_j u_{ij} \ket{\tilde{\varphi}_j}$，那么

        \begin{align*}
            \sum_i \ket{\tilde{\psi}_i} \bra{\tilde{\psi}_i} & = \sum_{i, j, k} u_{ij} u_{ik}^* \ket{\tilde{\varphi}_j} \bra{\tilde{\varphi}_k} \\
                                                             & = \sum_{j, k} \left(\sum_i u_{ki}^\dagger u_{ij}\right) \ket{\tilde{\varphi}_j} \bra{\tilde{\varphi}_k} \\
                                                             & = \sum_{j, k} \delta_{jk} \ket{\tilde{\varphi}_j} \bra{\tilde{\varphi}_k} \\
                                                             & = \sum_j \ket{\tilde{\varphi}_j} \bra{\tilde{\varphi}_j}.
        \end{align*}

        $(\Rightarrow)$ 假定 $A = \sum_i \ket{\tilde{\psi}_i} \bra{\tilde{\psi}_i} = \sum_j \ket{\tilde{\varphi}_j} \bra{\tilde{\varphi}_j}$.

        设 $A = \sum_k \lambda_k \ket{k} \bra{k}$ 是 $A$ 的谱分解，因而 $\ket{k}$ 是正交归一的. 证明的策略是将 $\ket{\tilde{\psi}_i}$ 和 $\ket{\tilde{\varphi}_j}$ 与 $\ket{\tilde{k}} = \sqrt{\lambda_k} \ket{k}$ 关联起来. 

        设 $\ket{\varphi}$ 是一个与 $\ket{\tilde{k}}$ 张成的空间正交的态，那么有 $\innerproduct{\varphi}{\tilde{k}} \innerproduct{\tilde{k}}{\varphi} = 0$. 从而

        \[
            0 = \bra{\varphi} A \ket{\varphi} = \sum_i \innerproduct{\varphi}{\tilde{\psi}_i} \innerproduct{\tilde{\psi}_i}{\varphi} = \sum_i \left\lvert \innerproduct{\varphi}{\tilde{\psi}_i} \right\rvert^2.
        \]

        所以对任意满足条件的 $i$ 和 $\ket{\varphi}$，有 $\innerproduct{\varphi}{\tilde{\psi}_i} = 0$. 所以 $\ket{\tilde{\psi}_i}$ 可以由 $\ket{\tilde{k}}$ 线性表示. 设 $\ket{\tilde{\psi}_i} = \sum_k c_{ik} \ket{\tilde{k}}$. 因为 $A = \sum_k \ket{\tilde{k}} \bra{\tilde{k}} = \sum_i \ket{\tilde{\psi}_i} \bra{\tilde{\psi}_i}$，所以

        \[
            \sum_k \ket{\tilde{k}} \bra{\tilde{k}} = \sum_{kl} \left(\sum_i c_{ik} c_{il}^*\right) \ket{\tilde{k}} \bra{\tilde{l}}.
        \]

        而因为 $\ket{\tilde{k}} \bra{\tilde{l}}$ 是线性无关的，所以 $\sum_i c_{ik} c_{il}^* = \delta_{kl}$. 进而向 $c$ 中添加额外列使其构成酉矩阵 $v$ 满足 $\ket{\tilde{\psi}_i} = \sum_k v_{ik} \ket{\tilde{k}}$. 类似地，可以得到 $\ket{\tilde{\varphi}_j} = \sum_k w_{jk} \ket{\tilde{k}}$. 从而 $\ket{\tilde{\psi}_i} = \sum_j u_{ij} \ket{\tilde{\varphi}_j}$，其中 $u = v w^\dagger$ 是酉矩阵.

!!! note "Exercise"
    (Bloch sphere for mixed states) The Bloch sphere picture for pure states of a single qubit was introduced in Section 1.2. This description has an important generalization to mixed states as follows.

    1. Show that an arbitrary density matrix for a mixed state qubit may be written as

        \[
            \rho = \dfrac{1}{2} (I + \vec{r} \cdot \vec{\sigma}),
        \]

        where $\vec{r}$ is a real three-dimensional vector such that $\lvert \vec{r} \rvert \leq 1$. This vector is known as the *Bloch vector* for the state $\rho$.

    2. What is the Bloch vector representation for the state $\rho = \dfrac{I}{2}$?

    3. Show that a state is pure if and only if $\lvert \vec{r} \rvert = 1$.

    4. Show that for pure states the description of the Bloch vector we have given coincides with that in Section 1.2.

### The reduced density operator

设 $A$ 和 $B$ 为两个物理系统，状态由密度算子 $\rho^{AB}$ 给出，那么系统 $A$ 的约化密度算子定义为

\[
    \rho^A = \op{Tr}_B (\rho^{AB}),
\]

其中 $\op{Tr}_B$ 是系统 $B$ 上的偏迹算子，按如下方式定义：

\[
    \op{Tr}_B (\ket{a_1} \bra{a_2} \otimes \ket{b_1} \bra{b_2}) = \ket{a_1} \bra{a_2} \op{Tr} (\ket{b_1} \bra{b_2}).
\]

也可以写作

\[
    \op{Tr}_B (C) = \sum_i (\bra{i} \otimes I) C (\ket{i} \otimes I).
\]

假定 $M$ 是系统 $A$ 的任意可观测量，并且可以实施对 $M$ 的测量. 设 $\tilde{M}$ 对应该观测量的测量，但是是在整个系统 $AB$ 上实施. 首先是证明 $\tilde{M} = M \otimes I_B$，其中 $I_B$ 是系统 $B$ 上的恒等算子. 注意到，如果 $AB$ 的状态为 $\ket{m} \ket{\psi}$，其中 $\ket{m}$ 是 $M$ 对应 $m$ 结果的本征态，$\ket{\psi}$ 是系统 $B$ 的任意态，那么测量结果为 $m$ 的概率为 $1$. 如果 $P_m$ 是 $M$ 对应 $m$ 结果的投影算子，那么 $\tilde{M}$ 对应的投影算子为 $P_m \otimes I_B$. 由此可知

\[
    \tilde{M} = \sum_m m P_m \otimes I_B = M \otimes I_B.
\]

接下来要证明偏迹给出了系统可观测量的正确的测量统计结果. 根据统计一致性的要求，无论是通过 $\rho^A$ 直接计算，还是通过 $\rho^{AB}$ 间接计算，都应该得到相同的结果. 也就应该有

\[
    \op{Tr} (\tilde{M} \rho^{AB}) = \op{Tr} ((M \otimes I_B) \rho^{AB}) = \op{Tr} (M \rho^A).
\]

如果选择 $\rho^A = \op{Tr}_B (\rho^{AB})$，那么上式显然是成立的. 接下来要证明其是唯一的. 假定存在一个映射 $f(\cdot)$ 将 $AB$ 上的密度算子映射到 $A$ 上的密度算子，且对于所有可观测量 $M$ 均满足

\[
    \op{Tr} (M f(\rho^{AB})) = \op{Tr} ((M \otimes I_B) \rho^{AB}).
\]

取自伴算子空间的一组正交基 $\{M_i\}$，按 Hilbert-Schmidt 内积定义（即 $(X, Y) = \op{Tr} (X Y)$），展开 $f(\rho^{AB})$，有

\begin{align*}
    f(\rho^{AB}) & = \sum_i (M_i, f(\rho^{AB})) M_i \\
                 & = \sum_i \op{Tr} (M_i f(\rho^{AB})) M_i \\
                 & = \sum_i \op{Tr} ((M_i \otimes I_B) \rho^{AB}) M_i \\
\end{align*}

所以 $f(\rho^{AB})$ 被唯一线性表示，并且 $\op{Tr}_B$ 满足上述要求，所以 $f = \op{Tr}_B$.

即使一个复合系统处于纯态，其子系统的约化密度算子也可能是混合态，如 Bell 态 $\dfrac{1}{\sqrt{2}} (\ket{00} + \ket{11})$.

#### Quantum teleportation and the reduced density operator

约化密度算子的一个重要应用便是分析量子隐形传态. 回忆在 Alice 进行测量前，整个系统的状态为

\begin{align*}
    \ket{\psi_2} = \dfrac{1}{2} [ & \ket{00} (\alpha \ket{0} + \beta \ket{1}) + \ket{01} (\alpha \ket{1} + \beta \ket{0}) \\
                                + & \ket{10} (\alpha \ket{0} - \beta \ket{1}) + \ket{11} (\alpha \ket{1} - \beta \ket{0}) ].
\end{align*}

在 Alice 的测量基下测量的话，系综为

\begin{gather*}
    p_1 = \dfrac{1}{4}, \quad \ket{\psi^1} = \ket{00} (\alpha \ket{0} + \beta \ket{1}), \\
    p_2 = \dfrac{1}{4}, \quad \ket{\psi^2} = \ket{01} (\alpha \ket{1} + \beta \ket{0}), \\
    p_3 = \dfrac{1}{4}, \quad \ket{\psi^3} = \ket{10} (\alpha \ket{0} - \beta \ket{1}), \\
    p_4 = \dfrac{1}{4}, \quad \ket{\psi^4} = \ket{11} (\alpha \ket{1} - \beta \ket{0}).
\end{gather*}

系统的密度算子为

\begin{align*}
    \rho = \dfrac{1}{4} [ & \ket{00} \bra{00} (\alpha \ket{0} + \beta \ket{1}) (\alpha^* \bra{0} + \beta^* \bra{1}) + \ket{01} \bra{01} (\alpha \ket{1} + \beta \ket{0}) (\alpha^* \bra{1} + \beta^* \bra{0}) \\
                        + & \ket{10} \bra{10} (\alpha \ket{0} - \beta \ket{1}) (\alpha^* \bra{0} - \beta^* \bra{1}) + \ket{11} \bra{11} (\alpha \ket{1} - \beta \ket{0}) (\alpha^* \bra{1} - \beta^* \bra{0}) ] .
\end{align*}

因而可以得到 Bob 系统的约化密度算子为

\begin{align*}
    \rho^B & = \op{Tr}_A (\rho) \\
           & = \dfrac{1}{4} [ (\alpha \ket{0} + \beta \ket{1}) (\alpha^* \bra{0} + \beta^* \bra{1}) + (\alpha \ket{1} + \beta \ket{0}) (\alpha^* \bra{1} + \beta^* \bra{0}) \\
           & + (\alpha \ket{0} - \beta \ket{1}) (\alpha^* \bra{0} - \beta^* \bra{1}) + (\alpha \ket{1} - \beta \ket{0}) (\alpha^* \bra{1} - \beta^* \bra{0}) ] \\
           & = \dfrac{2(\lvert \alpha \rvert^2 + \lvert \beta \rvert^2)\ket{0} \bra{0} + 2(\lvert \alpha \rvert^2 + \lvert \beta \rvert^2)\ket{1}}{4} \\
           & = \dfrac{I}{2}.
\end{align*}

所以 Alice 测量后但 Bob 接收到信息前，Bob 的系统状态与传输的 $\ket{\psi}$ 无关，无论 Bob 进行什么测量，都不会得到与 $\ket{\psi}$ 有关的信息. 这也就阻止了信息的超光速传输.

### The Schmidt decomposition and purifications

!!! note "Theorem"
    (Schmidt decomposition) 设 $\ket{\psi}$ 是复合系统 $AB$ 的一个纯态，那么存在 $A$ 的一组正交基 $\{\ket{i_A}\}$ 和 $B$ 的一组正交基 $\{\ket{i_B}\}$ 使得

    \[
        \ket{\psi} = \sum_i \lambda_i \ket{i_A} \ket{i_B},
    \]

    其中 $\lambda_i$ 是非负实数，且满足 $\sum_i \lvert \lambda_i \rvert^2 = 1$，被称作 Schmidt 系数.

    ??? note "Proof"
        以下给出 $A$ 和 $B$ 的状态空间维数相同的情况的证明. 

        设 $\ket{j}$ 和 $\ket{k}$ 分别是 $A$ 和 $B$ 的一组正交基，那么 $\ket{\psi}$ 可以展开为

        \[
            \ket{\psi} = \sum_{jk} a_{jk} \ket{j} \ket{k}.
        \]

        根据奇异值分解，$a = udv$，其中 $d$ 是元素为非负实数的对角矩阵，$u$ 和 $v$ 是酉矩阵. 从而

        \[
            \ket{\psi} = \sum_{ijk} u_{ji} d_{ii} v_{ik} \ket{j} \ket{k}.
        \]

        定义 $\ket{i_A} = \sum_j u_{ji} \ket{j}$ 和 $\ket{i_B} = \sum_k v_{ik} \ket{k}$，$\lambda_i = d_{ii}$，那么就有

        \[
            \ket{\psi} = \sum_i \lambda_i \ket{i_A} \ket{i_B}.
        \]

        容易验证 $\{\ket{i_A}\}$ 和 $\{\ket{i_B}\}$ 是正交的.

这一结果十分有效，考虑 $A$ 和 $B$ 的约化密度算子，可以得到

\begin{gather*}
    \rho^A = \sum_i \lambda_i^2 \ket{i_A} \bra{i_A}, \\
    \rho^B = \sum_i \lambda_i^2 \ket{i_B} \bra{i_B}.
\end{gather*}

也就是说二者的特征值是一致的. 

$\ket{i_A}$ 和 $\ket{i_B}$ 被称为 Schmidt 基，非零的 $\lambda_i$ 被称为态 $\ket{\psi}$ 的 Schmidt 数. 可以注意到 Schmidt 数在酉变化下是不变的.

纯化也是一个重要的技术. 给定量子系统 $A$ 的状态 $\rho^A$，可以引进一个参考系统 $R$，并在其上定义一个纯态 $\ket{AR}$，使得 $A$ 的约化密度算子 $\rho^A = \op{Tr}_R (\ket{AR} \bra{AR})$. 这便允许我们将纯态和混合态相关联. 

下面说明纯化可以对任何态进行，为此需要展示如何构建参考系统 $R$ 和纯态 $\ket{AR}$. 设 $\rho^A$ 的谱分解为 $\rho^A = \sum_i p_i \ket{i^A} \bra{i^A}$，定义 $R$ 的状态空间与 $A$ 相同，正交基为 $\{\ket{i^R}\}$，那么 $\ket{AR}$ 可以定义为

\[
    \ket{AR} = \sum_i \sqrt{p_i} \ket{i^A} \ket{i^R}.
\]

接下来验证 $\op{Tr}_R (\ket{AR} \bra{AR}) = \rho^A$.

\begin{align*}
    \op{Tr}_R (\ket{AR} \bra{AR}) & = \sum_{ij} \sqrt{p_i p_j} \ket{i^A} \bra{j^A} \op{Tr} (\ket{i^R} \bra{j^R}) \\
                                  & = \sum_{ij} \sqrt{p_i p_j} \ket{i^A} \bra{j^A} \delta_{ij} \\
                                  & = \sum_i p_i \ket{i^A} \bra{i^A} = \rho^A.
\end{align*}

所以 $\ket{AR}$ 确实是 $\rho^A$ 的纯化. 

!!! note "Exercise"
    (Freedom in purifications) Let $\ket{AR_1}$ and $\ket{AR_2}$ be two purifications of a state $\rho^A$ to a composite system $AR$. Prove that there exists a unitary operator $U_R$ acting on $R$ such that $\ket{AR_2} = (I_A \otimes U_R) \ket{AR_1}$.

## EPR and the Bell inequality

!!! note "Anti-correlations in the EPR experiment"
    假定制备了如下状态

    \[
        \ket{\psi} = \dfrac{\ket{01} - \ket{10}}{\sqrt{2}}.
    \]

    出于历史原因，该态也被称为自旋单态（spin singlet），不难验证这是一个纠缠态. 如果对两个量子比特进行 $\vec{v}$ 方向上的测量，那么便是进行可观测量 $\vec{v} \cdot \vec{\sigma}$ 的测量，每个量子比特上得到 $+1$ 或 $-1$. 而两个量子比特上的测量结果总是相反的，就好像第二个量子比特知道第一个量子比特的测量结果一样. 设 $\vec{v} \cdot \vec{\sigma}$ 的特征态为 $\ket{a}$ 和 $\ket{b}$，那么存在复数 $\alpha, \beta, \gamma, \delta$ 使得

    \begin{gather*}
        \ket{0} = \alpha \ket{a} + \beta \ket{b}, \\
        \ket{1} = \gamma \ket{a} + \delta \ket{b}.
    \end{gather*}

    代入 $\ket{\psi}$，可以得到

    \begin{align*}
        \ket{\psi} & = \dfrac{\ket{01} - \ket{10}}{\sqrt{2}} \\
                   & = \dfrac{1}{\sqrt{2}} ((\alpha \ket{a} + \beta \ket{b}) (\gamma \ket{a} + \delta \ket{b}) - (\gamma \ket{a} + \delta \ket{b}) (\alpha \ket{a} + \beta \ket{b})) \\
                   & = (\alpha \delta - \beta \gamma) \dfrac{\ket{ab} - \ket{ba}}{\sqrt{2}}.
    \end{align*}

    而 $\alpha \delta - \beta \gamma$ 是酉矩阵 $\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}$ 的行列式，所以 $\alpha \delta - \beta \gamma = e^{i \theta}$，其中 $\theta$ 是实数. 也就是说，$\ket{\psi}$ 与 $\dfrac{\ket{ab} - \ket{ba}}{\sqrt{2}}$ 在忽略一个全局相位的情况下是等价的.

所以，如果 Alice 持有该态的一个量子比特，Bob 持有另一个量子比特，只要他们都沿着 $\vec{v}$ 方向进行测量，那么他们的测量结果总是相反的. 如果 Alice 先进行测量的话，她便可以立刻知道 Bob 的测量结果. 

接下来介绍 Bell 不等式. 设 Alice 和 Bob 之间的距离足够远，Charles 制备了一个量子态，并且将其中一个量子比特送给 Alice，另一个量子比特送给 Bob. 一旦 Alice 接收到了量子比特，她便开始进行测量，其有两种测量选择，分别对应性质 $P_Q$ 和 $P_R$. Alice 本身不预设进行哪种测量，而是根据一个公平的硬币来决定. 假设 Alice 的粒子的 $P_Q$ 属性的值为 $Q$，$Q$ 被认为是粒子的客观属性，测量仅仅是揭示了这一属性. 类似地，$R$ 表示测量属性 $P_R$ 所揭示的属性. Bob 进行的测量对应的属性记为 $P_S$ 和 $P_T$，其值分别为 $S$ 和 $T$. 实验的安排使得 Alice 和 Bob 的测量是同时进行的，或者说以因果关系断开的方式进行的，他们的测量结果无法相互影响.

现在对表达式 $QS + RS + RT - QT$ 进行一些简单的代数运算. 注意到

\[
    QS + RS + RT - QT = (Q + R)S + (R - Q)T.   
\]

而因为 $R, Q = \pm 1$，所以要么 $(Q + R)S = 0$，要么 $(R - Q)T = 0$. 无论哪种情况，都有 $(Q + R)S + (R - Q)T = \pm 2$. 设 $p(q, r, s, t)$ 为测量前系统处于 $Q = q, R = r, S = s, T = t$ 的概率，用 $\mathbf{E}(\cdot)$ 表示期望值，那么

\begin{align*}
    \mathbf{E}(QS + RS + RT - QT) & = \sum_{qrst} p(q, r, s, t) (qr + rs + rt - qt) \\
                                  & \leq \sum_{qrst} p(q, r, s, t) \times 2 \\
                                  & = 2.
\end{align*}

另一方面，将期望展开，有

\[
    \mathbf{E}(QS + RS + RT - QT) = \mathbf{E}(QS) + \mathbf{E}(RS) + \mathbf{E}(RT) - \mathbf{E}(QT).
\]

所以得到 Bell 不等式

\[
    \mathbf{E}(QS) + \mathbf{E}(RS) + \mathbf{E}(RT) - \mathbf{E}(QT) \leq 2.
\]

现在 Charlie 制备了量子态

\[
    \ket{\psi} = \dfrac{\ket{01} - \ket{10}}{\sqrt{2}}
\]

其将第一个粒子传递给 Alice，第二个传递给 Bob，并且对如下可观测量进行测量

\begin{gather*}
    Q = Z_1, \quad S = \dfrac{-Z_2 - X_2}{\sqrt{2}}, \\
    R = X_1, \quad T = \dfrac{Z_2 - X_2}{\sqrt{2}}.
\end{gather*}

简单计算这些可观测量的期望，便可以得到

\[
    \langle QS \rangle = \dfrac{1}{\sqrt{2}}; \quad \langle RS \rangle = \dfrac{1}{\sqrt{2}}; \quad \langle RT \rangle = \dfrac{1}{\sqrt{2}}; \quad \langle QT \rangle = -\dfrac{1}{\sqrt{2}}.
\]

也就有

\[
    \langle QS \rangle + \langle RS \rangle + \langle RT \rangle - \langle QT \rangle = 2\sqrt{2} > 2.
\]

所以量子力学是违背贝尔不等式的，也就是说推导贝尔不等式的一个或者多个假设是错误的. 以下的两个假设是存疑的：

1. 实在性假设：物理属性 $P_Q, P_R, P_S, P_T$ 具有独立于测量的确定值 $Q, R, S, T$.

2. 局域性假设：Alice 和 Bob 之间的测量是因果关系断开的，他们的测量结果无法相互影响.

这两个假设合称为局域实在性假设. 它们看似符合直觉且与日常经验一致，但 Bell 不等式表明其中至少一个假设不成立.