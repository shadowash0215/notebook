# 数据库系统复习

## Indexing

### Concept

- 主索引(primary index)：以文件顺序存储，索引文件的每个记录对应数据文件的一个块，索引文件的记录数与数据文件的块数相同。通常也被称作聚集索引(clustered index)。

- 辅助索引(secondary index)：索引顺序通常与数据文件不同，并且索引可能不是唯一的。通常也被称作非聚集索引(non-clustered index)。

- 稠密索引(dense index)：索引文件中的每个索引项对应数据文件中的一个记录。

- 稀疏索引(sparse index)：索引文件中的只包含一部分数据文件的记录作为索引项。

### B+ Tree

$n$ 指的是树的扇出(fanout).

内部节点拥有 $\lceil \frac{n}{2} \rceil$ 到 $n$ 个子节点，叶子节点拥有 $\lceil \frac{n - 1}{2} \rceil$ 到 $n - 1$ 个键值对。对于根节点而言，如果其不是叶子节点，则至少有两个子节点。

每个节点的结构如下：

|$P_1$|$K_1$|$P_2$|$\ldots$|$P_{n - 1}$|$K_{n - 1}$|$P_n$|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|

$K_i$ 表示索引键，$P_i$ 表示指向子节点的指针（非叶子节点）或者指向数据记录的指针（叶子节点）。

如果文件当中有 $K$ 对键值对，那么树的高度的范围为 $\lceil \log_{\lceil \frac{n}{2} \rceil} K \rceil$ 到 $\lceil \log_{\lceil \frac{n}{2} \rceil} K/2 \rceil + 1$。

!!! example "有关 B+ Tree 的计算"
    Table definition:
    ```sql
    person( 
        pid     char(18) primary key,
        name    char(8),   
        age     smallint,                             
        address char(40) 
        );
    ``` 
    Block Size: 4K  
    Record Number: 1000000  
    Create index on `pid`.
    So:  

    - Record Size = $18 + 8 + 2 + 40 = 68$ bytes;  
    - Records per block = $\lfloor 4096 / 68 \rfloor = 60$;  
    - Block Number = $\lceil 1000000 / 60 \rceil = 16667$;  
    - Fanout $n = \lfloor \frac{4096 - 4}{18 + 4} \rfloor + 1 = 187$($4$ is the size of pointer);  
    - inner pointer numbers = $\lceil n / 2 \rceil = 94 \sim 187$;  
    - leaf pointer numbers = $\lceil (n - 1) / 2 \rceil = 93 \sim 186$;  
    - 2 Level B+ Tree node numbers: $\min = 2 * 93 = 186$, $\max = 187 * 186 = 34782$;  
    - 3 Level B+ Tree node numbers: $\min = 2 * 94 * 93 = 17484$, $\max = 187 * 187 * 186 = 6504234$;  
    - 4 Level B+ Tree node numbers: $\min = 2 * 94 * 94 * 93 = 1643496$, $\max = 187 * 187 * 187 * 186 = 1216291758$;  
    - The height of this B+ Tree is 3.
    - max node number corresponding to the half full leaf node,  
        - leaf levle node: $\lfloor 1000000 / 93 \rfloor = 10752$(cannot fit less);    
        - second level node: $\lfloor 10752 / 94 \rfloor = 114$;  
        - root: $1$;  
        - total: $10752 + 114 + 1 = 10867$;  
    - max node number corresponding to the full leaf node,  
        - leaf levle node: $\lceil 1000000 / 186 \rceil = 5377$(cannot fit more);    
        - second level node: $\lfloor 5376 / 187 \rfloor = 29$;  
        - root: $1$;  
        - total: $5376 + 29 + 1 = 5406$.

## Query Processing

### Selection

$t_T$ 表示块转移时间(block transfer time)，$t_s$ 表示寻道时间(seek time)，$b_r$ 表示关系的块数。

1. 线性扫描(linear search)  
    - Worst Cost：$b_r * t_T + t_s$;  
    - Average Cost：$(b_r / 2) * t_T + t_s$.  

