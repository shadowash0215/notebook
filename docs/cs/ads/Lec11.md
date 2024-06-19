# 近似算法

整体而言，我们对一个最优化问题的算法有如下三个期望：  
1. 算法要能找到确切的最优解（optimality）；  
2. 算法能高效（通常是多项式时间）运行（efficiency）；  
3. 算法是通用的，能够解决所有问题（all instances）。

对于 $\mathsf{NP}$ 完全问题，我们目前无法同时做到以上三点，除非 $\mathsf{P} = \mathsf{NP}$。因此，我们需要退而求其次。如果我们选择舍弃第一个期望，但能保证高效找到的解是和真正的最优解 “相差不大” 的，那么我们称这类算法为近似算法。

!!! info "Definition"
    假设有某类问题 $\mathcal{I}$（例如背包问题），其中的一个具体实例记为 $I$ （当背包问题的参数给定的时候即为一个实例），且有一个复杂度为多项式的近似算法 $A$. 定义：  
    - $A(I)$ 为算法 $A$ 在实例 $I$ 上得到的解；  
    - $OPT(I)$ 为实例 $I$ 的最优解.  
    考虑 $\mathcal{I}$ 是最小化问题，若存在 $r \geqslant 1$，使得对于任意实例 $I$ 有：  

    \[
        A(I) \leqslant r \cdot OPT(I)
    \]

    那么称 $A$ 为该问题的 $r \text{-}$ 近似算法。我们特别关心其中可以取到的最小 $r$，称  
    
    \[
        \rho = \operatorname{inf} \{ r \mid A(I) \leqslant r \cdot OPT(I), \forall I \}
    \]

    为近似比（approximation ratio，即算法 $A$ 最紧的近似界）. 它可以等价定义为：

    \[
        \rho = \sup_{I} \frac{A(I)}{OPT(I)}, 
    \]

    即这一比值最大的实例对应的比值就是最紧的界。反之，如果是极大化问题，那么上式应该改为

    \[
        \rho = \sup_{I} \frac{OPT(I)}{A(I)}.
    \]

    将两者合并，我们可以统一为

    \[
        \rho = \sup_{I} \left\{ \frac{A(I)}{OPT(I)}, \frac{OPT(I)}{A(I)} \right\}.
    \]

有时候近似比也可能与输入规模有关，但大部分情况下我们看到的结果都是常数的，所以一般而言我们的定义都是常数。

给定一类问题 $\mathcal{I}$ 和算法 $A$，事实上我们很难根据定义求出 $A$ 的近似比，因为 $OPT(I)$ 一般未知。因此，只能通过 $OPT(I)$ 的范围来确定近似比。以最小化问题为例，确定近似比需要以下两个步骤：  
1.  首先寻找一个 $r \geqslant 1$，对于任何实例 $I$ ，都有 $A(I) \leqslant r \cdot OPT(I)$（可以首先寻找到 $OPT(I)$ 的一个下界 $LB(I) \leqslant OPT(I)$，然后让 $A(I) \leqslant r \cdot LB(I)$ 即可）；  
2. 接下来证明 $r$ 是不可改进的，即对任意的 $\varepsilon > 0$，都存在一个实例 $I_{\varepsilon}$，使得 $A(I_{\varepsilon}) \geqslant (r - \varepsilon) \cdot OPT(I_{\varepsilon})$.

接下来我们给出一些近似算法的分类，设 $\lvert I \rvert$ 为实例 $I$ 的规模，而 $f$ 是一个可计算（computable）函数，但不一定为多项式函数，那么有  
1. PTAS（多项式时间近似方案，Polynomial time approximation scheme）：存在算法 $A$，对于任意 $\varepsilon > 0$，有 

\[
    A(I) \leqslant (1 + \varepsilon) \cdot OPT(I),  
\]
    
