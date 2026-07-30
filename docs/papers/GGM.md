# Attention is still what you need: Another Round of Exploring Shoup's GGM

## Introduction

自 Diffie-Hellman 以来，基于群的密码体制已成为现代密码学的基石（如密钥交换、公钥加密、数字签名等）. 主要发展的密码学群类型包括：

- **乘法群** (Multiplicative groups)
- **EC 群** (Elliptic Curve groups, EC)
- **配对友好群** (Pairing-friendly groups)

而在实际部署中，**编码长度**直接影响通信复杂度和效率. EC 群具有诸多优势，如**紧凑编码**（Compact encoding）和**受控编码**（admissible encoding）. 紧凑编码指 EC 群在同等安全水平下，所需的编码长度更短；受控编码则指 EC 群支持 $\mathbb{Z}_p$ 到群元素的高效映射，该映射支持**正则性**（原像长度恒定）和**原像可计算性**. 在受控编码的基础上就可以支持**不经意采样**（Oblivious Sampling）.

但因为无法证明特定群的无条件困难性，所以使用了**通用群模型**（Generic Group Model, GGM）来分析基于群的密码体制的计算困难性下界. 主要运用的两个版本为：

- Maurer's GGM: 基于状态系统，通过引用句柄进行查询；但限制性过强，无法实现数字签名和基础的伪随机构造.
- Shoup's GGM: 基于 $\mathbb{Z}_N$ 到足够长字符串的随机单射，通过提供字符串进行查询.

Shoup's GGM 中，群编码的长度也起着重要作用. 该模型的诸多应用都依赖于这样的一个要求：算法在不查询谕示机的情况下无法生成有效的群元素. 这就要求 GGM 是**稀疏编码**（Sparse encoding），所以稀疏 GGM 是 Shoup 框架的重要组成部分. 

但稀疏 GGM 不支持不经意采样，所以也就没有受控编码. 这便引出了一个重要问题：**稀疏 GGM 能否有效准确地对 EC 群或其他的稠密密码学群进行建模？** 

### Our results

答案是否定的. 具体来说，设 $G$ 是满足如下条件的密码学群：

- 计算性 Diffie-Hellman 假设（CDH）在 $G$ 上成立；
- 群编码是稠密的，或是关联了*良好*受控编码.

那么 $G$ 在稀疏 GGM 中无条件不存在.

首先解释稀疏通用群模型（GGMs），稠密群，以及具有良好受控编码的群这几个概念. 设 $\lambda$ 是安全参数：

- **稀疏与稠密 GGMs**: 对于 GGM $\mathcal{G}$，若其随机单射从 $\mathbb{Z}_N$ 出发，到达 $S$，其中 $N$ 为 $\lambda$ 位素数，$S = \{0, 1\}^m$，且差值 $m - \lambda \geq \omega (\log \lambda)$，则称 $\mathcal{G}$ 为**稀疏 GGM**；否则当差值满足 $m - \lambda \leq \Theta(\log \lambda)$ 时，称为**稠密 GGM**.

- **稀疏与稠密群编码**：类似地，对于阶为 $N$ 的密码学群 $G$，如果其群编码长度 $m$ 满足 $m - \lambda \geq \omega (\log \lambda)$，则称 $G$ 为稀疏的；否则当差值满足 $m - \lambda \leq \Theta(\log \lambda)$ 时，称为稠密的.

- **良好受控编码**：设群 $G$ 的阶为 $N$，对于常数 $\varrho$ 以及多项式 $\op{poly}_{\mathrm{AE}}$，若存在高效可计算函数 $\op{AE}: \mathbb{Z}_p \to G$，满足以下条件：

    1. 任意群元素在 $\op{AE}$ 下的原像是高效可计算的；
    2. 该编码是 $\varrho$-正则的，即任意群元素的原像长度为 $\varrho$；
    3. 定义域大小足够大，即 $p / N \geq \op{poly}_{\mathrm{AE}}$.

    那么称 $G$ 具有关于 $\varrho$ 和 $\op{poly}_{\mathrm{AE}}$ 的**良好受控编码**. 所有 EC 群在 $\varrho = 4$ 时均满足以上条件.

#### Impossibility results in sparse GGM/GBM

稀疏 GGM 存在不支持受控编码的固有缺陷，在此基础上建立了具有受控编码的 CDH 安全群和稀疏 GGM 的**黑盒分离**（Black-box separation）结果：

!!! note "Theorem 1.1 (Informal)"
    对任意常数 $\varrho$，具有关于 $\varrho$ 的受控编码的 CDH 安全群 $G$ 在稀疏 GGM 中不存在.

稀疏 GGM 的缺陷还体现在其编码无法以通用方法进行压缩，在此基础上建立了 CDH 安全稠密群和稀疏 GGM 的黑盒分离结果：

