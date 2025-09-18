# Random Oracles in a Quantum World

!!! info "Abstract"
    - 原文链接：[Random Oracles in a Quantum World](https://eprint.iacr.org/2010/428.pdf)

    - 只对论文主体部分以及影响理解的部分进行了翻译，摘要，介绍，总结等部分未翻译.

    - 整体思路为给出分离结果，构建无历史规约，运用无历史规约证明签名方案的安全性，最后对部分加密方案安全性进行证明.

## Preliminaries

一非负函数 $\varepsilon = \varepsilon(n)$ 是一个**可忽略(negligible)**函数，如果对于所有的多项式 $p(n)$，存在一个 $N$，使得对于所有的 $n > N$，有 $\varepsilon(n) < p(n)^{-1}$.而对于 $\Omega$ 上的两个分布 $D_1$ 和 $D_2$，二者之间的**变差距离(variational distance)**定义为

\[
    \abs{D_1 - D_2} = \sum_{x \in \Omega} \abs{\Pr{x \mid D_1} - \Pr{x \mid D_2}}
\]

如果两个分布之间的距离为 $\varepsilon$，那么二者关于输出满足某种特定性质的概率之差不会超过 $\varepsilon$.

一个经典的随机算法 $A$ 可以用如下两种方式去运用：

1. $A$ 被给定输入 $x$，并在计算中进行一些随机处理（如掷硬币），最终输出一个结果 $y$，记作 $A(x)$，其为一个随机变量.

2. $A$ 被给定输入 $x$ 和随机值 $r$，并输出一个结果 $y$，记作 $A(x; r)$，其为一个确定值.

算法 $A$ 被认为是 Probabilistic Polynomial Time ($\op{PPT}$) 的，如果其在 security parameter 上运行的时间是多项式的.

### Quantum Computation

一个量子系统 $A$ 是与一个有限维复 Hilbert 空间 $\mathcal{H}_A$ 相关联的，其上的内积为 $\innerproduct{\cdot}{\cdot}$.系统的状态向量可以用 $\ket{\varphi} \in \mathcal{H}_A$ 表示，其满足欧几里得范数 $\norm{\ket{\varphi}} = \sqrt{\innerproduct{\varphi}{\varphi}} = 1$.

给定量子系统 $A$ 和 $B$，其 Hilbert 空间分别为 $\mathcal{H}_A$ 和 $\mathcal{H}_B$，则 $A$ 和 $B$ 的**复合**是通过张量积 $\otimes$ 定义的，空间为 $\mathcal{H}_A \otimes \mathcal{H}_B$.对于两个态 $\ket{\varphi_A} \in \mathcal{H}_A$ 和 $\ket{\varphi_B} \in \mathcal{H}_B$，其复合态为 $\ket{\varphi_A} \otimes \ket{\varphi_B} \in \mathcal{H}_A \otimes \mathcal{H}_B$.一个 $n$ 量子比特系统的 Hilbert 空间是建立在 $n$ 个二维复 Hilbert 空间的复合上的，对于这样的系统，其标准正交计算基 $\ket{x}$ 由 $\ket{x_1} \otimes \cdots \otimes \ket{x_n}$ 给出，其中 $x = x_1 \cdots x_n$ 是一个 $n$ 位二进制串.任意一个二进制串都可以编码为一个态 $\ket{x}$，而任意的 $n$ 量子比特的纯态都可以用计算基表示为 $\ket{\varphi} = \sum_{x \in \{0, 1\}^n} \alpha_x \ket{x}$，其中 $\alpha_x$ 为复振幅满足 $\sum_{x \in \{0, 1\}^n} \abs{\alpha_x}^2 = 1$.

而量子系统的变化都是通过酉变换描述的.记 $\mathbb{I}_A$ 为系统 $A$ 上的恒等变换.对于复合量子系统 $\mathcal{H}_A \otimes \mathcal{H}_B$ 以及 $\mathcal{H}_A$ 上的酉变换 $U_A$，$U_A \ket{\varphi_A} \ket{\varphi_B}$ 实际上表示 $(U_A \otimes \mathbb{I}_B) \ket{\varphi_A} \ket{\varphi_B}$.

信息的提取依靠的是对量子态 $\ket{\varphi}$ 进行测量，其中一种测量方式称为 POVM (Positive Operator-Valued Measure).一个 POVM $M = \{M_i\}$ 是一组半正定测量算子，满足和为恒等算子，即 $\sum_i M_i = \mathbb{I}$.结果 $i$ 的概率为 $p_i = \bra{\varphi} M_i \ket{\varphi}$.特殊的例子是投影测量，量子态满足 $\ket{\varphi} = \sum_x \alpha_x \ket{x}$，结果为 $x$ 的概率为 $\abs{\alpha_x}^2$.

同样，也可以只对量子态的部分位进行测量，但直接计算得到的量子态的范数不为 1，所以需要规范化.比如考虑测量 $\ket{\psi} = \sum_{x, y} \alpha_{x, y} \ket{x, y}$ 的前 $n$ 位，那么得到结果 $x$ 的概率便是 $\sum_{y'} \abs{\alpha_{x, y'}}^2$，而规范化后的态为

\[
    \ket{x} \sum_y \frac{\alpha_{x, y}}{\sqrt{\sum_{y'} \abs{\alpha_{x, y'}}^2}} \ket{y}
\]

此外，也需要对量子攻击者 $\mathcal{A}_Q$ 进行建模，方法是通过一系列在 $k = \poly{n}$ 个量子比特上的酉变换 $U_1, O_1, U_2, O_2, \ldots, O_{T - 1}, U_T$ 来描述其行为，该攻击者能够访问的 Oracles 为 $O_1, O_2, \ldots$.这些 Oracles 满足 $O_i: \{0, 1\}^n \to \{0, 1\}^m$，并且将前 $n + m$ 位的输入从基态 $\ket{x}\ket{y}$ 映射到 $\ket{x}\ket{y \oplus O_i(x)}$，$\ket{x} \in \{0, 1\}^n$，$\ket{y} \in \{0, 1\}^m$.如果希望对 $O_i$ 的查询是经典的，那么只需要在施加相应于 $O_i$ 的酉变换之前对输入进行测量即可.此外，也经常用 $\mathcal{A}_Q^{\ket{O_1(\cdot)}, \ket{O_2(\cdot)}, \ldots}$ 符号来表示这些 Oracles 是量子可访问的.

为了引进渐进分析，假定 $\mathcal{A}_Q$ 是一系列酉变换的序列，由参数 $n$ 索引，并且每个酉变换序列由输入、输出、Oracles 调用以及工作空间的量子系统组成.而为了衡量多项式运行时间，假定 $U_i$ 都可以用一组通用门以足够的精度进行近似，而且这些通用门的数量是多项式的.此外，$T = T(n)$ 也是多项式的.

定义量子态之间的欧式距离为 $\abs{\ket{\varphi} - \ket{\psi}} = \left( \sum_x \abs{\alpha_x - \beta_x}^2 \right)^{1/2}$，其中 $\ket{\varphi} = \sum_x \alpha_x \ket{x}$，$\ket{\psi} = \sum_x \beta_x \ket{x}$.定义 $q_r(\ket{\varphi_t})$ 为第 $t$ 次查询的叠加态中 $r$ 的振幅的平方，也被称为第 $t$ 次查询中 $r$ 的查询概率.

!!! success "Lemma"
    设量子态 $\ket{\varphi}$ 和 $\ket{\psi}$ 之间的欧式距离至多为 $\varepsilon$，则在二者上进行相同的测量，得到的分布之间的统计距离至多为 $4 \varepsilon$.

!!! success "Lemma"
    设 $A_Q$ 是一个运行时间为 $T$ 且可访问 Oracle 为 $O$ 的量子算法.设 $\varepsilon > 0$ 且 $S \subset [1, T] \times \{0, 1\}^n$ 是一个时间-字符串对的集合，满足

    \[
        \sum_{(t, r) \in S} q_r(\ket{\psi_t}) \leq \varepsilon.
    \]

    如果将 $O$ 修改为 $O'$，使得其在时间 $t$ 时查询 $r$ 的回复都是一个相同的随机独立采样的字符串 $R$，那么 $A_Q$ 分别调用 $O$ 和 $O'$ 的最终状态之间的欧式距离至多为 $\sqrt{T \varepsilon}$.

### Quantum-Accessible Random Oracles

!!! info "Definition"
    **(Pseudorandom Function)** 一个量子可访问的伪随机函数是一个可以高效计算的函数 $\PRF$，满足对于所有高效的量子算法 $D$，有

    \[
        \abs{\Pr{D^{\PRF(k, \cdot)}(1^n) = 1} - \Pr{D^{O(\cdot)}(1^n) = 1}} < \varepsilon,
    \]

    其中 $\varepsilon = \varepsilon(n)$ 是一个可忽略函数，$O$ 是一个随机 Oracle. 第一个概率是分布在长度为 $n$ 的密钥 $k$ 上的，第二个概率是分布在所有随机 Oracles 和 $D$ 的输出的采样上的.

称一 Oracle $O'$ 与一个随机 Oracle $O$ 是**计算上不可区分的(computationally indistinguishable)**，如果对于所有的可访问 Oracle 的多项式时间量子算法 $D$，当 Oracle 为 $O'$ 的输出分布与 Oracle 为 $O$ 的输出分布之间的变差距离是可忽略的.

### Hard Problems for Quantum Computers

