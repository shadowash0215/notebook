# Schur-Weyl duality

量子 Fourier 变换让我们能够利用有限群在群代数上的左作用和右作用的对称性，并用来揭示隐藏子群状态的结构. 量子信息问题中另一种常见的对称性是置换不变性，特别体现在具有同一个量子态的多个副本时. 置换对称性与另一种对称性密切相关，其对应于集体酉变换. **Schur-Weyl 对偶**（Schur-Weyl duality）展示了这些对称性如何相互关联，以及如何利用它们. 其可用于各种量子信息处理任务，包括谱测试、层析成像、态纯化、纠缠浓缩和量子数据压缩，在大多数情况下，这些是量子输入的任务. 虽然 Schur-Weyl 对偶在理论上可以应用于解决经典问题的量子算法，但已被证明至少在弱 Fourier-Schur 采样背景下对于隐藏子群问题无用.

## The Schur decomposition

Fourier 变换依据左乘和右乘作用将群代数进行分解：

\[
    \mathbb{C}G \overset{G \times G}{\cong} \bigoplus_{\sigma \in \hat{G}} \mathcal{V}_{\sigma} \otimes \mathcal{V}_{\sigma}^*,
\]

其中 $\mathcal{V}_{\sigma}$ 是 $G$ 的不可约表示 $\sigma$ 的表示空间. 现在我们考虑另一种利用对称性分解量子态空间的方法，具体来说，考虑 $d$ 维空间 $\mathbb{C}^d$ 的 $k$ 个副本，以及 $(\mathbb{C}^d)^{\otimes k}$ 上的两类变换：

1. 对称群 $S_k$ 在 $(\mathbb{C}^d)^{\otimes k}$ 上的表示 $P$，对于 $\pi \in S_k$ 置换副本：

    \[
        P(\pi) \ket{i_1, i_2, \ldots, i_k} = \ket{i_{\pi^{-1}(1)}, i_{\pi^{-1}(2)}, \ldots, i_{\pi^{-1}(k)}},
    \]

2. 酉群 $\mathrm{U}(d)$ 在 $(\mathbb{C}^d)^{\otimes k}$ 上的表示 $Q$，对于 $U \in \mathrm{U}(d)$ 集体作用于每个副本：

    \[
        Q(U) \ket{i_1, i_2, \ldots, i_k} = U \ket{i_1} \otimes U \ket{i_2} \otimes \cdots \otimes U \ket{i_k}.
    \]

这些作用都是对易的，因此以及 Schur 引理可知，$P$ 的不可约表示只能作用于 $Q$ 的表示空间的多重度空间上，反之亦然. 但 $S_k$ 和 $\mathrm{U}(d)$ 的不可约表示均只恰好出现一次，因此可以用相同的方式标记这两类不可约表示. 具体来说，有以下分解：

\[
    (\mathbb{C}^d)^{\otimes k} \overset{S_k \times \mathrm{U}(d)}{\cong} \bigoplus_{\lambda \vdash k} \mathcal{P}_\lambda \otimes \mathcal{Q}_\lambda^d,
\]

这里的 $\mathcal{P}_\lambda$ 是由 $\lambda$ 标记的 $S_k$ 的不可约表示空间，记号 $\lambda \vdash k$ 表示 $\lambda$ 是 $k$ 的一个划分：$\lambda = (\lambda_1, \lambda_2, \ldots)$，其中正整数 $\lambda_1 \geq \lambda_2 \geq \cdots$ 且 $\sum_j \lambda_j = k$. 利用 Young 图可以直观地表示这些划分，其在坐标 $\{(i, j): 1 \leq j \leq \lambda_i\}$ 处有方格. 对于每个 $\lambda \vdash k$，还存在一个 $\mathrm{U}(d)$ 的不可约表示空间 $\mathcal{Q}_\lambda^d$. 对称群和酉群（或更一般的一般线性群）的不可约表示之间的这种关系称为 **Schur-Weyl 对偶**（Schur-Weyl duality）.

对称群和酉群的不可约表示的细节较为复杂，因此不会在此显式构造它们，但有对应的维数公式. 对于 $\lambda \vdash k$，对称群不可约表示的维数是**标准 Young 表**（standard Young tableaux）的数量，即将数字 $1, 2, \ldots, k$ 填入 $\lambda$ 的 Young 图中，使得每行和每列均严格递增. 这个量由**钩子长度公式**（hook-length formula）给出，对于 Young 图中的每个方格 $(i, j)$，其钩子长度 $h_\lambda(i, j)$ 定义为该方格右侧和下方的方格数加 1（包括自身）. 于是有

\[
    \dim \mathcal{P}_\lambda = \frac{k!}{\prod_{(i, j) \in \lambda} h_\lambda(i, j)}.
\]

对应的酉群不可约表示的维数由类似的公式给出：

\[
    \dim \mathcal{Q}_\lambda^d = \dim \mathcal{P}_\lambda \frac{d^k}{k!} \prod_{(i, j) \in \lambda} \left(1 + \frac{j - i}{d}\right).
\]

实现从 $(\mathbb{C}^d)^{\otimes k}$ 的标准基到对称群和酉群不可约表示基的变换称为 **Schur 变换**（Schur transform）. 

## Weak Schur sampling

回忆在弱 Fourier 采样中，仅测量 Fourier 基下的不可约表示标签. 类似地，在 Schur-Weyl 对偶的背景下，可以考虑一个仅测量对称群和酉群不可约表示标签 $\lambda$ 的过程，称为 **弱 Schur 采样**（weak Schur sampling）. 为了计算弱 Schur 采样的分布，可以将给定的态投影到 $\lambda$-同型子空间 $\mathcal{P}_\lambda \otimes \mathcal{Q}_\lambda^d$ 上，并取所得态的迹. 投影算子可以写作：

