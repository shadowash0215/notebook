# Quantum query complexity of the $\op{HSP}$

## The nonabelian $\op{HSP}$ and its applications

非阿贝尔群的隐藏子群问题不仅是阿贝尔群情况的推广，而且部分问题的解决有相当的实际意义. 最著名的应用是针对图自同构和图同构问题，这些问题目前还没有高效的经典算法. 

图自同构问题是对于给定的 $n$ 个顶点的图 $\Gamma$，确定是否存在非平凡的自同构映射 $\pi$，即是否存在非平凡置换 $\pi \in S_n$ 使得 $\pi(\Gamma) = \Gamma$. $\Gamma$ 的全体自同构构成一个群 $\op{Aut} \Gamma \leq S_n$，如果 $\op{Aut} \Gamma$ 是平凡的，那么称 $\Gamma$ 是**刚性**（rigid）的. 显然这可以通过函数 $f(\pi) = \pi(\Gamma)$ 来归约为 $S_n$ 上的 HSP，$f$ 隐藏的就是 $\op{Aut} \Gamma$. 

在介绍图同构问题前，先介绍**圈积**（wreath product）的概念.

!!! info "[Wreath product](https://en.wikipedia.org/wiki/Wreath_product)"
    设 $A$ 为一群，$H$ 是左作用在集合 $X$ 上的群. 群 $A$ 的直积 $A^X$ 中的元素为序列 $\bar{a} = (a_x)_{x \in X}$，由 $X$ 索引，运算为逐点乘法. $H$ 在 $X$ 上的作用可以通过重新索引扩展到 $A^X$ 上，即定义

    \[
        h \cdot (a_x)_{x \in X} = (a_{h^{-1} x})_{x \in X}.
    \]

    所以 $A$ 被 $H$ 在 $X$ 上的**无限制圈积**（unrestricted wreath product）$A \wr_X H$ 定义为半直积 $A^X \rtimes H$，$A^X$ 被称为该圈积的**底群**（base group）.

    **限制圈积**（restricted wreath product）$A \op{wr}_X H$ 定义与无限制圈积类似，但底群使用的是直和. 当 $X$ 是有限集时，两者相同.

    最常见的情况下，$X = H$，$H$ 通过左平移作用在自身上，称为**正规圈积**（restricted wreath product）.

图同构问题中，给出两个 $n$ 个顶点的图 $\Gamma, \Gamma'$，判断是否存在置换 $\pi \in S_n$ 使得 $\pi(\Gamma) = \Gamma'$，如果存在则称 $\Gamma$ 和 $\Gamma'$ 同构. 该问题可以归约为 $S_n \wr S_2 \leq S_{2n}$ 上的 $\op{HSP}$. 将 $S_n \wr S_2$ 上的元素记作 $(\pi, \tau, b)$，其中 $\pi, \tau \in S_n$，$b \in \{0,1\} 决定是否交换两个图. 定义函数

