# 多项式环 形式幂级数

!!! info "定义"
    设 $R$ 是环，记号 $R[x]$ 表示集合 $\{(a_0, a_1, \ldots, ) \mid a_i \in R, i \in I\}$，对其中有限数目的 $i$ 满足 $a_i \neq 0$，其余均为 0. 则  
    (i) $R[x]$ 在如下定义的加法和乘法下构成环：  

    $$
        (a_0, a_1, \ldots) + (b_0, b_1, \ldots) = (a_0 + b_0, a_1 + b_1, \ldots)
    $$

    $$
        (a_0, a_1, \ldots)(b_0, b_1, \ldots) = (c_0, c_1, \ldots),  
    $$

    其中 
    
    $$
        c_n = \sum_{i = 0}^{n} a_{n-i}b_i = a_nb_0 + a_{n-1}b_1 + \cdots + a_1b_{n-1} + a_0b_n = \sum_{k+j = n} a_kb_j.
    $$

    (ii) $R[x]$ 保留环 $R$ 的如下性质：交换，含幺，无零因子，整环.  
    (iii) 映射 $\varphi: R \rightarrow R[x]$，$r \mapsto (r, 0, 0, \ldots)$ 是一环单态.

环 $R[x]$ 被称为环 $R$ 上的**多项式环**(ring of polynomials)，其中的元素被称为**多项式**(polynomials)。上述定义中第三条的 $(r, 0, 0, \ldots)$ 也被简记为 $r$，因此有 $r(a_0, a_1, \ldots) = (ra_0, ra_1, \ldots)$。我们接下来会继续阐明其性质，使它更像我们所了解的多项式。

!!! note "定理"
    设 $R$ 是含幺环，记 $(0, 1_R, 0, 0, \ldots)$ 为 $x$，则有  
    (i) $x^n = (0, 0, \ldots, 0, 1_R, 0, \ldots)$，其中 $1_R$ 是第 $(n+1)$ 个坐标；  
    (ii) 若 $r \in R$，则对任一 $n \geqslant 0$，$rx^n = x^nr = (0, 0, \ldots, 0, r, 0, \ldots)$，其中 $r$ 是第 $(n+1)$ 个坐标；  
    (iii) 对任一一个 $R[x]$ 中的非零多项式 $f$，存在整数 $n \in N$，$a_0, a_1, \ldots, a_n \in R$，使得 $f = a_0x^0 + a_1x^1 + \cdots + a_nx^n$，且 $n, a_0, a_1, \ldots, a_n$ 在如下意义下唯一：若 $f = b_0x^0 + b_1x^1 + \cdots + b_mx^m$, $b_i \in R$，且 $m \geqslant n$，则当 $0 \leqslant i \leqslant n$ 时，$a_i = b_i$，而当 $n < i \leqslant m$ 时，$b_i = 0$. 

若 $R$ 是含幺环，则 $x^0 = 1_R$；若 $R$ 不是含幺环，我们知道 $R$ 可以被嵌入含幺环 $S$ 中，此时 $x^0 = 1_S$。所以我们可以将 $R[x]$ 中的任一多项式 $f$ 记作 $f = a_0 + a_1x + a_2x^2 + \cdots + a_nx^n$，并且用更熟悉的记号表示多项式的加法和乘法：

$$
    \sum_{i = 0}^n a_ix^i + \sum_{i = 0}^n b_ix^i = \sum_{i = 0}^n (a_i+b_i)x^i
$$

$$
    \left(\sum_{i = 0}^n a_ix^i\right)\left(\sum_{j = 0}^m b_jx^j\right) = \sum_{k = 0}^{m+n} c_kx^k, c_k = \sum_{i+j = k}a_ib_j.
$$

$a_i$ 被称作多项式 $f$ 的**系数**(coefficients)，$a_0$ 被称作**常数项**(constant term)。$R$ 中的元素 $r$ 都具有 $r = (r, 0, 0, \ldots) = rx^0$ 的形式，称作**常数多项式**(constant polynomials)。若 $f = \sum_{i = 0}^n a_ix^i = a_0 + a_1x + \cdots + a_nx^n, a_n \neq 0$，则称 $a_n$ 为 $f$ 的**首项系数**(leading coefficient)，若 $R$ 含幺且 $f$ 的首项系数为 $1_R$，则 $f$ 被称为**首一多项式**(monic polynomial)。

元素 $x$ 被称为**未定元**(indeterminate)。以上的多项式都是关于未定元 $x$ 的多项式，下面我们来讨论有多个未定元的多项式。方便起见，我们的讨论都是在未定元个数有限的情况下进行的。

