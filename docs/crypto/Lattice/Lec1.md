# 基本概念

## 格

**格**(Lattice) 的直观感受是 $n$ 维空间中具有周期性的点的集合。其正式的定义如下：

!!! info "Definition"
    (i) 给定 $n$ 个线性无关向量 $b_1, b_2, \cdots, b_n \in \mathbb{R}^n$，由这些向量张成的所有整系数线性组合的集合称为格，即

    \[
        \mathcal{L}(b_1, b_2, \cdots, b_n) = \left\{ \sum_{i=1}^n a_i b_i \mid a_i \in \mathbb{Z} \right\}
    \]

    $b_1, b_2, \cdots, b_n$ 称为格的**基**. 如果我们定义 $B$ 为 $m \times n$ 的矩阵，其列向量为 $b_1, b_2, \cdots, b_n$，则由 $B$ 产生的格为

    \[
        \mathcal{L}(B) = \left\{ B \cdot X \mid X \in \mathbb{Z}^n \right\}
    \]

    称格的**秩**为 $n$，**维数**为 $m$. 如果 $m = n$，则称该格为**满格**. 在此后的部分，我们只考虑满格.

    (ii) 格 $\mathcal{L}(B)$ 中基向量的所有实系数线性组合所形成的集合称为这组基向量**张成**的空间，

    \[
        \operatorname{span}(\mathcal{L}(B)) = \operatorname{span}(B) = \left\{ B \cdot Y \mid Y \in \mathbb{R}^n \right\}
    \]

    (iii) 对于任意格基，定义 

    \[
        \mathcal{P}(B) = \left\{ B \cdot X \mid X \in \mathbb{R}^n, 0 \leqslant x_i < 1 \right\}
    \]

    为此格的**基础区域**(Fundamental Parallelepiped)，因为将其放置在所有格点处可以形成整个空间.

构建出一个格之后，我们通过线性代数的学习，很容易想到关于格的基的逆问题，即

!!! question
    如何判断给定的向量组是否是给定格的一组基？

事实上，我们有如下引理：

!!! success "Lemma"
    设 $\Lambda$ 为秩为 $n$ 的格，设 $b_1, b_2, \cdots, b_n \in \Lambda$ 为 $n$ 个线性无关的格向量，则 $b_1, b_2, \cdots, b_n$ 是 $\Lambda$ 的一组基当且仅当 $\mathcal{P}(b_1, b_2, \cdots, b_n) \cap \Lambda = \{ 0 \}$.

    ??? success "Proof"
        $(\Rightarrow)$ 假设 $b_1, b_2, \cdots, b_n$ 是 $\Lambda$ 的一组基，则 $\mathcal{L}(b_1, b_2, \cdots, b_n) = \Lambda$，$\mathcal{L}$ 都是由 $b_1, b_2, \cdots, b_n$ 整系数扩张形成的，而 $\mathcal{P}(b_1, b_2, \cdots, b_n) = \left\{ \sum_{i=1}^n a_i b_i \mid 0 \leqslant a_i < 1 \right\}$，因此 $\mathcal{P}(b_1, b_2, \cdots, b_n) \cap \Lambda = \{ 0 \}$.

        $(\Leftarrow)$ 假设 $\mathcal{P}(b_1, b_2, \cdots, b_n) \cap \Lambda = \{ 0 \}$，因为 $\Lambda$ 是秩为 $n$ 的格，$b_1, b_2, \cdots, b_n$ 是 $n$ 个线性无关的格向量，因此对于任意 $x \in \Lambda$，存在唯一的实向量 $\lambda = (\lambda_1, \lambda_2, \cdots, \lambda_n) \in \mathbb{R}^n$，使得 $x = \sum_{i=1}^n \lambda_i b_i$，令 $x' = \sum_{i=1}^n (\lambda_i - \lfloor \lambda_i \rfloor) b_i$，则 $x' \in \mathcal{P}(b_1, b_2, \cdots, b_n)$，且 $x - x' = \sum_{i=1}^n \lfloor \lambda_i \rfloor b_i \in \Lambda$，可以得到 $x' \in \Lambda$，因此 $x' = 0$，所以 $\lambda$ 实际上是整数向量，$x$ 也就是 $b_1, b_2, \cdots, b_n$ 的整系数线性组合，因此 $b_1, b_2, \cdots, b_n$ 是 $\Lambda$ 的一组基.

接下来的问题也是容易联想到的：

!!! question
    给定两组基，如何判断它们是否生成同一个格？