!!! note "Theorem 1.2 (Informal)"
    CDH 安全的稠密群 $G$ 在稀疏 GGM 中不存在.

而只要理想化模型继续保持稀疏性，那么构建具有受控编码的群或稠密群的困难便会持续存在，即使该模型扩展为了通用双线性群模型（Generic Bilinear Group Model, GBM）. GBM $\mathcal{B}$ 对源通用群和目标通用群进行建模，如果源通用群和目标通用群均为稀疏的，那么称 $\mathcal{B}$ 为稀疏 GBM. 在此基础上建立了以下黑盒分离结果：

!!! note "Theorem 1.3 (Informal)"
    对任意常数 $\varrho$，具有关于 $\varrho$ 的受控编码的 CDH 安全群 $G$ 在稀疏 GBM 中不存在.

!!! note "Theorem 1.4 (Informal)"
    CDH 安全的稠密群 $G$ 在稀疏 GBM 中不存在.

#### Exploring the relationship between EC-GGM and sparse GGM

Groth 和 Shoup 引入了 GGM 的一个变体，称为**椭圆曲线通用群模型**（EC-GGM）. 设 $E$ 为阶为 $N$ 的 EC 群上所有点的集合，EC-GGM 对 $\mathbb{Z}_N$ 到 $E$ 的随机单射进行建模，同时保留了 EC 群的某些固有属性. 所以具有良好受控编码的 CDH 安全群在 EC-GGM 中存在. 

!!! note "Theorem 1.5 (Informal)"
    具有良好受控编码的 CDH 安全群在 EC-GGM 中存在.

接下来在不可区分性的框架下研究 EC-GGM 和稀疏 GGM 之间的关系，在计算受限敌手的前提下，证明了如下结果：

!!! note "Theorem 1.6 (Informal)"
    在不可区分性的框架下，EC-GGM 严格强于稀疏 GGM.

在此基础上，重新审视稠密 GGM 和稀疏 GGM 之间的关系，得到：

!!! note "Theorem 1.7 (Informal)"
    在不可区分性的框架下，稠密 GGM 严格强于稀疏 GGM.

!!! note "Theorem 1.8 (Informal)"
    CDH 安全的稠密群在稠密 GGM 中存在.

### Interpretation

Shoup's GGM 中证明安全性或建立黑盒分离结果时必须极度谨慎，从以下两个角度进行阐释：

- **用 EC 群实例化 GGM**: GGM 中的算法被要求是通用的，但并非所有针对基于群的假设（如离散对数问题）的算法都满足这一要求，例如针对 $\mathbb{Z}_N^*$ 的指数计算攻击（index calculus attack）. 幸运的是，在 EC 群的情况下，目前已知的攻击在本质上是通用的. 因此，GGM 常常使用 EC 群进行实例化. 但在许多实际的密码学构造中，GGM 通常被视作稀疏 GGM，即限制敌手在没有进行显式查询的情况下无法生成有效的群元素. 而所有 EC 群都属于拥有良好受控编码的群的范畴，并且我们的结果建立了具有受控编码的 CDH 安全群与稀疏 GGM 之间的黑盒分离结果，凸显了在用 EC 群实例化 GGM 时存在的一个潜在的、且此前被忽视的鸿沟.

- **GGM 中的黑盒分离**: GGM 常用于展示某些基于群的密码体制的局限性，而大多数的已知结果都是在稀疏 GGM 中建立的，这些结果存在重要的局限性，因为其排除了具有良好受控编码的 CDH 安全群以及 CDH 安全的稠密群. 因此，这些群和**基于身份加密**（Identity-based encryption, IBE）之间的**相对化分离**（relativized separation）问题实际上并未得到解决. 

    鉴于许多实际使用的群都属于具有良好受控编码的群这一范畴，我们的结果激励了对这类群的复杂性进行进一步研究. 当以细粒度（fine-grained）的方法进行审视时，GGM 和 GBM 之间的关系需要被重新解释. 具体而言，Zhang 和 Zhandry 曾证明 GBM 严格强于 GGM，但实际上 EC-GGM（或稠密 GGM）与稀疏 GBM 是不可比较的. 

### Technical overview

#### Impossibility of groups with AE in sparse GGM

为了证明某种密码学原语 $\mathcal{P}$ 在理想化模型 $\mathcal{O}$ 是不可能的，通常采用**黑盒分离**（Black-box separation）的方式. 具体来说，对于 $\mathcal{P}$ 的任意实例化 $\Pi^\mathcal{O}$，构造一个计算能力无限的敌手 $\mathcal{A}$，使得

1. $\mathcal{A}$ 破坏了 $\Pi^\mathcal{O}$ 的安全性；
2. $\mathcal{A}$ 是查询高效的（query-efficient）.

