# Mind the Bad Norms: Revisiting Compressed Oracle-based Quantum Indistinguishability Proofs

## Quantum Computing

### General Notation

$\mathcal{U}(\mathcal{H})$ 表示 $\mathcal{H}$ 上的酉算子集合. $\op{Tr}(\mathbf{L})$ 表示线性算子 $\mathbf{L}$ 的迹. $\op{Tr}_{\mathcal{H}_1}(\mathbf{L})$ 表示张量积 $\mathcal{H}_1 \otimes \mathcal{H}_2$ 上的线性算子 $\mathbf{L}$ 在 $\mathcal{H}_1$ 上的偏迹. $\op{D}(\mathcal{H})$ 表示 $\mathcal{H}$ 上的密度算子集合. $\lVert \mathbf{L} \rVert_1$ 表示 $\mathbf{L}$ 的迹范数. 

### Quantum (Non-Adaptive) Oracle-Algorithms

定义输入和输出空间分别为 $\mathcal{H}_{in} := \mathbb{C}^{2^m}$，$\mathcal{H}_{out} := \mathbb{C}^{2^n}$，工作空间 $\mathcal{H}_{work}$ 和状态空间 $\mathcal{H}_{state}$ 为有限维复 Hilbert 空间. 

谕示机状态空间可以被进一步划分为 $\mathcal{H}_{db} \otimes \mathcal{H}_{aux}$，其中 $\mathcal{H}_{db}$ 是数据库空间，$\mathcal{H}_{aux}$ 是辅助空间.

用 $\mathcal{A}^{\mathbf{O}_f}[\rho_\mathcal{A} \otimes \rho_{\mathbf{O}_f}] = b$ 表示由谕示机辅助的算法 $\mathcal{A}$ 在向 $\mathbf{O}_f$ 发起 $q$ 次查询后输出 $b$ 的事件. 其中 $\mathcal{A}$ 和 $\mathbf{O}_f$ 的初始状态分别为 $\rho_\mathcal{A}$ 和 $\rho_{\mathbf{O}_f}$，或者联合初始化为 $\rho_{\mathcal{A}, \mathbf{O}_f}^0 = \rho_\mathcal{A} \otimes \rho_{\mathbf{O}_f}$.

**描述非自适应性**：对于任何向 $\mathbf{O}_f$ 进行 $q$ 次非自适应查询的谕示机算法 $\mathcal{A}$，定义非自适应交互博弈 $\mathcal{A}^{\mathbf{O}_f^{\otimes q}}$ 为空间 $\mathcal{H}_{in}^{\otimes q} \otimes \mathcal{H}_{out}^{\otimes q} \otimes \mathcal{H}_{work} \otimes \mathcal{H}_{state}$ 上的酉算子 $U_1 \mathbf{O}_f^{\otimes q} U_0$，$\mathbf{O}_f^{\otimes q}$ 作用在 $\mathcal{H}_{in}^{\otimes q} \otimes \mathcal{H}_{out}^{\otimes q} \otimes \mathcal{H}_{state}$ 上，$U_0, U_1$ 作用在 $\mathcal{H}_{in}^{\otimes q} \otimes \mathcal{H}_{out}^{\otimes q} \otimes \mathcal{H}_{work}$ 上.

上述数学形式与经典设定类似，在经典设定中，非自适应算法一次性发出所有 $q$ 个查询 $\mathbf{x} = (\mathbf{x}_1, \ldots, \mathbf{x}_q) \in (\{0, 1\}^m)^q$，并同时从谕示机接收所有 $q$ 个响应 $\mathbf{y} = (\mathbf{y}_1, \ldots, \mathbf{y}_q) \in (\{0, 1\}^n)^q$. 对应地，在量子设定中，有