!!! info "Definition(Unimodular Matrix)"
    矩阵 $U \in \mathbb{Z}^{n \times n}$ 称为**幺模矩阵**，如果 $\det(U) = \pm 1$.

    !!! success "Lemma"
        1. 若 $U$ 是幺模矩阵，则 $U^{-1}$ 也是幺模矩阵.
        2. 两组基 $B_1, B_2 \in \mathbb{R}^{m \times n}$ 生成同一个格 $\Lambda$ 当且仅当存在幺模矩阵 $U \in \mathbb{Z}^{n \times n}$，使得 $B_2 = B_1 U$.
        3. 两组基生成同一个格 $\Lambda$ 当且仅当其中一组基的列向量可以由另一组基的列向量通过以下方式变换得到：

            a. $b_i \from b_i + k b_j$, $k \in \mathbb{Z}$

            b. $b_i \leftrightarrow b_j$
            
            c. $b_i \from -b_i$


        ??? success "Proof"
            1. 因为 $\det(U) = \pm 1$，所以 $U$ 可逆，且 $\det(U^{-1}) = \pm 1$，因此 $U^{-1}$ 也是幺模矩阵.

            2. $(\Rightarrow)$ 假设 $\mathcal{L}(B_1) = \mathcal{L}(B_2)$，则 $B_2$ 的列向量 $b_i \in \mathcal{L}(B_1)$，因此存在整数矩阵 $U \in \mathbb{Z}^{n \times n}$，使得 $B_2 = B_1 U$，同理存在整数矩阵 $V \in \mathbb{Z}^{n \times n}$，使得 $B_1 = B_2 V$，因此 $B_2 = B_1 U = B_2 V U$，所以

                \[
                    B_2^\mathrm{T} B_2 = (B_2 V U)^\mathrm{T} (B_2 V U) = (V U)^\mathrm{T} B_2^\mathrm{T} B_2 (V U)
                \]
            
                取行列式，得到 $\det(B_2^\mathrm{T} B_2) = \det((V U))^2 \det(B_2^\mathrm{T} B_2)$. 从而 $\det(V U) = \pm 1$，且 $U$ 和 $V$ 都是整数矩阵，因此 $\det(U) = \pm 1$，所以 $U$ 是幺模矩阵.

                ($\Leftarrow$) 假设存在幺模矩阵 $U \in \mathbb{Z}^{n \times n}$，使得 $B_2 = B_1 U$，则 $B_2$ 的列向量 $b_i \in \mathcal{L}(B_1)$，因此 $\mathcal{L}(B_2) \subseteq \mathcal{L}(B_1)$，同理存在幺模矩阵 $V \in \mathbb{Z}^{n \times n}$，使得 $B_1 = B_2 V$，因此 $\mathcal{L}(B_1) \subseteq \mathcal{L}(B_2)$，所以 $\mathcal{L}(B_1) = \mathcal{L}(B_2)$.

!!! info "Definition(Determinant of Lattice)"
    设 $\Lambda = \mathcal{L}(B)$ 为秩为 $n$ 的格，则 $\det(\Lambda)$ 定义为 $\mathcal{P}(B)$ 的体积，写作

    \[
        \det(\Lambda) = \sqrt{\det(B^\mathrm{T} B)}
    \]

    若 $\Lambda$ 是满格，则 $\det(\Lambda) = \lvert \det(B) \rvert$.

    这一定义是良定的，考虑 $\Lambda$ 的任意两个基 $B_1, B_2 \in \mathbb{R}^{m \times n}$，因为 $B_2 = B_1 U$，$U \in \mathbb{Z}^{n \times n}$ 是幺模矩阵，因此 

    \[
        \sqrt{\det(B_2^\mathrm{T} B_2)} = \sqrt{\det(U^\mathrm{T} B_1^\mathrm{T} B_1 U)} = \sqrt{\det(U)^2 \det(B_1^\mathrm{T} B_1)} = \sqrt{\det(B_1^\mathrm{T} B_1)}
    \]

## Gram-Schmidt 正交化

!!! info "Definition(Gram-Schmidt Orthogonalization)"
    给定 $n$ 个线性无关向量 $b_1, b_2, \cdots, b_n \in \mathbb{R}^m$，定义其 Gram-Schmidt 正交化为 $n$ 个正交向量 $b_1^*, b_2^*, \cdots, b_n^* \in \mathbb{R}^m$，其定义如下：

    \[
        b_i^* = b_i - \sum_{j=1}^{i-1} \mu_{i,j} b_j^*, \quad \mu_{i,j} = \frac{\langle b_i, b_j^* \rangle}{\langle b_j^*, b_j^* \rangle}.
    \]

