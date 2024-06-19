# 哈希

## 哈希表

- 哈希表（hash table）也称为散列表，是一种数据结构，它通过把关键字值映射到表中一个位置来访问记录，以加快查找的速度
    - 支持查找关键字是否在表中、查询关键字、插入关键字、删除关键字等操作
    - 关键字也称为标识符（identifier）
- 通常用一个数组来实现，也可以有多个槽（slot），即多个关键字对应同一个位置时，将不同关键字存在同一个位置的不同槽中
- 对于标识符 $x$，定义一个哈希函数 f(x) 将其映射到哈希表 ht[] 中的一个位置（索引）
- 设哈希表 ht 的大小为 b（即 f(x) 值域为 $[0, b - 1)$ 最多有 $s$ 个槽，则定义以下值:
    - $T$ 表示哈希表 $x$ 可能的不同值个数
    - $n$ 表示 ht 中所有不同关键字的个数
    - 标识符密度定义为 $n / T$
    - 装载密度定义为 $\lambda = n / (sb)$
- 当存在 $i_1 \neq i_2$ 但 $f(x_{i_1}) = f(x_{i_2})$ 时，称为发生了碰撞（collision）
- 当把一个新的标识符映射到一个已经满了的桶中时，称为溢出（overflow）
    - $s = 1$ 时，碰撞和溢出是等价的

## 哈希函数

- 哈希函数应该易于计算，并且减少碰撞的可能性
- 哈希函数应该是 unbiased 的，即 $P(f(x) = i) = 1 / b$，这种函数被称为均匀哈希函数（uniform hash function）
- 对于整数的哈希，例如 $f(x) = x \bmod \text{Tablesize}$，其中 $\text{Tablesize}$ 最好选择为质数，这样对于随机输入，关键字的分布更均匀

## 分离链接

- 解决冲突的一种方法是分离链接（separate chaining）
- 将哈希映射到同一个值的所有元素保存在一个列表（链表）中

## 开放地址

- 开放地址（open addressing）是另一种解决冲突的方法
- 当有冲突发生时，尝试选择其它单元，直到找到空的为止
- 即有多个哈希函数 $h_1(x), h_2(x), \cdots,$ 其中 $h_i(x) = (hash(x) + f_i(x)) \bmod \text{Tablesize}$，
    - 其中 $f_i(x)$ 是一个增量函数，有多种选择
- 一般来说 $\lambda < 0.5$

### 线性探测

- 即增量函数 $f_i(x) = i$
- 即冲突了就往后一个一个找，直到找到空的为止
- 会导致聚集（clustering），即一旦发生了冲突，那么后面的元素都会聚集在一起，搜索次数会变得非常大
    - 使用线性探测的探测次数对于插入和不成功查找来说约为 $\dfrac{1}{2}\left(1+\dfrac{1}{(1-\lambda)^2}\right)$
    - 对于成功的查找来说则需要 $\dfrac{1}{2}\left(1+\dfrac{1}{1-\lambda}\right)$ 次

### 二次探测

- 即 $f(i) = i^2$
- 如果使用二次探测，且表大小为质数时，那么当表至少有一半是空的时，总能插入一个新的元素
- 查找
    - $f(i) = f(i-1) + i^2 - (i-1)^2 = f(i-1) + 2i - 1$
    ```C
    Position find(ElementType key, HashTable H) {
        Position currentPos = hash(key, H->TableSize);
        int collisionNum = 0;
        while (H->TheCells[currentPos].Info != Empty && 
            H->TheCells[currentPos].Element != key) {
            currentPos += 2 * ++collisionNum - 1;
            if (currentPos >= H->TableSize) currentPos -= H->TableSize;
        }
        return currentPos;
    }
    ```
    - 插入
    ```C
    void insert(ElementType key, HashTable H) {
        Position pos = find(key, H);
        if (H->TheCells[pos].Info != Legitimate) {
            H->TheCells[pos].Info = Legitimate;
            H->TheCells[pos].Element = key;
        }
    }
    ```

### 双重哈希
- 即 $f(i) = i * \mathrm{hash}_2(x)$
- 一般选择 $\mathrm{hash}_2(x) = R - (x\bmod R)$，其中 $R$ 为小于表大小的质数
- 二次探测不需要使用第二个哈希函数，所以相比之下二次探测更简单快速

### 再哈希
- 使用二次探测，如果表的元素过多，那么操作时间会过长，而且可能插入失败
- 解决方法是再哈希（rehashing）
    - 建立一个两倍大的哈希表
    - 扫描原始哈希表
    - 利用新的哈希函数将元素映射到新的哈希值，并插入
- 如果有原来的哈希表有 $N$ 个元素，则再哈希的时间复杂度为 $O(N)$
- 什么时候进行再哈希
    - 表填满一半了
    - 插入失败
    - 当哈希表达到了某一个特定的装载密度时