且算法 $A$ 的运行时间以问题规模 $\lvert I \rvert$ 的多项式为上界，则称 $A$ 是该问题类的一个 PTAS。  
理论上 $A$ 在多项式时间内可以无限近似；不过对于不同的 $\varepsilon$，$A$ 的运行时间上界可能不同。例如 $A$ 可能是一个 $O(\lvert I \rvert^{1/\varepsilon})$ 乃至 $O(\lvert I \rvert^{\operatorname{exp}(1/\varepsilon)})$ 的算法，此时的算法表现就会非常糟糕。一般可以将 PTAS 的时间复杂度表示为 $O(\lvert I \rvert^{f(1/\varepsilon)})$，其中 $f$ 是一个函数。  
2. EPTAS（Efficient PTAS）：在 PTAS 的基础上，要求算法 $A$ 的复杂度是 $O(\lvert I \rvert^c)$，其中 $c \geqslant 0$ 是与 $\varepsilon$ 无关的常数。可以将 EPTAS 的时间复杂度表示为 $\lvert I \rvert^{O(1)}f(1/\varepsilon)$。  
3. FPTAS（Fully PTAS）：在 PTAS 的基础上，要求算法 $A$ 的运行时间关于 $\lvert I \rvert$ 和 $\varepsilon$ 都是多项式的。可以将 FPTAS 的时间复杂度表示为 $\lvert I \rvert^{O(1)}(1/\varepsilon)^{O(1)}$。

## 一维装箱问题

经典的（一维）装箱问题具体描述为：给定若干个带有尺寸的物品，要求将所有物品放入容量给定的箱子中，使得每个箱子中的物品尺寸之和不超过箱子容量并使所用的箱子数目最少。标准化后的描述为：给定 $n$ 个尺寸在 $(0, 1]$ 内的物品 $a_1, a_2, \ldots, a_n$，目标是使用数量尽可能少的单位容量箱子装下所有物品，每个箱子中物品尺寸和都不超过 1。

!!! note "Theorem"
    给定若干个物品，判断它们是否可由两个箱子装下是 $\mathsf{NP}$ 完全问题。

!!! note "Theorem"
    除非 $\mathsf{P} = \mathsf{NP}$，否则装箱算法不存在多项式算法有小于 $dfrac{3}{2}$ 的绝对近似比。

在装箱问题中，我们一般不关心全部的实例，而关心 $OPT(I)$ 较大的那些实例。因此定义 “渐近近似比（asymptotic approximation ratio）” 如下：  

!!! info "Definition"
    如果对任意常数 $\alpha \geqslant 1$，对任意实例 $I$ ，存在一个常数 $k$，满足  

    \[
        A(I) \leqslant \alpha \cdot OPT(I) + k.
    \]

    称所有满足上式的 $\alpha$ 的下确界为 $A$ 的渐近近似比.
    ??? tip
        $k$ 除了可以是某些固定的常数，也可以是 $o(OPT(I))$，只需要在 $OPT(I)$ 充分大时 $k/OPT(I) \to 0$ 即可。

此外，还有“在线”和“离线”的概念需要区分。若初始时物品信息并不全部给出，需要我们即时安排，而我们对未到达物品信息一无所知，同时做出的决定无法更改，此时称为在线（online）问题；若所有的物品信息在开始装箱前已知，则它是离线（offline）问题。

在线算法有以下几种：  
=== "Next Fit"

    每次将物品放入当前箱子，如果放不下则开新箱子；  

    ```c
    void NextFit ( )
    {   
        read item1;
        while ( read item2 ) {
            if ( item2 can be packed in the same bin as item1 ) {
                place item2 in the bin;
            } else {
                create a new bin for item2;
                item1 = item2;
            }
        } /* end-while */
    }
    ```

=== "First Fit"

    每次将物品放入第一个能放下的箱子，如果放不下则开新箱子；  

    ```c
    void FirstFit ( )
    {   
        while ( read item ) {
            scan for the first bin that is large enough for item;
            if ( found ) {
                place item in that bin;
            } else {
                create a new bin for item;
            }
        } /* end-while */
    }
    ```
    
