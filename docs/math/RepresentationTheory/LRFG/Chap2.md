# Character theory

## The character of a representation

$\rho: G \to \mathbf{GL}(V)$ 是有限群 $G$ 在 $V$ 上的线性表示. 对任一 $s \in G$，定义

\[
    \chi_\rho(s) = \op{Tr}(\rho(s)),
\]

这样定义得到的复值函数 $\chi_\rho: G \to \mathbb{C}$ 被称为表示 $\rho$ 的特征标.

!!! note "Proposition"
    - 如果 $\chi$ 是一个度为 $n$ 的表示的特征标，便有：

        1. $\chi(1) = n$

        2. $\chi(s^{-1}) = \overline{\chi(s)}, \forall s \in G$

        3. $\chi(tst^{-1}) = \chi(s), \forall s, t \in G$

        !!! tip "Remark"
            满足第 3 点的函数被称为类函数，类函数实际上都是特征标的线性组合.

    - $\rho^1: G \to \mathbf{GL}(V_1)$ 和 $\rho^2: G \to \mathbf{GL}(V_2)$ 是 $G$ 的两个线性表示，$\chi_1$ 和 $\chi_2$ 分别是这两个表示的特征标. 那么：

        1. 表示的直和 $V_1 \oplus V_2$ 的特征标 $\chi$ 为 $\chi_1 + \chi_2$.

        2. 表示的张量积 $V_1 \otimes V_2$ 的特征标 $\chi$ 为 $\chi_1 \cdot \chi_2$.

    - $\rho: G \to \mathbf{GL}(V)$ 为 $G$ 的一个线性表示，$\chi$ 为其特征标. 设 $\chi_\sigma^2$ 为 $\mathbf{Sym}^2(V)$ 的特征标，$\chi_\alpha^2$ 为 $\mathbf{Alt}^2(V)$ 的特征标. 则对于任意 $s \in G$，有：

        \begin{gather*}
            \chi_\sigma^2(s) = \frac{1}{2} \left( \chi(s)^2 + \chi(s^2) \right) \\
            \chi_\alpha^2(s) = \frac{1}{2} \left( \chi(s)^2 - \chi(s^2) \right).
        \end{gather*}

        显然也有 $\chi_\sigma^2 + \chi_\alpha^2 = \chi^2$.

## Schur's lemma; basic applications

!!! success "Schur's lemma"
    设 $\rho^1: G \to \mathbf{GL}(V_1)$ 和 $\rho^2: G \to \mathbf{GL}(V_2)$ 是 $G$ 的两个不可约表示，$f$ 为 $V_1$ 到 $V_2$ 的线性映射，满足 $\forall s \in G, \rho_s^2 \circ f = f \circ \rho_s^1$. 则：

    - 如果 $\rho^1$ 和 $\rho^2$ 是不同构的，则 $f = 0$;

    - 如果 $V_1 = V_2$ 并且 $\rho_1 = \rho_2$，则 $f$ 是一个位似（恒等映射的标量倍）.

    ???+ success "Proof"
        $f = 0$ 的情况是平凡的.

        考虑 $f \neq 0$，并且 $W_1$ 是 $f$ 的核空间. 对 $x \in W_1$，有 $f(\rho_s^1(x)) = \rho_s^2(f(x)) = 0$，也就是说 $\rho_s^1(x) \in W_1$，$W_1$ 在 $G$ 下不变. 因为 $V_1$ 是不可约的，所以 $W_1 = V_1$ 或 $W_1 = 0$. 第一种情况代表 $f = 0$，排除；所以 $W_1 = 0$. 类似的，设 $W_2$ 是 $f$ 的像空间，即 $y \in W_2$，总存在 $z \in V_1$，使得 $f(z) = y$. 从而 $\rho_s^2(f(z)) = \rho_s^2(y) = f(\rho_s^1(z)) \in W_2$，$W_2$ 在 $G$ 下不变. 同理得到 $W_2 = V_2$，即 $f$ 是 $V_1$ 到 $V_2$ 的同构.

        而 $V_1 = V_2$ 且 $\rho^1 = \rho^2$ 后，设 $\lambda$ 为 $f$ 的特征值. 令 $f' = f - \lambda I$，因为 $\lambda$ 是 $f$ 的特征值，所以 $\ker{f'} \neq 0$，并且同样有 $\rho_s^2 \circ f' = f' \circ \rho_s^1$，这表明 $f' = 0$，即 $f = \lambda I$.

