# Quantum Commitments and Signatures Without One-Way Functions

## Preliminaries

### Basic Notations

$X, Y, Z$ 对应 Pauli 算子，$X_j$ 表示应用在第 $j$ 个量子比特上的 Pauli $X$ 算子. 对于 $n$ 比特字符串 $x, z$，定义

\[
    X^x = \bigotimes_{j=1}^n X_j^{x_j}, \quad Z^z = \bigotimes_{j=1}^n Z_j^{z_j}.
\]

对于函数 $f$，若对于所有常数 $c > 0$，当 $\lambda$ 足够大的时候，都有 $f(\lambda) \leq \lambda^{-c}$，则称 $f$ 是**可忽略的**.

!!!+ lemma "Quantum one-time pad"
    对任意 $m$ 量子比特的状态 $\rho$，都有

    \[
        \frac{1}{4^m} \sum_{x \in \{0, 1\}^m} \sum_{z \in \{0, 1\}^m} X^x Z^z \rho Z^z X^x = \frac{I^{\otimes m}}{2^m}.
    \]

### Pseudorandom Quantum States Generators

!!!+ definition "Pseudorandom Quantum States Generators(PRSGs)"
    伪随机量子态生成器是一个 $\mathrm{QPT}$ 算法 $\mathsf{StateGen}$，它接收输入 $k \in \{0, 1\}^n$，输出一个 $m$ 量子比特的态 $\ket{\phi_k}$. 其安全性要求如下：对于任意多项式 $t$ 以及非均匀 $\mathrm{QPT}$ 敌手 $\mathcal{A}$，存在可忽略函数 $\mathsf{negl}$，使得对于所有的 $n$，都有

    \[
        \left\lvert \mathop{Pr}\limits_{k \gets \{0, 1\}^n}[\mathcal{A}(\ket{\phi_k}^{\otimes t(n)}) = 1] - \mathop{Pr}\limits_{\ket{\psi} \gets \mu_m}[\mathcal{A}(\ket{\psi}^{\otimes t(n)}) = 1] \right\rvert \leq \mathsf{negl}(n),
    \]

    其中 $\mu_m$ 表示 $m$ 量子比特的 Haar 测度.

    !!!+ remark
        在大部分的情形下，$\mathsf{StateGen}$ 是如下的 $\mathrm{QPT}$ 算法：首先接收输入 $k \in \{0, 1\}^n$，然后计算酉量子电路 $U_k$ 的经典描述，将 $U_k$ 应用到全零态 $\ket{0 \ldots m}$ 上，得到态 $\ket{\Phi_k}_{A B} = U_k \ket{0 \ldots 0}$，最终输出 $m$ 量子比特态 $\rho_k = \mathrm{Tr}_B(\ket{\Phi_k}\bra{\Phi_k}_{A B})$.

        平均而言，$\rho_k$ 需要接近纯态，否则 $\mathrm{QPT}$ 敌手可以在两个副本上运行 SWAP 测试安全性.

        考虑敌手 $\mathcal{A}$，其对收到的两个状态副本运行 SWAP 测试，当输入的是均匀随机的 $k$ 对应的 $\rho_k^{\otimes t}$ 时，$\mathcal{A}$ 的输出为 1 的概率为 $\frac{1 + \frac{1}{2^n} \sum_k \mathrm{Tr}(\rho_k^2)}{2}$，而当输入的是 Haar 测度下的随机态 $\ket{\psi}^{\otimes t}$ 时，$\mathcal{A}$ 的输出为 1 的概率为 $1$. 因此，为了满足安全性，必须有

        \[
            \left \lvert \frac{1 + \frac{1}{2^n} \sum_k \mathrm{Tr}(\rho_k^2)}{2} - 1 \right \rvert \leq \mathsf{negl}(\lambda),
        \]

        这也就意味着 $\rho_k$ 的平均纯度 $\frac{1}{2^n} \sum_k \mathrm{Tr}(\rho_k^2)$ 非常接近于 $1$. 

        为了简化讨论，本文认为 $\rho_k$ 是纯态 $\ket{\phi_k}$.

        因此，实际上 $\mathsf{StateGen}$ 生成的是 $\ket{\Phi_k}_{A B} = \ket{\phi_k}_A \otimes \ket{\eta_k}_B$，其中 $\ket{\eta_k}$ 是辅助系统中的状态. 为了简化记号，本文假设 $\mathsf{StateGen}$ 最终生成的状态中不包含辅助系统；但即使存在辅助态，本文的结果仍然成立.

本文的量子承诺构造只需要 PRSGs 的一个较弱版本，即只需要保证 $t = 1$ 时的安全性，称这种生成器为单副本安全的 PRSGs.