\[
    \Pi_\lambda = \frac{\dim \mathcal{P}_\lambda}{k!} \sum_{\pi \in S_k} \chi_\lambda(\pi) P(\pi).
\]

对于某些应用，这种测量可能足以揭示关于给定态的所有可用信息. 弱 Schur 采样比一般的 Schur 采样更容易执行. 特别地，可以使用一种称为**广义相位估计**（generalized phase estimation）的技术来，电路如下所示：

\qcircuit
     & & & & \multigate{2}{F_{S_k}} & \qw & \rstick{\ket{\lambda}} \\
    \lstick{\frac{1}{\sqrt{k!}} \sum_{\pi \in S_k} \ket{\pi}} & \qw & \ctrl{2} & \qw & \ghost{F_{S_k}} & \qw \\
     & & & & \ghost{F_{S_k}} & \qw \\
    \lstick{\rho} & \qw & \gate{P(\pi)} & \qw & \qw & \qw

顶端寄存器的输入态是置换群上的均匀叠加态，也可以看作对平凡表示施加逆 Fourier 变换得到的态. 对底部的寄存器施加受控置换操作后，再对顶端寄存器施加 Fourier 变换，输出一个由 $S_k$ 的不可约表示 $\lambda$ 标记的态，以及该表示内的行列标签. 弱 Schur 采样的的输出仅仅是 $\lambda$ 的值，且对称群上的 Fourier 变换可以高效执行.

对于某些任务，弱 Schur 采样提供了关于给定态的所有可用信息. 假设目标是从一个未知态 $\rho$ 的 $k$ 个副本推断其谱的某个性质. 这个性质在态的基变换下是不变的，并且在 $k$ 个副本的置换下也是不变的，因此在对称群或酉群的表示空间内部不包含任何信息. 换句话说，从该态中能够获得的唯一信息就是弱 Schur 采样所提供的关于 $\lambda$ 的分布.

一个自然的任务是从态的 $k$ 个副本中确定 $\rho$ 的整个谱. 为了解答这个问题，需要测量 $\lambda \vdash k$ 并推断最可能的谱. 因为 $d$ 维密度矩阵的谱是一个在 $d$ 个结果上的概率分布，估计值应该具有形式 $(p_1, p_2, \ldots, p_d)$，且 $\sum_{i=1}^d p_i = 1$. 假设估计的 Young 图为 $\lambda = (\lambda_1, \lambda_2, \ldots, \lambda_d)$（Young 图的行数不能超过 $d$，否则 $\dim \mathcal{Q}_\lambda^d = 0$），那么关联一个概率分布的最自然方法是取 $p_i = \lambda_i / k$，即简单归一化. 而这个简单的“经验 Young 图”过程实际上是一个良好的估计，它在给定误差内估计谱所需的副本数量是接近最优的. 大部分与谱相关的性质都应该从执行弱 Schur 采样，并从得到的 Young 图中进行估计.

如果任务不仅仅依赖于态的谱，如态层析，那么在弱 Schur 采样之后信息依然保留在 $\lambda$-同型子空间内. Schur-Weyl 对偶仍然提供了有用的工具来理解最优过程的形成，但需要额外的考虑去理解.

## The swap test

最后简要讨论著名的**交换测试**（swap test），其是 Schur 变换的一个特例.

考虑拥有 $\mathbb{C}^d$ 的 $k = 2$ 个副本的情况. 在这种情况下，相关对称群 $S_2$ 的表示理论非常简单. $2$ 的划分只有两个：$\lambda = (2)$ 和 $\lambda = (1, 1)$，二者均对应于 $S_2$ 的一维表示. $\lambda = (2)$ 是平凡表示，而 $\lambda = (1, 1)$ 表示将两个项的交换操作映射为 $-1$. 使用 $S_2$ 的相应特征标，投影到对应 $\lambda$-同型子空间的投影算子为 $\Pi_{(2)} = \frac{1}{2}(I + S)$ 和 $\Pi_{(1,1)} = \frac{1}{2}(I - S)$，其中 $S$ 是交换算子. 相应的子空间是对称子空间：

\[
    \op{span}(\{\ket{a, a}: 1 \leq a \leq d\} \cup \{\ket{a, b} + \ket{b, a}: 1 \leq a < b \leq d\})
\]

以及反对称子空间：

\[
    \op{span}(\{\ket{a, b} - \ket{b, a}: 1 \leq a < b \leq d\}).
\]

容易检查和 $\dim \mathcal{Q}_\lambda^d$ 的公式一致性，后者给出 $\dim \mathcal{Q}_{(2)}^d = \frac{d(d+1)}{2}$ 和 $\dim \mathcal{Q}_{(1,1)}^d = \frac{d(d-1)}{2}$.

这种情况下，弱 Schur 采样可以通过以下电路实现：

\qcircuit
    \lstick{\ket{0}} & \qw & \gate{H} & \ctrl{1} & \gate{H} & \qw \\
     & \qw & \qw & \multigate{1}{S} & \qw & \qw \\
     & \qw & \qw & \ghost{S} & \qw & \qw

执行此电路后，顶部的量子比特若处于状态 $\ket{0}$，则表示 $\lambda = (2)$，处于状态 $\ket{1}$ 则表示 $\lambda = (1, 1)$. 如果测量顶部量子比特，那么底部两个寄存器的态将依据测量结果被投影到对称子空间或反对称子空间. 