!!! info "Definition"
    **(Problem)** 一个问题是一个二元组 $P = (\op{Game}_P, \alpha_P)$，其中 $\op{Game}_P$ 描述了一个 Game，其敌手可能是量子的而挑战者是经典的. 这一 Game 按如下规则进行：

    - 输入 $1^n$，挑战者计算出一个值 $x$，并将其发送给敌手，作为输入；

    - 敌手以 $x$ 为输入运行，并且允许向挑战者进行经典查询；

    - 敌手输出一个值 $y$，并将其发送给挑战者；

    - 挑战者根据 $x$ 和 $y$ 以及敌手进行的经典查询，输出一个比特 $1$ 或 $0$.

    $\alpha_P$ 是一个 $[0, 1)$ 上的实数，其有可能是 $n$ 的一个函数，但此处只需要常数 $\alpha_P$，具体来说 $\alpha_P$ 总是 $0$ 或 $\frac{1}{2}$.

称敌手 $A$ 赢得了 Game $\op{Game}_P$，如果挑战者输出了 $1$. 定义敌手 $A$ 在问题 $P$ 中的优势为

\[
    \Adv_{A, P} = \abs{\Pr{A \text{ wins in } \op{Game}_P} - \alpha_P}.
\]

!!! info "Definition"
    **(Hard Problem)** 一个问题 $P = (\op{Game}_P, \alpha_P)$ 对量子计算机是困难的，如果对于所有的多项式时间量子敌手 $A$，其优势 $\Adv_{A, P}$ 是可忽略的.

### Cryptographic Primitives

一个陷门函数 $\mathcal{F}$ 是安全的，如果 $\op{Inv}(\mathcal{F}) = (\op{Game}_{\op{Inv}}(\mathcal{F}), 0)$ 对量子计算机是困难的. 其中在 $\op{Game}_{\op{Inv}}$ 中，敌手被给出了一个随机元素 $y$ 和公钥，若其能够给出 $y$ 关于公钥的逆便算成功. 而对于原像可采样陷门函数(Preimage Sampleable Trapdoor Function) $\mathcal{F}$，其安全性不仅需要 $\op{Inv}(\mathcal{F})$ 是困难的，还需要 $\op{Col}(\mathcal{F}) = (\op{Game}_{\op{Col}}(\mathcal{F}), 0)$ 是困难的. $\op{Game}_{\op{Col}}$ 给出了公钥，敌手需要输出两个不同的 $x_1$ 和 $x_2$，使得 $\mathcal{F}(x_1) = \mathcal{F}(x_2)$，即找到了一个碰撞.

对于签名方案 $\mathcal{S}$ 而言，其安全性需要满足 $\op{Sig-Forge}(\mathcal{S}) = (\op{Game}_{\op{Sig}}(\mathcal{S}), 0)$ 是困难的. $\op{Game}_{\op{Sig}}$ 是在选择明文攻击下的标准存在不可伪造性博弈. 最后，对于私钥（公钥）加密方案 $\mathcal{E}$，如果 $\op{Sym-CCA}(\mathcal{E}) = (\op{Game}_{\op{Sym}}(\mathcal{E}), \frac{1}{2})$ ($\op{ASym-CCA}(\mathcal{E}) = (\op{Game}_{\op{ASym}}(\mathcal{E}), \frac{1}{2})$) 是困难的，那么称其是安全的，其中 $\op{Game}_{\op{Sym}}$ ($\op{Game}_{\op{ASym}}$) 是标准的私钥（公钥）选择密文攻击博弈.

??? tip "[What does existential unforgeability mean in a digital signature scheme?](https://crypto.stackexchange.com/questions/91489/what-does-existential-unforgeability-mean-in-a-digital-signature-scheme)"
    *"Existential unforgeability" alone means adversaries can't create signatures that verify for messages they have not already a signature for. Strictly speaking, breaking existential unforgeability may only mean adversaries end up with a message and signature that verify, but the message is gibberish void of any use for the adversaries.*

    *There is also "strong existential unforgeability", which additionally means adversaries can't create new signatures that verify, against any message.*

## Separation Result

### Preliminaries

- **身份验证方案（Identification Scheme）**：身份验证方案 $\op{IS}$ 是一个三元组 $(\op{IS}.\mathsf{KGen}, \mathcal{P}, \mathcal{V})$. 其中 $\op{IS}.\mathsf{KGen}$ 输入 $1^n$，输出一个密钥对 $(\sk, \pk)$；$\mathcal{P}(\sk, \pk)$ 和 $\mathcal{V}(\pk)$ 定义了证明者 $\mathcal{P}$ 和验证者 $\mathcal{V}$ 之间的交互式协议，最终 $\mathcal{V}$ 输出 $1$ 或 $0$，表示验证成功或失败. 假定这个协议是完备的，即对于所有诚实的证明者 $\mathcal{P}$，验证者 $\mathcal{V}$ 总是接受. 而其安全性证明则是考虑敌手 $\mathcal{A}$，一阶段先和 $\mathcal{P}$ 交互，获取 $\sk$ 的信息，然后在第二阶段与 $\mathcal{V}$ 交互，使得其输出 $1$. 如果敌手能让 $\mathcal{V}$ 输出 $1$ 的概率是可忽略的，那么称 $\op{IS}$ 是可靠的（sound）.

- **（近似）碰撞抗性哈希函数（(Near-) Collision-Resistant Hash Function）**： 哈希函数 $\op{H} = (\op{H}.\mathsf{KGen}, \op{H}.\mathsf{Eval})$ 是一对高效的算法，满足 $\op{H}.\mathsf{KGen}(1^n)$ 输出一个密钥 $k$，$\op{H}.\mathsf{Eval}$ 以 $k$ 和 $M \in \{0, 1\}^*$ 为输入，确定性地输出一个摘要（digest）$h = \op{H}.\mathsf{Eval}(k, M)$. 对于随机 Oracle $H$，$k$ 被用作“盐”，并且常考虑 $H(k, \cdot)$ 这一随机函数. 而近似碰撞抗性哈希函数则需要满足对任意高效的算法 $\mathcal{A}$，$k \from \op{H}.\mathsf{KGen}(1^n)$，某常数 $1 \leq l \leq n$，有

    \begin{gather*}
        (M, M') \from \mathcal{A}(k, l) \\
        M \neq M' \land \op{H}.\mathsf{Eval}(k, M) \mid_{l} = \op{H}.\mathsf{Eval}(k, M') \mid_{l}
    \end{gather*}

    的概率是可忽略的. 这里的 $x \mid_l$ 表示 $x$ 的前 $l$ 位. 

    在经典情况下，任意哈希函数的（近似）碰撞抗性都被生日攻击所约束. 生日攻击阐明对任意 $n$ 位输出的哈希函数，攻击者在尝试 $2^{n/2}$ 次互异且随机的输入后，有大约 $1/2$ 的概率找到碰撞. 

- **Grover 算法和量子碰撞搜索（Grover's Algorithm and Quantum Collision Search）**：Grover 算法在未结构化的 $N$ 个元素的数据库上进行搜索，其时间复杂度为 $O(\sqrt{N})$，而最优的经典算法的时间复杂度为 $O(N)$. 粗略地说，这是依靠的是叠加态能够在同一时间检查所有条目. 这一思路也同样可以用于检索哈希函数的碰撞. 考虑 $H: \{0, 1\}^* \to \{0, 1\}^n$，首先选择 $K \subset \{0, 1\}^*$，然后在一指示函数 $f$ 上运用 Grover 算法，来检查对于任意输入 $M \in \{0, 1\}^* \setminus K$，是否存在 $M' \in K$ 使得 $H(M) = H(M')$. 通过设置 $\abs{K} = \sqrt[3]{2^n}$，该算法可以在 $O(\sqrt[3]{2^n})$ 时间内以至少 $1/2$ 的概率找到碰撞.

- **计算与时间假设（Computational and Timing Assumptions）**：此处对敌手的计算能力和量子计算机与经典计算机的时间流逝进行规范.

    1. 要求并行计算得到的加速比是被一个固定项所约束的. 换言之，不可能无限加速. 

        !!! success "Assumption"
            **(Parallel Speed-Up)** 记 $T(C)$ 为经典计算机解决问题 $C$ 所需的时间，$T_P(C)$ 为并行计算机解决问题 $C$ 所需的时间. 那么存在常数 $\alpha \geq 1$，使得对于所有问题 $C$，有 $T_P(C) \geq T(C) / \alpha$.

    2. 以下两个假设是关于哈希函数的计算与两方通信的时间流逝的. 

        !!! success "Assumption"
            **(Unit Time)** 对任意哈希函数 $H$，和任意输入 $M$($M_Q$ 用作量子态输入)，$H(M)$ 的计算需要一个恒定的时间，满足 $T(H(M)) = T_P(H(M)) = T_Q(H(M_Q))$，其中 $T_P$ 和 $T_Q$ 分别是并行计算机和量子计算机的计算时间. 

        !!! success "Assumption"
            **(Zero Time)** 任何不涉及哈希函数计算的计算或动作都是瞬时完成的.

        后者阐明量子计算机可能在其他方面获得的计算优势与哈希函数的计算时间相比是可忽略的.

### Construction

开始构建证明者 $\mathcal{P}$ 和验证者 $\mathcal{V}$ 之间的身份验证方案 $\op{IS}$，主要思想是通过增加一个哈希函数的碰撞发现阶段来增强其安全性. 

1. 验证者检查证明者能否在特定的时间内产生哈希函数的碰撞. 更具体而言，验证者对消息 $\langle c \rangle$ 计算哈希函数 $\op{H}.\mathsf{Eval}(k, \cdot)$，并进行计时，其中 $c = 1, 2, \ldots, \lceil \sqrt[3]{2^l} \rceil$，并且 $\langle c \rangle$ 是 $c$ 的二进制表示，长度为 $\log \lceil \sqrt[3]{2^l} \rceil$ 位. 证明者需要回复一个近似碰撞，即 $M \neq M'$ 但 $\op{H}.\mathsf{Eval}(k, M) \mid_l = \op{H}.\mathsf{Eval}(k, M') \mid_l$. 如果验证者收到了这样的一个碰撞，或是 $\sqrt[3]{2^l}$ 次哈希函数计算完成，则碰撞阶段结束. 验证者和证明者随后重复 $r = \poly{n}$ 次这一过程，并且每次验证者都会选择一个新的密钥 $k$.

