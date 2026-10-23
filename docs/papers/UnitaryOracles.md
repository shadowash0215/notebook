# How to Model Unitary Oracles

## Preliminaries

### Conventions for quantum gates and circuits

对于酉门 $U$，定义 $\mathsf{C} U$ 为其受控版本，具体实现为 $\mathsf{C} U (\ket{b} \ket{\psi}) = \ket{b} U^b \ket{\psi}$，其中 $b \in \{0, 1\}$.

对于任意量子态 $\ket{\psi} = \sum_x \alpha_x \ket{x}$，其共轭定义为 $\ket{\psi^*} = \sum_x \alpha_x^* \ket{x}$，其中 $\{\ket{x}\}$ 是计算基.

**关注全局相位**：通常认为只相差一个全局相位的量子电路是等价的，即 $U \cong V \iff U = e^{i \theta} V$. 但是在实现受控版本的时候，却需要关注其全局相位，因为 $\mathsf{C} U$ 和 $\mathsf{C} (e^{i \theta} U)$ 可能不等价. 考虑 $U = \mathbf{I}$，则 $\mathsf{C} U = \mathbf{I}$，而 $\mathsf{C} (e^{i \theta} U) = \mathsf{P}(\theta) \otimes \mathbf{I}$，其中 $\mathsf{P}(\theta)$ 是相位门. 

所以如果使用 $V$ 实现了 $U$，并且希望实现 $\mathsf{C} U$，要么 $V$ 和 $U$ 是一致的，要么掌握 $V$ 和 $U$ 的全局相位差 $\theta$.

通常所谓的通用门集，是在不考虑全局相位的情况下能够以足够高精度逼近任意酉变换，如果将全局相位也纳入考虑的话便不应期待一个通用门集能逼近任意酉变换. 例如，Clifford+T 门集是通用的，但是其中所有门的行列式都是 $i$ 的离散幂次，所以由这些门集构造的电路的行列式也只能是 $i$ 的离散幂集合；而一般酉变换的行列式可以是任意单位复数.

因此，本文总是认为量子电路带有全局相位 $\theta$，并且该电路实现的酉变换是所有门和 $e^{i \theta}$ 的乘积.

**关注辅助量子比特**：对于 $\mathsf{BQP}$ 等判定复杂类，通常认为辅助量子比特的作用如下：初始化为 $\ket{0}$，进行计算，最后测量并丢弃辅助量子比特. 但是对于一般的量子过程，需要确保辅助量子比特不与输出纠缠，所以辅助量子比特在计算结束时要恢复为 $\ket{0}$，这被称为酉变换扩展：

!!!+ definition
    设 $U$ 是作用在 $n$ 个量子比特上的酉变换，$\overline{U}$ 是作用在 $n + a$ 个量子比特上的酉变换，称 $\overline{U}$ 是 $U$ 的一个 $a$-量子比特扩展，如果 $\overline{U} (\ket{\phi} \ket{0}^{\otimes a}) = U \ket{\phi} \ket{0^{\otimes a}}$ 对任意 $\ket{\phi}$ 成立.

定义并没有约束 $\overline{U} \ket{\phi} \ket{x}, \ket{x} \neq \ket{0}^{\otimes a}$ 的行为，不过依据酉性可以知道其不应该包含形如 $\ket{\phi} \ket{0}^{\otimes a}$ 的分量.

### Quantum Complexity

为了度量量子计算问题的复杂度，首先固定一个通用门集，门集的选择通常只会带来多项式级别的差异，具体来说，选择 Clifford+T 门集.

计算模型为经典图灵机 $M$ 生成一个量子电路 $C$ 的经典描述，随后在给定输入上运行. 对于 $\mathsf{BQP}$ 等判定复杂类，$M$ 的输入只有实例长度，随后电路 $C$ 在编码为量子态 $\ket{x}$ 的实例 $x$ 上运行.

### Quantum Distance 

对于两个纯态 $\ket{\psi} = \sum_x \alpha_x \ket{x}$ 和 $\ket{\phi} = \sum_x \beta_x \ket{x}$，二者的距离可以用 $L_2$ 范数来度量：

\[
    \lVert \ket{\psi} - \ket{\phi} \rVert_2 = \sqrt{\sum_x \lvert \alpha_x - \beta_x \rvert^2}.
\]

考虑由密度矩阵表示的两个混合态 $\rho = \sum_{x, x'} \rho_{x, x'} \ket{x} \bra{x'}$ 和 $\tau = \sum_{x, x'} \tau_{x, x'} \ket{x} \bra{x'}$，二者的距离称为迹距离：

\[
    \lVert \rho - \tau \rVert_\mathsf{Tr} = \sum_\lambda \lvert \lambda \rvert,
\]