## 逐次最小值

!!! info "Definition(Successive Minima)"
    设 $\Lambda$ 为秩为 $n$ 的格，对 $i \in \{1, 2, \cdots, n\}$，定义第 $i$ 个逐次最小值 $\lambda_i(\Lambda)$ 为

    \[
        \lambda_i(\Lambda) = \inf \{ r \mid \dim(\operatorname{span}(\Lambda \cap \mathbf(\overline{B})(0, r))) \geqslant i \}
    \]

    其中 $\mathbf(\overline{B})(0, r) = \{x \in \mathbb{R}^m \mid \lVert x \rVert \leqslant r \}$ 为以原点为中心，半径为 $r$ 的闭球.

!!! note "Theorem"
    设 $B$ 为秩为 $n$ 的格的一组基，$B^*$ 为其 Gram-Schmidt 正交化，则有

    \[
        \lambda_1(\mathcal{L}(B)) \geqslant \min_{i \in [n]} \lVert b_i^* \rVert > 0.
    \]

    ??? note "Proof"
        设 $x \in \mathbb{Z}^n$ 为任意非零整数向量，只需证明 $\lVert B x \rVert \geqslant \min_{i \in [n]} \lVert b_i^* \rVert$，设 $j = \max\{ i \mid x_i \neq 0 \}$，则

        \[
            \lvert \langle B x, b_j^* \rangle \rvert = \lvert \langle \sum_{i=1}^j x_i b_i, b_j^* \rangle \rvert = \lvert x_j \rvert \langle b_j^*, b_j^* \rangle = \lvert x_j \rvert \lVert b_j^* \rVert^2.
        \]

        而另一方面，依据 Cauchy-Schwarz 不等式，有 $\lvert \langle B x, b_j^* \rangle \rvert \leqslant \lVert B x \rVert \cdot \lVert b_j^* \rVert$，因此

        \[
            \lVert B x \rVert \geqslant \lvert x_j \rvert \lVert b_j^* \rVert \geqslant \lVert b_j^* \rVert \geqslant \min_{i \in [n]} \lVert b_i^* \rVert.
        \]

    !!! success "Corollary"
        设 $\Lambda$ 为秩为 $n$ 的格，则对于任意 $x, y \in \Lambda$，总存在 $\varepsilon > 0$，使得 $\lVert x - y \rVert \geqslant \varepsilon$.

    !!! success "Claim"
        格的逐次最小值总是可达的，即对于任意 $i \in [n]$，总存在 $v_i \in \Lambda$，使得 $\lVert v_i \rVert = \lambda_i(\Lambda)$.

### 逐次最小值的上界

!!! note "Theorem(Blichfeldt's Theorem)"
    对任意满格 $\Lambda \subseteq \mathbb{R}^n$ 和可测集 $S \subseteq \mathbb{R}^n$，如果 $\operatorname{vol}(S) > \det(\Lambda)$，则存在两个互不相同的点 $z_1, z_2 \in S$，使得 $z_1 - z_2 \in \Lambda$.

    ??? note "Proof"
        设 $B$ 是 $\Lambda$ 的一组基，当 $x$ 取遍 $\Lambda$ 中的格点时，$x + \mathcal{P}(B)$ 形成 $\mathbb{R}^n$ 的一个划分. 定义 $S_x = S \cap (x + \mathcal{P}(B))$，$S = \cup_{x \in \Lambda} S_x$，因而 $\operatorname{vol}(S) = \sum_{x \in \Lambda} \operatorname{vol}(S_x)$. 定义 $\widehat{S}_x = S_x - x$，那么 $\widehat{S}_x \subseteq \mathcal{P}(B)$，且 $\operatorname{vol}(\widehat{S}_x) = \operatorname{vol}(S_x)$. 从而得到

        \[
            \sum_{x \in \Lambda} \operatorname{vol}(\widehat{S}_x) = \sum_{x \in \Lambda} \operatorname{vol}(S_x) = \operatorname{vol}(S) > \det(\Lambda) = \operatorname{vol}(\mathcal{P}(B)).
        \]

        因此，必然存在 $x, y \in \Lambda$，$x \neq y$，使得 $\widehat{S}_x \cap \widehat{S}_y \neq \varnothing$，设 $z \in \widehat{S}_x \cap \widehat{S}_y$，则 $z + x \in S_x$，$z + y \in S_y$，因此 $z + x, z + y \in S$，且 $(z + x) - (z + y) = x - y \in \Lambda$.

