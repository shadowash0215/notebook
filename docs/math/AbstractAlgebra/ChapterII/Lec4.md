# 分式环 局部化

仿照从整数环构建有理数域的过程，我们也可以从环构建域。在此之前我们需要补充几个定义：

!!! info "定义"
    环 $R$ 的一个非空子集合 $S$ 被称为**乘性子集**(multiplicative subset)，若 $a, b \in S \Rightarrow ab \in S$.  

考虑有理数域，$\forall \alpha \in \mathbf{Q}, \exists a \in \mathbf{Z}, b \in S, \alpha = a/b$. 考虑 $\beta = c/d$，就有 $\alpha = \beta \Leftrightarrow a/b = c/d \Leftrightarrow ad = bc(ad - bc = 0)$. 所以有理数域其实可以通过 $\mathbf{Z} \times S$ 上的等价关系构建。此关系定义为：

$$
    (a, b) \textrm{~} (c, d) \Leftrightarrow ad - bc = 0.
$$

$\mathbf{Q}$ 就被定义为此等价关系下所有等价类的集合。元素 $(a, b)$ 的等价类记为 $a/b$ 且按照正常的数的加法和乘法定义，进而可验证这些运算都是良定义的，且 $\mathbf{Q}$ 是一个域。映射 $\varphi: \mathbf{Z} \rightarrow \mathbf{Q}$，定义为 $a \mapsto a/1$，显然是一个单同态，将 $\mathbf{Z}$ 嵌入了 $\mathbf{Q}$。

考虑仿照这种定义方式，我们将其运用在任意交换环 $R$ 的任意乘性子集 $S$ 上，最终目标是构建一个记号为 $S^{-1}R$ 的含幺交换环和群同态 $\varphi_S: R \rightarrow S^{-1}R$。且 $R$ 是整环的话，$S^{-1}R$ 就会成为一个域，且 $\varphi_S$ 将 $R$ 嵌入 $S^{-1}R$。

第一件事是拓展等价关系。

!!! info "定义"
    设 $S$ 是交换环 $R$ 的一个乘性子集。在 $R \times S$ 上定义如下关系：

    $$
        (r, s) \textrm{~} (r', s') \Leftrightarrow s_1(rs' - r's) = 0, \ \textrm{for some} \ s_1 \in S
    $$

    是一个等价关系。进一步，若 $R$ 没有零因子，且 $0 \not \in S$，此等价关系可增强为 

    $$
        (r, s) \textrm{~} (r', s') \Leftrightarrow rs' - r's = 0.
    $$

通过此等价关系，我们可以将 $(r, s) \in R \times S$ 所在的等价类记作 $r/s$. $R \times S$ 在关系 ~ 下的所有等价类构成的集合即记作 $S^{-1}R$，其满足以下三条性质：

!!! success "性质"
    (i) $r/s = r'/s' \Leftrightarrow s_1(rs' - r's) = 0, \ \textrm{for some} \ s_1 \in S$;  
    (ii) $tr/ts = r/s, \forall r \in R, s, t \in S$;  
    (iii) 若 $0 \in S$，则 $S^{-1}R$ 只含有一个等价类.

进而有以下定理：

!!! note "定理"
    设 $S$ 是交换环 $R$ 的乘性子集，$S^{-1}R$ 是如上定义的等价类集合，则  
    (i) $S^{-1}R$ 是含幺交换环，加法和乘法按照如下定义：

    $$
        r/s + r'/s' = (rs'+r's)/ss' \enspace \textrm{and} \enspace (r/s)(r'/s') = rr'/ss'.
    $$

    (ii) 若 $R$ 不是零环，且没有零因子，且 $0 \not \in S$，则 $S^{-1}R$ 是整环.   
    (iii) 若 $R$ 不是零环，且没有零因子，且 $S$ 是 $R$ 中全体非零元素构成的集合，则 $S^{-1}R$ 是域. 