Impagliazzo 和 Rudich 的开创性结果表明，密钥协商原语不能存在于随机谕示机模型（Random Oracle Model, ROM）中. 具体来说，对于该模型中的任何协议，都存在一个能够在**密钥恢复攻击**（key-recovery attack, KRA）中获胜的敌手. 而回到我们的语境，值得注意的是，具有受控编码的 CDH 安全群本质上蕴含了 KRA 安全的密钥协商（如 Diffie-Hellman 协议）. 因此，如果能确定 KRA 安全的密钥协商在稀疏 GGM 中是不可实现的，那么就完成了分析.

为了阐述清晰，我们将分析集中在密钥协商原语的一个特例上，即**非交互式密钥交换**（Non-interactive key exchange, NIKE）. 首先简要回顾随机谕示机模型中 KRA 安全的 NIKE 的不可能性证明. 

- **KRA 安全的 NIKE vs. ROM**: 设 $\Pi^\mathcal{H} := (\mathsf{KGen}^\mathcal{H}, \mathsf{SHK}^\mathcal{H})$ 为随机谕示机模型 $\mathcal{H}$ 的一个 NIKE 方案，其中

    1. $\Pi^\mathcal{H}$ 实现了完美正确性（perfect correctness）；
    2. $\mathsf{KGen}$（密钥生成）和 $\mathsf{SHK}$（共享密钥计算）最多进行 $q$ 次查询.

    考虑 Alice 和 Bob 为两个诚实方，分别关联公钥 $\mathsf{pk}_1$ 和 $\mathsf{pk}_2$. 构造敌手 $\mathcal{A}$，给定 $\mathsf{pk}_1$ 和 $\mathsf{pk}_2$，$\mathcal{A}$ 能以良好的概率输出有效的共享密钥. 

    具体来说，敌手 $\mathcal{A}$ 初始化两个空集合 $S_\mathsf{que-res}$（查询-响应集） 和 $S_\mathsf{key}$（候选密钥集），然后通过 $4q + 1$ 次迭代执行以下步骤：

    - 模拟：为 Alice 模拟一个适当的视图（view）. 具体来说，该视图包含一组查询-响应对 $\tilde{S}_A$ 以及一个私钥 $\tilde{\mathsf{sk}}_1$，满足：

        1. $\tilde{S}_A$ 与 $S_\mathsf{que-res}$ 是一致的；
        2. 该视图能诱导出正确的 Alice 的公钥：$\mathsf{KGen}^{\tilde{S}_A \cup S_\mathsf{que-res}}(\tilde{\mathsf{sk}}_1) = \mathsf{pk}_1$.

        接下来便基于模拟的视图计算共享密钥：$\mathsf{shk} = \mathsf{SHK}^{\tilde{S}_A \cup S_\mathsf{que-res}}(\tilde{\mathsf{sk}}_1, \mathsf{pk}_2)$，并将 $\mathsf{shk}$ 添加到 $S_\mathsf{key}$ 中.

    - 更新：通过访问随机谕示机 $\mathcal{H}$ 来更新 $\tilde{S}_A \setminus S_\mathsf{que-res}$ 中的所有查询，并将这些查询-响应对添加到 $S_\mathsf{que-res}$ 中.

    最后 $\mathcal{A}$ 输出集合 $S_\mathsf{key}$ 中出现次数最多的共享密钥 $\mathsf{shk}^*$.

    接下来概述 $\mathcal{A}$ 极有可能在 KRA 安全博弈中获胜的原因. 令 $S_\mathsf{Bob}$ 为 Bob 在密钥交换协议的真实执行过程中所做的查询-响应对的集合. 对于任何迭代，存在两种情况：

    - Case 1(Bad): $\exists (\blue{\mathsf{que}_A}, \red{\mathsf{res}_A}) \in \tilde{S}_A, (\blue{\mathsf{que}_B}, \red{\mathsf{res}_B}) \in S_\mathsf{Bob}$，使得 $\blue{\mathsf{que}_A} = \blue{\mathsf{que}_B}$ 但 $\red{\mathsf{res}_A} \neq \red{\mathsf{res}_B}$.

    - Case 2(Good): $\forall (\blue{\mathsf{que}_A}, \red{\mathsf{res}_A}) \in \tilde{S}_A, (\blue{\mathsf{que}_B}, \red{\mathsf{res}_B}) \in S_\mathsf{Bob}$，若 $\blue{\mathsf{que}_A} = \blue{\mathsf{que}_B}$ 则 $\red{\mathsf{res}_A} = \red{\mathsf{res}_B}$.

    因为 $\abs{S_\mathsf{Bob}} \leq 2q$，所以 Case 1 至多发生 $2q$ 次. 而在这种情况下，更新阶段会把至少一对 $(\blue{\mathsf{que}_B}, \red{\mathsf{res}_B}) \in S_\mathsf{Bob}$ 吸收进 $S_\mathsf{que-res}$ 中. 而当 Case 2 发生时，存在一个替代谕示机 $\tilde{\mathcal{H}}$ 与 $\tilde{S}_A$ 和 $S_\mathsf{Bob}$ 都是一致的. 而由于完美正确性，此次迭代中计算出的共享密钥保证是有效的. 并且，Case 2 至少发生 $2q + 1$ 次，这确保了 $S_\mathsf{key}$ 中的大多数共享密钥都是有效的. 

