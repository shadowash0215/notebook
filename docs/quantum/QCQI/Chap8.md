# Quantum noise and quantum operations

## Classical noise and Markov processes

设 $p_0$ 和 $p_1$ 是比特初始处于 0 和 1 的概率，$q_0$ 和 $q_1$ 为噪声发生后的相应概率，$X$ 表示比特的初始状态，$Y$ 表示噪声发生后的状态，$p$ 为发生比特翻转的概率. 那么全概率公式指出

\[
    P(Y = y) = \sum_x P(Y = y | X = x) P(X = x),
\]

条件概率 $P(Y = y | X = x)$ 被称为转移概率，因为它们总结了系统中可能发生的变化. 将这些方程写作矩阵形式可以得到

\[
    \begin{pmatrix}
        q_0 \\
        q_1
    \end{pmatrix}
    =
    \begin{pmatrix}
        1 - p & p \\
        p & 1 - p
    \end{pmatrix}
    \begin{pmatrix}
        p_0 \\
        p_1
    \end{pmatrix}.
\]

经典系统中的噪声可以使用随机过程理论来描述. 在多阶段过程的分析中，使用马尔可夫过程通常是一个很好的假设. 对于单阶段过程，输出概率分布 $\mathbf{q}$ 与输入概率分布 $\mathbf{p}$ 之间的关系可以用线性方程

\[
    \mathbf{q} = E \mathbf{p}
\]

描述，其中 $E$ 是转移概率组成的矩阵，称为演化矩阵/转移矩阵. 因此，系统的最终状态 $\mathbf{q}$ 与初始状态 $\mathbf{p}$ 是线性相关的. 这一线性特征将在量子噪声的描述中得到呼应，只不过是用密度矩阵取代了概率分布.

演化矩阵 $E$ 必须具备哪些性质？我们要求：如果 $\mathbf{p}$ 是一个有效的概率分布，那么 $E \mathbf{p}$ 也必须是一个有效的概率分布. 满足这一条件等价于 $E$ 满足两个要求：

- 非负性：$E$ 的所有元素都必须是非负的，即 $E_{ij} \geq 0$.
- 归一性：$E$ 的每一列的元素之和必须为 1，即 $\sum_i E_{ij} = 1$.

总结而言，经典噪声的关键特征如下：输入与输出概率之间存在线性关系，由具有非负性和归一性的转移矩阵描述. 涉及多阶段的经典噪声过程，若噪声由独立环境引起，则可描述为马尔可夫过程. 这些关键特征中的每一个，在量子噪声理论中都有重要的对应物. 当然，量子噪声也会带来一些令人惊讶的新特性. 

## Quantum operations

### Overview

类似于经典状态按方程

\[
    \mathbf{q} = E \mathbf{p}
\]

进行变换，量子态的变换遵循：

\[
    \rho' = \mathcal{E}(\rho),
\]

这个方程中的映射 $\mathcal{E}$ 被称为量子操作. 先前已经遇到过两个简单的量子操作例子：酉变换和测量. 对于它们，$\mathcal{E}$ 的具体形式分别为：

- 酉变换：$\mathcal{E}(\rho) = U \rho U^\dagger$，其中 $U$ 是酉矩阵.
- 测量：$\mathcal{E}_m (\rho) = M_m \rho M_m^\dagger$，其中 $M_m$ 是测量算符.

量子操作 $\mathcal{E}$ 捕获了某个物理过程导致的状态动态变化：$\rho$ 是该过程发生前的初始态，$\mathcal{E}(\rho)$ 是该过程发生后的最终态（可能差一个归一化因子）.

接下来将阐述理解量子操作的三种不同方法，并且最终证明三者是等价的.

- 基于系统-环境相互作用的方法：第一种方法基于将动力学视为系统与环境相互作用的产物来研究，这非常类似于描述经典噪声的方式. 这种方法具体且易于与现实世界联系起来. 然而，它的缺点在于数学上不太方便. 

- 算子和表示法：第二种方法通过提供一种称为算子和表示的强大数学表示形式，克服了第一种方法的数学不便. 这种方法相当抽象，但对于计算和理论工作非常有用. 