2. 随后，两方按照标准的身份验证方案进行交互. 

3. 最后，如果证明者能够找到足够多的碰撞，或者在标准的身份验证方案中成功，那么验证者接受.

该协议 $\op{IS}^*$ 的完备性可自然地从 $\op{IS}$ 的完备性推导出来. 而其安全性则需要针对经典敌手和量子敌手分别进行分析. 证明过程即敌手 $\mathcal{A}$ 与诚实的证明者 $\mathcal{P}^*$ 交互后，并不能够冒充 $\mathcal{P}^*$ 通过 $\mathcal{V}^*$ 的验证.

设 $l > 6\log(\alpha)$，其中 $\alpha$ 是并行假设中的常数. 通过假定 $\op{IS}$ 是一个量子免疫身份验证方案，便可以证明 $\op{IS}^*$ 在标准的随机 Oracle 模型下是安全的，无论是对于经典敌手还是量子敌手. 

主要的想法在于对于随机 Oracle 模型，碰撞搜索的能力还是被生日攻击所约束的. 因为限制了搜索时间为 $O(\sqrt[3]{2^k})$，并且有 $l > 6\log(\alpha)$，所以即便敌手拥有量子或并行的计算能力，也不可能进行至少 $\sqrt{2^l}$ 次的随机 Oracle 访问. 因而，$\mathcal{A}$ 能够在 $r$ 轮中找到至少 $1/4$ 的碰撞的概率是可忽略的.

对于经典敌手 $\mathcal{A}$ 而言，这样的一个随机 Oracle 是可以实例化的，只需要利用接近于生日攻击约束上界的近似碰撞抗性哈希函数 $H$ 即可. 但对量子敌手 $\mathcal{A}_Q$ 而言，这样的哈希函数实例化是不存在的，因为 $\mathcal{A}_Q$ 可以在本地应用 Grover 算法来找到碰撞，并且在 $\sqrt[3]{2^l}$ 时间内找到碰撞的概率至少为 $1/2$. 而对于有量子可访问随机 Oracle 的敌手而言，这也是不安全的，因为 Grover 算法只要求对哈希函数的黑箱访问.

## Signature Schemes in the Quantum-Accessible Random Oracle Model

接下来给出的是经典随机 Oracle 安全性转化为量子可访问随机 Oracle 安全性的条件，被称为**无历史规约（history-free reduction）**，具体而言，Oracle 对于查询的回复与先前的查询以及查询序号无关.

!!! info "Definition"
    **(History-Free Reduction)** 如果一个随机 Oracle 签名方案 $\mathcal{S} = (G, S^O, V^O)$ 存在安全性证明使用 $\mathcal{S}$ 的经典 $\op{PPT}$ 敌手 $A$ 为困难问题 $P = (\op{Game}_P, 0)$ 构建经典 $\op{PPT}$ 算法 $B$，且满足以下条件：

    - $B$ 包含四部分经典算法：$\op{START}$, $\op{RAND}^{O_C}$, $\op{SIGN}^{O_C}$ 和 $\op{FINISH}^{O_C}$，后三者可以共享访问一个经典的随机 Oracle $O_C$. 除去 $\op{RAND}^{O_C}$，其余算法可以向问题 $P$ 的挑战者发送查询. 以下是算法的应用规则：

        1. 给定问题 $P$ 的一个实例 $x$ 作为输入，算法 $B$ 首先运行 $\op{START}(x)$，来获取 $(\pk, z)$，其中 $\pk$ 是公钥，$z$ 是一个可供 $B$ 使用的私有态. $B$ 将 $\pk$ 发送给 $A$，并扮演挑战者的角色.

        2. 当 $A$ 向 $O(r)$ 发送经典随机 Oracle 查询时，$B$ 会调用 $\op{RAND}^{O_C}(r, z)$ 来获取回复. 注意 $\op{RAND}$ 只使用当前查询作为输入，对先前的查询和回复无感知.

        3. 当 $A$ 发出经典签名查询 $S(\sk, m)$ 时，$B$ 会调用 $\op{SIGN}^{O_C}(m, z)$ 来获取签名并回复给 $A$.

        4. 当 $A$ 输出一个可能的伪造签名 $(m, \sigma)$ 时，$B$ 输出 $\op{FINISH}^{O_C}(m, \sigma, z)$.

    - 存在高效的可计算函数 $\op{INSTANCE}(\pk)$，能够给出问题 $P$ 的实例 $x$，并且存在 $z$ 使得 $\op{START}(x) = (\pk, z)$. 考虑整个过程，首先利用 $G(1^n)$ 生成 $(\pk, \sk)$，然后运行 $\op{INSTANCE}(\pk)$ 来获取 $x$，这样生成的 $x$ 的分布与 $\op{Game}_P$ 生成的 $x$ 的分布之间的变差距离是可忽略的.

    - 对固定的 $z$，考虑经典随机 Oracle $O(r) = \op{RAND}^{O_C}(r, z)$，定义一个量子 Oracle $O_{\op{quant}}$，由 $\ket{x, y} \mapsto \ket{x, y \oplus O(x)}$ 给出，要求其与随机 Oracle 是量子计算上不可区分的.

    - $\op{SIGN}^{O_C}$ 要么中止（因而使得 $B$ 中止），要么输出一个关于 Oracle $O(r) = \op{RAND}^{O_C}(r, z)$ 的有效签名，并且其分布与正确的签名分布之间的变差距离是可忽略的，并且需要没有任何一个签名查询中止的概率是不可忽略的.

    - 如果 $(m, \sigma)$ 是一个关于公钥 $\pk$ 和 Oracle $O(r) = \op{RAND}^{O_C}(r, z)$ 有效的伪造签名，那么 $B$ 的输出，即 $\op{FINISH}^{O_C}(m, \sigma, z)$，使得 $P$ 的挑战者输出 $1$ 的概率是不可忽略的.

    那么称 $\mathcal{S}$ 存在一个无历史规约.

下面给出无历史规约推出量子安全性的定理.

