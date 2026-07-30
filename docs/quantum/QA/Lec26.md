# The compressed oracle method

## The compressed oracle

假设我们拥有对随机均匀函数 $f: [n] \to \Sigma$ 的谕示机访问权限，其中 $\Sigma = \{0, 1\}^m$. 对该函数的量子查询为 $\ket{x}\ket{z} \mapsto \ket{x}\ket{z \oplus f(x)}$. 

通过引入额外的寄存器编码谕示机的真值表便可以实现查询. 真值表记为 $\ket{y_1, y_2, \ldots, y_n}$，其中 $y_x = f(x)$，令查询按如下酉算子进行作用：

\[
    \Lambda: \ket{x}\ket{z}\ket{y_1, y_2, \ldots, y_n} \mapsto \ket{x}\ket{z \oplus y_x}\ket{y_1, y_2, \ldots, y_n}.
\]

如果算法无法访问这些谕示机寄存器，那么其与拥有对 $f$ 的黑盒访问权限是不可区分的；并且，如果让谕示机寄存器的初始状态处于均匀叠加态，其便于一个均匀随机函数的谕示机是不可区分的. 

压缩谕示机（Compressed oracle）方法的核心思想是在收到查询时动态生成响应，并以算法无法察觉的方式记录下哪些内容已经被查询过. 符号 $\perp$ 表示某个特定项未被查询过，谕示机寄存器的初始状态均为 $\ket{\perp}$. 发起查询时，若该项未被查询过，则谕示机会随机响应；而若该项已经被查询过，则谕示机会返回之前的响应.

更具体地，如下定义压缩谕示机. 对于 $y \in \Sigma$，定义 $\ket{\hat{y}} := H^{\otimes m} \ket{y}$，其中 $H$ 是 Hadamard 门. 定义“压缩/解压”酉算子 $C$，其作用于 $\operatorname{span}(\{\ket{y}: y \in \Sigma\} \cup \{\ket{\perp}\})$，其中 $\ket{\perp}$ 是一个正交于所有 $\ket{y}$ 的归一态. $C$ 的具体作用如下所示：

\begin{align*}
    C \ket{\perp} &= \ket{\hat{0}} = \frac{1}{\sqrt{\lvert \Sigma \rvert}} \sum_{y \in \Sigma} \ket{y}, \\
    C \ket{\hat{0}} &= \ket{\perp}, \\
    C \ket{\hat{y}} &= \ket{\hat{y}} \quad \text{for all } y \in \Sigma \setminus \{0\}, \\
\end{align*}

压缩谕示机按 $(I \otimes I \otimes C^{\otimes n}) \Lambda (I \otimes I \otimes C^{\otimes n})$ 进行作用，其中对 $\Lambda$ 进行了延拓，使其在 $\ket{x}\ket{z}\ket{\perp}, \forall x \in [n]$ 的作用上和恒等算子一致. 换言之，压缩谕示机在每次查询前和查询后分别对谕示机寄存器进行了解压和压缩.

## Relating the standard and compressed oracles

!!! success "Lemma"
    设 $R \subseteq [n] \times \Sigma$ 为一组输入-输出对. 假设一个向随机谕示机进行查询的量子算法输出了 $k$ 个输入输出对 $(x_1, z_1), (x_2, z_2), \ldots, (x_k, z_k)$，满足对于任意 $i$，$f(x_i) = z_i$，并且 $(x_i, z_i) \in R$ 的概率为 $p$. 而考虑该算法向压缩谕示机进行查询的情况，在对应 $x_i$ 的谕示机寄存器的结果为 $y_i$，满足对于任意 $i$，$z_i = y_i$，并且 $(x_i, y_i) \in R$ 的概率为 $p'$. 则有 $\sqrt{p} \leq \sqrt{p'} + \sqrt{k/2^m}$.

    ??? success "Proof"
        设 $\ket{\psi}$ 为算法在向随机谕示机进行查询前的状态，谕示机的初始状态为 $\ket{\hat{0}}^{\otimes n}$，并且算法交替进行酉算子 $\Lambda$ 查询和任意非查询操作. 唯一的区分在于最后一步，压缩谕示机会对谕示机寄存器施加 $C^{\otimes n}$ 进行压缩.

        令 $\Pi_x = \ket{y_1} \bra{y_1} \otimes \cdots \otimes \ket{y_k} \bra{y_k}$ 为谕示机寄存器上的投影算子，对应 $f$ 在 $x = (x_1, \ldots, x_k)$ 处的求值. 不失一般性，假设算法会测量最终的工作空间寄存器，在计算基下得到结果 $w$，那么有

        \begin{align*}
            p &= \sum_{x, y \in R} \sum_w \Pr{\text{算法输出 } x, y, w} \Pr{f(x) = y \mid \text{算法输出 } x, y, w} \\
            &= \sum_{x, y \in R} \sum_w p_{x, y, w} \lVert \Pi_x \ket{\psi_{x, y, w}} \rVert^2,
        \end{align*}

        其中 $p_{x, y, w} := \Pr{\text{算法输出 } x, y, w}$，$\ket{\psi_{x, y, w}}$ 是在算法输出 $x, y, w$ 的条件下，谕示机寄存器的后选择状态. 