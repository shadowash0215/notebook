# 多项式环上的分解

设 $R$ 是一环，则非零单项式 $ax_1^{k_1}x_2^{k_2}\cdots x_n^{k_n}$ 的**次数**(degree)是指非负整数 $k_1+k_2+\cdots +k_n$。若 $f$ 是 $R[x_1, \ldots, x_n]$ 上的非零多项式，则 $f = \sum_{i = 0}^n a_i x_1^{k_{i1}}\cdots x_n^{k_{in}}$，其**全次数**是诸单项式 $a_i x_1^{k_{i1}}\cdots x_n^{k_{in}}(a_i \neq 0)$ 次数的最大值。若 $f$ 均是由次数为 $k$ 的单项式组成的，则称 $f$ 为 **$k$ 次齐次多项式**。而考虑到 $R[x_1, \ldots, x_{k-1}, x_{k+1}, \ldots, x_n]$ 是 $R[x_1, \ldots, x_n]$ 的子环，将 $f$ 看作 $R[x_1, \ldots, x_{k-1}, x_{k+1}, \ldots, x_n]$ 上的一个未定元 $x_k$ 的多项式时，其次数叫做 **$f$ 对于 $x_k$ 的次数**.

!!! note "定理"
    设 $R$ 是环，$f, g \in R[x_1, \ldots, x_n]$，则  
    (i) $\operatorname{\mathrm{deg}} (f+g) \leqslant \mathrm{max}(\operatorname{\mathrm{deg}} f, \operatorname{\mathrm{deg}} g)$;  
    (ii) $\operatorname{\mathrm{deg}}(fg) \leqslant \operatorname{\mathrm{deg}} f + \operatorname{\mathrm{deg}} g$;  
    (iii) 若 $R$ 没有零因子，则 $\operatorname{\mathrm{deg}} (f+g) = \operatorname{\mathrm{deg}} f + \operatorname{\mathrm{deg}} g$;  
    (iv) 若 $n = 1$，且 $f$ 或 $g$ 的首项系数不是 $R$ 中的零因子时，$\operatorname{\mathrm{deg}} (fg) = \operatorname{\mathrm{deg}} f + \operatorname{\mathrm{deg}} g$.

!!! note "定理"
    （带余除法）设 $R$ 是一含幺环，$f, g \in R[x]$ 是非零多项式，且 $g$ 的首项系数是 $R$ 中的单位，则存在唯一确定的多项式 $q, r \in R[x]$ 使得

    $$
        f = qg + r, \operatorname{\mathrm{deg}} r < \operatorname{\mathrm{deg}} g.
    $$

    （余数定理）设 $R$ 是一含幺环，且有

    $$
        f(x) = \sum_{i=0}^n a_ix^i \in R[x],
    $$

    则对任意的 $c \in R$，存在唯一的 $q(x) \in R[x]$ 使得 $f(x) = q(x)(x-c)+f(c)$.  

!!! success "推论"
    若 $F$ 是域，则 $F[x]$ 是欧几里得整环，从而 $F[x]$ 是主理想整环和唯一分解整环，$F[x]$ 中的单位恰是其中全部非零常数.

!!! info "定义"
    设 $R$ 是交换环 $S$ 的子环，$f = \sum_{i=0}^m a_ix_1^{k_{i1}}\cdots x_n^{k_{in}} \in R[x_1, \ldots, x_n]$ 是一多项式，若 $c_1, \ldots, c_n \in S$ 使得 $f(c_1, \ldots, c_n) = 0$，则称 $(c_1, \ldots, c_n)$ 为 $f$ 的**根**(root)或**零点**(zero)，或者叫多项式方程 $f(x_1, \ldots, x_n) = 0$ 的一个**解**(solution).

!!! note "定理"
    (i) 设 $R$ 是含幺交换环，$f \in R[x]$，则 $c \in R$ 是 $f$ 的根等价于 $x - c$ 可以整除 $f$.  
    (ii) 若 $D$ 是整环，并且包含在整环 $E$ 中，而 $f \in D[x]$ 的次数为 $n$，则 $f$ 在 $E$ 中至多有 $n$ 个不同的根.

在唯一分解整环上我们有如下的求解多项式的根的方法。