!!! note "Theorem(Minkowski's Convex Body Theorem)"
    设 $\Lambda \subseteq \mathbb{R}^n$ 为满格，$S \subseteq \mathbb{R}^n$ 为凸集且关于原点对称，如果 $\operatorname{vol}(S) > 2^n \det(\Lambda)$，则 $S$ 中至少存在一个非零的格点.

    ??? note "Proof"
        定义 $\hat{S} = \frac{1}{2} S = \{x \mid 2x \in S\}$，则 $\operatorname{vol}(\hat{S}) = 2^{-n} \operatorname{vol}(S) > \det(\Lambda)$，根据 Blichfeldt 定理，存在 $z_1, z_2 \in \hat{S}$，$z_1 \neq z_2$，使得 $z_1 - z_2 \in \Lambda$，依据定义，$2z_1, 2z_2 \in S$，因为 $S$ 关于原点对称所以 $-2z_2 \in S$，同时 $S$ 还是一个凸集，因此 $z_1 - z_2 = \frac{1}{2} (2z_1 - 2z_2) \in S$，所以 $S$ 中至少存在一个非零的格点.

    !!! success "Claim"
        半径为 $r$ 的 $n$ 维球的体积满足 $\operatorname{vol}(\mathbf{B}(0, r)) \geqslant \left( \frac{2r}{\sqrt{n}} \right)^n$.

    !!! success "Corollary(Minkowski's First Theorem)"
        对任意秩为 $n$ 的满格 $\Lambda$，

        \[
            \lambda_1(\Lambda) \leqslant \sqrt{n} \det(\Lambda)^{1/n}.
        \]

        ??? success "Proof"
            依据定义，开球 $\mathbf{B}(0, \lambda_1(\Lambda))$ 中没有非零的格点，依据定理和命题可以得到

            \[
                \left( \frac{2 \lambda_1(\Lambda)}{\sqrt{n}} \right)^n \leqslant \operatorname{vol}(\mathbf{B}(0, \lambda_1(\Lambda))) \leqslant 2^n \det(\Lambda).
            \]

            重排后得到 $\lambda_1(\Lambda) \leqslant \sqrt{n} \det(\Lambda)^{1/n}$.

    !!! success "Corollary(Minkowski's Second Theorem)"
        对任意秩为 $n$ 的满格 $\Lambda$，有

        \[
            \left( \prod_{i=1}^n \lambda_i(\Lambda) \right)^{1/n} \leqslant \sqrt{n} \det(\Lambda)^{1/n}.
        \]

        ??? success "Proof"
            设 $x_1, \ldots, x_n \in \Lambda$ 为达到逐次最小值的线性无关向量，$\lVert x_i \rVert = \lambda_i(\Lambda)$，$x_1^*, \ldots, x_n^*$ 为其 Gram-Schmidt 正交化，考虑轴线为 $x_1^*, \ldots, x_n^*$，各半轴长为 $\lambda_1, \ldots, \lambda_n$ 的开超椭球

            \[
                T = \left\{ y \in \mathbb{R}^n \mid \sum_{i=1}^n \frac{\langle y, x_i^* \rangle^2}{\lambda_i \lVert x_i^* \rVert^2} < 1 \right\}.
            \]

            声称 $T$ 并不包含任意非零的格点. 选取任意非零格点 $y \in \Lambda$，$1 \leqslant k \leqslant n$ 为满足 $\lVert y \rVert \geqslant \lambda_k(\Lambda)$ 的最大整数. 必然有 $y \in \operatorname{span}(x_1, \ldots, x_k) = \operatorname{span}(x_1^*, \ldots, x_k^*)$，否则 $x_1, \ldots, x_k, y$ 是 $k+1$ 个线性无关的且长度小于 $\lambda_{k + 1}(\Lambda)$ 的格向量，矛盾. 

            此时有

            \[
                \sum_{i=1}^n \left (\frac{\langle y, x_i^* \rangle}{\lambda_i \lVert x_i^* \rVert} \right)^2 = \sum_{i=1}^k \left( \frac{\langle y, x_i^* \rangle}{\lambda_i \lVert x_i^* \rVert} \right)^2 \geqslant \frac{1}{\lambda_k^2} \sum_{i=1}^k \left( \frac{\langle y, x_i^* \rangle}{\lVert x_i^* \rVert} \right)^2 = \frac{\lVert y \rVert^2}{\lambda_k^2} \geqslant 1,
            \]

            因此 $y \notin T$.

            依据定理，其体积必然满足 $\operatorname{vol}(T) \leqslant 2^n \det(\Lambda)$，而另一方面，

            \[
                \operatorname{vol}(T) = \left( \prod_{i=1}^n \lambda_i \right) \operatorname{vol}(\mathbf{B}(0, 1)) \geqslant \left( \prod_{i=1}^n \lambda_i \right) \left( \frac{2}{\sqrt{n}} \right)^n.
            \]

            二者结合便可得到

            \[
                \left( \prod_{i=1}^n \lambda_i(\Lambda) \right)^{1/n} \leqslant \sqrt{n} \det(\Lambda)^{1/n}.
            \]