- **为什么该攻击在 GGM 中失效？**: 与 ROM 不同，GGM 包含两种类型的查询：标记查询（labeling queries），如 $(\blue{x}, \red{\mathcal{G}(x)})$；以及加法查询（addition queries），如 $(\blue{\mathcal{G}(x)}, \blue{\mathcal{G}(y)}, \red{\mathcal{G}(x+y)})$. 所以为了保证共享密钥的有效性，$S_\mathsf{Bob}$ 中应该包含查询中出现的所有群编码（包括标记查询和加法查询），以及它们对应的离散对数. 

    对于任意一次迭代，有三种情况：

    - Case 1(Bad): $\exists (\blue{\mathsf{que}_A}, \red{\mathsf{res}_A}) \in \tilde{S}_A, (\blue{\mathsf{que}_B}, \red{\mathsf{res}_B}) \in S_\mathsf{Bob}$，使得 $\blue{\mathsf{que}_A} = \blue{\mathsf{que}_B}$ 但 $\red{\mathsf{res}_A} \neq \red{\mathsf{res}_B}$.

    - Case 2(Bad): $\exists (\blue{\mathsf{que}_A}, \red{\mathsf{res}_A}) \in \tilde{S}_A, (\blue{\mathsf{que}_B}, \red{\mathsf{res}_B}) \in S_\mathsf{Bob}$，使得 $\blue{\mathsf{que}_A} \neq \blue{\mathsf{que}_B}$ 但 $\red{\mathsf{res}_A} = \red{\mathsf{res}_B}$.

    - Case 3(Good): $\forall (\blue{\mathsf{que}_A}, \red{\mathsf{res}_A}) \in \tilde{S}_A, (\blue{\mathsf{que}_B}, \red{\mathsf{res}_B}) \in S_\mathsf{Bob}$，若 $\blue{\mathsf{que}_A} = \blue{\mathsf{que}_B}$ 则 $\red{\mathsf{res}_A} = \red{\mathsf{res}_B}$.

    Case 1 和 Case 3 可以用类似于 ROM 中的分析方法进行处理，但 Case 2 可能会一直发生，这意味着不能找到一个同时与 $\tilde{S}_A$ 和 $S_\mathsf{Bob}$ 都一致的 GGM 实例，这暗示了上述攻击的失效. 并且，进一步探索表明 Case 2 的发生意味着敌手可以在不知道离散对数的情况下生成有效的群元素，即无需进行标记查询.

    因此，为了推进分析，必须以更细粒度的方法来处理 NIKE 和 GGM，确保没有查询高效的敌手能够在不知道离散对数的情况下生成有效的群元素. 具体而言，该分析旨在识别一个细粒度 NIKE 和 GGM 相关的困难问题，并证明如果一个敌手在给定公钥 $\mathsf{pk}_1$ 和 $\mathsf{pk}_2$ 的情况下，成功输出一个有效的群元素而无需进行查询，那么该困难问题就不再成立.

- **JZW+24 的解决方法与局限性**：JZW+24 证明了具有较短群描述的 CDH 安全群，不能存在于具有较长编码的 GGM 中. 具体而言，他们在关联较短公钥的 KRA 安全 NIKE 方案与具有较长群编码的 GGM 之间，建立了一种某种程度上的黑盒分离. 他们工作中的核心思想是：给定公钥 $\mathsf{pk}_1$ 和 $\mathsf{pk}_2$，提取出的群元素 $\mathsf{str}$ 可能是以下两种情况之一：

    1. $\mathsf{str}$ 与 $\mathsf{pk}_1$ 和 $\mathsf{pk}_2$ 都有关；
    2. $\mathsf{str}$ 仅与 $\mathsf{pk}_1$ 或 $\mathsf{pk}_2$ 中的一个有关，而与另一个无关，不妨设为 $\mathsf{pk}_1$.

    在前一种情况下，$\mathsf{str}$ 通常是一个频繁查询（Frequent Query），这可以通过在足够多的随机输入上重复运行密钥生成算法来轻松处理；在后一种情况下，他们观察到 $\mathsf{pk}_1$ 是关于 $\mathsf{str}$ 信息的唯一载体，然而，由于 $\mathsf{pk}_1$ 的长度显著短于 $\mathsf{str}$，其缺乏必要的容量来恢复 $\mathsf{str}$ 所需的所有信息. 因此，没有任何查询高效的算法能够以不可忽略的概率成功提取 $\mathsf{str}$. JZW+24 中识别出的困难问题可以解释为：给定任意相对较短的公钥，除可忽略概率外，没有任何查询高效的算法能提取出一个有效的相对较长的群元素.

    然而，这一困难问题面临一个固有的局限性，具体来说，仅当 $\mathsf{pk}_1$ 的长度显著短于 $\mathsf{str}$ 的长度时，该结论才成立. 当 KRA 安全的 NIKE 和 GGM 共享相同的安全参数时，这一条件是有保证的；然而，如果 NIKE 和 GGM 关联不同的安全参数，便是另一种情况. 这种局限性的原因在于，"较短"和"较长"是相对于安全参数而言的相对术语. 在大安全参数下被认为"较短"的公钥，在安全参数较小时，可能仍然携带足够的信息来提取"较长"的 GGM 编码. 因此，JZW+24 中的困难问题基于一个不合理的假设，并且其分析偏离了传统的黑盒分离.