\[
    \mathbf{O}_f^{\otimes q} \ket{\mathbf{x}, \mathbf{y}, s} = \ket{\mathbf{x}, \mathbf{y} \oplus f(\mathbf{x}), s'},
\]

其中 $f(\mathbf{x}) = (f(\mathbf{x}_1), \ldots, f(\mathbf{x}_q))$ 表示 $f$ 在 $\mathbf{x}$ 上的逐点应用.

### Quantum Distinguishing Games

对于任意两个量子谕示机 $\mathbf{I}$ 和 $\mathbf{R}$，定义量子区分器 $\mathcal{A}$ 的区分优势为：

\[
    \mathbf{Adv}_{\mathbf{I}; \mathbf{R}}^\mathsf{dist}(\mathcal{A}) := \left\lvert \Pr{\mathcal{A}^{\mathbf{I}}(\rho_{\mathcal{A}, \mathbf{I}}^0) = 1} - \Pr{\mathcal{A}^{\mathbf{R}}(\rho_{\mathcal{A}, \mathbf{R}}^0) = 1} \right\rvert.
\]

对于计算能力无限的区分器 $\mathcal{A}$，其区分优势满足

\[
    \mathbf{Adv}_{\mathbf{I}; \mathbf{R}}^\mathsf{dist}(\mathcal{A}) \leq \frac{1}{2} \lVert \op{Tr}_{\mathcal{H}_{\mathbf{I}_{db}} (\rho_{\mathcal{A}, \mathbf{I}}^q}) - \op{Tr}_{\mathcal{H}_{\mathbf{R}_{db}}} (\rho_{\mathcal{A}, \mathbf{R}}^q) \rVert_1.
\]

其中 $\rho_{\mathcal{A}, \mathbf{O}^q} := \mathcal{A}^{\mathbf{O}} \rho_{\mathcal{A}, \mathbf{O}}^0 {\mathcal{A}^{\mathbf{O}}}^\dagger$ 是向当前谕示机 $\mathbf{O} \in \{\mathbf{I}, \mathbf{R}\}$ 发起 $q$ 次查询后的系统状态. 不失一般性的前提下，可以假设 $\mathcal{A}$ 是确定性的，因此存在某个固定的态 $\ket{\psi} \in \mathcal{H}_\mathcal{A}$，使得 $\rho_\mathcal{A} = \ket{\psi}\bra{\psi}$.

令 $\mathrm{F} = \{F_K: \{0, 1\}^m \to \{0, 1\}^n\}_{K \in \mathcal{K}}$ 为一个函数族，定义区分器 $\mathcal{A}$ 针对 $\mathrm{F}$ 的 $\mathrm{IND}$-$\\mathrm{qCPA}$ 区分优势为：

\[
    \mathbf{Adv}_{\mathrm{F}}^\mathsf{qcpa} := \mathbf{Adv}_{\mathbf{O}_{F_K}; \mathbf{O}_f}^\mathsf{dist}(\mathcal{A}).
\]

$K$ 在 $\mathcal{K}$ 上均匀分布，$f: \{0, 1\}^m \to \{0, 1\}^n$ 是一个均匀随机函数.

对于非自适应的区分器 $\mathcal{A}$，其非自适应 $\mathrm{IND}$-$\mathrm{qCPA}$ 区分优势为：

\[
    \mathbf{Adv}_{\mathrm{F}}^\mathsf{qncpa} := \mathbf{Adv}_{\mathbf{O}_{F_K}^{\otimes q}; \mathbf{O}_f^{\otimes q}}^\mathsf{dist}(\mathcal{A}).
\]

## Zhandry's Compressed Oracle

### The Chung-Fehr-Huang-Liao Interpretation

令 $\mathcal{Y}$ 表示 $\{0, 1\}^n$，$\mathsf{C}_\mathcal{Y}$ 表示 $n$-量子比特空间 $\mathbb{C}^{2^n}$ 上的计算基. 令 $\hat{\mathcal{Y}}$ 表示 $\mathcal{Y}$ 的对偶群，由所有群同态 $\hat{y}(z) = (-1)^{y \cdot z}$ 组成. $\hat{\mathcal{Y}}$ 同构于 $\mathcal{Y}$，将其视作加法群，群运算定义为 $\hat{y} + \hat{z} := \widehat{y \oplus z}$，其中 $\oplus$ 表示按位异或. $\hat{0}$ 表示单位元. 对于每个 $\hat{y} \in \hat{\mathcal{Y}}$，定义其 Fourier 态为

\[
    \ket{\hat{y}} := \frac{1}{2^{n/2}} \sum_{z \in \mathcal{Y}} \hat{y}(z) \ket{z} = \frac{1}{2^{n/2}} \sum_{z \in \mathcal{Y}} (-1)^{y \cdot z} \ket{z}.
\]

集合 $\mathsf{F}_\mathcal{Y} := \{\ket{\hat{y}}: \hat{y} \in \hat{\mathcal{Y}}\}$ 构成 $\mathbb{C}^{2^n}$ 上的 Fourier 基. 映射 $\ket{y} \mapsto \ket{\hat{y}}$ 就是 Hadamard 变换. 从 $\mathsf{F}_\mathcal{Y}$ 到 $\mathsf{C}_\mathcal{Y}$ 的逆变换为

\[
    \ket{y} := \frac{1}{2^{n/2}} \sum_{\hat{z} \in \hat{\mathcal{Y}}} \hat{z}(y) \ket{\hat{z}} = \frac{1}{2^{n/2}} \sum_{\hat{z} \in \hat{\mathcal{Y}}} (-1)^{z \cdot y} \ket{\hat{z}}.
\]

令 $\mathcal{Z}$ 表示 $\mathcal{Y} \cup \{\perp\}$；类似地，令 $\hat{\mathcal{Z}}$ 表示 $\hat{\mathcal{Y}} \cup \{\perp\}$，其中 $\perp$ 表示未定义，$\ket{\perp}$ 正交于已知的 $\mathbb{C}^{2^n}$ 空间. 因而，$\mathsf{C}_\mathcal{Z} := \{\ket{z}: z \in \mathcal{Z}\}$ 构成 $\mathbb{C}^{2^n + 1}$ 上的计算基，$\mathsf{F}_\mathcal{Z} := \{\ket{\hat{z}}: \hat{z} \in \hat{\mathcal{Z}}\}$ 构成 $\mathbb{C}^{2^n + 1}$ 上的 Fourier 基.

令 $\mathcal{X}$ 表示 $\{0, 1\}^m$，$\mathcal{F}$ 表示所有从 $\mathcal{X}$ 到 $\mathcal{Y}$ 的函数的集合. $f \in \mathcal{F}$ 的量子真值表定义为

\[
    \ket{f} := \bigotimes_{x \in \mathcal{X} } \ket{x} \ket{f(x)}.
\]

**函数和数据库**：$\hat{\mathcal{F}}$ 表示所有 Fourier 函数 $\mathcal{X} \to \hat{\mathcal{Y}}$ 的集合. $\hat{f} \in \hat{\mathcal{F}}$ 的量子真值表可以类似的定义

\[
    \ket{\hat{f}} := \bigotimes_{x \in \mathcal{X} } \ket{x} \ket{\hat{f}(x)}.
\]

对于任意子集 $\mathcal{S} \subseteq \mathcal{X}$，函数 $f: \mathcal{S} \to \mathcal{Y}$ 被称作 $\mathcal{X} \to \mathcal{Y}$ 的部分函数. 部分函数 $f$ 可以通过定义 $d_f(y) = \perp, y \in \mathcal{X} \setminus \mathcal{S}$ 来扩展为 $d_f: \mathcal{X} \to \mathcal{Z}$. 称 $d_f$ 为代表 $f$ 的数据库，其中 $\perp$ 表示 $f$ 未定义的位置；当 $f$ 是全函数时，$d_f$ 与 $f$ 重合. 数据库同样可以表为量子真值表

\[
    \ket{d_f} := \bigotimes_{x \in \mathcal{X} } \ket{x} \ket{d_f(x)}.
\]

类似地，定义部分 Fourier 函数 $\hat{f}: \mathcal{S} \to \hat{\mathcal{Y}}$，代表部分 Fourier 函数的数据库为 $d_{\hat{f}}: \mathcal{X} \to \hat{\mathcal{Z}}$，及其对应的量子真值表 $\ket{d_{\hat{f}}}$.

当 $f$ 或 $\hat{f}$ 可以从上下文清楚推断时，可以省略数据库的下标. 用 $\mathcal{D}$ 表示所有数据库 $d: \mathcal{X} \to \mathcal{Z}$ 的集合，$\hat{\mathcal{D}}$ 表示所有 Fourier 数据库 $\hat{d}: \mathcal{X} \to \hat{\mathcal{Z}}$ 的集合. 方便时也会将 $d$ 视为 $\mathcal{X} \times \mathcal{Y}$ 上的关系，$(x, y) \in d$ 表示 $d(x) = y$；此时 $\lvert d \rvert = \{x \in \mathcal{X} \mid d(x) \in \mathcal{Y}$.

对于 $f \in \mathcal{F}$，定义 $\hat{f} \in \hat{\mathcal{F}}$ 为映射 $x \mapsto \widehat{f(x)}$，那么有

\[
    \ket{\hat{f}} = \frac{1}{2^{n 2^{m/2}}} \sum_{g \in \mathcal{F}} (-1)^{f \cdot g} \ket{g},
\]

其中 $f \cdot g := \sum_{x \in \mathcal{X}} f(x) \cdot g(x)$ 表示 $f$ 和 $g$ 的点积. 因而 $\{\ket{f} \mid f \in \mathcal{F}\}$ 和 $\{\ket{\hat{f}} \mid \hat{f} \in \hat{\mathcal{F}}\}$ 都张成了同一个空间，其同构于 $\mathbb{C}^{2^{n 2^m}}$. 类似地，可以证明 $\{\ket{d} \mid d \in \mathcal{D}\}$ 和 $\{\ket{\hat{d}} \mid \hat{d} \in \hat{\mathcal{D}}\}$ 都张成了同一个空间，其同构于 $\mathbb{C}^{(2^n + 1)^{2^m}}$，该空间称为数据库空间 $\mathbb{D}$. 

用 $\mathbf{0}$ 表示常 $0$ 函数 $0^n$，并且注意到 $\mathbf{0} \cdot g = 0$ 对任意 $g \in \mathcal{F}$ 成立，因此有

\[
    \ket{\hat{\mathbf{0}}} = \frac{1}{2^{n 2^{m/2}}} \sum_{g \in \mathcal{F}} \ket{g},
\]

其就是所有 $\mathcal{F}$ 上的函数的均匀叠加态. 

**标准谕示机**：标准谕示机是带有状态的谕示机，数据库空间为 $\mathcal{H}_{db} := \mathbb{C}[\mathcal{F}]$. 给定函数 $f \in \mathcal{F}$ 的真值表表示 $\ket{f}$，标准谕示机 $\mathbf{stO}$ 作用于敌手寄存器 $\ket{x}\ket{y}$ 和函数真值表寄存器 $\ket{f}$ 的方式为

\[
    \mathbf{stO} \ket{x}\ket{y} \otimes \ket{f} = \ket{x}\ket{y \oplus f(x)} \otimes \ket{f}.
\]

当真值表寄存器初始化为 $\ket{\hat{\mathbf{0}}}$ 时，标准谕示机与均匀随机函数是完美不可区分的.

如果将敌手的响应寄存器和真值表寄存器置于 Fourier 基下，那么有

\[
    \mathbf{stO} \ket{x}\ket{\hat{y}} \otimes \ket{\hat{f}} = \ket{x}\ket{\hat{y}} \otimes \ket{\hat{f} + \hat{\delta}_{xy}},
\]

其中 $\delta_{xy}$ 表示 Kronecker delta 函数的变体，定义为 $\delta_{xy}(z) = y$ 当 $z = x$ 时成立，否则为 $0$. $\mathcal{F}$ 中的 $\oplus$ 运算和 $\hat{\mathcal{F}}$ 中的 $+$ 运算都是逐点定义的. 

在真值表寄存器上定义算子 $\mathbf{O}_{x \hat{y}}$，其作用为 $\mathbf{O}_{x \hat{y}} \ket{\hat{f}} = \ket{\hat{f} + \hat{\delta}_{xy}}$，那么有

\[
    \mathbf{stO} \ket{x}\ket{\hat{y}} \otimes \ket{\hat{f}} = \ket{x}\ket{\hat{y}} \otimes \mathbf{O}_{x \hat{y}} \ket{\hat{f}}.
\]

**压缩谕示机**：对于任意 $x \in \mathcal{X}$，$\mathbb{C}^{2^n + 1}$ 上单元压缩酉算子 $\mathbf{Comp}_x$ 在 $\mathsf{F}_\mathcal{Z}$ 上的定义为

\[
    \mathbf{Comp}_x := \ket{\perp}\bra{\hat{0}} + \ket{\hat{0}}\bra{\perp} + \sum_{\hat{y} \in \hat{\mathcal{Y}} \setminus \{\hat{0}\}} \ket{\hat{y}}\bra{\hat{y}}.
\]

数据库空间 $\mathbb{D}$ 上的数据库压缩酉算子 $\mathbf{Comp}$ 定义为

\[
    \mathbf{Comp} := \bigotimes_{x \in \mathcal{X}} \mathbf{Comp}_x.
\]

压缩谕示机 $\mathbf{cO}$ 是带有状态的谕示机，数据库空间为 $\mathcal{H}_{db} = \mathbb{D}$，其作用在敌手寄存器 $\ket{x}\ket{y}$ 和谕示机数据库寄存器 $\ket{d}$ 上的方式为

\[
    \mathbf{cO} := (\mathbf{I}_{\mathbb{C}[\mathcal{X}] \otimes \mathbb{C}[\hat{\mathcal{Y} }]} \otimes \mathbf{Comp}) \circ \mathbf{stO} \circ (\mathbf{I}_{\mathbb{C}[\mathcal{X}] \otimes \mathbb{C}[\hat{\mathcal{Y} }]} \otimes \mathbf{Comp}),
\]

对于 Fourier 数据库状态 $\ket{\hat{d}}$，有

\[
    \mathbf{cO} \ket{x}\ket{\hat{y}} \otimes \ket{\hat{d}} = \ket{x}\ket{\hat{y}} \otimes \mathbf{cO}_{x \hat{y}} \ket{\hat{d}},
\]

其中 $\mathbf{cO}_{x \hat{y}} := \mathbf{Comp} \circ \mathbf{O}_{x \hat{y}} \circ \mathbf{Comp}$.

### The Two-Domain Distance Technique

**限制定义域数据库**：对于子集 $\tilde{\mathcal{X}} \subseteq \mathcal{X}$，用 $\mathcal{D}\vert_{\tilde{\mathcal{X}}}$ 表示限制在 $\tilde{\mathcal{X}}$ 上的数据库集合，等价于 $\{d \vert_{\tilde{\mathcal{X}}} \mid d \in \mathcal{D}\}$，或者所有函数 $d: \tilde{\mathcal{X}} \to \mathcal{Z}$ 的集合. 因为 $\mathcal{D}$ 是 $\mathbb{D}$ 的一组基，所以限制定义域数据库空间会张成 $\mathbb{D}$ 的一个子空间，其同构于 $\mathbb{C}^{(2^n + 1)^{\lvert \tilde{\mathcal{X}} \rvert}}$. 

**转移容量**：对于任意限制定义域数据库集合 $\mathcal{D}\vert_{\tilde{\mathcal{X}}}$，其子集 $\mathcal{P} \subseteq \mathcal{D}\vert_{\tilde{\mathcal{X}}}$ 被称作 $\mathcal{D}\vert_{\tilde{\mathcal{X}}}$ 上的一个**数据库属性**，定义对应的投影算子为

\[
    \Pi_\mathcal{P} := \sum_{d \in \mathcal{P}} \ket{d}\bra{d}.
\]

对于数据库 $d \in \mathcal{D}\vert_{\tilde{\mathcal{X}}}$ 和 $x \in \tilde{\mathcal{X}}$，定义

\[
    d \vert^x := \{d' \in \mathcal{D}\vert_{\tilde{\mathcal{X}}} \mid d'(x') = d(x') \forall x' \in \tilde{\mathcal{X}} \setminus \{x\}\},
\]

即 $d \vert^x$ 是所有只与 $d$ 在 $x$ 上的值可能不同的数据库的集合. 

对于属性 $P$ 和 $P'$，定义转移容量为

\[
    \dbrack{\mathcal{P} \hookrightarrow \mathcal{P}'} := \max_{x \in \tilde{\mathcal{X}}, \hat{y} \in \hat{\mathcal{Y}}, d \in \mathcal{D} \vert_{\tilde{\mathcal{X}}}} \lVert \Pi_{\mathcal{P}' \cap d \vert^x} \circ \mathbf{cO}_{x \hat{y}} \circ \Pi_{\mathcal{P} \cap d \vert^x} \rVert.
\]

转移容量 $\dbrack{\mathcal{P} \hookrightarrow \mathcal{P}'}$ 大致上衡量了在对压缩谕示机 $\mathbf{cO}$ 发起单次查询后，处于属性 $\mathcal{P}$ 的数据库状态转移到属性 $\mathcal{P}'$ 的概率上界.

对于属性 $\mathcal{P}$，令 $\mathcal{P}^c := \mathcal{D}\vert_{\tilde{\mathcal{X}}} \setminus \mathcal{P}$ 表示 $\mathcal{P}$ 的补集. 有以下衡量转移容量上界的引理：

!!! success "Lemma"
    令 $\mathcal{P}$ 和 $\mathcal{P}'$ 为 $\mathcal{D}\vert_{\tilde{\mathcal{X}}}$ 上的两个属性. 如果对于每个 $x \in \tilde{\mathcal{X}}$ 和 $d \in \mathcal{D}\vert_{\tilde{\mathcal{X}}}$，都能找到一个集合 $S_{x, d}^{\mathcal{P}^c \hookrightarrow \mathcal{P}'} \subseteq \mathcal{Y}$，使得

    \[
        \mathcal{P}' \cap d \vert^x \subseteq \{d' \in d \vert^x \mid d'(x) \in S_{x, d}^{\mathcal{P}^c \hookrightarrow \mathcal{P}'}\} \subseteq \mathcal{P} \cap d \vert^x,
    \]

    换言之，对任何数据库 $d' \in d \vert^x$，

    \[
        d' \in \mathcal{P}' \implies d'(x) \in S_{x, d}^{\mathcal{P}^c \hookrightarrow \mathcal{P}'} \implies d' \in \mathcal{P}.
    \]

    那么有

    \[
        \dbrack{\mathcal{P}^c \hookrightarrow \mathcal{P}'} \leq \max_{x \in \tilde{\mathcal{X}}, d \in \mathcal{D}\vert_{\tilde{\mathcal{X}}}} \sqrt{\frac{10 \lvert S_{x, d}^{\mathcal{P}^c \hookrightarrow \mathcal{P}'} \rvert}{2^n}}.
    \]

