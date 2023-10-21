# 群作用

!!! info "定义"
    群 $G$ **作用**在集合 $S$ 上，是指存在一函数 $G \times S \rightarrow S$（常被记作 $(g,x) \mapsto gx$），使得 $\forall x \in S, g_1, g_2 \in G$,

    $$
        ex = x, \enspace (g_1g_2)x = g_1(g_2x).
    $$

!!! example "示例"
    设 $H$ 是 $G$ 的一个子群，群 $H$ 在集合 $G$ 上有如下的这样一种作用：$(h, x) \mapsto hxh^{-1}$. 这种作用被称作**共轭**(conjugation)，元素 $hxh^{-1}$ 被称作 $x$ 的一个共轭. 若 $K$ 是 $G$ 的任意子群，$h \in H$, 则 $hKh^{-1}$ 是 $G$ 的一个同构于 $K$ 的子群，群 $hKh^{-1}$ 也称共轭于 $K$. 

!!! note "定理"
    设群 $G$ 有一作用于 $S$ 上，则：  
    (i) 在 $S$ 上，由  

    $$
        x \text{~} x' \Leftrightarrow gx = x' \enspace \text{for some} \enspace g \in G.
    $$ 

    定义的关系是等价关系.  
    (ii) 对任一 $x \in S$, $G_x = \{g \in G \mid gx = x\}$ 是 $G$ 的一个子群. 

以上定理中定义的等价关系被称作 $G$ 在 $S$ 上的**轨道**(orbit), 对 $x \in S$，其相应的轨道被记作 $\overline{x}$. 子群 $G_x$ 被称作 $x$ 的**稳定化子**(stabilizer)。

!!! example "示例"
    (i) 若子群 $H$ 共轭作用于 $G$ 上，那么稳定化子 $H_x = \{h \in H \mid hxh^{-1} = x\} = \{h \in H \mid hx = xh\}$ 被称作 $x$ 在 $H$ 中的**中心化子**(centralizer)，记作 $C_H(x)$, 如果 $H = G$, 则 $C_G(x)$ 简称为 $x$ 的中心化子。  
    (ii) 若 $H$ 共轭作用于 $G$ 的所有子群构成的集合 $S$ 上，则 $\{hKh^{-1} = K\}$ 被叫做 $K$ 在 $H$ 中的**正规化子**(normalizer)，记作 $N_H(K)$. 群 $N_G(K)$ 简称为 $K$ 的正规化子. 显然 $K$ 是 $N_G(K)$ 的正规子群, $K$ 是 $G$ 的正规子群等价于 $N_G(K) = G$.

!!! note "定理"
    若群 $G$ 作用在 $S$ 上，则 $x \in S$ 的轨道的基数是指标 $[G : G_x]$.

!!! success "推论"
    设 $G$ 是一个有限群，$K$ 是 $G$ 的一个子群.  
    (i) 对于 $x \in G$，其共轭类中的元素个数是 $[G : C_G(x)]$，且整除 $\lvert G \rvert$;  
    (ii) (class equation) 若 $\overline{x}_1, \overline{x}_2, \ldots, \overline{x}_n, x_i \in G$ 是 $G$ 的互异共轭类，则 

    $$
        \lvert G \rvert = \sum_{i = 1}^{n} [G : C_G(x_i)];
    $$

    (iii) $G$ 中共轭于 $K$ 的子群数目是 $[G : N_G(K)]$，且整除 $\lvert G \rvert$.

!!! note "定理"
    指定群作用 $G \times S \rightarrow S$ 诱导一群同态 $G \rightarrow A(S)$, $A(S)$ 是置换群. 

!!! success "推论"
    (i) (Cayley) 任何群 $G$ 都能嵌入为 $A(G)$ 的子群. 具体而言，对任意群 $G$，存在单态 $G \rightarrow A(G)$. 因此每个群都同构于一置换群，每个有限群都同构于 $S_n$ 的一个子群，$n = \lvert G \rvert$.  
    (ii) 设 $G$ 是一群，则  
        (a) 对任一 $g \in G$，经 $g$ 共轭后诱导一个 $G$ 的自同态.  
        (b) 存在群同态 $G \rightarrow Aut \ G$，其核为 $C(G) = \{g \in G \mid gx = xg, \forall x \in G\}$.

我们称 $g$ 诱导的这一同构为群 $G$ 的**内自同构**(inner automorphism)，$C(G)$ 被称为 $G$ 的**中心**(center). $g \in C(G)$ 等价于 $g$ 的等价类中仅包含 $g$ 这一个元素，所以若 $G$ 是有限的，且 $x \in C(G)$，则有 $[G : C_G(x)] = 1$. 进而，类方程可被改写为如下形式：

$$
    \lvert G \rvert = \lvert C(G) \rvert + \sum_{i = 1}^m [G : C_G(x_i)],
$$

其中 $\overline{x}_1, \overline{x}_2, \ldots, \overline{x}_m, x_i \in G - C(G)$ 是 $G$ 中互异的共轭类，且 $[G : C_G(x_i)] > 1$.

!!! success "命题"
    设 $H$ 是 $G$ 的一个子群，且 $G$ 在 $H$ 的全体左陪集构成的集合 $S$ 上进行左平移作用，则诱导同构 $G \rightarrow A(S)$ 的核包含在 $H$ 中. 

!!! success "推论"
    (i) 设 $H$ 是 $G$ 中指标为 $n$ 的子群，并且 $H$ 中不包含 $G$ 中的非平凡正规子群，那么 $G$ 同构于 $S_n$ 的某个子群.  
    (ii) 设 $H$ 是有限群 $G$ 中指标为 $p$ 的子群，$p$ 是能够整除 $G$ 的阶的最小素数，则 $H$ 是 $G$ 的正规子群. 