其中 $\lambda$ 遍历 $\rho - \tau$ 的所有特征值. 迹距离也可以扩展到非自伴矩阵，此时使用的是奇异值. 纯态距离和迹距离之间满足：

\[
    \lVert \ket{\psi} \bra{\psi} - \ket{\phi} \bra{\phi} \rVert_\mathsf{Tr} \leq 2 \lVert \ket{\psi} - \ket{\phi} \rVert_2.
\]

量子信道是从混合态到混合态的一般映射，信道 $\mathcal{E}$ 和 $\mathcal{F}$ 的菱形距离定义为：

\[
    \lVert \mathcal{E} - \mathcal{F} \rVert_\diamond = \max_{\rho} \lVert (\mathcal{E} \otimes \mathbf{I}_N)(\rho) - (\mathcal{F} \otimes \mathbf{I}_N)(\rho) \rVert_\mathsf{Tr},
\]

即两个信道作用在某个混合态后的结果之间的最大迹距离.

对于酉变换，可以考虑多种距离概念，最简单的做法是将其视作量子信道，于是便可以得到两个酉变换 $U$ 和 $V$ 的菱形距离. 需要注意的是，酉变换之间的菱形距离是忽略全局相位的，所以可以定义更强的算子距离

\[
    \lVert U - V \rVert_{op} = \max_\lambda \lVert \lambda \rVert, 
\]

$\lambda$ 遍历 $U - V$ 的所有奇异值.

最后定义平均距离情形：

\[
    \lVert U - V \rVert_{avg} = 1 - \frac{\lvert \mathsf{Tr}(U^\dagger V) \rvert}{N},
\]

其中 $N$ 是 $U$ 和 $V$ 所作用的 Hilbert 空间的维度. 

!!!+ lemma
    如果 $\lVert U - V \rVert_{avg} = \varepsilon$，那么存在量子算法 $\mathcal{A}$，分别对 $U$ 和 $V$ 进行一次查询，使得

    \[
        \op{Pr}[\mathcal{A}^{U, V} (\cdot) = 1] = 1 - \Theta(\varepsilon).
    \]

    ???+ success "Proof"
        制备 Haar 随机态 $\ket{\psi}$ 的两个复制，计算 $U \ket{\psi}$ 和 $V \ket{\psi}$，随后进行 SWAP 测试. 接受的概率为

        \begin{align*}
            \frac{1}{2} + \frac{\lvert \bra{\psi} V^\dagger U \ket{\psi} \rvert^2}{2} &= \frac{1}{2} + \frac{\bra{\psi} V^\dagger U \ket{\psi} \bra{\psi} U^\dagger V \ket{\psi}}{2} \\
            &= \frac{1}{2} + \frac{\mathsf{Tr}((V^\dagger U) \otimes (U^\dagger V) \ket{\psi}^{\otimes 2} \bra{\psi}^{\otimes 2})}{2} \\
        \end{align*}

        现在考虑对 $\ket{\psi}$ 取平均，因为对于任意 $\mathcal{H}$ 上的 Haar 随机态 $\ket{\psi}$，$\ket{\psi}^{\otimes 2} \bra{\psi}^{\otimes 2}$ 都位于 $\mathcal{H}^{\otimes 2}$ 的对称子空间上，所以只需要选择能够对角化 $U^\dagger V$ 的正交基，对应的特征值为 $\lambda_i$，则

        \begin{align*}
            \mathbb{E}_\psi[\ket{\psi}^{\otimes 2} \bra{\psi}^{\otimes 2}] &= \frac{2}{N(N + 1)} \frac{I + \mathsf{SWAP}}{2} = \frac{2}{N(N + 1)} \sum_i \ket{i, i} \bra{i, i} + \frac{1}{2} \sum_{i < j} (\ket{i, j} + \ket{j, i})(\bra{i, j} + \bra{j, i}) \\
            (V^\dagger U) \otimes (U^\dagger V) &= \sum_{i, j} \lambda_i \lambda_j^* \ket{i, j} \bra{i, j}
        \end{align*}

        因此接受概率为

        \begin{align*}
            & \frac{1}{2} + \frac{\sum_i \lambda_i \lambda_i^* + \frac{1}{2} \sum_{i < j} (\lambda_i \lambda_j^* + \lambda_j \lambda_i^*)}{N(N + 1)} \\
            &= \frac{1}{2} + \frac{2 \sum_i \lambda_i \lambda_i^* + \sum_{i \neq j} \lambda_i \lambda_j^*}{2 N(N + 1)} \\
            &= \frac{1}{2} + \frac{\sum_i \lambda_i \lambda_i^* + \sum_{i, j} \lambda_i \lambda_j^*}{2 N(N + 1)} \\
            &= \frac{1}{2} + \frac{\sum_i \lvert \lambda_i \rvert^2 + \lvert \sum_i \lambda_i \rvert^2}{2 N(N + 1)} \\
            &= \frac{1}{2} + \frac{N + \lvert \mathsf{Tr}(U^\dagger V) \rvert^2}{2 N(N + 1)} \\
            &= \frac{1}{2} + \frac{1}{2(N + 1)} + \frac{N(1 - \varepsilon)^2}{2 (N + 1)} \\
            &= 1 - \frac{N}{N + 1} \varepsilon(1 - \varepsilon/2) \\
            &= 1 - \Theta(\varepsilon)
        \end{align*}

