# Fourier analysis in nonabelian groups

## A brief introduction to representation theory

群 $G$ 在向量空间 $\mathbb{C}^n$ 上的一个**表示**是一个群同态 $\sigma: G \to \op{GL}_n(\mathbb{C})$，即将每个群元素 $g \in G$ 映射到一个可逆的 $n \times n$ 复矩阵 $\sigma(g)$，并且满足对 $x, y \in G$ 有 $\sigma(xy) = \sigma(x)\sigma(y)$. 显然 $\sigma(e) = I_n$，且 $\sigma(g^{-1}) = \sigma(g)^{-1}$. 称 $\mathbb{C}^n$ 为表示 $\sigma$ 的**表示空间**，$n$ 为表示的**维数**，记为 $d_\sigma$.

表示空间均为 $\mathbb{C}^n$ 的两个表示 $\sigma, \sigma'$ 称为**同构**的，如果存在一个可逆线性变换 $M \in \mathbb{C}^{n \times n}$，使得对所有 $x \in G$ 有 $M \sigma(x) = \sigma'(x) M$，记为 $\sigma \sim \sigma'$. 显然不同维数的表示不可能同构.此外，可以证明有限群的表示都同构于一个酉表示（参照[Math-RepresentationTheory-GTM42-Chap1](https://note.shad0wash.cc/math/RepresentationTheory/GTM42/Chap1/#subrepresentations)），酉表示满足 $\sigma(x)^{-1} = \sigma(x)^\dagger, \forall x \in G$. 所以只需要关注酉表示即可，这也是量子计算中乐于看见的.

最简单的是那些一维表示，即 $\forall x \in G, \sigma(x) \in \mathbb{C}$ 且 $\lvert \sigma(x) \rvert = 1$. 定义 $\sigma(x) = 1, \forall x \in G$ 的表示称为**平凡表示**.

左正则表示和右正则表示是两个重要的表示，维度均为 $\lvert G \rvert$，表示空间为群代数 $\mathbb{C}G$，即由基向量 $\ket{x}, x \in G$ 张成的 $\lvert G \rvert$ 维复向量空间. 左正则表示 $L$ 定义为 $L(x)\ket{y} = \ket{xy}$，右正则表示 $R$ 定义为 $R(x)\ket{y} = \ket{y x^{-1}}$. 两个正则表示都是置换表示，每个表示矩阵都是置换矩阵.

给定两个表示 $\sigma: G \to V$ 和 $\sigma': G \to V'$，它们的**直和表示** $\sigma \oplus \sigma': G \to V \oplus V'$ 定义为

\[
    (\sigma \oplus \sigma')(x) = \begin{pmatrix}
        \sigma(x) & 0 \\
        0 & \sigma'(x)
    \end{pmatrix},
\]

维数为 $d_{\sigma \oplus \sigma'} = d_\sigma + d_{\sigma'}$.

如果一个表示不能分解为两个其他表示的直和，则称为**不可约表示**. 有限群 $G$ 的任何表示都可以分解为 $G$ 不可约表示的直和.

组合两个表示的另一种方法是张量积. 给定两个表示 $\sigma: G \to V$ 和 $\sigma': G \to V'$，它们的**张量积表示** $\sigma \otimes \sigma': G \to V \otimes V'$ 定义为

\[
    (\sigma \otimes \sigma')(x) = \sigma(x) \otimes \sigma'(x),
\]

且维数为 $d_{\sigma \otimes \sigma'} = d_\sigma \cdot d_{\sigma'}$.

表示 $\sigma$ 的**特征标**为函数 $\chi_\sigma: G \to \mathbb{C}$，定义为 $\chi_\sigma(x) = \op{Tr}(\sigma(x))$. 有如下性质：

- $\chi_\sigma(e) = d_\sigma$.

- $\chi_\sigma(x^{-1}) = \chi_\sigma(x)^*$.

- $\chi_\sigma(y x) = \chi_\sigma(x y)$.

所以 $\chi_\sigma(y x y^{-1}) = \chi_\sigma(x)$，即特征标在共轭类上是常数. 直和和张量积表示的特征标满足 $\chi_{\sigma \oplus \sigma'}(x) = \chi_\sigma(x) + \chi_{\sigma'}(x)$ 和 $\chi_{\sigma \otimes \sigma'}(x) = \chi_\sigma(x) \cdot \chi_{\sigma'}(x)$.

表示论中最重要的结果之一是**Schur's Lemma**，它说明了不可约表示之间的同态结构：

!!! note "Schur's Lemma"
    设 $\sigma$ 和 $\sigma'$ 是群 $G$ 的两个不可约表示，$M \in \mathbb{C}^{d_{\sigma} \times d_{\sigma'}}$ 是一个线性变换，满足对所有 $x \in G$ 有 $M \sigma(x) = \sigma'(x) M$. 那么如果 $\sigma \not\sim \sigma'$，则 $M = 0$；如果 $\sigma \sim \sigma'$，则存在一个标量 $\lambda \in \mathbb{C}$，使得 $M = \lambda I$.