保持 $V_1$ 和 $V_2$ 不可约的前提，记 $g$ 为群 $G$ 的阶.

!!! success "Corollary"
    - 设 $h$ 为 $V_1$ 到 $V_2$ 的线性映射，定义

        \[
            h^0 = \frac{1}{g} \sum_{t \in G} (\rho_t^2)^{-1} g \rho_t^1.
        \]

        则：

        1. 若 $\rho^1$ 和 $\rho^2$ 不同构有 $h^0 = 0$;

        2. 若 $V_1 = V_2$ 且 $\rho^1 = \rho^2$，则 $h^0$ 是一个比率为 $\frac{1}{n} \op{Tr}(h)$ 的位似.

        ???+ success "Proof"
            因为

            \begin{align*}
                (\rho_s^2)^{-1} h^0 \rho_s^1 & = \frac{1}{g} \sum_{t \in G} (\rho_s^2)^{-1} (\rho_t^2)^{-1} h \rho_t^1 \rho_s^1 \\
                & = \frac{1}{g} \sum_{t \in G} (\rho_{ts}^2)^{-1} h \rho_{ts}^1 = h^0.
            \end{align*}

            所以有 $\rho_s^2 h^0 = h^0 \rho_s^1$. 令 $f = h^0$ 便可以得到：

            1. 显然.

            2. $h^0 = \lambda I$. 此外，因为

                \[
                    \op{Tr}(h^0) = \frac{1}{g} \sum_{t \in G} \op{Tr}(\rho_t^{-1} h \rho_t) = \op{Tr}(h),
                \]

                所以 $n \lambda = \op{Tr}(h)$，$\lambda = \frac{1}{n} \op{Tr}(h)$.

    - 如果 $\rho^1$ 和 $\rho^2$ 是以矩阵形式给出的，即

        \[
            \rho_t^1 = (r_{i_1j_1}(t)), \rho_t^2 = (r_{i_2j_2}(t)).
        \]

        $h$ 由矩阵 $(x_{i_2i_1})$ 定义，$h^0$ 则类似由矩阵 $x_{i_2i_1}^0$ 定义，其中

        \[
            x_{i_2i_1}^0 = \frac{1}{g} \sum_{t, j_1, j_2} r_{i_2j_2}(t^{-1}) x_{j_2j_1} r_{j_1i_1}(t).
        \]

        右侧为关于 $x_{j_2j_1}$ 的线性形式. 
        
        1. 这个形式对于所有的 $x_{j_2j_1}$ 都是零，所以

            \[
                \frac{1}{g} \sum_{t \in G} r_{i_2j_2}(t^{-1}) x_{j_2j_1} r_{j_1i_1}(t) = 0.
            \]

            对任意 $i_1, i_2, j_1, j_2$ 成立.

        2. $h^0 = \lambda I$，所以 $x_{i_2i_1}^0 = \lambda \delta_{i_2i_1}$. 又因为 $\lambda = \frac{1}{n} \op{Tr}(h) = \frac{1}{n} \delta_{j_2j_1} x_{j_2j_1}$，所以对照 $x_{j_2j_1}$ 的系数可以得到

            \[
                \frac{1}{g} \sum_{t \in G} r_{i_2j_2}(t^{-1}) r_{j_1i_1}(t) = \frac{1}{n} \delta_{j_2j_1} \delta_{i_2i_1}.
            \]

    !!! tip "Remark"
        1. 若 $\phi$ 和 $\psi$ 均是 $G$ 上的函数，令

            \[
                \langle \phi, \psi \rangle = \frac{1}{g} \sum_{t \in G} \phi(t^{-1}) \psi(t) = \frac{1}{g} \sum_{t \in G} \psi(t^{-1}) \psi(t).
            \]

            也就有 $\langle \phi, \psi \rangle = \langle \psi, \phi \rangle$，并且 $\langle \phi, \psi \rangle$ 对于 $\phi$ 和 $\psi$ 是线性的. 所以矩阵形式的推论可以改写为

            \begin{gather*}
                \langle r_{i_2j_2}, r_{j_1i_1} \rangle = 0, \\
                \langle r_{i_2j_2}, r_{j_1i_1} \rangle = \frac{1}{n} \delta_{j_2j_1} \delta_{i_2i_1}.
            \end{gather*}

        2. 若矩阵 $r_{ij}(t)$ 均是酉矩阵，便有 $r_{ij}(t^{-1}) = \overline{r_{ji}(t)}$，此时矩阵形式的推论就是数量积 $(\phi \mid \psi)$ 的正交性关系.

