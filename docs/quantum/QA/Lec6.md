# The abelian $\op{HSP}$ and decomposing abelian groups

## The abelian $\op{HSP}$

阿贝尔群通常使用加法记号，所以隐藏条件写作 $f(x) = f(y) \iff x - y \in H$.

解决策略和离散对数算法很相近，首先从群上的均匀叠加态开始，然后计算函数：

\[
    \ket{G} := \frac{1}{\sqrt{\lvert G \rvert}} \sum_{x \in G} \ket{x} \mapsto \frac{1}{\sqrt{\lvert G \rvert}} \sum_{x \in G} \ket{x, f(x)}.
\]

丢弃第二个寄存器以获得 $H$ 在 $G$ 上的某个随机选择的陪集 $x + H := \{x + h \mid h \in H\}$ 的均匀叠加态：

\[
    \ket{x + H} := \frac{1}{\sqrt{\lvert H \rvert}} \sum_{h \in H} \ket{x + h},
\]

该状态被称为**陪集态**（coset state）. 因为陪集是未知且均匀随机的，所以丢弃后的状态可以用密度算子表示为

\[
    \rho_H := \frac{1}{\lvert G \rvert} \sum_{x \in G} \ket{x + H}\bra{x + H}.
\]

对陪集态施加 $\op{QFT}$，有

\begin{align*}
    \ket{\widehat{x + H}} &:= F_G \ket{x + H} \\
                          &= \frac{1}{\sqrt{\lvert H \rvert \cdot \lvert G \rvert}} \sum_{y \in \hat{G}} \sum_{h \in H} \chi_y(x + h) \ket{y} \\
                          &= \sqrt{\frac{\lvert H \rvert}{\lvert G \rvert}} \sum_{y \in \hat{G}} \chi_y(x) \chi_y(H) \ket{y},
\end{align*}

其中

\[
    \chi_y(H) := \frac{1}{\lvert H \rvert} \sum_{h \in H} \chi_y(h).
\]

接下来证明 $\rho_H$ 是 $G$-不变的，它与 $G$ 的正则表示对易，即对于满足 $U(x)\ket{y} = \ket{x + y}$ 的酉矩阵 $U(x)$，有

\begin{align*}
    U(x) \rho_H &= \frac{1}{\lvert G \rvert} \sum_{y \in G} \ket{x + y + H}\bra{y + H} \\
                &= \frac{1}{\lvert G \rvert} \sum_{z \in G} \ket{z + H}\bra{z - x + H} \\
                &= \rho_H U(-x)^\dagger \\
                &= \rho_H U(x).
\end{align*}

所以 $\hat{\rho}_H := F_G \rho_H F_G^\dagger$ 是对角化的，因而可以无损测量.

再考虑将 $\chi_y$ 限制到子群 $H$ 上. 显然若 $\chi_y(h) = 1, \forall h \in H$，则 $\chi_y(H) = 1$. 否则，$\chi_y$ 在 $H$ 上是非平凡的，即存在 $h' \in H$ 使得 $\chi_y(h') \neq 1$. 而 $h' + H = H$，所以