- **我们的解决方法**：为了建立具有良好受控编码的群与稀疏 GGM 之间的黑盒分离，需要识别一个新的且无条件的困难问题. 利用 GGM 的稀疏性，可以将该困难问题定义如下：对于任何只能访问稀疏 GGM 且仅接收安全参数作为输入的查询高效算法，其只能以可忽略的概率输出一个新的且有效的群元素. 

    如果群元素 $\mathsf{str}$ 满足：

    1. $\mathsf{str}$ 已被算法用作某些加法查询的输入；
    2. $\mathsf{str}$ 尚未作为任何先前查询的输出出现过.

    那么该群元素被称为“新的”. 以上问题的困难性是无条件成立的. 

    接下来将阐释将此困难问题整合到黑盒分离中的策略. 粗略地说，如果敌手 $\mathcal{A}$ 在给定输入 $\mathsf{pk}_1$ 和 $\mathsf{pk}_2$ 的情况下，能够以良好的概率生成一个新的群元素，那么便可以构造一个提取器（extractor） $\mathcal{E}$，其仅以安全参数作为输入，也能以良好的概率生成一个新的群元素. 

    要解决的第一个问题是确定提取器 $\mathcal{E}$ 如何生成这两个公钥. 一个自然的方法是：

    1. $\mathcal{E}$ 随机选择两个私钥 $\mathsf{sk}_1$ 和 $\mathsf{sk}_2$，计算对应的公钥 $\mathsf{pk}_i = \mathsf{KGen}(\mathsf{sk}_i)$，并运行 $\mathcal{A}^\mathcal{G}(\mathsf{pk}_1, \mathsf{pk}_2)$；

    2. 每当 $\mathcal{A}$ 使用一个新的群元素 $\mathsf{str}$ 作为输入发起加法查询时，$\mathcal{E}$ 就输出 $\mathsf{str}$.

    不幸的是，这种方法会立即失败. 鉴于 GGM 是稀疏的，敌手 $\mathcal{A}$ 生成的任何新群元素 $\mathsf{str}$ 都应该与 $\mathsf{pk}_1$ 或 $\mathsf{pk}_2$ 相关；更准确地说，$\mathsf{str}$ 极有可能是在 $\mathsf{KGen}(\mathsf{sk}_1)$ 或 $\mathsf{KGen}(\mathsf{sk}_2)$ 的计算过程中出现的. 因此，如果遵循上述方法，即使 $\mathcal{A}$ 生成了一个群元素，提取器也无法成功提取出一个新的群元素.

    为了克服这一技术挑战，需要在公钥生成方案中利用受控编码. 具体而言，需要将 NIKE 配置为具有良好受控编码的 KRA 安全 NIKE，这就意味着存在一个从 $\mathbb{Z}_p$ 到公钥空间的受控编码，其中 $p$ 足够大. 显然，具有良好受控编码的 CDH 安全群蕴含了这样的 NIKE. 在此基础上便可以构建如下的提取器 $\mathcal{E}$：

    1. $\mathcal{E}$ 随机选择两个种子 $\mathsf{seed}_1$ 和 $\mathsf{seed}_2$，通过受控编码计算公钥 $\mathsf{pk}_i = \op{AE}^\mathcal{G}(\mathsf{seed}_i)$，并运行 $\mathcal{A}^\mathcal{G}(\mathsf{pk}_1, \mathsf{pk}_2)$；

    2. 每当 $\mathcal{A}$ 使用一个新的群元素 $\mathsf{str}$ 作为输入发起加法查询时，$\mathcal{E}$ 就输出 $\mathsf{str}$.

    此时，第二个技术挑战出现了. 具体来说，令 $S_\mathsf{AE}$ 表示在执行 $\mathsf{pk}_1 = \op{AE}^\mathcal{G}(\mathsf{seed}_1)$ 和 $\mathsf{pk}_2 = \op{AE}^\mathcal{G}(\mathsf{seed}_2)$ 期间产生的查询-响应对的集合. 如果敌手 $\mathcal{A}$ 生成的新的群元素始终落在 $S_\mathsf{AE}$ 中，那么 $\mathcal{E}$ 依然无法成功提取出一个新的群元素. 

    为此，需要改进敌手的策略. 具体来说，引进一个**预处理阶段**，给定输入 $\mathsf{pk}_1$ 和 $\mathsf{pk}_2$，敌手 $\mathcal{A}$ 进行受控编码的逆运算，计算 $\mathsf{seed}_i = \op{inv-AE}^\mathcal{G}(\mathsf{pk}_i)$，随后 $\mathcal{A}$ 重新计算 $\mathsf{pk}_i = \op{AE}^\mathcal{G}(\mathsf{seed}_i)$，并将所有查询-响应对添加到 $S_\mathsf{que-res}$ 中. 

    敌手在进入迭代阶段之前，先执行预处理阶段，这样就能保证敌手已经收集了 $S_\mathsf{AE}$ 中的所有查询-响应对，如果再生成一个新的群元素 $\mathsf{str}$，它对 $\mathcal{E}$ 来说就也是新的了. （上述大纲并不全面；详细的技术解释请参阅 Section 3）.

    分析的核心思想是：有效的公钥可以通过两种截然不同的方法生成. 在具有稠密编码的 NIKE 语境下，同样存在两种生成公钥的方法，其中一种甚至不需要进行任何查询. 因此，分析可以自然地延拓，以建立 CDH 安全的稠密群与稀疏 GGM 之间的黑盒分离. 此外，上述困难问题在 GBM 中依然有效，使得所有不可能性结果也能自然地扩展到稀疏 GBM 中.

