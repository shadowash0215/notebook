# On the Compressed-Oracle Technique, and Post-Quantum Security of Proofs of Sequential Work

## Notation

### Operators and Their Norms

$\mathcal{H}$: 有限维复 Hilbert 空间，默认 $\mathcal{H} = \mathbb{C}^d$.

如果算子 $\rho \in \mathcal{L}(\mathcal{H})$ 的支撑落在 $\mathcal{H}_o \subset \mathcal{H}$ 上，那么混合态 $\rho$ 被称为被子空间 $\mathcal{H}_o$ **支撑**.

$\lVert A \rVert$: $A \in \mathcal{L}(\mathcal{H}, \mathcal{H'})$ 的算子范数，被 Frobenius 范数约束上界.

**Basic Properties**: 如果 $\mathcal{H}$ 可以被分解为若干互相正交子空间的直和 $\mathcal{H} = \bigoplus_i \mathcal{H}_i$，且 $A \in \mathcal{L}({\mathcal{H}})$ 在 $\mathcal{H}_i$ 上的限制为 $B_i \in \mathcal{L}(\mathcal{H}_i)$，那么

\[
    \lVert A \rVert = \max_{1 \leq i \leq m} \lVert B_i \rVert.
\]

### The Computational and the Fourier Basis

设 $\mathcal{Y}$ 为一个基数为 $M$ 的 Abelian 群，$\{\ket{y}\}_{y \in \mathcal{Y}}$ 为 $\mathcal{H} = \mathbb{C}^m$ 的一组（正交）基，其由 $\mathcal{Y}$ 中元素索引，称为**计算基**，这里的 $\mathcal{H}$ 也记作 $\mathbb{C}[\mathcal{Y}]$. 设 $\mathcal{Y}$ 的对偶群为 $\mathcal{\hat{Y}}$，其中的元素为所有群同态 $\mathcal{Y} \to \{w \in \mathbb{C} \mid \lvert w \rvert = 1\}$，考虑其为加法群，单位元为 $\hat{0}$. Fourier 基 $\{\ket{\hat{y}}\}_{\hat{y} \in \mathcal{\hat{Y}}}$ 由如下基本变换定义：

\[
    \ket{\hat{y}} = \frac{1}{\sqrt{M}} \sum_{y} \hat{y}(y)^* \ket{y} \quad \text{and} \quad \ket{y} = \frac{1}{\sqrt{M}} \sum_{\hat{y}} \hat{y}(y) \ket{\hat{y}},
\]

其中 $(\cdot)^*$ 为复共轭. 从而有 $\mathbb{C}[\mathcal{Y}] = \mathbb{C}[\mathcal{\hat{Y}}] = \mathcal{H}$. 设 $U \in \mathcal{L}(\mathbb{C}[\mathcal{Y}] \otimes \mathbb{C}[\mathcal{Y}])$ 定义为 $U\ket{y} \ket{y'} \to \ket{y + y'}\ket{y'}, y, y' \in \mathcal{Y}$. 那么对于 $\hat{y}, \hat{y}' \in \mathcal{\hat{Y}}$，其作用为 $U\ket{\hat{y}}\ket{\hat{y}'} \to \ket{\hat{y}}\ket{\hat{y}' - \hat{y}}$.

??? "proof"
    \begin{align*}
        U \ket{\hat{y}} \ket{\hat{y}'} &= U \left( \frac{1}{\sqrt{M}} \sum_{y} \hat{y}(y)^* \ket{y} \right) \left( \frac{1}{\sqrt{M}} \sum_{y'} \hat{y}'(y')^* \ket{y'} \right) \\
        &= \frac{1}{M} \sum_{y,y'} \hat{y}(y)^* \hat{y}'(y')^* U \ket{y} \ket{y'} \\
        &= \frac{1}{M} \sum_{y,y'} \hat{y}(y)^* \hat{y}'(y')^* \ket{y + y'} \ket{y'}.
    \end{align*}

    令 $z = y + y'$，则 $y = z - y'$.

    \begin{align*}
        U \ket{\hat{y}} \ket{\hat{y}'} &= \frac{1}{M} \sum_{z,y'} \hat{y}(z - y')^* \hat{y}'(y')^* \ket{z} \ket{y'} \\
                                       &= \frac{1}{M} \sum_{z,y'} \hat{y}(z)^* \hat{y}(-y')^* \hat{y}'(y')^* \ket{z} \ket{y'} \\
                                       &= \frac{1}{M} \sum_{z,y'} \hat{y}(z)^* (\hat{y} - \hat{y}')(y') \ket{z} \ket{y'} \\
                                       &= \frac{1}{\sqrt{M}} \sum_{z} \hat{y}(z)^* \ket{z} \otimes \frac{1}{\sqrt{M}} \sum_{y'} (\hat{y}' - \hat{y})(y')^* \ket{y'} \\
                                       &= \ket{\hat{y}} \ket{\hat{y}' - \hat{y}}.
    \end{align*}

可以通过添加 $\perp$ 来扩展 $\mathcal{Y}$ 和 $\mathcal{\hat{Y}}$. 选择一个归一化的 $\ket{\perp} \in \mathbb{C}^{M+1}$，其和 $\mathbb{C}[\mathcal{Y}] = \mathbb{C}[\mathcal{\hat{Y}}]$ 正交. $\mathbb{C}^{M+1}$ 便可以记作 $\mathbb{C}[\mathcal{Y} \cup \{\perp\}] = \mathbb{C}[\mathcal{\hat{Y}} \cup \{\perp\}]$.

### Functions and Their (Quantum) Representations

对任意固定非空集合 $\mathcal{X}$，$H: \mathcal{X} \to \mathcal{Y}$ 构成的集合记作 $\mathfrak{H}$. $\mathfrak{\hat{H}} = \{\hat{H}: \mathcal{\hat{X}} \to \mathcal{\hat{Y}}\}$. 考虑 $\ket{H} = \bigotimes_{x \in \mathcal{X}} \ket{H(x)}$ 作为 $H$ 的**量子表示**，由所有的向量 $\ket{H}$ 张成的空间 $\bigotimes_x \mathbb{C}[\mathcal{Y}]$ 记作 $\mathbb{C}[\mathfrak{H}]$. $\ket{\hat{H}}$ 和 $\mathbb{C}[\mathfrak{\hat{H}}]$ 的定义类似，同样有 $\mathbb{C}[\mathfrak{H}] = \mathbb{C}[\mathfrak{\hat{H}}]$.

将 $\mathcal{Y}$ 扩展为 $\mathcal{\bar{Y}} = \mathcal{Y} \cup \{\perp\}$，函数 $D: \mathcal{X} \to \mathcal{\bar{Y}}$ 构成的集合记作 $\mathfrak{D}$. $\mathfrak{\hat{D}}, \ket{D}$ 等的定义类似，且有 $\mathbb{C}[\mathfrak{D}] = \mathbb{C}[\mathfrak{\hat{D}}]$.

对 $D \in \mathfrak{D}$ 以及 $\mathbf{x} = (x_1, \ldots, x_k) \in \mathcal{X}^k$，记 $D(\mathbf{x}) = (D(x_1), \ldots, D(x_k)) \in \mathcal{\bar{Y}}^k$，$\mathcal{H} \in \mathfrak{H}$ 类似. 而如果 $\mathbf{x}$ 的分量两两互异，且 $\mathbf{r} = (r_1, \ldots, r_k) \in \mathcal{\bar{Y}}^k$，则可以定义 $D[\mathbf{x} \mapsto \mathbf{r}] \in \mathfrak{D}$ 为

\[
    D[\mathbf{x} \mapsto \mathbf{r}] (x_i) = r_i \quad \text{and} \quad D[\mathbf{x} \mapsto \mathbf{r}] (\bar{x}) = D(\bar{x}) \ \forall \bar{x} \not \in \{x_1, \ldots, x_k\}.
\]

## Zhandry's Compressed Oracle - Refurbished

### The Compressed Oracle

核心是考虑所有 $H \in \mathfrak{H}$ 的一个叠加态 $\sum_{H} \ket{H}$，然后在 Fourier 基下分析：

\[
    \ket{\Pi_0} = \sum_{H} \ket{H} = \bigotimes_x (\sum_{y} \ket{y}) = \sqrt{M} \bigotimes_x \ket{\hat{0}} = \sqrt{M} \ket{\mathbf{\hat{0}}} \in \mathbb{C}[\mathfrak{H}]
\]

设谕示机请求中包含的酉变换在计算基下为

\[
    \mathsf{O} = \ket{x}\ket{y} \otimes \ket{H} \mapsto \ket{x} \ket{y + H(x)} \otimes \ket{H},
\]

那么在 Fourier 基下，我们有

\[
    \mathsf{O} = \ket{x}\ket{\hat{y}} \otimes \ket{\hat{H}} \mapsto \ket{x} \ket{\hat{y}} \otimes \mathsf{O}_{x \hat{y}} \ket{\hat{H}} = \ket{x} \ket{\hat{y}} \otimes \ket{\hat{H} - \hat{y} \cdot \delta_x}.
\]

等式给出了 $\mathsf{O}_{x \hat{y}}$ 的定义. $\mathsf{O}_{x \hat{y}}$ 只对 $x$ 寄存器作用，并且有 $\mathsf{O}_{x \hat{y}} \mathbf{O}_{x \hat{y}'} = \mathsf{O}_{x, \hat{y} + \hat{y}'}$，所以 $\mathbf{O}_{x \hat{y}}$ 和 $\mathbf{O}_{x' \hat{y}'}$ 均可交换. 因而 $q$ 次查询后，谕示机内部的状态由 $\ket{\hat{H}} = \ket{\hat{y}_1 \delta_{x_1} + \cdots + \hat{y}_q \delta_{x_q}}$ 支撑.

实际的压缩谕示机通过对所有的寄存器 $x$ 施加如下的同构获得：

\[
    \op{Comp}_x = \ket{\perp} \bra{\hat{0}} + \sum_{\hat{z} \neq \hat{0}} \ket{\hat{z}} \bra{\hat{z}}: \mathbb{C}[\mathcal{Y}] \to \mathbb{C}[\mathcal{\bar{Y}}], \ket{\hat{y}} \to \begin{cases} \ket{\perp}, \text{ if } \hat{y} = \hat{0} \\ \ket{\hat{y}}, \text{ if } \hat{y} \neq \hat{0} \end{cases}
\]

整个压缩算子 $\op{Comp} = \bigotimes_x \op{Comp}_x: \mathbb{C}[\mathfrak{H}] \to \mathbb{C}[\mathfrak{D}]$ 将 $\ket{\Pi_0}$ 映射为

\[
    \op{Comp} \ket{\Pi_0} = \left(\bigotimes_x \op{Comp}_x \right) \left(\bigotimes_x \ket{\hat{0}} \right) = \bigotimes_x \op{Comp}_x \ket{\hat{0}} = \bigotimes_x \ket{\perp} = \ket{\mathbf{\perp}}.
\]

推而广之，对任意的 $\hat{H} \in \hat{\mathfrak{H}}$，$\op{Comp} \ket{\hat{H}} = \ket{\hat{D}}$，其中 $\hat{D} \in \hat{\mathfrak{D}}$，若 $\hat{H}(x) \neq 0$ 则 $\hat{D}(x) = \hat{H}(x)$，否则 $\hat{D}(x) = \perp$. 

### Linking the Compressed and the Original Oracle

!!! success "Lemma"
    考虑任意（归一化）的量子态 $\ket{\Pi} \in \mathbb{C}[\mathfrak{H}]$，$\ket{\Delta} = \op{Comp} \ket{\Pi} \in \mathbb{C}[\mathfrak{D}]$ 为对应的“压缩数据库”. 设 $\mathbf{x} = (x_1, \ldots, x_l)$ 包含的都是两两互异的 $x_i \in \mathcal{X}$，$\mathbf{y} = (y_1, \ldots, y_l) \in \mathcal{Y}^l$，$P_\mathbf{x} = \ket{y_1}\bra{y_1} \otimes \cdots \otimes \ket{y_l}\bra{y_l}$，其中 $\ket{y_i}\bra{y_i}$ 作用在寄存器 $x_i$ 上，那么

    \[
        \lVert P_\mathbf{x} \ket{\Pi} \rVert \leq \lVert P_\mathbf{x} \ket{\Delta} \rVert + \sqrt{\frac{l}{M}}.
    \]

    ???+ success "Proof"
        $\op{Comp}_{\mathbf{x}}$ 为作用在寄存器 $x_1, \ldots, x_l$ 上的压缩算子，$I_\bar{\mathbf{x}}$ 为作用在其余寄存器上的恒等算子. 有

        \begin{align*}
            \lVert P_\mathbf{x} \ket{\Pi} \rVert - \lVert P_\mathbf{x} \op{Comp} \ket{\Pi} \rVert
            & = \lVert P_\mathbf{x} \ket{\Pi} \rVert - \lVert P_\mathbf{x} \op{Comp}_{\mathbf{x}} \ket{\Pi} \rVert \\
            & \leq \lVert (P_\mathbf{x} - P_\mathbf{x} \op{Comp}_{\mathbf{x}}) \ket{\Pi} \rVert \\
            & \leq \lVert (P_\mathbf{x} - P_\mathbf{x} \op{Comp}_{\mathbf{x}}) \otimes I_\bar{\mathbf{x}} \rVert \\
            & = \lVert (P_\mathbf{x} - P_\mathbf{x} \op{Comp}_{\mathbf{x}}) \rVert
        \end{align*}

        考虑 Fourier 下的 $P_\mathbf{x}$，因为

        \begin{align*}
            \ket{y_i} \bra{y_i} &= \left(\frac{1}{\sqrt{M}} \sum_{\hat{z} \in \mathcal{\hat{Y}}} \hat{z}(y_i) \ket{\hat{z}} \right) \left(\frac{1}{\sqrt{M}} \sum_{\hat{y} \in \mathcal{\hat{Y}}} \hat{y}(y_i)^* \bra{\hat{y}} \right) \\
                                &= \frac{1}{M} \sum_{\hat{z}, \hat{y} \in \mathcal{\hat{Y}}} \hat{z}(y_i) \hat{y}(y_i)^* \ket{\hat{z}} \bra{\hat{y}},
        \end{align*}

        引入相位因子 $\omega_{\hat{z}/\hat{y}} (y_i) = \hat{z}(y_i) \hat{y}(y_i)^*$，便有

        \[
            P_\mathbf{x} = \bigotimes_i \frac{1}{M} \sum_{\hat{z}, \hat{y} \in \mathcal{\hat{Y}}} \omega_{\hat{z}/\hat{y}}(y_i) \ket{\hat{z}} \bra{\hat{y}}.
        \]

        所以有

        \[
            P_\mathbf{x} \op{Comp}_\mathbf{x} = \bigotimes_i \frac{1}{M} \sum_{\hat{z}, \hat{0} \neq \hat{y} \in \mathcal{\hat{Y}}} \omega_{\hat{z}/\hat{y}}(y_i) \ket{\hat{z}} \bra{\hat{y}}.
        \]

        张量积展开得到

        \begin{align*}
            P_\mathbf{x} - P_\mathbf{x} \op{Comp}_\mathbf{x} 
            & = \frac{1}{M^l} \sum_{\hat{y}_1, \ldots, \hat{z}_l \in \mathcal{\hat{Y}} \text{ and } \exists i: \hat{y}_i = \hat{0}} \omega_{\hat{z}_i/\hat{y}_i}(y_i) \ket{\hat{z}_i} \bra{\hat{y}_i} \\
            & = \frac{1}{M^l} \sum_{\hat{\mathbf{y}}, \hat{\mathbf{z}} \text{ and } \exists i: \hat{y}_i = \hat{0}} \omega_{\hat{\mathbf{z}}/\hat{\mathbf{y}}} \ket{\hat{\mathbf{z}}} \bra{\hat{\mathbf{y}}}.
        \end{align*}

        其中 $\hat{\mathbf{y}} = (\hat{y}_1, \ldots, \hat{y}_l), \hat{\mathbf{z}} = (\hat{z}_1, \ldots, \hat{z}_l) \in \mathcal{\hat{Y}}^l$. $\omega_{\hat{\mathbf{z}}/\hat{\mathbf{y}}} = \prod_i \omega_{\hat{z}_i/\hat{y}_i}$.

        使用 Frobenius 范数约束算子范数，有

        \begin{align*}
            \lVert P_\mathbf{x} - P_\mathbf{x} \op{Comp}_\mathbf{x} \rVert^2 
            & \leq \sum_{\hat{\mathbf{y}}, \hat{\mathbf{z}}} \lvert \bra{\hat{\mathbf{z}} (P_\mathbf{x} - P_\mathbf{x} \op{Comp}_\mathbf{x})} \ket{\hat{\mathbf{y}}} \rvert^2 \\
            & = \frac{1}{M^{2l}} \sum_{\hat{\mathbf{y}}, \hat{\mathbf{z}} \text{ and } \exists i: \hat{y}_i = \hat{0}} \lvert \omega_{\hat{\mathbf{z}}/\hat{\mathbf{y}}} \rvert^2 \\
            & \leq \frac{1}{M^{2l}} l M^{2l-1} = \frac{l}{M}.
        \end{align*}

        最后一行是简单的计数估计，为 $0$ 的位置有 $l$ 种，并且对应的有 $M^{l-1}$ 种选择. 尽管有所重复，但实际上是放的更松了.

!!! success "Corollary"
    设关系 $R \subset \mathcal{X}^l \times \mathbf{Y}^l$，$\mathcal{A}$ 为输出 $\mathbf{x} \in \mathcal{X}^l$ 和 $\mathbf{y} \in \mathcal{Y}^l$ 的量子谕示机算法. 设 $p$ 为在 $\mathcal{A}$ 与用均匀随机函数 $H$ 初始化的标准随机谕示机交互的条件下满足 $\mathbf{y} = H(\mathbf{x})$ 且 $(\mathbf{x}, \mathbf{y}) \in R$ 的概率，而 $p'$ 为在 $\mathcal{A}$ 与压缩谕示机交互且 $D$ 为测量压缩谕示机内部状态获得的条件下满足 $\mathbf{y} = D(\mathbf{x})$ 且 $(\mathbf{x}, \mathbf{y}) \in R$ 的概率，则有

    \[
        \sqrt{p} \leq \sqrt{p'} + \sqrt{\frac{l}{M}}.
    \]

    ???+ success "Proof"
        考虑 $\mathcal{A}$ 和纯化谕示机交互时的执行. 假定测量 $\mathbf{x}, \mathbf{y}$ 后，$\mathcal{A}$ 还会在计算基下测量其内部状态得到字符串 $w$，并且输出. 设 $q_{\mathbf{x}, \mathbf{y}, w}$ 为 $\mathcal{A}$ 输出三元组 $\mathbf{x}, \mathbf{y}, w$ 的概率， $p_{\mathbf{x}, \mathbf{y}, w}$ 为给定 $\mathcal{A}$ 的输出的条件下 $\mathbf{y} = H(\mathbf{x})$ 的概率，$p_{\mathbf{x}, \mathbf{y}, w}'$ 为同样条件下 $\mathbf{y} = D(\mathbf{x})$ 的概率，首先观察到：

        \begin{align*}
            p &= \sum_{\mathbf{x}, \mathbf{y}, w \text{ and } (x, y) \in R} q_{\mathbf{x}, \mathbf{y}, w} \ p_{\mathbf{x}, \mathbf{y}, w}, \\ 
            p' &= \sum_{\mathbf{x}, \mathbf{y}, w \text{ and } (x, y) \in R} q_{\mathbf{x}, \mathbf{y}, w} \ p_{\mathbf{x}, \mathbf{y}, w}'.
        \end{align*}

        $p_{\mathbf{x}, \mathbf{y}, w} = \lVert P_\mathbf{x} \ket{\Pi} \rVert^2$，$\ket{\Pi}$ 是根据 $\mathbf{x}, \mathbf{y}$ 和 $w$ **后选择**的纯化谕示机的内部状态. 同理 $p_{\mathbf{x}, \mathbf{y}, w}' = \lVert P_\mathbf{x} \op{Comp} \ket{\Pi} \rVert^2$. 依据引理再平方有

        \[
            p_{\mathbf{x}, \mathbf{y}, w} \leq (\sqrt{p_{\mathbf{x}, \mathbf{y}, w}'}) + \sqrt{\frac{l}{M}})^2 = p_{\mathbf{x}, \mathbf{y}, w}' + 2\sqrt{p_{\mathbf{x}, \mathbf{y}, w}'}\sqrt{\frac{l}{M}} + \frac{l}{M}.
        \]

        设 $Q = \sum_{\mathbf{x}, \mathbf{y}, w \text{ and } (x, y) \in R} q_{\mathbf{x}, \mathbf{y}, w}$，两侧用 $q_{\mathbf{x}, \mathbf{y}, w}$ 加权平均并应用 Jensen 不等式可以得到

        \begin{align*}
            p & \leq p' + 2 \sum_{\mathbf{x}, \mathbf{y}, w \text{ and } (x, y) \in R} q_{\mathbf{x}, \mathbf{y}, w} \sqrt{p_{\mathbf{x}, \mathbf{y}, w}'} \sqrt{ \frac{l}{M} } + Q \cdot \frac{l}{M} \\
              & \leq p' + 2 \sqrt{ \frac{l}{M} } Q \cdot \sqrt{ \frac{\sum_{\mathbf{x}, \mathbf{y}, w \text{ and } (x, y) \in R} q_{\mathbf{x}, \mathbf{y}, w} p_{\mathbf{x}, \mathbf{y}, w}'}{Q} } + \frac{l}{M} \\
              & \leq p' + 2 \sqrt{ \frac{l}{M} } \cdot \sqrt{Q \cdot p'} + \frac{l}{M} \\
              & \leq (\sqrt{p'} + \sqrt{\frac{l}{M}})^2.
        \end{align*}

        从而有

        \[
            \sqrt{p} \leq \sqrt{p'} + \sqrt{\frac{l}{M}}.
        \]

### Working Out the Transition Matrix

扩展 $\op{Comp}_x$ 的定义域到 $\mathbb{C}[\mathcal{\bar{Y}}]$，定义 $\op{Comp}_x \ket{\perp} = \ket{\hat{0}}$.

定义：

\[
    \mathsf{cO} = \op{Comp} \circ \mathsf{O} \circ \op{Comp}^\dagger \in \mathcal{L}(\mathbb{C}[\mathcal{X}] \otimes \mathbb{C}[\mathcal{Y}] \otimes \mathbb{C}[\mathfrak{D}])
\]

对任意 $D \in \mathfrak{D}$，其将 $\ket{x} \ket{\hat{y}} \otimes \ket{D}$ 映射为 $\ket{x} \ket{\hat{y}} \otimes \mathsf{cO}_{x\hat{y}} \ket{D}$，其中 $\mathsf{cO}_{x\hat{y}} = \op{Comp}_x \circ \mathsf{O}_{x\hat{y}} \circ \op{Comp}_x^\dagger \in \mathcal{L}(\mathbb{C}[\mathcal{\bar{Y}}])$ 只作用在寄存器 $x$ 上. 

有交换图：

\tikzcd
    \mathbb{C}[\mathfrak{H}] \arrow[r, "\operatorname{Comp}"] \arrow[d, "\mathsf{O}_{x\hat{y}}"] & \mathbb{C}[\mathfrak{D}] \arrow[d, "\mathsf{cO}_{x\hat{y}}"] \\
    \mathbb{C}[\mathfrak{H}] \arrow[r, "\operatorname{Comp}"] & \mathbb{C}[\mathfrak{D}]

!!! success "Lemma"
    对任意 $\hat{y} \neq \hat{0}$，$\mathsf{cO}_{x \hat{y}}$ 在计算基下的矩阵表示由下表给出，也即对任意 $r, u \in \mathcal{\bar{Y}}$ 有 $\bra{u} \mathsf{cO}_{x \hat{y}} \ket{r} = \gamma^{\hat{y}}_{u, r}$. 此外 $\mathsf{cO}_{x, \hat{0}} = I$.

    |         | $\perp$ | $r \in \mathcal{Y}$ |
    |:-------:|:-------:|:-------------------:|
    | $\perp$ | $\gamma^{\hat{y}}_{\perp, \perp} = 0$ | $\gamma^{\hat{y}}_{\perp, r} = \frac{\hat{y}(r)}{\sqrt{M}}$ |
    | $u \in \mathcal{Y}$ | $\gamma^{\hat{y}}_{u, \perp} = \frac{\hat{y}(u)}{\sqrt{M}}$ | $\gamma^{\hat{y}}_{u, r} = \begin{cases} (1 - \frac{2}{M})\hat{y}(u) + \frac{1}{M} & \text{if } u = r \\ \frac{1 - \hat{y}(r) - \hat{y}(u)}{M} & \text{if } u \neq r \end{cases}$ |


    ???+ success "Proof"
        对任意 $r \neq \perp$ 以及 $\hat{y} \neq \hat{0}$ 有

        \[
            \sqrt{M}\ket{r} = \sum_{\hat{r}} \hat{r}(r) \ket{\hat{r}} = \ket{\hat{0}} + \sum_{\hat{r} \neq \hat{0}} \hat{r}(r) \ket{\hat{r}},
        \]

        经过 $\op{Comp}^\dagger$ 的作用后映射为 $\ket{\perp} + \sum_{\hat{r} \neq \hat{0}} \hat{r}(r) \ket{\hat{r}}$. 再经 $\mathsf{O}_{x\hat{y}}$ 的作用后映射为

        \begin{align*}
            & \mapsto \ket{\perp} + \sum_{\hat{r} \neq \hat{0}} \hat{r}(r) \ket{\hat{r} - \hat{y}} \\
            & = \ket{\perp} - \ket{-\hat{y}} + \sum_{\hat{r}} \hat{r}(r) \ket{\hat{r} - \hat{y}} \\
            & = \ket{\perp} - \ket{-\hat{y}} + \hat{y}(r) \sum_{\hat{r}} \hat{r}(r) \ket{\hat{r}} \\
            & = \ket{\perp} - \ket{-\hat{y}} + \hat{y}(r) \ket{\hat{0}} + \hat{y}(r) \sum_{\hat{r} \neq \hat{0}} \hat{r}(r) \ket{\hat{r}}.
        \end{align*}

        继续经过 $\op{Comp}$ 映射

        \begin{align*}
            & \mapsto \ket{\hat{0}} - \ket{-\hat{y}} + \hat{y}(r)\ket{\perp} + \hat{y}(r) \sum_{\hat{r} \neq \hat{0}} \hat{r}(r) \ket{\hat{r}} \\
            & = \ket{\hat{0}} - \ket{-\hat{y}} + \hat{y}(r)\ket{\perp} - \hat{y}(r)\ket{\hat{0}} + \hat{y}(r) \sum_{\hat{r}} \hat{r}(r) \ket{\hat{r}} \\
            & = \frac{1}{\sqrt{M}} \sum_u \ket{u} - \frac{1}{\sqrt{M}} \sum_u \hat{y}(u) \ket{u} + \hat{y}(r)\ket{\perp} - \frac{\hat{y}(r)}{\sqrt{M}} \sum_u \ket{u} + \sqrt{M} \hat{y}(r) \ket{r}.
        \end{align*}

        所以有

        \[
            \mathsf{cO}_{x\hat{y}} \ket{r} = \frac{1}{M} \sum_u \ket{u} - \frac{1}{M} \sum_u \hat{y}(u) \ket{u} + \frac{\hat{y}(r)}{\sqrt{M}}\ket{\perp} - \frac{\hat{y}(r)}{M} \sum_u \ket{u} + \hat{y}(r) \ket{r}.
        \]

        由此便可以得出 $r \neq \perp$ 对应的系数 $\gamma^{\hat{y}}_{u, r}$. 而对于 $r = \perp$ 的情况，有

        \[
            \ket{\perp} \mapsto \ket{\hat{0}} \mapsto \ket{-\hat{y}} \mapsto \ket{-\hat{y}} = \frac{1}{\sqrt{M}} \sum_u \hat{y}(u) \ket{u},
        \]

        也就能得到 $r = \perp$ 对应的系数 $\gamma^{\hat{y}}_{u, \perp}$. 利用 $\mathsf{O}_{x, \hat{0}} = I$ 便可以得到 $\hat{y} = \hat{0}$ 的情况.

### The Parallel-Query (Compressed) Oracle

$k$-并行查询定义为

\[
    \mathsf{O}^k: \ \ket{\mathbf{x}}\ket{\mathbf{y}} \otimes \ket{H} \mapsto \ket{\mathbf{x}} \ket{\mathbf{y} + H(\mathbf{x})} \otimes \ket{H}.
\]

其中 $\mathbf{x} = (x_1, x_2, \ldots, x_k) \in \mathcal{X}^k$，$\mathbf{y} = (y_1, y_2, \ldots, y_k) \in \mathcal{Y}^k$. $\mathsf{cO}^k = \op{Comp} \circ \mathsf{O}^k \circ \op{Comp}^\dagger$，作用为

\[
    \mathsf{cO}^k: \ \ket{\mathbf{x}}\ket{\mathbf{\hat{y}}} \otimes \ket{\Delta} \mapsto \ket{\mathbf{x}} \ket{\mathbf{\hat{y}} \otimes \mathsf{cO}_{\mathbf{x} \mathbf{\hat{y}}}} \otimes \ket{\Delta}.
\]

其中 $\mathbf{cO}_{\mathbf{x} \mathbf{\hat{y}}} = \mathsf{cO}_{x_1 \hat{y}_1} \cdots \mathsf{cO}_{x_k \hat{y}_k}$.

## A Framework for Proving Quantum Query Lower Bounds

## Setting Up the Framework

数据库性质：数据库 $\mathfrak{D}$ 的一个子集 $\mathsf{P} \subset \mathfrak{D}$.

$\mathsf{P}(D)$ 也用来表示 $D \in \mathsf{P}$，即 $D$ 满足 $\mathsf{P}$；$\mathsf{P}$ 也被重载表示为投影算子 $\sum_{D \in \mathsf{P}} \ket{D}\bra{D} \in \mathcal{L}(\mathbb{C}[\mathfrak{D}])$.

- $\mathsf{PRMG} = \{D \mid \exists x: \ D(x) = 0\}$;

- $\mathsf{CL} = \{D \mid \exists x, x': \ D(x) = D(x') \neq \perp\}$;

- $\mathsf{CHN}^q = \{D \mid \exists x_0, x_1, \ldots, x_q \in \mathcal{X}: \ D(x_{i-1}) \lhd x_i \ \forall i\}$.

$\lhd$ 表示任意关系.

对任意元素互异的 $\mathbf{x} = (x_1, x_2, \ldots, x_k)$，以及任意 $D: \mathcal{X} \to \mathcal{\bar{Y}}$，定义

\[
    D\vert^\mathbf{x} = \{D[\mathbf{x} \mapsto \mathbf{r}] \mid \mathbf{r} \in \mathcal{\bar{Y}}^k \} \subset \mathfrak{D},
\]

其是所有除 $\mathbf{x}$ 外其余位置的值与 $D$ 相同的函数的集合. 对于任意数据库性质 $\mathsf{P} \subset \mathfrak{D}$，定义

\[
    \mathsf{P}\vert_{D\vert^\mathbf{x}} = \mathsf{P} \cap D\vert^\mathbf{x}
\]

为 $\mathsf{P}$ 在 $D\vert^\mathbf{x}$ 上的限制.

对于固定的 $\mathbf{x}$ 和 $D$，因为存在 $\mathbf{r} \mapsto D[\mathbf{x} \mapsto \mathbf{r}]$ 的映射，所以可以将 $\mathcal{\bar{Y}}^k$ 和 $D\vert^\mathbf{x}$ 等同，此时性质 $\mathsf{P}\vert_{D\vert^\mathbf{x}}$ 可以视为 $\mathcal{\bar{Y}}^k$ 上的性质，即 $\{\mathbf{r} \in \mathcal{\bar{Y}}^k \mid D[\mathbf{x} \mapsto \mathbf{r}] \in \mathsf{P}\}$. 

因此，也不再区分以下两个投影算子，统一记作 $\mathsf{P}\vert_{D\vert^\mathbf{x}}$：

\begin{gather*}
    \sum_{D' \in \mathsf{P}\vert_{D\vert^\mathbf{x}}} \ket{D'}\bra{D'} \in \mathcal{L}(\mathbb{C}[D\vert^\mathbf{x}]) \subset \mathcal{L}(\mathbb{C}[\mathfrak{D}]) \\
    \sum_{\mathbf{r} \in \mathcal{\bar{Y}}^k \text{ and } D[\mathbf{x} \mapsto \mathbf{r}] \in \mathsf{P}} \ket{\mathbf{r}}\bra{\mathbf{r}} \in \mathcal{L}(\mathbb{C}[\mathcal{\bar{Y}}^k])
\end{gather*}

!!! note "Definition"
    （量子传输能力） 设 $\mathsf{P}, \mathsf{P}'$ 是两个数据库性质，那么定义（阶为 $k$ 的）量子传输能力：

    \[
         \dbrack{\mathsf{P} \xrightarrow{k} \mathsf{P}'} = \max_{\mathbf{x}, \mathbf{\hat{y}}, D} \lVert \mathsf{P}'\vert_{D\vert^\mathbf{x}} \ \mathsf{cO}_{\mathbf{x} \mathbf{\hat{y}}} \ \mathsf{P}\vert_{D\vert^\mathbf{x}} \rVert.
    \]

    而 $q$ 步的量子转移能力则定义为

    \[
        \dbrack{\mathsf{P} \xRightarrow{k, q} \mathsf{P}'} = \sup_{U_1, \ldots, U_{q-1}} \lVert \mathsf{P}' \mathsf{cO}^k U_{q-1} \mathsf{cO}^k \cdots U_1 \mathsf{cO}^k \mathsf{P} \rVert.
    \]

    其中 $U_i$ 均作用于 $\mathbb{C}[\mathcal{X}] \otimes \mathbb{C}[\mathcal{Y}] \otimes \mathbb{C}^d$，$d$ 是任意的正整数.

!!! success "Lemma"
    对任意性质序列 $\mathsf{P}_0, \mathsf{P}_1, \ldots, \mathsf{P}_q$，有

    \[
        \dbrack{\neg \mathsf{P}_0 \xRightarrow{k, q} \mathsf{P}_q} \leq \sum_{s=1}^q \dbrack{\neg \mathsf{P}_{s-1} \xrightarrow{k} \mathsf{P}_s}.
    \]

    ???+ success "Proof"
        