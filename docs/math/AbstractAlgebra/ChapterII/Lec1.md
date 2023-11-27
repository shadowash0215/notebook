# 环基本定义

在群之后，我们要开始研究在其基础上进行加强的一种新的代数结构：**环**(ring)。

!!! info "定义"
    环是由非空集合 $R$ 和满足以下条件的两个二元运算（常被记作加法和乘法）形成的：  
    (i) $(R, +)$ 是一个阿贝尔群；  
    (ii) $\forall a, b, c \in R$, $(ab)c = a(bc)$（乘法结合律）；  
    (iii) $a(b+c) = ab+ac, (a+b)c = ac+bc$（左右分配律）；  
    若有以下额外条件：  
    (iv) $\forall a, b \in R, ab = ba$,  
    称 $R$ 为**交换环**(commutative ring).  
    若 $R$ 中有一元素 $1_R$ 使得
    (v) $\forall, a \in R, 1_Ra = a1_R = a$,  
    称 $R$ 为**含幺环**(ring with identity).  

!!! tip "提示"
    尽管本书中将含幺环与环进行了区分，但现代环论中讨论的环几乎全是含幺环，故此处进行区分.

加法中的单位元我们常记作 $0$。自然而然的，我们就会想了解一个运算中的单位元在另一个运算中的表现是怎样的。先看 $0$ 在乘法中的情况和部分运算律：

!!! success "引理"
    若 $R$ 是一个环，则  
    (i) $\forall a \in R, 0a = a0 = 0$;  
    (ii) $\forall a, b \in R, (-a)b = a(-b) = -ab$;  
    (iii) $\forall a, b \in R, (-a)(-b) = ab$;  
    (iv) $\left(\sum_{i=1}^n a_i\right)\left(\sum_{j=1}^m b_j\right) = \sum_{i=1}^n\sum_{j=1}^m a_ib_j$.

然后对乘法性质的“精细化”可以帮助我们获得性质更好的环，我们来看有哪些“精细化”。

!!! info "定义"
    (i) 对环 $R$ 中的非零元素 $a$，若存在非零元素 $b \in R$ 使得 $ab = 0$，则称 $a$ 是**左零因子**(left zero divisor)；若是 $ba = 0$，则称 $a$ 为**右零因子**(right zero divisor). 若一个元素既是左零因子又是右零因子，则称其为 $R$ 上的**零因子**(zero divisor).  

    (ii) 对含幺环 $R$ 中的元素 $a$，若存在 $c \in R$ 使得 $ca = 1_R$，则称 $a$ 是**左可逆的**(left invertible)，$c$ 称作 $a$ 的**左逆元**(left inverse)；若存在 $b \in R$ 使得 $ab = 1_R$，则称 $a$ 是**右可逆的**(right invertible)，$b$ 称作 $a$ 的**右逆元**(right inverse). 若一个元素既是左可逆的又是右可逆的，则称其为**可逆的**(invertible)，或称其为 $R$ 的一个**单位**(unit).

环 $R$ 没有零因子等价于在其上左右消去律都成立。有了这些定义之后，就有更好的环了。

!!! info "定义"
    若含幺交换环 $R$，$1_R \neq 0$没有零因子，则其被称为**整环**(integer domain). 若含幺环 $D$，$1_D \neq 0$ 上的非零元素都是 $D$ 的单位，则称其为**除环**(division ring). **域**(field) 就是交换除环.

!!! example "示例"
    (i) 设 $A$ 是阿贝尔群，而 $\mathrm{End} A$ 是由全部自同态 $\varphi: A \to A$ 构成的环，其中加法为 $\varphi + \psi = \varphi + \psi$，乘法为 $\varphi\psi = \varphi\circ\psi$，幺元为恒等自同态 $\mathrm{1}_A$.  
    (ii) 设 $G$ 是乘法群，$R$ 是环，以 $R(G)$ 表示加法群 $\sum_{g \in G} R$ (指对每个 $g \in G$ 都有 $R$ 中的元素与之对应). 设 $R(G)$ 中的元素 $x = \{r_g\}_{g \in G}$ 只有有限个非零坐标，设为 $r_{g_1}, \cdots, r_{g_n}(g_i \in G)$. 将 $x$ 表示为形式和 $r_{g_1}g_1 + \cdots + r_{g_n}g_n$，或者 $\sum_{i = 1}^n r_{g_i}g_i$. 我们也允许某些 $r_{g_i}$ 为 0. 以这种记号，我们定义 $R(G)$ 上的加法为 

    \[
        \sum_{i = 1}^n r_{g_i}g_i + \sum_{i = 1}^n s_{g_i}g_i = \sum_{i = 1}^n (r_{g_i} + s_{g_i})g_i.
    \]

    乘法为

    \[
        \left(\sum_{i = 1}^n r_{g_i}g_i\right)\left(\sum_{j = 1}^m s_{g_j}g_j\right) = \sum_{i = 1}^n\sum_{j = 1}^m (r_{g_i}s_{g_j})(g_ig_j).
    \]

    $R(G)$ 被称为 $G$ 在 $R$ 上的**群环**(group ring).
  
!!! info "定义"
    设 $R$ 和 $S$ 都是环，函数 $f: R \to S$ 若满足 $\forall a, b \in R$，有 $f(a+b) = f(a) + f(b), f(ab) = f(a)f(b)$，则称 $f$ 是 $R$ 到 $S$ 的**环同态**(ring homomorphism). 环的同态也依赖于加法群的同态，所以我们可以借用相同的术语，如单态，满态，同构等等. 环的单同态 $R \rightarrow S$ 也称为 $R$ 在 $S$ 中的**嵌入**(embedding).   
    注意，若 $R$ 和 $S$ 均是含幺环，我们并不需要同态满足 $f(1_R) = 1_S$.  

!!! info "定义"
    设 $R$ 是环，如果存在最小正整数 $n$，使得对于所有 $a \in R$，有 $na = 0$，则称 $R$ 是**特征为 $n$ 的环**(ring of characteristic $n$)，记作 $\mathrm{Char} R = n$. 若不存在这样的 $n$，则称 $R$ 的特征为 $0$.

!!! note "定理"
    设 $R$ 是含幺环，并且其特征为 $n > 0$.  
    (i) 若 $\varphi: \mathrm{Z} \rightarrow R$ 是由 $m \mapsto m1_R$ 给出的映射，则 $\varphi$ 是环同态，且 $\mathrm{Ker} \varphi = n\mathrm{Z}$.  
    (ii) $n$ 是最小的正整数使得 $n1_R = 0$.  
    (iii) 如果 $R$ 没有零因子（特别地，若 $R$ 是整环），则 $n$ 是素数. 

!!! note "定理"
    所有的环 $R$ 都可以被嵌入一含幺环 $S$ 中. 环 $S$ 并非是唯一的，其特征可以被选取为 0，也可以被选取为 $\mathrm{Char} R$.