!!! note "定理"
    设 $D$ 是唯一分解整环，其分式域为 $F$，令 $f = \sum_{i = 0}^n a_ix^i \in D[x]$. 如果 $u = c/d \in F$，$c, d \in D$，$c, d$ 互素，且 $u$ 是 $f$ 的根，则 $c \mid a_0$，同时 $d \mid a_n$.

!!! example "示例"
    设 $f = x^4 - 2x^3 - 7x^2 - \frac{11}{3}x - \frac{4}{3} \in \mathbb{Q}[x]$，则 $f$ 与 $3f = 3x^4 - 6x^3 - 21x^2 - 11x - 4 \in \mathbb{Z}[x]$ 在 $\mathbb{Q}$ 中有相同的根. 由上可知，$c \mid a_0 = -4$，$d \mid a_n = 3$，因此 $3f$ 只可能有如下的有理根 $u = \pm 1, \pm 2, \pm 4, \pm \frac{1}{3}, \pm \frac{2}{3}, \pm \frac{4}{3}$. 代入验证可知只有 $u = 4$ 是 $3f$ 的根，因此 $f$ 的有理根只可能是 $u = 4$.  

设 $D$ 为整环，$f \in D[x]$。若 $c \in D$ 是 $f$ 的根，则重复利用上述定理，可知存在最大整数 $m(0 \leqslant m \leqslant \operatorname{\mathrm{deg}} f)$，使得 $f(x) = (x - c)^mg(x)$，其中 $g(x) \in D[x]$ 且 $(x - c) \not \mid g(x)$，也就是说 $g(c) \neq 0$。整数 $m$ 被称作 $f$ 的**根 $c$ 的重数**(multiplicity of the root c)。如果 $c$ 的重数为 1，则 $c$ 被称作**单根**(simple root)。如果 $c$ 的重数大于 1，则 $c$ 被称作**重根**(multiple root)。下面引入新的运算来决定多项式是否有重根。

!!! note "定理"
    设 $D$ 是整环，$f = \sum_{i = 1}^n a_ix^i \in D[x]$. 令 $f' \in D[x]$ 是多项式 $f' = \sum_{k = 1}^n ka_kx^{k - 1} = a_1 + 2a_2x + \cdots + na_nx^{n - 1}$，则对所有 $f, g \in D[x]$ 和 $c \in D$，有  
    (i) $(cf)' = cf'$;  
    (ii) $(f + g)' = f' + g'$;  
    (iii) $(fg)' = f'g + fg'$;  
    (iv) $(g^n)' = ng^{n - 1}g'$.  

多项式 $f'$ 被称为**形式微商**(formal derivative)。称之为形式是因为其不涉及有关极限的定义。

回忆整环中不可约元的定义，对多项式环而言，若非零多项式 $f \in R[x]$ 是**不可约的**(irreducible)，则 $f$ 不是单位，且对于每个分解式 $f = gh$，$g$ 或 $h$ 至少有一个是 $R[x]$ 的单位。  

!!! note "定理"
    设 $D$ 是整环，且是整环 $E$ 的子环，令 $f \in D[x]$，$c \in E$，则  
    (i) $c$ 是 $f$ 的重根等价于 $f(c) = 0$ 且 $f'(c) = 0$；  
    (ii) 若 $D$ 是域且 $f$ 和 $f'$ 互素，则 $f$ 在 $E$ 中没有重根；  
    (iii) 若 $D$ 是域，$f$ 在 $D[x]$ 中不可约，而 $E$ 包含 $f$ 的一个根，则 $f$ 在 $E$ 中无重根等价于 $f' \neq 0$.

接下来就要决定多项式环 $D[x]$($D$ 是整环)中的单位和不可约元了，我们有如下定理作为支撑。  

!!! note "定理"
    (i) $D[x]$ 中的单位恰好是常系数多项式，且这些常数必须是 $D$ 中的单位；  
    (ii) 若 $c \in D$ 且 $c$ 在 $D$ 中不可约，则常数多项式 $c$ 在 $D[x]$ 中也不可约；  
    (iii) 若一次多项式的首项系数是 $D$ 中的单位，则其在 $D[x]$ 中是不可约的，特别地，域上的每个一次多项式都不可约；  
    (iv) 假设 $D$ 是整环 $E$ 的子环并且 $f \in D[x] \subset E[x]$ 则 $f$ 可能在 $E[x]$ 中不可约但在 $D[x]$ 中可约，也可能在 $D[x]$ 中不可约但在 $E[x]$ 中可约.