**规模受限属性**：对于限制定义域数据库集合 $\mathcal{D}\vert_{\tilde{\mathcal{X}}}$，属性 $\mathcal{P} \subseteq \mathcal{D}\vert_{\tilde{\mathcal{X}}}$ 以及某个 $i \leq \lvert \tilde{\mathcal{X}} \rvert$，定义

\[
    \mathcal{P}_{[\leq i]} := \{d \in \mathcal{P} \mid \lvert d \rvert \leq i\},
\]

此时，转移容量 $\dbrack{\mathcal{P}^c_{[\leq i - 1]} \hookrightarrow \mathcal{P}_{[\leq i]}}$ 衡量了一个在属性 $\mathcal{P}$ 之外，且最多包含 $i - 1$ 个记录的数据库，在单次应用 $\mathbf{cO}_{x \hat{y}}$ 后转移到属性 $\mathcal{P}$ 内且大小不超过 $i$ 的数据库的概率上界. 

令 $\perp := \{d_\perp\}$ 表示空数据库属性，那么对于不包含 $d_\perp$ 的属性 $\mathcal{P}$，有 $\perp = P^c_{[\leq 0]}$，定义

\[
    (\perp \overset{q}{\leadsto} \mathcal{P}) := \sum_{i = 1}^q \dbrack{\mathcal{P}^c_{[\leq i - 1]} \hookrightarrow \mathcal{P}_{[\leq i]}}.
\]

