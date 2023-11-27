# 多项式环上的分解

设 $R$ 是一环，则非零单项式 $ax_1^{k_1}x_2^{k_2}\cdots x_n^{k_n}$ 的**次数**(degree)是指非负整数 $k_1+k_2+\cdots +k_n$。若 $f$ 是 $R[x_1, \ldots, x_n]$ 上的非零多项式，则 $f = \sum_{i = 0}^n a_i x_1^{k_{i1}}\cdots x_n^{k_{in}}$，其**全次数**是诸单项式 $a_i x_1^{k_{i1}}\cdots x_n^{k_{in}}(a_i \neq 0)$ 次数的最大值。若 $f$ 均是由次数为 $k$ 的单项式组成的，则称 $f$ 为 **$k$ 次齐次多项式**。而考虑到 $R[x_1, \ldots, x_{k-1}, x_{k+1}, \ldots, x_n]$ 是 $R[x_1, \ldots, x_n]$ 的子环，将 $f$ 看作 $R[x_1, \ldots, x_{k-1}, x_{k+1}, \ldots, x_n]$ 上的一个未定元 $x_k$ 的多项式时，其次数叫做 **$f$ 对于 $x_k$ 的次数**.

!!! note "定理"
    设 $R$ 是环，$f, g \in R[x_1, \ldots, x_n]$，则  
    (i) $\mathrm{deg} (f+g) \leqslant \mathrm{max}(\mathrm{deg} f, \mathrm{deg} g)$;  
    (ii) $\mathrm{deg}(fg) \leqslant \mathrm{deg} f + \mathrm{deg} g$;  
    (iii) 若 $R$ 没有零因子，则 $\mathrm{deg} (f+g) = \mathrm{deg} f + \mathrm{deg} g$;  
    (iv) 若 $n = 1$，且 $f$ 或 $g$ 的首项系数不是 $R$ 中的零因子时，$\mathrm{deg} (fg) = \mathrm{deg} f + \mathrm{deg} g$.

!!! note "定理"
    （带余除法）设 $R$ 是一含幺环，$f, g \in R[x]$ 是非零多项式，且 $g$ 的首项系数是 $R$ 中的单位，则存在唯一确定的多项式 $q, r \in R[x]$ 使得

    $$
        f = qg + r, \mathrm{deg} r < \mathrm{deg} g.
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