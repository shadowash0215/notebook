# Generalities on linear representations

## Definitions

设 $V$ 是一复线性空间，$\mathbf{GL}(V)$ 是 $V$ 的自同构组成的群. 显然若 $V$ 有一组有 $n$ 个元素的基 $(e_i)$ 时，每个线性映射 $a \in \mathbf{GL}(V)$ 都可以用一个 $n$ 阶的可逆矩阵 $(a_{ij})$ 表示.

设 $G$ 是有限乘法群，$G$ 在 $V$ 上的一个线性表示是指从群 $G$ 到 $\mathbf{GL}(V)$ 的一个群同态 $\rho: G \to \mathbf{GL}(V)$，满足

\[
    \rho(st) = \rho(s)\rho(t), \ s, t \in G.
\]

也经常简记 $\rho(s)$ 为 $\rho_s$.

当 $\rho$ 给定后，称 $V$ 为 $G$ 的表示空间. 我们在这里只研究表示空间为有限维的情况.

设 $R_s$ 为 $\rho_s$ 在基 $(e_i)$ 下的矩阵表示，显然有

\[
    \det(R_s) \neq 0, \quad R_{st} = R_s \cdot R_t, \ s, t \in G.
\]

从矩阵元角度入手的话，第二条规则变为

\[
    r_{ik}(st) = \sum_j r_{ij}(s) \cdot r_{jk} (t).
\]

设 $\rho$ 和 $\rho'$ 是同一群 $G$ 分别在空间 $V$ 和 $V'$ 上的表示，这两个表示被称为等价的，如果存在线性同构 $\tau: V \to V'$ 满足

\[
    \tau \circ \rho_s = \rho'_s \circ \tau, \quad \forall s \in G.
\]

矩阵形式为

\[
    T \cdot R_s = R_s' \cdot T, \quad \forall s \in G.
\]


!!! example
    - 群 $G$ 的度为 $1$ 的表示指同态 $\rho: G \to \mathbb{C}^*$，而因为 $G$ 中的元素的阶都是有限的，所以 $\rho(s)$ 都是单位根，即有 $\abs{\rho(s)} = 1$. 而 $\rho(s) = 1, \forall s \in G$ 的表示被称为 $G$ 的单位/平凡表示.

    - 设 $g$ 为 $G$ 的阶，$V$ 为维数为 $g$ 的线性空间，且有以 $G$ 中元素 $t \in G$ 索引的一组基 $\{e_t\}_{t \in G}$. 对于任意 $s \in G$，设 $\rho_s$ 为 $V$ 的自同构，其将 $e_t$ 映射到 $e_{st}$. 这便定义了群 $G$ 的一个线性表示，称为正则表示，其度等于 $G$ 的阶. 因为 $e_s = \rho_s(e_1)$，所以 $e_1$ 的所有像形成了 $V$ 的一组基. 反之，如果 $W$ 是 $G$ 的一个表示，并且包含一个向量 $w$，使得 $\rho_s(w), s \in G$ 形成了 $W$ 的一组基，那么 $W$ 同构于正则表示.

## Subrepresentations

设 $\rho: G \to \mathbf{GL}(V)$，$W$ 为 $V$ 的子空间. 称 $W$ 在 $G$ 的作用下不变，若 $x \in W$，则有 $\rho_s x \in W, \forall s \in G$. $\rho_s$ 在 $W$ 上的限制 $\rho_s^W$ 实际上也是 $W$ 的自同构，并且满足 $\rho_{st}^W = \rho_s^W \cdot \rho_t^W$. 所以 $\rho^W: G \to \mathbf{GL}(W)$ 是 $G$ 在 $W$ 上的表示，称为子表示.

