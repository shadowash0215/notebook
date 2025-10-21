# Kuperberg's algorithm for the dihedral $\op{HSP}$

二面体群 $\op{HSP}$ 还没有已知的多项式时间量子算法，但 Kuperberg 提出了一个亚指数时间的量子算法，时间复杂度为 $2^{O(\sqrt{\log \lvert G \rvert})}$.

## The $\op{HSP}$ in the dihedral group

阶为 $2N$ 的二面体群 $D_N$ 包含的是对正 $N$ 边形的对称变换. 表示为

\[
    D_N = \langle r, s : r^2 = s^N = e, r s r = s^{-1} \rangle,
\]

$r$ 被视作关于固定轴的反射，而 $s$ 被视作将正 $N$ 边形旋转 $2\pi / N$ 的操作. 利用以上的定义关系，可以将所有群元素写作 $s^x r^a$，其中 $x \in \mathbb{Z}_N, a \in \mathbb{Z}_2$. 因此也可以等价地认为该群由群元素 $(x, a) \in \mathbb{Z}_N \times \mathbb{Z}_2$ 组成.

由于

\begin{align*}
    (s^x r^a)(s^y r^b) & = s^x r^a s^y (r^a r^a) r^b \\
                       & = s^x (r^a s^y r^a) r^{a + b} \\
                       & = s^{x + (-1)^a y} r^{a + b},
\end{align*}

所以这些元素上的群运算 $\cdot$ 可以定义为

\[
    (x, a) \cdot (y, b) = (x + (-1)^a y, a + b).
\]

实际上这也表明二面体群实际上是半直积 $\mathbb{Z}_N \rtimes_\varphi \mathbb{Z}_2$，其中 $\varphi : \mathbb{Z}_2 \to \op{Aut}(\mathbb{Z}_N)$ 定义为 $\varphi(a)(y) = (-1)^a y$. 也容易得到元素的逆为

\[
    (x, a)^{-1} = (-(-1)^a x, a).
\]

$D_N$ 的子群要么是循环群，要么是二面体群. 可能的循环子群形式为 $\langle (x, 0) \rangle$，其中 $x \in \mathbb{Z}_N$ 是 $0$ 或是 $N$ 的因子. 可能的二面体子群形式为 $\langle (y, 1) \rangle$，或 $\langle (x, 0), (y, 1) \rangle$，其中 $x$ 是 $N$ 的因子，$y \in \mathbb{Z}_x$. Ettinger 和 Høyer 的一个结果将一般的二面体群 $\op{HSP}$ 归约到了如下的一种情况：承诺隐藏子群形如 $\langle (y, 1) \rangle = \{ (0, 0), (y, 1) \}$，即由反射 $(y, 1)$ 生成的 $2$ 阶子群. 规约的基本思想如下：假设 $f: D_N \to S$ 隐藏了子群 $\langle (x, 0), (y, 1) \rangle$，那么便可以考虑将函数 $f$ 限制到阿贝尔子群 $\mathbb{Z}_N \times \{0\}$ 上. 该限制函数隐藏了循环子群 $\langle (x, 0) \rangle$，可以通过 Shor 算法高效求解. 因为 $\langle (x, 0) \rangle \triangleleft D_N$，所以可以定义商群 $D_N / \langle (x, 0) \rangle$，这是一个阶为 $2N/(N/x) = 2x$ 的二面体群. 如果定义 $f'$ 为 $f$ 在陪集代表元上的取值的话，那么 $f'$ 隐藏了子群 $\langle (y, 1) \rangle$. 所以在不失一般性的前提下，都假设隐藏子群具有形式 $\langle (y, 1) \rangle$.

## Fourier sampling in the dihedral group

当隐藏子群为 $H = \langle (y, 1) \rangle$ 时，$H$ 在 $G$ 中的左陪集代表元集合由 $\{ (z, 0) : z \in \mathbb{Z}_N \}$ 构成，对应于陪集 $(z, 0) H = \{ (z, 0), (y + z, 1) \}$ 的陪集态为

\[
    \ket{(z, 0) H} = \frac{1}{\sqrt{2}} \left( \ket{(z, 0)} + \ket{(y + z, 1)} \right).
\]

为了区分陪集态，通常从弱 Fourier 采样开始. 但在这个问题下，只对第一个寄存器在 $\mathbb{Z}_N$ 上执行 Fourier 变换，而保持第二个寄存器不变. 可以证明，测量结果态的第一个寄存器等价于在 $D_N$ 上执行弱 Fourier 采样并丢弃行寄存器，为了简化便只考虑阿贝尔过程.

对第一个寄存器执行 $\mathbb{Z}_N$ 上的 Fourier 变换，得到

