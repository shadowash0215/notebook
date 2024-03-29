# Elliptic Curve Cryptography

!!! abstract
    本部分主要来源于 2023 年浙江大学短学期 **CTF101** 课程中 crypto 专题的第二讲[^1]，并结合了一部分网上的 blog 和文档。

!!! warning 
    正在建设中。

## 基础知识

### 定义

正式定义而言，椭圆曲线是光滑的、射影的、亏格为 1 的代数曲线，其上有一个特定的点 $O$。椭圆曲线是阿贝尔簇 – 也就是说，它有代数上定义的乘法，并且对该乘法形成阿贝尔群 – 其中 $O$ 即为单位元。

但还是采取一些更容易理解的方法来解释一下。我们称有如下形式的方程定义

$$
y^2 = x^3 + ax + b
$$

且满足图形无尖点、自相交和孤立点的曲线称为椭圆曲线，且该方程形式被称为椭圆曲线的 Weierstrass 形式。那么自然也存在着一些其他形式[^2]：

| Form Name | Equation |
|:-----------:|:----------:|
|Weierstrass|$y^2 = x^3 + ax + b$|
|projective|$y^2z = x^3 + axz^2 + bz^3$|
|Jacobian|$y^2 = x^3 + axz^4 + bz^6$|
|Montgomery|$by^2 = x^3 + ax^2 + x$|
|Edward|$x^2 + y^2 = c^2(1 + dx^2y^2)$|
|Twisted Edward|$ax^2 + y^2 = 1 + dx^2y^2$|
|Huff|$ax(y^2−1) = by(x^2−1)$|
|Normmal|$y^2 + axy + cy = x^3 + bx^2 + dx + e$|

不过常用的还是 Weierstrass 形式，而图形满足的条件也可以参数化的表示，即

$$
\Delta = 4a^3 + 27b^2 \neq 0.
$$

但我们在密码学领域应用的椭圆曲线大部分都是定义在有限域上的，也就是说，其实我们使用的是有限个离散的点构成的图形，而不是整个曲线。

在 sage 中，其默认的椭圆曲线方程形式是

$$
y^2 + a_1xy + a_3y = x^3 + a_2x^2 + a_4x + a_6.
$$

定义语句是 `EllipticCurve([a1,a2,a3,a4,a6])`. 但我们常用的其实是 Weierstrass 形式，所以定义时只需要传进两个参数即可，也就是 `EllipticCurve([a4,a6])`. 而如果要限制定义域的话则可以再传入一个参数 $\mathcal R，$ 其只要是个任意的交换环即可。而像上面说的有限域上的椭圆曲线则可以这样定义： `EllipticCurve(GF(p), [a1,a2,a3,a4,a6])`. 此外还有许多定义方法，sage 的文档[^3]中都已写出，不再赘述。

### 运算

椭圆曲线上的元素都是点，那么该如何定义点的运算呢？

- 取负：由于椭圆曲线是关于 $x$ 轴对称的，所以对于其上一点 $A = (x, y)$，取负运算就是将其 $y$ 取负，即 $-A = (x, -y)$

- 加法：椭圆曲线上有两点 $A, B$，它们相加的结果定义为 $C$，即 $C = A + B$. 那么就有必要稍微讨论一下 $A, B$  之间的关系，来确定 $C$ 是如何运算的。

    - $A \neq B$ 且 $B \neq -A$ ：这两点确定了一条直线，与椭圆曲线联立的话发现是可以解出第三个解的，第三个解就是 $-C$ ，$C$ 点取负就行。
    
    - $B = -A$ ：根据一种朴素的想法，$A + (-A) = O$，事实上也确实是这样，但垂直于 $x$ 轴的直线又在哪找到第三个点呢？这就涉及到 $O$ 的定义，其作为椭圆曲线群上的单位元，指的是无穷远点 $\infty$，借助于黎曼几何，我们可以不严谨地认为，这条直线事实上在无穷远点与椭圆曲线相交。
    
    - $B = A$ ：此时的这条直线就变成了椭圆曲线在点 $A$ 处的切线，斜率 
    $k = \frac{3x_A^2 + a}{2y_A}.$ 联立后还是三解，除去两个点 $A$ 便是点 $-C$ ，与第一种情况类似。

    所以，椭圆曲线上的加法是构成一个群的。在实际应用中我们希望获取一个大素数阶的循环群，所以选取一点作为生成元（或称基点）$G$，在这个生成元生成的循环子群上进行讨论。而我们也可以证明，其实椭圆曲线群必然与一个循环群或者两个循环群的直和同构。

- 乘法：定义自加法，将 $k$ 个点 $A$ 的和称为 $kA$，但或许叫数乘更合理些。如果我们换一种叫法，称椭圆曲线的加法为“乘法”，那么椭圆曲线的乘法就变成了“幂”，就可以使用反复平方法（快速幂）来计算乘法。为防止侧信道攻击，通常采用 Montgomery's Ladder 算法[^4]，其优势在于计算时间确定。

