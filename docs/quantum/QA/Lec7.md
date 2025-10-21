# Quantum attacks on elliptic curve cryptography

## Elliptic curves

固定一个特征不为 $2$ 或 $3$ 的域 $\mathbb{F}$. （实际密码学应用中经常使用特征为 $2$ 的域 $\mathbb{F}_{2^n}$，但这种情况下的椭圆曲线定义略微复杂，所以此处不讨论这种情形.） 考虑等式

\[
    y^2 = x^3 + ax + b,
\]

其中 $a, b \in \mathbb{F}$ 为参数. 满足该等式的点 $(x, y) \in \mathbb{F}^2$ 以及一个**无穷远点**（point at infinity） $\mathcal{O}$ 构成了椭圆曲线 $E_{a, b}$. 如果曲线的**判别式**（discriminant）$\Delta = -16(4a^3 + 27b^2) \neq 0$，则其称为**非奇异的**（nonsingular），以下均只考虑非奇异的椭圆曲线. 对于密码学应用希望能够将曲线上的点用有限数量的位精确表示，所以考虑的是有限域上的. 简单起见，只考虑 $\mathbb{F}_p$，其中 $p$ 是不为 $2$ 或 $3$ 的素数.

总的来说，曲线上点的数量依赖于参数 $a, b$，但对较大的 $p$ 来说，点的数量大约为 $p$，更精确地说，Hasse 定理表明点的数量 $N = p + 1 - t$，其中 $\lvert t \rvert \leq 2\sqrt{p}$. （不过对于椭圆曲线而言，存在一个叫做 Schoof 的算法可以在 $\op{poly}(\log p)$ 时间内计算出 $N$ 的精确值.）对于有限域上由多项式方程定义的更一般的曲线，也存在类似于 Hasse 定理的结果，但精确计算点的数量则是困难的. 不过对于某些曲线，存在 Kedlaya 这一高效的量子算法来计算点的数量.

椭圆曲线上也能定义群结构. 给定 $P, Q \in E_{a, b}$，定义 $P + Q$ 的方法如下. 先考虑都不是无穷远点 $\mathcal{O}$ 的情形. 连接 $P, Q$ 的直线与曲线的交点为 $R$（注意如果 $P = Q$，则取切线），如果这条线是垂直的，那么 $R = \mathcal{O}$. 否则，$R$ 也是曲线上的点. $P + Q$ 定义为 $R$ 关于 $x$ 轴的对称点，而 $\mathcal{O}$ 关于 $x$ 轴的对称点仍然是 $\mathcal{O}$. 如果 $Q = \mathcal{O}$，则通过 $P$ 作一条垂直线，交点的对称点仍然是 $P$，所以 $P + \mathcal{O} = P$，$\mathcal{O}$ 是加法的单位元. $P = (x, y)$ 的加法逆元为 $-P = (x, -y)$. 还需要证明的就是结合律，但这需要一定的代数几何知识，此处不再赘述. 下面给出具体的计算公式.

设 $P = (x_P, y_P), Q = (x_Q, y_Q)$，直线 $L$ 连接 $P, Q$ 的斜率为

\[
    \lambda = \frac{y_Q - y_P}{x_Q - x_P}
\]

所以线上的点 $(x, y)$ 满足 $y = \lambda x + y_0$，其中 $y_0 = y_P - \lambda x_P$. 将其代入椭圆曲线方程，得到

\[
    x^3 - \lambda^2 x^2 + (a - 2\lambda y_0)x + (b - y_0^2) = 0.
\]

利用维达定理（Vieta's formulas），设 $R = (x_R, y_R)$ 是第三个交点，则有 $x_P + x_Q + x_R = \lambda^2$. 所以

\begin{align*}
    x_{P+Q} & = x_R \\
            & = \lambda^2 - x_P - x_Q \\
            & = \left(\frac{y_Q - y_P}{x_Q - x_P}\right)^2 - x_P - x_Q, \\
\end{align*}

以及

\begin{align*}
    y_{P+Q} & = -y_R \\
            & = -(\lambda x_{P+Q} + y_0) \\
            & = \lambda(x_P - x_{P+Q}) - y_P \\
            & = \frac{y_Q - y_P}{x_Q - x_P}(x_P - x_{P+Q}) - y_P.
\end{align*}

而当 $P = Q$ 时，便是取切线. 若 $y_P = 0$，则切线是垂直的，所以 $P + P = \mathcal{O}$. 否则，切线的斜率为

\[
    \lambda = \frac{3x_P^2 + a}{2y_P}.
\]

进行类似地计算，得到

\begin{align*}
    x_{2P} & = \lambda^2 - 2x_P, \\
           & = \left(\frac{3x_P^2 + a}{2y_P}\right)^2 - 2x_P, \\
\end{align*}

以及

\begin{align*}
    y_{2P} & = \lambda(x_P - x_{2P}) - y_P, \\
           & = \frac{3x_P^2 + a}{2y_P}(x_P - x_{2P}) - y_P.
\end{align*}

由此便脱离了几何图像定义的束缚，使得有限域上的椭圆曲线也能定义加法运算. 

## Elliptic curve cryptography

固定椭圆曲线 $E_{a, b}$ 并选择一个点 $G \in E_{a, b}$，研究子群 $\langle G \rangle. 运用群中的幂运算，便可以定义 Diffie-Hellman 密钥交换协议和 ElGamal 公钥加密方案的类似物，显然其安全性依赖于椭圆曲线上的离散对数问题（Elliptic Curve Discrete Logarithm Problem, ECDLP）的难度. 

实践中选用曲线需要考虑诸多细节，因为存在针对“超奇异”曲线和“异常”曲线的特殊攻击. 一般情况下，尚未知晓如何在椭圆曲线群上比通用方法更快地解决离散对数问题，这些通用方法的运行时间为 $O(\sqrt{p})$. 

## Shor's algorithm for discrete log over elliptic curves

Shor's algorithm 也可以在 $\op{poly}(\log p)$ 时间内解决 $\mathbb{F}_p$ 上椭圆曲线群的离散对数问题. 因为这些公式只涉及域上的基本算术运算，最困难的模逆运算也能利用扩展欧几里得算法完成.