所以我们得到 $S^{-1}R$ 实际上可以构成环，我们称其为**分式环**(ring of fractions)。而其中的特殊情况便是第(iii)条，此时称 $S^{-1}R$ 为整环 $R$ 上的**分式域**(quotient field of the integral domain $R$)。并且，如果 $S$ 是 $R$ 中所有非零因子的元素构成的且 $S$ 非空，此时 $S^{-1}R$ 被称为**全分式环**(complete ring of fractions)。

接下来轮到同态的构建，回忆 $\varphi: \mathbf{Z} \rightarrow \mathbf{Q}$, $n \mapsto n/1$，显然 $\varphi$ 是一个满同态，且将 $\mathbf{Z}$ 嵌入 $\mathbf{Q}$。但更进一步我们发现，$\forall n \neq 0, \varphi(n)$ 都是 $\mathbf{Q}$ 中的单位，仿照此性质，我们有如下定理：

!!! note "定理"
    设 $S$ 是交换环 $R$ 的一个乘性子集，则：  
    (i) 映射 $\varphi_S: R \rightarrow S^{-1}R$，定义为 $r \mapsto rs/s, \forall s \in S$，是一良定义的环同态，且任一 $s \in S$，$\varphi_S(s)$ 都是 $S^{-1}R$ 的一个单位.  
    (ii) 若 $0 \not \in S$ 且 $S$ 不含有零因子，则 $\varphi_S$ 是一个单同态. 特别地，所有整环都能被嵌入其分式域中.  
    (iii) 若 $R$ 是含幺环且 $S$ 全由单位组成，则 $\varphi_S$ 是一个环同构. 特别地，所有域 $F$ 的全分式环（事实上就是分式域）同构于 $F$.

下面描述分式环的泛性质：

!!! note "定理"
    设 $S$ 是交换环 $R$ 的乘性子集，$T$ 是任意含幺交换环. 若 $f: R \rightarrow T$ 是一环同态，且 $\forall s \in S, f(s)$ 是 $T$ 中的单位，则存在唯一的环同态 $\overline{f}: S^{-1}R \rightarrow T$ 使得 $\overline{f}\varphi_S = f$. 环 $S^{-1}R$ 在不计同构的情况下完全由此性质决定.

也就是说下图是交换的：

\tikzcd
    R \arrow[r, "f"] \arrow[d, "\varphi_S"swap] & T \\
    S^{-1}R \arrow[ru, "\overline{f}"swap]

!!! success "推论"
    设 $R$ 是一整环，并且将其视作其分式域 $F$ 的子环. 若 $E$ 为一域，且 $f: R \rightarrow E$ 是一环单态，则存在唯一的域单态 $\overline{f}: F \rightarrow E$，使得 $\overline{f} \mid R = f$. 特别地，每一个包含 $R$ 的域 $E_1$ 必包含一同构于 $F$ 的一个子域 $F_1$，使得 $R \subset F_1 \subset E_1$.

下面开始处理分式环的理想问题，但这些定理会隔很长时间才用得到，此处先写下。

!!! note "定理"
    设 $S$ 是交换环 $R$ 的乘性子集，则  
    (i) 若 $I$ 是 $R$ 的一个理想，则 $S^{-1}I = \{a/s \mid a \in I, s \in S\}$ 是 $S^{-1}R$ 的一个理想.  
    (ii) 若 $J$ 是 $R$ 的另一个理想，则 
    
    $$
        S^{-1}(I+J) = S^{-1}I + S^{-1}J;
    $$

    $$
        S^{-1}(IJ) = (S^{-1}I)(S^{-1}J);
    $$

    $$
        S^{-1}(I \cap J) = S^{-1}I \cap S^{-1}J.
    $$

$S^{-1}I$ 被称为理想 $I$ 在 $S^{-1}R$ 上的**扩展**(extension)

!!! note "定理"
    设 $S$ 是含幺交换环 $R$ 的乘性子集，$I$ 是 $R$ 的一个理想，则 $S^{-1}I = S^{-1}R$ 等价于 $S \cap I \neq \varnothing$