- 公理化方法：第三种方法是通过一组基于物理动机的公理进行的. 期望量子力学中的动力学映射能满足这些公理. 这种方法的优点在于它极其普适——它表明在极其广泛的情形下，量子动力学都可以用量子操作来描述. 然而，它不具备第二种方法的计算便利性，也不具备第一种方法的具体性. 

### Environments and quantum operations

封闭量子系统的动力学由酉变换描述. 从概念上讲，可以将酉变换视为一个"黑箱"：输入态进入其中，输出态从中出来. 无需在意黑箱的内部运作方式，它可以通过量子电路、某个哈密顿系统或其他任何方式实现. 

描述开放量子系统动力学的一种自然方式是：将其视为主系统（principal system）与一个环境（environment）之间的相互作用所产生，主系统和环境共同构成一个封闭的量子系统. 换句话说，假设有一个处于状态 $\rho$ 的系统，被送入一个与环境耦合的黑箱. 通常，系统的最终态 $\mathcal{E}(\rho)$ 可能无法通过酉变换与初始态 $\rho$ 相关联. 

假设系统环境的输入为直积态 $\rho \otimes \rho_{\op{env}}$，经过黑箱的酉变换 $U$ 后，系统不再与环境作用，此时便可以对环境进行偏迹操作，得到系统本身的约化态：

\[
    \mathcal{E}(\rho) = \op{Tr}_{\op{env}}(U (\rho \otimes \rho_{\op{env}}) U^\dagger).
\]

当然，如果 $U$ 不涉及任何与环境的相互作用，那么 $\mathcal{E}(\rho) = \tilde{U} \rho \tilde{U}^\dagger$，其中 $\tilde{U}$ 是 $U$ 在系统上的限制. 

一般情况下，系统和环境会持续作用，建立起关联，使得初始状态并非直积态. 关联的一种表现形式便是系统与环境之间的热量交换，一个量子系统如果被孤立放置，它会弛豫到与环境相同的温度，这导致两者之间存在关联.

然而，在许多实际应用场景中，假设系统和环境初始处于直积态是合理的. 当实验人员将量子系统制备到特定状态时，他们解除了该系统与环境之间的所有关联. 理想情况下，这些关联会被完全破坏，使系统处于一个纯态. 即使做不到这一点，稍后也会看到，量子操作形式体系甚至能够描述系统和环境并非起始于直积态时的量子动力学. 

另一个可能提出的问题是：如果环境拥有近乎无限的自由度，该如何指定描述相互作用的酉算子 $U$ 呢？非常有趣的是，结果表明：为了让这个模型能够正确描述任何可能的变换 $\rho \to \mathcal{E}(\rho)$，如果主系统的 Hilbert Space 维度为 $d$，那么只需将环境建模为不超过 $d^2$ 维的 Hilbert Space 就足够了. 而且，环境也无需起始于混合态，一个纯态就足够了. 

考虑一个实际的例子，$U$ 是 CNOT 门，主系统为控制量子比特，环境初始处于状态 $\rho_{\op{env}} \ket{0} \bra{0}$ 为目标量子比特. 将其代入公式可得

\[
    \mathcal{E}(\rho) = P_0 \rho P_0 + P_1 \rho P_1,
\]

其中 $P_0 = \ket{0} \bra{0}$ 和 $P_1 = \ket{1} \bra{1}$ 分别是投影算符. 直观上，这种动力学之所以发生，是因为仅当系统处于 $\ket{0}$ 态时，环境才会处于 $\ket{0}$ 态，否则环境会被翻转为 $\ket{1}$ 态. 

### Operator-sum representation

量子操作也可以用名为算子和的纠缠形式表示，其使用主系统 Hilbert Space 上的算子来对式

\[
    \mathcal{E}(\rho) = \op{Tr}_{\op{env}}(U (\rho \otimes \rho_{\op{env}}) U^\dagger)
\]

重写. 设 $\ket{e}_k$ 为环境状态空间的一组标准正交基，且 $\rho_{\op{env}} = \ket{e_0} \bra{e_0}$ 为环境的初始状态. 不失一般性，设环境的初始状态为纯态，因为如果是混合态的话，可以引入额外的系统进行纯化. 重写为如下式子：

