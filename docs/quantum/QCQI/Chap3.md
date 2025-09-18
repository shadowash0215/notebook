# Introduction to computer science

## Models for computation

### Turing machines

!!! note "Church–Turing thesis"
    图灵机可计算的函数类对应于算法可计算的函数类.

### Circuits

图灵机模型和电路模型通过均匀电路族的概念联系起来. 电路族由一组电路 $\{C_n\}$ 构成，并且通过正整数 $n$ 进行索引. 电路 $C_n$ 具有 $n$ 个输入位，可以包含任意有限数量的额外工作位，以及输出位. 当输入一个长度不超过 $n$ 位的数 $x$ 时，电路 $C_n$ 的输出记为 $C_n(x)$. 要求这些电路满足一致性，即若 $m < n$ 且 $x$ 的长度不超过 $m$，则 $C_n(x) = C_m(x)$. 电路族计算的函数 $C(\cdot)$ 定义为 $C(x) = C_{|x|}(x)$.

但是只考虑无限制的电路族是不够的，实际当中需要一种算法来构建电路. 如果对电路族不加任何限制，那么它们可能计算出各种在合理计算模型中无法预期的函数. 例如，令 $h_n(x)​ 表示仅作用于 $n$ 位输入 $x$ 的停机函数（即判断程序 $x$ 是否停机）. $h_n$ 是从 $n$ 位输入到 $1$ 位输出的函数，且我们已证明存在计算 $h_n(\cdot)$ 的电路 $C_n$. 因此，电路族 $\{C_n\}$ 可以计算停机函数！但实际上并无法指定一个算法来为所有 $n$ 生成电路 $C_n$，因此这个电路族并不是一个合理的计算模型.

因而提出了均匀电路族的概念. 一个电路族 $\{C_n\}$ 是均匀的，如果存在一个在图灵机上运行的算法，当输入 $n$ 时，可以生成电路 $C_n$ 的描述. 具体来说，需要输出：

- 电路中包含的门的类型和数量

- 门的连接方式

- 所需的辅助位

- 扇出与交换操作

- 输出位的读取方式

如果没有这样的算法，那么该电路族便被称为非均匀的. 

## The analysis of computational problems

1. 可计算问题是什么？为了建立计算问题的通用理论，我们聚焦于一类特殊的问题，即判定问题. 

2. 如何设计算法来解决给定的计算问题？

3. 解决给定计算问题所需的最小资源是什么？

### How to quantify computational resources

#### Asymptotic notation: examples

### Computational complexity

如果一个问题存在一种只利用多项式资源的算法，那么我们称这个问题是简单的，易处理的，或是可解的. 如果一个问题的最优算法需要超多项式资源，那么我们称这个问题是困难的，难处理的，或是不可解的.

!!! note "strong Church–Turing thesis"
    任何计算模型都可以用概率多项式图灵机模拟，并且需要的操作数只增加原来的多项式次幂.

### Decision problems and the complexity classes $\mathsf{P}$ and $\mathsf{NP}$

### A plethora of complexity classes

!!! note "$\mathsf{BPP}$ and Chernoff bound"
    假定一个判定问题的一个算法给出正确答案的概率为 $\frac{1}{2} + \epsilon$，给出错误答案的概率为 $\frac{1}{2} - \epsilon$，其中 $\epsilon > 0$. 如果运行该算法 $n$ 次，那么似乎猜测出现次数更多的答案是更合理的. 那么这一过程的可靠性如何？Chernoff bound 给出了一个答案.

    !!! note "Theorem"
        (The Chernoff bound) 设 $X_1, \ldots, X_n$ 是 $n$ 个独立同分布的随机变量，且 $X_i \in \{0, 1\}$，$p(X_i = 1) = \dfrac{1}{2} + \epsilon$，$p(X_i = 0) = \dfrac{1}{2} - \epsilon$，其中 $\epsilon > 0$. 那么

        \[
            p\left(\sum_{i=1}^n X_i \leq \dfrac{n}{2}\right) \leq e^{-2\epsilon^2 n}.
        \]

        ??? note "Proof"
            考虑任意包含至多 $\dfrac{n}{2}$ 个 $1$ 的序列 $(x_1, \ldots, x_n)$，那么当该序列包含 $\lfloor \dfrac{n}{2} \rfloor$ 个 $1$ 时，概率最大，因此有

            \[
                p(X_1 = x_1, \ldots, X_n = x_n) \leq (\dfrac{1}{2} + \epsilon)^{\frac{n}{2}} (\dfrac{1}{2} - \epsilon)^{\frac{n}{2}} = \dfrac{(1 - 4\epsilon^2)^{\frac{n}{2}}}{2^n}.
            \]

            因为满足条件的序列有至多 $2^n$ 个，所以

            \[
                p \left(\sum_i X_i \leq \dfrac{n}{2}\right) \leq 2^n \cdot \dfrac{(1 - 4\epsilon^2)^{\frac{n}{2}}}{2^n} = (1 - 4\epsilon^2)^{\frac{n}{2}}.
            \]

            由于 $1 - x \leq e^{-x}$，所以

            \[
                p \left(\sum_i X_i \leq \dfrac{n}{2}\right) \leq e^{-4\epsilon^2 n/2} = e^{-2\epsilon^2 n}.
            \]

### Energy and computation

!!! note "Theorem"
    **Landauer's principle (first form):** 假设计算机擦除了一位信息，那么它耗散到环境中的能量至少为 $k_BT \ln 2$，其中 $k_B$ 是玻尔兹曼常数，$T$ 是电脑环境的温度.

    **Landauer's principle (second form):** 假设计算机擦除了一位信息，那么环境增加的熵至少为 $k_B \ln 2$，其中 $k_B$ 是玻尔兹曼常数.

    