\begin{align*}
    \chi_y(H) &= \frac{1}{\lvert H \rvert} \sum_{h \in h' + H} \chi_y(h) \\
              &= \frac{1}{\lvert H \rvert} \sum_{h \in H} \chi_y(h' + h) \\
              &= \chi_y(h') \chi_y(H),
\end{align*}

也就是说 $\chi_y(H) = 0$. 这也能从 $H$ 的特征标正交性关系

\[
    \frac{1}{\lvert H \rvert} \sum_{x \in H} \chi_y(x) \chi_{y'}(x)^* = \delta_{y, y'}
\]

得到，选取 $y'$ 为平凡特征标即可. 所以有

\[
    \ket{\widehat{x + H}} = \sqrt{\frac{\lvert H \rvert}{\lvert G \rvert}} \sum_{y: \chi_y(H) = 1} \chi_y(x) \ket{y},
\]

以及混合态：

\[
    \hat{\rho}_H = \frac{\lvert H \rvert}{\lvert G \rvert^2} \sum_{x \in G} \sum_{y, y': \chi_y(H) = \chi_{y'}(H) = 1} \chi_y(x) \chi_{y'}(x)^* \ket{y}\bra{y'} = \frac{\lvert H \rvert}{\lvert G \rvert} \sum_{y: \chi_y(H) = 1} \ket{y}\bra{y}.
\]

在计算基下测量便会得到某个在隐藏子群 $H$ 上平凡的特征标 $\chi_y$，此时便可以将范围缩小，考虑满足 $\chi_y(g) = 1$ 的 $g \in G$，记为 $\chi_y$ 的核 $\ker \chi_y = \{g \in G : \chi_y(g) = 1\}$，显然其是 $G$ 的子群，且包含 $H$. 重复上述过程，并计算核的交集. 可以证明在多项式步后便会以高概率得到 $H$.

假设在计算过程中，核的交集为 $K \leq G$ 且 $K \neq H$. 因为 $H < K$，根据 Lagrange 定理，必然有 $\lvert K \rvert \geq 2 \lvert H \rvert$. 因为 $G$ 的特征 $\chi_y$ 满足 $\chi_y(H) = 1$ 的概率为 $\lvert H \rvert / \lvert G \rvert$，而满足 $K \leq \ker \chi_y$ 的概率为 

\[
    \frac{\lvert H \rvert}{\lvert G \rvert} \cdot \lvert \{y \in \hat{G} : K \leq \ker \chi_y\} \rvert.
\]

而满足这样条件的 $y$ 的个数为 $\lvert G \rvert / \lvert K \rvert$，因为假如 $K$ 是被隐藏的子群，那么得到这些 $y$ 的概率为 $\lvert K \rvert / \lvert G \rvert$. 因而得到一个满足 $K \leq \ker \chi_y$ 的 $y$ 的概率实际上为 $\lvert H \rvert / \lvert K \rvert \leq 1/2$. 若测量得到 $K \not \leq \ker \chi_y$，那么有 $\lvert K \cap \ker \chi_y \rvert \leq \lvert K \rvert / 2$. 也就是说每次测量都有至少 $1/2$ 的概率将 $K$ 的大小缩小至少一半，重复 $O(\log \lvert G \rvert)$ 次便能以高概率得到 $H$.

## Decomposing abelian groups

问题来到了如何在群 $G$ 上进行 $\op{QFT}$ 的计算. 如果有每个群元素的唯一编码，能够进行群运算，并且知道 $G$ 的生成集，便可以将 $G$ 分解为循环子群的直和：

\[
    G = \langle \gamma_1 \rangle \oplus \langle \gamma_2 \rangle \oplus \cdots \oplus \langle \gamma_t \rangle.
\]

首先把问题规约到 $p$-群的情形. 对给定的生成元 $g$，因为有高效的寻阶量子算法，所以可以得到其阶为 $r$；此外还存在高效的因数分解量子算法，所以 $r$ 可以写作 $r = st$，利用 Euclid 算法可以得到 $a, b$ 使得 $as + bt = 1$，所以 $asg + btg = g$，所以可以用生成元 $sg$ 和 $tg$ 来代替 $g$. 重复此过程，直到所有生成元的阶均为素数幂为止. 对于给定的素数 $p$，设 $G_p$ 为 $G$ 中所有阶为 $p$ 的元素所生成的子群，那么 $G = \bigoplus_p G_p$，所以只需要考虑 $G_p$ 的分解. 不失一般性，设 $G$ 的阶是 $p$ 的幂.

现在给定 $G$ 的生成集 $\{g_1, g_2, \ldots, g_d\}$，设 $q$ 是这些生成元阶的最大值，考虑群 $\mathbb{Z}_q^d$ 上的一个隐藏子群问题. 定义函数 $f: \mathbb{Z}_q^d \to G$ 为

\[
    f(x_1, x_2, \ldots, x_d) = \sum_{i=1}^d x_i g_i.
\]

所以 $f(x_1, x_2, \ldots, x_d) = f(y_1, y_2, \ldots, y_d)$ 当且仅当 $\sum_{i=1}^d (x_i - y_i) g_i = 0$，也就是 $f(x - y) = 0$. $f$ 的核

\[
    K := \{ x \in \mathbb{Z}_q^d : f(x) = 0 \}
\]

形成了 $G$ 的一个子群. 在其上利用隐藏子群问题解法便可以得到 $K$ 的一个生成集 $W = \{w_1, w_2, \ldots, w_m\}, w_i \in \mathbb{Z}_q^d$. 

显然 $f$ 是一个 $\mathbb{Z}_d^q$ 到 $G$ 的满同态，依据第一同构定理，有 $G \cong \mathbb{Z}_q^d / K$. 所以问题转化为分析商群 $\mathbb{Z}_q^d / K$ 的结构. 如果 $\mathbb{Z}_q^d / K = \langle u_1 + K \rangle \oplus \langle u_2 + K \rangle \oplus \cdots \oplus \langle u_t + K \rangle$，那么 $G = \langle f(u_1) \rangle \oplus \langle f(u_2) \rangle \oplus \cdots \oplus \langle f(u_t) \rangle$.

最后一个要素是实现商群直和分解的多项式时间经典算法，这就需要利用到线性代数的工具. 考虑 $x \in \mathbb{Z}_q^d$，那么 $x + K = K$ 当且仅当 $x \in \op{span}_{\mathbb{Z}_q} W$. 而推广到任意整数向量 $x \in \mathbb{Z}^d$ 上的话，$x + K = K$ 当且仅当 $x \in \op{span}_{\mathbb{Z}} (W \cup \{q e_i : 1 \leq i \leq d\})$，其中 $e_i$ 是标准基. 这样的 $x$ 便是冗余向量.

接下来要用到来自整数线性代数的 Smith 标准形（Smith normal form）. 给定一个整数矩阵 $M$，其 Smith 标准形为 $M = UDV^{-1}$，其中 $U, V$ 为幺模矩阵，$D = \op{diag}(1, \ldots, 1, d_1, \ldots, d_t, 0, \ldots, 0)$ 为整数对角矩阵，其正对角线元素满足 $d_1 \mid d_2 \mid \cdots \mid d_t$. Smith 标准形可以在多项式时间内计算出来.

此情形下，设 $M$ 的列向量为 $w_1, w_2, \ldots, w_m, q e_1, q e_2, \ldots, q e_d$，$M = U D V^{-1}$ 为 $M$ 的 Smith 标准形. 设 $u_1, \ldots, u_t$ 为 $U$ 对应 $D$ 中非平凡对角线元素的列向量. 断言 $\mathbb{Z}_q^d / K = \langle u_1 + K \rangle \oplus \langle u_2 + K \rangle \oplus \cdots \oplus \langle u_t + K \rangle$.

因为 $U$ 是可逆的，所以如果选取了 $U$ 所有列向量也依然是生成集，但 $D$ 中 $0$ 和 $1$ 对角元对应的 $U$ 的列向量是冗余的. 设 $u$ 是 $U$ 的第 $j$ 个列向量，若 $u + K = K$，那么 $u \in \op{span}_\mathbb{Z} {\op{cols}(M)}$. 而由于 $V$ 是幺模矩阵，所以有

\[
    \op{span}_\mathbb{Z} {\op{cols}(M)} = \op{span}_\mathbb{Z} {\op{cols}(MV)}.
\]

所以 $u + K = K$ 当且仅当 $u \in \op{span}_\mathbb{Z} {\op{cols}(MV)}$，即 $U^{-1} u = e_j \in \op{span}_\mathbb{Z} {\op{cols}(U^{-1} MV)} = \op{span}_\mathbb{Z} {\op{cols}(D)}$. 如果第 $j$ 个对角线元素为 $1$，那么显然 $e_j \in \op{span}_\mathbb{Z} {\op{cols}(D)}$，所以 $u + K = K$，对应的 $u$ 是冗余的. 

!!! tip "Remark"
    对角元为 $0$