=== "Best Fit"

    每次将物品放入剩余空间最小的箱子，如果放不下则开新箱子。

    ```c
    void BestFit ( )
    {   
        while ( read item ) {
            sort the bins in increasing order of the remaining space;
            scan for the first bin that is large enough for item;
            if ( found ) {
                place item in that bin;
            } else {
                create a new bin for item;
            }
        } /* end-while */
    }
    ```

关于在线算法我们有以下的结论：

!!! note "Theorem"
    一维装箱问题的在线算法不存在有小于 $\dfrac{5}{3}$ 的近似比.  
    ??? example
        考虑 

        \begin{aligned}
            s_i & ={} \frac{1}{7} + \varepsilon, \frac{1}{7} + \varepsilon, \frac{1}{7} + \varepsilon, \frac{1}{7} + \varepsilon, \frac{1}{7} + \varepsilon, \frac{1}{7} + \varepsilon, \\
            & ={} \frac{1}{3} + \varepsilon, \frac{1}{3} + \varepsilon, \frac{1}{3} + \varepsilon, \frac{1}{3} + \varepsilon, \frac{1}{3} + \varepsilon, \frac{1}{3} + \varepsilon, \\
            & ={} \frac{1}{2} + \varepsilon, \frac{1}{2} + \varepsilon, \frac{1}{2} + \varepsilon, \frac{1}{2} + \varepsilon, \frac{1}{2} + \varepsilon, \frac{1}{2} + \varepsilon
        \end{aligned}

        其中 $\varepsilon = 0.001$，这样的话，最优解是 6，而在线算法的解是 10.

## 0-1 背包问题

## 选址问题

问题描述：给定 $n$ 个点 $p_1, p_2, \ldots, p_n$，以及一个整数 $k$，要求选择 $K$ 个中心，使得每个点到最近的中心的距离最大值 $r(C)$ 最小化。这个问题被称为 $K \text{-}$中心问题（$K\text{-}$center problem）。距离的定义满足自反性、对称性和三角不等式。

第一个想法是进行穷举，但是可以发现，因为备选的中心点有无数个，所以穷举是不现实的。我们可以考虑使用最大边际效应贪心算法，即先根据所有点选择一个中心，然后再选择一个中心，以此类推。但是这样的算法很可能会得到一个很差的解。在整个过程中，我们发现，任意选择中心这样的条件是在是过于苛刻了，我们可以适当放宽条件，即在给定的点集中选择点作为中心，然后再进行贪心选择。

### 已知最优解的贪心算法（Greedy Algorithm with Oracle）

假设我们已经知道了最优解 $r(C^*)$，虽然我们还是无法确定最优解对应的中心点，但是我们可以对半径进行放缩。因为某个点 $s$ 到最优解中最近的中心 $C_s$ 的距离不会超过 $r(C^*)$，而如果我选择了 $s$ 作为中心点，那么只需要将半径设置为 $2r(C^*)$ 就可以将原先以 $C_s$ 为中心的，半径为 $r(C^*)$ 的最优解包含在内。

```c

Centers  Greedy_2r (Sites S0[], int n, int K, double r)
{   
    Sites  S[ ] = S0[ ]; /* S' is the set of the remaining sites */
    Centers  C[ ] = emptyset; /* C is the set of centers */
    while ( S[ ] != emptyset ) {
        Select any s0 from S and add it to C;
        Delete all s from S that are at dist(s, s0) less than or equal to 2*r;
    } /* end-while */
    if ( |C| less than or equal to K ) return C;
    else ERROR(No set of K centers with covering radius at most r);
}
```

