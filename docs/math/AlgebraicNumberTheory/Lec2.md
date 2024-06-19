# Norm, Trace, Discriminant

## Norm, Trace

设 $A$ 是含幺交换环，$E$ 是一个自由 $A$-模，秩为 $n$，有一组基 $e = \{e_1, e_2, \ldots, e_n\}$. 考虑 $E$ 的一个模同态 $u: E \to E$，则 $u$ 在 $e$ 下的矩阵表示记为 $M_u = (a_{ij}) \in M_n(A)$. 考虑以下多项式展开：

\[
    \operatorname{det}(XI - M_u) = X^n + \operatorname{Tr}(M_u)X^{n-1} + \cdots + (-1)^n\operatorname{det}(M_u).
\]

其定义了矩阵 $M_u$ 的行列式和迹.  

而考虑环 $A \subset B$，二者均为含幺交换环，$B$ 为秩为 $n$ 的自由 $A$-模. 对于 $x \in B$，考虑 $A$-模同态 $u_x: y \mapsto xy$，则 $u_x$ 的迹被称为 $x$ 的迹，记为 $\operatorname{Tr}_{B/A}(x)$. 同理，$u_x$ 的行列式被称为 $x$ 的范数，记为 $\operatorname{N}_{B/A}(x)$.

对于域扩张 $E/F$，$E$ 中元素的迹和范数是“下降”到 $F$ 的重要方法. 以下给出域扩张下元素的迹和范数的等价定义：

!!! note "Theorem"
    设 $F$ 为有限域或特征为 0 的域，域扩张 $E/F$ 满足 $[E:F] = n$，取 $\alpha \in E$，其极小多项式为 $f_{\alpha}(X)$，度为 $m$，且其根为 $\alpha_1, \alpha_2, \ldots, \alpha_m \in F^{\text{alg}}$，满足两两互异. 则以下式子成立：  
    
    \begin{gather}
        \operatorname{det}_{E/F}(X\operatorname{Id}_E - \alpha) = f_{\alpha}(X)^{\frac{n}{m}} = \prod_{\sigma \in \operatorname{Hom}_F(E, F^{\text{alg}})} (X - \sigma(\alpha)), \\
        \operatorname{Tr}_{E/F}(\alpha) = \frac{n}{m} \sum_{i=1}^m \alpha_i, \quad \operatorname{N}_{E/F}(\alpha) = (\prod_{i=1}^m \alpha_i)^{\frac{n}{m}}.
    \end{gather}

    ??? note "Proof"
        (i) 设 $E = F[\alpha]$，则 $n = m$. 取 $E$ 的一组基 $B = \{1, \alpha, \ldots, \alpha^{n - 1}\}$，则 $B$ 为 $F$-线性无关的. 将 $f_\alpha(X)$ 展开，有

        \begin{align}
            f_{\alpha}(X) &= X^n + a_{n-1}X^{n-1} + \cdots + a_0 \\
            &= \prod_{i=1}^n (X - \alpha_i). \\
        \end{align}

        同时考虑 $u_{\alpha}$ 在 $B$ 下的矩阵表示，如下所示：

        \[
            M_{\alpha} = \begin{pmatrix}
                0 & 0 & \cdots & 0 & -a_0 \\
                1 & 0 & \cdots & 0 & -a_1 \\
                0 & 1 & \cdots & 0 & -a_2 \\
                \vdots & \vdots & \ddots & \vdots & \vdots \\
                0 & 0 & \cdots & 1 & -a_{n-1}
            \end{pmatrix}.
        \]

        计算后可以得到 $\operatorname{det}_{E/F}(X\operatorname{Id}_E - \alpha) = f_{\alpha}(X)$. 迹与范数只需在此基础上进行计算即可. 此处的 $M_{\alpha}$ 也就是多项式 $f_{\alpha}(X)$ 的友矩阵.
        
        (ii) 而对于一般的情况，