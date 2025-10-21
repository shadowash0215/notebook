# Fourier sampling

## Weak Fourier sampling

回忆陪集态

\[
    \ket{gH} := \frac{1}{\sqrt{\lvert H \rvert}} \sum_{h \in H} \ket{g h},
\]

以及隐藏子群态

\[
    \rho_H := \frac{1}{\lvert G \rvert} \sum_{g \in G} \ket{gH}\bra{gH}.
\]

这种状态的对称性可以为 $\op{QFT}$ 所用，具体来说，利用正则表示改写陪集态：

\[
    \ket{gH} = \frac{1}{\sqrt{\lvert H \rvert}} \sum_{h \in H} R(h) \ket{g},
\]

所以隐藏子群态可以写成

\begin{align*}
    \rho_H & = \frac{1}{\lvert G \rvert \cdot \lvert H \rvert} \sum_{g \in G} \sum_{h, h' \in H} R(h) \ket{g} \bra{g} R(h')^\dagger \\
           & = \frac{1}{\lvert G \rvert \cdot \lvert H \rvert} \sum_{h, h' \in H} R(hh'^{-1}) \\
           & = \frac{1}{\lvert G \rvert} \sum_{h \in H} R(h).
\end{align*}

因为右正则表示在 Fourier 基下是分块对角的，所以 $\rho_H$ 在 Fourier 基下也是分块对角的，具体来说：

\begin{align*}
    \hat{\rho}_H & := F_G \rho_H F_G^\dagger \\
                & = \frac{1}{\lvert G \rvert} \bigoplus_{\sigma \in \hat{G}} \left( I_{d_\sigma} \otimes \sigma(H)^* \right),
\end{align*}

其中 $\sigma(H) := \sum_{h \in H} \sigma(h)$.

现在便可以在不损失信息的前提下对 $\rho_H$ 进行测量，这一过程称为**弱 Fourier 采样**（weak Fourier sampling）. 在弱 Fourier 采样中得到 $\sigma \in \hat{G}$ 的概率为

\begin{align*}
    \op{Pr}(\sigma) & = \frac{1}{\lvert G \rvert} \op{Tr} \left( I_{d_\sigma} \otimes \sigma(H)^* \right) \\
                    & = \frac{d_\sigma}{\lvert G \rvert} \sum_{h \in H} \chi_\sigma(h)^* \\
                    & = \frac{d_\sigma \lvert H \rvert}{\lvert G \rvert} (\chi_\sigma, \chi_1)_H,
\end{align*}

也就是 $\frac{d_\sigma \lvert H \rvert}{\lvert G \rvert}$ 乘以平凡表示在 $\op{Res}_H^G \sigma$ 中出现的次数. 现在需要考虑的是从该分布中抽取多项式多个样本是否足以确定隐藏子群 $H$，如果可以，能否利用这些信息高效地重构出 $H$.

## Normal subgroups

如果 $G$ 是阿贝尔群，那么它所有的表示都是一维的，所以弱 Fourier 采样揭示了关于 $\rho_H$ 的全部信息，此前的推导也已表明弱 Fourier 采样足以高效的确定隐藏子群 $H$.

而当 $H \triangleleft G$，即 $\forall g \in G, g H g^{-1} = H$ 时，弱 Fourier 采样由于类似的原因也能成功. 在这种情况下，每一个不可约表示块内的隐藏子群态正比于

\[
    \sigma(H)^* = \frac{1}{\lvert G \rvert} \sum_{g \in G, h \in H} \sigma(g h g^{-1})^*,
\]

其与 $\sigma(g)^*, \forall g \in G$ 交换. 根据 Schur 引理，$\sigma(H)^*$ 必然与单位矩阵成比例，因而 $\hat{\rho}_H$ 在每一个不可约表示块内都是与单位矩阵成比例的，弱 Fourier 采样同样揭示了关于 $\rho_H$ 的全部信息.

此外，当 $H \triangleleft G$ 时，弱 Fourier 采样下的分布是阿贝尔群情况的一个简单推广，有

\[
    \op{Pr}(\sigma) = \begin{cases}
        \frac{d_\sigma^2 \lvert H \rvert}{\lvert G \rvert}, & H \leq \ker \sigma; \\
        0, & \text{otherwise}.
    \end{cases}
\]