!!! info "定义"
    设 $R$ 是环，记 $R[x_1, \ldots, x_n]$ 是所有满足如下性质的函数的集合：$f: N^n \rightarrow R$，只有有限个元素 $u \in N^n$ 使得 $f(u) \neq 0$，则  
    (i) $R[x_1, \ldots, x_n]$ 在如下的加法和乘法下构成环：

    $$
        (f + g)(u) = f(u) + g(u), (fg)(u) = \sum_{v+w = u, v, w \in N^n} f(v)g(w),
    $$

    其中 $f, g \in R[x_1, \ldots, x_n], u \in N^n$.

    (ii) $R[x_1, \ldots, x_n]$ 保留环 $R$ 的如下性质：交换，含幺，无零因子，整环.  

    (iii) 映射 $\varphi: R \rightarrow R[x_1, \ldots, x_n]$，$r \mapsto f_r$，其中 $f_r(0, \ldots, 0) = r$，$f(u) = 0, u \in N^n, u \neq (0, \ldots, 0)$. $\varphi$ 是一环单态.

环 $R[x_1, \ldots, x_n]$ 被称为 $R$ 上的 **$n$（个未定）元多项式环**(ring of polynomials in $n$ indeterminates)。取定 $N^n$ 的自然基 $\varepsilon$：$\varepsilon_i = (0, \ldots, 0, 1, 0, \ldots, 0), i \in \{1, 2, \ldots, n\}$，其中 1 是 $\varepsilon_i$ 的第 $i$ 个坐标，我们利用这组基来化简 $n$ 元多项式环的表示。

!!! note "定理"
    设 $R$ 是一含幺环，$n$ 是一正整数，对 $i = 1, 2, \ldots, n$，$x_i$ 是 $R[x_1, \ldots, x_n]$ 中按如下式子定义的元素：$x_i(\varepsilon_i) = 1_R$，$x_i(\varepsilon_i) = 0$，则：  
    (i) 对任意整数 $k \in N$，$x_i^k(k\varepsilon_i) = 1_R, x_i^k(u) = 0, u \neq k\varepsilon_i$.  
    (ii) 任一 $(k_1, \ldots, k_n) \in N^n$，$x_1^{k_1}x_2^{k_2}\cdots x_n^{k_n}(k_1\varepsilon_1 + \cdots + k_n \varepsilon_n) = 1_R,x_1^{k_1}x_2^{k_2}\cdots x_n^{k_n}(u) = 0, u \neq k_1\varepsilon_1 + \cdots + k_n \varepsilon_n$.  
    (iii) $\forall s, t \in N, i, j = 1, 2, \ldots, n$, $x_i^sx_j^t = x_j^tx_i^s$.  
    (iv) $\forall r \in R, t \in N$, $x_i^tr = rx_i^t$.  
    (v) 对 $R[x_1, \ldots, x_n]$ 中任意的非零多项式 $f$，均存在由 $(k_1, \ldots, k_n) \in N^n$ 标记的 $a_{k_1, \ldots, k_n} \in R$，且至多有限项非零，使得  

    $$
        f = \sum a_{k_1, \ldots, k_n}x_1^{k_1}x_2^{k_2}\cdots x_n^{k_n}.
    $$

??? tip "提示"
    注意这里的 $x_i^{k_i}$ 就是乘积，而 $x_i^{k_i}(k_i \varepsilon_i) = 1_R$ 是可以依靠 $x_i(\varepsilon_i) = 1_R$，$x_i(u) = 0$ 以及定义的乘法法则得到的，$x_1^{k_1}x_2^{k_2}\cdots x_n^{k_n}(k_1\varepsilon_1 + \cdots + k_n \varepsilon_n) = 1_R$ 同理.

形如 $ax_1^{k_1}x_2^{k_2}\cdots x_n^{k_n}$ 的式子被称为**单项式**(monomial)。对于 $\{1, 2, \ldots, n\}$ 的任意子集 $\{i_1, i_2, \ldots, i_k\}$，都存在环单态 $R[x_{i_1}, \ldots, x_{i_k}] \rightarrow R[x_1, \ldots, x_n]$，所以考虑 $R[x_{i_1}, \ldots, x_{i_k}]$ 时，通常考虑其同构像，并视作 $R[x_1, \ldots, x_n]$ 的子环。

设 $\varphi: R \rightarrow S$ 是环同态，$f \in R[x_1, \ldots, x_n]$，而 $s_1, s_2, \ldots, s_n \in S$。由以上定理，我们可以将 $f$ 表作 $f = \sum_{i = 0}^m x_1^{k_{i1}}\cdots x_n^{k_{in}}, a_i \in R, k_{ij} \in N$。去除掉指数为 $0$ 的全部 $x_i$，我们定义 $\varphi f(s_1, \ldots, s_n) = \sum_{i = 0}^m \varphi(a_i) s_1^{k_{i1}} \cdots s_n^{k_{in}} \in S$. 因为 $a_i$ 和 $k_{ij}$ 是唯一确定的，所以 $\varphi f(s_1, \ldots, s_n)$ 是良定义的。如果 $\varphi$ 是包含映射，那么我们依然使用 $f(s_1, \ldots, s_n)$ 表示 $\varphi f(s_1, \ldots, s_n)$.

