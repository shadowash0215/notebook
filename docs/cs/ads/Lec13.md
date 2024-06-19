# 随机算法

## 雇佣问题

设每天面试一个人，共面试 $N$ 天，面试的代价为 $C_i$，雇佣的代价为 $C_h$，且最后雇佣的人数为 $M$，那么容易得到最终的代价为 $O(N \cdot C_i + M \cdot C_h)$。示意代码如下：

```c
int Hiring (EventType C[ ], int N)
{   
    /* candidate 0 is a least-qualified dummy candidate */
    int Best = 0;
    int BestQ = the quality of candidate 0;
    for (i = 1; i <= N; i++) {
        Qi = interview(i); /* Ci */
        if (Qi > BestQ) {
            BestQ = Qi;
            Best = i;
            hire(i);  /* Ch */
        }
    }
    return Best;
}

```

但显然这样存在一个问题，如果面试人是以能力升序排列的，最终的代价为 $O(N \cdot C_i + N \cdot C_h)$，也就是最坏的情况。为了避免这种情况，我们设置需要设置面试者的面试顺序是随机的，以下为分析：

!!! success "Analysis"
    设 $X$ 为雇佣的次数，$X_i$ 表示第 $i$ 个人是否被雇佣，$1$ 表示被雇佣，$0$ 表示没有被雇佣。那么有 
    
    \[
        X = \sum_{i=1}^{N} X_i, E[X] = \sum_{i=1}^{N} E[X_i]
    \]
    
    而我们假设前 $i$ 个候选人都有同等的可能成为最佳的人选，所以第 $i$ 个人被雇佣的概率为 $1/i$，所以 $E[X_i] = 1/i$，所以 $E[X] = \sum_{i=1}^{N} 1/i = \ln N + O(1)$。最终代价的期望为 $O(N \cdot C_i + \ln N \cdot C_h)$。

相应地代码只需要在原先的基础上添加一次随机排序即可。

现在考虑以上问题的一个变体，加入我们只能进行一次雇佣，也就是说，整个算法是在线进行决策的。一个简单的想法是，我们将前 $k$ 个人选作为“训练集”，然后从第 $k+1$ 个人开始，如果有人比训练集中的人好，那么就雇佣他。示意代码如下：

```c

int OnlineHiring (EventType C[ ], int N, int k)
{
    int Best = N;
    int BestQ = -infty ;
    for (i = 1; i <= k; i++) {
        Qi = interview(i);
        if (Qi > BestQ) {
            BestQ = Qi;
        }
    }
    for (i = k + 1; i <= N; i++ ) {
        Qi = interview(i);
        if (Qi > BestQ) {
            Best = i;
            break;
        }
    }
    return Best;
}

```

所以现在的问题是，如何选择 $k$ 的值，使得最终的效果最好呢？我们设事件 $S_i$ 为第 $i$ 个候选人是最佳的，并且被雇佣，那么需要满足以下两个条件：

- $A_i$: 最佳的候选人的位置为 $i$；
- $B_i$: $k + 1$ 到 $i - 1$ 之间的候选人都没有被雇佣。

这两个事件是独立的，因为候选人的位置并不因为我们的决策而改变。所以我们有

\[
    \operatorname{Pr}[S_i] = \operatorname{Pr}[A_i \cap B_i] = \operatorname{Pr}[A_i] \cdot \operatorname{Pr}[B_i] = \frac{1}{N} \cdot \frac{k}{i - 1}.
\]

那记事件 $S$ 为雇佣的候选人是最佳的，则有

\[
    \operatorname{Pr}[S] = \sum_{i = k + 1}^N \operatorname{Pr}[S_i] = \sum_{i = k + 1}^N \frac{k}{N(i - 1)} = \frac{k}{N} \sum_{i = k}^{N - 1} \frac{1}{i}.
\]

现在我们需要对级数 $\sum_{i = k}^{N - 1} \frac{1}{i}$ 的上下界进行估计，来实现对概率 $\operatorname{Pr}[S]$ 的估计。事实上我们有如下估计

!!! note "Theorem"

    \[
        \int_k^N \frac{1}{x} \mathrm{d}x \leqslant \sum_{i = k}^{N - 1} \frac{1}{i} \leqslant \int_{k - 1}^{N - 1} \frac{1}{x} \mathrm{d}x
    \]
    ??? note "Proof"
        将积分依据整数拆分为 $N - k$ 个区间，每个区间用区间最大值或最小值替代进行放缩.

        \[
            \int_k^N \frac{1}{x} \mathrm{d}x \leqslant \sum_{i = k + 1}^N \frac{1}{i} \leqslant \sum_{i = k}^{N - 1} \frac{1}{i} \leqslant \sum_{i = k - 1}^{N - 2} \frac{1}{i} \leqslant \int_{k - 1}^{N - 1} \frac{1}{x} \mathrm{d}x.
        \]

由此可以得到

\[
    \frac{k}{N} \ln \left(\frac{N}{k}\right) \leqslant \operatorname{Pr}[S] \leqslant \frac{k}{N} \ln \left(\frac{N - 1}{k - 1}\right).
\]

我们希望保证这一概率的下界尽可能大，所以我们需要选择 $k$ 使得 $f(k) = \ln \left(\frac{N}{k}\right)$ 最大，容易得到 $k = N / e$ 时，$f(k)$ 达到最大值，为 $\frac{1}{e}$。实际情况中，我们选择距离 $N / e$ 最近的整数即可。

## 快速排序