## Orthogonality relations for characters

设 $\psi$ 和 $\phi$ 是两个 $G$ 上的复值函数，定义

\[
    (\phi \mid \psi) = \frac{1}{g} \sum_{t \in G} \phi(t) \overline{\psi(t)},
\]

为数量积，其对于 $\phi$ 线性，$\psi$ 共轭线性，且对任意 $\phi \neq 0$ 有 $(\phi \mid \phi) > 0$.

定义 $\hat{\psi}$ 满足 $\hat{\psi}(t) = \overline{\psi(t^{-1})}$，便有

\[
    (\phi \mid \psi) = \langle \phi, \hat{\psi} \rangle.
\]

而对于特征标 $\chi$，$\chi = \hat{\chi}$，因而对任意 $G$ 上的函数 $\phi$，均有 $(\phi \mid \chi) = \langle \phi, \chi \rangle$.

!!! note "Theorem"
    1. 若 $\chi$ 是不可约表示的特征标，则有 $(\phi \mid \chi) = 1$.

    2. 若 $\chi$ 和 $\chi'$ 分别是两个不同构的不可约表示的特征标，则有 $(\phi \mid \chi') = 0$.

    ???+ note "Proof"
        1. 设 $\rho$ 是特征标为 $\chi$ 的不可约表示，矩阵形式为 $\rho_t = r_{ij}(t)$. $\chi_t = \sum r_{ii}(t)$，因此

            \[
                (\phi \mid \chi) = \langle \phi, \chi \rangle = \sum_{i, j} \langle r_{ii}, r_{jj} \rangle.
            \]

            而 $\langle r_{ii}, r_{jj} \rangle = \delta_{ij}/n$，$n$ 为 $\rho$ 的度，所以

            \[
                (\phi \mid \chi) = \sum_{ij} \frac{\delta_{ij}}{n} = 1.
            \]

        2. 为类似的证明，不过用到的是 $\langle r_{ii}, r_{jj}' \rangle = 0$.

!!! note "Theorem"
    设 $V$ 是 $G$ 的一个线性表示，特征标为 $\phi$. $V$ 能被分解为一系列不可约表示的直和

    \[
        V = W_1 \oplus \cdots \oplus W_k.
    \]

    如果 $W$ 是一个不可约表示，特征标为 $\chi$，那么同构于 $W$ 的 $W_i$ 的个数等于数量积 $(\phi \mid \chi) = \langle \phi, \chi \rangle$.

    ???+ note "Proof"
        设 $W_i$ 的特征标为 $\chi_i$，则 

        \[
            \phi = \chi_1 + \cdots + \chi_k.
        \]

        从而 $(\phi \mid \chi) = (\chi_1 \mid \chi) + \cdots + (\chi_k \mid \chi)$. 而 $(\chi_i \mid \chi) = \begin{cases} 1, W_i \cong W \\ 0, W_i \ncong W \end{cases}$，所以得证.

    
!!! success "Corollary"
    - 同构于 $W$ 的 $W_i$ 的个数不依赖于直和分解的选取.

    - 拥有相同特征标的表示同构.

以上的结果将对表示的研究规约为对特征标的研究. 设 $\chi_1, \ldots, \chi_h$ 为 $G$ 的互异不可约特征标，$W_1, \ldots, W_h$ 为对应的不可约表示. 每个表示 $V$ 都同构于直和

\[
    V = m_1 W_1 \oplus \cdots \oplus m_h W_h,
\]

其中 $m_i$ 为非零整数. 所以 $V$ 的特征标为 $\phi = m_1 \chi_1 + \cdots + m_h \chi_h$，且 $m_i = (\phi \mid \chi_i)$. $\chi_i$ 之间的正交关系还可以得出：

\[
    (\phi \mid \phi) = \sum_{i = 1}^h m_i^2,
\]

所以有

!!! note "Theorem"
    若 $\phi$ 为表示 $V$ 的特征标，那么 $(\phi \mid \phi)$ 为正整数，并且等于 $1$ 当且仅当 $V$ 是不可约表示.

