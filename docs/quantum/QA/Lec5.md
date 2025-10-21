# Discrete log and the hidden subgroup problem

## Discrete log

$G = \langle g \rangle$ 是 $g$ 生成的循环群，而对于 $x \in G$，$x$ 关于 $g$ 的离散对数 $\log_g x$ 定义为满足 $g^\alpha = x$ 的最小非负整数 $\alpha$. 离散对数问题是指给定 $g, x$ 求 $\log_g x$. 

## Diffie-Hellman key exchange

密钥交换的目的是让远距离的两方 Alice 和 Bob 通过不安全的公开信道协商出一个共同的密钥，整个流程如下：

1. Alice 和 Bob 公开选定一个大素数 $p$ 和一个高阶整数 $g$. 简单起见，假设 $g$ 生成 $\mathbb{Z}_p^*$.

2. Alice 随机均匀选取 $a \in \mathbb{Z}_{p-1}$，计算 $A = g^a \mod p$ 并发送给 Bob. Bob 随机均匀选取 $b \in \mathbb{Z}_{p-1}$，计算 $B = g^b \mod p$ 并发送给 Alice.

3. Alice 计算 $K := B^a \mod p = g^{ab} \mod p$，Bob 计算 $A^b \mod p = g^{ab} \mod p$，得到相同的密钥 $K$.

所以 Alice 和 Bob 共享了密钥 $K$，而 Eve 只能知道 $p, g, A, B$. 

## The hidden subgroup problem

实际上，离散对数问题是隐藏子群问题的一个特例. 隐藏子群问题的定义如下：

!!! info "Hidden subgroup problem"
    给定群 $G$ 和集合 $S$，以及黑盒函数 $f: G \to S$，该函数满足

    \[
        f(x) = f(y) \iff x^{-1}y \in H,
    \]

    其中 $H \leq G$ 是某个未知的子群. 称函数 $f$ **隐藏**了子群 $H$. 目标是通过查询 $f$ 来确定 $H$.

$f$ 在陪集 $gH := \{gh : h \in H\}$ 上是常数，但不同的陪集上取不同值. 

Simon's problem 对应 $G = \mathbb{Z}_2^n$，$H = \{0, s\}$ 的情形. 因为集合 $S$ 是无结构的，所以在经典算法下，只要尚未得到 $f(x) = f(y)$ 的信息，就无法做到比随机查询群元素更优. 而依据生日悖论，期望需要 $O(\sqrt{\lvert G \rvert / \lvert H \rvert})$ 次查询才能得到碰撞.

!!! note "Theorem"
    设群 $G$ 有一个由 $N$ 个子群组成的集合 $\mathcal{H} = \{H_1, H_2, \ldots, H_N\}$，且 $\cap_{i=1}^N H_i = \{e\}$. 那么为了解决隐藏子群问题，任何经典确定性算法需要 $\Omega(\sqrt{N})$ 次查询.

    ???+ note "Proof"
        假设谕示机并没有事先隐藏某个子群，而是采取对抗的行为，行为如下：

        在第 $l$ 次查询时，算法查询了 $g_l$，不失一般性假设其与 $g_1, g_2, \ldots, g_{l-1}$ 都互异. 如果存在子群 $H \in \mathcal{H}$ 使得对任意 $1 \leq j < k \leq l$ 都有 $g_k \notin g_j H$，也就是说，谕示机仍可以将 $g_l$ 分配到一个尚未查询的陪集上，那么谕示机就简单的返回 $l$；否则，谕示机认输并输出一个与目前查询结果相容的子群的生成集.

        现在考虑一个迫使谕示机认输前进行了 $t$ 次查询的算法，算法只能得到 $1, 2, \ldots, t$ 作为查询结果. 但不管查询了哪 $t$ 个群元素，最多只能得到 $t(t-1)$ 个非单位元的 $g_kg_j^{-1}$，而总共有 $N$ 个子群，若想要覆盖所有子群，必须有 $t(t-1) \geq N$，所以 $t = \Omega(\sqrt{N})$.

        如果对抗性谕示机在 $t$ 次查询后仍没有认输，这就表明存在两个或更多的标准谕示机在 $t$ 次查询后无法被区分开来. 