#### EC-GGM vs. Sparse GGM

为了证明 EC-GGM 严格强于稀疏 GGM，我们将目标设定在不可区分性的框架内. 具体来说，我们确立了 EC-GGM（记为 $\op{\mathsf{ec}-\mathcal{G}}$）在统计意义上蕴含稀疏 GGM（记为 $\mathcal{G}$）；而稀疏 GGM 在计算意义上无法蕴含 EC-GGM.

- **EC-GGM 统计蕴含稀疏 GGM**: 首先解释为什么 $\op{\mathsf{ec}-\mathcal{G}}$ 能够抵抗统计敌手从而蕴含 $\mathcal{G}$. 令 $\op{\mathsf{ec}-\mathcal{G}} = (\op{ec-\mathcal{G}^\mathsf{L}}, \op{ec-\mathcal{G}^\mathsf{A}})$ 表示一个对应于定义在 $\mathbb{Z}_p$ 上的椭圆曲线的 EC-GGM，其中每个群元素表示为 $(u, b) \in \mathbb{Z}_p \times \{0, 1\}$. 根据 Hasse 界，EC-GGM 的编码本质上是稠密的. 为了将编码扩展至稀疏 GGM 所需的 $m$ 比特，需要引入一个额外的谕示机，即定义在 $\{0, 1\}^m$ 上的随机置换 $\mathsf{Perm}$ 以及其逆 $\mathsf{Perm}^\mathsf{Inv}$. 标记函数的定义如下：

    \[
        \mathsf{L}^\op{\mathsf{ec}-\mathcal{G}}(x) := \mathsf{Perm}(\op{ec-\mathcal{G}^\mathsf{L}}(x) \Vert 0\cdots 0).
    \]

    加法运算则通过调用逆谕示机 $\mathsf{Perm}^\mathsf{Inv}$ 来实现.

    为了证明不可区分性，需要构建一个模拟器 $\mathcal{S}$，其在只有 $\mathcal{G}$ 的访问权限的情况下，能够准确地模拟 $\op{\mathsf{ec}-\mathcal{G}}$ 以及 $(\mathsf{Perm}, \mathsf{Perm}^\mathsf{Inv})$ 的行为. 
    
    为了模拟 $\op{\mathsf{ec}-\mathcal{G}}$，模拟器会维护一张表来记录椭圆曲线点 $P := (u, b)$ 与字符串 $\mathsf{str} := \mathcal{G}(x)$ 之间的对应关系. EC-GGM 的一个重要性质为对于任意 $(u, b) \from \op{ec-\mathcal{G}^\mathsf{L}}(x)$ 和 $(u'. b') \from \op{ec-\mathcal{G}^\mathsf{L}}(-x)$，满足 $u = u'$ 且 $b = 1 - b'$. 因此，每当模拟器记录元组 $(P, \mathsf{str})$ 时，也会记录元组 $(-P, \mathcal{G}(-x))$，其中 $-P = (u, 1 - b)$. 值得注意的是，即便不知道 $x$ 的值，模拟器也能通过向 $\mathcal{G}$ 发起关于 $\mathsf{str}$ 的额外查询来计算 $\mathcal{G}(-x)$ 的值. 

    而为了模拟 $\mathsf{Perm}$，模拟器 $\mathcal{S}$ 首先检查该查询是否对应一个椭圆曲线点，以及是否存在对应的 $\mathcal{G}(x)$. 如果两个条件都满足，那么 $\mathcal{S}$ 就直接回复 $\mathcal{G}(x)$. 否则，$\mathcal{S}$ 根据查询是否对应一个有效点，分别回复 $\mathcal{G}(x)$（其中 $x$ 随机采样自 $\mathbb{Z}_N$）或者一个随机选择无效字符串 $\mathsf{str}$. 模拟 $\mathsf{Perm}^\mathsf{Inv}$ 的方法与此类似.

    ???+ tip "Remark"
        细心的读者可能会争辩说，在 EC-GGM 中，敌手可以执行某些非通用操作，例如不经意采样. 因而 EC-GGM 扩展了敌手的能力，这就有必要重新解释某些安全性假设（如 DLOG 和 CDH）的困难性.

    幸运的是，由于统计不可区分性，CDH 假设的困难性保持完好. 具体来说，可以证明：如果存在一个查询高效的统计敌手能在 EC-GGM 中攻破 CDH，就能构造一个能够攻破不可区分性的区分器. 更准确地说，该区分器充当 CDH 游戏中的挑战者，与敌手交互，并通过观察敌手是否成功赢得 CDH 游戏来区分现实世界与理想世界.

