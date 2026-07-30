# LLL 算法

## 规约基

!!! note "Review(Gram-Schmidt Orthogonalization)"
    给定一个基 $B = \{b_1, b_2, \ldots, b_n\}$，其 Gram-Schmidt 正交化为 $\{b_1^*, b_2^*, \ldots, b_n^*\}$，其中

    \[
        b_i^* = b_i - \sum_{j=1}^{i-1} \mu_{i,j} b_j^*, \quad \mu_{i,j} = \frac{\langle b_i, b_j^* \rangle}{\langle b_j^*, b_j^* \rangle}.
    \]

!!! info "Definition($\delta$-LLL Reduced Basis)"
    $B = \{b_1, b_2, \ldots, b_n\}$ 是 $\mathbb{R}^n$ 中的一个基，若满足以下两个条件，则称 $B$ 是 $\delta$-LLL 规约基：

    1. $\forall 1 \leqslant i \leqslant n, j < i, \mu_{i,j} \leqslant \frac{1}{2}$.

    2. $\forall 1 \leqslant i < n, \delta \lVert b_i^* \rVert^2 \leqslant \lVert \mu_{i+1,i} b_i^* + b_{i+1}^* \rVert^2$.

    !!! tip "Remark"
        1. 总可以将一组基转换为规约基，这就是 LLL 算法所做的事情.

        2. 算法在 $\frac{1}{4} < \delta < 1$ 的范围内都能工作，通常取 $\delta = \frac{3}{4}$.

        3. 定义的第二条性质也可写作：

            \[
                \delta \lVert b_i^* \rVert^2 \leqslant \lVert \mu_{i+1,i} b_i^* + b_{i+1}^* \rVert^2 = \mu_{i+1,i}^2 \lVert b_i^* \rVert^2 + \lVert b_{i+1}^* \rVert^2.
            \]

            改写后得到

            \[
                \lVert b_{i+1}^* \rVert^2 \geqslant (\delta - \mu_{i+1,i}^2) \lVert b_i^* \rVert^2 \geqslant (\delta - \frac{1}{4}) \lVert b_i^* \rVert^2.
            \]

            所以第二条性质是指 $b_{i+1}^*$ 的长度并不非常小于 $b_i^*$ 的长度.

!!! success "Claim"
    设 $B = (b_1, b_2, \ldots, b_n)$ 是一个 $\delta$-LLL 规约基，则 $\lVert b_1 \rVert \leqslant \left( \frac{2}{\sqrt{4\delta - 1}} \right)^{n-1} \lambda_1(\mathcal{L}(B))$.

    对 $\delta = \frac{3}{4}$，即 $\lVert b_1 \rVert \leqslant 2^{(n-1)/2} \lambda_1(\mathcal{L}(B))$.

    这表明 $\delta$-LLL 规约基的第一个向量是相对短的，且可以用来近似最短向量问题.

    ??? success "Proof"
        因为对于任意基 $B = (b_1, b_2, \ldots, b_n)$，有 $\lambda_1(\mathcal{L}(B)) \geqslant \min_i \lVert b_i^* \rVert$，所以有

        \[
            \lVert b_n^* \rVert^2 \geqslant (\delta - \frac{1}{4}) \lVert b_{n-1}^* \rVert^2 \geqslant \cdots \geqslant (\delta - \frac{1}{4})^{n-1} \lVert b_1^* \rVert^2 = (\delta - \frac{1}{4})^{n-1} \lVert b_1 \rVert^2.
        \]

        因此对任意 $i \in [n]$，有

        \[
            \lVert b_1^* \rVert \leqslant (\delta - \frac{1}{4})^{-(n-1)/2} \lVert b_i^* \rVert \leqslant (\delta - \frac{1}{4})^{-(n-1)/2} \lVert b_i^* \rVert.
        \]

        从而

        \[
            \lVert b_1 \rVert \leqslant (\delta - \frac{1}{4})^{-(n-1)/2} \min_i \lVert b_i^* \rVert \leqslant (\delta - \frac{1}{4})^{-(n-1)/2} \lambda_1(\mathcal{L}(B)).
        \]

