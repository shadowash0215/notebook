# Course overview and discriminating two pure states

## Discriminating between two pure states

### Problem statement

!!!+ definition "POVMs"
    **正算子值测量 (POVM)** 是一组正算子 $E = \{E_1, \ldots, E_m\}$，满足 $\forall 1 \leq i \leq m, E_i \succeq 0$ 且 $\sum_{i=1}^m E_i = I$. 如果其施加在纯态 $\ket{\psi}$ 上，则测量结果为 $i$ 的概率为 $\bra{\psi} E_i \ket{\psi}$. 此外，如果其施加在混合态 $\rho$ 上，则测量结果为 $i$ 的概率为 $\mathsf{Tr}(E_i \rho)$.

!!!+ definition "Worst-case error"
    **最坏情况误差** 是指在所有可能的输入中，算法输出错误的最大概率. 对于只有两个正算子 $E_1$ 和 $E_2$ 的 POVM，最坏情况误差为 $\max\{\bra{\psi_1} E_2 \ket{\psi_1}, \bra{\psi_2} E_1 \ket{\psi_2}\}$.

在没有先验知识的情况下，最坏情况误差是衡量测量的合理依据.

### Strategies for two state discrimination

**Nontrivial strategies**

!!! note "Observation"
    尽管 $\ket{\psi_1}$ 和 $\ket{\psi_2}$ 都是 $d$-维的，但其二者只张成了一个 $2$-维的子空间 $S = \mathrm{span}\{\ket{\psi_1}, \ket{\psi_2}\}$. 因此，测量策略可以只定义在 $S$ 上.

记 $\theta$ 为 $\ket{\psi_1}$ 和 $\ket{\psi_2}$ 之间的夹角. 不失一般性，设 $\theta \in [0, \pi/2]$，否则的话使用 $-\ket{\psi_2}$ 代替 $\ket{\psi_2}$ 即可.

!!!+ theorem "Optimal worst-case distinguisher"
    设 $\ket{\psi_1}$ 和 $\ket{\psi_2}$ 是两个纯态，且 $\theta$ 为它们之间的夹角. 则最优的最坏情况区分器是在基 $\{\ket{v_1}, \ket{v_2}\}$ 下测量，直观来说就是将 $\ket{\psi_1}$ 和 $\ket{\psi_2}$ 向外同时旋转相同的角度直到二者正交.

!!!+ theorem "Optimal worst-case error"
    最优策略的的成功概率为 $\frac{1}{2} + \frac{1}{2}\sin(\theta)$，最坏情况误差为 $\frac{1}{2} - \frac{1}{2}\sin(\theta)$.

## Unambiguous state discrimination

两个非正交态无法被完美区分，但这不代表测量策略一定会以非零概率输出错误的结果. 事实上，存在测量策略可以在不输出错误结果的情况下区分两个非正交态，但代价是有一定概率输出“不确定”结果，这就是无歧义态区分 (unambiguous state discrimination) 的概念. 存在一个总是猜测“不确定”的平凡策略，那么定义

\[
    p_1 := \op{Pr}[\text{ “不知道” } \mid \ket{\psi_1}], \quad p_2 := \op{Pr}[\text{ “不知道” } \mid \ket{\psi_2}].
\]

平凡策略有 $p_1 = p_2 = 1$. 我们希望找到一个最优策略最小化 $\max\{p_1, p_2\}$. 

### Strategies for unambiguous state discrimination

1. 可以考虑在基 $\{\ket{\psi_1}, \ket{\psi_1^\perp}\}$ 下测量. 如果测量结果为 $\ket{\psi_1^\perp}$，则可以确定输入态为 $\ket{\psi_2}$. 但是如果测量结果为 $\ket{\psi_1}$，就无法确定输入态，因此应该输出“不确定”. 这种策略输出不知道的概率为 $p_1 = 1$ 和 $p_2 = \lvert \innerproduct{\psi_1}{\psi_2} \rvert^2 = \cos^2(\theta)$. 按照指标来说其并不算优秀，但其确实能够以 $1 - \cos^2(\theta) = \sin^2(\theta)$ 的概率正确判断输入态为 $\ket{\psi_2}$.