- 除法：Schoof's algorithm 提供了一个多项式时间内计算椭圆曲线阶 $\lvert E \rvert$ 的方法，而根据 Langrange's theorem，循环子群的阶必整除群阶，所以若是可以因式分解 $\lvert E \rvert$，即 $\lvert E \rvert = n_1^{p_1}n_2^{p_2}\cdots n_k^{p_k}$ ，并找出满足 $nP = 0$ 的最小正整数 $n_i$ ，便求得了子群的阶，也就是椭圆曲线群的阶。
    
    而在 sage 上可以直接执行 `E.order()` 得出椭圆曲线 $E$ 的阶。

    而当椭圆曲线的阶 $n$ 是一个大素数时，由于 
    
    $$
    (kn + x)G = knG + xG = kO + xG = xG, \forall k, x \in \mathbb{Z}
    $$

    所以当乘数在模 $n$ 意义下相同时，乘法结果相同，那么就可以把所有的乘数都先模 $n$ ，限制在 $GF(n)$ 上，那么相应的除法就是乘以乘法逆元了，即 $G/x = (x^{-1})G$. 

### 双线性配对

一般来说，双线性配对是一个依托于三个素数 $p$ 阶循环乘法群而定义的映射。而在椭圆曲线群下的话，得先引进一个概念。

**嵌入度数**：当曲线定义在 $GF(p)$ 上，曲线群的阶为 $n$ 时，定义曲线的嵌入度数为满足 $p^k \equiv 1 \pmod n$ 的最小正整数 $k$。而如果模 $n$ 意义下的整数乘法是一个群，那么 $k$ 就是由 $p$ 生成的子群的阶。

椭圆曲线群上的双线性配对建立在定义域为 $GF(p)$ 的椭圆曲线群，定义域为 $GF(p^k)$ 的椭圆曲线群，以及 $GF(p^k)$ 这三个群上。即双线性映射 $e$: $E(GF(p)) \times E(GF(p^k)) \rightarrow GF(p^k)$，有 $e(A, B) = c$，其中 $A$ 为 $E(GF(p))$ 上的点，$B$ 为 $E(GF(p^k))$ 上的点，$c$ 为 $GF(p^k)$ 上的数。注意这里的双线性配对是从两个加法循环群映射到一个乘法循环群上的，其所满足的双线性如下。

**双线性**：

\begin{gather}
\forall A, C \in E(GF(p)), B, D \in E(GF(p^k)), x, y \in \mathbb{Z}_p, \\ 
e(xA, yB) = e(A, B)^{xy}, e(A + C, B) = e(A, B)e(A, C), e(A, B + D) = e(A, B)e(A, D)
\end{gather}

其在三方密钥一轮密钥协商、BLS 短签名算法和 SM9 标识密码算法中有所应用。

## 离散对数与相应攻击

### 椭圆曲线群上的离散对数困难问题（ECDLP）

椭圆曲线之所以能应用于密码学中，是因为在其上有一个著名的困难问题：离散对数困难问题。但仔细一想的话会发现，其实椭圆曲线群是和模 $n$ 意义下的整数加法群同构的，按理说求解离散对数并不应该困难。事实也是如此，椭圆曲线群和整数加法群的运算本身并不太困难，但困难在于同构映射的构建，这才是核心所在。而以下的几种攻击，就建立在曲线特殊而导致的同构映射易于构建。

### 攻击手段

- 奇异曲线攻击

前面我们提到椭圆曲线的定义满足图形无尖点、自相交和孤立点，但假如参数并没有被恰当的选取而出现了这些情况会发生什么呢？

曲线 $y^2=(x- \alpha)^3$ 被称作 cusp，而曲线 $y^2=(x- \alpha)^2(x- \beta)$ 被称作 node，对他们而言，点 $( \alpha, 0)$ 都被称作奇异点。
这两种曲线致命的问题就是它们太过简单，以致于很容易就能找到同构映射，将椭圆曲线群上的问题转移到加法群或乘法群上。

对 cusp 而言，存在如下的从椭圆曲线群到 $GF(p)$ 加法群上的同构映射：

$$
\begin{array}{rrcl}
\varphi : & E(GF(p))     & \longrightarrow & GF(p)^{+}, \\
          & (x,y) & \longmapsto     & \frac{y}{x-\alpha}.
\end{array}
$$

而对 node 而言，存在如下的从椭圆曲线群到 $GF(p)$ 乘法群上的同构映射：

$$
\begin{array}{rrcl}
\varphi : & E(GF(p))     & \longrightarrow & GF(p)^{\times}, \\
          & (x,y) & \longmapsto     & \frac{y + \sqrt{\alpha-\beta}(x-\alpha)}{y - \sqrt{\alpha-\beta}(x-\alpha)}.
\end{array}
$$

借助这两个映射，这两种曲线上的离散对数问题就可以求解了。

- 异常曲线攻击[^5]（Anomalous Curves & SMART Attack）

之前提到，我们所使用的椭圆曲线都是模 $p$ 意义下的。而如果我们所使用的椭圆曲线的阶恰好是我们所模的素数 $p$，即 $\lvert E \rvert = p$ 时，这类曲线被称作 **Anomalous curve**，而我们利用 SMART Attack 就可以轻松攻击它们。
  
[^1]: [CTF101-Labs-2023-Crypto-Lab3](https://courses.zjusec.com/topic/crypto-lab3/).

[^2]: 表格参考了这篇 [blog](https://utaha1228.github.io/ctf-note/2021/08/01/Elliptic-Curve-Form/).

[^3]: [Elliptic curve constructor](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/constructor.html)

[^4]: [Montgomery's Ladder](https://cryptohack.org/challenges/ecc/).

[^5]: 本部分攻击实现的数学基础参见这篇 [blog](https://utaha1228.github.io/ctf-note/2021/07/20/Smart-s-Attack/)，不过也有其他的数学理论可以达到同样的效果. 