!!!+ definition "Single-copy-secure PRSGs"
    单副本安全的伪随机量子态生成器是一个 $\mathrm{QPT}$ 算法 $\mathsf{StateGen}$，它接收输入 $k \in \{0, 1\}^n$，输出一个 $m$ 量子比特的态 $\ket{\phi_k}$. 其安全性要求如下：对于非均匀 $\mathrm{QPT}$ 敌手 $\mathcal{A}$，存在可忽略函数 $\mathsf{negl}$，使得对于所有的 $n$，都有

    \[
        \left\lvert \mathop{Pr}\limits_{k \gets \{0, 1\}^n}[\mathcal{A}(\ket{\phi_k}) = 1] - \mathop{Pr}\limits_{\ket{\psi} \gets \mu_m}[\mathcal{A}(\ket{\psi}) = 1] \right\rvert \leq \mathsf{negl}(n),
    \]

    其中 $\mu_m$ 表示 $m$ 量子比特的 Haar 测度.

    !!!+ remark
        因为从 Haar 分布中随机抽取的 $m$ 量子比特的状态的单个副本在密度矩阵意义下等价于 $m$ 个量子比特的最大混合态 $\frac{I^{\otimes m}}{2^m}$，因此单副本安全的 PRSGs 的安全性实际上意味着单个 $\ket{\phi_k}$ 在计算上与 $\frac{I^{\otimes m}}{2^m}$ 无法区分.

    !!!+ remark
        在单副本安全的 PRSGs 中，基于 SWAP 测试的攻击不再有效，所以可以构建一个输出不是纯态的单副本安全的 PRSGs：$\mathsf{StateGen}(k) \to \frac{I^{\otimes m}}{2^m}$. 但在讨论单副本安全的 PRSGs 时，本文仍然假设 $\mathsf{StateGen}$ 输出的是纯态 $\ket{\phi_k}$.

    !!!+ remark
        单副本安全的 PRSGs 可能比多副本安全的 PRSGs 更容易构造. 可以利用经典的伪随机生成器 $G: \{0, 1\}^n \to \{0, 1\}^m$ 构造一个简单的单副本安全的 PRSGs：对任意 $k \in \{0, 1\}^n$，定义 $\mathsf{StateGen}(k) = \ket{\phi_k} = \ket{G(k)}$.

    !!!+ remark
        有人可能会认为，当 $m \geq n + 1$ 时，一个单副本安全的 PRSG 本身就是一个经典伪随机生成器（PRG）. 理由是如果在计算基下测量 $m$ 量子比特态 $\ket{\phi_k}$，那么测量结果的概率分布在计算上无法与均匀的 $m$ 比特分布区分；而对于最大混合态 $\frac{I^{\otimes m}}{2^m}$ 进行计算基测量时，测量结果的概率分布正是均匀的 $m$ 比特分布. 然而，这种推论很奇怪，因为如果它成立，单副本安全 PRSG 的存在就会推出经典 PRG 的存在，这与先前的研究相矛盾. 关键在于：在计算基下测量 $\ket{\phi_k}$ 并不能得到一个 PRG，因为测量结果不是确定性得到的，而 PRG 必须是确定性算法.

## Commitments

### Definition

!!!+ definition "Non-interactive quantum commitments(Syntax)"
    非交互式量子承诺方案包含以下协议.

    - 承诺阶段：$b \in \{0, 1\}$ 为承诺比特，发送方在寄存器 $R$ 和 $C$ 上生成量子态 $\ket{\psi_b}_{R C}$，并将 $C$ 发送给接收方. 状态集合 $\{\ket{\psi_b}\}_{b \in \{0, 1\}}$ 必须能够通过量子多项式时间算法从全零态生成.

    - 揭示阶段：发送方将寄存器 $R$ 和承诺比特 $b$ 发送给接收方，接收方在寄存器 $R$ 和 $C$ 上执行测量 $\{\ket{\psi_b}\bra{\psi_b}, I - \ket{\psi_b}\bra{\psi_b}\}$，若测量结果为 $\ket{\psi_b}\bra{\psi_b}$，则接收方输出 $b$，否则输出 $\perp$. 因为 $\{\ket{\psi_b}\}_{b \in \{0, 1\}}$ 可以通过量子多项式时间算法从全零态生成，因此上述测量也可以高效实现.

!!!+ definition "Perfect correctness"
    如果诚实发送方承诺了比特 $b$，诚实接收方在揭示阶段输出 $b$ 的概率为 $1$，则称该承诺方案具有**完美正确性**.

!!!+ definition "Computational hiding"
    考虑挑战者 $\mathcal{C}$ 和 $\mathrm{QPT}$ 敌手 $\mathcal{A}$ 之间的安全游戏 $\mathsf{Exp}(b)$，其中 $b \in \{0, 1\}$.

    1. $\mathcal{C}$ 生成 $\ket{\psi_b}_{R C}$，并将 $C$ 发送给 $\mathcal{A}$.

    2. 敌手 $\mathcal{A}$ 接收 $C$，并输出一个比特 $b' \in \{0, 1\}$.

    如果对于任意 $\mathrm{QPT}$ 敌手 $\mathcal{A}$，存在可忽略函数 $\mathsf{negl}$，使得对于所有的 $n$，都有

    \[
        \left\lvert \op{Pr}[\mathsf{Exp}(0) = 1] - \op{Pr}[\mathsf{Exp}(1) = 1] \right\rvert \leq \mathsf{negl}(n),
    \]

    则称该非交互式量子承诺方案具有**计算隐藏性**.