!!! note "Theorem"
    设 $\mathcal{S} = (G, S, V)$ 是一个签名方案，其存在一个无历史规约. 若问题 $P$ 对于多项式量子计算机是困难的，且量子可访问伪随机函数是存在的，那么 $\mathcal{S}$ 在量子可访问随机 Oracle 模型下是安全的.

    ???+ note "Proof"
        使用一系列的 $\op{Game}$ 进行证明.

        - **Game 0**：定义 $\op{Game}_0$ 为量子敌手 $A_Q$ 在问题 $\op{Sig-Forge}(\mathcal{S})$ 上的博弈. 为了制造反例，假定 $A_Q$ 的优势是不可忽略的.

        - **Game 1**：在 $\op{Game}_0$ 上进行修改，定义 $\op{Game}_1$. 要求挑战者生成 $(\sk, \pk)$ 后，计算出 $x \from \op{INSTANCE}(\pk)$ 以及 $(\pk, z) \from \op{START}(x)$. 并且，当 $A_Q$ 向量子随机 Oracle 发送查询时，改为使用量子可访问随机 Oracle $O_{\op{quant}}$ 进行模拟. 其将 $\ket{x, y}$ 映射到 $\ket{x, y \oplus \op{RAND}^{O_q}(x, z)}$，其中 $O_q$ 是一个真正的量子可访问随机 Oracle. 因为无历史规约保证了 $O_{\op{quant}}$ 对于量子敌手而言是计算上不可区分的，也就是说，$A_Q$ 在 $\op{Game}_1$ 上获胜的概率与其在 $\op{Game}_0$ 上获胜的概率的差距是可忽略的，从而整个概率是不可忽略的.

        - **Game 2**：在 $\op{Game}_1$ 上进行修改，$\op{Game}_2$ 不再自行生成 $(\sk, \pk)$，以及计算 $x \from \op{INSTANCE}(\pk)$，而是通过运行问题 $P$ 的挑战者开始，当其发送 $x$ 后，便运行 $\op{Game}_1$ 的挑战者，以 $x$ 作为输入. 并且，当 $A_Q$ 查询 $m$ 的签名时，使用 $\op{SIGN}^{O_q}(m, z)$ 进行回复. 因为 $\op{INSTANCE}$ 本身是无历史规约的一部分，$x$ 的计算方法的改变带来的分布变化是可忽略的. 而后，只要所有的签名算法都成功了，那么如何回复签名查询是无关紧要的. 所以，$A_Q$ 成功的概率是以下两个概率之乘积：

            - 所有签名都成功回复，没有中止的概率；

            - 假定所有签名都成功回复，$A_Q$ 能够伪造有效签名的概率.

            根据假设，第一个概率是不可忽略的，第二个概率与 $A_Q$ 在 $\op{Game}_1$ 上获胜的概率的差距是可忽略的，因此整个概率是不可忽略的.

        - **Game 3**：$\op{Game}_3$ 在 $\op{Game}_2$ 上做了两处修改，一是其为量子可访问 $\PRF$ 生成了密钥 $k$，二为挑战者通过施加酉变换，将 $\ket{x, y}$ 映射到 $\ket{x, y \oplus \PRF(k, x)}$，来回复随机 Oracle 查询 $O_q(\ket{\psi})$. 如果 $\op{Game}_3$ 的成功概率与 $\op{Game}_2$ 的成功概率的差距是不可忽略的话，那就可以为 $\PRF$ 构建一个区分器，其同时扮演敌手 $A_Q$ 和挑战者的角色. 所以，$\op{Game}_3$ 的成功概率与 $\op{Game}_2$ 的成功概率的差距是可忽略的.

        而根据 $\op{Game}_3$ 中拥有不可忽略的优势的量子敌手，便可以构建一个可以攻破问题 $P$ 的量子算法 $B_Q$. 当 $B_Q$ 从问题 $P$ 的挑战者处接收到实例 $x$ 后，便可以计算出 $(\pk, z) \from \op{START}(x)$，并且生成 $\PRF$ 的密钥 $k$. 然后，其以 $\pk$ 为输入模拟 $A_Q$. $B_Q$ 使用 $\op{RAND}^{\PRF(k, \cdot)}$ 构建得到的量子可访问函数来回复随机 Oracle 查询，如同 $\op{Game}_1$ 中一样；至于签名查询，其使用 $\op{SIGN}^{\PRF(k, \cdot)}$ 来回复. 当 $A_Q$ 输出一个可能的伪造签名 $(m, \sigma)$ 时，$B_Q$ 输出 $\op{FINISH}^{\PRF(k, \cdot)}(m, \sigma, z)$，并将该输出返回给问题 $P$ 的挑战者. 

        因为 $\op{Game}_3$ 中的 $A_Q$ 行为和 $B_Q$ 中的子例程是相同的，所以 $A_Q$ 会输出一个有效的伪造签名的概率是不可忽略的. 而一旦 $(m, \sigma)$ 是有效的伪造签名，因为 $\op{FINISH}$ 也是无历史规约的一部分，$\op{FINISH}^{\PRF(k, \cdot)}(m, \sigma, z)$ 会使得问题 $P$ 的挑战者输出 $1$ 的概率是不可忽略的. 这样，$B_Q$ 就成功地攻破了问题 $P$，这与问题 $P$ 是困难的矛盾. 因此，任何多项式时间的量子算法在 $\op{Sig-Forge}(\mathcal{S})$ 上的优势是可忽略的，从而证明了定理.

### Secure Signatures From Preimage Sampleable Trapdoor Functions (PSF)

下面利用无历史规约这一定理证明利用原像可采样陷门函数构建的全域哈希签名方案是安全的. 粗略来说，$\op{PSF}$ $\mathcal{F}$ 是一个由 $\op{PPT}$ 算法组成的元组 $(G, \op{Sample}, f, f^{-1})$. $G(\cdot)$ 生成一个密钥对 $(\sk, \pk)$，$f(\pk, \cdot)$ 是一个可高效计算的函数，而 $f^{-1}(\sk, y)$ 从 $y$ 的原像集中随机采样，$\op{Sample}(\pk)$ 从 $f(\pk, \cdot)$ 的定义域中随机采样得到 $x$，从而使得 $f(\pk, x)$ 在 $f(\pk, \cdot)$ 的值域中在统计意义上接近于均匀分布. 这一 $\op{PSF}$ 不仅是单向的，同时也是具有碰撞抗性的.

!!! info "Definition"
    **(Full Domain Hash)** 设 $\mathcal{F} = (G, f, f^{-1})$ 是一个陷门置换函数，并且 $O$ 是一个值域与 $f$ 相同的哈希函数. 全域哈希签名方案 $\mathcal{S} = (G, S, V)$ 按如下方式定义：

    - $G = G_0$

    - $S^O(\sk, m) = f^{-1}(\sk, O(m))$

    - $V^O(\pk, m, \sigma) = \begin{cases} 1, & \text{if } O(m) = f(\pk, \sigma) \\ 0, & \text{otherwise} \end{cases}$

