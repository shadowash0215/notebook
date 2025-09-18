# Distance measures for quantum information

## Distance measures for classical information

Hamming distance: 本质依赖于标签的设定，而对于 Hilbert Space 不存在先天的标签设定.

更好的起点是比较经典的概率分布，总共有两种方式. 第一种是迹距离（trace distance）：

!!! info "Definition(trace distance)"
    设 $\{p_x\}$ 和 $\{q_x\}$ 是在指标集 $X$ 上的两个概率分布，则它们的迹距离定义为

    \[
        D(\{p_x\}, \{q_x\}) = \frac{1}{2} \sum_{x \in X} \lvert p_x - q_x \rvert.
    \]

    这也被称为 $L_1$ 距离或 Kolmogorov 距离. 迹距离也是概率分布上的度量，因为其满足对称性和三角不等式.

第二种是保真度（fidelity）：

!!! info "Definition(fidelity)"
    设 $\{p_x\}$ 和 $\{q_x\}$ 是在指标集 $X$ 上的两个概率分布，则它们的保真度定义为

    \[
        F(\{p_x\}, \{q_x\}) = \sum_{x \in X} \sqrt{p_x q_x}.
    \]

    其显然不是度量. 可以通过球面上的向量 $(\sqrt{p_x})_{x \in X}$ 和 $(\sqrt{q_x})_{x \in X}$ 的内积来理解保真度. 

迹距离可以被证明满足如下的性质：

\[
    D_{p_x, q_x} = \max_S \lvert p(S) - q(S) \rvert = \max_S \lvert \sum_{x \in S} p_x - \sum_{x \in S} q_x \rvert.
\]

其中最大化遍历指标集 $\{x\}$ 的所有子集 $S$，被最大化的量为事件 $S$ 在分布 $\{p_x\}$ 下的发生概率和在分布 $\{q_x\}$ 下的发生概率之差的绝对值. 因此，事件 $S$ 本质上是区分分布 $\{p_x\}$ 和 $\{q_x\}$ 的最优检测事件，而迹距离决定了这种区分的最大可能程度.

遗憾的是，对于保真度而言，尚未发现类似迹距离的清晰物理操作解释. 然而，保真度在数学分析中具有充分的应用价值，即使缺乏明确的物理解释，其研究意义依然重大. 此外，我们无法排除未来可能发现保真度新解释的可能性. 最后需要强调的是：保真度与迹距离存在深刻联系，二者的性质常可相互推导，这一事实在实际应用中往往带来意外价值. 

迹距离和保真度是用于比较固定概率分布的静态距离度量. 还存在第三种距离概念：动态距离度量，它通过物理过程的信息保真度来评估距离. 假设随机变量 $X$ 通过噪声信道传输后输出随机变量 $Y$，形成马尔可夫过程 $X \to Y$. 为简化，假定 $X$ 和 $Y$ 取值于同一集合 $\{x\}$. 此时，输出与输入不相等的概率 $p(X \neq Y)$ 是衡量信息在过程中保留程度的一个直观且重要的指标.

动态距离可以被视作静态迹距离的一个特例. 给定一个随机变量 $X$，首先创建一个新的随机变量 $\hat{X} = X$，而后将 $X$ 通过噪声信道传输得到 $Y$，那么 $(\hat{X}, X)$ 和 $(\hat{X}, Y)$ 有多接近呢？可以通过计算它们的迹距离来回答这个问题：