Schur's Lemma 可以证明不可约表示的正交性：

!!! note "Theorem"
    对于 $G$ 的两个不可约表示 $\sigma$ 和 $\sigma'$，有

    \[
        \frac{d_\sigma}{\lvert G \rvert} \sum_{x \in G} \sigma(x)_{i,j}^* \sigma'(x)_{i',j'} = \delta_{\sigma, \sigma'} \delta_{i,i'} \delta_{j,j'},
    \]

    其中 $\delta_{\sigma, \sigma'} = \begin{cases}
        1, & \sigma \sim \sigma' \\
        0, & \sigma \not\sim \sigma'
    \end{cases}$.

这也就导出了不可约表示的特征标的相应正交关系：

!!! note "Theorem"
    对于 $G$ 的两个不可约表示 $\sigma$ 和 $\sigma'$，有

    \[
        (\chi_\sigma, \chi_{\sigma'}) := \frac{1}{\lvert G \rvert} \sum_{x \in G} \chi_\sigma(x)^* \chi_{\sigma'}(x) = \delta_{\sigma, \sigma'}.
    \]

所以 $G$ 的特征标为类函数空间提供了一组正交基. 这可以通过特征标表来表示，表的行对应不可约表示，列对应共轭类，每个元素为该表示在该共轭类上的特征标值. 特征标正交定理表明，在每个元素按共轭类大小归一化的前提下，特征标表的行向量是正交的.

$G$ 的正则表示对于理解表示的不可约分解非常有用，因为正则表示包含了 $G$ 的所有不可约表示，每个不可约表示 $\sigma$ 出现的次数等于其维数 $d_\sigma$. 设 $\hat{G}$ 表示 $G$ 的一个完全的不可约表示系，则有：

\[
    L \cong \bigoplus_{\sigma \in \hat{G}} (\sigma \otimes I_{d_\sigma}), \quad R \cong \bigoplus_{\sigma \in \hat{G}} (I_{d_\sigma} \otimes \sigma^*).
\]

实际上，$L$ 和 $R$ 使用的是相同的同构映射，因为左右正则表示是可交换的；而这个同构映射就是 $G$ 上的 Fourier 变换.

考虑 $\chi_L(e) = \chi_R(e) = \lvert G \rvert$，以及以上的这个分解式，可以得到著名的恒等式：

\[
    \sum_{\sigma \in \hat{G}} d_\sigma^2 = \lvert G \rvert.
\]

而注意到对于任何 $x \in G \setminus \{ e \}$，都有 $\chi_L(x) = \chi_R(x) = 0$，所以可以得到另一个恒等式：

\[
    \sum_{\sigma \in \hat{G}} d_\sigma \chi_\sigma(x) = 0.
\]

一般来说，不可约表示 $\sigma \in \hat{G}$ 在任意表示 $\tau$ 中的重数由 $\mu_\sigma^\tau =  (\chi_\sigma, \chi_\tau)$ 给出. 因此，任意表示 $\tau$ 都可以写成不可约表示的直和：

\[
    \tau \cong \bigoplus_{\sigma \in \hat{G}} (\sigma \otimes I_{\mu_\sigma^\tau}).
\]

这也提供了一个简单不可约性的检验：对于任何表示 $\sigma$，$(\chi_\sigma, \chi_\sigma)$ 都是整数，且当且仅当 $\sigma$ 不可约时取值为 1.

$G$ 上的任何表示也可被视为其任何子群 $H \leq G$ 上的表示，只需限制定义域即可，由此得到的限制表示记为 $\op{Res}_H^G \sigma$. 不过。即使 $\sigma$ 在 $G$ 上不可约，其限制表示 $\op{Res}_H^G \sigma$ 在 $H$ 上也可能是可约的. 

## Fourier analysis for nonabelian groups

Fourier 变换是从群代数 $\mathbb{C}G$ 映射到复向量空间 $\oplus_{\sigma \in \hat{G}} \mathbb{C}^{d_\sigma \times d_\sigma}$ 的线性变换，该复向量空间的基向量对应 $G$ 的所有不可约表示的矩阵元素. 

对应于群元素 $x \in G$ 的基向量 $\ket{x} \in \mathbb{C}G$ 的 Fourier 变换实际上是覆盖所有不可约表示 $\sigma \in \hat{G}$ 的加权叠加：

\[
    \ket{\hat{x}} := \sum_{\sigma \in \hat{G}} \sqrt{\frac{d_\sigma}{\lvert G \rvert}} \ket{\sigma, \sigma(x)},
\]

其中 $\ket{\sigma}$ 是标记不可约表示的量子态，$\ket{\sigma(x)}$ 是一个归一化的 $d_\sigma^2$ 维量子态，其振幅对应矩阵 $\sigma(x)/\sqrt{d_\sigma}$ 的各个元素：

\[
    \ket{\sigma(x)} := \sum_{j, k=1}^{d_\sigma} \frac{\sigma(x)_{j,k}}{\sqrt{d_\sigma}} \ket{j,k}.
\]

!!! tip "Remark"
    如果 $\sigma$ 是一维表示，那么 $\ket{\sigma(x)}$ 只是一个相位因子 $\sigma(x) = \chi_\sigma(x) \in \mathbb{C}$，其中 $\lvert \sigma(x) \rvert = 1$.

所以 $G$ 上的 Fourier 变换为

\begin{align*}
    F_G & := \sum_{x \in G} \ket{\hat{x}}\bra{x} \\
        & = \sum_{x \in G} \sum_{\sigma \in \hat{G}} \sqrt{\frac{d_\sigma}{\left\lvert G \right\rvert}} \sum_{j, k=1}^{d_\sigma} \sigma(x)_{j,k} \ket{\sigma, j, k} \bra{x}.
\end{align*}

需要注意的是，$G$ 上的 Fourier 变换与 $G$ 的不可约表示的选择有关. 接下来验证 $F_G$ 是酉变换，利用恒等式：

\begin{align*}
    \innerproduct{\sigma(y)}{\sigma(x)} & = \op{Tr} \sigma^\dagger(y) \sigma(x) / d_\sigma \\
                                        & = \op{Tr} \sigma(y^{-1} x) / d_\sigma \\
                                        & = \chi_\sigma(y^{-1} x) / d_\sigma. 
\end{align*}

从而

\begin{align*}
    \innerproduct{\hat{y}}{\hat{x}} & = \sum_{\sigma} \frac{d_\sigma^2}{\lvert G \rvert} \innerproduct{\sigma(y)}{\sigma(x)} \\
                                    & = \sum_{\sigma} \frac{d_\sigma}{\lvert G \rvert} \chi_\sigma(y^{-1} x).
\end{align*}

依据不可约表示维数平方和恒等式，便可以得到 $\innerproduct{\hat{y}}{\hat{x}} = \delta_{x,y}$，从而 $F_G$ 是酉变换.

$F_G$ 正是将 $G$ 的左右正则表示分解成其不可约表示的同构映射. 以左正则表示为例来验证，回忆 $L(x)\ket{y} = \ket{xy}$，则有

\begin{align*}
    \hat{L}(x) & := F_G L(x) F_G^\dagger \\
               & = \sum_{y \in G} \ket{\widehat{xy}} \bra{\hat{y}} \\
               & = \sum_{y \in G} \sum_{\sigma, \sigma' \in \hat{G}} \sum_{j, k=1}^{d_\sigma} \sum_{j', k'=1}^{d_{\sigma'}} \frac{\sqrt{d_\sigma d_{\sigma'}}}{\lvert G \rvert} \sigma(xy)_{j,k} \sigma'(y)_{j',k'}^* \ket{\sigma, j, k} \bra{\sigma', j', k'} \\
               & = \sum_{y \in G} \sum_{\sigma, \sigma' \in \hat{G}} \sum_{j, k, l=1}^{d_\sigma} \sum_{j', k'=1}^{d_{\sigma'}} \frac{\sqrt{d_\sigma d_{\sigma'}}}{\lvert G \rvert} \sigma(x)_{j,l} \sigma(y)_{l,k} \sigma'(y)_{j',k'}^* \ket{\sigma, j, k} \bra{\sigma', j', k'} \\
               & = \sum_{\sigma \in \hat{G}} \sum_{j, k, l=1}^{d_\sigma} \sigma(x)_{j,l} \ket{\sigma, j, k} \bra{\sigma, l, k} \\
               & = \bigoplus_{\sigma \in \hat{G}} (\sigma(x) \otimes I_{d_\sigma}),
\end{align*}

其中利用了正交性关系 $\sum_{y \in G} \sigma(y)_{l,k} \sigma'(y)_{j',k'}^* = \frac{\lvert G \rvert}{d_\sigma} \delta_{\sigma, \sigma'} \delta_{l,j'} \delta_{k,k'}$.

对右正则表示 $R(x) \ket{y} = \ket{y x^{-1}}$ 进行类似的验证得到：

\begin{align*}
    \hat{R}(x) & := F_G R(x) F_G^\dagger \\
               & = \bigoplus_{\sigma \in \hat{G}} (I_{d_\sigma} \otimes \sigma^*(x)).
\end{align*}

这个恒等式在分析 $\op{QFT}$ 在隐藏子群问题中的应用时将非常有用.

为了将 Fourier 变换用作量子计算的一部分，我们必须能够通过某种量子电路来高效地实现它. 对于某些特殊的非阿贝尔群这已经被实现了，包括亚循环群（循环群的半直积），如二面体群；对称群；以及许多具有良好性质子群塔的群族. 但有一些著名的群尚未知晓是否存在高效的 $\op{QFT}$ 实现方法，例如在具有 $q$ 个元素的有限域 $\mathbb{F}_q$ 上的一般线性群 $\op{GL}_n(q)$.