\begin{align*}
    \mathcal{E}(\rho) & = \sum_k (I \otimes \bra{e_k}) U (\rho \otimes \ket{e_0} \bra{e_0}) U^\dagger (I \otimes \ket{e_k}) \\
                      & = \sum_k (I \otimes \bra{e_k}) U [(I \otimes \ket{e_0}) (\rho \otimes 1) (I \otimes \bra{e_0})] U^\dagger (I \otimes \ket{e_k}) \\
                      & = \sum_k (I \otimes \bra{e_k}) U (I \otimes \ket{e_0}) \rho (I \otimes \bra{e_0}) U^\dagger (I \otimes \ket{e_k}) \\
                      & = \sum_k E_k \rho E_k^\dagger,
\end{align*}

其中 $E_k = (I \otimes \bra{e_k}) U (I \otimes \ket{e_0})$ 是作用在主系统上的算子. 这个方程被称为 $\mathcal{E}$ 的算子和表示（operator-sum representation）. $\{E_k\}$ 是 $\mathcal{E}$ 的 Kraus 算子，因为：

\begin{align*}
    1 & = \op{Tr} (\mathcal{E}(\rho)) \\
      & = \op{Tr} \left( \sum_k E_k \rho E_k^\dagger \right) \\
      & = \op{Tr} \left( \sum_k E_k^\dagger E_k \rho \right).
\end{align*}

对所有的 $\rho$ 都成立，因此 $\sum_k E_k^\dagger E_k = I$，这称为完备性条件，由所有保迹的量子操作 $\mathcal{E}$ 满足. 而如果是非保迹的量子操作，则 $\sum_k E_k^\dagger E_k \leq I$，它们描述了在过程中通过测量额外获取了事件发生信息的情况. 这也就提供了量子操作的第二个定义.

#### Physical interpretation of the operator-sum representation

设想在施加酉变换 $U$ 后，我们对环境以基 $\{\ket{e_k}\}$ 进行测量. 应用隐式测量原理（principle of implicit measurement），该测量仅影响环境状态，而不改变主系统状态. 

设 $\rho_k$ 为给定测量结果为 $k$ 时主系统的状态. 那么

\begin{align*}
    \rho_k & \propto \op{Tr}_{\op{env}}(\ket{e_k} \bra{e_k} U (\rho \otimes \ket{e_0} \bra{e_0}) U^\dagger \ket{e_k} \bra{e_k}) \\
           & = \bra{e_k} U (\rho \otimes \ket{e_0} \bra{e_0}) U^\dagger \ket{e_k} \\
           & = E_k \rho E_k^\dagger,
\end{align*}

归一化后得到

\[
    \rho_k = \frac{E_k \rho E_k^\dagger}{\op{Tr}(E_k \rho E_k^\dagger)}.
\]

所以得到结果 $k$ 的概率为

\[
    p(k) = \op{Tr}(\ket{e_k} \bra{e_k} U (\rho \otimes \ket{e_0} \bra{e_0}) U^\dagger \ket{e_k} \bra{e_k}) = \op{Tr}(E_k \rho E_k^\dagger).
\]

所以

\[
    \mathcal{E}(\rho) = \sum_k p(k) \rho_k = \sum_k E_k \rho E_k^\dagger,
\]

这为操作元 $\{E_k\}$ 描述的量子操作提供了优美的物理解释：量子操作的作用等价于将状态 $\rho$ 以概率 $\operatorname{Tr}(E_k \rho E_k^\dagger)$ 随机替换为 $\frac{E_k \rho E_k^\dagger}{\operatorname{Tr}(E_k \rho E_k^\dagger)}$.

在此意义上，它与经典信息论中噪声通信信道 (noisy communication channels) 的概念高度相似. 因此，有时将描述量子噪声过程的量子操作称为噪声量子信道 (noisy quantum channels). 

#### Measurements and the operator-sum representation

给定一个开放量子系统的描述，如何确定其动力学的算子和表示？我们已有一种答案：给定酉系统-环境变换算子 $U$ 和环境的一组基态 $\{\ket{e_k}\}$，操作元为：

\[
    E_k \equiv \bra{e_k} U \ket{e_0}.
\]

此结果可进一步推广：允许在酉相互作用后对系统-环境整体进行测量，从而获取量子态的信息. 这种物理可能性自然与非保迹量子操作相关联，即映射