!!!+ definition "Statistical sum-binding"
    考虑挑战者 $\mathcal{C}$ 和计算能力无限的敌手 $\mathcal{A}$ 之间的安全游戏：

    1. $\mathcal{A}$ 生成寄存器 $E, R, C$ 上的量子态 $\ket{\Psi}_{E R C}$.

    2. $\mathcal{A}$ 将寄存器 $C$ 发送给 $\mathcal{C}$，作为承诺.

    3. 如果敌手希望挑战者打开 $b \in {0, 1}$，就在寄存器 $E, R$ 上施加酉变换 $U^{(b)}_{E R}$，然后将寄存器 $R$ 和 $b$ 发送给 $\mathcal{C}$，作为揭示.

    4. 挑战者在寄存器 $R, C$ 上执行测量 $\{\ket{\psi_b}\bra{\psi_b}, I - \ket{\psi_b}\bra{\psi_b}\}$，若测量结果为 $\ket{\psi_b}\bra{\psi_b}$，则挑战者输出 $b$，否则输出 $\perp$.

    设 $p_b$ 为对手使挑战者成功打开 $b$ 的概率，则

    \[
        p_b = \bra{\psi_b}_{R C} \mathrm{Tr}_E(U^{(b)}_{E R} \ket{\Psi}\bra{\Psi}_{E R C} U^{(b) \dagger}_{E R}) \ket{\psi_b}_{R C}.
    \]

    如果对于任意计算能力无限的敌手 $\mathcal{A}$，都存在可忽略函数 $\mathsf{negl}$，使得对于所有的 $n$，都有

    \[
        p_0 + p_1 \leq 1 + \mathsf{negl}(n),
    \]

    则称该非交互式量子承诺方案具有**统计求和绑定性**.

    该定义表示恶意发送方让同一个承诺分别成功打开为 $0$ 和 $1$ 的概率之和至多比 $1$ 大一个可忽略函数. 

### Construction

设 $\mathsf{StateGen}$ 是一个单副本安全的 PRSG，以 $k \in \{0, 1\}^n$ 为输入，输出一个 $m$ 量子比特的态 $\ket{\phi_k}$. 

承诺阶段如下：

1. 设 $b \in \{0, 1\}$ 为承诺比特，发送方生成 

    \[
        \ket{\psi_b} := \frac{1}{\sqrt{2^{2m + n}}} \sum_{x, z \in \{0, 1\}^m} \sum_{k \in \{0, 1\}^n} \ket{x, z, k}_{R} \otimes P_{x, z}^b \ket{\phi_k}_{C},
    \]

    其中 $P_{x, z} := \bigotimes_{j=1}^m X_j^{x_j} Z_j^{z_j}$，并将寄存器 $C$ 发送给接收方.

揭示阶段如下：

1. 发送方将寄存器 $R$ 和承诺比特 $b$ 发送给接收方.

2. 接收方在寄存器 $R, C$ 上执行测量 $\{\ket{\psi_b}\bra{\psi_b}, I - \ket{\psi_b}\bra{\psi_b}\}$，若测量结果为 $\ket{\psi_b}\bra{\psi_b}$，则接收方输出 $b$，否则输出 $\perp$. (该测量是可以高效执行的，因为 $\ket{\psi_b} = V_b \ket{0 \ldots 0}$，接收方可以先施加 $V_b^\dagger$，然后在计算基上测量，当且仅当所有结果均为 $0$ 时接受.)

!!!+ remark
    对以上构造稍作修改，就可以使揭示阶段的通信是完全经典的；这种修改适用于更一般的非交互式量子承诺.

    承诺阶段，发送方均匀随机选择 $x, z \gets \{0, 1\}^{\lvert R \rvert}$，其中 $\lvert R \rvert$ 表示寄存器 $R$ 的量子比特数，随后发送方在 $\ket{\phi_b}_{R C}$ 的寄存器 $R$ 上施加 $\bigotimes_{j=1}^{\lvert R \rvert} X_j^{x_j} Z_j^{z_j}$，随后将寄存器 $C$ 和 $R$ 均发送给接收方. 

    揭示阶段，发送方向接收方发送 $b$ 以及经典字符串 $(x, z)$. 接收方先在寄存器 $R$ 上施加同样的 Pauli 算子 $\bigotimes_{j=1}^{\lvert R \rvert} X_j^{x_j} Z_j^{z_j}$，随后运行原先的验证算法.

    计算隐藏性是显然的，因为在揭示阶段前，因为量子一次一密的作用，寄存器 $R$ 相当于被偏迹掉了.

    统计求和绑定性也容易理解. 假设修改后的方案存在一个能破坏统计求和绑定性的恶意发送方，那么就可以构造一个能破坏原先方案统计求和绑定性的恶意发送方，因为原方案中的恶意发送方可以在内部模拟修改后方案的恶意发送方.

!!!+ remark
    承诺构造还可以推广到 PRSGs 使用辅助量子比特的情形. 考虑一个更一般的 PRSG，其生成 $\ket{\phi_k} \otimes \ket{\eta_k}$，并且输出 $\ket{\phi_k}$. 此情况下，只需要将 $\ket{\psi_b}$ 替换为

    \[
        \ket{\psi_b} := \frac{1}{\sqrt{2^{2m + n}}} \sum_{x, z \in \{0, 1\}^m} \sum_{k \in \{0, 1\}^n} (\ket{x, z, k} \otimes \ket{\eta_k})_{R} \otimes P_{x, z}^b \ket{\phi_k}_{C},
    \]

    承诺方案仍然满足隐藏性和绑定性.

### Computational Hiding