!!! note "Theorem"
    $\rho: G \to \mathbf{GL}(V)$ 是 $G$ 在 $V$ 上的线性表示，$W$ 为 $V$ 在 $G$ 下的不变子空间，那么存在 $W$ 的一个补空间 $W^0$ 也在 $G$ 下不变.

    ???+ note "Proof"
        设 $W'$ 为 $W$ 的任意补空间，$p$ 为其对应的 $V$ 到 $W$ 的投影映射，通过将 $p$ 与 $G$ 的元素共轭后取平均来构造 $p_0$：

        \[
            p_0 = \frac{1}{g} \sum_{t \in G} \rho_t \cdot p \cdot \rho_t^{-1}
        \]

        容易验证 $p_0$ 将 $V$ 映射到 $W$，并且有

        \[
            \rho_t \cdot p \cdot \rho_t^{-1} x = \rho_t \cdot \rho_t^{-1} x = x, \forall x \in W.
        \]

        所以有 $p_0 x = x$，$p_0$ 也是 $V$ 到 $W$ 的投影映射，对应于某个补空间 $W^0$. 并且还有

        \[
            \rho_s p_0 = p_0 \rho_s, \forall s \in G.
        \]

        所以如果 $x \in W^0$，就有 $p^0 x = 0$，即对于任意的 $p^0 \cdot p_s x = p_s \cdot p^0 x = 0$，即 $p_s x \in W^0$，$W^0$ 在 $G$ 下不变.

    !!! tip "通过构建 $G$ 下不变的内积也可以证明"

内积的不变性表明如果 $(e_i)$ 是一组单位正交基，那么 $\rho_s$ 关于这组基的矩阵便是酉矩阵.

## Irreducible representations

设 $\rho: G \to \mathbf{GL}(V)$ 为 $G$ 的线性表示，若 $V$ 不为 $0$ 且没有非平凡子空间在 $G$ 下不变，那么 $\rho$ 被称为不可约的，第二个条件也就等同于其不是两个表示的直和.

!!! note "Theorem"
    每个表示都是不可约表示的直和.

    ??? note "Proof"
        数学归纳法.

## Tensor product of two representations

$\rho^1: G \to \mathbf{GL}(V_1)$，$\rho^2: G \to \mathbf{GL}(V_2)$ 为群 $G$ 的两个线性表示，对于 $s \in G$，定义 $\rho_s: G \to \mathbf{GL}(V_1 \otimes V_2)$ 为

\[
    \rho_s(x_1 \cdot x_2) = \rho_s^1(x_1) \cdot \rho_s^2(x_2), \ x_1 \in V_1, x_2 \in V_2.
\]

也就是

\[
    \rho_s = \rho_s^1 \otimes \rho_s^2.
\]

## Symmetric square and alternating square

设 $(e_i)$ 为 $V$ 的一组基，$\theta$ 为 $V \otimes V$ 的一个自同构，满足：

\[
    \theta(e_i \cdot e_j) = e_j \cdot e_i, \ \forall (i, j).
\]

而对于任意 $x, y \in V$，有

\[
    \theta(x \cdot y) = y \cdot x,
\]

说明 $\theta$ 是不依赖于基的；此外有 $\theta^2 = 1$. 所以 $V \otimes V$ 可以分解为直和

\[
    V \otimes V = \mathbf{Sym}^2(V) \oplus \mathbf{Alt}^2(V),
\]

其中 $\mathbf{Sym}^2(V)$ 是 $z \in V \otimes V$ 使得 $\theta(z) = z$ 的集合，而 $\mathbf{Alt}^2(V)$ 是 $z \in V \otimes V$ 使得 $\theta(z) = -z$ 的集合. $(e_i \cdot e_j + e_j \cdot e_i)_{i \leq j}$ 形成了 $\mathbf{Sym}^2(V)$ 的一组基，而 $(e_i \cdot e_j - e_j \cdot e_i)_{i < j}$ 形成了 $\mathbf{Alt}^2(V)$ 的一组基. 如果 $\op{dim} V = n$，显然有

\[
    \op{dim} \mathbf{Sym}^2(V) = \frac{n(n+1)}{2}, \quad \op{dim} \mathbf{Alt}^2(V) = \frac{n(n-1)}{2}.
\]

它们都在 $G$ 的作用下不变，因此分别定义了对称平方表示和交替平方表示.