## Decomposition of the regular representation

设 $R$ 为 $G$ 的正则表示. 注意到若 $s \neq 1$，$\forall t$ 有 $st \neq t$，也就是说 $\rho_s$ 的主对角线上的元素均为零，$\op{Tr}(\rho_s) = 0$. 而 $s = 1$ 的话，就有 $\op{Tr}(\rho_1) = g$.

!!! note "Proposition"
    正则表示的特征标 $r_G$ 满足：

    \begin{gather*}
        r_G(1) = g, \\
        r_G(s) = 0, \quad s \neq 1. 
    \end{gather*}

!!! success "Corollary"
    - 所有不可约表示 $W_i$ 都包含在正则表示中，且重数等于其度数.

        ???+ success "Proof"
            \[
                \langle r_G, \chi_i \rangle = \frac{1}{g} \sum_{s \in G} r_G(s^{-1}) \chi_i(s) = \frac{1}{g} g \chi_i(1) = n_i.
            \]

    - 
        1. $n_i$ 满足 $\sum_{i=1}^h n_i^2 = g$.

        2. 如果 $s \in G$ 不等于 $1$，则 $\sum_{i=1}^h n_i \chi_i(s) = 0$.

## Number of irreducible representations

!!! note "Proposition"
    设 $f$ 为 $G$ 上的类函数，$\rho: G \to \mathbf{GL}(V)$ 是 $G$ 的一个线性表示，$\rho_f$ 为如下定义的 $V$ 上的线性变换：

    \[
        \rho_f = \sum_{t \in G} f(t) \rho_t.
    \]

    若 $V$ 度数为 $n$，不可约，特征标为 $\chi$，则 $\rho_f$ 是一个位似，比率为

    \[
        \lambda = \frac{1}{n} \sum_{t \in G} f(t) \chi(t) = \frac{g}{n} (f \mid \overline{\chi}).
    \]

    ???+ note "Proof"
        计算 $\rho_s^{-1} \rho_f \rho_s$，有

        \begin{align*}
            \rho_s^{-1} \rho_f \rho_s & = \sum_{t \in G} f(t) \rho_s^{-1} \rho_t \rho_s \\
                                      & = \sum_{t \in G} f(t) \rho_{s^{-1}ts} \\ 
                                      & = \sum_{u \in G} f(sus^{-1}) \rho_u \\ 
                                      & = \sum_{u \in G} f(u) \rho_u = \rho_f.
        \end{align*}

        即 $\rho_f \rho_s = \rho_s \rho_f$，$\rho_f$ 是一个位似，从而有

        \begin{gather*}
            n \lambda = \sum_{t \in G} f(t) \op{Tr}(\rho_t), \\
            \lambda = \frac{1}{n} \sum_{t \in G} f(t) \chi(t) = \frac{g}{n} (f \mid \overline{\chi}).
        \end{gather*}

现在引入群 $G$ 上类函数空间 $H$，不可约特征标 $\chi_1, \ldots, \chi_h$ 属于 $H$.

!!! note "Theorem"
    - 特征标 $\chi_1, \ldots, \chi_h$ 构成 $H$ 的一组标准正交基.

        ???+ note "Proof"
            先前的定理证明了不可约特征标之间的正交关系，接下来证明其张成整个空间 $H$，那么只需要证明和所有 $\overline{\chi_i}$ 都正交的元素只能是 $0$. 设 $f$ 为这样的元素，对任一 $G$ 的表示 $\rho$，定义 $\rho_f = \sum_{t \in G} f(t) \rho_t$. 若 $\rho$ 是不可约的，根据命题便可以计算得到 $\rho_f$ 为 $0$；而任一表示都可以直和分解为不可约表示，所以 $\rho_f$ 恒为 $0$. 将此结论应用于正则表示，并计算 $\rho_f$ 在基向量 $e_1$ 上的像，有

            \[
                \rho_f e_1 = \sum_{t \in G} f(t) \rho_t e_1 = \sum_{t \in G} f(t) e_t = 0.
            \]

            因为 $(e_i)$ 为表示空间的一组基，所以 $f(t) = 0, \forall t \in G$，即 $f = 0$.


    - $G$ 的不可约表示的数量（同构意义下）等于 $G$ 的共轭类数量.

        ???+ note "Proof"
            设 $C_1, \ldots, C_k$ 为 $G$ 的互异共轭类. $f$ 是 $G$ 上的类函数，即 $f$ 分别在 $C_i$ 为常数，所以 $f$ 是由 $C_i$ 上的取值 $\lambda_i$ 决定的. 因而，$H$ 的维度为 $k$，也就等于不可约表示的数量.