!!!+ theorem "Computational Hiding"
    以上构造满足计算绑定性.

    ???+ note "Proof"
        考虑 $\mathsf{Hyb}_0(b)$ 这一安全游戏，其定义与原实验一致.

        1. 挑战者 $\mathcal{C}$ 生成 

            \[
                \ket{\psi_b} := \frac{1}{\sqrt{2^{2m + n}}} \sum_{x, z \in \{0, 1\}^m} \sum_{k \in \{0, 1\}^n} \ket{x, z, k}_{R} \otimes P_{x, z}^b \ket{\phi_k}_{C},
            \]

            并将寄存器 $C$ 发送给敌手 $\mathcal{A}$，其中 $P_{x, z} := \bigotimes_{j=1}^m X_j^{x_j} Z_j^{z_j}$.

        2. 敌手 $\mathcal{A}$ 输出比特 $b' \in \{0, 1\}$，作为该混合实验的输出.

        定义 $\mathsf{Hyb}_1(b)$ 如下：

        1. 如果 $b = 0$，则 $\mathcal{C}$ 选择一个 Haar 测度下的 $m$ 个量子比特的 Haar 随机态 $\ket{\psi} \gets \mu_m$，并将其发送给 $\mathcal{A}$；如果 $b = 1$，则 $\mathcal{C}$ 生成 $\ket{\psi_1}_{R C}$，并将寄存器 $C$ 发送给 $\mathcal{A}$.

        2. 敌手 $\mathcal{A}$ 输出比特 $b' \in \{0, 1\}$，作为该混合实验的输出.

        !!!+ lemma
            \[
                \lvert \op{Pr}[\mathsf{Hyb}_0(b) = 1] - \op{Pr}[\mathsf{Hyb}_1(b) = 1] \rvert \leq \mathsf{negl}(n).
            \]

            ???+ success "Proof"
                显然 $\op{Pr}[\mathsf{Hyb}_0(1) = 1] = \op{Pr}[\mathsf{Hyb}_1(1) = 1]$. 只需证明 $\lvert \op{Pr}[\mathsf{Hyb}_0(0) = 1] - \op{Pr}[\mathsf{Hyb}_1(0) = 1] \rvert \leq \mathsf{negl}(n)$.

                假设 $\lvert \op{Pr}[\mathsf{Hyb}_0(0) = 1] - \op{Pr}[\mathsf{Hyb}_1(0) = 1] \rvert$ 不是可忽略的，那么就可以按照如下步骤构造一个可以攻破 PRSGs 的敌手 $\mathcal{A}'$. 设 $b''$ 是 PRSGs 的安全游戏中的参数：

                1. 如果 $b'' = 0$，则 $\mathcal{C}'$ 使用均匀随机的 $k \in \{0, 1\}^n$ 生成 $\ket{\phi_k}$，并将其发送给 $\mathcal{A}'$；如果 $b'' = 1$，则 $\mathcal{C}'$ 从 Haar 测度中随机选择一个 $m$ 个量子比特的态 $\ket{\psi} \gets \mu_m$，并将其发送给 $\mathcal{A}'$.

                2. 敌手 $\mathcal{A}'$ 将接收到的态发送给 $\mathcal{A}$.

                3. 敌手 $\mathcal{A}'$ 输出 $\mathcal{A}$ 的输出.

                如果 $b'' = 0$，那么模拟的是 $\mathsf{Hyb}_0(0)$，如果 $b'' = 1$，那么模拟的是 $\mathsf{Hyb}_1(0)$，从而 $\mathcal{A}'$ 攻破了 PRSGs 的安全性.

        定义 $\mathsf{Hyb}_2(b)$ 如下：

        1. 挑战者 $\mathcal{C}$ 选择一个 Haar 测度下的 $m$ 个量子比特的 Haar 随机态 $\ket{\psi} \gets \mu_m$，并将其发送给 $\mathcal{A}$.

        2. 敌手 $\mathcal{A}$ 输出比特 $b' \in \{0, 1\}$，作为该混合实验的输出.

        !!!+ lemma
            \[
                \lvert \op{Pr}[\mathsf{Hyb}_1(b) = 1] - \op{Pr}[\mathsf{Hyb}_2(b) = 1] \rvert \leq \mathsf{negl}(n).
            \]

            ???+ success "Proof"
                显然 $\op{Pr}[\mathsf{Hyb}_1(0) = 1] = \op{Pr}[\mathsf{Hyb}_2(0) = 1]$. 只需证明 $\lvert \op{Pr}[\mathsf{Hyb}_1(1) = 1] - \op{Pr}[\mathsf{Hyb}_2(1) = 1] \rvert \leq \mathsf{negl}(n)$.

                依然反证，假设 $\lvert \op{Pr}[\mathsf{Hyb}_1(1) = 1] - \op{Pr}[\mathsf{Hyb}_2(1) = 1] \rvert$ 不是可忽略的，那么就可以按照如下步骤构造一个可以攻破 PRSGs 的敌手 $\mathcal{A}'$：

                1. 如果 $b'' = 0$，则 $\mathcal{C}'$ 使用均匀随机的 $k \in \{0, 1\}^n$ 生成 $\ket{\phi_k}$，并将其发送给 $\mathcal{A}'$；如果 $b'' = 1$，则 $\mathcal{C}'$ 从 Haar 测度中随机选择一个 $m$ 个量子比特的态 $\ket{\psi} \gets \mu_m$，并将其发送给 $\mathcal{A}'$.

                2. 敌手 $\mathcal{A}'$ 均匀随机选择 $x, z \gets \{0, 1\}^m$，并对接收到的态施加 Pauli 算子 $P_{x, z} := \bigotimes_{j=1}^m X_j^{x_j} Z_j^{z_j}$，随后将其发送给 $\mathcal{A}$.

                3. 敌手 $\mathcal{A}'$ 输出 $\mathcal{A}$ 的输出.

                如果 $b'' = 0$，那么模拟的是 $\mathsf{Hyb}_1(1)$，如果 $b'' = 1$，那么模拟的是 $\mathsf{Hyb}_2(1)$，从而 $\mathcal{A}'$ 攻破了 PRSGs 的安全性.

        而显然 $\op{Pr}[\mathsf{Hyb}_2(0) = 1] = \op{Pr}[\mathsf{Hyb}_2(1) = 1]$. 所以依据三角不等式，有

        \[
            \lvert \op{Pr}[\mathsf{Hyb}_0(0) = 1] - \op{Pr}[\mathsf{Hyb}_0(1) = 1] \rvert \leq \mathsf{negl}(n).
        \]