2. 主索引上的对键属性的等值查找(primary B+ tree index, equality on key)
    - Cost: $(h_i + 1) * (t_T + t_s)$;  
    - $h_i$ 是指 B+ tree 的层高。  
    - 每层都有一个块需要被 seek & transfer，最后存有记录的块也需要被 seek & transfer。

3. 主索引上的对非键属性的等值查找(primary B+ tree index, equality on nonkey)  
    - Cost: $h_i * (t_T + t_s) + t_s + b * t_T$;  
    - 与 2 差距不大，区别在于所要查找的记录可能有多条，分布在连续的不同的块中，$b$ 是所要查找的记录所在的块数。

4. 辅助索引上的对键属性的等值查找(secondary B+ tree index, equality on key)  
    - Cost: $(h_i + 1) * (t_T + t_s)$;
    - 虽然记录是分散的，但是键属性是唯一的。

5. 辅助索引上的对非键属性的等值查找(secondary B+ tree index, equality on nonkey)  
    - Cost = $(h_i + m + n) * (t_T + t_s)$;  
    - $n$ 是所要查找的记录的条数，$m$ 是指针所在的块数。最坏的情况是 $n$ 条记录各自在一个块中。

6. 主索引上的比较查找（已经排序的情况）(primary B+ tree index, comparison)  
    - $\sigma_{A \geqslant V}(r)$ Cost: $h_i * (t_T + t_s) + t_s + b * t_T$;  
    - 与主索引上的对非键属性的等值查找相似，找到第一个 $A \geqslant V$ 的记录后将后续的记录都 transfer 过来。

7. 辅助索引上的比较查找(secondary B+ tree index, comparison)  
    - 这种情况下可能还不如线性扫描的效果好。

### Complex Selection

1. Conjunctive Selection: $\sigma_{\theta_1 \cap \theta_2 \cap \ldots \cap \theta_n}(r)$  
    - 其中一个条件有索引的话，就用索引先选出，然后检验是否满足其他条件。  
    - 有联合索引的情况下，可以直接使用索引。  
    - 根据单个条件选择出结果集，然后再进行交集操作。  

2. Disjunctive Selection: $\sigma_{\theta_1 \cup \theta_2 \cup \ldots \cup \theta_n}(r)$  
    - 根据单个条件选择出结果集，然后再进行交集操作。

3. Negation Selection: $\sigma_{\neg \theta}(r)$  
    - 一般情况下，先找出满足条件的记录，然后再取补集。
    - 线性扫描也是可取的。

### External Sorting

$M$ 是内存块数.  

1. 创建初始归并段
    - 初始化变量 $i = 0$;  
    - 重复以下步骤直到所有记录都被读入过内存：
        - 读入 $M$ 个块到内存；  
        - 对这些块进行排序；  
        - 将排序后的块写入段 $R_i$ 当中；  
        - $i = i + 1$.  
    - $i$ 的最终输出记为 $N$，实际上满足 $N = \lceil \frac{b_r}{M} \rceil$.
2. 归并（$N$ 路归并）
    - 若 $N < M$，只需要一次归并；
        - $N$ 块作为输入缓冲，$1$ 块作为输出缓冲，读进每个归并段的第一个块；  
        - 重复以下步骤直到所有输入缓冲都为空：
            - 选取输入缓冲中最小的记录，写入输出缓冲，若输出缓冲已满，则写入磁盘；
            - 删除已经写入的记录，如果输入缓冲已经为空，则读入下一个块。
    - 若 $N \geqslant M$  
        - 每次归并都使用 $M - 1$ 块作为输入缓冲，$1$ 块作为输出缓冲，读入每个归并段的第一个块；
        - 每次归并都会让段数目减少为原先的 $\frac{1}{M - 1}$，直到最后只剩下一个段。