\begin{align*}
    D((\hat{X}, X), (\hat{X}, Y)) & = \frac{1}{2} \sum_{x, x'} \lvert \delta_{x, x'}p(X = x) - p(\hat{X} = x, Y = x') \rvert \\
                                  & = \frac{1}{2} \sum_{x \neq x'} p(\hat{X} = x, Y = x') + \frac{1}{2} \sum_{x = x'} \lvert p(X = x) - p(\hat{X} = x, Y = x) \rvert \\
                                  & = \frac{1}{2} \sum_{x \neq x'} p(\hat{X} = x, Y = x') + \frac{1}{2} \sum_{x} (p(X = x) - p(\hat{X} = x, Y = x)) \\
                                  & = \frac{1}{2} (p(\hat{X} \neq Y) + 1 - p(\hat{X} = Y)) \\
                                  & = \frac{1}{2} (p(\hat{X} \neq Y) + p(\hat{X} = Y)) \\
                                  & = p(\hat{X} \neq Y).
\end{align*}

因此信道错误概率等于关联对 $(\hat{X}, X)$ 和 $(\hat{X}, Y)$ 的迹距离. 其将作为量子类比的基础，因为量子力学中不存在类似 $p(X \neq Y)$ 的概念（量子态无不同时间的联合分布）. 取而代之，可以采用以上的构造方法，将量子纠缠作为量子信道动态过程中需保护的核心要素.

## How close are two quantum states?

### Trace distance

首先定义量子态的迹距离：

!!! info "Definition(trace distance)"
    设 $\rho$ 和 $\sigma$ 是两个量子态，则它们的迹距离定义为

    \[
        D(\rho, \sigma) = \frac{1}{2} \op{Tr} \lvert \rho - \sigma \rvert.
    \]

    定义 $\lvert A \rvert = \sqrt{A^\dagger A}$ 为 $A^\dagger A$ 的正平方根.

注意到量子迹距离实际上是经典迹距离的推广，如果 $\rho$ 和 $\sigma$ 是可交换的，那么 $\rho$ 和 $\sigma$ 的迹距离等于它们的特征值之间的迹距离. 因为 $\rho$ 和 $\sigma$ 可交换，所以它们可以在同一组基下对角化，设存在正交基 $\{\ket{i}\}$ 使得 $\rho$ 和 $\sigma$ 的对角形式为

\[
    \rho = \sum_i r_i \ket{i} \bra{i}, \quad \sigma = \sum_i s_i \ket{i} \bra{i},
\]

那么

\[
    D(\rho, \sigma) = \frac{1}{2} \op{Tr} \left\lvert \sum_i (r_i - s_i) \ket{i} \bra{i} \right\rvert = D(\{r_i\}, \{s_i\}).
\]

假定 $\rho$ 和 $\sigma$ 的 Bloch 向量分别为 $\vec{r}$ 和 $\vec{s}$，即

\[
    \rho = \frac{1}{2} (I + \vec{r} \cdot \vec{\sigma}), \quad \sigma = \frac{1}{2} (I + \vec{s} \cdot \vec{\sigma}),
\]

那么 $\rho$ 和 $\sigma$ 的迹距离可以被写为

\[
    D(\rho, \sigma) = \frac{1}{4} \op{Tr} \left\lvert (\vec{r} - \vec{s}) \cdot \vec{\sigma} \right\rvert.
\]

$(\vec{r} - \vec{s}) \cdot \vec{\sigma}$ 的特征值为 $\pm \lvert \vec{r} - \vec{s} \rvert$，所以迹为 $2\lvert \vec{r} - \vec{s} \rvert$，因此

\[
    D(\rho, \sigma) = \frac{1}{2} \lvert \vec{r} - \vec{s} \rvert.
\]

也就是说，两个单量子比特之间的距离是其 Bloch 向量之间的距离的一半. 因而，某些 Bloch 球上距离性质可以类比到迹距离上，如 Bloch 球的旋转不改变距离，那么很自然的联想到迹距离在酉操作下不变，即

\[
    D(U \rho U^\dagger, U \sigma U^\dagger) = D(\rho, \sigma).
\]

为了更好地了解量子迹距离，首先证明一个经典迹距离的等价式的推广：

\[
    D(\rho, \sigma) = \max_{P} \op{Tr} \lvert (P(\rho - \sigma)) \rvert,
\]

其中最大化遍历了所有的投影算子 $P$，或所有正算子 $P \leq I$. 因为 POVM 的元素都是满足 $P \leq I$ 的正算子，所以迹距离相当于同一 POVM 元素 $P$ 在量子态 $\rho$ 和 $\sigma$ 上出现概率的最大值，即最优量子测量下的可区分度.

!!! note "exercise"
    证明对任意量子态 $\rho$ 和 $\sigma$，可将 $\rho - \sigma$ 分解为 $Q - S$，其中 $Q$ 和 $S$ 是正算子，并且 $Q$ 和 $S$ 的支撑空间正交. 

    ???+ note "Proof"
        设 $A = \rho - \sigma$，因为 $\rho$ 和 $\sigma$ 都是密度算子，所以 $A$ 是自伴算子，依据谱定理，存在酉算子 $U$ 和对角矩阵 $D$ 使得

        \[
            A = U D U^\dagger,
        \]

        其中 $D = \op{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$，$\lambda_i \in \mathbb{R}$ 是 $A$ 的特征值. 

        将 $D$ 分解为 $D = D_+ - D_-$，其中 $D_+ = \op{diag}(\max(\lambda_i, 0))$ 和 $D_- = \op{diag}(\max(-\lambda_i, 0))$，$D_+$ 和 $D_-$ 都是正算子，并且 $D_+ D_- = 0$.

        定义 $Q = U D_+ U^\dagger$ 和 $S = U D_- U^\dagger$，则 $Q$ 和 $S$ 都是正算子，并且 $Q - S = A$. 因为 $D_+ D_- = 0$，所以

        \[
            Q S = (U D_+ U^\dagger)(U D_- U^\dagger) = U D_+ D_- U^\dagger = 0,
        \]

        从而 $Q$ 和 $S$ 的支撑空间正交.

下面证明 $\lvert \rho - \sigma \rvert = Q + S$. 设 $A = \rho - \sigma$，则 

\[
    A^2 = (Q - S)^2 = Q^2 - QS - SQ + S^2 = Q^2 + S^2,
\]

而 $A$ 是自伴算子，有

\[
    \lvert A \rvert = \sqrt{A^\dagger A} = \sqrt{A^2} = \sqrt{Q^2 + S^2}.
\]

因为 $Q$ 和 $S$ 的支撑空间正交，所以存在一组标准正交基 $\{\ket{i}\}$ 使得

\[
    Q = \sum_i q_i \ket{i} \bra{i}, \quad S = \sum_i s_i \ket{i} \bra{i},
\]

代入得到 $\lvert A \rvert = \sum_i \sqrt{q_i^2 + s_i^2} \ket{i} \bra{i}$，并且因为 $q_i s_i = 0$，所以

- 若 $q_i > 0$，则 $s_i = 0$，因此 $\sqrt{q_i^2 + s_i^2} = q_i$；
- 若 $s_i > 0$，则 $q_i = 0$，因此 $\sqrt{q_i^2 + s_i^2} = s_i$；
- 若 $q_i = s_i = 0$，则 $\sqrt{q_i^2 + s_i^2} = 0$.

也就有 $\lvert \rho - \sigma \rvert =  \lvert A \rvert = \sum_i (q_i + s_i) \ket{i} \bra{i} = Q + S$.

进而 $D(\rho, \sigma) = \frac{1}{2} (\op{Tr} Q + \op{Tr} S)$. 而因为 $\op{Tr} (\rho - \sigma) = \op{Tr} (Q - S) = 0$，所以 $\op{Tr} Q = \op{Tr} S$，也就有 $D(\rho, \sigma) = \op{Tr} Q = \op{Tr} S$.

设 $P$ 是 $Q$ 的支撑空间上的投影算子，那么

\[
    \op{Tr} (P(\rho - \sigma)) = \op{Tr} (P(Q - S)) = \op{Tr} Q = D(\rho, \sigma).
\]

而如果 $P$ 是任意投影算子，那么

\[
    \op{Tr} (P(\rho - \sigma)) = \op{Tr} (P(Q - S)) \leq \op{Tr} (PQ) \leq \op{Tr} Q = D(\rho, \sigma).
\]

得证.

!!! note "Theorem"
    设 $\{E_m\}$ 为一个 POVM，其中 $p_m \equiv \op{Tr} (\rho E_m)$ 和 $q_m \equiv \op{Tr} (\sigma E_m)$ 分别是量子态 $\rho$ 和 $\sigma$ 下得到结果 $m$ 的概率，则

    \[
        D(\rho, \sigma) = \max_{\{E_m\}} D(\{p_m\}, \{q_m\}).
    \]

    其中最大化遍历所有的 POVM $\{E_m\}$.

    ???+ note "Proof"
        注意到

        \[
            D(\{p_m\}, \{q_m\}) = \frac{1}{2} \sum_m \lvert \op{Tr} (E_m (\rho - \sigma)) \rvert.
        \]

        应用先前的谱分解有 $\rho - \sigma = Q - S$，且 $\lvert \rho - \sigma \rvert = Q + S$，因此

        \begin{align*}
            \lvert \op{Tr} (E_m (\rho - \sigma)) \rvert & = \lvert \op{Tr} (E_m Q) - \op{Tr} (E_m S) \rvert \\
                                                        & \leq \op{Tr} (E_m Q) + \op{Tr} (E_m S) \\
                                                        & = \op{Tr} (E_m (Q + S)) \\
                                                        & = \op{Tr} (E_m \lvert \rho - \sigma \rvert).
        \end{align*}

        因而有

        \begin{align*}
            D(\{p_m\}, \{q_m\}) & = \frac{1}{2} \sum_m \lvert \op{Tr} (E_m (\rho - \sigma)) \rvert \\
                                & \leq \frac{1}{2} \sum_m \op{Tr} (E_m \lvert \rho - \sigma \rvert) \\
                                & = \frac{1}{2} \op{Tr} \left(\lvert \rho - \sigma \rvert \sum_m E_m \right) \\
                                & = \frac{1}{2} \op{Tr} \left(\lvert \rho - \sigma \rvert \cdot I \right) \\
                                & = D(\rho, \sigma).
        \end{align*}

        而另一个方向上，只需构造投影到 $Q$ 和 $S$ 的投影算子 $P_Q$ 和 $P_S$，则有 $D(\rho, \sigma) = D(\{p_m\}, \{q_m\})$.

因此，若两个密度算子在迹距离下接近，则对这两个量子态执行的任何测量所产生的概率分布，在经典迹距离意义下也是接近的. 这给出了量子态间迹距离的第二种解释：它是通过量子态测量所得概率分布之间迹距离的可达到上界. 

接下来证明迹距离的三角不等式，注意到存在投影算子 $P$ 使得 $D(\rho, \sigma) = \op{Tr} (P (\rho - \sigma))$，因此

\begin{align*}
    D(\rho, \sigma) & = \op{Tr} (P (\rho - \sigma)) \\
                    & = \op{Tr} (P (\rho - \tau + \tau - \sigma)) \\
                    & = \op{Tr} (P (\rho - \tau)) + \op{Tr} (P (\tau - \sigma)) \\
                    & \leq D(\rho, \tau) + D(\tau, \sigma).
\end{align*}

!!! note "Theorem(Trace-preserving quantum operations are contractive)"
    设 $\mathcal{E}$ 是一个迹保持的量子操作，则对任意密度算子 $\rho$ 和 $\sigma$，有

    \[
        D(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \leq D(\rho, \sigma).
    \]

    ???+ note "Proof"
        应用谱分解 $\rho - \sigma = Q - S$，设 $P$ 为满足 $D(\mathcal{E}(\rho), \mathcal{E}(\sigma)) = \op{Tr} (P (\mathcal{E}(\rho) - \mathcal{E}(\sigma)))$ 的投影算子. 因为 $\op{Tr} Q - \op{Tr} S = \op{Tr} (\rho - \sigma) = 0$，所以 $\op{Tr} Q = \op{Tr} S$，$\op{Tr} (\mathcal{E}(Q)) = \op{Tr} (\mathcal{E}(S))$，因此

        \begin{align*}
            D(\rho, \sigma) & = \frac{1}{2} \op{Tr} \lvert \rho - \sigma \rvert \\
                            & = \frac{1}{2} \op{Tr} (Q + S) \\
                            & = \frac{1}{2} \op{Tr} Q + \frac{1}{2} \op{Tr} S \\
                            & = \frac{1}{2} \op{Tr} \mathcal{E}(Q) + \frac{1}{2} \op{Tr} \mathcal{E}(S) \\
                            & = \op{Tr} \mathcal{E}(Q) \\
                            & \geq \op{Tr} (P (\mathcal{E}(Q))) \\
                            & \geq \op{Tr} (P (\mathcal{E}(Q) - \mathcal{E}(S))) \\
                            & = \op{Tr} (P (\mathcal{E}(\rho) - \mathcal{E}(\sigma))) \\
                            & = D(\mathcal{E}(\rho), \mathcal{E}(\sigma)).
        \end{align*}

!!! note "Theorem(Strong convexity of the trace distance)"
    设 $\{p_i\}$ 和 $\{q_i\}$ 是两个同一指标集上的概率分布，$\rho_i$ 和 $\sigma_i$ 是同一指标集下的密度算子，则

    \[
        D(\sum_i p_i \rho_i, \sum_i q_i \sigma_i) \leq D(\{p_i\}, \{q_i\}) + \sum_i p_i D(\rho_i, \sigma_i),
    \]

    其中 $D(\{p_i\}, \{q_i\})$ 是经典迹距离.

    ???+ note "Proof"
        存在投影算子 $P$ 使得

        \begin{align*}
            D(\sum_i p_i \rho_i, \sum_i q_i \sigma_i) & = \op{Tr} (P (\sum_i p_i \rho_i - \sum_i q_i \sigma_i)) \\
                                                      & = \sum_i p_i \op{Tr} (P (\rho_i - \sigma_i)) + \sum_i (p_i - q_i) \op{Tr} (P \sigma_i) \\
                                                      & \leq \sum_i p_i D(\rho_i, \sigma_i) + D(\{p_i\}, \{q_i\}).
        \end{align*}

### Fidelity

接下来定义量子态的保真度：

!!! info "Definition(fidelity)"
    设 $\rho$ 和 $\sigma$ 是两个量子态，则它们的保真度定义为

    \[
        F(\rho, \sigma) = \op{Tr} \sqrt{\rho^{1/2} \sigma \rho^{1/2}}.
    \]

初看这不是衡量 $\rho$ 和 $\sigma$ 之间距离的直观方法，因为其看起来似乎不满足对称性，但接下来将证明保真度满足对称性，并且具备诸多优秀度量所具有的性质.

在两种特例下，保真度可以得到简化. 一是 $\sigma$ 和 $\rho$ 可交换，即可以在同一组标准正交基下对角化：

\[
    \rho = \sum_i r_i \ket{i} \bra{i}, \quad \sigma = \sum_i s_i \ket{i} \bra{i}.
\]

那么保真度为

\begin{align*}
    F(\rho, \sigma) & = \op{Tr} \sqrt{\sum_i r_i s_i \ket{i} \bra{i}} \\
                    & = \op{Tr} \left(\sum_i \sqrt{r_i s_i} \ket{i} \bra{i}\right) \\
                    & = \sum_i \sqrt{r_i s_i} \\
                    & = F(\{r_i\}, \{s_i\}).
\end{align*}

即当 $\sigma$ 和 $\rho$ 可交换时，量子保真度退化为其特征值分布的经典保真度.

二是纯态和任意态的情况，代入计算有

\begin{align*}
    F(\ket{\psi}, \rho) & = \op{Tr} \sqrt{\sqrt{\ket{\psi} \bra{\psi}} \rho \sqrt{\ket{\psi} \bra{\psi}}} \\
                        & = \op{Tr} \sqrt{\ket{\psi} \bra{\psi} \rho \ket{\psi} \bra{\psi}} \\
                        & = \op{Tr} \sqrt{\bra{\psi} \rho \ket{\psi} \ket{\psi} \bra{\psi}} \\
                        & = \op{Tr} \left(\sqrt{\bra{\psi} \rho \ket{\psi}} \ket{\psi} \bra{\psi}\right) \\
                        & = \sqrt{\bra{\psi} \rho \ket{\psi}}.
\end{align*}

所以保真度为 $\ket{\psi}$ 和 $\rho$ 的重叠度的平方根. 

!!! note "Theorem(Uhlmann's theorem)"
    设 $\rho$ 和 $\sigma$ 是量子系统 $Q$ 的两个量子态，引入 $R$ 为 $Q$ 的一个副本，则

    \[
        F(\rho, \sigma) = \max_{\ket{\psi}, \ket{\varphi}} \lvert \bra{\psi} \ket{\varphi} \rvert,
    \]

    其中最大化遍历 $\rho$ 在 $RQ$ 中的所有纯化态 $\ket{\psi}$ 和 $\sigma$ 在 $RQ$ 中的所有纯化态 $\ket{\varphi}$.

    !!! success "Lemma"
        设 $A$ 为任意算子，$U$ 为酉算子，则

        \[
            \lvert \op{Tr} (A U) \rvert \leq \op{Tr} \lvert A \rvert,
        \]

        当 $U = V^\dagger$ 时等号成立，其中 $A = \lvert A \rvert V$ 是 $A$ 的极分解.

        ??? success "Proof"
            等号成立条件是显然正确的. 观察到

            \[
                \lvert \op{Tr} (A U) \rvert = \lvert \op{Tr} (\lvert A \rvert V U) \rvert = \lvert \op{Tr} (\lvert A \rvert^{1/2} \cdot (\lvert A \rvert^{1/2} V U)) \rvert.
            \]

            依据 Cauchy-Schwarz 不等式，有

            \[
                \lvert \op{Tr} (A U) \rvert \leq \sqrt{\op{Tr} \lvert A \rvert \cdot \op{Tr} (U^\dagger V^\dagger \lvert A \rvert V U)} = \op{Tr} \lvert A \rvert.
            \]

    ???+ note "Proof"
        固定系统 $R$ 和 $Q$ 的标准正交基 $\{\ket{i}\}_R$ 和 $\{\ket{i}\}_Q$. 定义 $\ket{m} = \sum_i \ket{i}_R \ket{i}_Q$，$\ket{\psi}$ 为 $\rho$ 的任意纯化，依据 Schmidt 分解，可以得到

        \[
            \ket{\psi} = (U_R \otimes \sqrt{\rho} U_Q) \ket{m}.
        \]

        同理 $\ket{\varphi}$ 为 $\sigma$ 的任意纯化，可以得到

        \[
            \ket{\varphi} = (V_R \otimes \sqrt{\sigma} V_Q) \ket{m}.
        \]

        计算内积有

        \[
            \lvert \innerproduct{\psi}{\varphi} \rvert = \lvert \bra{m} (U_R^\dagger V_R \otimes U_Q^\dagger \sqrt{\rho} \sqrt{\sigma} V_Q) \ket{m} \rvert.
        \]

        !!! note "exercise"
            设量子系统 $R$ 和 $Q$ 具有相同的 Hilbert 空间，$\{\ket{i_R}\}$ 和 $\{\ket{i_Q}\}$ 分别是 $R$ 和 $Q$ 的标准正交基，定义 $\ket{m} = \sum_i \ket{i_R} \ket{i_Q}$，若 $A$ 和 $B$ 分别是系统 $R$ 和 $Q$ 的算子，其矩阵表示分别相应于基 $\{\ket{i_R}\}$ 和 $\{\ket{i_Q}\}$，证明：

            \[
                \op{Tr} (A^\mathrm{T} B) = \bra{m} (A \otimes B) \ket{m}.
            \]

        从而有

        \[
            \lvert \innerproduct{\psi}{\varphi} \rvert = \lvert \op{Tr} (V_R^\mathrm{T} \overline{U_R} U_Q^\dagger \sqrt{\rho} \sqrt{\sigma} V_Q) \rvert.
        \]

        定义 $U = V_Q V_R^\mathrm{T} \overline{U_R} U_Q^\dagger$，则有

        \[
            \lvert \innerproduct{\psi}{\varphi} \rvert = \lvert \op{Tr} (\sqrt{\rho} \sqrt{\sigma} U) \rvert.
        \]

        依据引理，得到

        \[
            \lvert \innerproduct{\psi}{\varphi} \rvert \leq \op{Tr} \lvert \sqrt{\rho} \sqrt{\sigma} \rvert = \op{Tr} \sqrt{\rho^{1/2} \sigma \rho^{1/2}}.
        \]

        设 $\sqrt{\rho} \sqrt{\sigma} = \lvert \sqrt{\rho} \sqrt{\sigma} \rvert V$ 是 $\sqrt{\rho} \sqrt{\sigma}$ 的极分解，令 $U_Q = U_R = V_R = I$，$V_Q = V^\dagger$，则等号成立. 

Uhlmann 公式在证明保真度的性质时更有优势. 比如很显然地能够得到保真度的对称性，以及 $0 \leq F(\rho, \sigma) \leq 1$，第一个等号成立当且仅当 $\rho$ 和 $\sigma$ 的支撑空间正交，第二个等号成立当且仅当 $\rho = \sigma$.

我们已通过测量诱导的概率分布将量子迹距离与经典迹距离关联. 类似地，可证明：

\[
    F(\rho, \sigma) = \min_{\{E_m\}} F(\{p_m\}, \{q_m\}),
\]

其中最小化遍历所有 POVM $\{E_m\}$，$p_m = \op{Tr} (\rho E_m)$ 和 $q_m = \op{Tr} (\sigma E_m)$ 分别是量子态 $\rho$ 和 $\sigma$ 下得到结果 $m$ 的概率.

证明运用极分解 $\sqrt{\rho^{1/2} \sigma \rho^{1/2}} = \sqrt{\rho} \sqrt{\sigma} U$，其中 $U$ 是酉算子，得到

\begin{align*}
    F(\rho, \sigma) & = \op{Tr} \sqrt{\rho^{1/2} \sigma \rho^{1/2}} \\
                    & = \op{Tr} (\sqrt{\rho} \sqrt{\sigma} U) \\
                    & = \sum_m \op{Tr} (\sqrt{\rho} \sqrt{E_m} \sqrt{E_m} \sqrt{\sigma} U) \\
                    & \leq \sum_m \sqrt{\op{Tr} (\rho E_m) \op{Tr} (\sigma E_m)} \\
                    & = F(\{p_m\}, \{q_m\}).
\end{align*}

从而得到

\[
    F(\rho, \sigma) \leq \min_{\{E_m\}} F(\{p_m\}, \{q_m\}).
\]

为了证明等号成立需要找到一个 POVM $\{E_m\}$ 使得 Cauchy-Schwarz 不等式的等号成立，即 $\sqrt{E_m} \sqrt{\rho} = \alpha_m \sqrt{E_m} \sqrt{\sigma} U$，其中 $\alpha_m$ 是复数. 又因为 $\sqrt{\rho} \sqrt{\sigma} U = \sqrt{\rho^{1/2} \sigma \rho^{1/2}}$，所以对于可逆的 $\rho$，有

\[
    \sqrt{\sigma} U = \rho^{-1/2} \sqrt{\rho^{1/2} \sigma \rho^{1/2}}.
\]

通过代换可以得到取等条件为

\[
    \sqrt{E_m} (I - \alpha_m M) = 0,
\]

其中 $M = \rho^{-1/2} \sqrt{\rho^{1/2} \sigma \rho^{1/2}} \rho^{-1/2}$. 若 $M = \sum_m \beta_m \ket{m} \bra{m}$ 是 $M$ 的谱分解，那么令 $E_m = \ket{m} \bra{m}$，$\alpha_m = 1/\beta_m$ 即可. $\rho$ 不可逆的情况可以通过连续性证明.

先前证明了迹距离的三个重要性质：度量性、收缩性和强凸性. 保真度也具有类似的性质，且其证明技术与迹距离的证明截然不同，因此有必要详细探讨这些结果.

保真度本身不是度量，但可通过简单变换转化为度量，核心思想是球面上两点的夹角是度量. 在量子情形下，Uhlmann 定理指出两态的保真度等于其纯化态间最大内积，这边启发我们定义态 $\rho$ 和 $\sigma$ 的夹角为

\[
    A(\rho, \sigma) = \arccos F(\rho, \sigma).
\]

显然其满足对称性，非负性，并且当且仅当 $\rho = \sigma$ 时等号成立. 接下来只需要证明其满足三角不等式，便能证明其是度量. 设 $\ket{\varphi}$ 是 $\sigma$ 的纯化态，并且选择 $\rho$ 的纯化态 $\ket{\psi}$ 和 $\tau$ 的纯化态 $\ket{\gamma}$ 使得

\begin{gather*}
    F(\rho, \sigma) = \innerproduct{\psi}{\varphi}, \\
    F(\sigma, \tau) = \innerproduct{\varphi}{\gamma}, 
\end{gather*}

并且 $\innerproduct{\psi}{\gamma}$ 是正的. 依据球面上夹角的三角不等式，有

\[
    \arccos (\innerproduct{\psi}{\varphi}) \leq A(\rho, \sigma) + A(\sigma, \tau).
\]

根据 Uhlmann 定理，$F(\rho, \tau) \geq \innerproduct{\psi}{\gamma}$，因此 $A(\rho, \tau) \leq \arccos (\innerproduct{\psi}{\gamma}) \leq A(\rho, \sigma) + A(\sigma, \tau)$，从而证明了三角不等式.

定性来看，保真度的行为与迹距离相反. 所以不应该期望保真度具有迹距离的收缩性，而应该是具有某种不减的性质. 这称为保真度的单调性（monotonicity）：

!!! note "Theorem(Monotonicity of fidelity)"
    设 $\mathcal{E}$ 是一个保迹的量子操作，则对任意密度算子 $\rho$ 和 $\sigma$，有

    \[
        F(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \geq F(\rho, \sigma).
    \]

    ???+ note "Proof"
        设 $\ket{\psi}$ 和 $\ket{\varphi}$ 分别是 $\rho$ 和 $\sigma$ 在系统 $RQ$ 上的纯化态，并且使得 $F(\rho, \sigma) = \lvert \innerproduct{\psi}{\varphi} \rvert$. 为量子操作 $\mathcal{E}$ 引入环境系统 $E$，初始态为纯态 $\ket{0}_E$，并且通过酉相互作用 $U$ 与量子系统 $Q$ 耦合. 注意到 $U \ket{\psi} \ket{0}_E$ 和 $U \ket{\varphi} \ket{0}_E$ 分别是 $\mathcal{E}(\rho)$ 和 $\mathcal{E}(\sigma)$ 的纯化态. 依据 Uhlmann 定理，有

        \begin{align*}
            F(\mathcal{E}(\rho), \mathcal{E}(\sigma)) & \geq \lvert \bra{\psi} \bra{0}_E U^\dagger U \ket{\varphi} \ket{0}_E \rvert \\
                                                      & = \lvert \innerproduct{\psi}{\varphi} \rvert \\
                                                      & = F(\rho, \sigma).
        \end{align*}

通过 Uhlmann 定理证明保真度的强凹性，完成对保真度基本性质的讨论.

!!! note "Theorem(Strong concavity of the fidelity)"
    设 $\{p_i\}$ 和 $\{q_i\}$ 是同一指标集上的概率分布，$\rho_i$ 和 $\sigma_i$ 是同一指标集下的密度算子，则

    \[
        F(\sum_i p_i \rho_i, \sum_i q_i \sigma_i) \geq \sum_i \sqrt{p_i q_i} F(\rho_i, \sigma_i),
    \]

    此结论可用于证明保真度的凹性，因此称为保真度的强凹性. 该性质虽与迹距离的强凸性不完全类比，但思想相似，故采用类似术语.

    ???+ note "Proof"
        设 $\ket{\psi}_i$ 和 $\ket{\varphi}_i$ 分别是 $\rho_i$ 和 $\sigma_i$ 的纯化态，且满足 $F(\rho_i, \sigma_i) = \innerproduct{\psi_i}{\varphi_i}$. 引入辅助系统，其标准正交基 $\ket{i}$ 对应于概率分布的指标集. 定义

        \[
            \ket{\psi} = \sum_i \sqrt{p_i} \ket{\psi_i} \ket{i} , \quad \ket{\varphi} = \sum_i \sqrt{q_i} \ket{\varphi_i} \ket{i}.
        \]

        所以 $\ket{\psi}$ 和 $\ket{\varphi}$ 分别是 $\sum_i p_i \rho_i$ 和 $\sum_i q_i \sigma_i$ 的纯化态. 依据 Uhlmann 定理，有

        \begin{align*}
            F(\sum_i p_i \rho_i, \sum_i q_i \sigma_i) & \geq \lvert \innerproduct{\psi}{\varphi} \rvert \\
                                                      & = \sum_i \sqrt{p_i q_i} \innerproduct{\psi_i}{\varphi_i} \\
                                                      & = \sum_i \sqrt{p_i q_i} F(\rho_i, \sigma_i).
        \end{align*}

### Relationships between distance measures

对于纯态而言，迹距离和保真度是等同的. 考虑两个纯态 $\ket{a}$ 和 $\ket{b}$，利用 Gram-Schmidt 正交化可以得到一组正交基 $\ket{0}$ 和 $\ket{1}$，使得

\[
    \ket{a} = \ket{0}, \quad \ket{b} = \cos \theta \ket{0} + \sin \theta \ket{1},
\]

注意 $F(\ket{a}, \ket{b}) = \lvert \cos \theta \rvert$. 而

\begin{align*}
    D(\ket{a}, \ket{b}) & = \frac{1}{2} \op{Tr} \left\lvert \begin{pmatrix}
        1 - \cos^2 \theta & -\cos \theta \sin \theta \\
        -\cos \theta \sin \theta & \sin^2 \theta
    \end{pmatrix} \right\rvert \\
                        & = \lvert \sin \theta \rvert \\
                        & = \sqrt{1 - F(\ket{a}, \ket{b})^2}.
\end{align*}

进而考虑任意两个量子态 $\rho$ 和 $\sigma$，$\ket{\psi}$ 和 $\ket{\varphi}$ 分别是 $\rho$ 和 $\sigma$ 的纯化态，并且满足

\[
    F(\rho, \sigma) = \lvert \innerproduct{\psi}{\varphi} \rvert = F(\ket{\psi}, \ket{\varphi}).
\]

因此，如果两个量子态之间的保真度很接近于 1，则它们的迹距离也会很接近. 反之也成立，设 $\{E_m\}$ 为满足

\[
    F(\sigma, \rho) = \sum_m \sqrt{p_m q_m} 
\]

的 POVM，其中 $p_m = \op{Tr} (\rho E_m)$ 和 $q_m = \op{Tr} (\sigma E_m)$. 观察到

\begin{align*}
    \sum_m (\sqrt{p_m} - \sqrt{q_m})^2 & = \sum_m p_m + \sum_m q_m - 2 F(\sigma, \rho) \\
                                       & = 2(1 - F(\sigma, \rho)).
\end{align*}

而 $\lvert \sqrt{p_m} - \sqrt{q_m} \rvert \leq \lvert \sqrt{p_m} + \sqrt{q_m} \rvert$，因此

\begin{align*}
    \sum_m \lvert \sqrt{p_m} - \sqrt{q_m} \rvert^2 & \leq \sum_m \lvert \sqrt{p_m} - \sqrt{q_m} \rvert \lvert \sqrt{p_m} + \sqrt{q_m} \rvert \\
                                                  & \leq \sum_m \lvert p_m - q_m \rvert \\
                                                  & = 2 D(\{p_m\}, \{q_m\}) \\
                                                  & \leq 2 D(\rho, \sigma).
\end{align*}

因此

\[
    1 - F(\rho, \sigma) \leq D(\rho, \sigma) \leq \sqrt{1 - F(\rho, \sigma)^2}.
\]