### Statistical Binding

!!!+ theorem "Statistical Binding"
    以上构造满足统计求和绑定性.

    ???+ note "Proof"
        令

        \[
            F(\rho, \sigma) := \left( \mathrm{Tr} \sqrt{\sqrt{\rho} \sigma \sqrt{\rho}} \right)^2
        \]

        为两个量子态 $\rho, \sigma$ 之间的保真度. 从而有

        \begin{align*}
            p_b &= \bra{\psi_b}_{R C} \mathrm{Tr}_E(U^{(b)}_{E R} \ket{\Psi}\bra{\Psi}_{E R C} U^{(b) \dagger}_{E R}) \ket{\psi_b}_{R C} \\
            &= F(\ket{\psi_b}\bra{\psi_b}_{R C}, \mathrm{Tr}_E(U^{(b)}_{E R} \ket{\Psi}\bra{\Psi}_{E R C} U^{(b) \dagger}_{E R})) \\
            &\leq F(\mathrm{Tr}_R (\ket{\psi_b}\bra{\psi_b}_{R C}), \mathrm{Tr}_{E R}(U^{(b)}_{E R} \ket{\Psi}\bra{\Psi}_{E R C} U^{(b) \dagger}_{E R})) \\
            &= F(\mathrm{Tr}_R (\ket{\psi_b}\bra{\psi_b}_{R C}), \mathrm{Tr}_{E R}(\ket{\Psi}\bra{\Psi}_{E R C})).
        \end{align*}

        因而，

        \begin{align*}
            p_0 + p_1 &\leq 1 + \sqrt{F(\mathrm{Tr}_R (\ket{\psi_0}\bra{\psi_0}_{R C}), \mathrm{Tr}_R (\ket{\psi_1}\bra{\psi_1}_{R C}))} \\
            &= 1 + \sqrt{F\left(\frac{1}{2^n} \sum_k \ket{\phi_k}\bra{\phi_k}, \frac{1}{2^{2m}} \frac{1}{2^n} \sum_{x, z} \sum_k P_{x, z} \ket{\phi_k}\bra{\phi_k} P_{x, z}^\dagger\right)} \\
            &= 1 + \sqrt{F\left(\frac{1}{2^n} \sum_k \ket{\phi_k}\bra{\phi_k}, \frac{I^{\otimes m}}{2^m}\right)} \\
            &= 1 + \left \lVert \sum_{i = 1}^\xi \sqrt{\lambda_i} \frac{1}{\sqrt{2^m}} \ket{\lambda_i} \bra{\lambda_i} \right \rVert_1 \\
            &= 1 + \sum_{i = 1}^\xi \sqrt{\lambda_i} \frac{1}{\sqrt{2^m}} \\
            &\leq 1 + \sqrt{\sum_{i = 1}^\xi \lambda_i} \sqrt{\sum_{i = 1}^\xi \frac{1}{2^m}} \\
            &= 1 + \sqrt{\frac{2^n}{2^m}} \\
            &\leq 1 + \frac{1}{\sqrt{2^{(c - 1) n}}}.
        \end{align*}

        其中 $\sum_{i = 1}^\xi \lambda_i \ket{\lambda_i}\bra{\lambda_i}$ 是 $\frac{1}{2^n} \sum_k \ket{\phi_k}\bra{\phi_k}$ 的谱分解，$\xi \leq 2^n$ 是其秩.

## Digital Signatures

### One-Way Quantum States Generators