3. 代价分析(simple version)：
    - 初始归并段个数：$N = \lceil \frac{b_r}{M} \rceil$;  
    - 需要的归并次数：$\lceil \log_{M - 1} N \rceil$;  
    - 创建初始归并段以及之后的每次归并都需要 $2 * b_r$ 的块转移次数；  
        - 但最后一次归并的写入次数**可能**不需要计算，因为结果可能会被传递到上一层的操作而非写入磁盘。  
        - 这种情况下的块转移次数为 $b_r * (2 * \lceil \log_{M - 1} \lceil \frac{b_r}{M} \rceil \rceil + 1)$.
    - 创建初始归并段的寻道次数为 $2 * \lceil \frac{b_r}{M} \rceil$，因为每一段寻道成功之后就可以连续读入 $M$ 个块；  
    - 每次归并的寻道次数为 $2 * b_r$，也就是在不同的段之间切换；
        - 但最后一次归并的写入磁盘的寻道次数**可能**不需要计算；  
        - 这种情况下的寻道次数为 $b_r * (2 * \lceil \log_{M - 1} \lceil \frac{b_r}{M} \rceil \rceil - 1) + 2 * \lceil \frac{b_r}{M} \rceil$.
4. 代价分析(advanced version)：
    - 现在每个段都可以从内存中得到 $b_b$ 个块作为输入缓冲，同理也有 $b_b$ 个块作为输出缓冲；  
    - 归并路数为 $\lfloor \frac{M}{b_b} \rfloor - 1$（$-1$ 是因为还有一个输出缓冲）；  
    - 归并次数为 $\lceil \log_{\lfloor \frac{M}{b_b} \rfloor - 1} \lceil \frac{b_r}{M} \rceil \rceil$，有所增加；  
    - 创建初始归并段以及之后的每次归并的块转移次数依然不变，为 $2 * b_r$；
        - 依然考虑最后一次**可能**不需要写入磁盘的情况，块转移次数为 $b_r * (2 * \lceil \log_{\lfloor \frac{M}{b_b} \rfloor - 1} \lceil \frac{b_r}{M} \rceil \rceil + 1)$，实际上就是归并次数的替换。
    - 创建初始归并段的寻道次数不变，为 $2 * \lceil \frac{b_r}{M} \rceil$；  
    - 每次归并的寻道次数变为 $2 * \lceil \frac{b_r}{b_b} \rceil$，因为每次归并可以连续读入 $b_b$ 个块；  
        - 依然考虑最后一次**可能**不需要写入磁盘的情况，寻道次数为 $\lceil \frac{b_r}{b_b} \rceil * (2 * \lceil \log_{\lfloor \frac{M}{b_b} \rfloor - 1} \lceil \frac{b_r}{M} \rceil \rceil - 1) + 2 * \lceil \frac{b_r}{M} \rceil$，是归并次数与归并寻道次数的替换。

### Join Operation

计算 $r \Join_{\theta} s$ 有如下算法：

1. Nested-Loop Join
    - 伪代码描述如下：

        > for each tuple $t_r$ in $r$ do begin  
        > $\quad$ for each tuple $t_s$ in $s$ do begin  
        > $\quad$ $\quad$ test pair $(t_r, t_s)$ to see if they satisfy the join condition $\theta$  
        > $\quad$ $\quad$ if they do, add $t_r \cdot t_s$ to the result.  
        > $\quad$ end  
        > end

    - $r$ 被称为外层关系，$s$ 被称为内层关系。
    - 最坏情况需要 $n_r * b_s + b_r$ 次块转移，$n_r + b_r$ 次寻道，因为对于外循环的每条记录，内循环都需要读入一次 $s$ 的所有块。
    - 最好情况为内存可以容纳 $r$ 的所有记录和 $s$ 的所有块，此时只需要 $b_r + b_s$ 次块转移和 $2$ 次寻道。

