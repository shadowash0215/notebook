# Quantum-Secure Message Authentication Codes

## Preliminaries: Definitions and Notation

### Quantum secure MACs

MAC 系统包括两个算法：

- 随机化的 MAC 签名算法 $S(k, m)$；

- MAC 验证算法 $V(k ,m, t)$.

$k, m$ 是密钥和消息，而 $t$ 是消息 $m$ 上的 MAC 标签. 这些算法和空间是基于安全参数 $\lambda$ 的.

MAC 系统的安全性是选择明文攻击的不可伪造性. 敌手可以和签名 Oracle $S(k, \cdot)$ 交互，得到消息-标签对集合 $Q = \{(m_i, t_i)\}_{i = 1}^q$，胜利条件为成功伪造 $(m^*, t^*) \not\in Q$，使得 $V(k, m^*, t^*) = 1$. 如果不存在高效的敌手能够以不可忽略的概率成功伪造，则称 MAC 系统是安全的.

**量子选择明文查询（Quantum chosen message queries）** 量子设置下允许敌手保持自己的量子态，并且向签名 Oracle 发起量子查询. 设 $\sum_{m, x, y} \psi_{m, x, y} \ket{m, x, y}$ 是敌手发起量子查询前的量子态，MAC 签名 Oracle 按如下方式转换该量子态：

1. 随机选择一个字符串 $r$ 用于 MAC 签名；

2. 对给定叠加态中的每个基态运行 $S(k, m; r)$，即使用随机度 $r$ 生成 MAC 签名，具体进行的操作为：

\[
    \sum_{m, x, y} \psi_{m, x, y} \ket{m, x, y} \xrightarrow{S(k, m; r)} \sum_{m, x, y} \psi_{m, x, y} \ket{m, x \oplus S(k, m; r), y}.
\]

如果签名算法是确定的，便不需要随机度 $r$；但如果是随机化的，那就需要使用同一个随机度 $r$ 来给叠加态中的所有基态生成标签.（如果使用不同的随机度 $r$ 在量子设备上的实现难度会增加）. 事实上，使用相同和不同随机度的模型是十分接近的，也可以利用将 $r$ 用作 $\op{QPRF}$ 的密钥来生成不同的随机度.

**存在性伪造（Existential forgery）** 如果敌手在发起 $q$ 次量子查询后能够生成 $q + 1$ 个有效的经典的消息-标签对，那么称其获胜.

!!! info "Definition"
    如果没有敌手能够以不可忽略的概率赢得以上量子 MAC 博弈，则称该 MAC 系统是量子选择明文攻击下存在性不可伪造的（$\op{EUF-qCMA}$）.

## The Rank Method

秩方法是一种通用的用于证明量子算法下界的技术.

量子算法 $A$ 可以访问某个集合 $\mathcal{H}$ 中的元素 $H$，访问的含义是最终量子态是 $H$ 的某种函数. 本文中 $\mathcal{H}$ 是一个函数集合，$H \in \mathcal{H}$ 是其中的元素，算法 $A$ 可以对 $H$ 发起 $q$ 次量子 Oracle 查询. 不过先对 $\mathcal{H}$ 进行抽象的处理，然后再回到函数集合的情况.

秩方法的核心思想在于，如果将算法 $A$ 在不同 $H$ 输入下的终态视为向量，那么这些向量张成的空间就是整个 Hilbert 空间的一个子空间. 如果这个子空间的维度足够小，那么这个子空间以及其中的向量必然远离测量基中的大部分向量，进而限制此类算法达成某种目标的能力.

对 $H \in \mathcal{H}$，设 $\ket{\psi_H}$ 是算法 $A$ 访问 $H$ 后但是测量之前的量子态. 假定所有 $\ket{\psi_H}$ 都落在同一个 $d$ 维子空间中，定义 $\mathbf{\Psi_{A, \mathcal{H}}}$ 为一个 $\lvert \mathcal{H} \rvert \times d$ 矩阵，每一行对应不同 $H$ 的向量 $\ket{\psi_H}$.

!!! info "Definition"
    对于可访问某些 $H \in \mathcal{H}$ 的量子算法 $A$，定义其秩为矩阵 $\mathbf{\Psi_{A, \mathcal{H}}}$ 的秩，记作 $\op{rank}(A, \mathcal{H})$.

$A$ 的秩似乎只包含很少的信息，其给出了 $\ket{\psi_H}$ 张成的子空间的维度，但完全不涉及该子空间的方向或是 $\ket{\psi_H}$ 在子空间的具体位置. 即便如此，也可以证明仅通过秩就可以从理论上约束算法 $A$ 的成功概率.

!!! note "Theorem"
    设 $A$ 是一个可以访问某些依据分布 $D$ 抽取的 $H \in \mathcal{H}$ 的量子算法，并且产生输出 $w \in \mathcal{W}$. 设 $R: \mathcal{H} \times \mathcal{W} \to \{\mathsf{True}, \mathsf{False}\}$ 为一个二元关系，那么 $A$ 输出某些 $w$ 满足 $R(H, w) = \mathsf{True}$ 的概率为至多为

    \[
        \left(\max_{w \in \mathcal{W}} \op{Pr}_{H \from D} [R(H, w)] \right) \times \op{rank}(A, \mathcal{H}).
    \]

    换言之，$A$ 成功输出满足 $R(H, w) = \mathsf{True}$ 的 $w$ 的概率至多为 $\op{rank}(A, \mathcal{H})$ 和最优固定策略的成功概率（忽略 $H$ 直接输出某个固定 $w$ 的最大概率）的乘积.

    ???+ note "Proof"
        $A$ 输出 $w$ 满足 $R(H, w) = \mathsf{True}$ 的概率为

        \[
            \op{Pr}_{H \from D \land w \from \ket{\psi_H}} [R(H, w)] = \sum_H \op{Pr}_D [H] \sum_{w: R(H, w)} \lvert \innerproduct{w}{\psi_H} \rvert^2 = \sum_w \sum_{H: R(H, w)} \op{Pr}_D [H] \lvert \innerproduct{w}{\psi_H} \rvert^2.
        \]