!!! note "Proposition"
    设 $s \in G$，$c(s)$ 为 $s$ 所在的共轭类中的元素数量.

    - $\sum_{i = 1}^h \overline{\chi_i(s)} \chi_i(s) = g/c(s)$;

    - 对不与 $s$ 共轭的 $t \in G$，$\sum_{i = 1}^h \overline{\chi_i(s)} \chi_i(t) = 0$.

    ???+ note "Proof"
        设 $f_s$ 在 $s$ 所在的类上取值为 $1$，其余类上为 $0$. 因为其为类函数，所以可以用不可约特征标表示，即

        \[
            f_s = \sum_{i=1}^h \lambda_i \chi_i,
        \]

        系数 $\lambda_i$ 为 $f_s$ 与 $\chi_i$ 的数量积：

        \[
            \lambda_i = (f_s \mid \chi_i) = \frac{1}{g} \sum_{t \in G} f_s(t) \overline{\chi_i(s)} = \frac{c(s)}{g} \overline{\chi_i(s)}.
        \]

        所以对任意 $t \in G$，

        \[
            f_s(t) = \frac{c(s)}{g} \sum_{i = 1}^h \overline{\chi_i(s)} \chi_i(t).
        \]

        代入验证即可.

## Canonical decomposition of a representation

接下来考虑更粗略但可以唯一确定的分解. 设 $\chi_1, \ldots, \chi_h$ 为 $G$ 的不可约表示 $W_1, \ldots, W_h$ 的互异特征标，度分别为 $n_1, \ldots, n_h$. 设 $V = U_1 \oplus \cdots \oplus U_m$ 为 $V$ 的不可约分解，$V_i$ 为 $U_1, \ldots, U_m$ 中与 $W_i$ 同构的表示的直和，显然有

\[
    V = V_1 \oplus \cdots \oplus V_h.
\]

这被称为 $V$ 的典则分解.

!!! note "Theorem"
    1. 典则分解 $V = V_1 \oplus \cdots \oplus V_h$ 不依赖于最初选择的将 $V$ 分解为不可约表示的方式.

    2. 与该分解相关联的投影 $p_i: V \to V_i$ 满足

        \[
            p_i = \frac{n_i}{g} \sum_{t \in G} \overline{\chi_i(t)} \rho_t.
        \]

    ???+ note "Proof"
        只用证明第 2 条，因为 $p_i$ 决定了 $V_i$ 的结构.

        定义

        \[
            q_i = \frac{n_i}{g} \sum_{t \in G} \overline{\chi_i(t)} \rho_t.
        \]

        前面的命题表明，如果将 $q_i$ 限制到一个特征标为 $\chi_j$，度为 $n$ 的不可约表示 $W$ 上的话，其是一个位似，比率为

        \[
            \lambda = \frac{g}{n} \left(\frac{n_i}{g} \overline{\chi}_i \mid \overline{\chi} \right) = \frac{n_i}{n} \overline{(\chi_i \mid \chi)}.
        \]

        若 $\chi_i \neq \chi$ 其值为 $0$，否则为 $1$. 也就是说 $q_i$ 在一个同构于 $W_i$ 的不可约表示上为恒等映射，在其他的不可约表示上为 $0$，所以 $q_i$ 限制在 $V_i$ 上是恒等映射，而在 $V_j \neq V_i$ 上为 $0$. 如果将元素 $x$ 分解为分量 $x_i \in V_i$，那么有

        \[
            q_i(x) = q_i(x_1 + x_2 + \cdots + x_m) = q_i(x_1) + q_i(x_2) + \cdots + q_i(x_m) = x_i.
        \]

        所以 $q_i$ 是 $V$ 到 $V_i$ 的投影算子 $p_i$.

## Explicit decomposition of a representation

前面已经掌握了典则分解的方法，接下来就是考虑如何将 $V_i$ 分解为同构于 $W_i$ 的子表示的直和. 设 $W_i$ 相对于基 $(e_1, \ldots, e_n)$ 的矩阵形式为 $r_{\alpha \beta} (s)$，则 $\chi_i (s) = \sum_{\alpha} r_{\alpha \alpha} (s)$，且 $n = n_i = \dim W_i$. 定义 $p_{\alpha \beta}$ 为