2. Block Nested-Loop Join
    - 伪代码描述如下：

        > for each block $B_r$ of $r$ do begin  
        > $\quad$ for each block $B_s$ of $s$ do begin  
        > $\quad$ $\quad$ for each tuple $t_r$ in $B_r$ do begin  
        > $\quad$ $\quad$ $\quad$ for each tuple $t_s$ in $B_s$ do begin  
        > $\quad$ $\quad$ $\quad$ $\quad$ test pair $(t_r, t_s)$ to see if they satisfy the join condition $\theta$  
        > $\quad$ $\quad$ $\quad$ $\quad$ if they do, add $t_r \cdot t_s$ to the result.  
        > $\quad$ $\quad$ $\quad$ end  
        > $\quad$ $\quad$ end  
        > $\quad$ end  
        > end

    - 最坏情况需要 $b_r * b_s + b_r$ 次块转移和 $2 * b_r$ 次寻道；
    - 最好情况同上，只需要 $b_r + b_s$ 次块转移和 $2$ 次寻道。
    - 所以我们需要将较小的关系作为外层关系。  
    - 如果内存有 $M$ 块，其中一块作为输出缓冲，那么外关系分配 $M - 1$ 块，内关系分配 $1$ 块，这样减少了内关系对应块的读取次数，代价为 $\lceil \frac{b_r}{M - 2} \rceil * b_s + b_r$ 次块转移和 $2 * \lceil \frac{b_r}{M - 2} \rceil$ 次寻道。
    - 如果连接的属性是键属性，那么可以在成功找到匹配的记录之后就停止内循环。
    - 利用 LRU 策略的特点，inner 正向扫描后再反过来，这样最近的块很可能还在内存中，提高缓存命中率。

3. Indexed Nested-Loop Join
    - 内循环有索引的话，就没有必要扫描内循环所有的块；
    - 代价为 $b_r * (t_T + t_s) + n_r * c$，其中 $c$ 是遍历索引并取出所有匹配的元组的时间。

4. Merge Join
    - 如果两个属性都已经排序，那么可以使用归并的方式进行连接；  
    - 代价为 $b_r + b_s$ 次块转移和 $b_r + b_s$ 次寻道，因为寻道的最坏情况是在两个关系之间来回切换。  
    - 如果内存总共有 $M$ 块，那么可以将 $r$ 和 $s$ 分别分为 $x_r$ 和 $x_s$ 个块，其中 $x_r + x_s = M$，这样可以减少寻道次数，代价为 $b_r + b_s$ 次块转移和 $\lceil \frac{b_r}{x_r} \rceil + \lceil \frac{b_s}{x_s} \rceil$ 次寻道。  
    - 最优的分配方法为 $x_r = \frac{\sqrt{b_r}}{\sqrt{b_r} + \sqrt{b_s}} * M$，$x_s = \frac{\sqrt{b_s}}{\sqrt{b_r} + \sqrt{b_s}} * M$。
    - 如果未排序的话需要加上排序的代价。

5. Hash Join
    - 通过哈希函数将两个关系的元组切片为更小的块，以使得内存可以容纳 $s_i$，从而只需要将 $r_i$ 和 $s_i$ 进行连接；
    - $s$ 被称为 build 关系，$r$ 被称为 probe 关系；
    - 通过哈希函数得到的块的个数应当满足 $n \geqslant \lceil \frac{b_s}{M} \rceil$，但通常会乘上一个修正因子 $f$ 以预留一些空间；
    - 算法描述如下：
        - 利用哈希函数 $h$ 将 $s$ 进行划分，每一个划分得到的块都需要一个块作为输出缓冲；
        - 同理划分 $r$；
        - 对于每个 $i$，将 $s_i$ 放入内存并且对连接属性建立哈希索引，这个哈希函数应该与 $h$ 不同；
        - 从 $r_i$ 中读取元组，$t_r$ 通过哈希索引与 $t_s$ 进行连接，输出连接成功的元组。
    - 但也存在一次哈希之后得到的 $n$ 个块无法放入内存的情况，这时候需要进行 recursive partitioning，即将 $s_i$ 再次划分为 $s_{ij}$，直到可以放入内存为止。这里与归并排序相反，利用不同的哈希函数进行划分将 $s$ 划分的越来越多也越来越小；
    - 不需要 Recursive Partitioning 的条件是 $M > \lceil \frac{b_s}{n} \rceil + 1$，近似为 $M > \sqrt{b_s}$；
    - 代价为 $3 * (b_r + b_s) + 4 * n_h$ 次块转移和 $2 * (\lceil \frac{b_r}{b_b} \rceil + \lceil \frac{b_s}{b_b} \rceil) + 2 * n_h$ 次寻道，其中 $n_h$ 是哈希索引的块数，一般较小。划分的时候的块转移次数为 $2 * (b_r + b_s)$，连接的时候的块转移次数为 $b_r + b_s$。
    - 如果需要进行 Recursive Partitioning，那么采取的次数为 $\lceil \log_{\lfloor \frac{M}{b_b} \rfloor - 1} \lceil \frac{b_s}{M} \rceil \rceil$。代价为 $2 * (b_r + b_s) * \lceil \log_{\lfloor \frac{M}{b_b} \rfloor - 1} \lceil \frac{b_s}{M} \rceil \rceil + (b_r + b_s)$ 次块转移和 $2 * (\lceil \frac{b_r}{b_b} \rceil + \lceil \frac{b_s}{b_b} \rceil) * \lceil \log_{\lfloor \frac{M}{b_b} \rfloor - 1} \lceil \frac{b_s}{M} \rceil \rceil$ 次寻道。

