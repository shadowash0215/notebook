# Quantum Proof of Knowledge

## Quantum Proofs of Knowledge

### Definition

- **交互式量子机器（Interactive Quantum Machine, IQM）**：$M$ 保存了两个量子寄存器，$S$ 保存 $M$ 的内部状态，$N$ 用于发送与接收消息，也可被称为网络寄存器. 每次激活后，$M$ 都会读取 $N$ 中的消息以及 $S$ 中先前调用的状态；而激活结束后，$S$ 存储 $M$ 的新状态，而 $N$ 存储 $M$ 的输出消息. 机器 $M$ 的输入包括：

    - 安全参数 $\eta$；
    - 经典输入 $x$；
    - 量子输入 $\ket{\psi}$（起初保存在 $S$ 中）.

    简单起见，假定收发信息的数量是由 $\eta$ 和 $x$ 决定的. 形式化定义的话，量子机器是由量子电路族 $(M_{\eta, x})_{\eta \in \mathbb{N}, x \in \{0, 1\}^*}$ 以及整数族 $(r^M_{\eta, x})_{\eta \in \mathbb{N}, x \in \{0, 1\}^*}$ 所描述的，$M_{\eta, x}$ 决定了 $S$ 和 $N$ 上所施加的酉变换，而 $r^M_{\eta, x}$ 决定了消息的数量. 在此基础上，继续定义**量子多项式时间机器**，其需要满足：

    - 电路 $M_{\eta, x}$ 的规模是 $\eta + \lvert x \rvert$ 的多项式函数；
    - $r^M_{\eta, x}$ 是 $\eta + \lvert x \rvert$ 的多项式有界函数；
    - 在给定 $\eta$ 和 $x$ 的情况下，$r^M_{\eta, x}$ 和电路描述可以在确定性多项式时间内计算出来.