设 $D$ 是唯一分解整环，$f = \sum_{i = 0}^n a_ix^i \in D[x]$，则 $f$ 的**容度**(content)是 $f$ 的系数的最大公因子，记作 $\mathrm{C}(f)$，其在相伴意义下是唯一的。记 $a, b$ 相伴为 $a \approx b$，则 $\approx$ 是 $D$ 上的等价关系。因为 $D$ 是整环，所以 $a \approx b \Leftrightarrow a = bu$，其中 $u$ 是 $D$ 中单位。若 $a \in D$ 且 $f \in D[x]$，则有 $C(af) \approx aC(f)$。而若 $f \in D[x]$ 且 $C(f)$ 是 $D$ 中单位，则称 $f$ 为**本原多项式**(primitive polynomial)。显然，对每个多项式 $g \in D[x]$，存在本原多项式 $f \in D[x]$ 使得 $g = \mathrm{C}(g)f$。

!!! note "定理"
    (Gauss) 若 $D$ 是唯一分解整环且 $f, g \in D[x]$，则 $C(fg) \approx C(f)C(g)$. 特别地，本原多项式的乘积仍是本原多项式.

??? note "证明"
    设 $f = C(f)f_1, g = C(g)g_1$，$f_1, g_1$ 是本原多项式，则 $C(fg) = C(C(f)f_1C(g)g_1) \approx C(f)C(g)C(f_1g_1)$. 从而我们只要证明 $f_1g_1$ 是本原多项式，也就是 $C(f_1g_1)$ 是单位即可. 设 $f_1 = \sum_{i = 0}^n a_ix^i, g_1 = \sum_{j = 0}^m b_jx^j$，则 $f_1g_1 = \sum_{k = 0}^{n + m} c_kx^k$，其中 $c_k = \sum_{i + j = k} a_ib_j$. 若 $f_1g_1$ 不是本原多项式，则 $D$ 中存在不可约元 $p$，使得 $p \mid c_k, \forall k$. 因为 $C(f_1)$ 是单位，所以 $p \not \mid C(f_1)$，从而存在整数 $s$，使得 $p \mid a_i, i < s$，但 $p \not \mid a_s$. 类似地，存在整数 $t$，使得 $p \mid b_j, j < t$，但 $p \not \mid b_t$. 于是 $p \mid c_{s + t} = a_0b_{s +t} + \cdots + a_{s - 1}b_{t + 1} + a_sb_t + a_{s + 1}b_{t - 1} + \cdots +a_{s + t}b_0$，所以 $p \mid a_sb_t$，但 $D$ 中的不可约元是素元，从而有 $p \mid a_s$ 或 $p \mid b_t$，矛盾. 所以 $f_1g_1$ 是本原多项式，即 $C(fg) \approx C(f)C(g)$.

下面两条引理是关于本原多项式在分式域上的刻画。

!!! success "引理"
    (i) 设 $D$ 是唯一分解整环，其分式域为 $F$. 设 $f, g$ 是 $D[x]$ 中的本原多项式，则 $f, g$ 在 $D[x]$ 中相伴等价于 $f, g$ 在 $F[x]$ 中相伴.  
    (ii) 设 $D$ 是唯一分解整环，其分式域为 $F$，$f \in D[x]$ 是正次数的本原多项式，则 $f$ 在 $D[x]$ 中不可约等价于 $f$ 在 $F[x]$ 中不可约.  

然后来到了我们的最终定理和判别法。

!!! note "定理"
    (i) 若 $D$ 是唯一分解整环，则多项式环 $D[x_1, \ldots, x_n]$ 也是唯一分解整环.  
    (ii) (Eisenstein's Criterion) 设 $D$ 是唯一分解整环，分式域为 $F$. 若 $f = \sum_{i = 0}^n a_ix^i \in D[x]$，$\operatorname{\mathrm{deg}} \geqslant 1$，且 $p$ 是 $D$ 中的不可约元，使得 $p \not \mid a_n, p \mid a_i(0 \leqslant i \leqslant n-1), p^2 \not \mid a_0$，则 $f$ 在 $F[x]$ 中不可约. 若 $f$ 是本原的，则 $f$ 在 $D[x]$ 中不可约.