!!!+ lemma
    如果 $\lVert U - V^{-1} \rVert_{avg} = \varepsilon$，那么存在量子算法 $\mathcal{A}$，分别对 $U$ 和 $V$ 进行一次查询，使得

    \[
        \op{Pr}[\mathcal{A}^{U, V} (\cdot) = 1] = 1 - \Theta(\varepsilon).
    \]

    ???+ success "Proof"
        $\lVert U - V^{-1} \rVert_{avg} = \varepsilon \implies \lVert U V - I \rVert_{avg} = \varepsilon$.

!!!+ lemma
    如果 $\lVert U - V^* \rVert_{avg} = \varepsilon$，那么存在量子算法 $\mathcal{A}$，分别对 $U$ 和 $V$ 进行一次查询，使得

    \[
        \op{Pr}[\mathcal{A}^{U, V} (\cdot) = 1] = 1 - \Theta(\varepsilon).
    \]

    ???+ success "Proof"
        算法制备最大纠缠态 $\ket{\Phi} = \frac{1}{\sqrt{N}} \sum_i \ket{i, i}$，对第一个系统施加 $V$，对第二个系统施加 $U$，随后将 $\ket{\Phi}$ 投影到结果上. 接受的概率为

        \[
            \lvert \bra{\Phi} (V \otimes U) \ket{\Phi} \rvert^2.
        \]

        考虑将 $\ket{\Phi}$ 视作矩阵，列由第一个系统索引，行由第二个系统索引，则 $\ket{\Phi} = \frac{I}{\sqrt{N}}$，并且对第一个系统作用 $V$ 等价于矩阵左乘 $V$，对第二个系统作用 $U$ 等价于矩阵右乘 $U^T$，所以接受概率为

        \begin{align*}
            \lvert \mathsf{Tr}(\Phi^\dagger V \Phi U^T) \rvert^2 &= \lvert \mathsf{Tr}(U^T V) \rvert^2 / N^2 = \lvert \mathsf{Tr}(U^\dagger V^*) \rvert^2 / N^2 \\
            &= (1 - \lVert U - V^* \rVert_{avg})^2 = (1 - \varepsilon)^2 = 1 - \Theta(\varepsilon).
        \end{align*}

### Other Useful Quantum Lemmas

考虑量子查询算法在进行第 $t$ 次查询时所处的状态为 $\ket{\phi_t}$，定义 $q_x(\ket{\phi_t})$ 为第 $t$ 次查询的叠加态中 $\ket{x}$ 的振幅平方，即 $q_x(\ket{\phi_t}) = \sum_{y} \lvert \alpha_{x, y} \rvert^2$，称为 $x$ 的查询幅度，定义 $q_x = \sum_t q_x(\ket{\phi_t})$ 为 $x$ 的总查询幅度. 对任意一个集合 $S$，定义 $q_S = \sum_{x \in S} q_x$ 为集合 $S$ 的总查询幅度.

!!!+ lemma
    设 $\lVert \ket{\psi} - \ket{\phi} \rVert_2 \leq \varepsilon$，那么对 $\ket{\psi}$ 和 $\ket{\phi}$ 执行同一个测量所得到的分布的统计距离至多为 $4 \varepsilon$.