## LLL 算法

\algorithm
    \caption{LLL 算法}
    \KwIn{基 $B = (b_1, b_2, \ldots, b_n)$}
    \KwOut{$\mathcal{L}(B)$ 的 $\delta$-LLL 规约基}
    \KwResult{}
    $\text{开始} \quad \text{计算} b_1^*, b_2^*, \ldots, b_n^*$\;
    $\text{规约步骤}$\;
    $\enspace \text{for } i = 2 \text{ to } n \text{ do}$\;
    $\enspace \enspace \text{for } j = i-1 \text{ down to } 1 \text{ do}$\;
    $\enspace \enspace \enspace b_i \gets b_i - c_{i, j} b_j, \quad c_{i,j} = \lceil \langle b_i, b_j^* \rangle / \langle b_j^*, b_j^* \rangle \rfloor$\;
    $\enspace \text{交换步骤}$\;
    $\enspace \text{if } \exists i \text{ such that } \delta \lVert b_i^* \rVert^2 > \lVert \mu_{i+1,i} b_i^* + b_{i+1}^* \rVert^2 \text{ then}$\;
    $\enspace \enspace b_i \leftrightarrow b_{i+1}$\;
    $\enspace \enspace \text{回到开始}$\;

!!! success "Lemma(Correctness of LLL Algorithm)"
    LLL 算法总是终止，并且输出一个 $\delta$-LLL 规约基.

    ??? success "Proof"
        $\delta$-LLL 规约基的第二个条件在交换步骤中得以满足，并且在整个过程中只进行了 $b_i \from b_i + a b_j$ 形式的操作，这不会破坏作为基的条件.

        接下来证明在规约步骤后 $b_1, b_2, \ldots, b_n$ 满足 $\lvert \mu_{i,j} \rvert \leqslant \frac{1}{2}, \forall i > j$，从而满足 $\delta$-LLL 规约基的第一个条件.

        考虑 $i > j$，内层循环为 $j$、外层循环为 $i$ 的情况.

        \[
            \lvert \mu_{i,j} \rvert = \left\lvert \frac{ \langle b_i - c_{i,j} b_j, b_j^* \rangle }{\langle b_j^*, b_j^* \rangle} \right\rvert = \left\lvert \frac{ \langle b_i, b_j^* \rangle}{\langle b_j^*, b_j^* \rangle} - \left\lceil \frac{\langle b_i, b_j^* \rangle}{\langle b_j^*, b_j^* \rangle} \right\rfloor \cdot \frac{\langle b_j, b_j^* \rangle}{\langle b_j^*, b_j^* \rangle} \right\rvert = \left\lvert \frac{\langle b_i, b_j^* \rangle}{\langle b_j^*, b_j^* \rangle} - \left\lceil \frac{\langle b_i, b_j^* \rangle}{\langle b_j^*, b_j^* \rangle} \right\rfloor \right\rvert \leqslant \frac{1}{2}.
        \]

### 分析运行时间

首先分析迭代数，然后分析单个迭代运行时.