$(\perp \overset{q}{\leadsto} \mathcal{P})$ 衡量了连续进行 $q$ 次查询的过程中，空数据库在任意时刻转移到属性 $\mathcal{P}$ 内数据库的概率上界.

**前缀谕示机**：固定某个 $\bar{t} < m$，并将输入空间写为 $\mathcal{X} = \mathcal{T} \times \mathcal{I}$，其中 $\mathcal{T} := \{0, 1\}^\bar{t}$，$\mathcal{I} := \{0, 1\}^{m - \bar{t}}$. 对任意非零的 $t \leq 2^{\bar{t}}$，任意函数族 $\mathbf{p} = (\mathbf{p}_k: \mathcal{I} \to \mathcal{X})_{k \in [t]}$ 如果满足对于每个 $k \in [t]$，以及所有 $x \in \mathcal{I}$，$\mathbf{p}_k(x) \in \{\delta_\bar{t} (k) \Vert x: x \in \mathcal{I}\}$，其中 $\delta_\bar{t}: [t] \to \mathcal{T}$ 是某个固定的单射函数，则称其为一个 $(\bar{t}, m)$-域分离器. 令 $\mathbf{p}_k(\mathcal{I}) := \{\mathbf{p}_k(x): x \in \mathcal{I}\}$，以及 $\mathbf{p}(\mathcal{I}) := \bigcup_{k \in [t]} \mathbf{p}_k(\mathcal{I})$.

