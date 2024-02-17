# 群作用

!!! info "定义"
    群 $G$ **作用**在集合 $S$ 上，是指存在一函数 $G \times S \rightarrow S$（常被记作 $(g,x) \mapsto gx$），使得 $\forall x \in S, g_1, g_2 \in G$,

    $$
        ex = x, \enspace (g_1g_2)x = g_1(g_2x).
    $$

!!! example "示例"
    设 $H$ 是 $G$ 的一个子群，群 $H$ 在集合 $G$ 上有如下的这样一种作用：$(h, x) \mapsto hxh^{-1}$. 这种作用被称作**共轭**(conjugation)，元素 $hxh^{-1}$ 被称作 $x$ 的一个共轭. 若 $K$ 是 $G$ 的任意子群，$h \in H$, 则 $hKh^{-1}$ 是 $G$ 的一个同构于 $K$ 的子群，群 $hKh^{-1}$ 也称共轭于 $K$. 

我们可以看一下共轭作用在对称群上的作用。

!!! example "示例"
    考虑 $S_5$ 上的置换 $\sigma  = (1345), \tau = (125)$，$\tau \sigma \tau^{-1} = (125)(1345)(521) = (2341)$，会发现置换上的共轭作用实际上进行了某种替换的作用，即 $\tau(i_1i_2\cdots i_r)\tau^{-1} = (\tau(i_1)\tau(i_2)\cdots \tau(i_r))$. 

在此基础上我们便可以分析 $S_n$ 的生成元. 

!!! note "定理"
    ($S_n$ 的生成元) (i) $S_n$ 可以由 $\{(1 \ 2), (1 \ 3), \ldots ,(1 \ n)\}$ 生成；  
    (ii) $S_n$ 可以由 $\{(1 \ 2), (2 \ 3), \ldots, (n-1 \ n)\}$ 生成；  
    (iii) $S_n$ 可以由 $\{(1 \ 2 \ 3 \cdots \ n), (1 \ 2)\}$ 生成.

!!! note "定理"
    设群 $G$ 有一作用于 $S$ 上，则：  
    (i) 在 $S$ 上，由  

    $$
        x \text{~} x' \Leftrightarrow gx = x' \enspace \text{for some} \enspace g \in G.
    $$ 

    定义的关系是等价关系.  
    (ii) 对任一 $x \in S$, $G_x = \{g \in G \mid gx = x\}$ 是 $G$ 的一个子群. 

以上定理中定义的等价关系被称作 $G$ 在 $S$ 上的**轨道**(orbit), 对 $x \in S$，其相应的轨道被记作 $\bar{x}$. 子群 $G_x$ 被称作 $x$ 的**稳定化子**(stabilizer)。事实上，轨道代表元素 $x$ 在集合 $G$ 的作用下能到达的位置，稳定化子则是对于任意 $S$ 中的元素 $x$，$g \in G$ 都不会将其改变，这是横向与纵向的区别。

!!! example "示例"
    (i) 若子群 $H$ 共轭作用于 $G$ 上，那么稳定化子 $H_x = \{h \in H \mid hxh^{-1} = x\} = \{h \in H \mid hx = xh\}$ 被称作 $x$ 在 $H$ 中的**中心化子**(centralizer)，记作 $C_H(x)$, 如果 $H = G$, 则 $C_G(x)$ 简称为 $x$ 的中心化子。  
    (ii) 若 $H$ 共轭作用于 $G$ 的所有子群构成的集合 $S$ 上，则 $\{h \in H \mid hKh^{-1} = K\}$ 被叫做 $K$ 在 $H$ 中的**正规化子**(normalizer)，记作 $N_H(K)$. 群 $N_G(K)$ 简称为 $K$ 的正规化子. 显然 $K$ 是 $N_G(K)$ 的正规子群, $K$ 是 $G$ 的正规子群等价于 $N_G(K) = G$.

!!! note "定理"
    若群 $G$ 作用在 $S$ 上，则 $x \in S$ 的轨道的基数是指标 $[G : G_x]$.

??? note "证明"
    设 $g, h \in G$. 若 $gx = hx$，则有 

    $$
        gx = hx \Leftrightarrow g^{-1}hx = x \Leftrightarrow g^{-1}h \in G_x \Leftrightarrow gG_x = hG_x. 
    $$

    所以由 $gG_x \mapsto gx$ 给出的映射可定义出 $G_x$ 在 $G$ 中的全体陪集构成的集合与轨道 $\bar{x} = \{gx \mid g \in G\}$ 上的元素建立了一一对应，所以 $\lvert \bar{x} \rvert = [G: G_x]$.

!!! success "推论"
    设 $G$ 是一个有限群，$K$ 是 $G$ 的一个子群.  
    (i) 对于 $x \in G$，其共轭类中的元素个数是 $[G : C_G(x)]$，且整除 $\lvert G \rvert$;  
    (ii) (class equation) 若 $\bar{x}_1, \bar{x}_2, \ldots, \bar{x}_n, x_i \in G$ 是 $G$ 的互异共轭类，则 

    $$
        \lvert G \rvert = \sum_{i = 1}^{n} [G : C_G(x_i)];
    $$

    (iii) $G$ 中共轭于 $K$ 的子群数目是 $[G : N_G(K)]$，且整除 $\lvert G \rvert$.