\begin{align*}
    (F_{\mathbb{Z}_N} \otimes I_2) \ket{(z, 0) H} & = \frac{1}{\sqrt{2N}} \sum_{k \in \mathbb{Z}_N} (\omega_N^{k z} \ket{k, 0} + \omega_N^{k (y + z)} \ket{k, 1}) \\
                                                 & = \frac{1}{\sqrt{N}} \sum_{k \in \mathbb{Z}_N} \omega_N^{k z} \ket{k} \otimes \frac{1}{\sqrt{2}} (\ket{0} + \omega_N^{k y} \ket{1}),
\end{align*}

随后测量第一个寄存器，便会以均匀随机的方式得到 $k$ 的 $N$ 个值，并得到后测量态

\[
    \ket{\psi_k} := \frac{1}{\sqrt{2}} (\ket{0} + \omega_N^{k y} \ket{1}).
\]

所以问题又转变为了给定产生这种单量子比特态的能力，且 $k$ 已知，如何确定 $y$.

## Combining states

如果能够制备具有特定 $k$ 值的态 $\ket{\psi_k}$，那么可以通过测量来确定 $y$ 的一些信息. 如制备了 $\ket{\psi_{N/2}}$，那么就可以在 $\ket{\pm} := \frac{1}{\sqrt{2}} (\ket{0} \pm \ket{1})$ 基下测量来获得 $y \bmod 2$ 的值. Kuperberg's algorithm 的主要思想是组合形如 $\ket{\psi_k}$ 的态以产生具有相同形式，但是 $k$ 值更理想的新态. 为了组合态需要用到以下过程：给定两个态 $\ket{\psi_p}, \ket{\psi_q}$，利用前者对后者执行受控非门，得到

\begin{align*}
    \ket{\psi_p, \psi_q} & = \frac{1}{2} (\ket{0, 0} + \omega_N^{y p} \ket{1, 0} + \omega_N^{y q} \ket{0, 1} + \omega_N^{y (p + q)} \ket{1, 1}) \\
    & \mapsto \frac{1}{2} (\ket{0, 0} + \omega_N^{y p} \ket{1, 1} + \omega_N^{y q} \ket{0, 1} + \omega_N^{y (p + q)} \ket{1, 0}) \\
    & = \frac{1}{\sqrt{2}} (\ket{\psi_{p + q}, 0} + \omega_N^{y q} \ket{\psi_{p - q}, 1}).
\end{align*}

然后对第二个量子比特测量，将使第一个量子比特处于态 $\ket{\psi_{p \pm q}}$，$0$ 对应 $p + q$，$1$ 对应 $p - q$，且概率均为 $1/2$. 

这个组合操作有一个很好的表示论解释，态索引 $p$ 和 $q$ 可以被视为 $D_N$ 的不可约表示的标签，而提取 $\ket{\psi_{p \pm q}}$ 的过程对应于表示的张量积分解分解为两个不可约分量之一.

## The Kuperberg sieve

现在准备描述算法的工作原理. 简化起见假设 $N =2^n$. 对于这样的二面体群只需要确定 $y$ 的最低有效位即可，因为算法在此基础上便可以递归确定 $y$ 的所有位. 群 $D_N$ 包含两个同构于 $D_{N/2}$ 的子群，分别为 $\{ (2x, 0), (2x, 1) : x \in \mathbb{Z}_{N/2} \}$ 和 $\{ (2x, 0), (2x + 1, 1) : x \in \mathbb{Z}_{N/2} \}$. 当 $y$ 是偶数时，隐藏子群是前者的子群，否则是后者的子群. 而一旦知道 $y \bmod 2$，便可以将函数 $f$ 限制到相应的子群上，并递归地解决问题.

Kuperberg's algorithm 的想法是从大量态开始，并将他们收集成对 $\ket{\psi_p}, \ket{\psi_q}$，这些对共享许多最低有效位，因而也使得 $\ket{\psi_{p - q}}$ 的许多最低有效位很可能为零. 试图一次性清零除最高有效位外的所有位将需要指数运行时间，所以改为分阶段进行，每阶段只尝试清零部分最低有效位. 算法的步骤如下：

1. 制备 $\Theta(16^\sqrt{n})$ 个陪集态，其中每个副本的 $k \in \mathbb{Z}_N$ 是独立均匀随机选择的.

2. 对于每个阶段 $j = 0, 1, \ldots, m - 1$，其中 $m := \lceil \sqrt{n} \rceil$，假设当前的陪集态都形如 $\ket{\psi_k}$，且 $k$ 的至少 $mj$ 个最低有效位为零. 将接下来至少 $m$ 个最低有效位相同的态收集成对，并丢弃任何无法配对的态. 从每一对中创建态 $\ket{\psi_{p \pm q}}$，丢弃 $+$ 结果的态. 所以产生的态至少有 $m(j + 1)$ 个最低有效位为零.