!!! success "Lemma"
    定义 $M := \max(n, \log (\max_i \lVert b_i \rVert))$，则 LLL 算法的迭代次数是 $M$ 的多项式.

    ???+ success "Proof"
        建立一个将格基映射到正整数的势函数.

        !!! info "Definition"
            设 $B = (b_1, b_2, \ldots, b_n)$ 是一个基，定义 $B$ 的势 $\mathcal{D}(B)$ 为

            \[
                \prod_{i=1}^{n} \lVert b_i^* \rVert^{n - i + 1} =  \prod_{i=1}^{n} \lVert b_1^* \rVert \lVert b_2^* \rVert \cdots \lVert b_i^* \rVert = \prod_{i=1}^{n} \mathcal{D}_{B, i}, 
            \]

            其中 $\mathcal{D}_{B, i} := \det \Lambda_i$，$\Lambda_i$ 是由 $b_1, b_2, \ldots, b_i$ 生成的格.

        目标是证明 $\mathcal{D}(B)$ 的初值不大，并且能很快的衰减. 因为 $\lVert b_i^* \rVert \leqslant \lVert b_i \rVert$，所以 $\mathcal{D}(B) \leqslant (\max_i \lVert b_i \rVert)^{n(n+1)/2}$，后者取对数后是关于 $M$ 的多项式.

        在规约步骤中 $\mathcal{D}(B)$ 不变，因为 Gram-Schmidt 基并未改变. 在交换步骤中，假设 $b_i$ 和 $b_{i+1}$ 被交换，对于任意 $k \neq i$，$\Lambda_k$ 不变，所以 $\mathcal{D}_{B, k}$ 也不变. 只有 $\mathcal{D}_{B, i}$ 变化，设 $\Lambda_i', \mathcal{D}_{B, i}'$ 分别为交换后的格和势.

        \begin{align*}
            \frac{\mathcal{D}_{B, i}'}{\mathcal{D}_{B, i}} &= \frac{\det \Lambda_i'}{\det \Lambda_i} \\
            &= \frac{\det \mathcal{L}(b_1, b_2, \ldots, b_{i-1}, b_{i+1})}{\det \mathcal{L}(b_1, b_2, \ldots, b_i)} \\
            &= \frac{\prod_{j=1}^{i-1} \lVert b_j^* \rVert \cdot \lVert \mu_{i+1,i} b_i^* + b_{i+1}^* \rVert}{\prod_{j=1}^i \lVert b_j^* \rVert} \\
            &= \frac{\lVert \mu_{i+1,i} b_i^* + b_{i+1}^* \rVert}{\lVert b_i^* \rVert} < \sqrt{\delta}.
        \end{align*}

        最后一个小于号来自于交换步骤的条件. 

        所以每次迭代，$\mathcal{D}(B)$ 都会减少一个乘法因子 $\sqrt{\delta}$. 设 $\mathcal{D}_{B, 0}$ 为初始势，$\mathcal{D}_B$ 为非零整数，至少为 $1$，所以可以按如下方式约束迭代次数

        \[
            \log_{\frac{1}{\sqrt{\delta}}} \mathcal{D}_{B, 0} = \frac{\log \mathcal{D}_{B, 0}}{\log \frac{1}{\sqrt{\delta}}} \leqslant \frac{1}{\log \frac{1}{\sqrt{\delta}}} \cdot \frac{n(n+1)}{2} \log (\max_i \lVert b_i \rVert).
        \]

        对于任意 $\delta < 1$，这都是关于 $M$ 的多项式. 