### Other Operations

1. Duplicate Elimination: 在排序的过程（生成、合并归并段）就进行去重，哈希也是类似的；
2. Aggregation: 在排序的过程中，同一段的就可以统计统一结果。

## Query Optimization

### Equivalence Rules

1. Selection Pushdown: $\sigma_{\theta_1 \cap \theta_2}(E) \Leftrightarrow \sigma_{\theta_1}(\sigma_{\theta_2}(E))$;

2. Commutativity of Selection: $\sigma_{\theta_1}(\sigma_{\theta_2}(E)) \Leftrightarrow \sigma_{\theta_2}(\sigma_{\theta_1}(E))$;

3. Projection omit: $\Pi_{L_1}(\Pi_{L_2}(\ldots(\Pi_{L_n}(E))\ldots)) \Leftrightarrow \Pi_{L_1}(E)$;

4. Selection combined with Cartesian Product and Join: 

    \begin{gather}
        \sigma_{\theta}(E_1 \times E_2) \Leftrightarrow E_1 \Join_{\theta} E_2 \\
        \sigma_{\theta_1}(E_1 \Join_{\theta_2} E_2) \Leftrightarrow E_1 \Join_{\theta_1 \cap \theta_2} E_2
    \end{gather}

5. Commutativity of Join: $E_1 \Join_{\theta} E_2 \Leftrightarrow E_2 \Join_{\theta} E_1$;

6. Associativity of Natural Join: $(E_1 \Join E_2) \Join E_3 \Leftrightarrow E_1 \Join (E_2 \Join E_3)$;

7. Associativity of Theta Join: $(E_1 \Join_{\theta_1} E_2) \Join_{\theta_2 \cap \theta_3} E_3 \Leftrightarrow E_1 \Join_{\theta_1 \cap \theta_3} (E_2 \Join_{\theta_2} E_3)$, $\theta_2$ involves only attributes of $E_2$ and $E_3$;

8. Selection Distribution over Join: 

    \begin{gather}
        \sigma_{\theta_0}(E_1 \Join_{\theta} E_2) \Leftrightarrow (\sigma_{\theta_0}(E_1)) \Join_{\theta} E_2, \\ 
        \sigma_{\theta_1 \cap \theta_2}(E_1 \Join_{\theta} E_2) \Leftrightarrow (\sigma_{\theta_1}(E_1)) \Join_{\theta} (\sigma_{\theta_2}(E_2))
    \end{gather}

    $\theta_0$ involves only attributes of $E_1$, $\theta_1$ involves only attributes of $E_1$ and $\theta_2$ involves only attributes of $E_2$;

9. Projection Distribution over Join: 

    \[
        \Pi_{L_1 \cup L_2}(E_1 \Join_{\theta} E_2) \Leftrightarrow \Pi_{L_1 \cup L_2}(\Pi_{L_1 \cup L_3}(E_1) \Join_{\theta} \Pi_{L_2 \cup L_4}(E_2))
    \]

    $L_3$ involves the attributes of $E_1$ in join condition $\theta$ but not in $L_1 \cup L_2$, $L_4$ involves the attributes of $E_2$ in join condition $\theta$ but not in $L_1 \cup L_2$;

    If $\theta$ involves only attributes in $L_1 \cup L_2$, then $\Pi_{L_1 \cup L_2}(E_1 \Join_{\theta} E_2) \Leftrightarrow \Pi_{L_1}(E_1) \Join_{\theta} \Pi_{L_2}(E_2)$.

