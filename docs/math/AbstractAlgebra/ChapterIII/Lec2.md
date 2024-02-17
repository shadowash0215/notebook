# 自由模和向量空间

本节研究自由模，其在数学领域中有着广泛的应用，而除环上的自由模就是向量空间。自由阿贝尔群也是自由模的一个特例。我们通过其作为一开始的参照。

仿照自由阿贝尔群的定义和性质，我们有如下定义：

!!! info "定义"
    $R$-模 $A$ 的子集合 $X$ 被称作**线性无关**(linearly independent)，如果对于任意两两不同的元素 $x_1, \dots, x_n \in X$ 和 $r_1, \dots, r_n \in R$，如果 $r_1 x_1 + \dots + r_n x_n = 0$，则 $r_1 = \dots = r_n = 0$. 不是线性无关的子集合被称作**线性相关**(linearly dependent)。如果 $A$ 作为 $R$-模由集合 $Y$ 生成，我们就称 $Y$ **张成**(span) $A$. 如果 $R$ 是含幺环，$A$ 是幺作用模，则 $Y$ 张成 $A$ 当且仅当 $A$ 中的每一个元素都可以写成 $Y$ 中元素的线性组合：$a = r_1 y_1 + \dots + r_n y_n$，其中 $r_1, \dots, r_n \in R$，$y_1, \dots, y_n \in Y$. $A$ 的一个线性无关子集合如果张成 $A$，则称其为 $A$ 的一个**基**(basis)。

!!! note "定理"
    设 $R$ 是含幺环，则关于幺作用 $R$-模 $F$ 的下列条件等价：  
    (i) $F$ 有一组非空的基；  
    (ii) $F$ 是一族循环 $R$-模的内直和，其中每个循环 $R$-模都同构于左 $R$-模 $R$；  
    (iii) 作为 $R$-模，$F$ 同构于若干左 $R$-模 $R$ 的直和；  
    (iv) 存在非空集合 $X$ 和函数 $\iota: X \rightarrow F$ 具有以下的性质：对于任意幺作用 $R$-模 $A$ 和函数 $f: X \rightarrow A$，存在唯一的 $R$-模同态 $\bar{f}: F \rightarrow A$ 使得 $\bar{f} \circ \iota = f$.

含幺环 $R$ 上的幺作用模 $F$ 如果满足如上的等价条件，就被称作集合 $X$ 上的**自由 $R$-模**(free $R$-module)。  

!!! success "推论"
    （含幺）环 $R$ 上的每个（幺作用）$R$-模都是一个自由 $R$-模的同态像. 如果 $A$ 是有限生成的，则 $F$ 也可被选取为有限生成的.

!!! success "引理"
    除环 $D$ 上向量空间 $V$ 的极大线性无关子集合是 $V$ 的一组基.

??? success "证明"
    设 $W$ 是由集合 $X$ 张成的 $V$ 的子空间. 因为 $X$ 是线性无关的并且张成 $W$，从而 $X$ 是 $W$ 的一组基. 如果 $W = V$，则证毕. 若不然，则存在非零元素 $a \in V, a \not \in W$. 考虑集合 $X \cup \{a\}$. 如果 $ra + r_1x_1 + \dots + r_nx_n = 0$，其中 $r, r_1, \dots, r_n \in D$，$x_1, \dots, x_n \in X$. 若 $r \neq 0$,则 $a = r^{-1}(ra) = -r^{-1}(r_1x_1 + \dots + r_nx_n) \in W$，矛盾. 所以 $r = 0$，从而 $r_1x_1 + \dots + r_nx_n = 0$. 因为 $X$ 是线性无关的，从而 $r_1 = \dots = r_n = 0$. 从而 $X \cup \{a\}$ 也是线性无关的. 与 $X$ 是极大线性无关子集合矛盾. 所以 $V = W$.  

!!! note "定理"
    (i) 除环 $D$ 上的每个向量空间 $V$ 都有基，即都是自由 $R$-模. 更一般的，$V$ 的每个线性无关子集合都包含在 $V$ 的一组基中.  
    (ii) 如果 $V$ 是除环 $D$ 上的向量空间，$X$ 是 $V$ 的子集合并且张成 $V$，则 $X$ 包含 $V$ 的一组基.