!!! success "Lemma"
    单次迭代的运行时间是 $M$ 的多项式.

    ???+ success "Proof"
        在每一次迭代中只执行了多项式次的算术运算，因此只需要证明在每次迭代中出现的数值其比特长度也是 $M$ 的多项式. 

        !!! tip "为什么要说明数值的比特长度是 $M$ 的多项式？"
            考虑重复平方法，该算法给定数 $x$，并对其连续进行 $n$ 次平方. 虽然该算法只执行了 $n$ 次算术运算，但表示结果所需的比特数会膨胀到 $2^{O(n)}$，所以该算法的运行时间对于 $n$ 是指数级的.

        接下来会采用两个命题来确定单次迭代中出现数值的上界. 第一个命题关注 Gram-Schmidt 正交化向量，第二个命题则关注格基向量.

        !!! success "Claim"
            Gram-Schmidt 正交化向量 $b_1^*, b_2^*, \ldots, b_n^*$ 可以在 $M$ 的多项式时间内计算得到. 此外，对每个 $1 \leqslant i \leqslant n$，都有 $\mathcal{D}_B^2 b_i^* \in \mathbb{Z}^n$，且 $\lVert b_i^* \rVert \leqslant \mathcal{D}_B^2$.

            ??? success "Proof"
                因为 $b_i^* - b_i \in \operatorname{span}(b_1, b_2, \ldots, b_{i-1})$，所以可以将 $b_i^*$ 写作 $b_i^* = b_i + \sum_{j=1}^{i-1} a_j b_j$，其中 $a_j \in \mathbb{R}$. 希望寻找使得 $b_i^*$ 正交于 $b_1, b_2, \ldots, b_{i-1}$ 的系数 $a_j$，即对于任意 $1 \leqslant l \leqslant i-1$，有 $\langle b_i^*, b_l \rangle = 0$，从而有

                \[
                    \langle b_i^*, b_l \rangle = \langle b_i + \sum_{j=1}^{i-1} a_j b_j, b_l \rangle = \langle b_i, b_l \rangle + a_1 \langle b_1, b_l \rangle + a_2 \langle b_2, b_l \rangle + \cdots + a_{i-1} \langle b_{i-1}, b_l \rangle = 0.
                \]

                得到 $i-1$ 元的 $i-1$ 线性方程组，

                \begin{gather*}
                    a_1 \langle b_1, b_1 \rangle + a_2 \langle b_2, b_1 \rangle + \cdots + a_{i-1} \langle b_{i-1}, b_1 \rangle = -\langle b_i, b_1 \rangle, \\
                    a_1 \langle b_1, b_2 \rangle + a_2 \langle b_2, b_2 \rangle + \cdots + a_{i-1} \langle b_{i-1}, b_2 \rangle = -\langle b_i, b_2 \rangle, \\
                    \vdots \\
                    a_1 \langle b_1, b_{i-1} \rangle + a_2 \langle b_2, b_{i-1} \rangle + \cdots + a_{i-1} \langle b_{i-1}, b_{i-1} \rangle = -\langle b_i, b_{i-1} \rangle.
                \end{gather*}

                这个线性方程组是多项式时间内可解的.

                对于命题的第二部分，运用 Cramer's rule，得到 $a_j = \frac{\det A_j}{\det A}$，其中 

                \[
                    A = \begin{pmatrix}
                        \langle b_1, b_1 \rangle & \cdots & \langle b_{i-1}, b_1 \rangle \\
                        \vdots & \ddots & \vdots \\
                        \langle b_1, b_{i-1} \rangle & \cdots & \langle b_{i-1}, b_{i-1} \rangle
                    \end{pmatrix} = B_{i-1}^T B_{i-1}, 
                \]

                $A_j$ 则是将 $A$ 的第 $j$ 列替换为 $(-\langle b_i, b_1 \rangle, -\langle b_i, b_2 \rangle, \ldots, -\langle b_i, b_{i-1} \rangle)^T$ 得到的矩阵. 对于任意的 $1 \leqslant j \leqslant i-1$，$A_j$ 都是整数矩阵，所以 $\det A_j = z_j \in \mathbb{Z}$，且 $\det A = \det(B_{i-1}^T B_{i-1}) = (\det \Lambda_{i-1})^2$. 因而 $a_j = \frac{z_j}{\det \Lambda_{i-1}^2}$，$b_i^* = b_i + \sum_{j=1}^{i-1} a_j b_j$ 中的 $a_j$ 均是有理数，且分母都是 $\det \Lambda_{i-1}^2$. 这便表明 $\mathcal{D}_{B, i}^2 b_i^*$ 以及 $\mathcal{D}_B^2 b_i^*$ 都是整数向量.

                接下来证明 $b_i^*$ 的范数并不大. 依据势函数定义

                \[
                    \mathcal{D}_{B, i} = (\prod_{j=1}^{i - 1} \lVert b_j^* \rVert) \cdot \lVert b_i^* \rVert,
                \]

                因而

                \[
                    \lVert b_i^* \rVert = \frac{\mathcal{D}_{B, i}}{\prod_{j=1}^{i - 1} \lVert b_j^* \rVert} \leqslant \mathcal{D}_{B, i} \prod_{j = 1}^{i - 1} \mathcal{D}_{B, j}^2 \leqslant \mathcal{D}_B^2.
                \]

                第一个不等式是因为 $\lvert b_j^* \rVert \geqslant \frac{1}{\mathcal{D}_{B, j}}^2$.

        因为 $\lVert b_i^* \rVert \leqslant \mathcal{D}_B^2$，所以每个分量都不可能超过 $\mathcal{D}_B^2$；又因为 $\mathcal{D}_B^2 b_i^* \in \mathbb{Z}^n$，所以每个分量的分母不会超过 $\mathcal{D}_B^2$，因此每个分量的分母的比特数不会超过 $2 \log \mathcal{D}_B$. 再考虑每个分量的分子，分子不会超过 $\mathcal{D}_B^4$，所以每个分量的分子比特数不会超过 $4 \log \mathcal{D}_B$. 因此 Gram-Schmidt 正交化向量的表示是 $\operatorname{poly}(M)$ 的比特数.

        !!! success "Claim"
            所有在单个迭代过程中出现的格基向量 $b_i$ 都可以用 $\operatorname{poly}(M)$ 的比特数表示.

            ??? success "Proof"
                首先证明规约步骤之后，$b_i$ 的长度并不大. 对 $1 \leqslant i \leqslant n$，有

                \[
                    \lVert b_i \rVert^2 = \lVert b_i^* \rVert^2 + \sum_{j=1}^{i-1} \mu_{i,j}^2 \lVert b_j^* \rVert^2 \leqslant \mathcal{D}_B^4 + \frac{n}{4} \mathcal{D}_B^4 \leqslant n \mathcal{D}_B^4.
                \]

                因此每个分量的大小至多为 $\sqrt{n} \mathcal{D}_B^2$. 对于整数向量而言，这表明其可以用 $\log (\sqrt{n} \mathcal{D}_B^2)$ 的比特数表示，并且在规约步骤后 $b_i$ 仍然保持整数向量的形式. 

                最终证明在整个规约过程中，$b_i$ 依然是不太长的. 考虑 $b_i$ 在内层循环的变化. 首先对 $c_{i,j}$ 进行上界分析. 

                \[
                    \lvert c_{i,j} \rvert = \left\lvert \left\lceil \frac{\langle b_i, b_j^* \rangle}{\langle b_j^*, b_j^* \rangle} \right\rfloor \right\rvert \leqslant \frac{\lVert b_i \rVert \cdot \lVert b_j^* \rVert}{\lVert b_j^* \rVert^2} + 1 = \frac{\lVert b_i \rVert}{\lVert b_j^* \rVert} + 1 \leqslant \frac{\lVert b_i \rVert}{1/\mathcal{D}_B^2} + 1 \leqslant 2 \mathcal{D}_B^2 \lVert b_i \rVert.
                \]

                因此

                \begin{align*}
                    \lVert b_i - c_{i,j} b_j \rVert &\leqslant \lVert b_i \rVert + \lvert c_{i,j} \rvert \cdot \lVert b_j \rVert \\
                    &\leqslant (1 + 2 \mathcal{D}_B^2 \lVert b_j \rVert) \cdot \lVert b_i \rVert \\
                    &\leqslant (1 + 2 \mathcal{D}_B^2 \sqrt{n} \mathcal{D}_B^2) \cdot \lVert b_i \rVert \\
                    &\leqslant (4 n \mathcal{D}_B)^4 \cdot \lVert b_i \rVert.
                \end{align*}

                因为对 $j < i$，处理 $b_i$ 时，$b_j$ 已经被规约过了，所以对 $b_j$ 的约束是可使用的. $n$ 次迭代后，$b_i$ 的长度至多增长 $(4 n \mathcal{D}_B)^4$ 倍，依然是可以用 $\operatorname{poly}(M)$ 的比特数表示的.

        综合两个命题可以得到，单次迭代中出现的数值均可以用 $\operatorname{poly}(M)$ 的比特数表示，因此单次迭代的运行时间是 $M$ 的多项式.