!!!+ lemma
    设 $\mathcal{A}$ 是对谕示机 $\mathcal{O}$ 进行 $T$ 次查询的量子算法. 设 $\varepsilon > 0$，集合 $S$ 满足 $q_S \leq \varepsilon$，$\mathcal{O}'$ 与 $\mathcal{O}$ 在 $S$ 之外的点上都是一致的. 令 $p = \op{Pr}[\mathcal{A}^{\mathcal{O}} (\cdot) = 1]$，$p' = \op{Pr}[\mathcal{A}^{\mathcal{O}'} (\cdot) = 1]$，则 $\lvert p - p' \rvert \leq O(\sqrt{T \varepsilon})$.

设 $\mathcal{O}_\ket{\psi}$ 关于 $\ket{\psi} 做反射的谕示机，等价地，也可以将其视为一个投影到 $\ket{\psi}$ 上的谕示机.

!!!+ lemma
    存在一个有状态的模拟机 $\mathcal{S}$，可以使用 $\ket{\psi}$ 的若干拷贝近似模拟 $\mathcal{O}_\ket{\psi}$. 对于任意状态 $\ket{\psi}$ 以及任意进行 $q$ 次查询的量子算法 $\mathcal{A}$，
    
    \[
        \lVert \op{Pr}[\mathcal{A}^{\mathcal{O}_\ket{\psi}} (\cdot) = 1] - \op{Pr}[\mathcal{A}^{\mathcal{S}(\ket{\psi}^l)} (\cdot) = 1] \rVert \leq O(q / \sqrt{l}).
    \]

!!!+ lemma
    设 $\ket{\psi} 和 $\ket{\phi}$ 是两个 $n$ 个量子比特的相互独立的 Haar 随机态，那么有

    \[
        \lVert \mathbb{E}[(\ket{\psi} \bra{\psi})^{\otimes t} \otimes (\ket{\psi^*} \bra{\psi^*})^{\otimes u}] - \mathbb{E}[(\ket{\psi} \bra{\psi})^{\otimes t}] \otimes \mathbb{E}[(\ket{\phi} \bra{\phi})^{\otimes u}] \rVert \leq \frac{3(t + u)^2}{2^n}.
    \]

    ???+ success "Proof"
        令 $\rho_0$ 为对 $\ket{\psi}^{\otimes t} \ket{\psi^*}^{\otimes u}$ 取平均得到的密度矩阵. $P$ 为投影到计算基态 $\ket{x_1，\ldots, x_{t+u}}$ 上的投影算子，其中 $\forall i \neq j, x_i \neq x_j$. $\rho_1 = P \rho_0 P / \mathsf{Tr}(P \rho_0 P)$ 为重新归一化后的密度矩阵. 

        首先计算 $\mathsf{Tr}(P \rho_0 P)$，其等于在计算基下测量 $\rho_0$，若所有测量结果都不同则接受的概率. 如果将 $\ket{\psi}$ 展开

        \[
            \ket{\psi} = \sum_x \alpha_x \ket{x},
        \]

        那么得到特定结果 $(x_1, \ldots, x_{t+u})$ 的概率为 $\prod_i \lvert \alpha_{x_i} \rvert^2$. 这就和收到 $t + u$ 份 $\ket{\psi}$ 的拷贝并测量它们的结果相同. 这 $t + u$ 份拷贝构成了对称子空间上的完全混合态，该子空间由标记为包含 $t + u$ 个元素的无序多重集的向量张成. 这样的多重集总数为 $\binom{2^n + t + u - 1}{t + u}$，而所有元素都不同的多重集总数为 $\binom{2^n}{t + u}$，所以得到所有元素都不同的概率为

        \begin{align*}
            \frac{\binom{2^n}{t + u}}{\binom{2^n + t + u - 1}{t + u}} &= \frac{2^n! (2^n - 1)!}{(2^n - t - u)! (2^n + t + u - 1)!} \\
            &= \left( \frac{2^n}{2^n + t + u - 1} \right) \left( \frac{2^n - 1}{2^n + t + u - 2} \right) \cdots \left( \frac{2^n - t - u + 1}{2^n} \right) \\
            &= \left(1 + \frac{t + u - 1}{2^n} \right)^{-1} \cdots \left(1 + \frac{t + u - 1}{2^n - t - u + 1} \right)^{-1} \\
            &\geq \left(1 + \frac{t + u - 1}{2^n - t - u + 1} \right)^{-(t + u)} \\
            &\geq \left(1 - \frac{t + u - 1}{2^n - t - u + 1} \right)^{t + u} \\
            &\geq 1 - \frac{(t + u)(t + u - 1)}{2^n - t - u + 1} \\
            &\geq 1 - \frac{2}{3} \frac{(t + u)^2}{2^n}.
        \end{align*}

        以上放缩在 $t + u \leq 2^n/3$ 的情况下成立. 因为 $\mathsf{Tr}(P \rho_0 P) \geq 1 - \frac{2}{3} \frac{(t + u)^2}{2^n}$，所以 $\lVert \rho_0 - \rho_1 \rVert_\mathsf{Tr} = 1 - \mathsf{Tr}(P \rho_0 P) \leq \frac{2}{3} \frac{(t + u)^2}{2^n}$.

        设 $\rho_3$ 为对 $\ket{\psi}^{\otimes t} \ket{\phi}^{\otimes u}$ 取平均得到的密度矩阵. $\rho_2 = P \rho_3 P / \mathsf{Tr}(P \rho_3 P)$ 为重新归一化后的密度矩阵. 类似地可以得到 $\lVert \rho_2 - \rho_3 \rVert_\mathsf{Tr} \leq \frac{3}{2} \frac{t^2 + u^2}{2^n} \leq \frac{3}{2} \frac{(t + u)^2}{2^n}$.

        现在考虑 $\lVert \rho_1 - \rho_2 \rVert$