!!! note "定理"
    (i) 设 $R$ 为含幺环. $F$ 是自由 $R$-模并且具有一组无限的基 $X$，则 $F$ 的每一组基都与 $X$ 等势.  
    (ii) 如果 $V$ 是除环 $D$ 上的向量空间，则 $V$ 的任意两组基有相同的势.

!!! info "定义"
    设 $R$ 是含幺环，如果对于每个自由 $R$-模 $F$，$F$ 的任意两组基均具有同样的势，我们便称 $R$ 具有**不变维数性质**(invariant dimension property). $F$ 的任意一组基的势被称作 $F$ 在 $R$ 上的**维数**(dimension)或者 $F$ 的**秩**(rank).

除环 $D$ 上的向量空间 $V$ 的维数表示为 $\operatorname{dim}_D V$。
 
!!! success "命题"
    设 $E$ 和 $F$ 均是环 $R$ 上的自由模，而且 $R$ 具有不变维数性质. 则 $E \cong F$ 等价于 $E$ 和 $F$ 有相同的秩.

!!! success "引理"
    设 $R$ 是含幺环，$I(\neq R)$ 是 $R$ 的理想，$F$ 是自由 $R$-模，$X$ 是 $F$ 的一组基. $\pi: F \rightarrow F/IF$ 是典范满射. 则 $F/IF$ 是自由 $R/I$-模，$\pi(x)$ 是 $F/IF$ 的一组基. 并且 $\lvert X \rvert = \lvert \pi(X) \rvert$. (回忆：$IF = \{\sum_{i = 1}^n r_ia_i \mid r_i \in I, a_i \in F, n \in N^*\}$, $R/I$ 在 $F/IF$ 上的作用为 $(r + I)(a + IF) = ra + IF$)

!!! success "命题"
    如果 $f: R \rightarrow S$ 是含幺环的非零满同态，并且 $S$ 具有不变维数性质，则 $R$ 也具有不变维数性质.  

!!! success "推论"
    如果 $R$ 是一个以除环作为同态像的含幺环，则 $R$ 具有不变维数性质. 特别地，每一个含幺交换环具有不变维数性质.  

现在视角转回除环 $D$ 上的向量空间，研究其维数性质。除环上的向量空间 $V$ 被称作**有限维**(finite-dimensional)，如果 $\operatorname{dim}_D V$ 是有限的。

!!! note "定理"
    设 $W$ 是除环 $D$ 上的向量空间 $V$ 的子空间. 则  
    (i) $\operatorname{dim}_D W \leqslant \operatorname{dim}_D V$;  
    (ii) 如果 $\operatorname{dim}_D W = \operatorname{dim}_D V$，且 $\operatorname{dim}_D V$ 是有限的，则 $W = V$;  
    (iii) $\operatorname{dim}_D V = \operatorname{dim}_D W + \operatorname{dim}_D V/W$.

!!! note "定理"
    如果 $f: V \rightarrow V'$ 是除环 $D$ 上向量空间之间的线性变换，则存在 $V$ 的一组基 $X$，使得 $X \cap \operatorname{Ker} f$ 是 $\operatorname{Ker} f$ 的一组基，并且 $\{f(x) \mid f(x) \neq 0, x \in X\}$ 是 $\operatorname{Im} f$ 的一组基. 特别地，  

    \[
        \operatorname{dim}_D V = \operatorname{dim}_D \operatorname{Ker} f + \operatorname{dim}_D \operatorname{Im} f.
    \]

!!! success "推论"
    设 $V$ 和 $W$ 均是除环 $D$ 上某个向量空间的有限维子空间，则  

    \[
        \operatorname{dim}_D V + \operatorname{dim}_D W = \operatorname{dim}_D (V + W) + \operatorname{dim}_D (V \cap W).
    \]

!!! note "定理"
    设 $R, S, T$ 均是除环，并且 $R \subset S \subset T$. 则有 $\operatorname{dim}_R T = \operatorname{dim}_R S + \operatorname{dim}_S T$. 此外，$\operatorname{dim}_R T$ 是有限的当且仅当 $\operatorname{dim}_R S$ 和 $\operatorname{dim}_S T$ 均是有限的.