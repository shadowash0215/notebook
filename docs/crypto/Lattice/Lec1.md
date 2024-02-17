# 基本概念

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