- **稀疏 GGM 无法计算地蕴含 EC-GGM**: 接下来证明即使在计算能力受限的敌手的前提下，也不可能在稀疏 GGM 中构造出一个不可区分的 EC-GGM. 假设存在一个从稀疏 GGM 派生出 EC-GGM 的推荐构造 $\Pi^\mathcal{G} := (\mathsf{L}^\mathcal{G}, \mathsf{A}^\mathcal{G})$，如何证明一个计算能力受限的敌手可以区分 $\Pi^\mathcal{G}$ 与 $\op{\mathsf{ec}-\mathcal{G}}$？

    一个常用的方法是找到一个在 $\op{\mathsf{ec}-\mathcal{G}}$ 中安全但是在任何 $\Pi^\mathcal{G}$ 构造中都能轻易攻破的一个安全游戏. 遵循 ZZ23 中概述的策略，将该安全游戏定义为**离散对数识别**（Discrete Logarithm Identification, DLI），其为离散对数问题的一个变体. DLI 游戏的内容如下：给定 $\mathsf{str} := \mathsf{L}(x)$，构造一个高效且无查询的概率电路 $\mathcal{C}$，使得 $\mathcal{C}(x)$ 以高概率被接受，而 $\mathcal{C}(x')$（其中 $x' \neq x$）以压倒性概率被拒绝. 
    
    接下来简要回顾 ZZ23 中的技术，其建立了 GGM 和 ROM 在计算能力受限敌手下的分离. 显然，DLI 在 GGM 中是安全的. 为了建立分离，其展示了 DLI 在任何由 ROM 构造的群中都可以被轻易攻破，敌手可以构造电路 $C$，$C(\cdot)$ 的功能与 $\mathsf{L}^\mathcal{H}(\cdot)$ 的功能相同，但不能访问 $\mathcal{H}$，并且如果重构的结果和 $\mathsf{L}^\mathcal{H}(x)$（硬编码在 $C$ 中）相同，则 $C$ 接受，否则拒绝. 

    ZZ23 中的核心思想是预测 $C$ 将向随机谕示机模型发出的查询，这使得敌手能够提前进行所有敏感查询，并将相应的查询-响应对硬编码到电路 $C$ 中，从而创建一个无谕示机的电路. 通过如下方式收集可以高概率得到敏感查询：

    1. 随机采样 $r, r_1, \ldots, r_n$，执行 $\mathsf{L}^\mathcal{H}(r), \mathsf{L}^\mathcal{H}(-r), \mathsf{L}^\mathcal{H}(r_1), \ldots, \mathsf{L}^\mathcal{H}(r_n)$，并将所有查询-响应对添加到集合 $S_\mathsf{que-res}$ 中.

    2. 执行 $\blue{\mathsf{L}^\mathcal{H}(x - r)} \from \mathsf{A}^\mathcal{H}(\mathsf{L}^\mathcal{H}(x), \mathsf{L}^\mathcal{H}(-r))$ 以及 $\mathsf{A}^\mathcal{H}(\blue{\mathsf{L}^\mathcal{H}(x - r)}, \mathsf{L}^\mathcal{H}(r))$，并将所有查询-响应对添加到集合 $S_\mathsf{que-res}$ 中.

    然后概述将上述技术纳入稀疏 GGM 分析的方法. 具体来说，给定输入 $\mathsf{L}^\mathcal{G}(x)$，敌手 $\mathcal{A}$ 首先执行上述步骤来收集查询-响应对，并将查询-响应对和 $\mathsf{L}^\mathcal{G}(x)$ 一起硬编码到电路 $C$ 中，然后输出 $C(\cdot)$. 随后分析 $\mathcal{A}$ 获胜的概率. 令 $Q_x$ 为执行 $\mathcal{L}^\mathcal{G}(x)$ 时生成的查询-响应对的集合，对每个对 $(\blue{\mathsf{que}}, \red{\mathsf{res}}) \in Q_x$，存在四种情况：

    1. 标签 $\mathsf{L}^\mathcal{G}(x)$ 完全不依赖于 $\red{\mathsf{res}}$；

    2. 标签 $\mathsf{L}^\mathcal{G}(x)$ 依赖于 $\red{\mathsf{res}}$，但在计算 $\mathsf{A}^\mathcal{G}(\mathsf{L}^\mathcal{G}(x - r), \mathsf{L}^\mathcal{G}(r))$ 时，$\red{\mathsf{res}}$ 未出现在响应中；

    3. 标签 $\mathsf{L}^\mathcal{G}(x)$ 依赖于 $\red{\mathsf{res}}$，且是在计算 $\mathsf{A}^\mathcal{G}(\mathsf{L}^\mathcal{G}(x - r), \mathsf{L}^\mathcal{G}(r))$ 时，通过对 $\mathcal{G}$ 进行标记查询得到的；

    4. 标签 $\mathsf{L}^\mathcal{G}(x)$ 依赖于 $\red{\mathsf{res}}$，且是在计算 $\mathsf{A}^\mathcal{G}(\mathsf{L}^\mathcal{G}(x - r), \mathsf{L}^\mathcal{G}(r))$ 时，通过对 $\mathcal{G}$ 进行加法查询得到的.

    情况 1 称为非敏感查询，因为 $\mathsf{L}^\mathcal{G}(x)$ 的计算不依赖于 $\red{\mathsf{res}}$，所以使用均匀采样的字符串替换对 $\blue{\mathsf{que}}$ 的响应也不会影响最终结果. 
    
    情况 2 称为敏感但频繁查询，由于 $\mathsf{A}^\mathcal{G}(\mathsf{L}^\mathcal{G}(x - r), \mathsf{L}^\mathcal{G}(r))$ 的计算中并没有通过查询获取 $\red{\mathsf{res}}$，所以 $\red{\mathsf{res}}$ 必然能从输入 $\mathsf{L}^\mathcal{G}(x - r)$ 或 $\mathsf{L}^\mathcal{G}(r)$ 中提取出来. 这就表明 $(\blue{\mathsf{que}}, \red{\mathsf{res}}) \in Q_x \cap (Q_{x-r} \cup Q_r)$ 以高概率成立. 此外，因为 $x, x - r, r$ 是两两独立的，这就意味着 $Q_x \cap Q_{x-r}$ 和 $Q_x \cap Q_r$ 只包含足够频繁的查询. 因此这一查询-响应对可以通过让 $\mathsf{L}^\mathcal{G}(\cdot)$ 在足够多的随机输入上运行来收集.

    情况 3 称为敏感标记查询，可以在 $\mathsf{A}^\mathcal{G}(\mathsf{L}^\mathcal{G}(x - r), \mathsf{L}^\mathcal{G}(r))$ 计算过程中直接收集所有标记查询.

    情况 4 称为敏感加法查询，其中 $\blue{\mathsf{que}} = (\blue{\mathsf{str}_1}, \blue{\mathsf{str}_2})$ 由两个有效的群元素组成. 尽管 $\red{\mathsf{res}}$ 出现在此查询中，但收集这类查询通常对我们的目的没有帮助. 具体来说，在执行 $\mathsf{L}^\mathcal{G}(x)$ 时，算法可能仅在点 $(x_1, \ldots, x_q)$ 处发起标记查询，但 $S_\mathsf{que-res}$ 中可能仅包含加法形式的查询-响应对，如 $(\blue{\mathsf{L}^\mathcal{G}(y_i)}, \blue{\mathsf{L}^\mathcal{G}(z_i)}, \red{\mathsf{L}^\mathcal{G}(y_i + z_i)})$，而并不显式知道 $y_i$ 和 $z_i$ 的值. 结果是在重构 $\mathsf{L}^\mathcal{G}(x)$ 时，算法可能在某些特定的点发起标记查询，但 $C$ 无法识别哪个元组对应正确的响应，导致重构失败.

    为了克服这一技术挑战，我们再次利用 GGM 的稀疏性属性. 注意，情况 4 查询的出现表明对手能够在不知道离散对数的情况下生成一个新的且有效的群元素. 因此，通过应用 1.3.1 节中概述的相同分析，我们可以构造一个提取器，仅给定安全参数作为输入，就能在情况 4 发生时产生一个新的且有效的群元素. 这证明了情况 4 发生的概率是可忽略的. 

## Preliminaries