对于任何 $(\bar{t}, m)$-域分离器 $\mathbf{p} = (\mathbf{p}_k)_{k \in [t]}$，将其与一个前缀压缩谕示机 $\mathbf{cO}^{\mathbf{p}}$ 相关联，定义为谕示机族 $\{\mathbf{cO}^{\mathbf{p}_k}\}_{k \in [t]}$，其中 $\mathbf{cO}^{\mathbf{p}_k}$ 表示将 $\mathbf{cO}$ 限制在 $\mathbf{p}_k(\mathcal{I}) \subseteq \mathcal{X}$ 的输入上. 对于任何 $k \in [t]$，$x \in \mathcal{I}$，$\hat{y} \in \hat{\mathcal{Y}}$，以及 $\hat{d} \in \hat{\mathcal{D}}$，有

\[
    \mathbf{cO}^{\mathbf{p}_k} \ket{x}\ket{\hat{y}} \otimes \ket{\hat{d}} = \ket{x}\ket{\hat{y}} \otimes \mathbf{cO}^{\mathbf{p}_k}_{x \hat{y}} \ket{\hat{d}},
\]

其中 $\mathbf{cO}^{\mathbf{p}_k}_{x \hat{y}} := \mathbf{Comp}_{\mathbf{p}_k(x)} \circ \mathbf{O}_{\mathbf{p}_k(x) \hat{y}} \circ \mathbf{Comp}_{\mathbf{p}_k(x)}$. 因此 $\mathbf{cO}^{\mathbf{p}}$ 也可以视作将 $\mathbf{cO}$ 限制在来自 $\mathbf{p}(\mathcal{I})$ 的输入上.

**双域系统**：令 $\mathbf{I}$ 和 $\mathbf{R}$ 为两个带有状态的谕示机，其输入空间 $\mathcal{H}_{in} = \mathbb{C}[\mathcal{I}]$，输出空间 $\mathcal{H}_{out} = \mathbb{C}[\mathcal{Z}]$，数据库空间 $\mathcal{H}_{db} = \mathbb{D}$，由以下序列定义

\begin{gather*}
    \mathbf{I} := \mathbf{F}_t \mathbf{cO}^{\mathbf{I}_t} \cdots \mathbf{cO}^{\mathbf{I}_1} \mathbf{F}_0, \\
    \mathbf{R} := \mathbf{F}_t \mathbf{cO}^{\mathbf{R}_t} \cdots \mathbf{cO}^{\mathbf{R}_1} \mathbf{F}_0,
\end{gather*}

此处稍微滥用记号，使用 $\mathbf{I}$ 和 $\mathbf{R}$ 来表示对应的 $(\bar{t}, m)$-域分离器. 酉算子 $\mathbf{F}_0, \ldots, \mathbf{F}_t$ 只作用在输入、输出和辅助量子比特上.

考虑 $q$ 次查询的交互博弈，计算能力无上界的确定性区分器 $\mathcal{A}$ 需要区分 $\mathbf{I}$ 和 $\mathbf{R}$. 在与 $\mathbf{I}$ 或 $\mathbf{R}$ 交互的过程中，压缩谕示机 $\mathbf{cO}$ 总共被调用了 $q' = tq$ 次. 固定两个定义域 $\tilde{\mathcal{X}}_\mathbf{I} := \mathbf{I}(\mathcal{I})$ 和 $\tilde{\mathcal{X}}_\mathbf{R} := \mathbf{R}(\mathcal{I})$，并定义 $\mathcal{D}_\mathbf{I} := \mathcal{D}\vert_{\tilde{\mathcal{X}}_\mathbf{I}}$ 和 $\mathcal{D}_\mathbf{R} := \mathcal{D}\vert_{\tilde{\mathcal{X}}_\mathbf{R}}$. 考虑属性 $\mathcal{B}_\mathbf{I} \subseteq \mathcal{D}_\mathbf{I} \setminus \perp$ 和 $\mathcal{B}_\mathbf{R} \subseteq \mathcal{D}_\mathbf{R} \setminus \perp$，并定义 $\mathcal{G}_\mathbf{I} := \mathcal{D}_\mathbf{I} \setminus \mathcal{B}_\mathbf{I}$ 和 $\mathcal{G}_\mathbf{R} := \mathcal{D}_\mathbf{R} \setminus \mathcal{B}_\mathbf{R}$. 核心引理如下：