- 交互式机器的执行：给定一对机器 $M$ 和 $M'$，安全参数 $\eta$，一对量子输入 $\ket{\psi}$ 和 $\ket{\psi}'$，以及一对经典输入 $x$ 和 $x'$，定义**执行过程** $\langle M(x, \ket{\psi}), M'(x', \ket{\psi}') \rangle$ 如下：

    - 初始化 $S$ 为 $\ket{\psi}$，$S'$ 为 $\ket{\psi}'$，$N$ 为 $\ket{0}$；

    - 交替执行在 $S$ 和 $N$ 上应用 $M_{\eta, x}$，以及在 $S'$ 和 $N$ 上应用 $M'_{\eta, x'}$，应用 $r^M_{\eta, x}$ 次后停止应用 $M_{\eta, x}$，应用 $r^{M'}_{\eta, x'}$ 次后停止应用 $M'_{\eta, x'}$；

    - 最终在计算基下测量 $S'$，测量结果记为随机变量 $\langle M(x, \ket{\psi}), M'(x', \ket{\psi}') \rangle$.

    简而言之，$\langle M(x, \ket{\psi}), M'(x', \ket{\psi}') \rangle$ 是 $M$ 先被激活的交互中 $M'$ 的经典输出.

- 支持回放的谕示机算法：量子谕示机算法 $A$ 是可以访问以谕示机形式给出的量子交互机器的算法，除去安全参数 $\eta$ 和其自身的经典输入 $x$ 外，$A$ 还可以访问一个在经典输入 $x'$ 和量子输入 $\ket{\psi}'$ 上运行的量子交互机器 $M$. $A$ 被允许进行以下操作：

    - 向 $M_{\eta, x'}$ 发送消息或读取 $M_{\eta, x'}$ 的输出消息；
    - 执行描述 $M$ 的量子电路 $M_{\eta, x'}$；
    - 执行 $M_{\eta, x'}$ 的量子电路的逆操作，即 $M_{\eta, x'}^\dagger$，对应于经典情况下的回放操作；
    - 处于“执行 $M_{\eta, x'}$”和“不执行 $M_{\eta, x'}$”的叠加态.

    但被禁止直接访问 $M$ 的内部状态以及量子输入. 形式化定义的话，量子谕示机算法 $A$ 是由作用于三个量子寄存器 $S_A, N, S_M$ 上的电路族 $(A_{\eta, x})_{\eta \in \mathbb{N}, x \in \{0, 1\}^*}$ 所描述，其中 $S_A, S_M$ 分别保存 $A$ 和 $M$ 的内部状态，$N$ 用于 $A$ 和 $M$ 之间的消息传递. $A_{\eta, x}$ 可以包含两种操作：

    - 普通量子门，只作用于 $S_A$ 和 $N$ 上；
    - 特殊门 $\square$ 和 $\square^\dagger$，代表对谕示机的访问，作用于 $S_A$ 中的一个控制位和整个 $(N, S_M)$ 上. 

    定义执行过程 $A^{M(x', \ket{\psi})}(x)$ 如下：

    - 初始化 $S_A$ 为 $\ket{0}$，$S_M$ 为 $\ket{\psi}$，$N$ 为 $\ket{0}$；
    - 执行 $A_{\eta, x}$，其中特殊门 $\square$ 的作用规则为应用如下的酉算子 $U$：

        \begin{align*}
            U(\ket{0}_C \otimes \ket{\psi}_N \otimes \ket{\varphi}_{S_M}) & := \ket{0} \otimes \ket{\psi} \otimes \ket{\varphi} \\
            U(\ket{1}_C \otimes \ket{\psi}_N \otimes \ket{\varphi}_{S_M}) & := \ket{1} \otimes M_{\eta, x'}(\ket{\psi} \otimes \ket{\varphi})
        \end{align*}

        $\square^\dagger$ 的作用规则只需用 $M_{\eta, x'}^\dagger$ 替换 $M_{\eta, x'}$ 即可. 

    - 最终在计算基下测量 $S_A$，测量结果记为随机变量 $A^{M(x', \ket{\psi})}(x)$.

    量子多项式时间谕示机算法 $A$ 则需要满足 $A_{\eta, x}$ 的规模是 $\eta + \lvert x \rvert$ 的多项式函数，且在给定 $\eta$ 和 $x$ 的情况下，其描述可以在确定性多项式时间内计算出来.

- 证明系统：接下来考虑由安全参数 $\eta$ 参数化的关系，即关系 $R$ 实际上是一个关系族 $(R_\eta)_{\eta \in \mathbb{N}}$，其中 $R_\eta \subseteq \{0, 1\}^* \times \{0, 1\}^*$. 而关系 $R$ 的**量子证明系统**是一对机器 $(P, V)$，其中 

    - $P$ 是证明者，接受经典输入 $(x, w) \in R$；
    
    - $V$ 是验证者，只接受经典输入 $x$.

    其有以下两个性质：

    - 完备性：存在可忽略函数 $\mu$ 使得对于任意 $\eta \in \mathbb{N}$ 和任意 $(x, w) \in R$，都有

        \[
            \op{Pr}[\langle P(x, w), V(x) \rangle = 1] \geq 1 - \mu(\eta).
        \]

    - 可靠性：设可容忍错误为 $s$，对于任意恶意证明者 $P^*$，$\eta \in \mathbb{N}$，辅助输入 $\ket{\psi}$，以及所有满足 $\nexists w: (x, w) \in R$ 的 $x$，均有

        \[
            \op{Pr}[\langle P^*(x, \ket{\psi}), V(x) \rangle = 1] \leq s(\eta).
        \]

- **量子知识证明**：粗略来说，一个量子证明系统 $(P, V)$ 被称为量子知识证明，当且仅当存在一个量子谕示机算法 $K$，若恶意证明者 $P^*$ 能够使验证者 $V$ 接受，则提取器 $K^{P^*}$ 能够输出该陈述的见证. 此处可以容忍知识错误 $\kappa$：若 $P^*$ 能够使验证者 $V$ 接受的概率小于 $\kappa(\eta)$，则不对提取器做出要求；并且不要求 $K^{P^*}$ 的成功概率和 $P^*$ 的成功概率相同，只要求二者多项式相关. 而为了支持量子知识证明作为子协议嵌入，还允许恶意证明者带有辅助输入 $\ket{\psi}$. 正规定义如下：

    !!! info "Definition(Quantum Proofs of Knowledge)"
        关系 $R$ 的量子证明系统 $(P, V)$ 被称为为可容忍知识错误 $\kappa$ 的量子可提取系统，当且仅当存在常数 $d > 0$，多项式有界函数 $p > 0$，以及量子多项式时间谕示机算法 $K$，使得对于任意交互式量子机器 $P^*$，任意多项式 $l$，任意安全参数 $\eta \in \mathbb{N}$，任意量子输入 $\ket{\psi}$，以及任意 $x \in \{0, 1\}^{\leq l(\eta)}$，满足：

        \begin{align*}
            \op{Pr}[\langle P^*(x, \ket{\psi}), V(x) \rangle = 1] & \geq \kappa(\eta) \Rightarrow \\
            \op{Pr}[(x, w) \in R: w \from K^{P^*(x, \ket{\psi})}(x)] & \geq \frac{1}{p(\eta)}(\op{Pr}[\langle P^*(x, \ket{\psi}), V(x) \rangle = 1] - \kappa(\eta))^d.
        \end{align*}

        $R$ 的可容忍知识错误 $\kappa$ 的量子知识证明（QPoK）即为完备的可容忍知识错误 $\kappa$ 的量子可提取系统 $(P, V)$.


### Discussion

本节阐释 QPoK 定义中各项设计选择的动机.

- 安全参数：以上的定义中均包含了安全参数 $\eta$，在复杂度理论中，通常不显式引入安全参数，而是让所有界限依赖于输入长度 $\lvert x \rvert$. 但显式安全参数可以避免人为填充输入长度的情况，导致不自然的机制设计，同时更好地支持了子协议的兼容性.

- 对黑盒证明者状态与输入的访问限制：提取器无权访问证明者的内部状态或其量子输入，这一设计遵循前人的工作，即“知识证明旨在‘捕获证明者通过交互所展示的知识’，因此提取器不应窥探证明者的内部状态。”

- 技术视角下的酉与可逆证明者：定义中最重要的设计选择为要求证明者是酉操作，并允许提取器执行该操作的逆运算. 以下从技术视角讨论此选择：

    - 必要性：在量子世界中，对状态进行快照/复制并不可行，因此必须允许提取器“反向运行”证明者。而非酉量子操作通常不存在逆运算，故回放仅适用于酉证明者.

    - 实用性：核心问题是该定义在基于归约的密码学证明中是否合理？这还需要更多使用 QPoK 的协议被分析后才能定论，不过接下来的示例表明该定义可以类似经典知识证明的方式使用.

    - 非酉证明者的处理：任何非酉证明者均可通过纯化转化为酉形式，再应用 QPoK 定义。因此仅允许酉恶意证明者非实际限制.

- 关于提取器的成功概率：要求提取器在量子多项式时间内运行，且成功概率为 $\frac{1}{p}(\op{Pr}_V - \kappa)^d$，其中 $\op{Pr}_V$ 是验证者接受的概率. 另一种可能的定义为要求证明者在期望时间 $\frac{p}{(\op{Pr}_V - \kappa)^d}$ 内以概率 1（或无限接近 1）成功提取见证. 经典情况下前者能够通过重复的手段得到后者，但量子情况下则不然，因为一旦失败就无法复原到原始状态. 并且当 QPoK 用于需绝对成功的场景时（如零知识证明的模拟器构造），当前定义可能不足以满足这些场景的需求.

- 量子知识论证：量子知识证明针对的是计算能力无限制的恶意证明者 $P^*$，不过在很多情形下可以弱化条件，只考虑量子多项式时间的证明者，这便引出了量子知识论证（Quantum Arguments of Knowledge, QAoK），亦可称为量子计算可靠的知识证明（Quantum Computationally Sound Proofs of Knowledge）. 本文不深究量子知识论证，前人证明接下来一节的知识证明构造无法直接迁移到量子知识论证，甚至不能构成量子论证.

    !!! info "Definition(Quantum Arguments of Knowledge)"
        关系 $R$ 的量子证明系统 $(P, V)$ 被称为可容忍知识错误 $\kappa$ 的量子可计算提取系统，当且仅当存在常数 $d > 0$，多项式有界函数 $p > 0$，以及量子多项式时间谕示机算法 $K$，使得对于任意量子多项式时间交互式量子机器 $P^*$，任意多项式 $l$，存在可忽略函数 $\mu$，使得对于任意安全参数 $\eta \in \mathbb{N}$，任意量子输入 $\ket{\psi}$，以及任意 $x \in \{0, 1\}^{\leq l(\eta)}$，满足：

        \begin{align*}
            \op{Pr}[\langle P^*(x, \ket{\psi}), V(x) \rangle = 1] & \geq \kappa(\eta) \Rightarrow \\
            \op{Pr}[(x, w) \in R: w \from K^{P^*(x, \ket{\psi})}(x)] & \geq \frac{1}{p(\eta)}\left(\op{Pr}[\langle P^*(x, \ket{\psi}), V(x) \rangle = 1] - \kappa(\eta)\right)^d - \mu(\eta).
        \end{align*}

        $R$ 的可容忍知识错误 $\kappa$ 的量子知识论证（QAoK）即为完备的可容忍知识错误 $\kappa$ 的量子可计算提取系统 $(P, V)$.

    相较于 QPoK，QAoK 的定义额外引入了可忽略误差 $\mu(\eta)$，并且其可以依赖于恶意证明者 $P^*$，因为 $\kappa(\eta)$ 不允许依赖于 $P^*$ 的行为，但通常存在于依赖于 $P^*$ 的可忽略概率 $\mu(\eta)$（如 $\mu = 2^{-\eta}T$，其中 $T$ 是 $P^*$ 的运行时间）. 

### Amplification

在某些情况下，基础构造只能产生具有常数知识错误 $\kappa$ 的 QPoK，但大多数情况下需要可忽略的知识错误. 一种解决方法是对常数错误的 QPoK 进行**顺序迭代**（Sequential Iteration），迭代后系统的知识错误将呈指数级衰减. 该结论在经典场景中广为人知，其量子版本的证明思路完全一致.

!!! note "Theorem"
    设 $n = n(\eta)$ 是一个多项式有界且可高效计算的函数，若 $(P, V)$ 是一个可容忍知识错误 $\kappa$ 的可提取系统，$(P', V')$ 是 $(P, V)$ 顺序执行 $n$ 次构成的证明系统，则 $(P', V')$ 可容忍的知识错误为 $\kappa' = \kappa^n$.

    ???+ note "Proof"
        简记 $n = n(\eta), \kappa = \kappa(\eta), p = p(\eta)$，称 $(P, V)$ 为原子协议，$(P', V')$ 为组合协议，固定恶意证明者 $P^*$，安全参数 $\eta$，陈述 $x$，以及 $P^*$ 的辅助量子输入 $\ket{\psi}$. 在组合协议执行中，每次原子协议的运行称为一轮. 不失一般性，假设 $P^*$ 由 $n$ 个顺序执行的子证明者 $P_i^*$ 组成，其中 $P_i^*$ 执行第 $i$ 轮协议. 对 $i \geq 2$，$P_i^*$ 的量子输入为 $P_{i-1}^*$ 的输出态. 设 $K$ 是原子协议的知识提取器，构造如下的组合协议的知识提取器 $K'$：

        - $K'$ 随机选取 $i \in [n]$；
        - 内部使用 $P_1^*, \ldots, P_{i - 1}^*$ 模拟前 $i - 1$ 轮协议；
        - 设 $\ket{\psi'}$ 表示 $P_{i - 1}^*$ 的输出态（若 $i = 1$，则 $\ket{\psi'} = \ket{\psi}$）；
        - 运行 $w \from K^{P_i^*(x, \ket{\psi'})}(x)$，并输出 $w$.

        在剩余的证明中，将固定安全参数 $\eta$，并且使用如下的符号：$a_i$ 为使用恶意证明者 $P^*$ 下前 $i$ 轮协议的成功概率，显然 $a_{i - 1}$ 也是模拟器 $K'$ 内部模拟前 $i - 1$ 轮协议的成功概率；$c_i$ 表示前 $i - 1$ 轮协议成功的情况下，第 $i$ 轮协议的成功概率，显然 $a_i = c_i \cdot a_{i - 1}$.

        记 $\op{Pr}_{V'}$ 为组合协议成功的概率，$\op{Pr}_{K'}$ 为提取器 $K'$ 成功的概率. 固定轮次 $i$，并记 $\op{Pr}_{K'}^{(i)}$ 为提取器 $K'$ 选择该 $i$ 的情况下 $K'$ 成功的概率，依据 $K'$ 的构造，有：

        \[
            \op{Pr}_{K'} = \frac{1}{n} \sum_{i = 1}^n \op{Pr}_{K'}^{(i)} \geq \frac{1}{n} \max_{i \in [n]} \op{Pr}_{K'}^{(i)}.
        \]

        接下来将证明存在依赖于 $P^*, \ket{\psi}, \eta, x$ 的轮次 $i$，以及独立于这些参数的多项式有界函数 $p > 0$ 和整数 $d > 0$，使得当 $\op{Pr}_{V'} \geq \kappa^n$ 时，

        \[
            \op{Pr}_{K'}^{(i)} \geq \frac{1}{p} (\op{Pr}_{V'} - \kappa^n)^d.
        \]

        由此可得

        \[
            \op{Pr}_{K'} \geq \frac{1}{np} (\op{Pr}_{V'} - \kappa^n)^d,
        \]

        也就有 $(P', V')$ 可容忍的知识错误 $\kappa' = \kappa^n$.

        接下来用 $a_{i - 1}$ 和 $c_i$ 来约束 $\op{Pr}_{K'}^{(i)}$. 设 $\ket{\psi'}$ 为组合协议前 $i - 1$ 轮成功时 $P_{i - 1}^*$ 的输出态，定义 $\op{Pr}_{K}^{(i)} (\ket{\psi'})$ 为 $K^{P^*(x, \ket{\psi'})}(x)$ 成功的概率，$\op{Pr}_{V}^{(i)} (\ket{\psi'})$ 为带有证明者 $P^*$ 和辅助输入 $\ket{\psi'}$ 的原子协议成功的概率. 那么在前 $i - 1$ 轮成功的情况下，$K'$ 成功的概率为 $\op{Pr}_{K}^{(i)} (\ket{\psi'})$，所以有

        \[
            \op{Pr}_{K'}^{(i)} = a_{i - 1} \cdot \op{Pr}_{K}^{(i)} (\ket{\psi'}).
        \]

        因为原子协议可容忍的知识错误为 $\kappa$，所以存在多项式有界函数 $p > 0$ 和整数 $d > 0$，使得对于任意 $\ket{\psi'}$，

        \[
            \op{Pr}_{K}^{(i)} (\ket{\psi'}) \geq \frac{1}{p} (\op{Pr}_{V}^{(i)} (\ket{\psi'}) - \kappa)^d.
        \]

        不失一般性，设 $d \geq 1$，注意 $p, d$ 是独立于 $i, P^*, \ket{\psi}, \eta, x$ 的. 因此有

        \[
            \op{Pr}_{K'}^{(i)} \geq a_{i - 1} \cdot \frac{1}{p} (\op{Pr}_{V}^{(i)} (\ket{\psi'}) - \kappa)^d = a_{i - 1} \cdot \frac{1}{p} (c_i - \kappa)^d
        \]

        总结一下，此时知道 $\op{Pr}_{K'} \geq \frac{1}{n} \max_{i \in [n]} \op{Pr}_{K'}^{(i)} \geq \frac{1}{np} \max_{i \in [n]} (a_{i - 1} \cdot (c_i - \kappa)^d)$，$a_i = c_i \cdot a_{i - 1}$，且 $\op{Pr}_{V'} = a_n$. 

        设 $\delta = \op{Pr}_{V'} - \kappa^n$，并假设 $\delta > 0, \kappa \leq 1$. 因为 $a_0 \leq 1 = \kappa^0 + \frac{0\delta}{n}$，而 $a_n \geq \kappa^n + \frac{n\delta}{n}$，所以存在 $i \in [n]$ 使得 $a_{i - 1} \leq \kappa^{i - 1} + \frac{(i - 1)\delta}{n}$ 且 $a_i \geq \kappa^i + \frac{i\delta}{n}$. 对于这个 $i$，有

        \[
            a_{i - 1} \cdot (c_i - \kappa) = a_i - \kappa a_{i - 1} \geq (\kappa^i + \frac{i\delta}{n}) - \kappa (\kappa^{i - 1} + \frac{(i - 1)\delta}{n}) = \frac{i\delta}{n} - \frac{(i - 1)\kappa\delta}{n} \geq \frac{\delta}{n}.
        \]

        因而

        \begin{align*}
            \op{Pr}_{K'} & \geq \frac{1}{np} \max_{i \in [n]} (a_{i - 1} \cdot (c_i - \kappa)^d) \\ 
                         & \geq \frac{1}{np} \max_{i \in [n]} a_{i - 1}^d \cdot (c_i - \kappa)^d \\ 
                         & \geq \frac{1}{np} \left(\frac{\delta}{n}\right)^d \\ 
                         & = \frac{1}{pn^{d + 1}} (\op{Pr}_{V'} - \kappa^n)^d.
        \end{align*}

        而 $pn^{d + 1}$ 是多项式有界函数，因此 $(P', V')$ 可容忍的知识错误 $\kappa' = \kappa^n$.

## Elementary constructions

在特定条件下，PoK 也是 QPoK. 

!!! info "Definition($\Sigma$-Protocol)"
    证明系统 $(P, V)$ 被称为 $\Sigma$-协议，当且仅当 $P, V$ 为经典交互式机器，且交互过程如下：

    - $P$ 发送承诺（$\mathcal{com}$）；
    - $V$ 发送挑战（$\mathcal{ch}$）；
    - $P$ 发送响应（$\mathcal{resp}$）.

    其中 $\mathcal{ch}$ 是从只和 $x$ 与 $\eta$ 相关的挑战空间 $C_{\eta, x}$ 中均匀随机选取的，要求在概率多项式时间内以可忽略误差均匀采样 $C_{\eta, x}$，并且给定 $x$ 和 $\eta$ 时，可以在关于 $\eta + \lvert x \rvert$ 的多项式时间内判断元素是否在 $C_{\eta, x}$ 中. 验证基于确定性多项式时间内进行 $x, \mathcal{com}, \mathcal{ch}, \mathcal{resp}$ 的计算结果决定是否接受，如果 $V$ 接受 $(x, \mathcal{com}, \mathcal{ch}, \mathcal{resp})$，则称 $(\mathcal{com}, \mathcal{ch}, \mathcal{resp})$ 是 $x$ 的一个可接受对话.

!!! info "Definition(Special soundness)"
    称关于关系 $R$ 的 $\Sigma$-协议 $(P, V)$ 具有**特殊可靠性**（Special Soundness），当且仅当存在确定多项式时间算法 $K_0$（称为特殊提取器），使得对于 $x$ 的任意两个可接受对话 $(\mathcal{com}, \mathcal{ch}, \mathcal{resp})$ 和 $(\mathcal{com}, \mathcal{ch}', \mathcal{resp}')$，且 $\mathcal{ch} \neq \mathcal{ch}'$，$\mathcal{ch}, \mathcal{ch}' \in C_{\eta, x}$，都有 $w = K_0(x, \mathcal{com}, \mathcal{ch}, \mathcal{resp}, \mathcal{ch}', \mathcal{resp}')$，使得 $(x, w) \in R$.

!!! info "Definition(Strict soundness)"
    称 $\Sigma$-协议 $(P, V)$ 具有**严格可靠性**（Strict Soundness），当且仅当存在对于 $x$ 的任意两个可接受对话 $(\mathcal{com}, \mathcal{ch}, \mathcal{resp})$ 和 $(\mathcal{com}, \mathcal{ch}, \mathcal{resp}')$，都有 $\mathcal{resp} = \mathcal{resp}'$.

- **正规提取器**（Canonical Extractor）：设 $(P, V)$ 是一个满足特殊可靠性和严格可靠性的 $\Sigma$-协议，且 $K_0$ 是特殊提取器，定义正规提取器 $K$，尽管定义的谕示机算法只能进行酉操作，但这里允许 $K$ 进行测量操作，这只是为了方便，因为利用纯化便可以得到具有相同效果的酉操作. 给定恶意证明者 $P^*$，$K^{P^*(x, \ket{\psi})}(x)$ 在两个量子寄存器 $N, S_{P^*}$ 上运行. 记 $P^*_{\eta, x}$ 为描述 $P^*$ 单次激活的酉变换. $K$ 的操作如下：

    - $N$ 初始化为 $\ket{0}$，$S_{P^*}$ 初始化为 $\ket{\psi}$；
    - $K$ 对 $N, S_{P^*}$ 施加 $P^*_{\eta, x}$，这对应于运行 $P^*$ 的第一步，此时 $N$ 中的消息应当为承诺；
    - $K$ 在计算基下测量 $N$，得到承诺 $\mathcal{com}$；
    - $K$ 更新 $N$ 为 $\ket{0}$，然后均匀随机选取 $\mathcal{ch}, \mathcal{ch}' \in C_{\eta, x}$；
    - 记 $U_{\mathcal{ch}}$ 为对 $N$ 施加的满足 $U_{\mathcal{ch}}\ket{x} = \ket{x \oplus \mathcal{ch}}$ 的酉变换，接下来 $K$ 施加 $P^*_{\eta, x} U_{\mathcal{ch}}$，此时 $N$ 中的消息应当为对于挑战 $\mathcal{ch}$ 的响应 $\mathcal{resp}$；
    - $K$ 在计算基下测量 $N$，得到 $\mathcal{resp}$；
    - $K$ 施加 $(P^*_{\eta, x}U_{\mathcal{ch}})^\dagger$，这便是对证明者的回放操作；
    - $K$ 施加 $P^*_{\eta, x} U_{\mathcal{ch}'}$，此时 $N$ 中的消息应当为对于挑战 $\mathcal{ch}'$ 的响应 $\mathcal{resp}'$；
    - $K$ 在计算基下测量 $N$，得到 $\mathcal{resp}'$；
    - $K$ 施加 $(P^*_{\eta, x} U_{\mathcal{ch}'})^\dagger$，最终输出 $w = K_0(x, \mathcal{com}, \mathcal{ch}, \mathcal{resp}, \mathcal{ch}', \mathcal{resp}')$.

- 正规提取器的分析：为了分析正规提取器，需要先证明一个约束的引理，其刻画当随机选取 $\mathcal{ch} \neq \mathcal{ch}'$ 时，两次连续量子测量 $P_{\mathcal{ch}}$ 和 $P_{\mathcal{ch}'}$ 都成功的概率如何用单次测量成功的概率来约束. 在经典情况下，两次测量是独立的，所以容易刻画；而在量子情况下，因为首次测量的结果可能会扰动量子态，因此需要更细致的分析来刻画这种依赖关系.

!!! success "Lemma 7"
    设 $C$ 为基数 $\# C = c$ 的集合，$(P_i)_{i \in C}$ 是 Hilbert 空间 $\mathcal{H}$ 上的正交投影算子. 设 $\ket{\psi} \in \mathcal{H}$ 为单位向量，定义 $V = \sum_{i \in C} \frac{1}{c} \lVert P_i \ket{\psi} \rVert^2$，$F = \sum_{i, j \in C} \frac{1}{c^2} \lVert P_i P_j \ket{\psi} \rVert^2$，则有 $F \geq V^3$.

    ???+ success "Proof"
        **Claim 1**: 对于任意 $\mathcal{H}$ 上的正算子 $A$ 和单位向量 $\ket{\psi} \in \mathcal{H}$，都有 $\left(\bra{\psi} A \ket{\psi}\right)^3 \leq \bra{\psi} A^3 \ket{\psi}$.

        因为 $A$ 是正算子，所以可以被对角化，不失一般性，假设 $A$ 是对角矩阵，$a_i$ 为第 $i$ 个对角元素，$f_i$ 为 $\ket{\psi}$ 的第 $i$ 个分量，则有

        \[
            \left(\bra{\psi} A \ket{\psi}\right)^3 = \left(\sum_i a_i \lvert f_i \rvert^2\right)^3 \leq \sum_i a_i^3 \lvert f_i \rvert^2 = \bra{\psi} A^3 \ket{\psi}.
        \]

        注意到中间的放缩利用了 Jensen 不等式，因为 $a_i \geq 0$，$\sum_i \lvert f_i \rvert^2 = 1$，且 $x \mapsto x^3$ 是凸函数.

        **Claim 2**: 对于任意向量 $\ket{\psi_1}, \ldots, \ket{\psi_c} \in \mathcal{H}$，都有 $\lVert \frac{1}{c} \sum_{i} \ket{\psi_i} \rVert^2 \leq \frac{1}{c} \sum_{i} \lVert \ket{\psi_i} \rVert^2$.

        设 $\ket{\Psi} = \frac{1}{c} \sum_{i} \ket{\psi_i}$，则有

        \begin{align*}
            \sum_i \left(\lVert \ket{\psi_i} \rVert^2 - \lVert \ket{\Psi} \rVert^2\right) & = \sum_i \left(\lVert \ket{\psi_i} \rVert - \lVert \ket{\Psi} \rVert\right)\left(\lVert \ket{\psi_i} \rVert - \lVert \ket{\Psi} \rVert + 2 \lVert \ket{\Psi} \rVert\right) \\
            & = \sum_i \left(\lVert \ket{\psi_i} \rVert - \lVert \ket{\Psi} \rVert\right)^2 + 2\lVert \ket{\Psi} \rVert \sum_i \left(\lVert \ket{\psi_i} \rVert - \lVert \ket{\Psi} \rVert\right) \\
            & \geq 2 \lVert \ket{\Psi} \rVert \sum_i \left(\lVert \ket{\psi_i} \rVert - \lVert \ket{\Psi} \rVert\right) \\
            & = 2 \lVert \ket{\Psi} \rVert \left(\sum_i \lVert \ket{\psi_i} \rVert - \lVert c \ket{\Psi} \rVert\right) \\
            & = 2 \lVert \ket{\Psi} \rVert \left(\sum_i \lVert \ket{\psi_i} \rVert - \left\lVert \sum_i \ket{\psi_i} \right\rVert\right) \geq 0.
        \end{align*}

        所以 $\frac{1}{c} \sum_i \lVert \ket{\psi_i} \rVert^2 - \lVert \frac{1}{c} \sum_i \ket{\psi_i} \rVert^2 = \frac{1}{c} \sum_i \left(\lVert \ket{\psi_i} \rVert^2 - \lVert \ket{\Psi} \rVert^2\right) \geq 0$.

        设 $A = \frac{1}{c} \sum_{i \in C} P_i$, $\ket{\phi_{ij}} = P_j \ket{\psi}$，则 $A$ 是正算子，并且有：

        \begin{align*}
            V^3 & = \left(\sum_{i \in C} \frac{1}{c} \bra{\psi} P_i \ket{\psi}\right)^3 \\
                & = \left(\bra{\psi} A \ket{\psi}\right)^3 \\
                & \leq \bra{\psi} A^3 \ket{\psi} \\
                & = \sum_{i, j, k} \frac{1}{c^3} \lVert P_i P_j P_k \ket{\psi} \rVert^2 \\
                & = \sum_{i, j, k} \frac{1}{c^3} \innerproduct{\phi_{ij}}{\phi_{kj}} \\
                & = \sum_j \frac{1}{c} \left(\sum_i \frac{1}{c} \bra{\phi_{ij}}\right) \left(\sum_k \frac{1}{c} \ket{\phi_{kj}}\right) \\
                & = \sum_j \frac{1}{c} \left\lVert \sum_i \frac{1}{c} \ket{\phi_{ij}} \right\rVert^2 \\
                & \leq \sum_j \frac{1}{c} \sum_i \frac{1}{c} \lVert \ket{\phi_{ij}} \rVert^2 \\
                & = \sum_{i, j} \frac{1}{c^2} \lVert P_i P_j \ket{\psi} \rVert^2 = F.
        \end{align*}

        由此可得 $F \geq V^3$.

!!! success "Lemma 8"
    设 $C$ 为基数 $\# C = c$ 的集合，$(P_i)_{i \in C}$ 是 Hilbert 空间 $\mathcal{H}$ 上的正交投影算子. 设 $\ket{\psi} \in \mathcal{H}$ 为单位向量，定义 $V = \sum_{i \in C} \frac{1}{c} \lVert P_i \ket{\psi} \rVert^2$，$E = \sum_{i, j \in C, i \neq j} \frac{1}{c^2} \lVert P_i P_j \ket{\psi} \rVert^2$，如果 $V \geq \frac{1}{\sqrt{c}}$，则有 $E \geq V (V^2 - \frac{1}{c})$.

    ???+ success "Proof"
        设 $F$ 为先前所定义，那么

        \begin{align*}
            E & = \sum_{i, j \in C, i \neq j} \frac{1}{c^2} \lVert P_i P_j \ket{\psi} \rVert^2 \\
              & = \sum_{i, j \in C} \frac{1}{c^2} \lVert P_i P_j \ket{\psi} \rVert^2 - \sum_{i \in C} \frac{1}{c^2} \lVert P_i P_i \ket{\psi} \rVert^2 \\
              & = \sum_{i, j \in C} \frac{1}{c^2} \lVert P_i P_j \ket{\psi} \rVert^2 - \sum_{i \in C} \frac{1}{c^2} \lVert P_i \ket{\psi} \rVert^2 \\
              & = F - \frac{V}{c} \\
              & \geq V^3 - \frac{V}{c} \\
              & = V \left(V^2 - \frac{1}{c}\right).
        \end{align*}

!!! note "Theorem 9"
    设 $(P, V)$ 是关系 $R$ 的一个 $\Sigma$-协议，并且挑战空间为 $C_{\eta, x}$. 固定函数 $c$ 使得对于任意 $\eta \in \mathbb{N}$，$x \in \{0, 1\}^*$，都有 $\# C_{\eta, x} \geq c(\eta)$. 假定 $(P, V)$ 具有特殊可靠性和严格可靠性，那么 $(P, V)$ 是一个可容忍知识错误 $1/\sqrt{c}$ 的量子可提取系统.

    ???+ note "Proof"
        为了证明 $(P, V)$ 是可提取的，需要构造正规提取器 $K$. 固定恶意敌手 $P^*$，陈述 $x$，以及 $P^*$ 的辅助量子输入 $\ket{\psi}$. 记 $\op{Pr}_V$ 为验证者与 $P^*$ 交互后接受的概率，$\op{Pr}_K$ 为 $K^{P^*(x, \ket{\psi})}(x)$ 输出 $w$ 使得 $(x, w) \in R$ 的概率. 希望证明对于 $\op{Pr}_V \geq \frac{1}{\sqrt{\# C_{\eta, x}}}$ 时，有 $\op{Pr}_K \geq \op{Pr}_V (\op{Pr}_V^2 - \frac{1}{\# C_{\eta, x}})$. 从而对于 $\op{Pr}_V \geq \frac{1}{\sqrt{c(\eta)}} \geq \frac{1}{\sqrt{\# C_{\eta, x}}}$，有

        \begin{align*}
            \op{Pr}_V (\op{Pr}_V^2 - \frac{1}{\# C_{\eta, x}}) 
            & \geq \op{Pr}_V (\op{Pr}_V^2 - \frac{1}{c(\eta)}) \\ 
            & = \op{Pr}_V (\op{Pr}_V + \frac{1}{\sqrt{c(\eta)}})(\op{Pr}_V - \frac{1}{\sqrt{c(\eta)}}) \\ 
            & \geq (\op{Pr}_V - \frac{1}{\sqrt{c(\eta)}})^3.
        \end{align*}

        因为 $K$ 是量子多项式时间的，这也就表明 $(P, V)$ 是可容忍知识错误 $1/\sqrt{c}$ 的量子可提取系统.

        而为了证明 $\op{Pr}_K \geq \op{Pr}_V (\op{Pr}_V^2 - \frac{1}{\# C_{\eta, x}})$，会使用一个博弈序列，每个博弈都包含一个事件 $\mathbf{Succ}$，而在第一个博弈中，$\op{Pr}[\mathbf{Succ}: \op{Game}_1] = \op{Pr}_K$. 对任意两个连续的博弈，都会有 $\op{Pr}[\mathbf{Succ}: \op{Game}_i] \geq \op{Pr}[\mathbf{Succ}: \op{Game}_{i + 1}]$，而对于最后的博弈 $\op{Game}_7$，将有 $\op{Pr}[\mathbf{Succ}: \op{Game}_7] \geq \op{Pr}_V (\op{Pr}_V^2 - \frac{1}{\# C_{\eta, x}})$，这样便完成了证明. 对每个博弈的都只会描述其与先前的博弈不同的方面.

        **Game 1**: 直接运行 $K^{P^*(x, \ket{\psi})}(x)$，$\mathbf{Succ}$ 表示事件 $K$ 成功输出 $x$ 的一个合法见证 $w$. 依据定义，$\op{Pr}[\mathbf{Succ}: \op{Game}_1] = \op{Pr}_K$.

        **Game 2**: $\mathbf{Succ}$ 表示事件 $(\mathcal{com}, \mathcal{ch}, \mathcal{resp})$ 和 $(\mathcal{com}, \mathcal{ch}', \mathcal{resp}')$ 是 $x$ 的两个可接受对话，且 $\mathcal{ch} \neq \mathcal{ch}'$. 因为 $(P, V)$ 具有特殊可靠性，所以如果 $\mathbf{Succ}$ 发生，$K$ 都能输出一个合法见证 $w$. 因此 $\op{Pr}[\mathbf{Succ}: \op{Game}_1] \geq \op{Pr}[\mathbf{Succ}: \op{Game}_2]$.

        **Game 3**: 在 $K$ 测量 $\mathcal{resp}$ 之前，其首先测量“测量 $\mathcal{resp}$ 是否意味着这个对话会被接受”. 更精确地说，其使用正交投影算子 $P_\mathcal{ch}$ 测量 $N$，其中 $P_\mathcal{ch}$ 投影到空间 $V_\mathcal{ch} = \op{span}\{\ket{\mathcal{resp}}: (\mathcal{com}, \mathcal{ch}, \mathcal{resp}) \text{ 是被接受的}\}$. 测量 $\mathcal{resp}'$ 同理. 因为完全的测量是在 $P_\mathcal{ch}$ 和 $P_{\mathcal{ch}'}$ 后对 $N$ 进行的，引入额外的测量并不会改变 $\mathcal{resp}$ 和 $\mathcal{resp}'$ 的结果和测量后量子态，所以 $\op{Pr}[\mathbf{Succ}: \op{Game}_2] = \op{Pr}[\mathbf{Succ}: \op{Game}_3]$.

        **Game 4**: $\mathbf{Succ}$ 表示事件 $\mathcal{ch} \neq \mathcal{ch}'$ 并且测量 $P_\mathcal{ch}$ 和 $P_{\mathcal{ch}'}$ 均成功. 依据这两个测量的定义，事件发生当且仅当 $(\mathcal{com}, \mathcal{ch}, \mathcal{resp})$ 和 $(\mathcal{com}, \mathcal{ch}', \mathcal{resp}')$ 均为可接受对话，并且 $\mathcal{ch} \neq \mathcal{ch}'$. 因此 $\op{Pr}[\mathbf{Succ}: \op{Game}_3] = \op{Pr}[\mathbf{Succ}: \op{Game}_4]$.

        **Game 5**: 不再执行 $K_0$，即施加 $(P^*_{\eta, x} U_\mathcal{ch})^\dagger$ 后便终止. 因为此时 $\mathbf{Succ}$ 已经可以确定了，所以 $\op{Pr}[\mathbf{Succ}: \op{Game}_4] = \op{Pr}[\mathbf{Succ}: \op{Game}_5]$.

        **Game 6**: 不再对 $\mathcal{resp}$ 和 $\mathcal{resp}'$ 进行测量，注意这些测量的结果都没有使用过. 因为 $(P, V)$ 具有严格可靠性，所以 $V_\mathcal{ch} = \op{span}\{\ket{\mathcal{resp}_0}\}$，$\mathcal{resp}_0$ 是依赖于 $\mathcal{com}$ 和 $\mathcal{ch}$ 的单值. 因此，如果测量 $P_\mathcal{ch}$ 成功，$N$ 中的测量后量子态即为 $\ket{\mathcal{resp}_0}$. 换言之，$N$ 此时的状态是经典的，再对 $N$ 应用计算基进行测量并不会改变其状态，也就是说，测量 $\mathcal{resp}$ 并不改变状态. $\mathcal{resp}'$ 的测量同理. 因而 $\op{Pr}[\mathbf{Succ}: \op{Game}_5] = \op{Pr}[\mathbf{Succ}: \op{Game}_6]$.

        **Game 7**: 
        
        - $N$ 和 $S_{P^*}$ 初始化为 $\ket{0}$ 和 $\ket{\psi}$；
        - 施加酉变换 $P_{\eta, x}^*$；
        - 对 $N$ 进行完全测量得到承诺 $\mathcal{com}$；
        - 更新 $N$ 为 $\ket{0}$，随机选取 $\mathcal{ch}, \mathcal{ch}' \in C_{\eta, x}$；
        - 施加酉变换 $P_{\eta, x}^* U_\mathcal{ch}$；
        - 进行测量 $P_\mathcal{ch}$；
        - 施加酉变换 $(P_{\eta, x}^* U_\mathcal{ch})^\dagger$；
        - 施加酉变换 $P_{\eta, x}^* U_{\mathcal{ch}'}$；
        - 进行测量 $P_{\mathcal{ch}'}$；
        - 施加酉变换 $(P_{\eta, x}^* U_{\mathcal{ch}'})^\dagger$.

        $\mathbf{Succ}$ 依然表示事件 $\mathcal{ch} \neq \mathcal{ch}'$ 并且两次测量均成功. Game 6 和 Game 7 是等同的，Game 7 只是为了清晰而把整个流程再叙述了一遍. 所以 $\op{Pr}[\mathbf{Succ}: \op{Game}_6] = \op{Pr}[\mathbf{Succ}: \op{Game}_7]$.

        在 Game 7 中，对某些值 $d$，记 $p_d$ 为测量得到 $\mathcal{com} = d$ 的概率，$\ket{\psi_d}$ 为 $N, S_{P^*}$ 在测量 $\mathcal{com} = d$ 以及更新 $N$ 为 $\ket{0}$ 后的状态. 记 $K_d$ 为状态 $\ket{\psi_d}$ 下两次测量均成功且 $\mathcal{ch} \neq \mathcal{ch}'$ 的概率. 那么 $\op{Pr}[\mathbf{Succ}: \op{Game}_7] = \sum_d p_d K_d$，并且

        \begin{align*}
            K_d & = \sum_{\mathcal{ch}, \mathcal{ch}' \in C_{\eta, x}, \mathcal{ch} \neq \mathcal{ch}'} \frac{1}{\# C_{\eta, x}^2} \lVert (P_{\eta, x}^* U_{\mathcal{ch}'})^\dagger P_{\mathcal{ch}'} (P_{\eta, x}^* U_{\mathcal{ch}'})(P_{\eta, x}^* U_{\mathcal{ch}})^\dagger P_{\mathcal{ch}} (P_{\eta, x}^* U_{\mathcal{ch}}) \ket{\psi_d} \rVert^2 \\
            & = \sum_{\mathcal{ch}, \mathcal{ch}' \in C_{\eta, x}, \mathcal{ch} \neq \mathcal{ch}'} \frac{1}{\# C_{\eta, x}^2} \lVert P_{\mathcal{ch}'}^* P_{\mathcal{ch}}^* \ket{\psi_d} \rVert^2
        \end{align*}

        其中 $P_\mathcal{ch}^* = (P_{\eta, x}^* U_{\mathcal{ch}})^\dagger P_{\mathcal{ch}} (P_{\eta, x}^* U_{\mathcal{ch}})$. 因为 $P_\mathcal{ch}$ 是正交投影算子，而 $P_{\eta, x}^* U_\mathcal{ch}$ 是酉变换，所以 $P_\mathcal{ch}^*$ 也是正交投影算子. 定义 $\varphi(v)$ 为

        \[
            \varphi(v) = \begin{cases}
                v (v^2 - \frac{1}{\# C_{\eta, x}}) & \frac{1}{\sqrt{\# C_{\eta, x}}} \leq v \leq 1 \\
                0 & 0 \leq v < \frac{1}{\sqrt{\# C_{\eta, x}}}
            \end{cases}.
        \]

        那么依据先前的引理，设 $V_d = \sum_{\mathcal{ch} \in C_{\eta, x}} \frac{1}{\# C_{\eta, x}} \lVert P_\mathcal{ch}^* \ket{\psi_d} \rVert^2$，则有 $K_d \geq \varphi(V_d)$.

        此外，依据诚实验证者的构造，有

        \begin{align*}
            \op{Pr}_V & = \sum_d p_d \sum_{\mathcal{ch} \in C_{\eta, x}} \frac{1}{\# C_{\eta, x}} \lVert P_\mathcal{ch} (P_{\eta, x}^* U_\mathcal{ch}) \ket{\psi_d} \rVert^2 \\
                      & = \sum_d p_d \sum_{\mathcal{ch} \in C_{\eta, x}} \frac{1}{\# C_{\eta, x}} \lVert (P_{\eta, x}^* U_\mathcal{ch})^\dagger P_\mathcal{ch} (P_{\eta, x}^* U_\mathcal{ch}) \ket{\psi_d} \rVert^2 \\
                      & = \sum_d p_d V_d.
        \end{align*}

        最终有

        \begin{align*}
            \op{Pr}_K & = \op{Pr}[\mathbf{Succ}: \op{Game}_1] \\
                      & \geq \op{Pr}[\mathbf{Succ}: \op{Game}_7] \\
                      & = \sum_d p_d K_d \\
                      & \geq \sum_d p_d \varphi(V_d) \\
                      & \geq \varphi(\op{Pr}_V).
        \end{align*}

        最后一行使用了 Jensen 不等式，因为 $\varphi$ 是凸函数. 按先前的分析，当 $\op{Pr}_V \geq \frac{1}{\sqrt{\# C_{\eta, x}}}$ 时，$\op{Pr}_K \geq \varphi(\op{Pr}_V) = \op{Pr}_V (\op{Pr}_V^2 - \frac{1}{\# C_{\eta, x}})$，这表明 $(P, V)$ 是一个可容忍知识错误 $1/\sqrt{c}$ 的量子可提取系统.

**知识论证**：或许有人会认为以上的结果可以直接过渡到可计算情况，即如果一个 $\Sigma$-协议具有可计算特殊可靠性和可计算严格可靠性，那么它是一个知识论证. 然而这并不成立，因为在以上定理的证明中，当从 Game 5 过渡到 Game 6 时，使用了关于 $\mathcal{resp}$ 的测量不会影响状态的结果，这建立在严格可靠性上. 但可计算严格可靠性只保证在多项式时间内无法同时找到两个 $\mathcal{resp}$，但整个寄存器可能是若干个 $\mathcal{resp}$ 的叠加态，因此测量 $\mathcal{resp}$ 可能会改变状态. 并且先前的研究表明，存在一个具有特殊可靠性和可计算严格可靠性的证明系统并非是量子知识论证，并且存在一个具有可计算特殊可靠性和可计算严格可靠性的证明系统甚至并非是量子论证.

### On using existing bounds from the literature

!!! success "Lemma 10(Rewinding of mBQKW commitment)"
    考虑两个形如 $P_i = U_i^\dagger (\ket{\hat{w}_i} \bra{\hat{w}_i} \otimes I) U_i$ 的投影算子 $P_0$ 和 $P_1$，其中 $U_i$ 是酉变换，$\ket{\hat{w}_i} \in \{0, 1\}^n$. 考虑量子态 $\ket{\psi}$，定义概率 $p_i = \lVert P_i \ket{\psi} \rVert^2$，$p_\oplus = \lVert P_1 P_0 \ket{\psi} \rVert^2$. 如果存在 $\varepsilon > 0$，使得 $p_0 + p_1 \geq 1 + \varepsilon$，则有 $p_\oplus \geq \varepsilon^2/ 4$.

将其按先前的引理格式进行重新叙述：

!!! success "Lemma 11"
    令 $C = \{0, 1\}$，$P_0, P_1$ 为先前所定义的投影算子，$\ket{\psi}$ 为单位向量，令 $V = \frac{1}{2} \sum_{i \in C} \lVert P_i \ket{\psi} \rVert^2$，$E = \lVert P_1 P_0 \ket{\psi} \rVert^2$. 那么如果 $V \geq \frac{1}{2}$，则有 $E \geq (V - \frac{1}{2})^2$.

可以使用这一引理证明先前定理在 $\# C = 2$ 时的一个变体，其能容忍的知识错误为 $\kappa = \frac{1}{2}$.

!!! success "Corollary 12"
    设 $(P, V)$ 是关系 $R$ 的一个 $\Sigma$-协议，并且挑战空间为 $C_{\eta, x}$. 假定对于任意 $\eta, x$，$\# C_{\eta, x} = 2$，且 $(P, V)$ 具有特殊可靠性和严格可靠性，那么 $(P, V)$ 是一个可容忍知识错误 $\kappa = \frac{1}{2}$ 的量子可提取系统.

    ???+ success "Proof"
        不失一般性，设 $C_{\eta, x} = \{0, 1\}$，构造一个始终选择 $\mathcal{ch} = 0, \mathcal{ch}' = 1$ 的提取器 $K$，其余条件与标准提取器一致. 与先前的定理类似，对于每个承诺 $d$，都有 $K_d = \lVert P_1^* P_0^* \ket{\psi_d} \rVert^2$. 定义辅助函数 $\varphi$ 为

        \[
            \varphi(v) = \begin{cases}
                v (v - \frac{1}{2})^2 & \frac{1}{2} \leq v \leq 1 \\
                0 & 0 \leq v < \frac{1}{2}
            \end{cases}.
        \]

        依据引理，便有 $K_d \geq \varphi(V_d)$，其中 $V_d = \frac{1}{2} \sum_{i = 0, 1} \lVert P_i^* \ket{\psi_d} \rVert^2$. 

        ??? note
            应用引理 11 的条件是投影算子的形式为引理 10 中的特殊形式，而因为严格可靠性的限制，$P_\mathcal{ch}$ 都是秩为 1 的投影算子，并且 $P_\mathcal{ch}^* = (P_{\eta, x}^* U_\mathcal{ch})^\dagger P_\mathcal{ch} (P_{\eta, x}^* U_\mathcal{ch})$，所以 $P_0^*$ 和 $P_1^*$ 都符合要求.

        最终依据 Jensen 不等式，有

        \[
            \op{Pr}_K = \sum_d p_d K_d \geq \sum_d p_d \varphi(V_d) \geq \varphi\left(\sum_d p_d V_d\right) = \varphi(\op{Pr}_V).
        \]

        因此如果 $\op{Pr}_V \geq \frac{1}{2}$，则 $\op{Pr}_K \geq (\op{Pr}_V - \frac{1}{2})^2$, 这表明 $(P, V)$ 是一个可容忍知识错误 $\kappa = \frac{1}{2}$ 的量子可提取系统.

## Zero knowledge

前述章节中研究了 QPoK 的定义，以及 $\Sigma$-协议何时成为 QPoK. 但是仅仅是知识证明的协议的用处是有限的，通常还需要满足零知识性，本节将研究零知识性质.

!!! info "Definition(Honest-verifier Zero-Knowledge)"
    称 $\Sigma$-协议 $(P, V)$ 具有**诚实验证者零知识性**（Honest-verifier Zero-Knowledge），当且仅当存在量子多项式时间算法 $S_\Sigma$（模拟器）使得交互过程 $\langle P(x, w), V(x) \rangle$ 的协议转录本与 $S_\Sigma(x)$ 的输出在量子计算意义下不可区分. 也就是说，存在量子多项式时间算法 $S_\Sigma$，使得对于任意量子多项式时间算法 $D_\Sigma$（区分器）和任意多项式 $l$，存在可忽略函数 $\mu$ 使得对于所有满足 $\lvert x \rvert, \lvert w \rvert \leq l(\eta)$ 的 $(x, w) \in R$，以及所有量子态 $\ket{\psi}$，都有

    \begin{align*}
        \lvert & \op{Pr}[b = 1: (\mathcal{com}, \mathcal{ch}, \mathcal{resp}) \from \langle P(x, w), V(x) \rangle,  b \hookleftarrow D_\Sigma (\ket{\psi}, \mathcal{com}, \mathcal{ch}, \mathcal{resp})] \\ 
        - & \op{Pr}[b = 1: (\mathcal{com}, \mathcal{ch}, \mathcal{resp}) \from S_\Sigma(x), b \hookleftarrow D_\Sigma (\ket{\psi}, \mathcal{com}, \mathcal{ch}, \mathcal{resp})] \rvert \leq \mu(\eta).
    \end{align*}

    这里的 $(\mathcal{com}, \mathcal{ch}, \mathcal{resp}) \from \langle P(x, w), V(x) \rangle$ 表示在 $P$ 和 $V$ 交互中发送的信息.

考虑 HVZK 的一个统计变体：

!!! info "Definition(Statistical Honest-verifier Zero-Knowledge)"
    称 $\Sigma$-协议 $(P, V)$ 具有**统计诚实验证者零知识性**（Statistical Honest-verifier Zero-Knowledge），当且仅当存在量子多项式时间算法 $S_\Sigma$（模拟器）使得交互过程 $\langle P(x, w), V(x) \rangle$ 的协议转录本与 $S_\Sigma(x)$ 的输出在统计意义下不可区分. 即该定义与上一个定义十分类似，区别在于要求对所有（可能无限制）的区分器 $D_\Sigma$ 都成立.

接下来阐述量子计算零知识的定义：

!!! info "Definition(Quantum Computational Zero-Knowledge)"
    一个关于关系 $R$ 的交互式证明系统 $(P, V)$ 是**量子计算零知识**（Quantum Computational Zero-Knowledge），当且仅当对于任意量子多项式时间算法 $V^*$ 存在量子多项式时间算法 $S$ 使得对于任意量子多项式时间算法 $D$ 和任意多项式 $l$，存在可忽略函数 $\mu$ 使得对于所有满足 $\lvert x \rvert, \lvert w \rvert \leq l(\eta)$ 的 $(x, w) \in R$，以及所有量子态 $\ket{\psi}$，都有

    \begin{align*}
        \lvert & \op{Pr}[b = 1: ZE \from \ket{\psi}, \langle P(x, w), V^*(Z) \rangle, b \hookleftarrow D(\ket{\psi}, Z, E)] \\
        - & \op{Pr}[b = 1: ZE \from \ket{\psi}, S(x, Z), b \hookleftarrow D(\ket{\psi}, Z, E)] \rvert \leq \mu(\eta).
    \end{align*}

    此处的 $ZE \from \ket{\psi}$ 表示量子寄存器 $Z$ 和 $E$ 被联合初始化为量子态 $\ket{\psi}$，并且 $\langle P(x, w), V^*(Z) \rangle$ 表示证明者 $P$ 和验证者 $V^*$ 之间的一次交互，其中 $V^*$ 可以访问量子寄存器 $Z$，注意在交互后 $V^*$ 可能会改变 $Z$ 的状态. $S(x, Z)$ 同样可以访问 $Z$，并且可能改变其状态.

同样有一个统计变体：

!!! info "Definition(Quantum statistical Computational Zero-Knowledge)"
    类似于 Quantum computational Zero-Knowledge 的定义，除了区分器 $D$ 可以是无限制的.

!!! success "Corollary(Quantum Rewinding Lemma with small perturbations)"
    设 $C, Z, E, Y$ 都是量子寄存器，其中 $C$ 只有一个量子比特. 记 $S_1$ 是作用在 $C, Z, Y$ 上的酉操作，$M$ 为在计算基下对 $C$ 进行的测量.

    对量子态 $\ket{\psi}$，记 $p(\ket{\psi}) = \op{Pr}[\mathcal{succ} = 1: S_1(CZY), \mathcal{succ} \from M(C)]$，其中 $Z, E$ 被联合初始化为 $\ket{\psi}$，$Y, C$ 被初始化为 $\ket{0}$. 当 $\mathcal{succ} = 1$ 时，令密度算符 $\rho_\psi^1$ 表示此时寄存器 $ZE$ 的状态.

    令 $\varepsilon \in (0, 1/2)$，$p \in (\varepsilon, 1/2]$，假定对于任意 $\ket{\psi}$，都有 $\lvert p(\ket{\psi}) - q \rvert \leq \varepsilon$.

    那么存在一个作用在寄存器 $Z$ 上的量子电路 $S$，其规模为 $O(\frac{\log(1/\varepsilon) \op{size}(S_1)}{(q - \varepsilon)(1 - q + \varepsilon)})$.（$S$ 是一个通用量子电路，即 $S$ 可以创建辅助或销毁量子比特，以及进行测量）给定 $S_1$ 的描述，便能在 $O(\frac{\log(1/\varepsilon) \op{size}(S_1)}{(q - \varepsilon)(1 - q + \varepsilon)})$ 的时间内计算出 $S$ 的描述. 并且对于任意 $\ket{\psi}$，都有

    \[
        \op{TD}(\rho_\psi^1, \rho_\psi^2) \leq 4 \sqrt{\varepsilon} \frac{\log(1/\varepsilon)}{(q - \varepsilon)(1 - q + \varepsilon)},
    \]

    其中密度算子 $\rho_\ket{\psi}^2$ 表示 $ZE$ 在 $S$ 作用下的状态.

    ???+ success "Proof"
        !!! success "Wat09, Lemma 9"
            设 $Q$ 是一个 $(n, k)$-量子电路，并且 $p_0, q \in (0, 1)$，$\varepsilon \in (0, 1/2)$，对任意的 $n$ 量子比特的量子态 $\ket{\psi}$ 满足：

            1. $\lvert p(\ket{\psi}) - q \rvert \leq \varepsilon$；
            2. $p_0(1 - p_0) \leq q(1 - q)$；
            3. $p_0 \leq p(\ket{\psi})$.

            那么存在通用量子电路 $R$ 满足

            \[
                \op{size}(R) = O\left(\frac{\log(1/\varepsilon) \op{size}(Q)}{p_0(1 - p_0)}\right)
            \]

            使得对于任意 $n$ 量子比特的量子态 $\ket{\psi}$，$R$ 的输出 $\rho(\ket{\psi})$ 满足

            \[
                \bra{\phi_0(\psi)} \rho(\ket{\psi}) \ket{\phi_0(\psi)} \geq 1 - 16 \varepsilon \frac{\log^2(1/\varepsilon)}{p_0^2(1 - p_0)^2}.
            \]

        令 $p_0 = q - \varepsilon$，$Q = S_1$，则可以在 $O\left(\frac{\log(1/\varepsilon) \op{size}(S_1)}{p_0(1 - p_0)}\right)$ 的时间内构造出通用量子电路 $R$，其作用在寄存器 $CZEY$ 上. 设纯态 $\ket{\phi(\psi)}$ 为执行 $S_1 (ZY)$ 后 $\mathcal{succ} \xleftarrow{R} M(Z)$ 得到 $\mathcal{succ} = 1$ 时 $CZEY$ 的状态，那么保真度 $F(\cdot, \cdot)$ 满足

        \[
            F(\rho(\psi), \ket{\phi(\psi)} \bra{\phi(\psi)})^2 \geq 1 - 16 \varepsilon \frac{\log^2(1/\varepsilon)}{p_0^2(1 - p_0)^2}.
        \]

        !!! success "NC10, (9.101)"
            $D(\rho, \sigma) \leq \sqrt{1 - F(\rho, \sigma)^2}$.

        因此

        \[
            \op{TD}(\rho(\psi), \ket{\phi(\psi)} \bra{\phi(\psi)}) \leq 4 \sqrt{\varepsilon} \frac{\log(1/\varepsilon)}{p_0(1 - p_0)}.
        \]

        从电路 $R$ 构建作用在寄存器 $ZE$ 上的电路 $S$，首先初始化辅助寄存器 $C$ 和 $Y$ 为 $\ket{0}$，然后运行 $R$，再摧毁寄存器 $C$ 和 $Y$. 此时有

        \[
            \rho_\psi^1 = \op{Tr}_{CY}(\ket{\phi(\psi)} \bra{\phi(\psi)}), \quad \rho_\psi^2 = \op{Tr}_{CY}(\rho(\psi)).
        \]

        而迹距离在偏迹操作下不会增加，因此

        \[
            \op{TD}(\rho_\psi^1, \rho_\psi^2) \leq 4 \sqrt{\varepsilon} \frac{\log(1/\varepsilon)}{p_0(1 - p_0)} = 4 \sqrt{\varepsilon} \frac{\log(1/\varepsilon)}{(q - \varepsilon)(1 - q + \varepsilon)}.
        \]

!!! note "Theorem"
    设 $(P, V)$ 是一个 $\Sigma$-协议，假定如果 $P$ 接收到挑战 $\mathcal{ch} \not \in C_{\eta, x}$ 便会返回固定的响应 $\mathcal{error}$：

    - 如果 $\lvert C_{\eta, x} \rvert$ 是关于 $\eta + \lvert x \rvert$ 多项式有界的，并且协议是统计诚实验证者零知识的，那么 $(P, V)$ 是量子统计零知识的；

    - 如果 $\lvert C_{\eta, x} \rvert$ 是关于 $\eta + \lvert x \rvert$ 多项式有界的，并且协议是诚实验证者零知识的，那么 $(P, V)$ 是量子计算零知识的.

    ???+ note "Proof"
        不失一般性，假设 $V^*$ 永远都不会发送 $\mathcal{ch} \not \in C_{\eta, x}$. 具体来说，当其发送 $\mathcal{ch} \not \in C_{\eta, x}$ 时，将其转换为验证者 $\hat{V}^*$，其运行 $V^*$，但当 $V^*$ 发送无效挑战 $\mathcal{ch} \not \in C_{\eta, x}$ 时，$\hat{V}^*$ 改为发送 $\mathcal{ch}_0 \in C_{\eta, x}$，并且 $\hat{V}^*$ 忽略证明者 $P$ 的响应 $\mathcal{resp}$，而是直接发送 $\mathcal{error}$ 给 $V^*$. 因此 $\langle P(x, w), V^*(Z) \rangle$ 和 $\langle P(x, w), \hat{V}^*(Z) \rangle$ 的 $Z$ 的最终状态是相同的. 因此可以假设 $V^*$ 永远都不会发送 $\mathcal{ch} \not \in C_{\eta, x}$.

        依据定义，为了证明 $\Sigma$ 是量子统计[计算]零知识的，对于任意量子多项式时间的 $V^*$ 和任意多项式 $l$，需要构造一个量子多项式时间的模拟器 $S$，使得对于任意[量子多项式时间]的区分器 $D$ 和 $\lvert x \rvert, \lvert w \rvert \leq l(\eta)$，

        \begin{align*}
            \lvert & \op{Pr}[b = 1: ZE \from \ket{\psi}, \langle P(x, w), V^*(Z) \rangle, b \hookleftarrow D(Z, E)] \\
            - & \op{Pr}[b = 1: ZE \from \ket{\psi}, S(x, Z), b \hookleftarrow D(Z, E)] \rvert
        \end{align*}

        是可忽略的.

        因为 $\Sigma$ 协议是一个三轮协议，所以可以将证明者 $P$ 表示为两个量子多项式时间算法 $P_1$ 和 $P_2$，承诺 $\mathcal{com}$ 由 $\mathcal{com} \from P_1(x, w)$ 生成，而对挑战 $\mathcal{ch}$ 的响应 $\mathcal{resp}$ 由 $\mathcal{resp} \from P_2(x, w, \mathcal{ch})$ 生成. $P_1$ 和 $P_2$ 可以共享状态. 类似地，恶意验证者 $V^*$ 也可以被表示为两个量子多项式时间算法 $V_1^*$ 和 $V_2^*$，其中 $V_1^*(\mathcal{com}, Z)$ 生成挑战 $\mathcal{ch}$，而 $V_2^*(\mathcal{resp}, Z)$ 进行验证. $V_1^*$ 和 $V_2^*$ 也可以共享状态.

        所以，$\langle P(x, w), V^*(Z) \rangle$ 和

        \[
            \mathcal{com} \from P_1(x, w), \mathcal{ch} \from V_1^*(\mathcal{com}, Z), \mathcal{resp} \from P_2(x, w, \mathcal{ch}), V_2^*(\mathcal{resp}, Z)
        \]

        是一致的.

        因为 $\Sigma$ 是统计诚实验证者零知识的[诚实验证者零知识的]，所以存在量子多项式时间算法 $S_\Sigma$ 使得对于任意[量子多项式时间]的区分器 $D_\Sigma$，有

        \begin{align*}
            \lvert & \op{Pr}[b = 1: \mathcal{com} \from P_1(x, w), \mathcal{ch} \xleftarrow{R} C_{\eta, x}, \mathcal{resp} \from P_2(x, w, \mathcal{ch}), b \hookleftarrow D_\Sigma(\ket{\psi}, \mathcal{com}, \mathcal{ch}, \mathcal{resp})] \\
            - & \op{Pr}[b = 1: (\mathcal{com}, \mathcal{ch}, \mathcal{resp}) \from S_\Sigma(x), b \hookleftarrow D_\Sigma(\ket{\psi}, \mathcal{com}, \mathcal{ch}, \mathcal{resp})] \rvert \leq \varepsilon_D.
        \end{align*}

        