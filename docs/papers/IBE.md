# Secure Identity-Based Encryption in the Quantum Random Oracle Model

## Preliminaries

### Weight Assignments

集合 $\mathcal{X}$ 上的权重分配指的是满足 $\sum_{x \in \mathcal{X}} D(x) = 1$ 的函数 $D: \mathcal{X} \to \mathbb{R}$，也会用 $\op{Pr}_D[{\text{event}}]$ 来表示相容于该事件的所有结果的权重之和.

集合 $\mathcal{X}$ 上的分布指的是满足 $D(x) \geq 0, \forall x \in \mathcal{X}$ 的权重分配. 如果 $D$ 是一个分布，那么 $x$ 发生的概率即为 $D(x)$. 记 $U_\mathcal{X}$ 为集合 $\mathcal{X}$ 上的均匀分布，$U_\mathcal{X}(x) = \frac{1}{\lvert \mathcal{X} \rvert}$.

给定一组 $\mathcal{X}$ 的权重分配 $D_y$，由 $y \in \mathcal{Y}$ 索引，以及 $\mathcal{Y}$ 上的一个权重分配 $D$，按如下定义 $\mathcal{X}$ 上的权重分配 $D'$：

\[
    D'(x) = \sum_{y \in \mathcal{Y}} D(y) D_y(x), \forall x \in \mathcal{X}
\]

给定 $\mathcal{Y}$ 上的两个权重分配 $D_1$ 和 $D_2$，可以对应的定义 $\mathcal{X}$ 上的两个权重分配 $D_1'$ 和 $D_2'$，可以证明：

\begin{align*}
    \lvert D_1' - D_2' \rvert & = \sum_{x \in \mathcal{X}} \lvert \sum_{y \in \mathcal{Y}} (D_1(y) - D_2(y)) D_y(x) \rvert \\
    & \leq \sum_{x \in \mathcal{X}, y \in \mathcal{Y}} \lvert (D_1(y) - D_2(y)) D_y(x) \rvert \\
    & = \sum_{x \in \mathcal{X}, y \in \mathcal{Y}} \lvert D_1(y) - D_2(y) \rvert D_y(x) \\
    & = \sum_{y \in \mathcal{Y}} \lvert D_1(y) - D_2(y) \rvert = \lvert D_1 - D_2 \rvert.
\end{align*}

考虑函数族 $H: \mathcal{X} \to \mathcal{Y}$，所构成的集合记为 $\mathcal{H}_{\mathcal{X}, \mathcal{Y}}$，并定义其上的一个权重分配 $D$. 设 $\mathcal{W} \subseteq \mathcal{X}$，定义边际权重分配 $D_\mathcal{W}$，其中函数 $H_\mathcal{W}: \mathcal{W} \to \mathcal{Y}$ 的权重等于所有与 $H_\mathcal{W}$ 在 $\mathcal{W}$ 上的值相同的函数 $H \in \mathcal{H}_{\mathcal{X}, \mathcal{Y}}$ 的权重之和. 也就是说，

\[
    D_\mathcal{W}(H_\mathcal{W}) = \op{Pr}_D[H(w) = H_\mathcal{W}(w), \forall w \in \mathcal{W}].
\]

称两个权重分配 $D_1$ 和 $D_2$ 是 $k-wise$ 等价的，如果对于任意 $\mathcal{W} \subseteq \mathcal{X}$，$\lvert \mathcal{W} \rvert = k$，两个边际权重分配 $D_{1, \mathcal{W}}$ 和 $D_{2, \mathcal{W}}$ 是相同的. 

### Cryptographic Primitives

基于身份的加密方案（IBE）是一个概率多项式算法四元组 $\mathsf{IBE} = (\mathsf{IBE.Gen}, \mathsf{IBE.Extract}, \mathsf{IBE.Enc}, \mathsf{IBE.Dec})$. 其中：

1. $\mathsf{IBE.Gen}(1^n)$ 生成主密钥对 $(\mathsf{mpk}, \mathsf{msk})$；

2. $\mathsf{IBE.Extract}_\mathsf{msk}(\cdot)$ 为对应身份生成私钥；

3. $\mathsf{IBE.Enc}_{\mathsf{mpk}}(\cdot)$ 使用主公钥加密消息给对应身份；

4. $\mathsf{IBE.Dec}(\cdot)$ 使用私钥解密消息.

安全性使用选择身份和明文攻击下的不可区分性定义（IND-ID-CPA）定义.

## Distinguishing Oracles With Quantum Queries

## Semi-Constant Distributions

!!! info "Semi-Constant Distributions"
    定义 $\mathsf{SC}_\lambda$ 为半恒定分布，其为 $\mathcal{H}_{\mathcal{X}, \mathcal{Y}}$ 上的一个分布，满足：

    - 随机选取 $\mathcal{Y}$ 中的一个元素 $y$；

    - 对每个 $x \in \mathcal{X}$：

        - 以 $\lambda$ 的概率，令 $H(x) = y$，称 $x$ 是 $H$ 的一个可区分输入；

        - 以 $1 - \lambda$ 的概率，设置 $H(x)$ 为 $\mathcal{Y}$ 中的一个随机元素.

注意到 $\mathsf{SC}_0$ 就是均匀分布. 想法便是约束量子算法区分 $\mathsf{SC}_\lambda$ 和 $\mathsf{SC}_0 = U$ 的能力，采用的是上一部分的定理.

!!! success "Lemma"
    固定 $k$，对每 $k$ 个对 $(x_i, r_i)$，概率 $\op{Pr}_{H \from \mathsf{SC}_\lambda}[H(x_i) = r_i \forall i \in {1, \ldots, k}]$ 是一个 $\lambda$ 的 $k$ 阶多项式，并且一阶导数在 $0$ 处的值为 $0$.