[[GPV08]](https://eprint.iacr.org/2007/432.pdf) 给出了 $\op{FDH}$ 签名方案可以用 $\op{PSF}$ 替代陷门置换函数来构建，称为 $\op{FDH-PSF}$ 系统.

考虑一个从 $\op{FDH-PSF}$ 签名方案的经典敌手 $A$ 到 $\mathcal{F}$ 的碰撞搜索算法 $B$ 的规约：

- 输入 $\pk$ 后，$B$ 计算 $\op{START}(\pk) = (\pk, \pk)$，并以 $\pk$ 为输入模拟 $A$.

- 当 $A$ 查询 $O(r)$ 时，$B$ 按如下计算并回复：

    \[
        \op{RAND}^{O_C}(r, \pk) := f(\pk, \op{Sample}(1^n; O_c(r)))
    \]

- 当 $A$ 查询 $S(\sk, m)$ 时，$B$ 按如下计算并回复：

    \[
        \op{SIGN}^{O_C}(m, \pk) := \op{Sample}(1^n; O_c(m))
    \]

- 当 $A$ 输出 $(m, \sigma)$ 时，$B$ 按如下计算并回复：

    \[
        \op{FINISH}^{O_C}(m, \sigma, \pk) := (\op{Sample}(1^n; O_c(m)), \sigma)
    \]

此外，定义 $\op{INSTANCE}(pk) = \pk$. 

显然 $\op{INSTANCE}$ 和 $\op{START}$ 满足无历史规约的要求. 

!!! success "Lemma"
    设 $A$ 是一个进行 $q$ 次量子查询的量子算法. 进一步，假设从两个分布中抽取 Oracle $O$，第一个分布是一个随机 Oracle 分布，第二个分布是 Oracle 在每个输入 $x$ 处的值独立同分布地由某个分布 $D$ 所生成而形成的分布，并且 $D$ 与均匀分布的变差距离不超过 $\varepsilon$. 那么，$A$ 使用两种 Oracle 的输出分布之间的变差距离不超过 $4q^2 \sqrt{\varepsilon}$.

以上引理表明可以使用一个依据近似于均匀分布的分布 $D$ 生成的 Oracle $O_D$ 替代真正的随机 Oracle $O$，而不会对 $A$ 的行为产生影响. 不过，尽管这对 $A$ 的输出的影响可以忽略，但造成的影响依然比经典情况下的影响要大. 经典情况的影响为 $q \varepsilon$，而量子情况下的影响为 $4q^2 \sqrt{\varepsilon}$. 所以，使用以上引理的量子安全规约往往不像其对应的经典规约的约束那样严格.

!!! note "Theorem"
    上述提到的 $\op{FDH-PSF}$ 签名方案上的规约是无历史的. 

    ???+ note "Proof"
        $\op{PSF}$ 的定义表明 $f(\pk, \op{Sample}(1^n))$ 的分布与均匀分布的变差距离小于 $\varepsilon_{\op{Sample}}$，其值可忽略. 因为 $O(r) = \op{RAND}^{O_C}(r, \pk) = f(\pk, \op{Sample}(1^n; O_C(r)))$，且 $O_C$ 是一个真正的随机 Oracle，所以 $O(r)$ 的分布独立于其他输入，并且与均匀分布的变差距离不超过 $\varepsilon_{\op{Sample}}$. 定义一量子 Oracle $O_{\op{quant}}$，其将 $\ket{x, y}$ 映射到 $\ket{x, y \oplus O(x)}$. 根据上述引理，对于任意进行 $q$ 次随机 Oracle 查询的算法 $B$ 而言，其使用真正的随机 Oracle 所产生的输出的分布与其使用“不那么”随机的 Oracle $O_{\op{quant}}$ 所产生的输出的分布之间的变差距离不超过 $4q^2 \sqrt{\varepsilon_{\op{Sample}}}$，依然是可忽略的. 因此，$O_{\op{quant}}$ 与随机 Oracle 是计算上不可区分的.

        [[GPV08]](https://eprint.iacr.org/2007/432.pdf) 还表明，对于所有查询，$\op{SIGN}^{O_C}(m, \pk)$ 与 $\op{RAND}^{O_C}(\cdot, \pk)$ 是相一致的，并且如果 $A$ 输出一个有效的伪造签名 $(m, \sigma)$，那么 $\op{FINISH}^{O_C}(m, \sigma, \pk)$ 产生 $\mathcal{F}$ 的一个碰撞的概率为 $1 - 2^{-E}$，其中 $E$ 为给定 $f(\pk, \sigma) = y$ 时，分布在 $\sigma$ 上的最小熵在 $f(\pk, \cdot)$ 的值域内的所有 $y$ 上的最小值. 因为 $\op{PSF}$ 具备的是超对数最小熵，所以 $1 - 2^{-E}$ 与 $1$ 之间的差距是可忽略的. 不过，任何一个非零常数最小熵都足以使得这个数字是一个不可忽略的 1 的分数. 

从以上的两个定理可以得到这部分的主要结论：

!!! success "Corollary"
    如果量子可访问伪随机函数是存在的，并且 $\mathcal{F}$ 是一个能够安全抵抗量子敌手的 $\op{PSF}$，那么 $\op{FDH-PSF}$ 签名方案在量子可访问随机 Oracle 模型下是安全的.

### Secure Signatures from Claw-Free Permutations

这部分将会给出如何使用无爪置换构建三个具有无历史规约进而在量子可访问随机 Oracle 模型下是安全的签名方案. 首先是标准的 $\op{FDH}$ 签名方案，使用无爪置换；然后是 *Katz and Wang*[[KW03]](https://dl.acm.org/doi/10.1145/948109.948132) 的签名方案；最后是通过无爪置换诱导得到一个 $\op{PSF}$，最后用于构建 $\op{FDH-PSF}$ 签名方案.

回顾无爪置换的定义，其是一对陷门置换 $(\mathcal{F}_1, \mathcal{F}_2)$，其中 $\mathcal{F}_i = (G_i, f_i, f_i^{-1})$，满足以下性质：

- $G_1 = G_2 = G$

- 对任意公钥 $\pk$，$f_1(\pk, \cdot)$ 和 $f_2(\pk, \cdot)$ 的定义域和值域是相同的

- 只给出公钥 $\pk$，任何 $\op{PPT}$ 敌手能够找出一组 $(x_1, x_2)$ 使得 $f_1(\pk, x_1) = f_2(\pk, x_2)$ 的概率是可忽略的，这样的一个组叫做一个爪

无爪置换实际上是具有随机自规约的陷门置换的推广. **随机自规约（random self-reduction）** 是指一种将问题的最坏情况的实例 $x$ 转化为同一问题的某个随机实例 $y$，使得 $y$ 的解决方法可以帮助解决 $x$ 的方法. [[DR03]](https://eprint.iacr.org/2002/103.pdf) 表明任意带有随机自规约的陷门置换（如 RSA）都可以用于构建一个无爪置换. 目前还没有无爪置换可以抵御量子攻击.

- **无爪置换构建的全域哈希签名（FDH Signatures from Claw-Free Permutations）**：这里的构建只使用了 $\mathcal{F}_1$ 进行实例化，如下：

    - $G$ 是无爪置换的生成算法

    - $S^O(\sk, m) = f_1^{-1}(\sk, O(m))$

    - $V^O(\pk, m, \sigma) = 1$ 当且仅当 $O(m) = f_1(\pk, \sigma)$

    下面给出一个无历史规约. 这一规约的随机 Oracle $O_C(r)$ 会返回一个随机对 $(a, b)$，其中 $a$ 是一个从 $\mathcal{F}_1$ 和 $\mathcal{F}_2$ 的定义域中随机采样得到的，而 $b$ 是从 $\{1, 2, \ldots, p\}$ 中随机采样得到的，其中 $p$ 会在之后选取.

    接下来从 $\mathcal{S}$ 的经典敌手 $A$ 去构建一个 $(\mathcal{F}_1, \mathcal{F}_2)$ 的经典敌手 $B$. $B$ 接受输入 $\pk$ 后，按如下工作：

    - 计算 $\op{START}(\pk) = (\pk, \pk)$，以 $\pk$ 为输入模拟 $A$

    - 当 $A$ 查询 $O(r)$ 时，计算 $\op{RAND}^{O_C}(r, \pk)$，对于每个字符串 $r$，$\op{RAND}$ 按如下工作：计算 $(a, b) \from O_C(r)$，如果 $b = 1$，则返回 $f_2(\pk, a)$，否则返回 $f_1(\pk, a)$

    - 当 $A$ 查询 $S(\sk, m)$ 时，计算 $\op{SIGN}^{O_C}(m, \pk)$. $\op{SIGN}$ 按如下工作：计算 $(a, b) \from O_C(m)$，如果 $b \neq 1$，则返回 $a$，否则失败

    - 当 $A$ 输出 $(m, \sigma)$ 时，计算 $\op{FINISH}^{O_C}(m, \sigma, \pk)$. $\op{FINISH}$ 按如下工作：计算 $(a, b) \from O_C(m)$，输出 $(\sigma, a)$

    此外，$\op{INSTANCE}(\pk) = \pk$，与之前的方案类似，所以 $\op{INSTANCE}$ 和 $\op{START}$ 满足无历史规约的要求.

    !!! note "Theorem"
        上述的规约是无历史的.

        ???+ note "Proof"
            $\op{RAND}^{O_C}(r, \pk)$ 是完全随机且独立分布的，因为 $f_1(\pk, a)$ 和 $f_2(\pk, a)$ 都是随机的（$f_b(\pk, \cdot)$ 是置换而 $a$ 是随机的）. 只要 $O_C(m)$ 计算得到的 $b \neq 1$，$\op{SIGN}^{O_C}(m, \pk)$ 的行为就与 $\op{RAND}^{O_C}(\cdot, \pk)$ 是一致的. 因为如果 $\op{RAND}^{O_C}(m, \pk) = f_1(\pk, \op{SIGN}^{O_C}(m, \pk))$，那么 $V^{\op{RAND}^{O_C}(\cdot, \pk)}(\pk, m, \op{SIGN}^{O_C}(m, \pk))$ 会输出 1. 而因为 $b \neq 1$ 有 $\op{RAND}^{O_C}(m, \pk) = f_1(\pk, a)$，且 $\op{SIGN}^{O_C}(m, \pk) = a$，所以等式成立. 所有签名查询均不失败的概率为 $(1 - 1/p)^{q_{\op{SIGN}}}$，如果选定 $p = q_{\op{SIGN}}$，那么该值为 $e^{-1} - O(1)$，是不可忽略的. 

            假设 $A$ 返回了一个有效的伪造签名 $(m, \sigma)$，这意味着 $A$ 从未查询过对 $m$ 的签名，并且 $f_1(\pk, \sigma) = \op{RAND}^{O_C}(m, \pk)$. 如果 $O_C(m)$ 计算得到的 $b = 1$ 的话，那么就有 $f_1(\pk, \sigma) = \op{RAND}^{O_C}(m, \pk) = f_2(\pk, a)$，这意味着 $(\sigma, a)$ 是一个爪. 因为 $A$ 从未查询过对 $m$ 的签名，所以其不可能区分出 $a$，也就是说，$b = 1$ 使得 $a$ 是 $O(m)$ 在 $f_2$ 下的原像，以及 $b \neq 1$ 使得 $a$ 是 $O(m)$ 在 $f_1$ 下的原像的这两种情况是不可区分的. 而 $b = 1$ 的概率是 $1/p$，所以 $B$ 将一个有效的签名以不可忽略的概率转化为一个爪.

    !!! success "Corollary"
        如果量子可访问伪随机函数是存在的，并且 $(\mathcal{F}_1, \mathcal{F}_2)$ 是一对无爪陷门置换，那么用 $\mathcal{F}_1$ 构建的 $\op{FDH}$ 签名方案可以抵御量子敌手.

    因为在上述规约中模拟运行的 Oracle 是真随机的，也就没有用到之前的引理，所以该约束的紧度与经典情况下的是相同的. 也就是说，如果 $A$ 在进行 $q_{\op{SIGN}}$ 次签名查询时有 $\varepsilon$ 的优势，那么 $B$ 有大约 $\varepsilon/q_{\op{SIGN}}$ 的优势. 

- **Katz-Wang 签名方案（Katz-Wang Signature Scheme）**：其是 $\op{FDH}$ 的一种变体，这一方案容许一个近似经典情况下的非常紧的规约，即如果有敌手的优势为 $\varepsilon$，那么该规约可以以 $\varepsilon/2$ 的优势找到一个爪. 给定一对陷门置换 $(\mathcal{F}_1, \mathcal{F}_2)$，按如下方法构建：

    - $G$ 是 $\mathcal{F}$ 的密钥生成算法

    - $S^O(\sk, m) = f_1^{-1}(\sk, O(b, m))$，其中 $b$ 是一个随机比特

    - $V^O(\pk, m, \sigma) = 1$ 当且仅当 $O(0, m) = f_1(\pk, \sigma)$ 或 $O(1, m) = f_1(\pk, \sigma)$

    进而从 $\mathcal{S}$ 的敌手 $A$ 构建一个 $(\mathcal{F}_1, \mathcal{F}_2)$ 的敌手 $B$. 这一规约的随机 Oracle $O_C(r)$ 会生成一个随机对 $(a, b)$，其中 $a$ 是 $\mathcal{F}_1$ 和 $\mathcal{F}_2$ 定义域中的一个随机元素，而 $b$ 是一个随机比特. $B$ 接受输入 $\pk$ 后，按如下工作：

    - 计算 $\op{START}(\pk) = (\pk, \pk)$，以 $\pk$ 为输入模拟 $A$

    - 当 $A$ 查询 $O(b, r)$ 时，计算 $\op{RAND}^{O_C}(b, r, \pk)$，对于每个字符串 $(b, r)$，$\op{RAND}$ 按如下工作：计算 $(a, b') \from O_C(r)$，如果 $b = b'$，则返回 $f_1(\pk, a)$，否则返回 $f_2(\pk, a)$

    - 当 $A$ 查询 $S(\sk, m)$ 时，计算 $\op{SIGN}^{O_C}(m, \pk)$，$\op{SIGN}$ 按如下工作：计算 $(a, b) \from O_C(m)$，返回 $a$

    - 当 $A$ 输出 $(m, \sigma)$ 时，计算 $\op{FINISH}^{O_C}(m, \sigma, \pk)$，$\op{FINISH}$ 按如下工作：计算 $(a, b) \from O_C(m)$，如果 $a = \sigma$，则中止，否则输出 $(\sigma, a)$

    $\op{INSTANCE}$ 和 $\op{START}$ 不再赘述，其满足无历史规约的要求.

    !!! note "Theorem"
        上述的规约是无历史的.

        ???+ note "Proof"
            $\op{RAND}^{O_C}(b, r, \pk)$ 是完全随机且独立分布的，同之前一致. 观察到 $f_1(\pk, \op{SIGN}^{O_C}(m, \pk)) = f_1(\pk, a) = O(b, m)$，其中 $(a, b) \from O_C(m)$. 所以，签名查询总是会以合法的签名进行回复，并且因为 $b$ 是均匀选选取的，整个签名的分布与正确的签名算法是相同的.

            假设 $A$ 返回了一个有效的伪造签名. 令 $(a, b) \from O_C(m)$，共会有两种情况，分别对应 $\sigma$ 对应的签名使用的是 $b$ 还是 $1 - b$. 第一种情况下，就会有 $f_1(\pk, \sigma) = O(b, m) = f_1(\pk, a)$，也就有 $\sigma = a$，这种情况下会中止. 第二种情况下，就会有 $f_1(\pk, \sigma) = O(1 - b, m) = f_2(\pk, a)$，这种情况下 $(\sigma, a)$ 是一个爪. 而因为敌手从未查询过对 $m$ 的签名，所以其不可能区分出两种情况. 也就是说，失败的概率至多为 $1/2$，所以成功的概率是不可忽略的.

    !!! success "Corollary"
        如果量子可访问伪随机函数是存在的，并且 $(\mathcal{F}_1, \mathcal{F}_2)$ 是一对无爪陷门置换，那么用 $\mathcal{F}_1$ 构建的 Katz-Wang 签名方案可以抵御量子敌手.

- **无爪置换诱导的 $\op{PSF}$ 签名（PSF Signatures from Claw-Free Permutations）**：给定一组无爪置换 $(\mathcal{F}_1, \mathcal{F}_2)$，按如下定义 $\op{PSF}$：

    - $G$ 是置换的生成算法

    - $\op{Sample}(\pk)$ 生成一个随机比特 $b$，以及 $f_b$ 的定义域内的一个随机元素 $x$，返回 $(x, b)$

    - $f(\pk, x, b) = f_b(\pk, x)$，以及 $f^{-1}(\sk, y) = (f_b^{-1}(\sk, y), b)$，其中 $b$ 是随机比特

    如果这一 $\op{PSF}$ 已经有一对碰撞 $((x_1, b_1), (x_2, b_2))$，那么就有

    \[
        f_{b_1}(\pk, x_1) = f(\pk, x_1, b_1) = f(\pk, x_2, b_2) = f_{b_2}(\pk, x_2).
    \]

    如果 $b_ = b_2$，因为 $f_{b_1}$ 是一个置换，所以必然有 $x_1 = x_2$. 但因为这是一对碰撞，必然有 $(x_1, b_1) \neq (x_2, b_2)$，所以 $b_1 \neq b_2$，也就是说，$(x_1, x_2)$ 或 $(x_2, x_1)$ 是一个爪.

    因此，可以用以上 $\op{PSF}$ 实例化一个 $\op{FDH}$ 签名方案.

    - $G$ 是置换的生成算法

    - $S^O(\sk, m) = (f_b^{-1}(\sk, O(m)), b)$，其中 $b$ 是一个随机比特

    - $V^O(\pk, m, (\sigma, b)) = 1$ 当且仅当 $O(m) = f_b(\pk, \sigma)$

    这一方案的安全性来自于 $\op{FDH-PSF}$ 签名方案的安全性. 不过这一 $\op{PSF}$ 的最小熵只有 1，会在约束的紧度上有所损失.

## Encryption Schemes in the Quantum-Accessible Random Oracle Model

这一部分将证明两种加密方案的安全性，第一种是由 Bellare 和 Rogaway 提出的 BR 加密方案，将会证明其为 $\op{CPA}$ 安全的. 第二种是由 BR 加密方案的混合泛化版本，将会证明其为 $\op{CCA}$ 安全的.

理想情况上，也可以像证明签名方案的安全性那样定义一个普遍的规约，然后证明这样的规约表明了量子可访问随机 Oracle 模型下的安全性. 不幸的是，对于加密方案定义无历史规约是比签名方案更加困难的. 因此，接下来会直接在量子可访问随机 Oracle 模型下证明这两种加密方案的安全性.

### CPA Security of BR Encryption

!!! info "Definition"
    **(BR Encryption Scheme)** 设 $\mathcal{F} = (G_0, f, f^{-1})$ 是一个单射陷门函数，$O$ 是一个值域与 $f(\pk, \cdot)$ 相同的哈希函数. 定义如下的加密方案 $\mathcal{E} = (G, E, D)$：

    - $G = G_0$

    - $E^O(\pk, m) = (f(\pk, r), O(r) \oplus m)$，其中 $r$ 是一个随机串

    - $D^O(\sk, c) = c \oplus f^{-1}(\sk, y)$

    其中用到的量子免疫单射陷门函数可以从格中困难问题构建.

!!! note "Theorem"
    如果量子可访问伪随机函数是存在的，并且 $\mathcal{F}$ 是一个量子免疫单射陷门函数，那么 $\mathcal{E}$ 是量子 CPA 安全的.

此处证明省略，因为 BR 加密方案的 $\op{CPA}$ 安全性是混合加密方案的 $\op{CCA}$ 安全性的一个特殊情况.

### CCA Security of Hybrid Encryption

接下来证明下述标准混合加密的 $\op{CCA}$ 安全性，其是 BR 加密方案的一个泛化版本，可以用一个单射陷门函数和对称加密方案构建.

!!! info "Definition"
    **(Hybrid Encryption Scheme)** 设 $\mathcal{F} = (G_0, f, f^{-1})$ 是一个单射陷门函数，$\mathcal{E_S} = (E_S, D_S)$ 是一个 $\op{CCA}$ 安全的对称加密方案，$O$ 是一个哈希函数. 定义如下的混合加密方案 $\mathcal{E} = (G, E, D)$：

    - $G = G_0$

    - $E^O(\pk, m) = (f(\pk, r), E_S(O(r), m))$，其中 $r$ 是一个随机串

    - $D^O(\sk, (y, c)) = D_S(O(r'), c)$，其中 $r' = f^{-1}(\sk, y)$

可以发现 BR 加密方案实际上是 $\mathcal{E_S}$ 为一次一密的混合加密方案，也就是说，$E_S(k, m) = k \oplus m$，$D_S(k, c) = k \oplus c$.

!!! note "Theorem"
    如果量子可访问伪随机函数是存在的，并且 $\mathcal{F}$ 是一个量子免疫单射陷门函数，$\mathcal{E_S}$ 是一个量子 $\op{CCA}$ 安全的对称加密方案，那么 $\mathcal{E}$ 是量子 $\op{CCA}$ 安全的.

    ???+ note "Proof"
        假定存在能够攻破 $\mathcal{E}$ 的敌手 $A_Q$. 首先从标准的 $\op{CCA}$ 安全博弈开始.

        - **Game 0**: 定义 $\op{Game}_0$ 为量子敌手 $A_Q$ 在问题 $\op{Asym-CCA}(\mathcal{E})$ 上的博弈. 

        - **Game 1**: 定义 $\op{Game}_1$ 为如下的博弈：挑战者生成 $(\sk, \pk) \from G(1^n)$，$\mathcal{F}$ 定义域上的一个随机元素 $r$，$\mathcal{E_S}$ 的密钥空间上的一个随机密钥 $k$，并且计算 $y = f(\pk, r)$. 挑战者可以访问一个值域为 $\mathcal{E_S}$ 的密钥空间的量子可访问随机 Oracle $O_q$. 之后挑战者将 $\pk$ 发送给 $A_Q$，并按如下处理 $A_Q$ 的查询：

            - 随机 Oracle 查询以随机 Oracle $O_{\op{quant}}$ 的查询进行回复，其将 $\ket{x, y}$ 映射到 $\ket{x, y \oplus O_q(f(\pk, x))}$

            - 对 $(y', c')$ 的解密查询按如下回复：

                - 如果 $y = y'$，则回复 $D_S(k, c')$

                - 如果 $y \neq y'$，则回复 $D_S(O_q(y'), c')$

            - 对 $(m_0, m_1)$ 的挑战查询则是随机选取 $b$，回复 $(y, E_S(k, m_b))$

            当 $A_Q$ 回复 $b'$ 后，比较 $b$ 和 $b'$，如果相等称 $A_Q$ 胜利.

            因为 $f$ 是一个单射，并且 $O_q$ 是随机的，所以 Oracle $O_{\op{quant}}$ 是一个真正的随机 Oracle，并且值域和 $O_q$ 相同. $A_Q$ 所见的挑战密文 $(y, c)$ 的分布与 $\op{Game}_0$ 中的分布是相同的. 此外，如果 $O_q(y) = k$，那么其是相对于随机 Oracle $O_{\op{quant}}$ 的 $m_b$ 的一个有效加密. 对于 $y \neq y'$ 的情况，解密过程如下：

            \[
                D_S(O_q(y'), c') = D_S(O_{\op{quant}}(f^{-1}(\sk, y')), c') = D^{\op{quant}}(\sk, (y', c'))
            \]

            其是正确的. 同样的，对于 $y = y'$ 的情况，解密依然是正确的. 因此，若 $O_q(y) = k$，那么 $A_Q$ 在 $\op{Game}_1$ 中的视角与 $\op{Game}_0$ 中的视角是相同的. 又有如下观察：

            - 挑战查询和解密查询的回复算法都没有向 $O_q$ 查询过 $y$ 作为输入的结果

            - 每个敌手向 $O_{\op{quant}}$ 的量子随机 Oracle 查询都导致了一个挑战者向 $O_q$ 的量子随机 Oracle 查询. 挑战者向 $O_q$ 查询 $y$ 的振幅与敌手向 $O_{\op{quant}}$ 查询 $r$ 的振幅是相同的.

            设 $\varepsilon$ 所有向 $O_q$ 做出的查询中 $y$ 的平方幅度的总和（即 $y$ 的总查询概率）. 这与所有 $A_Q$ 向 $O_{\op{quant}}$ 做出的查询中 $r$ 的总查询概率是相同的. 

            接下来构建一个使用量子可访问随机 Oracle $O_q$ 的量子算法 $B_{\mathcal{F}}^{O_q}$，并且将以 $\varepsilon / q$ 的概率反转 $f$，其中 $q$ 是 $A_Q$ 做出的随机 Oracle 查询次数. $B_{\mathcal{F}}^{O_q}$ 以 $(\pk, y)$ 为输入，目标是输出 $r = f^{-1}(\sk, y)$，按如下方法工作：

            - 在 $\mathcal{E_S}$ 的密钥空间上随机生成一个密钥 $k$，在 $\{1, \ldots, q\}$ 上随机生成一个数 $i$. 而后将 $\pk$ 发送给 $A_Q$ 兵扮演挑战者的角色

            - 以随机 Oracle $O_{\op{quant}}$ 回复随机 Oracle 查询，其中 $O_{\op{quant}}$ 将 $\ket{x, y}$ 映射到 $\ket{x, y \oplus O_q(f(\pk, x))}$

            - 对 $(y', c')$ 的解密查询按如下回复：

                - 如果 $y = y'$，则回复 $D_S(k, c')$

                - 如果 $y \neq y'$，则回复 $D_S(O_q(y'), c')$

            - 对 $(m_0, m_1)$ 的挑战查询则是随机选取 $b$，回复 $(y, E_S(k, m_b))$

            - 在第 $i$ 次随机 Oracle 查询时，采样查询得到 $r'$，输出 $r'$ 并终止

            比较 $B_{\mathcal{F}}^{O_q}$ 和 $\op{Game}_1$ 的定义，可以发现 $A_Q$ 在两种情况下的视角都是一样的，所以 $A_Q$ 向 $O_{\op{quant}}$ 查询 $r$ 的总查询概率为 $\varepsilon$. 因此，$B_{\mathcal{F}}^{O_q}$ 最终输出 $r$ 的概率为 $\varepsilon / q$. 如果假定 $\mathcal{F}$ 对使用量子可访问随机 Oracle 的量子敌手是安全的，那么 $\varepsilon$ 必然是可忽略的. 对于签名的情况，这一假设可以用 $\mathcal{F}$ 对不可使用量子可访问随机 Oracle 的量子敌手是安全的以及伪随机函数存在来替换，并且得到的结论是相同的.

            因为 $\varepsilon$ 是可忽略的，所以 $\op{Game}_1$ 中的 $O_q(y) = k$ 是可以被改变的，进而得到一个敌手视角中与 $\op{Game}_0$ 相同的博弈. 而在 $\op{Game}_0$ 和 $\op{Game}_1$ 中，因为只进行了酉变换，测量操作以及经典通信操作，所以 $A_Q$ 始终处于纯态. 因为只以可忽略的总查询概率改变了 Oracle 在一点的值，所以依据引理，这只会以可忽略的概率影响 $\op{Game}_1$ 的输出的分布. 因此，$A_Q$ 在 $\op{Game}_1$ 中的成功概率与 $\op{Game}_0$ 中的成功概率之间的差距是可忽略的.

            现在假定 $A_Q$ 在 $\op{Game}_1$ 中成功的概率是不可忽略的. 接下来定义一个使用量子可访问随机 Oracle  $O_q$ 的量子算法 $B_{\mathcal{E_S}}^{O_q}$ 来攻破 $\mathcal{E_S}$ 的 $\op{CCA}$ 安全性. $B_{\mathcal{E_S}}^{O_q} 按如下工作：

            - 输入 $1^n$ 时，生成 $(\pk, \sk) \from G(1^n)$，并且生成随机串 $r$，计算 $y = f(\pk, r)$. 将 $\pk$ 发送给 $A_Q$ 并且充当挑战者的角色

            - 以随机 Oracle $O_{\op{quant}}$ 回复随机 Oracle 查询，其中 $O_{\op{quant}}$ 将 $\ket{x, y}$ 映射到 $\ket{x, y \oplus O_q(f(\pk, x))}$

            - 对 $(y', c')$ 的解密查询按如下回复：

                - 如果 $y = y'$，则向 $\mathcal{E_S}$ 挑战者查询解密 $D_S(k, c')$ 以得到 $m'$，并回复 $m'$

                - 如果 $y \neq y'$，则回复 $D_S(O_q(y'), c')$

            - 对 $(m_0, m_1)$ 的挑战查询则是通过转发 $\mathcal{E_S}$ 的信息对. 当挑战者回复 $c$（存在 $b$ 使其与 $E_S(k, m_b)$ 相等）时，返回 $(y, c)$

            - 当 $A_Q$ 回复 $b'$ 后，输出 $b'$ 并停机

            比较 $B_{\mathcal{E_S}}^{O_q}$ 和 $\op{Game}_1$ 的定义，可以发现 $A_Q$ 在两种情况下的视角是一样的，所以 $A_Q$ 的成功概率时不可忽略的. 如果 $A_Q$ 成功，也就是说其输出了 $b$，那么 $B_{\mathcal{E_S}}^{O_q}$ 也成功了，这一使用了量子可访问随机 Oracle 的算法攻破了 $\mathcal{E_S}$，与 $\mathcal{E_S}$ 对使用量子可访问随机 Oracle 的量子敌手的 $\op{CCA}$ 安全性相矛盾. 

            因此，$A_Q$ 在 $\op{Game}_1$ 中的成功概率是可忽略的，进而 $\op{Game}_0$ 中的成功概率也是可忽略的. 也就证明了所有的多项式时间量子算法在攻破 $\mathcal{E}$ 的 $\op{CCA}$ 安全性上的优势是可忽略的，所以 $\mathcal{E}$ 是 $\op{CCA}$ 安全的. 

简要解释一下为什么 BR 加密的 $\op{CPA}$ 安全性是混合加密方案的 $\op{CCA}$ 安全性的一个特殊情况. 在上述证明中 $B_{\mathcal{E_S}}$ 只在回复 $A_Q$ 的解密查询时才会查询其解密 Oracle，并且从未进行过加密查询. 因此，只要 $A_Q$ 不进行解密查询，那么 $B_{\mathcal{E_S}}$ 就只会进行挑战查询. 如果只关心 $\mathcal{E}$ 的 $\op{CPA}$ 安全性，那么就只需要 $E_S$ 对只能进行挑战查询的敌手是安全的. 更进一步，如果只允许 $A_Q$ 进行挑战查询。并且限制消息长度为 $n$，那么 $E_S$ 只需要对只能以特定长度的消息进行挑战查询的敌手是安全的即可. 而这恰恰就是一次一密无条件安全的情况，所以 BR 加密的 $\op{CPA}$ 安全性是混合加密方案的 $\op{CCA}$ 安全性的一个特殊情况.

## Appendix

### Definition

!!! info "Definition"
    **(Trapdoor Permutation)** 陷门置换是一个函数三元组 $\mathcal{F} = (G, f, f^{-1})$，其中：

    - $G(1^n)$ 生成密钥对 $(\sk, \pk)$

    - $f(\pk, \cdot)$ 是一个对所有 $\pk$ 的置换

    - 对于所有由 $G$ 生成的 $(\sk, \pk)$，$f^{-1}(\sk, \cdot)$ 是 $f(\pk, \cdot)$ 的逆，也就有 $f^{-1}(\sk, f(\pk, x)) = x$ 以及 $f(\pk, f^{-1}(\sk, y)) = y$

对陷门置换 $\mathcal{F}$，定义问题 $\op{Inv}(\mathcal{F}) = (\op{Game}(\mathcal{F}), 0)$，其中 $\op{Game}(\mathcal{F})$ 是量子敌手 $A$ 和挑战者 $\op{Ch}$ 之间的如下的博弈：

- $\op{Ch}$ 以 $n$ 为输入，运行 $G(1^n)$ 生成密钥对 $(\sk, \pk)$，并在 $f(\pk, \cdot)$ 的值域上生成一个随机元素 $y$，将 $(\pk, y)$ 发送给 $A$

- $A$ 被允许进行量子随机 Oracle 查询 $O(\cdot)$

- 当 $A$ 输出 $x$ 时，当且仅当 $f(\pk, x) = y$ 时，$\op{Ch}$ 输出 1

!!! info "Definition"
    如果 $\op{Inv}(\mathcal{F})$ 对量子计算机是困难的，那么 $\mathcal{F}$ 对量子敌手具有安全性.

!!! info "Definition"
    **(Preimage Sampleable Trapdoor Function)** 具有预像可采样性质的陷门碰撞抗性哈希函数是具有如下性质的函数四元组 $\mathcal{F} = (G, \op{Sample}, f, f^{-1})$：

    - $G(1^n)$ 生成密钥对 $(\sk, \pk)$

    - $f(\pk, \cdot)$ 的定义域为 $D$，值域为 $R$

    - $\op{Sample}(1^n)$ 从 $D$ 上的某一分布进行采样，使得对于任意的 $\pk$，$f(\pk, \op{Sample}(1^n))$ 与均匀分布的变差距离不超过 $\varepsilon_{\op{Sample}}$

    - $f^{-1}(\sk, y)$ 生成满足 $f(\pk, x) = y$ 的 $x$，且分布与给定 $f(\pk, x) = y$ 的 $\op{Sample}()$ 的条件分布之间的距离不超过 $\varepsilon_{\op{pre}}$，其中 $\varepsilon_{\op{pre}}$ 是可忽略的

    - 原像最小熵：对所有 $y \in R$，给定 $f(\pk, x) = y$ 的 $\op{Sample}(1^n)$ 的条件分布中的任何元素的概率都小于 $\varepsilon_{\op{prob}}$，其中 $\varepsilon_{\op{prob}}$ 是可忽略的

对于 $\op{PSF}$，除了定义问题 $\op{Inv}$ 之外，还会定义问题 $\op{Col} = (\op{Game}(\mathcal{F}), 0)$，其中 $\op{Game}(\mathcal{F})$ 是量子敌手 $A$ 和挑战者 $\op{Ch}$ 之间的如下的博弈：

- 挑战者 $\op{Ch}$ 以 $n$ 为输入，运行 $G(1^n)$ 生成密钥对 $(\sk, \pk)$，将 $\pk$ 发送给 $A$

- $A$ 被允许进行量子随机 Oracle 查询 $O(\cdot)$

- 当 $A$ 输出 $(x_1, x_2)$ 时，当且仅当 $x_1 \neq x_2$ 且 $f(\pk, x_1) = f(\pk, x_2)$ 时，$\op{Ch}$ 输出 1

!!! info "Definition"
    如果 $\op{Inv}(\mathcal{F})$ 和 $\op{Col}(\mathcal{F})$ 对量子计算机均是困难的，那么 $\mathcal{F}$ 对量子敌手具有安全性.

!!! info "Definition"
    **(Signature Scheme)** 随机 Oracle 签名方案是一个函数三元组 $\mathcal{S} = (G, S^O, V^O)$，其中：

    - $O$ 是一个随机 Oracle

    - $G(1^n)$ 生成密钥对 $(\sk, \pk)$，$\sk$ 是签名者的私钥，$\pk$ 是一个公钥

    - $S^O(\sk, m)$ 是签名算法，其输出一个签名 $\sigma$

    - $V^O(\pk, m, \sigma)$ 是验证算法，其输出 1 当且仅当 $\sigma$ 是 $m$ 的合法签名，要求对所有 $m$ 和 $G$ 生成的 $(\sk, \pk)$，$V^O(\pk, m, S^O(\sk, m)) = 1$

对签名算法 $\mathcal{S}$，定义问题 $\op{Sig-Forge}(\mathcal{S}) = (\op{Game}(\mathcal{S}), 0)$，其中 $\op{Game}(\mathcal{S})$ 是量子敌手 $A$ 和挑战者 $\op{Ch}^O$ 之间的如下的博弈：

- $\op{Ch}^O$ 以 $n$ 为输入，运行 $G(1^n)$ 生成密钥对 $(\sk, \pk)$，并将 $\pk$ 发送给 $A$

- $A$ 被允许进行量子随机 Oracle 查询 $O(\cdot)$ 和向 $\op{Ch}^O$ 进行经典签名查询 $S^O(\sk, \cdot)$

- 当 $A$ 输出一个可能的伪造签名 $(m, \sigma)$ 时，当且仅当 $A$ 从未查询过 $m$ 的签名且 $V^O(\pk, m, \sigma) = 1$ 时，$\op{Ch}^O$ 输出 1

!!! info "Definition"
    如果 $\op{Sig-Forge}(\mathcal{S})$ 对量子计算机是困难的，那么 $\mathcal{S}$ 对量子敌手具有安全性.

!!! info "Definition"
    **(Symmetric Key Encryption Scheme)** 对称密钥随机 Oracle 加密方案是一个函数二元组 $\mathcal{E} = (E^O, D^O)$，其中：

    - $E^O(k, m)$ 生成密文 $c$

    - $D^O(k, c)$ 计算出对应的明文 $m$，要求 $D^O(k, E^O(k, m)) = m$

对 $\mathcal{E}$，定义问题 $\op{Sym-CCA}(\mathcal{E}) = (\op{Game}(\mathcal{E}), \frac{1}{2})$，其中 $\op{Game}(\mathcal{E})$ 是量子敌手 $A$ 和挑战者 $\op{Ch}^O$ 之间的如下的博弈：

- $\op{Ch}^O$ 以 $n$ 为输入，随机生成长度为 $n$ 的密钥 $k$，并将 $k$ 发送给 $A$

- $A$ 被允许进行量子随机 Oracle 查询 $O(\cdot)$，经典加密查询 $E^O(k, \cdot)$ 和经典解密查询 $D^O(k, \cdot)$. 

- 此外 $A$ 被允许进行一次经典挑战查询，其向 $\op{Ch}^O$ 发送一对消息 $(m_0, m_1)$，$\op{Ch}^O$ 随机选取 $b$，计算 $c = E^O(k, m_b)$ 并将 $c$ 发送给 $A$

- 当 $A$ 输出一个比特 $b'$ 时，当且仅当 $b = b'$ 并且在挑战查询后 $A$ 从未查询过 $c$ 的解密 $D^O(k, c)$ 时，$\op{Ch}^O$ 输出 1

!!! info "Definition"
    如果 $\op{Sym-CCA}(\mathcal{E})$ 对量子计算机是困难的，那么 $\mathcal{E}$ 对量子敌手具有 $\op{CCA}$ 安全性.

!!! info "Definition"
    **(Asymmetric Key Encryption Scheme)** 非对称密钥加密方案是一个函数三元组 $\mathcal{E} = (G, E^O, D^O)$，其中：

    - $G(1^n)$ 生成密钥对 $(\sk, \pk)$

    - $E^O(\pk, m)$ 生成密文 $c$

    - $D^O(\sk, c)$ 计算出对应的明文 $m$，要求 $D^O(\sk, E^O(\pk, m)) = m$

对 $\mathcal{E}$，定义问题 $\op{Asym-CCA}(\mathcal{E}) = (\op{Game}(\mathcal{E}), \frac{1}{2})$，其中 $\op{Game}(\mathcal{E})$ 是量子敌手 $A$ 和挑战者 $\op{Ch}^O$ 之间的如下的博弈：

- $\op{Ch}^O$ 以 $n$ 为输入，运行 $G(1^n)$ 生成密钥对 $(\sk, \pk)$，并将 $\pk$ 发送给 $A$

- $A$ 被允许进行量子随机 Oracle 查询 $O(\cdot)$，经典加密查询 $E^O(\pk, \cdot)$ 和经典解密查询 $D^O(\sk, \cdot)$.

- 此外 $A$ 被允许进行一次经典挑战查询，其向 $\op{Ch}^O$ 发送一对消息 $(m_0, m_1)$，$\op{Ch}^O$ 随机选取 $b$，计算 $c = E^O(\pk, m_b)$ 并将 $c$ 发送给 $A$

- 当 $A$ 输出一个比特 $b'$ 时，当且仅当 $b = b'$ 并且在挑战查询后 $A$ 从未查询过 $c$ 的解密 $D^O(\sk, c)$ 时，$\op{Ch}^O$ 输出 1

!!! info "Definition"
    如果 $\op{Asym-CCA}(\mathcal{E})$ 对量子计算机是困难的，那么 $\mathcal{E}$ 对量子敌手具有 $\op{CCA}$ 安全性.

### Security of the $\op{IS}^*$ Protocol

### Proof of Lemma 3

证明之前先给出两条技术性引理：

!!! success "Lemma"
    设 $\ket{\phi}$ 和 $\ket{\phi'}$ 是两个叠加态，并且 $\abs{\phi - \phi'} \leq \gamma$. 设 $P$ 是字符串上的某种性质. 假定测量叠加态 $\ket{psi}$ 得到一个符合性质 $P$ 的字符串的概率为 $\varepsilon$，那么测量叠加态 $\ket{\phi'}$ 得到一个符合性质 $P$ 的字符串的概率 $\varepsilon'$ 满足
    
    \[
        \sqrt{\varepsilon} - \gamma \leq \sqrt{\varepsilon'} \leq \sqrt{\varepsilon} + \gamma
    \]

    ???+ success "Proof"
        可以从几何意义上去证明这一引理. 认为 $\ket{\phi}$ 为 $\mathbb{C}^n$ 中的一个向量 $\mathbf{\phi}$. 那么基础元素 $\ket{x}$ 就可以被认为是 $\mathbb{C}^n$ 的标准基中的元素. 给定了 $\abs{\phi - \phi'} \leq \gamma$，那么 $\mathbf{\phi}$ 和 $\mathbf{\phi'}$ 的欧式距离至多为 $\gamma$.

        对一个二进制串 $x$，测量 $\ket{\phi}$ 得到 $x$ 的概率为 $\abs{\innerproduct{x}{\phi}}^2$. 设 $S_P$ 是满足性质 $P$ 的 $x$ 的基础元素 $\mathbf{x}$ 的集合. 