3. 剩余的态都形如 $\ket{\psi_0}$ 和 $\ket{\psi_{2^{n - 1}}}$，在 $\ket{\pm}$ 基下测量后者以确定 $y$ 的最低有效位.

该算法需要 $2^{O(\sqrt{n})}$ 次初始查询，并经过 $O(\sqrt{n})$ 个阶段，每个阶段最多需要 $2^{O(\sqrt{n})}$ 次步，因此总运行时间为 $2^{O(\sqrt{n})}$.

## Analysis of the Kuperberg sieve

为了证明算法有效，需要证明在最后阶段，有一定数量的量子比特以不可忽略的概率存活下来.

假设在每个阶段清零 $m$ 个最低有效位，因此共有 $n/m$ 个阶段. 如果从 $2^\ell$ 个态开始，每个组合操作以 $1/2$ 的概率成功，并将 $2$ 个态转换为 $1$ 个，因此在每一步中只保留了 $1/4$ 的可配对态. 而清零 $m$ 个最低有效位时，至多有 $2^m$ 个态未匹配. 如果确保每个阶段至少有 $2 \cdot 2^m$ 个态，那么期望在下一个阶段保留至少 $1/8$ 的态. 从 $2^{\ell}$ 个态开始，经过 $n/m$ 个阶段后，期望保留的态数至少为 $2 \cdot 2^m$ 个，只要

\[
    2^{\ell - 3 n/m} \geq 2 \cdot 2^m,
\]

即 $l > m + 3 n/m + 1$. 取 $m \approx \sqrt{n}$ 可最小化该值，由此可见 $l \approx 4 \sqrt{n}$ 即可满足要求.

!!! tip "Remark"
    这是非常不精准的分析，$2 \cdot 2^m$ 和 $1/8$ 的出现让人困惑. 在大多数阶段中，都有远超过 $2 \cdot 2^m$ 个态存活下来，因此几乎所有态都能被配对，且保留比例接近于 $1/4$.

使用 Chernoff 界的更精确的分析表明该过程以高概率成功. 不过需要注意的是，该算法不仅需要超多项式的时间，还需要超多项式的空间来存储态. 后续 Regev 通过每次创建较少陪集态以及依据子集和问题的解的组合，设计了一个多项式空间的算法，并仅略微增加运行时间.

## Entangled measurements

尽管该算法每次只作用于一对陪集态，但产生 $\ket{\psi_{p \pm q}}$ 的组合操作会纠缠陪集态 $\ket{\psi_p}$ 和 $\ket{\psi_q}$，因此算法有效地实现了对所有 $\Theta(16^{\sqrt{n}})$ 个陪集态的纠缠测量. 

很自然地会想到类似的筛选方法是否可以应用于其他隐藏子群问题，如对称群. Alagic, Moore 和 Russell 使用类似地方法为群 $G^n$ 设计了一个亚指数时间的量子算法，其中 $G$ 是一个固定的非阿贝尔群. 但不幸的是，这种筛法不太适用于对称群. Moore, Russell 和 Sniad 对于 $S_m \wr \mathbb{Z}_2$ 中的 $\op{HSP}$ 给出了负面的结果. 任何通过组合成对的隐藏子群态并将张量积分解为不可约表示（即 Clebsch-Gordan 分解）以产生新状态，并使用测量结果序列来猜测隐藏子群是平凡还是非平凡的算法，都需要 $2^{\Omega(\sqrt{n})}$ 次查询，因此不可能通过此方法为图同构问题提供一个显著优于经典算法的量子算法，因为存在 $2^{O(\sqrt{n / \log n})}$ 时间的经典算法.

注意对于二面体群 $\op{HSP}$，纠缠测量在信息论上并不是必需的. Ettinger 和 Høyer给出了一种明确的测量，从该测量的结果中可以获得足够的信息来确定隐藏子群. 假设给定单量子比特态，直接在 $\ket{\pm}$ 基下测量获得 $\ket{+}$ 的概率为

\[
    \lvert \innerproduct{+}{\psi_k} \rvert^2 = \left\lvert \left( \frac{1}{\sqrt{2}} (\bra{0} + \bra{1}) \right) \left( \frac{1}{\sqrt{2}} (\ket{0} + \omega_N^{k y} \ket{1}) \right) \right\rvert^2 = \left\lvert \frac{1 + \omega_N^{k y}}{2} \right\rvert^2 = \cos^2 \frac{\pi k y}{N}.
\]

如果我们在获得这个结果的情况下进行后选择，那么实际上会以概率 $\op{Pr}(k \mid +) = \frac{2}{N} \cos^2 \frac{\pi k y}{N}$ 获得每个 $k \in \mathbb{Z}_N$. 不难证明，对于不同的 $k$ 值，这些分布在统计上相差很远，原则上只需要多项式数量的样本就可以区分它们. 但实际上，目前并不知道有任何高效的算法能做到这点.