## Shor's algorithm

简单起见假设 $N := \lvert G \rvert$ 是已知的（可以使用 Shor period-finding 算法来得到）. 离散对数问题可以被视作群 $\mathbb{Z}_N \times \mathbb{Z}_N$ 上的隐藏子群问题. 定义函数 $f: \mathbb{Z}_N \times \mathbb{Z}_N \to G$ 为

\[
    f(\alpha, \beta) = x^\alpha g^\beta = g^{\alpha \log_g x + \beta}.
\]

所以 $f$ 在线

\[
    L_\lambda := \{(\alpha, \beta) \in \mathbb{Z}_N^2 : \alpha \log_g x + \beta = \lambda \}
\]

上是常数. 所以 $f$ 隐藏了子群

\[
    H = L_0 = \{(0, 0), (1, -\log_g x), (2, -2\log_g x), \ldots, (N-1, -(N-1)\log_g x)\}.
\]

陪集形式为 $(\gamma, \delta) + H, \gamma, \delta \in \mathbb{Z}_N$. 但 $\delta$ 取遍 $\mathbb{Z}_N$ 时，

\[
    (0, \delta) + H = \{\alpha, \delta - \alpha \log_g x) : \alpha \in \mathbb{Z}_N\} = L_\delta,
\]

给出了陪集的完整表示. （因此 $\{0\} \times \mathbb{Z}_N$ 是 $H$ 在 $\mathbb{Z}_N \times \mathbb{Z}_N$ 中的一个**横截**（transversal）.）

首先从 $\mathbb{Z}_N \times \mathbb{Z}_N$ 上的均匀叠加态开始，而后计算隐藏函数：

\[
    \ket{\mathbb{Z}_N \times \mathbb{Z}_N} := \frac{1}{N} \sum_{\alpha, \beta \in \mathbb{Z}_N} \ket{\alpha, \beta} \mapsto \frac{1}{N} \sum_{\alpha, \beta \in \mathbb{Z}_N} \ket{\alpha, \beta, f(\alpha, \beta)}.
\]

然后丢弃第三个寄存器. 概念上可以想象成实际上测量了第三个寄存器，测量得到 $f(\alpha, beta) = g^\delta, \delta \in \mathbb{Z}_N$，对应的 $(\alpha, \beta)$ 落在陪集 $L_\delta$ 上，也就得到了陪集态

\[
    \ket{(0, \delta) + H} = \ket{L_\delta} = \frac{1}{\sqrt{N}} \sum_{\alpha \in \mathbb{Z}_N} \ket{\alpha, \delta - \alpha \log_g x}.
\]

但实际上进行的是丢弃，丢弃会使得整个系统处于由陪集态系综描述的混合态中，$\delta$ 均匀分布在 $\mathbb{Z}_N$ 上. 进而执行 $\mathbb{Z}_N \times \mathbb{Z}_N$ 上的 $\op{QFT}$：

\[
    \frac{1}{N^{3/2}} \sum_{\alpha, \mu, \nu \in \mathbb{Z}_N} \omega_N^{\alpha \mu + (\delta - \alpha \log_g x) \nu} \ket{\mu, \nu} = \frac{1}{N^{3/2}} \sum_{\mu, \nu \in \mathbb{Z}_N} \omega_N^{\delta \nu} \sum_{\alpha \in \mathbb{Z}_N} \omega_N^{\alpha(\mu - \nu \log_g x)} \ket{\mu, \nu}.
\]

利用式子 $\sum_{\alpha \in \mathbb{Z}_N} \omega_N^{\alpha \beta} = N \delta_{\beta, 0}$，上式化简为

\[
    \frac{1}{\sqrt{N}} \sum_{\nu \in \mathbb{Z}_N} \omega_N^{\delta \nu} \ket{\nu \log_g x, \nu}.
\]

此时测量便会得到某个对 $(\nu \log_g x, \nu)$，如果 $\nu$ 在模 $N$ 下有乘法逆元，那么直接相除即可；否则重复上述步骤直到得到的 $\nu$ 有逆元为止. 每次尝试成功的概率为 $\phi(N) / N = \Omega(1 / \log \log N)$，所以不需要太多次尝试.