2. 接下来修改该策略以对称处理 $\ket{\psi_1}$ 和 $\ket{\psi_2}$. 

    - 以 $\frac{1}{2}$ 的概率选择测量基 $\{\ket{\psi_1}, \ket{\psi_1^\perp}\}$，观察到 $\ket{\psi_1}$ 则输出“不确定”，观察到 $\ket{\psi_1^\perp}$ 则输出 $\ket{\psi_2}$.

    - 以 $\frac{1}{2}$ 的概率选择测量基 $\{\ket{\psi_2}, \ket{\psi_2^\perp}\}$，观察到 $\ket{\psi_2}$ 则输出“不确定”，观察到 $\ket{\psi_2^\perp}$ 则输出 $\ket{\psi_1}$.

    这也是一个有效的无歧义量子态区分算法. 因为其对称处理 $\ket{\psi_1}$ 和 $\ket{\psi_2}$，所以输入为 $\ket{\psi_1}$ 和 $\ket{\psi_2}$ 时输出“不确定”的概率相同. 不妨假设输入的态为 $\ket{\psi_2}$，此时算法以 $\frac{1}{2}$ 的概率选择测量基 $\{\ket{\psi_2}, \ket{\psi_2^\perp}\}$，此时输出“不确定”的概率为 $\frac{1}{2}$. 以 $\frac{1}{2}$ 的概率选择测量基 $\{\ket{\psi_1}, \ket{\psi_1^\perp}\}$，此时输出 $\ket{\psi_1^\perp}$ 的概率为 $\frac{1}{2} \sin^2(\theta)$，输出 $\ket{\psi_1}$ 的概率为 $\frac{1}{2} \cos^2(\theta)$. 因此成功的概率为 $\frac{1}{2} \sin^2(\theta)$，输出“不确定”的概率为 $\frac{1}{2} + \frac{1}{2} \cos^2(\theta)$.

3. 因为区分点都是在测量出 $\ket{\psi_1^\perp}$ 或 $\ket{\psi_2^\perp}$ 时，所以自然地会定义以下两个测量算子：

\[
    \Pi_1 := \ket{\psi_2^\perp}\bra{\psi_2^\perp}, \quad \Pi_2 := \ket{\psi_1^\perp}\bra{\psi_1^\perp}.
\]

如果定义测量 $\{\Pi_1, \Pi_2, \Pi_?\}$，其中 $\Pi_? := I - \Pi_1 - \Pi_2$，那么这似乎就给出了一个自然的无歧义区分策略. 但问题在于，如果 $\theta < \frac{\pi}{2}$，那么 $\ket{\psi_1^\perp}$ 和 $\ket{\psi_2^\perp}$ 并不正交，此时

\[
    \lambda := \lambda_{\max}(\Pi_1 + \Pi_2) 
\]

就可能大于 $1$，从而 $\Pi_?$ 不是正算子. 因此需要对 $\Pi_1$ 和 $\Pi_2$ 进行缩放. 考虑 $E = \{E_1, E_2, E_?\}$，其中

\[
    E_1 := \frac{1}{\lambda} \Pi_1, \quad E_2 := \frac{1}{\lambda} \Pi_2, \quad E_? := I - E_1 - E_2.
\]

那么问题变成了如何求解 $\lambda$. 求矩阵最大特征值等价于遍历所有单位向量 $\ket{v}$，求解 

\[
    \bra{v} (\Pi_1 + \Pi_2) \ket{v} = (\lvert \innerproduct{v}{\psi_1^\perp} \rvert^2 + \lvert \innerproduct{v}{\psi_2^\perp} \rvert^2).
\]

的最大值. 一个自然的猜测是 $\ket{v} = \frac{1}{\sqrt{2}}(\ket{\psi_1^\perp} + \ket{\psi_2^\perp})$，此时 $\ket{v}$ 与 $\ket{\psi_1^\perp}$ 和 $\ket{\psi_2^\perp}$ 的夹角都是 $\frac{\theta}{2}$，从而得到 $\lambda \geq \cos^2(\frac{\theta}{2}) + \cos^2(\frac{\theta}{2}) = 1 + \cos(\theta)$. 事实上，这个 $\lambda$ 就是最大特征值. 

!!!+ lemma "Maximum eigenvalue of $\Pi_1 + \Pi_2$"
    以上向量 $\ket{v} = \frac{1}{\sqrt{2}}(\ket{\psi_1^\perp} + \ket{\psi_2^\perp})$ 是 $\Pi_1 + \Pi_2$ 的最大特征向量，最大特征值为 $\lambda = 1 + \cos(\theta)$.

!!!+ theorem "Performance of the optimal strategy"
    输出“不确定”的最优最坏情形概率 $\cos(\theta)$.