10. Selection Distribution over Aggregation: $\sigma_{\theta}(_G\gamma_A(E)) \Leftrightarrow (_G\gamma_A)(\sigma_{\theta}(E))$;


### Size Estimation

- $n_r$ 表示关系 $r$ 的记录数；
- $b_r$ 表示关系 $r$ 的块数；
- $l_r$ 表示关系 $r$ 的记录长度；
- $f_r$ 表示关系 $r$ 的块的填充因子，即一块中实际存储的记录数，$b_r = \lceil \frac{n_r}{f_r} \rceil$；
- $V(A, r)$ 表示属性 $A$ 在关系 $r$ 中的不同值的个数，和 $\Pi_{A}(r)$ 的结果集大小相同；

1. $\sigma_{A = V}(r)$
    - 估计选中的记录数：$n_r / V(A, r)$，认为每个值都是均匀分布的；
    - 对键属性的等值查找认为返回的记录数为 $1$。

2. $\sigma_{A \leqslant V}(r)$
    - 如果可以获得 $\min(A, r)$ 和 $\max(A, r)$，那么估计选中的记录数为：

    \begin{cases}
        0, & \text{if } V < \min(A, r) \\
        \frac{V - \min(A, r)}{\max(A, r) - \min(A, r)} \cdot n_r, & \text{if } \min(A, r) \leqslant V \leqslant \max(A, r) \\
        n_r, & \text{if } V > \max(A, r)
    \end{cases}

    - 如果无法获得 $\min(A, r)$ 和 $\max(A, r)$，那么估计选中的记录数为 $n_r / 2$。

3. 对于条件 $\theta_i$ 来说，其中选率为 $\frac{s_i}{n_r}$，其中 $s_i$ 表示选中的记录数。
    - Conjunctive Selection: 假设独立，那么选中的记录数为 $n_r \cdot \prod_{i = 1}^{n} \frac{s_i}{n_r}$；
    - Disjunctive Selection: 假设独立，那么选中的记录数为 $n_r \cdot (1 - \prod_{i = 1}^{n} (1 - \frac{s_i}{n_r}))$。

4. $r \Join_\theta s$
    - 如果 $r \cap s = \varnothing$，那么 $n_{r \Join s} = n_r \cdot n_s$；
    - 如果连接属性是 $r$ 的一个键属性，那么 $n_{r \Join s} \leqslant n_s$；
    - 如果连接属性是 $s$ 的一个参照 $r$ 的外键，那么 $n_{r \Join s} = n_s$；
    - 如果连接属性是 $r$ 和 $s$ 的非键属性，那么估计为 $\min(\frac{n_r}{V(A, r)} \cdot n_s, \frac{n_s}{V(A, s)} \cdot n_r)$。

5. Projection: $\operatorname{Size}(\Pi_{A}(r)) = V(A, r)$；
6. Aggregation: $\operatorname{Size}(_G\gamma_A(r)) = V(A, r)$；
7. 集合的操作总是按上界估计。

### Distinct Value Estimation

1. Selection
    - 如果 $\theta$ 使 $A$ 取一个特定值，那么 $V(A, \sigma_{\theta}(r)) = 1$；
    - 如果 $\theta$ 使 $A$ 取指定值中的一个，那么 $V(A, \sigma_{\theta}(r)) = \text{# of specified values}$；
    - 如果 $\theta$ 使 $A$ 取一个范围，如 $A \leqslant V$，那么 $V(A, \sigma_{\theta}(r)) = V(A, r) * s$，其中 $s$ 是中选率；
    - 其他情况下，用 $\min(V(A, r), n_{\sigma_{\theta}(r)})$ 作为估计值。

2. Join
    - 如果条件中的属性全部来自 $r$，那么估计 $V(A, r \Join s) = \min(V(A, r), n_{r \Join s})$；
    - 如果条件中 $A_1$ 来自 $r$，$A_2$ 来自 $s$，那么估计 $V(A, r \Join s) = \min(V(A_1, r) * V(A_2 - A_1, s), V(A_2, s) * V(A_1 - A_2, r), n_{r \Join s})$。

## Transaction



## Concurrency Control

## Recovery