!!! note "Theorem"
    $Greedy\text{-}2r$ 算法在给定最优解 $r(C^*)$ 的情况下是一个 $2\text{-}$近似算法。  
    ??? note "Proof"
        因为每次都是删除选取的中心 $2r(C^*)$ 为半径的圆内所有点，所以如果算法能在 $K$ 步之内停止，那么得到的解一定是小于等于最优解的 2 倍，因此我们只需要证明算法能在 $K$ 步之内停止即可。如果最优解是 $r(C^*)$，么在上面的算法中，每次随机选择一个剩余的点作为中心，半径为 $2r(C^*)$ 的圆至少会带走一个真正的最优解中的点为中心，$r(C^*)$ 的圆内的所有点。因此 $K$ 步之后必然最优解覆盖的所有点都被我们的算法覆盖，因此必然停止。
    !!! tip
        考虑逆否命题，这一定理及其证明表明：如果 $Greedy\text{-}2r$ 算法在 $K$ 步之内不停止，那么最优解一定不是 $r(C^*)$，即一定会大于 $r(C^*)$。因为考虑 $K + 1$ 步停止，那么必有两个点（记为 $s_1, s_2$）对应的圆覆盖了同一个最优解中的圆心（记为 $C^*$），那么 $s_1, s_2$ 到 $C^*$ 的距离一定小于 $r(C^*)$，但 $s_1, s_2$ 之间的距离一定大于 $2r(C^*)$，矛盾。

因为我们事实上并没有得到最优解，所以我们需要考虑使用二分法，结合上面的算法，去判断我们选择的 $r(C^*)$ 是否合适。

```c
Calculate rmax = max{dist(s, t) | s, t in S};
r1 = 0, r2 = rmax;
while (r1 < r2 - epsilon) {
    r = (r1 + r2) / 2;
    if (Greedy_2r(S, n, K, r) is successful) {
        r2 = r;
    } else {
        r1 = r;
    }
}
```

### 未知最优解的贪心算法

而事实上，我们也可以不依赖于最优解，直接使用贪心算法，基本的思想是避免圆与圆之间的重叠。思路如下：首先从输入点集中随机选取一个点作为第一个中心，加入中心点集 $C$。然后每轮循环在剩余的点中找到一个点 $s$ 的 $\operatorname{dist}(s, C)$ 最大，即 $s$ 是到现有中心最短距离最大的点，将其加入中心点集 $C$，直到 $C$ 的大小达到 $K$ 为止。

```c
Centers Greedy_Kcenter (Sites S[ ], int n, int K)
{   
    Centers C[ ] = emptyset; 
    Select any s from S and add it to C;
    while ( |C| < K ) {
        Select s from S with maximum dist(s, C);
        Add s it to C;
    } /* end-while */
    return C;
}
```

同样，我们有如下的结论：

!!! note "Theorem"
    $Greedy\text{-}Kcenter$ 算法是一个 $2\text{-}$近似算法。
    ??? note "Proof"
        利用反证法，设最优解为 $r(C^*)$，并假设 $Greedy\text{-}Kcenter$ 算法给出的最优解大于 $2r(C^*)$，这说明当 $Greedy\text{-}Kcenter$ 算法结束后，一定存在一个点 $s$，它到所有的中心的距离都大于 $2r(C^*)$，否则所有点都落在某个中心的 $2r(C^*)$ 的圆内，最优解一定不会大于 $2r(C^*)$。  
        因为每一步我们都在选择一个距离现有中心 $C′$ 最远的点，既然 $s$ 每一步都没有被选到，这就说明我们每一步选取的点 $c$ 都有（假设最终的中心为 $C$）  
        
        \[
            \operatorname{dist}(s, C') \geqslant \operatorname{dist}(s, C') \geqslant \operatorname{dist}(s, C) \geqslant 2r(C^*).
        \]

        按上述方法选出的集合也满足 $Greedy\text{-}2r$ 算法的条件，但我们知道 $Greedy\text{-}2r$ 算法 $K$ 步之后一定会停止，这就说明 $s$ 一定会被选到，矛盾。