\[
    p_{\alpha \beta} = \frac{n}{g} \sum_{t \in G} r_{\beta \alpha} (t^{-1}) \rho_t.
\]

!!! note "Proposition"
    1. 映射 $p_{\alpha \alpha}$ 是一个投影，在 $V_{j \neq i}$ 上为 $0$. 其像空间 $V_{i, \alpha}$ 包含着 $V_i$ 中，且 $V_i = \oplus_{\alpha} V_{i, \alpha}$，也就有 $p_i = \sum_{\alpha} p_{\alpha \alpha}$.

    2. 映射 $p_{\alpha \beta}$ 在 $V_{j \neq i}$ 上为 $0$，在 $V_{i, \gamma \neq \beta}$ 上也为 $0$. 它是一个 $V_{i, \beta}$ 到 $V_{i, \alpha}$ 的同构.

    3. 设 $0 \neq x_1 \in V_{i, 1}$，$x_\alpha = p_{\alpha 1}(x_1) \in V_{i, \alpha}$. $x_\alpha$ 线性无关并且生成了一个 $G$ 下不变的维数为 $n$ 的子空间 $W(x_1)$. 对每个 $s \in G$，有

        \[
            \rho_s(x_\alpha) = \sum_{\beta} r_{\beta \alpha} (s) x_\beta.
        \]

    4. 若 $(x_1^{(1)}, \ldots, x_1^{(m)})$ 是 $V_{i, 1}$ 的一组基，那么 $V_i$ 是子表示 $W(x_1^{(1)}), \ldots, W(x_1^{(m)})$ 的直和.

    ???+ note "Proof"
        对于 $W_i$，有

        \[
            p_{\alpha \beta} (e_\gamma) = \frac{n}{g} \sum_{t \in G} r_{\beta \alpha} (t^{-1}) \rho_t(e_\gamma) = \frac{n}{g} \sum_{\delta} \sum_{t \in G} r_{\beta \alpha} (t^{-1}) r_{\delta \gamma} e_\delta.
        \]

        依据 Schur's Lemma 的第 2 个矩阵元推论，有

        \[
            p_{\alpha \beta} (e_\gamma) = \begin{cases} e_\alpha, \text{ if } \gamma = \beta \\ 0, \text{ otherwise.} \end{cases}
        \]

        所以 $\sum_\alpha p_{\alpha \alpha}$ 是 $W_i$ 上的恒等映射，且

        \[
            p_{\alpha \beta} \circ p_{\gamma \delta} = \begin{cases} p_{\alpha \delta}, & \text{ if } \beta = \gamma \\ 0, & \text{ otherwise.} \end{cases}
        \]

        \begin{align*}
            \rho_s \circ p_{\alpha \gamma} & = \frac{n}{g} \sum_{t \in G} r_{\gamma \alpha} (t^{-1}) \rho_s \circ \rho_t \\
                                           & = \frac{n}{g} \sum_{u \in G} r_{\gamma \alpha} (u^{-1} s) \rho_u \\
                                           & = \frac{n}{g} \sum_{u \in G} \sum_\beta r_{\gamma \beta} (u^{-1}) r_{\beta \alpha} (s) \rho_u \\
                                           & = \sum_{\beta} r_{\beta \alpha} (s) p_{\gamma \beta}.
        \end{align*}

        而对于 $W_{j \neq i}$，应用 Schur's Lemma 的第 1 个矩阵元推论，就可以证明出所有 $p_{\alpha \beta}$ 的值为 $0$.

        此时 1 和 2 的结论证明完成，接下来证明 3. $x_\alpha$ 线性无关是显然的，且有

        \[
            \rho_s (x_\alpha) = \rho_s \circ p_{\alpha 1}(x_1) = \sum_{\beta} r_{\beta \alpha} (s) p_{\beta 1} (x_1) = \sum_{\beta} r_{\beta \alpha} (s) x_\beta.
        \]

        所以 $W(x_1)$ 在 $G$ 下不变，而且同构于 $W_i$，因为在 $W_i$ 上有

        \[
            \rho_s (e_\alpha) = \sum_{\beta} r_{\beta \alpha} (s) e_\beta.
        \]

        4 的结论结合 1 2 3 即可.