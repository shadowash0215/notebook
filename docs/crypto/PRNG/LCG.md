# 线性同余生成器

## 简介

线性同余生成器（Linear Congruential Generator, LCG）是一种伪随机数生成器，其生成的随机数序列是通过一个线性方程递推生成的。LCG 的递推公式为：

\[
    X_{n+1} = (aX_n + c) \mod m,
\]

其中 $m > 0$ 被称为模，$0 < a < m$ 被称为乘数，$0 \leqslant c < m$ 被称为增量，$0 \leqslant X_0 < m$ 被称为种子，它们被称为 LCG 的参数。

## 周期

- $m$ 是素数，$c = 0$.  
    $a$ 是 $m$ 的原根时，LCG 的周期为 $m - 1$。  
    但模掉一个素数也有一些缺点，较为显著的是在计算的时候我们需要计算两倍位宽的乘积，以及对乘积进行约化以确保结果落在 $m$ 之内，这些都会造成额外的开销。不过通常我们会使用一些只比 2 的幂次小一点的素数作为 $m$，比如 Mersenne Prime $2^{31} - 1$ 或 $2^{61} - 1$。所以在计算 $a \cdot x \bmod {m ( = 2^e - d)}$ 时，可以计算 $a \cdot x \bmod {2^e} + d \cdot \lfloor a \cdot x / 2^e \rfloor$，如果这个结果较大，则需要减去 $m$，不过次数限制为 $\dfrac{a \cdot d}{m}$，当 $d$ 较小的时候，这个值通常为 1。  
    当我们没有两倍 $m$ 的位宽时，我们可以使用 Schrage 方法来计算。首先将 $m$ 写为 $m = q \cdot a + r$，其中 $q = \lfloor m / a \rfloor$，$r = m \bmod a$，然后计算 $a \cdot x \bmod m$，其值为 $a \cdot (x \bmod q) - r \cdot \lfloor x / q \rfloor$。

    ??? note "Proof"
        考虑 $aq = a \cdot ((m - r) / a) = m - r \equiv -r \pmod m$，所以 
        
        \[
            a \cdot x = a \cdot (x \bmod q) + a \cdot q \cdot \lfloor x / q \rfloor \equiv a \cdot (x \bmod q) - r \cdot \lfloor x / q \rfloor \pmod m.
        \]

    因为 $x \bmod q < q \leqslant m$，所以这一项的值不会超过 $m$，而如果我们通过选择合适的 $a$ 控制 $r/q \leqslant 1$，那么有 $r \cdot \lfloor x / q \rfloor \leqslant r \cdot (x / q) \leqslant x \cdot r / q \leqslant m$，所以这一项的值也不会超过 $m$。所以我们可以通过这种方式计算 $a \cdot x \bmod m$。

- $m$ 是 2 的幂次，$c = 0$.  
    此时的优势在于我们的模运算可以非常快速的进行，因为我们只需要取 $x$ 的低 $e$ 位即可。但这样的情况也有不少的缺点。  
    这一形势下的周期最多只有 $\dfrac{m}{4}$，当 $a \equiv \pm 3 \pmod 8$ 且 $X_0$ 为奇数时取到最大值。即使在最好的情况下，生成的随机数的低三位也只会在两个值之间循环。

- $m$ 是 2 的幂次，$c \neq 0$.  

    !!! note "Hull-Dobell Theorem"
        如果 $m$ 为 2 的幂次，那么当且仅当：  
        1. $c$ 与 $m$ 互质；  
        2. $a - 1$ 能被 $p$ 整除，其中 $p$ 是 $m$ 的所有质因子；  
        3. $a - 1$ 能被 4 整除，如果 $m$ 能被 4 整除。  
        时，LCG 才能达到最大周期 $m$。