!!!+ definition "One-way quantum states generators(OWSGs)" {#def:owsgs}
    设 $G$ 是一个 $\mathrm{QPT}$ 算法，它接收输入 $k \in \{0, 1\}^n$，输出一个量子态 $\ket{\phi_k}$. 考虑挑战者 $\mathcal{C}$ 和 $\mathrm{QPT}$ 敌手 $\mathcal{A}$ 之间的安全游戏 $\mathsf{Exp}$：

    1. $\mathcal{C}$ 选择 $k \gets \{0, 1\}^n$；

    2. $\mathcal{C}$ 运行 $t + 1$ 次 $\ket{\phi_k} \gets G(k)$；

    3. $\mathcal{C}$ 将 $\ket{\phi_k}^{\otimes t}$ 发送给 $\mathcal{A}$；

    4. 敌手 $\mathcal{A}$ 将 $\sigma \in \{0, 1\}^n$ 发送给 $\mathcal{C}$；

    5. $\mathcal{C}$ 使用 $\{\ket{\phi_\sigma} \bra{\phi_\sigma}, I - \ket{\phi_\sigma}\bra{\phi_\sigma}\}$ 测量 $\ket{\phi_k}$，若测量结果为 $\ket{\phi_\sigma}\bra{\phi_\sigma}$，则 $\mathcal{C}$ 输出 $1$，否则输出 $0$.

    称 $G$ 是一个**单向量子态生成器**，如果对于任意多项式 $t = \op{poly}(n)$，以及任意 $\mathrm{QPT}$ 敌手 $\mathcal{A}$，存在可忽略函数 $\mathsf{negl}$，使得

    \[
        \op{Pr}[\mathsf{Exp} = 1] \leq \mathsf{negl}(n).
    \]

    !!!+ remark
        单向性的另一种自然定义是给定 $\ket{\phi_k}^{\otimes t}$，敌手很难恢复 $k$，但这种定义并不适用于本文的数字签名构造.
    
    !!!+ remark {#rem:owsgs-with-auxiliary-states}
        $G$ 的最一般形式如下：给定 $k \in \{0, 1\}^n$，算法首先计算量子酉电路 $U_k$ 的经典描述，然后将 $U_k$ 应用到全零态 $\ket{0 \ldots 0}$ 上，得到态 $\ket{\Phi_k}_{A B} = U_k \ket{0 \ldots 0}$，最终输出 $\rho_k := \mathrm{Tr}_B(\ket{\Phi_k}\bra{\Phi_k}_{A B})$. 因为在本文的构造中，$\rho_k$ 将作为公钥使用，因此假设 $\rho_k$ 是纯态. 如果公钥和私钥处于纠缠状态，这种设定并不自然. 因而 $U_k \ket{0 \ldots 0} = \ket{\phi_k}_A \otimes \ket{\eta_k}_B$，其中 $\ket{\eta_k}$ 是辅助系统中的状态. 为了简化记号，本文假设 $G$ 最终生成的状态中不包含辅助系统. 在没有辅助系统的情况下，\adref{def:owsgs} 中挑战者的测量可以按照如下方式实现：挑战者首先对接收到的状态施加 $U_\sigma^\dagger$，随后在计算基上测量，全 $0$ 的测量结果对应于 $\ket{\phi_\sigma}\bra{\phi_\sigma}$，否则对应于 $I - \ket{\phi_\sigma}\bra{\phi_\sigma}$. 即使存在辅助态，结论仍然成立. 此时给定 $\sigma$，挑战者首先生成 $U_\sigma \ket{0 \ldots 0} = \ket{\phi_\sigma}_A \otimes \ket{\eta_\sigma}_B$ 以得到 $\ket{\eta_\sigma}$，随后对 $\ket{\phi_k} \otimes \ket{\eta_\sigma}$ 施加 $U_\sigma^\dagger$，随后在计算基上测量，测量结果为全 $0$ 则接受，否则拒绝.

!!!+ lemma "PRSGs imply OWSGs"
    如果存在一个满足 $m \geq cn$ 的 PRSG，其中 $c > 1$ 是常数，则存在一个 OWSG.

    ???+ success "Proof"
        假设 \adref{def:owsgs} 中定义的安全游戏中，当 $G = \mathsf{StateGen}$ 时，$\op{Pr}[\mathsf{Exp} = 1]$ 不是可忽略的，那么就可以构造一个能攻破 PRSGs 的敌手 $\mathcal{A}'$，设 $b'$ 是 PRSGs 的安全游戏中的参数：

        1. 如果 $b' = 0$，则 PRSGs 的挑战者 $\mathcal{C}'$ 均匀随机选择 $k \in \{0, 1\}^n$，运行 $t + 1$ 次 $\ket{\phi_k} \gets \mathsf{StateGen}(k)$，并将 $\ket{\phi_k}^{\otimes t + 1}$ 发送给 $\mathcal{A}'$；如果 $b' = 1$，则 $\mathcal{C}'$ 则发送 $t + 1$ 个 Haar 随机态 $\ket{\psi}$ 的副本 $\ket{\psi}^{\otimes t + 1}$ 给 $\mathcal{A}'$. 即 $\mathcal{A}'$ 接收到的态是 $\rho^{\otimes t + 1}$，当 $b' = 0$ 时，$\rho = \ket{\phi_k}$，当 $b' = 1$ 时，$\rho = \ket{\psi}$.

        2. 敌手 $\mathcal{A}'$ 将 $\rho^{\otimes t}$ 发送给 $\mathcal{A}$.

        3. 敌手 $\mathcal{A}$ 输出 $\sigma \in \{0, 1\}^n$.

        4. 敌手 $\mathcal{A}'$ 在 $\{ket{\phi_\sigma}\bra{\phi_\sigma}, I - \ket{\phi_\sigma}\bra{\phi_\sigma}\}$ 上测量 $\rho$，若测量结果为 $\ket{\phi_\sigma}\bra{\phi_\sigma}$，则 $\mathcal{A}'$ 输出 $1$，否则输出 $0$.

        显然 $\op{Pr}[\mathcal{A}' \to 1 \mid b' = 0] = \op{Pr}[\mathsf{Exp} = 1]$，另一方面：

        \begin{align*}
            \op{Pr}[\mathcal{A}' \to 1 \mid b' = 1] &= \int \mathrm{d}\mu(\psi) \sum_{\sigma \in \{0, 1\}^n} \op{Pr}[\sigma \gets \mathcal{A}(\ket{\psi}^{\otimes t})] \lvert \innerproduct{\phi_\sigma}{\psi} \rvert^2 \\
            &\leq \int \mathrm{d}\mu(\psi) \sum_{\sigma \in \{0, 1\}^n} \lvert \innerproduct{\phi_\sigma}{\psi} \rvert^2 \\
            &= \int \mathrm{d}\mu(\psi) \sum_{\sigma \in \{0, 1\}^n} \innerproduct{\phi_\sigma}{\psi} \innerproduct{\psi}{\phi_\sigma} \\
            &= \sum_{\sigma \in \{0, 1\}^n} \bra{\phi_\sigma} \left( \int \mathrm{d}\mu(\psi) \ket{\psi}\bra{\psi} \right) \ket{\phi_\sigma} \\
            &= \sum_{\sigma \in \{0, 1\}^n} \bra{\phi_\sigma} \frac{I^{\otimes m}}{2^m} \ket{\phi_\sigma} \\
            &\leq \frac{2^n}{2^m} \\
            &\leq \frac{1}{2^{(c - 1) n}}.
        \end{align*}

        因此 $b' = 0$ 时，$\mathcal{A}'$ 能够以不可忽略的概率输出 $1$，而 $b' = 1$ 时，$\mathcal{A}'$ 输出 $1$ 的概率是可忽略的，从而 $\mathcal{A}'$ 可以区分 PRSGs 的输出和 Haar 随机态，从而攻破 PRSGs 的安全性. 

    !!!+ remark
        带有辅助系统的测量验证与 \adref{rem:owsgs-with-auxiliary-states} 中的讨论类似. 

### Definition of Digital Signatures with Quantum Public Keys

!!!+ definition "Digital signatures with quantum public keys"
    具有量子密钥的数字签名方案由以下四个算法 $(\mathsf{Gen}_1, \mathsf{Gen}_2, \mathsf{Sign}, \mathsf{Verify})$ 组成：

    - $\mathsf{Gen}_1(1^\lambda)$：经典 $\mathrm{PPT}$ 算法，接收安全参数 $1^\lambda$，输出经典私钥 $sk$.

    - $\mathsf{Gen}_2(sk)$：量子 $\mathrm{QPT}$ 算法，接收经典私钥 $sk$，输出量子公钥 $pk$.

    - $\mathsf{Sign}(sk, m)$：经典确定性多项式时间算法，接收经典私钥 $sk$ 和消息 $m$，输出经典签名 $\sigma$.

    - $\mathsf{Verify}(pk, m, \sigma)$：量子 $\mathrm{QPT}$ 算法，接收量子公钥 $pk$、消息 $m$ 和签名 $\sigma$，输出 $\top / \bot$ 分别表示接受或拒绝签名.

!!!+ definition "Perfect correctness"
    如果对于任意消息 $m$，都有

    \[
        \op{Pr}[\top \gets \mathsf{Verify}(pk, m, \sigma) \mid sk \gets \mathsf{Gen}_1(1^\lambda), pk \gets \mathsf{Gen}_2(sk), \sigma \gets \mathsf{Sign}(sk, m)] = 1,
    \]

    则称该数字签名方案具有**完美正确性**.

!!!+ definition "One-time security of digital signatures with quantum public keys"
    考虑挑战者 $\mathcal{C}$ 和 $\mathrm{QPT}$ 敌手 $\mathcal{A}$ 之间的安全游戏 $\mathsf{Exp}$：

    1. 挑战者 $\mathcal{C}$ 运行 $sk \gets \mathsf{Gen}_1(1^\lambda)$.

    2. 敌手 $\mathcal{A}$ 可以进行多项式次查询 $pk \gets \mathsf{Gen}_2(sk)$.

    3. 敌手 $\mathcal{A}$ 向挑战者 $\mathcal{C}$ 发送消息 $m$.

    4. 挑战者 $\mathcal{C}$ 运行 $\sigma \gets \mathsf{Sign}(sk, m)$，并将 $\sigma$ 发送给敌手 $\mathcal{A}$.

    5. 敌手 $\mathcal{A}$ 发送 $(m', \sigma')$ 给挑战者 $\mathcal{C}$.  

    6. 挑战者 $\mathcal{C}$ 运行 $\mathsf{Verify}(pk, m', \sigma')$，若输出为 $\top$ 且 $m' \neq m$，则挑战者 $\mathcal{C}$ 输出 $1$，否则输出 $0$.

    如果对于任意 $\mathrm{QPT}$ 敌手 $\mathcal{A}$，存在可忽略函数 $\mathsf{negl}$，使得对于所有的 $n$，都有

    \[
        \op{Pr}[\mathsf{Exp} = 1] \leq \mathsf{negl}(n),
    \]

    则称该数字签名方案具有**一次性安全性**.   

### Construction

设 $G$ 是一个 OWSG，下面构造一个具有量子公钥的一次性安全数字签名方案. 简单起见，限制消息空间为 $\{0, 1\}$.

- $\mathsf{Gen}_1(1^n)$：选择 $k_0, k_1 \gets \{0, 1\}^n$，输出 $sk := (sk_0, sk_1)$，其中 $sk_b := k_b$.

- $\mathsf{Gen}_2(sk)$：运行 $\ket{\phi_{k_b}} \gets G(sk_b)$，输出 $pk := (pk_0, pk_1)$，其中 $pk_b := \ket{\phi_{k_b}}$.

- $\mathsf{Sign}(sk, m)$：输出 $\sigma := sk_m$.

- $\mathsf{Verify}(pk, m, \sigma)$：在 $\{\ket{\phi_\sigma}\bra{\phi_\sigma}, I - \ket{\phi_\sigma}\bra{\phi_\sigma}\}$ 上测量 $pk_m$，若测量结果为 $\ket{\phi_\sigma}\bra{\phi_\sigma}$，则输出 $\top$，否则输出 $\bot$.

显然构造满足完美正确性. 

### Security

!!!+ theorem
    该数字签名方案具有一次性安全性.

    ???+ note "Proof"
        考虑挑战者 $\mathcal{C}$ 和 $\mathrm{QPT}$ 敌手 $\mathcal{A}$ 之间的安全游戏 $\mathsf{Exp}$.

        1. 挑战者 $\mathcal{C}$ 选择 $k_0, k_1 \gets \{0, 1\}^n$.

        2. $\mathcal{A}$ 可以进行 $\poly{n}$ 次查询 $\ket{\phi_{k_b}} \gets G(k_b)$.

        3. 敌手 $\mathcal{A}$ 向挑战者 $\mathcal{C}$ 发送消息 $m$.

        4. 挑战者 $\mathcal{C}$ 将 $k_m$ 发送给敌手 $\mathcal{A}$.

        5. 敌手 $\mathcal{A}$ 发送 $\sigma$ 给挑战者 $\mathcal{C}$.

        6. 挑战者 $\mathcal{C}$ 在 $\{\ket{\phi_\sigma}\bra{\phi_\sigma}, I - \ket{\phi_\sigma}\bra{\phi_\sigma}\}$ 上测量 $\ket{\phi_{k_{m \oplus 1}}}$，若测量结果为 $\ket{\phi_\sigma}\bra{\phi_\sigma}$，则挑战者 $\mathcal{C}$ 输出 $1$，否则输出 $0$.

        假设构造不是一次性安全的，即存在一个敌手 $\mathcal{A}$，其分别查询 $\mathsf{Gen}_2(sk_0)$ 和 $\mathsf{Gen}_2(sk_1)$ 各 $s = \poly{n}$ 次，且 $\op{Pr}[\mathsf{Exp} = 1]$ 不是可忽略的. 那么就可以构造一个能攻破 OWSG 的敌手 $\mathcal{A}'$，设 $\mathcal{C}'$ 是 OWSG 的挑战者：

        1. $\mathcal{C}'$ 选择 $k \gets \{0, 1\}^n$，运行 $s + 1$ 次 $\ket{\phi_k} \gets G(k)$，并将 $\ket{\phi_k}^{\otimes s}$ 发送给 $\mathcal{A}'$.

        2. $\mathcal{A}'$ 选择 $r \gets \{0, 1\}$，以及 $k' \gets \{0, 1\}^n$，运行 $s$ 次 $\ket{\phi_{k'}} \gets G(k')$. 如果 $r = 0$，则 $\mathcal{A}'$ 将 $(\ket{\phi_k}^{\otimes s}, \ket{\phi_{k'}}^{\otimes s})$ 发送给 $\mathcal{A}$；如果 $r = 1$，则 $\mathcal{A}'$ 将 $(\ket{\phi_{k'}}^{\otimes s}, \ket{\phi_k}^{\otimes s})$ 发送给 $\mathcal{A}$.

        3. 敌手 $\mathcal{A}$ 向 $\mathcal{A}'$ 发送消息 $m$.

        4. 如果 $r = m$，则 $\mathcal{A}'$ 中止；如果 $r \neq m$，则 $\mathcal{A}'$ 将 $k'$ 发送给 $\mathcal{A}$.

        5. 敌手 $\mathcal{A}$ 发送 $\sigma$ 给 $\mathcal{A}'$.

        6. $\mathcal{A}'$ 将 $\sigma$ 发送给 $\mathcal{C}'$.

        7. $\mathcal{C}'$ 在 $\{\ket{\phi_\sigma}\bra{\phi_\sigma}, I - \ket{\phi_\sigma}\bra{\phi_\sigma}\}$ 上测量 $\ket{\phi_k}$，若测量结果为 $\ket{\phi_\sigma}\bra{\phi_\sigma}$，则 $\mathcal{C}'$ 输出 $1$，否则输出 $0$.

        直接计算便可以得到 

        \[
            \op{Pr}[\mathcal{C}' \to 1] = \frac{1}{2} \op{Pr}[\mathsf{Exp} = 1],
        \]

        因为 $\op{Pr}[\mathsf{Exp} = 1]$ 不是可忽略的，所以 $\op{Pr}[\mathcal{C}' \to 1]$ 也不是可忽略的，从而 $\mathcal{A}'$ 攻破了 OWSG 的安全性.