$\ker \sigma := \{ g \in G : \sigma(g) = I_{d_\sigma} \}$ 是 $\sigma$ 的核，同样是 $G$ 的正规子群. 首先考虑 $H \not\leq \ker \sigma$ 的情况，此时存在 $h' \in H$ 使得 $\sigma(h') \neq I_{d_\sigma}$，但 $\sigma(h') \sigma(H) = \sum_{h \in H} \sigma(h' h) = \sigma(H)$，且 $\sigma(h')$ 是酉矩阵，$\sigma(H)$ 是单位矩阵的倍数，所以只能是 $\sigma(H) = 0$；而如果 $H \leq \ker \sigma$，则 $\chi_\sigma(h) = d_\sigma, \forall h \in H$，结果立刻可得.

为了得到 $H$，可以按照阿贝尔群情况下的步骤进行：首先执行 $O(\log \lvert G \rvert)$ 次弱 Fourier 采样，并计算得到的不可约表示的核的交（假设这可以高效完成）. 同样，得到的子群包含 $H$，并且其以高概率等于 $H$. 假设处理过程中的某个阶段得到的子群为 $K$，满足 $K \triangleleft G$ 且 $H \leq K$，那么再次得到一个满足 $K \leq \ker \sigma$ 的不可约表示 $\sigma$ 的概率为

\[
    \sum_{\sigma : K \leq \ker \sigma} \op{Pr}(\sigma) = \frac{\lvert H \rvert}{\lvert G \rvert} \sum_{\sigma : K \leq \ker \sigma} d_\sigma^2 = \frac{\lvert H \rvert}{\lvert K \rvert} \leq \frac{1}{2}.
\]

这样就和阿贝尔群的情况类似，每次弱 Fourier 采样后，至少有一半的概率使得核的交集的大小至少减半，从而 $O(\log \lvert G \rvert)$ 次采样后以高概率得到 $H$. 而当 $H$ 不一定在 $G$ 中正规时，应用相同的方法可以找到 $H$ 的**正规核**（normal core），即 $H$ 在 $G$ 中正规的最大子群.

这个算法可以用于在某种意义下“接近阿贝尔群”的群中寻找隐藏子群. 特别地，Grigni 等人表明，如果 $G$ 所有子群的正规化子的交集 $\kappa(G)$ 足够大，具体来说满足 $\lvert G \rvert / \lvert \kappa(G) \rvert = 2^{O(\log^{1/2} \log \lvert G \rvert)}$，例如 $G = \mathbb{Z}_3 \rtimes \mathbb{Z}_{2^n}$，那么 $G$ 中的 $\op{HSP}$ 可以在多项式时间内解决. 思路为将正规子群的算法应用于 $G$ 到所有包含 $\kappa(G)$ 的子群的限制上，通过这种方式获得的所有子群的并集以高概率给出隐藏子群. 这一结果后来为 Gavinsky 改进，只要满足 $\lvert G \rvert / \lvert \kappa(G) \rvert = \op{poly}(\log \lvert G \rvert)$ 即可给出多项式时间量子算法.

## Strong Fourier sampling

对于大多数隐藏子群问题而言，弱 Fourier 采样并不能提供足够的信息来恢复隐藏子群 $H$，如二面体群和对称群. 为了获得关于隐藏子群的更多信息，我们可以在弱 Fourier 采样返回结果 $\sigma$ 时，对产生的 $d_\sigma^2$ 状态进行测量，这一方法称为**强 Fourier 采样**（strong Fourier sampling）.

回顾 $\hat{\rho}_H$ 在行寄存器上是最大叠加态，因此可以无损丢弃这一寄存器，使得强 Fourier 采样实际上是对 $d_\sigma$ 维空间中的态

\[
    \hat{\rho}_{H, \sigma} := \frac{\sigma(H)^*}{\op{Tr} \sigma(H)^*} = \frac{\sigma(H)^*}{\sum_{h \in H} \chi_\sigma(h)^*}.
\]

而这个态实际上正比于投影算子，秩为平凡表示在 $\op{Res}_H^G \sigma$ 中出现的次数. 因为

\[
    \sigma(H)^2 = \sum_{h, h' \in H} \sigma(h h') = \lvert H \rvert \sigma(H),
\]

由此可得

\[
    \hat{\rho}_{H, \sigma}^2 = \frac{\lvert H \rvert}{ \sum_{h \in H} \chi_\sigma(h)^* } \hat{\rho}_{H, \sigma}.
\]

所以 $\hat{\rho}_{H, \sigma}$ 正比于投影算子，秩为 $\sum_{h \in H} \chi_\sigma(h)^* / \lvert H \rvert$.

但基的选择也是有一定困难的，自然的想法是考虑在随机基中测量的结果（在 $\mathbb{C}^{d_\sigma}$ 上依照 Harr 测度均匀随机选择的基）. 在某些情况下，这种随机强 Fourier 采样能产生足够的信息识别隐藏子群，Sen 证明了在 $\op{rank}(\hat{\rho}_{H, \sigma}) = \op{poly}(\log \lvert G \rvert)$ 的情况下，该方法总是有效的.

但在很多情况下这种随机强 Fourier 采样无法提供帮助. Grigni 等人证明如果 $H$ 足够小，且 $G$ 在“某种意义”下足够“非阿贝尔”的话，那么随机强 Fourier 采样提供的信息量不大，他们证明了这对于对称群寻找隐藏对合是成立的. Moore 等人证明了当 $q \leq p^{1-\epsilon}$ 时，随机强 Fourier 采样在亚循环群 $\mathbb{Z}_p \rtimes \mathbb{Z}_q$ 上失效.

即使在随机基上测量在信息论意义下是足够的，但因为不能进行高效测量，其也不能给出一个高效的量子算法. 转而去寻找能够高效实现并且信息量大的伪随机基是一个有趣的研究方向，但在缺乏此类技术的情况下，去寻找显式的基，使得强 Fourier 采样能够高效执行，并且给出 $\op{HSP}$ 的解，也是可以料想的. Moore 等人针对先前提到的亚循环群给出了第一个这样的算法，但是要求 $q = p/\op{poly} (\log p)$. 目前仍未找到强 Fourier 采样成功而随机强 Fourier 采样失败的例子. 制约 $\op{HSP}$ 量子算法设计的不仅有合适的基，还有测量结果的后处理方法. Ettinger 和 Høyer 为二面体群的 $\op{HSP}$ 给出了一个基，在该基下测量能够得到足够的信息来确定隐藏子群，但后处理方法并不高效. 

而对于某些群，例如对称群，强 Fourier 采样被证明是行不通的. Moore, Russell 和 Schulman 证明了对于任何测量基，当隐藏子群是平凡子群和对合子群时，测量结果的分布是指数接近的. 因此，通常我们必须考虑对多个隐藏子群状态副本进行纠缠测量，Hallgren 等人证明对于对称群而言，可能需要 $\Omega(\log \lvert G \rvert)$ 个副本进行纠缠测量. 接下来两讲将介绍一些利用纠缠测量解决 $\op{HSP}$ 的方法.