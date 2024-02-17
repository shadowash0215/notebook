# 交换环上的因子分解

本节将从代数的角度去刻画数论当中的一些问题，并将其推广到其他的环上。

!!! info "定义"
    交换环 $R$ 中的非零元素 $a$ 被称作**整除**(divide) $b$，如果存在 $x \in R$ 使得 $b = ax$. 记作 $a \mid b$. 并且 $a$ 和 $b$ 被称作**相伴**(associate)，如果 $a \mid b$ 且 $b \mid a$.

!!! note "定理"
    设 $a, b, u$ 是含幺交换环 $R$ 中的非零元素，那么以下结论成立：  
    (i) $a \mid b$ 当且仅当 $(b) \subset (a)$;  
    (ii) $a$ 和 $b$ 相伴当且仅当 $(a) = (b)$;  
    (iii) $u$ 是 $R$ 的单位当且仅当 $\forall r \in R, u \mid r$;  
    (iv) $u$ 是 $R$ 的单位当且仅当 $(u) = R$;  
    (v) 相伴关系是等价关系;  
    (vi) 若 $a = br$, $r$ 是 $R$ 的单位，那么 $a$ 和 $b$ 相伴; 若 $R$ 是整环，那么逆命题成立.

下面是对不可约元和素元的定义。

!!! info "定义"
    设 $R$ 是含幺交换环. $c \in R$ 被称作**不可约元**(irreducible element)，如果 $c$ 不是非零元素，不是单位，且 $c = ab$ 蕴含 $a$ 或 $b$ 是单位. $p \in R$ 被称作**素元**(prime element)，如果 $p$ 不是非零元素，不是单位，且 $p \mid ab$ 蕴含 $p \mid a$ 或 $p \mid b$.

环中素元和素理想有着密切的联系，不可约元和极大理想重要的关系。

!!! note "定理"
    设 $p$ 和 $c$ 是整环 $R$ 的非零元素，那么以下结论成立：  
    (i) $p$ 是素元当且仅当 $(p)$ 是非零素理想;  
    (ii) $c$ 是不可约元当且仅当 $(c)$ 在由 $R$ 的所有真主理想构成的集合 $S$ 中是极大的;  
    (iii) $R$ 的素元都是不可约元;  
    (iv) 若 $R$ 是主理想整环，那么 $p$ 是素元当且仅当 $p$ 是不可约元;  
    (v) $R$ 中所有与不可约元(素元)相伴的元素都是不可约元(素元);  
    (vi) $R$ 中所有不可约元的因子要么是单位，要么与自身相伴.

我们已经将许多 $\mathrm{Z}$ 中的性质推广到了一般的环上，下面我们将进一步推广到交换环上的因子分解。

!!! info "定义"
    环 $R$ 被称作**唯一分解整环**(unique factorization domain, UFD)，如果 $R$ 是整环，且满足以下条件：  
    (i) $R$ 中的每个非零非单位元素 $a$ 都可以写成有限个不可约元 $c_1, c_2, \ldots, c_n$ 的乘积，即 $a = c_1c_2\cdots c_n$;  
    (ii) 若 $a = c_1c_2\cdots c_n = d_1d_2\cdots d_m$，其中 $c_i, d_j$ 是不可约元，那么 $m = n$ 且存在 $\{1, 2, \ldots, n\}$ 的一个排列 $\sigma$，使得 $c_i$ 和 $d_{\sigma(i)}$ 相伴，$\forall i = 1, 2, \ldots, n$.

接下来是主理想环的一些定理。

!!! success "引理"
    设 $R$ 是主理想环，且 $(a_1) \subset (a_2) \subset \cdots$ 是 $R$ 的一串理想，那么存在 $n \in \mathrm{N}^*$，使得 $(a_n) = (a_{n+1  }) = \cdots$.

!!! note "定理"
    所有主理想整环都是唯一分解整环.

接下来是对另外一些有着特殊性质的环的定义。

!!! info "定义"
    设 $N$ 是所有非负整数的集合，$R$ 是交换环. 则 $R$ 被称作**欧几里得环**(Euclidean ring)，若存在函数 $\varphi: R - \{0\} \rightarrow N$，满足以下条件： 
    (i) 若 $a, b \in R$，且 $ab \neq 0$，那么 $\varphi(a) \leqslant \varphi(ab)$;  
    (ii) 若 $a, b \in R$，且 $b \neq 0$，那么存在 $q, r \in R$，使得 $a = bq + r$，其中 $r = 0$ 或 $r\neq 0, \varphi(r) < \varphi(b)$.  
    若 $R$ 是欧几里得环也是唯一分解整环，那么 $R$ 被称作**欧几里得整环**(Euclidean domain, ED).

!!! note "定理"
    所有欧几里得环都是含幺主理想环，从而所有欧几里得整环都是唯一分解整环.

接下来是最大公因子的推广。

!!! info "定义"
    设 $X$ 是交换环 $R$ 的非空子集，$d \in R$ 被称作 $X$ 的**最大公因子**(greatest common divisor, GCD)，如果满足以下条件：  
    (i) $d \mid x, \forall x \in X$;  
    (ii) 若 $c \mid x, \forall x \in X$，那么 $c \mid d$.

所以 $R$ 中的元素 $a_1, a_2, \ldots, a_n$ 被称作**互素**(relatively prime)，如果它们的最大公因子是单位.  

!!! note "定理"
    设 $a_1, a_2, \ldots, a_n$ 是含幺交换环 $R$ 的元素，那么以下结论成立：  
    (i) $d \in R$ 是 $a_1, a_2, \ldots, a_n$ 的最大公因子，则存在 $r_1, r_2, \ldots, r_n \in R$，使得 $d = r_1a_1 + r_2a_2 + \cdots + r_na_n$ 当且仅当 $(d) = (a_1) + (a_2) + \cdots + (a_n)$;  
    (ii) 若 $R$ 是主理想整环，则 $a_1, a_2, \ldots, a_n$ 的最大公因子存在且所有的最大公因子都有 $r_1a_1 + r_2a_2 + \cdots + r_na_n$ 的形式，其中 $r_1, r_2, \ldots, r_n \in R$;    
    (iii) 若 $R$ 是唯一分解整环，则 $a_1, a_2, \ldots, a_n$ 的最大公因子存在.