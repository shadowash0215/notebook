# 分治

## 主定理

分治法递归的时间复杂度递推公式具有如下形式：

\[
    T(n) = aT(\frac{n}{b}) + f(n)
\]

其中 $a$ 是分了多少个子问题，$b$ 与子问题划分方式有关，是子问题输入长度的收缩因子，$f(n)$ 则是合并各个子问题的解需要的时间。

### 递归树

### 主定理形式

!!! note "Theorem"
    考虑以下形式 

    \[
        T(n) = aT(\frac{n}{b}) + f(n), a \geqslant 1, b \geqslant 2,
    \]

    1. 若对于某个 $\varepsilon > 0$，有 $f(n) = O(n^{\log_b a - \varepsilon})$，则 $T(n) = \Theta(n^{\log_b a})$；
    2. 若 $f(n) = \Theta(n^{\log_b a})$，则 $T(n) = \Theta(n^{\log_b a} \log n)$；
    3. 若对于某个 $\varepsilon > 0$，有 $f(n) = \Omega(n^{\log_b a + \varepsilon})$，且对于某个常数 $c < 1$，有 $a f(\frac{n}{b}) \leqslant c f(n)$，则 $T(n) = \Theta(f(n))$。

!!! success "Lemma"
    1. 对于某个常数 $c > 1$ 有 $a f(\frac{n}{b}) = c f(n)$，则 $T(n) = \Theta(n^{\log_b a} )$；
    2. 若 $a f(\frac{n}{b}) = f(n)$，则 $T(n) = \Theta(n^{\log_b a} \log n)$；
    3. 若对于某个常数 $c < 1$ 有 $a f(\frac{n}{b}) = c f(n)$，则 $T(n) = \Theta(f(n))$。

!!! note "Theorem"
    对于递推式 $T(n) = aT(\frac{n}{b}) + \Theta(n^k \log^p n), a \geqslant 1, b > 1, k \geqslant 0, p \geqslant 0$，

    1. 若 $a > b^k$，则 $T(n) = \Theta(n^{\log_b a})$；
    2. 若 $a = b^k$，则 $T(n) = \Theta(n^k \log^{p+1} n)$；
    3. 若 $a < b^k$，则 $T(n) = \Theta(n^k \log^p n)$。

## 最近点对问题

给定平面上的 $N$ 个点，找到距离最近的两个点。暴力搜索的时间复杂度为 $O(N^2)$，所以我们考虑使用分治法。问题在于我们需要在线性时间内找到跨越中线的点对，否则时间复杂度会退化为 $O(N^2)$。

首先先取 $x$ 坐标来看的中点，其 $x$ 坐标记为 $\bar{x}$，然后考虑 $[\bar{x} - \delta, \bar{x} + \delta]$ （$\delta$ 是左右两半中的最近点对距离）区间内的点 $q_1, q_2, \ldots, q_l$，我们可以将这些点按照 $y$ 坐标排序，设 $q_i$ 的 $y$ 坐标为 $y_i$，那我们只需要对 $q_i$ 检查 $x$ 坐标在 $[\bar{x} - \delta, \bar{x} + \delta]$ 内，$y$ 坐标在 $[y_i, y_i + \delta]$ 内的点即可。将这个长方形区域分为平均分割为 8 块，则每块内最多出现 1 个点，否则会存在单侧的点对距离小于 $\dfrac{\sqrt{2}}{2} \delta$，与 $\delta$ 的定义矛盾。所以对于每个 $q_i$，我们只需找向上 7 个点即可，所以找分离最近点对的时间复杂度是线性的。