## 计算难题

$\mathsf{SVP}$ (Shortest Vector Problem)：

- Search $\mathsf{SVP}$: 给定格基 $B \in \mathbb{Z}^{m \times n}$，寻找 $v \in \mathcal{L}(B)$，使得 $\lVert v \rVert = \lambda_1(\mathcal{L}(B))$.

- Optimization $\mathsf{SVP}$: 给定格基 $B \in \mathbb{Z}^{m \times n}$，寻找 $\lambda_1(\mathcal{L}(B))$.

- Decision $\mathsf{SVP}$: 给定格基 $B \in \mathbb{Z}^{m \times n}$ 和有理数 $r \in \mathbb{Q}$，判断是否 $\lambda_1(\mathcal{L}(B)) \leqslant r$. 

$\mathsf{SVP}_\gamma$ (Approximate Shortest Vector Problem)：

- Search $\mathsf{SVP}_\gamma$: 给定格基 $B \in \mathbb{Z}^{m \times n}$，寻找 $v \in \mathcal{L}(B)$，使得 $\lVert v \rVert \leqslant \gamma \cdot \lambda_1(\mathcal{L}(B))$.

- Optimization $\mathsf{SVP}_\gamma$: 给定格基 $B \in \mathbb{Z}^{m \times n}$，寻找实数 $d$ 使得 $d \leqslant \lambda_1(\mathcal{L}(B)) \leqslant \gamma \cdot d$.

- Promise $\mathsf{SVP}_\gamma$: 给定格基 $B \in \mathbb{Z}^{m \times n}$ 和有理数 $r \in \mathbb{Q}$，“是”实例下要求 $\lambda_1(\mathcal{L}(B)) \leqslant r$，“否”实例下要求 $\lambda_1(\mathcal{L}(B)) > \gamma \cdot r$.

$\mathsf{CVP}_\gamma$ (Approximate Closest Vector Problem)：

- Search $\mathsf{CVP}_\gamma$: 给定格基 $B \in \mathbb{Z}^{m \times n}$ 和目标向量 $t \in \mathbb{R}^m$，寻找 $v \in \mathcal{L}(B)$，使得 $\lVert v - t \rVert \leqslant \gamma \cdot d(t, \mathcal{L}(B))$.

- Optimization $\mathsf{CVP}_\gamma$: 给定格基 $B \in \mathbb{Z}^{m \times n}$ 和目标向量 $t \in \mathbb{R}^m$，寻找实数 $d$ 使得 $d(t, \mathcal{L}(B)) \leqslant d \leqslant \gamma \cdot d(t, \mathcal{L}(B))$.

- Promise $\mathsf{CVP}_\gamma$: 给定格基 $B \in \mathbb{Z}^{m \times n}$、目标向量 $t \in \mathbb{R}^m$ 和有理数 $r \in \mathbb{Q}$，“是”实例下要求 $d(t, \mathcal{L}(B)) \leqslant r$，“否”实例下要求 $d(t, \mathcal{L}(B)) > \gamma \cdot r$.

部分简单的计算问题：

- Membership: 给定格基 $B \in \mathbb{Z}^{m \times n}$ 和向量 $v \in \mathbb{R}^m$，判断 $v \in \mathcal{L}(B)$. 方程 $Bx = v$ 可以看作 $n$ 元 $m$ 个线性方程组，运用 Gaussian elimination 可以高效解决. 如果解存在并且属于 $\mathbb{Z}^n$，则输出“是”；否则输出“否”.

- Equivalence: 给定两组格基 $B_1, B_2 \in \mathbb{Z}^{m \times n}$，判断 $\mathcal{L}(B_1) = \mathcal{L}(B_2)$. 检查 $B_1$ 的列向量是否包含在 $\mathcal{L}(B_2)$ 中，且 $B_2$ 的列向量是否包含在 $\mathcal{L}(B_1)$ 中 即可.