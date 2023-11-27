# 对称群 交错群 二面体群

首先来介绍**对称群**(symmetric group)。

!!! info "定义"
    对称群 $S_n$ 是底集合为从 $I_n$ 到 $I_n$ 的全体置换和映射复合作为乘法构成的群，其中 $I_n = \{1, 2, \ldots, n\}$，因为 $n$ 个元素的全排序的个数为 $n!$，所以 $S_n$ 中元素个数为 $n!$，即 $S_n$ 的阶为 $n!$.

但我们对于置换的表示太过复杂，比如 $\begin{pmatrix} 1 & 2 & \cdots & n \\ \sigma(1) & \sigma(2) & \cdots & \sigma(n) \end{pmatrix}$，在复合的时候更是头大，于是我们尝试将置换进行分解简化。

!!! info "定义"
    设 $i_1, i_2, \ldots, i_r, (r \leqslant n)$ 是 $I_n$ 中互异的元素，那么 $(i_1i_2\cdots i_r)$ 定义了如下的映射：$i_1 \mapsto i_2, i_2 \mapsto i_3, \cdots, i_{r-1} \mapsto i_r \enspace \textrm{and} \enspace i_r \mapsto i_1; i_k \mapsto i_k \enspace \textrm{otherwise}$. $(i_1i_2\cdots i_r)$ 被称为长度为 $r$ 的**循环**(cycle)，或者 $r$-循环. 长度为 2 的循环被称为**对换**(transposition)

循环的记号并不是固定的，例如 $(1234) = (2341) = (3412) = (4123)$。显然 $r$-循环的阶都是 $r$，且循环 $(i_1i_2\cdots i_r)$ 的逆就是 $(i_ri_{r-1}i_{r-2}\cdots i_1)$。一般来说，置换的乘积是不可交换的，但在下面的这种情况下是可交换的。

!!! info "定义"
    一组 $S_n$ 中的置换 $\sigma_1, \sigma_2, \ldots, \sigma_r$ 被称为**不交的**(disjoint)，如果对于任一 $1 \leqslant i \leqslant n$，任一 $k \in I_n$，若 $\sigma_i(k) \neq k$，则必有 $\sigma_j(k) = k, \forall j \neq i$. 即所有的元素没有被 $\sigma_1, \sigma_2, \ldots, \sigma_r$ 移动超过一次.

而一旦 $\sigma$ 和 $\tau$ 是不交的，必有 $\sigma \tau = \tau \sigma$，这就可以为我们的简化提供思路。

!!! note "定理"
    每个 $S_n$ 中的非恒等置换在不计因子次序的意义下都可以被唯一分解为不交循环的乘积，且每个循环的长度至少为 2.

有了这个定理，下面的这两个推论就是显而易见的。

!!! success "推论"
    (i) $S_n$ 中的置换 $\sigma$ 的阶是其分解的诸循环之阶的最小公倍数. 

    (ii) 所有 $S_n$ 的置换可以被写成一系列对换的乘积.

这也就引出了下面这个定义。

!!! info "定义"
    $S_n$ 中的一个置换 $\tau$ 被称为偶的(even)（或奇的(odd)），若其可被写作偶数个（奇数个）对换的乘积.

我们可以定义如下符号态射 $\textrm{sgn} \ \tau$(sign of a permutation $\tau$)，

$$
    \textrm{sgn} \ \tau = \begin{cases} 1, \tau \ \textrm{is even}, \\ -1, \tau \ \textrm{is odd}.\end{cases}
$$

其良定义的证明需要以下定理。

!!! note "定理"
    $S_n, n \geqslant 2$ 中的置换不可能既是奇的又是偶的.  

这之后我们来看符号态射的核，可以发现其是由 $S_n$ 中全体偶置换组成的，显然它也构成群，称为**交错群**(alternating group)，记作 $A_n$，并有如下定理：

!!! note "定理"
    $\forall n \geqslant 2$，$A_n$ 是 $S_n$ 中唯一的指标为 2 的正规子群，阶为 $\frac{\lvert S_n \rvert}{2} = \frac{n!}{2}$.

这里我们引入一个新的概念：

!!! info "定义"
    若群 $G$ 没有非平凡正规子群，则其被称为**单群**(simple group)。

这就有了接下来这个结论，事实上，其在 Galois theory 中也有应用。

!!! note "定理"
    交错群 $A_n$ 是单群等价于 $n \neq 4$.

证明它需要以下两个引理。

!!! success "引理"
    (i) 设 $r, s$ 是 $\{1, 2, \ldots, n\}$ 中互异的元素，则 $A_n (n \geqslant 3)$ 由 $3$-循环 $\{(rsk) \mid 1 \leqslant k \leqslant n, k \neq r, s\}$ 生成.

    (ii) 设 $N$ 是 $A_n$ 的一个正规子群，且 $N$ 包含一个 $3$-循环，那么 $N = A_n$.

$S_n$ 还有一个重要的子群，被称为**二面体群**(dihedral group)，记作 $D_n$，其由置换 $a = (123\cdots n)$ 和 $b = \begin{pmatrix} 1 & 2 & 3 & \cdots & i & \cdots & n-1 & n \\ 1 & n & n-1 & \cdots & n+2-i & \cdots & 3 & 2 \end{pmatrix}$ 生成。其实它同构于对正 $n$ 边形做如下操作构成的群： $a=$ 逆时针旋转 $\frac{2\pi}{n}$，$b=$ 绕 $x$ 轴翻转。由此可以发现其生成元满足如下的性质：

!!! note "定理"
    对二面体群 $D_n(n \geqslant 3)$，其生成元 $a, b$ 满足如下条件：  
    (i) $a^n = (1), b^2 = (1), a^k \neq (1), 0 < k < n$;  
    (ii) $ba = a^{-1}b$.