!!! note "定理"
    指定群作用 $G \times S \rightarrow S$ 诱导一群同态 $G \rightarrow A(S)$, $A(S)$ 是由 $S$ 的全体置换构成的群. 

??? note "证明"
    若 $g \in G$，则定义 $\tau_g: S \rightarrow S$，$x \mapsto gx$. 因为 $x = g(g^{-1}x)$，所以 $\tau_g$ 是满射. 同理，若 $gx = gy(x, y \in S)$，则 $x = g^{-1}(gx) = g^{-1}(gy) = y$，所以 $\tau_g$ 是单射，进而是双射，也就是 $S$ 的一个置换. 而 $\forall g, g' \in G, \tau_{gg'} = \tau_g\tau_{g'}: S \rightarrow S$，所以映射 $\tau: G \rightarrow A(S)$, $g \mapsto \tau_g$ 是一群同态.

!!! success "推论"
    (i) (Cayley) 任何群 $G$ 都能嵌入为 $A(G)$ 的子群. 具体而言，对任意群 $G$，存在单态 $G \rightarrow A(G)$. 因此每个群都同构于一置换群，每个有限群都同构于 $S_n$ 的一个子群，$n = \lvert G \rvert$.  
    (ii) 设 $G$ 是一群，则  
        (a) 对任一 $g \in G$，经 $g$ 共轭后诱导一个 $G$ 的自同态.  
        (b) 存在群同态 $G \rightarrow Aut \ G$，其核为 $C(G) = \{g \in G \mid gx = xg, \forall x \in G\}$.

我们称 $g$ 诱导的这一同构为群 $G$ 的**内自同构**(inner automorphism)，$C(G)$ 被称为 $G$ 的**中心**(center). $g \in C(G)$ 等价于 $g$ 的共轭类中仅包含 $g$ 这一个元素，所以若 $G$ 是有限的，且 $x \in C(G)$，则有 $[G : C_G(x)] = 1$. 进而，类方程可被改写为如下形式：

$$
    \lvert G \rvert = \lvert C(G) \rvert + \sum_{i = 1}^m [G : C_G(x_i)],
$$

其中 $\bar{x}_1, \bar{x}_2, \ldots, \bar{x}_m, x_i \in G - C(G)$ 是 $G$ 中互异的共轭类，且 $[G : C_G(x_i)] > 1$.

!!! success "推论"
    (i) 设 $H$ 是 $G$ 的一个子群，且 $G$ 在 $H$ 的全体左陪集构成的集合 $S$ 上进行左平移作用，则诱导同构 $G \rightarrow A(S)$ 的核包含在 $H$ 中.  
    (ii) 设 $H$ 是 $G$ 中指标为 $n$ 的子群，并且 $H$ 中不包含 $G$ 中的非平凡正规子群，那么 $G$ 同构于 $S_n$ 的某个子群.  
    (iii) 设 $H$ 是有限群 $G$ 中指标为 $p$ 的子群，$p$ 是 $\lvert G \rvert$ 的最小素因子，则 $H$ 是 $G$ 的正规子群. 

??? success "证明"
    (i) 诱导同构 $\tau: G \rightarrow A(S)$ 由 $g \mapsto \tau_g$ 给出. 而 $\tau_g: S \rightarrow S$，$\tau_g(xH) = gxH$. 若 $g \in \ker \tau$，有 $\tau_g = 1_S$，进而 $\forall x \in G, gxH = xH$. 特别地，当 $x = e$ 时，$geH = eH = H$，所以 $g \in H$.  
    (ii) $\tau: G \rightarrow A(S)$, $\ker \tau$ 是 $G$ 的正规子群，且由 (i) 知其包含在 $H$ 中，所以 $\ker \tau = \langle e \rangle$，$G \rightarrow A(S)$ 是单同态. 因此 $G$ 同构于 $H$ 的 $n$ 个左陪集上的置换群的某个子群（这是单同态保证的），而 $H$ 的 $n$ 个左陪集上的置换群显然同构于 $S_n$.  
    (iii) 设 $S$ 是 $H$ 在 $G$ 中的全体左陪集构成的集合. 因为 $[G : H] = p$，故 $A(S) \cong S_p$. 设 $K$ 是同态 $\tau: G \rightarrow A(S)$ 的核，则 $K$ 在 $G$ 中正规且包含在 $H$ 中，且 $G/K$ 同构于 $S_p$ 的某个子群（事实上，应该同构于 $\operatorname{\mathrm{Im}} \tau$）. 所以 $\lvert G/K \rvert = [G : K] \mid \lvert S_p \rvert = p!$. 而 $[G : K]$ 的每个因子一定整除 $\lvert G \rvert(\lvert G \rvert = \lvert K \rvert [G : K])$. 但除 $1$ 之外没有比 $p$ 更小的整除 $\lvert G \rvert$ 的数，故 $[G : K] = p$ 或 $[G : K] = 1$. 而 $[G : K] = [G: H][H : K] = p[H : K] \geqslant p$，所以 $[G : K] = p, [H : K] = 1$，也就有 $H = K$. 考虑到 $K \triangleleft G,$ 所以 $H \triangleleft G$.