\[
    f(\pi, \tau, b) = \begin{cases}
        (\pi(\Gamma), \tau(\Gamma')) & b = 0 \\
        (\pi(\Gamma'), \tau(\Gamma)) & b = 1
    \end{cases}.
\]

这个函数隐藏的是 $\Gamma$ 和 $\Gamma'$ 不交并的自同构群，如果 $\Gamma$ 和 $\Gamma'$ 同构，那么隐藏子群中会有一个非平凡元素对应于交换两个图的置换. 考虑 $\Gamma$ 和 $\Gamma'$ 都是刚性的情况，如果它们不同构，那么隐藏子群就是平凡的；否则隐藏子群会包含一个满足 $\pi(\Gamma) = \Gamma'$ 的元素 $(\pi, \pi^{-1}, 1)$.

第二个潜在的应用是格问题. $n$ 维格 $\Lambda$ 是 $\mathbb{R}^n$ 中由 $n$ 个线性无关向量的所有整数线性组合构成的离散子群. 在**最短向量问题**（shortest vector problem, SVP）中，需要找到 $\Lambda$ 中的非零最短向量. 而 **$g(n)$-唯一最短向量问题**（$g(n)$-unique SVP）是 SVP 的一个变种，要求格 $\Lambda$ 满足：存在唯一的最短非零向量 $v$，并且比任何其他非平行向量都要短 $g(n)$ 倍. 如果 $g(n)$ 足够大，那么该问题可以用经典算法在多项式时间内解决；而如果 $g(n) = O(1)$，那么就是 $\mathrm{NP}$-难的. 对于中间情况知之甚少，但即使 $g(n) = \op{poly}(n)$，也被怀疑是经典计算机难以解决的. 而 Regev 证明，基于所谓的标准方法的用于解决二面体隐藏子群问题的高效量子算法，可以用来解决 $\op{poly}(n)$-唯一最短向量问题. 

理解一般群上 $\op{HSP}$ 的复杂性主要有以下三个原因：

1. 该问题似乎天然地提供了一个探索量子计算机相对于经典计算机的优势程度地场景；

2. 为其他 $\op{HSP}$ 开发的技术最终可能应用于对称群或二面体群；

3. 探索量子计算机解决 $\op{HSP}$ 的局限性有助于提出面对量子攻击也能保持安全的密码系统.

## The standard method

几乎所有已知的非阿贝尔隐藏子群问题算法都以与阿贝尔 $\op{HSP}$ 类似的方式使用黑盒函数 $f$，因此这种方法被称为**标准方法**（standard method）. 

标准方法中，首先制备群元素的均匀叠加态：

\[
    \ket{G} := \frac{1}{\sqrt{\lvert G \rvert}} \sum_{g \in G} \ket{g},
\]

然后在辅助寄存器中计算 $f$，得到状态：

\[
    \frac{1}{\sqrt{\lvert G \rvert}} \sum_{g \in G} \ket{g, f(g)}.
\]

最后丢弃辅助寄存器，如果结果是 $s \in S$，那么主寄存器的状态将投影到所有满足 $f(g) = s$ 的 $g \in G$ 的均匀叠加态上，而依据 $f$ 的定义，这些 $g$ 构成某个左陪集 $gH$，因此主寄存器的状态变为陪集态：

\[
    \ket{gH} := \frac{1}{\sqrt{\lvert H \rvert}} \sum_{h \in H} \ket{gh}.
\]

所以最终结果应该为混合态

\[
    \rho_H := \frac{1}{\lvert G \rvert} \sum_{g \in G} \ket{gH}\bra{gH},
\]

称为隐藏子群状态. 在标准方法中，会去使用隐藏子群的样本来确定 $H$. 换言之，在给定 $\rho_H^{\otimes k}$，其中 $k = \op{poly}(\log \lvert G \rvert)$ 的情况下，寻找 $H$ 的一个生成元集合.

## Query complexity of the $\op{HSP}$

理解 $\op{HSP}$ 量子计算复杂度的第一步是考虑对 $f$ 的查询复杂度，如果证明需要指数次查询才能确定 $H$，那么便不存在高效的量子算法来解决该问题. 但 Ettiner, Høyer 和 Knill 证明只需要 $\op{poly}(\log \lvert G \rvert)$ 次查询便能确定 $H$，他们也在标准方法的框架下证明了 $\rho_H^{\otimes \op{poly}(\log \lvert G \rvert)}$ 包含足够的信息来恢复 $H$. 但这并非意味着存在高效的量子算法来解决该问题，因为尚不清楚如何高效地执行隐藏子群态的量子后处理.

为了证明隐藏子群问题的查询复杂度是多项式的，只需证明单副本的隐藏子群态是两两统计可区分的，度量标准为量子保真度：

\[
    F(\rho_H, \rho_{H'}) = \op{Tr} \lvert \sqrt{\rho} \sqrt{\rho'} \rvert.
\]

因为 $\lvert A \rvert := \sqrt{A^\dagger A}$，所以这与 [Quantum-QCQI-Chap9](https://note.shad0wash.cc/quantum/QCQI/Chap9/#fidelity) 中的定义一致. 

这一结果来自 Barnum 和 Knill，他们证明了以下的定理：

!!! note "Theorem"
    设 $\rho$ 是从系综 $\{\rho_1, \ldots, \rho_N\}$ 中抽取的，每个 $\rho_i$ 的概率为固定的 $p_i$. 那么存在一个量子测量，能够以至少

    \[
        1 - N \sqrt{\max_{i \neq j} F(\rho_i, \rho_j)}
    \]

    的概率正确识别 $\rho$. 而实际上，依据极小极大定理，即使不假设系综的先验概率分布，这一结论依然成立.

给定隐藏子群态的一个副本，上式只能给出一个平凡界；但通过获取多个隐藏子群态的副本，便可以确保整体态之间是近似正交的，因而可区分. 特别地，如果使用 $\rho$ 的 $k$ 个副本，便存在一种测量能够以至少

\[
    1 - N \sqrt{\max_{i \neq j} F(\rho_i^{\otimes k}, \rho_j^{\otimes k})} = 1 - N \sqrt{\max_{i \neq j} F(\rho_i, \rho_j)^k}
\]

的概率正确识别 $\rho$.（保真度在张量积下是乘性的.）令该表达式为 $1 - \epsilon$，并求解 $k$，便得到只要使用

\[
    k \geq \left \lceil \frac{2 (\log N - \log \epsilon)}{\log (1 / \max_{i \neq j} F(\rho_i, \rho_j))} \right \rceil
\]

个 $\rho$ 的副本，就能实现任意小的错误概率 $\epsilon$. 

假设子群 $G$ 的数量不太多，并且不同隐藏子群态之间的保真度不是太接近 $1$，这便表明使用多项式数量的 $\rho_H$ 副本就足以解决 $\op{HSP}$. $G$ 的子群总数为 $2^{O(\log^2 \lvert G \rvert)}$，原因如下：任何群 $K$ 都可以用至多 $\log_2 \lvert K \rvert$ 个生成元指定，而因为任何冗余的生成元都会使得群大小至少增加一倍，所以 $G$ 的每个子群都可以由最多 $\log_2 \lvert G \rvert$ 个 $G$ 中的元素构成的子集指定，所以 $G$ 的子群总数的上界为 $\lvert G \rvert^{\log_2 \lvert G \rvert} = 2^{O(\log^2 \lvert G \rvert)}$. 进而取 $\log N = \op{poly}(\log \lvert G \rvert)$ 即可，那么只要最大保真度和 $1$ 的差距至少为 $1/\op{poly}(\log \lvert G \rvert)$，利用 $k = \op{poly}(\log \lvert G \rvert)$ 个隐藏子群态的副本便能以常数概率识别 $H$.

为了给出两个态 $\rho$ 和 $\rho'$ 之间保真度的上界，考虑投影到 $\rho$ 的支撑集或其正交补集上的二结果测量. 回忆量子保真度和经典保真度之间的关系：

\[
    F(\rho, \sigma) = \min_{\{E_m\}} F(\{p_m\}, \{q_m\}),
\]

其中最小化遍历所有 POVM 测量 $\{E_m\}$，$p_m = \op{Tr} E_m \rho$，$q_m = \op{Tr} E_m \sigma$. 因此：

\begin{align*}
    F(\rho, \rho') & \leq \sqrt{\op{Tr} \Pi_\rho \rho \op{Tr} \Pi_\rho \rho'} + \sqrt{\op{Tr} (1 - \Pi_\rho) \rho \op{Tr} ((1 - \Pi_\rho) \rho')} \\
    & = \sqrt{\op{Tr} \Pi_\rho \rho'}.
\end{align*}

现在考虑两个不同子群 $H, H' \leq G$ 对应的态 $\rho_H$ 和 $\rho_{H'}$ 之间的保真度. 不失一般性，假设 $\lvert H \rvert \geq \lvert H' \rvert$. 定义 $T_H$ 为 $H$ 在 $G$ 中的左陪集的一个代表元的集合，那么可以将 $\rho_H$ 重写为

\[
    \rho_H = \frac{1}{\lvert G \rvert} \sum_{g \in G} \ket{gH}\bra{gH} = \frac{\lvert H \rvert}{\lvert G \rvert} \sum_{g \in T_H} \ket{gH}\bra{gH}.
\]

又因为右侧实际上是 $\rho_H$ 的谱分解式，所以

\[
    \Pi_{\rho_H} = \sum_{g \in T_H} \ket{gH}\bra{gH} = \frac{1}{\lvert H \rvert} \sum_{g \in G} \ket{gH}\bra{gH}.
\]

进而有

\begin{align*}
    F(\rho_H, \rho_{H'})^2 & \leq \op{Tr} \Pi_{\rho_H} \rho_{H'} \\
                           & = \frac{1}{\lvert H \rvert \lvert G \rvert} \sum_{g, g' \in G} \lvert \innerproduct{gH}{g'H'} \rvert^2 \\
                           & = \frac{1}{\lvert H \rvert \lvert G \rvert} \sum_{g, g' \in G} \frac{\lvert gH \cap g'H' \rvert^2}{\lvert H \rvert \lvert H' \rvert} \\
                           & = \frac{1}{\lvert G \rvert \cdot \lvert H \rvert^2 \cdot \lvert H' \rvert} \sum_{g, g' \in G} \lvert gH \cap g'H' \rvert^2.
\end{align*}

而

\begin{align*}
    \lvert gH \cap g'H' \rvert & = \lvert \{（h, h'） \in H \times H' : gh = g'h' \} \rvert \\
                               & = \lvert \{（h, h'） \in H \times H' : hh' = g^{-1} g' \} \rvert \\
                               & = \begin{cases}
                                   \lvert H \cap H' \rvert & g^{-1} g' \in H H' \\
                                   0 & g^{-1} g' \notin H H'
                                 \end{cases}.
\end{align*}

所以

\begin{align*}
    \sum_{g, g' \in G} \lvert gH \cap g'H' \rvert^2 & = \lvert G \rvert \cdot \lvert H H' \rvert \cdot \lvert H \cap H' \rvert^2 \\
                                                    & = \lvert G \rvert \cdot \lvert H \rvert \cdot \lvert H' \rvert \cdot \lvert H \cap H' \rvert.
\end{align*}
    
最终有

\begin{align*}
    F(\rho_H, \rho_{H'})^2 & \leq \frac{\lvert G \rvert \cdot \lvert H \rvert \cdot \lvert H' \rvert \cdot \lvert H \cap H' \rvert}{\lvert G \rvert \cdot \lvert H \rvert^2 \cdot \lvert H' \rvert} \\
                           & = \frac{\lvert H \cap H' \rvert}{\lvert H \rvert} \\
                           & \leq \frac{1}{2},
\end{align*}

$F(\rho_H, \rho_{H'}) \leq 1/\sqrt{2}$，所以 $\op{HSP}$ 的查询复杂度是 $\op{poly}(\log \lvert G \rvert)$.