!!! success "Lemma(Two-Domain Distance Lemma)"
    假设可以找到满足如下条件的映射 $h: \mathcal{G}_\mathbf{I} \to \mathcal{G}_\mathbf{R}$：

    - $h$ 是 $\mathcal{G}_\mathbf{I}$ 到 $\mathcal{G}_\mathbf{R}$ 的双射；

    - 对于所有的 $i \in [q'] \cup \{0\}$，$h \vert_{\mathcal{G}_{\mathbf{I} [\leq i]}}$ 是 $\mathcal{G}_{\mathbf{I} [\leq i]}$ 到 $\mathcal{G}_{\mathbf{R} [\leq i]}$ 的双射；

    - 对于所有的 $i \in [q']$，$x \in \mathcal{I}$，$\hat{y} \in \hat{\mathcal{Y}}$，以及 $d \in \mathcal{G}_{\mathbf{I} [\leq i - 1]}$，有

        \[
            \bra{d'} \mathbf{cO}^{\mathbf{I}_k}_{x \hat{y}} \ket{d} = \bra{h(d')} \mathbf{cO}^{\mathbf{R}_k}_{x \hat{y}} \ket{h(d)}, 
        \]

        其中当 $i \equiv 0 \pmod{t}$ 时，$k = t$，否则 $k = i \pmod{t}$.

    那么有

    \[
        \lVert \op{Tr}_\mathbb{D} (\rho_{\mathcal{A}, \mathbf{I}}^q) - \op{Tr}_\mathbb{D} (\rho_{\mathcal{A}, \mathbf{R}}^q) \rVert_1 \leq 3 (\perp \overset{q'}{\leadsto} \mathcal{B}_\mathbf{I}) + 3 (\perp \overset{q'}{\leadsto} \mathcal{B}_\mathbf{R}).
    \]

    其中 $\rho_{\mathcal{A}, \mathbf{p}}^q := \mathcal{A}^{\mathbf{p}} \ket{\psi_\mathcal{A}, d_\perp}\bra{\psi_\mathcal{A}, d_\perp} {\mathcal{A}^{\mathbf{p}}}^\dagger$ 是向当前谕示机 $\mathbf{p} \in \{\mathbf{I}, \mathbf{R}\}$ 发起 $q$ 次查询后，对于某个单位状态 $\ket{\psi_\mathcal{A}}$ 以及空数据库状态 $\ket{d_\perp}$ 的系统状态.

### The Hosoyamada-Iwata Interpretation

Hosoyamada 和 Iwata 提出了一种略有不同的标准谕示机 $\mathbf{stO}$ 变体，目的是借助一个辅助标记位来指示该数据库条目是否已定义. 

令 $\mathcal{S} \subseteq \mathcal{X}$ 且 $\mathcal{Z} = \{0, 1\} \times \mathcal{Y}$，对于任意部分函数 $f: \mathcal{S} \to \mathcal{Y}$，将其与一个数据库函数进行关联 $d_f: \mathcal{X} \to \mathcal{Z}$，定义为

\[
    d_f(x) := \begin{cases}
        (1, f(x)), & f(x) = y \in \mathcal{Y}, \\
        (0, 0^n), & f(x) \text{ 未定义}.
    \end{cases}
\]

数据库空间定义为 $2^{(n + 1)2^m}$ 维的复 Hilbert 空间 $\mathcal{H}_{db} := \mathbb{C}[\mathcal{Z}]$. 但此时并不是所有的 $d \in \mathcal{Z}^{2^m}$ 都可以和某个部分函数 $f$ 相关联. 数据库 $d = ((b_0, \beta_0), \ldots, (b_{2^m - 1}, \beta_{2^m - 1}))$ 被称作**有效的**，如果其满足，对于每个 $i \in \{0, \ldots, 2^m - 1\}$，若 $b_i = 0$，则必有 $\beta_i = 0^n$. 事实上，任何有效数据库 $((b_0, \beta_0), \ldots, (b_{2^m - 1}, \beta_{2^m - 1}))$ 都等同于集合 $\{(i, \beta_i) \mid b_i = 1\}$，这就是从 $\{0, 1\}^m$ 到 $\{0, 1\}^n$ 的部分函数 $f$ 的真值表. 相应地，令 $\Pi_{valid}$ 表示投影到有效数据库的投影算子.

任何数据库状态 $\ket{d} \in \mathbb{C}[\mathcal{Z}]$ 都可以等价地视为 $2^m$ 个单元 $\ket{d[0]} \ldots \ket{d[2^m - 1]}$ 组成的阵列. 将 $\ket{d[i]}$ 写为 $\ket{b_i, \beta_i}$，那么标准谕示机定义为

\[
    \mathbf{stO} \ket{i, y} \ket{d} = \ket{i, y + \beta_i} \ket{d}.
\]

对于满足 $\ket{d[i]} = \ket{0, 0^n}$ 的状态 $\ket{d}$，定义 $\ket{d \cup (1, \beta)}$ 为将第 $i$ 个单元替换为 $\ket{1, \beta}$，其余所有单元均与 $\ket{d}$ 相同的数据库. 在数据库单元上定义如下的酉算子：

\begin{align*}
    \mathbf{IH}_0 & := \mathbf{I}_1 \otimes H^{\otimes n}, \\
    \mathbf{Tg}_0 & := \mathbf{I}_1 \otimes \ket{0^n}\bra{0^n} + \mathbf{X} \otimes (\mathbf{I}_{2^n} - \ket{0^n}\bra{0^n}), \\
    \mathbf{cH}_0 & := \ket{0}\bra{0} \otimes \mathbf{I}_{2^n} + \ket{1}\bra{1} \otimes H^{\otimes n}.
\end{align*}

以及对应的数据库版本：

\[
    \mathbf{IH} := \mathbf{IH}_0^{\otimes 2^m}, \quad
    \mathbf{Tg} := \mathbf{Tg}_0^{\otimes 2^m}, \quad
    \mathbf{cH} := \mathbf{cH}_0^{\otimes 2^m}.
\]

其中 $\mathbf{x}$ 表示 Pauli-X 算子，$\mathbf{I}_k$ 表示 $k$ 维单位算子，$H$ 表示 Hadamard 算子.

利用这些算子，可以在数据库上定义编码算子 $\mathbf{enc}$ 和解码算子 $\mathbf{dec}$：

\begin{align*}
    \mathbf{enc} & := \mathbf{cH} \circ \mathbf{Tg} \circ \mathbf{IH}, \\
    \mathbf{dec} & := \mathbf{enc}^\dagger = \mathbf{IH} \circ \mathbf{Tg} \circ \mathbf{cH}.
\end{align*}

Hosoyamada 和 Iwata 提出的带记录的标准谕示机 $\mathbf{RStOE}$ 定义为

\[
    \mathbf{RStOE} := (\mathbf{I}_{2^{m + n}} \otimes \mathbf{enc}) \mathbf{stO} (\mathbf{I}_{2^{m + n}} \otimes \mathbf{dec}).
\]

执行过程为先对数据库解码，然后将标准谕示机作用与敌手的寄存器和解码后的数据库，最后再对数据库编码. 令 $\ket{\mathbf{0}}$ 表示有效的空数据库. 有如下的命题：

!!! note "Proposition"
    假设谕示机状态初始化为 $\ket{\mathbf{0}}$，对于任意 $i \geq 1$，如果谕示机寄存器在 $i$ 次查询后被测量，那么得到的数据库 $d$ 必然是有效的，且包含最多 $i$ 个记录. 

!!! note "Proposition"
    对于任何满足 $\ket{d[i]} = \ket{0, 0^n}$ 的有效数据库 $d$，有

    \begin{align*}
        \mathbf{RStOE} \ket{i, y} \ket{d \cup (i, \beta)} & = \ket{i, y \oplus \beta} \ket{d \cup (i, \beta)} + \ket{\varepsilon_1}; \\
        \mathbf{RStOE} \ket{i, y} \ket{d} & = \sum_{\beta \in \{0, 1\}^n} \frac{1}{2^{n/2}} \ket{i, y \oplus \beta} \ket{d \cup (i, \beta)} + \ket{\varepsilon_2},
    \end{align*}

    其中 $\ket{\varepsilon_1}$ 和 $\ket{\varepsilon_2}$ 满足 $\lVert \ket{\varepsilon_1} \rVert$，$\lVert \ket{\varepsilon_2} \rVert \in O(1/\sqrt{2^n})$.

直观上，$\ket{\varepsilon_1}$ 和 $\ket{\varepsilon_2}$ 可以被视为由于量子干涉而在量子随机函数惰性采样中引入的误差项.

最后，用于研究不可区分性博弈并给出优势上界的主要成果如下：

!!! note "Proposition"
    对于每个 $j \in \{0, 1, \ldots, q\}$，令 $\ket{\mathbb{R}_j}$ 和 $\ket{\mathbb{I}_j}$ 分别表示在第 $j$ 次查询后对应于真实世界和理想世界的状态. 假设存在状态 $\ket{\mathbb{R}_j^g}$，$\ket{\mathbb{R}_j^b}$，$\ket{\mathbb{I}_j^g}$，$\ket{\mathbb{I}_j^b}$，以及非负实数 $\epsilon_\mathbf{I}^{(j)}$，$\epsilon_\mathbf{R}^{(j)}$，使得

    1. $\ket{\mathbb{R}_j} = \ket{\mathbb{R}_j^g} + \ket{\mathbb{R}_j^b}$，$\ket{\mathbb{I}_j} = \ket{\mathbb{I}_j^g} + \ket{\mathbb{I}_j^b}$；

    2. $\ket{\mathbb{R}_j^g} \bra{\mathbb{R}_j^g} = \ket{\mathbb{I}_j^g} \bra{\mathbb{I}_j^g}$；

    3. $\lVert \ket{\mathbb{I}_j^b} \rVert \leq \lVert \ket{\mathbb{I}_{j - 1}^b} \rVert + \epsilon_\mathbf{I}^{(j)}$，$\lVert \ket{\mathbb{R}_j^b} \rVert \leq \lVert \ket{\mathbb{R}_{j - 1}^b} \rVert + \epsilon_\mathbf{R}^{(j)}$.

    那么对于任何计算能力无上界的确定性区分器 $\mathcal{A}$，有

    \[
        \lVert \op{Tr}_{\mathcal{H}_{\mathbf{I}_{db}}} (\rho_{\mathcal{A}, \mathbf{I}}^q) - \op{Tr}_{\mathcal{H}_{\mathbf{R}_{db}}} (\rho_{\mathcal{A}, \mathbf{R}}^q) \rVert_1 \leq \sum_{j = 1}^q (\epsilon_\mathbf{I}^{(j)} + \sum_{j = 1}^q \epsilon_\mathbf{R}^{(j)}).
    \]

    其中 $\rho_{\mathcal{A}, \mathbf{I}}^q := \ket{\psi_\mathcal{A}}\bra{\psi_\mathcal{A}} \otimes \ket{\mathbf{0}_\mathbf{I}}\bra{\mathbf{0}_\mathbf{I}}$，$\rho_{\mathcal{A}, \mathbf{R}}^q := \ket{\psi_\mathcal{A}}\bra{\psi_\mathcal{A}} \otimes \ket{\mathbf{0}_\mathbf{R}}\bra{\mathbf{0}_\mathbf{R}}$.

## Revisiting $\mathrm{IND}$-$\mathrm{qCPA}$ Security of $\mathsf{LR}_4$

### The Luby-Rackoff Construction

对于 $r \geq 1$ 以及 $f_1, \ldots, f_r: \{0, 1\}^n \to \{0, 1\}^n$，定义 $g:[r] \times \{0, 1\}^{2n} \to \{0, 1\}^{2n}$ 为

\[
    (i, x_1, x_2) \mapsto (x_2 \oplus f_i(x_1), x_1),
\]

并定义 $g_i(\cdot, \cdot) := g(i, \cdot, \cdot)$. $r$ 轮 Luby-Rackoff 构造 $\mathsf{LR}_r$ 定义为

\[
    (x_1, x_2) \mapsto g_r \circ \cdots \circ g_1 (x_1, x_2).
\]

对所有 $i \in [r]$，记：

- $x^{i - 1} := (x_1^{i - 1}, x_2^{i - 1})$ 为 $g_i$ 的输入，其中 $x^0 := x = (x_1, x_2)$ 为 $\mathsf{LR}_r$ 的输入；

- $(u_i, v_i)$ 表示与 $f_i$ 对应的输入-输出元组；

- $y = (y_1, y_2) := (x_1^r, x_2^r)$ 为 $\mathsf{LR}_r$ 的输出.

Hosoyamada 和 Iwata 给出了如下的关于 $\mathsf{LR}_4$ 的 $\mathrm{IND}$-$\mathrm{qCPA}$ 安全界：

!!! note "Theorem"
    设 $f_1, f_2, f_3, f_4: \{0, 1\}^n \to \{0, 1\}^n$ 是四个相互独立的均匀随机函数，那么对于任何 $q \geq 0$ 以及任何最多进行 $q$ 次 $\mathrm{CPA}$ 查询的量子敌手 $\mathcal{A}$，有

    \[
        \mathbf{Adv}_{\mathsf{LR}_4}^{\mathsf{qcpa}}(\mathcal{A}) \leq O\left(\sqrt{\frac{q^3}{2^n}}\right).
    \]

该定理的证明使用了 Zhandry 压缩谕示机的 HI 诠释，即 $\mathbf{RStOE}$. 思路如下：

1. 使用独立的 $\mathbf{RStOE}$ 以及相应的数据库 $d_1, d_2, d_3, d_4$ 分别模拟随机函数 $f_1, f_2, f_3, f_4$.

2. 随后使用一系列混合论证，在真实构建 $\mathsf{LR}_4$ 和理想构建（均匀随机函数 $\mathsf{\Gamma}: \{0, 1\}^{2n} \to \{0, 1\}^{2n}$）之间引入了中间构造. 第一个中间构造是一个长度保持函数，记作 $\widetilde{\mathsf{LR}}_4$, 其定义为

    \[
        (x_1, x_2) \mapsto g_4 \circ G_3 \circ g_2 \circ g_1 (x_1, x_2),
    \]

    其中 $G_3(x_1', x_2') := (F_3(x_1', x_2'), x_1')$，$\forall (x_1', x_2') \in \{0, 1\}^{2n}$. 函数 $F_3: \{0, 1\}^{2n} \to \{0, 1\}^n$ 是一个均匀随机函数，由适当的 $\mathbf{RStOE}$ 以及数据库 $d_\mathbf{I}$ 实现. 此处只关注 $\mathsf{LR}_4$ 和 $\widetilde{\mathsf{LR}}_4$ 之间的距离，证明这个距离是可忽略的是该证明的核心技术难点. 在本文的讨论中只考虑截断输出 $x_1^3$ 就足够了，因此省去了 $f_4$ 的调用. 记数据库三元组为 $d^\mathrm{R} = (d_1, d_2, d_\mathrm{R})$，$d^\mathrm{I} = (d_1, d_2, d_\mathrm{I})$.

3. 运用命题 $3$ 来限制优势上界，今儿迭代应用命题 $2$，按顺序研究 $f_1, f_2, f_3$（仅在真实世界中）和 $F_3$（仅在理想世界中） 的作用，随后依次进行针对 $f_2$ 和 $f_1$ 的撤销计算步骤.

4. 证明的核心思想在于：只要在所有查询中，输入到 $f_3$（理想世界中对应 $F_3$）的值是两两互不相同的，那么 $\mathsf{LR}_4$ 和 $\widetilde{\mathsf{LR}}_4$ 就是不可区分的. 数据库三元组 $d^\mathrm{R} = (d_1, d_2, d_\mathrm{R})$（理想世界中的 $d^\mathrm{I} = (d_1, d_2, d_\mathrm{I})$）被认为是好的，当且仅当不存在互异的数据库条目 $(u_1, v_1), (u_1', v_1') \in d_1$，$(u_2, v_2), (u_2', v_2') \in d_2$，以及 $(u_3, v_3) \in d_\mathrm{R}$（理想世界中对应 $(u_3, x_2^2, v_3) \in d_\mathrm{I}$），使得

    \[
        u_1 \oplus v_2 = u_1' \oplus v_2' = u_3.
    \]

    所有其他的数据库三元组都被认为是坏的. 令 $\Pi_{bad}$ 为坏数据库所张成的空间上的投影算子. 好数据库三元组的一个关键性质是其存在从现实世界数据库到理想世界数据库的一一对应，即 $d^\mathrm{R} \mapsto [d^\mathrm{R}]_\mathrm{I}$. 所以，如果数据库在整个过程中保持为好的，那么容易证明这两个世界的行为是一致的. 通过设置 $\ket{\mathbb{R}_j^b} = \Pi_{bad} \ket{\mathbb{R}_j}$，$\ket{\mathbb{R}_j^g} = \ket{\mathbb{R}_j} - \ket{\mathbb{R}_j^b}$，$\ket{\mathbb{I}_j^b} = \Pi_{bad} \ket{\mathbb{I}_j}$，$\ket{\mathbb{I}_j^g} = \ket{\mathbb{I}_j} - \ket{\mathbb{I}_j^b}$，就能够满足命题 $3$ 的条件 $1$ 和条件 $2$. 剩下的工作就是研究每个函数调用的作用，并假设在调用前状态由好数据库张成，从而限制调用后坏向量的范数.

### Action of $f_1$ and the Trivialization of Norm

对于任意单位态 $\ket{\psi}$ 和任意投影算子 $\Pi$，当 $\lVert \Pi \ket{\psi} \rVert \leq 1$ 时，称 $\lVert \Pi \ket{\psi} \rVert$ 被平凡限制.

以下将针对理想世界中的作用进行研究. 简便起见，假设 $f_1$ 的输出被写入了某个辅助寄存器中，通过对命题 $2$ 的递归应用，存在向量 $\ket{\varepsilon_1}$ 和 $\ket{\varepsilon_2}$，使得：

\begin{align*}
    \mathbf{O}_{f_1} \ket{\mathbb{I}_{j - 1}^g} & = \sum_{\substack{x, y, z, d^\mathrm{I} \\ d^\mathrm{I} : \text{good} \\ d_1(x_1) \neq \perp} } 
\end{align*}