如同其他代数结构，多项式环也可以用泛性质刻画，其泛性质如下：

!!! note "定理"
    设 $R$ 和 $S$ 是含幺交换环，且环同态 $\varphi: R \rightarrow S$ 满足 $\varphi(1_R) = 1_S$. 若 $s_1, s_2, \ldots s_n \in S$，则存在唯一的环同态 $\bar{\varphi}: R[x_1, \ldots, x_n] \rightarrow S$ 使得 $\bar{\varphi} \mid R = \varphi$，且 $\bar{\varphi}(x_i) = s_i, i = 1, 2, \ldots, n$. 这个性质在不计同构的情况下完全确定了多项式环. 

!!! success "推论"
    (i) 若 $\varphi : R \rightarrow S$ 是交换环的同态，$s_1, s_2, \ldots, s_n \in S$，则映射 $\psi : R[x_1, \ldots, x_n] \rightarrow S$，$f \mapsto \varphi f(s_1, \ldots, s_n)$ 是环同态.  
    (ii) 设 $R$ 是含幺交换环，$n$ 是正整数，则对于每个 $k(1 \leqslant k \leqslant n)$，均存在环同构 $R[x_1, \ldots, x_k][x_{k+1}, \ldots, x_n] \cong R[x_1, \ldots, x_n] \cong R[x_{k+1}, \ldots, x_n][x_1, \ldots, x_k]$. 
 
!!! warning "注意"
    $\varphi$ 是**交换环**同态的要求必不可少.

最后简单介绍一下**形式幂级数环**(rings of formal power series)。

!!! info "定义"
    设 $R$ 是环，以 $R[[x]]$ 表示全体 $R$ 中元素序列 $(a_0, a_1, \ldots)$ 所组成的集合，则  
    (i) $R[[x]]$ 对于如下定义的加法和乘法构成环:  

    \begin{gather}
        + : (a_0, a_1, \ldots) + (b_0, b_1, \ldots) = (a_0 + b_0, a_1 + b_1, \ldots) \\  
        * : (a_0, a_1, \ldots)(b_0, b_1, \ldots) = (c_0, c_1, \ldots), \\ c_n = \sum_{i = 0}^n a_ib_{n-i} = a_0b_n + a_1b_{n-1} + \cdots + a_nb_0 = \sum_{i+j = n} a_ib_j.
    \end{gather}  

    (ii) 多项式环 $R[x]$ 是 $R[[x]]$ 的子环.  
    (iii) $R[[x]]$ 保留环 $R$ 的如下性质：交换，含幺，无零因子，整环.

环 $R[[x]]$ 被称作环 $R$ 上的形式幂级数环，其元素被称为**幂级数**(power series)。若 $R$ 有幺元，则多项式 $x = (0, 1_R, 0, \ldots) \in R[[x]]$ 便是未定元，不难验证 $x^ir = rx^i$。如果 $(a_0, a_1, \ldots) \in R[[x]]$，则对于每个 $n$，$(a_0, a_1, \ldots, a_n, 0, 0, \ldots)$ 是多项式。所以我们可以将幂级数 $(a_0, a_1, \ldots) \in R[[x]]$ 表示为形式和 $\sum_{i = 1}^{\infty} a_ix^i$，元素 $a_i$ 称作系数，$a_0$ 称作常数项。同多项式环情形一致，即使 $R$ 不含幺元，我们也可以使用这一套记号，只是 $x \not \in R[[x]]$。

!!! note "定理"
    (i) 设 $R$ 是含幺环，$f = \sum_{i = 1}^{\infty} a_ix^i \in R[[x]]$. 则  
        (a) $f$ 为 $R[[x]]$ 中单位等价于其常数项 $a_0$ 是 $R$ 中单位.  
        (b) 若 $a_0$ 在 $R$ 中不可约，则 $f$ 在 $R[[x]]$ 中也不可约.  
    
    (ii) 若 $R$ 是除环，则 $R[[x]]$ 中元素为单位的充要条件是该元素有非零常数项. 主理想 $(x)$ 恰好由 $R[[x]]$ 中所有非单位构成，并且它是 $R[[x]]$ 中唯一极大理想. 从而当 $R$ 是域时，$R[[x]]$ 是局部环.