\[
    \mathcal{E}(\rho) = \sum_k E_k \rho E_k^\dagger
\]

满足

\[
    \sum_k E_k^\dagger E_k \leq I.
\]
 

设主系统初始态为 $\rho$. 为方便起见，将主系统记为 $Q$，环境系统记为 $E$. 假设 $Q$ 与 $E$ 初始独立，且 $E$ 始于某标准态 $\sigma$. 联合系统初始态为：

\[
    \rho^{QE} = \rho \otimes \sigma
\]

系统按酉相互作用 $U$ 演化后，对联合系统进行投影测量，投影算符为 $P_m$. 不测量的情况对应于单一结果 $m = 0$，此时 $P_0 \equiv I$.

目标是确定 $Q$ 的末态作为初始态 $\rho$ 的函数. 联合系统 $QE$ 的末态为：

\[
    \frac{P_m U (\rho \otimes \sigma) U^\dagger P_m}{\op{Tr} \left[P_m U (\rho \otimes \sigma) U^\dagger P_m\right]}
\]

对环境部分进行偏迹，得到主系统 $Q$ 的末态：

\[
    \frac{\op{Tr}_{\op{env}} \left[ P_m U (\rho \otimes \sigma) U^\dagger P_m \right]}{\op{Tr} \left[P_m U (\rho \otimes \sigma) U^\dagger P_m\right]}.
\]

定义映射

\[
    \mathcal{E}_m(\rho) = \op{Tr}_{\op{env}} \left[ P_m U (\rho \otimes \sigma) U^\dagger P_m \right],
\]

所以 $Q$ 最后的状态为 $\mathcal{E}_m(\rho) / \op{Tr} \left[\mathcal{E}_m(\rho)\right]$. 设 $\sigma = \sum_j q_j \ket{j} \bra{j}$ 为 $\sigma$ 的集合分解，引入环境的一组正交基 $\{\ket{e_k}\}$，则

\begin{align*}
    \mathcal{E}_m(\rho) & = \sum_{j,k} q_j \op{Tr} \left[ \ket{e_k} \bra{e_k} P_m U (\rho \otimes \ket{j} \bra{j}) U^\dagger P_m \ket{e_k} \bra{e_k} \right] \\
                        & = \sum_{j,k} E_{jk} \rho E_{jk}^\dagger,
\end{align*}

其中

\[
    E_{jk} = \sqrt{q_j} \bra{e_k} P_m U \ket{j}.
\]

#### System–environment models for any operator-sum representation

可以证明，对任意保迹或不保迹的量子操作 $\mathcal{E}$，其 Kraus 算子为 $\{E_k\}$，都有存在一个环境模型 $E$，以纯态 $\ket{e_0}$ 开始，模型动力学由酉算子 $U$ 和投影算子 $P$ 描述，使得

\[
    \mathcal{E}(\rho) = \op{Tr}_E (P U (\rho \otimes \ket{e_0} \bra{e_0}) U^\dagger P).
\]

首先考虑 $\mathcal{E}$ 是保迹的情况. 所以其 Kraus 算子满足 $\sum_k E_k^\dagger E_k = I$，因而只需要去寻找合适的酉算子就行了. 设 $\ket{e_k}$ 是环境的正交基，且按索引对应于 $E_k$. 定义算子 $U$ 在 $\ket{\psi} \ket{e_0}$ 上的作用为：

\[
    U \ket{\psi} \ket{e_0} = \sum_k E_k \ket{\psi} \ket{e_k}.
\]

$\ket{e_0}$ 只是环境的一个标准态，注意到对主系统的任意量子态 $\ket{\psi}, \ket{\varphi}$ 都有

\[
    \bra{\psi} \bra{e_0} U^\dagger U \ket{\varphi} \ket{e_0} = \sum_k \bra{\psi} E_k^\dagger E_k \ket{\varphi} = \innerproduct{\psi}{\varphi},
\]

所以 $U$ 保持主系统的内积不变，进而可以扩展为复合系统的状态空间上的酉算子. 容易验证：

\[
    \op{Tr}_E (P U (\rho \otimes \ket{e_0} \bra{e_0}) U^\dagger P) = \sum_k E_k \rho E_k^\dagger.
\]

### Axiomatic approach to quantum operations

