# The quantum adversary method

## Quantum adversaries

量子敌手方法的动机来源于以下构造：假设谕示机由对抗方操作，其持有一个量子态来确定谕示机字符串，可能是叠加态 $\sum_{x \in S} a_x \ket{x}$. 为了实现每次查询，敌手执行“超谕示机”

\[
    O := \sum_{x \in S} \ket{x}\bra{x} \otimes O_x.
\]

因为算法不能直接访问谕示机字符串 $x$, 因此只能在敌手叠加态上执行表现为恒等操作的酉算子，$t$ 次查询后，算法将整体状态映射为

\begin{align*}
    \ket{\psi^t} & := (I \otimes U_t) O \cdots (I \otimes U_2) O (I \otimes U_1) O (\sum_{x \in S} a_x \ket{x} \otimes \ket{\psi}) \\
                 & = \sum_{x \in S} a_x \ket{x} \otimes \ket{\psi_x^t}.
\end{align*}

该方法的主要思想在于，为了让算法了解 $x$，整个状态必须变得非常纠缠. 而为了量化纯态 $\ket{\psi^t}$ 的纠缠程度，考虑以下谕示机的约化密度矩阵：

\[
    \rho^t := \sum_{x,y \in S} a_x^* a_y \innerproduct{\psi_x^t}{\psi_y^t} \ket{x}\bra{y}.
\]

初始状态的 $\rho^0$ 是纯态，目标是量化在错误概率为 $\varepsilon$ 的情况下计算出 $f$ 前其能达到的混合程度. 容易考虑的是 $\rho^t$ 的熵，但事实证明其他的度量更容易处理.

事实上有以下关于量子态可区分的基本事实：

!!! note "Fact"
    给定纯态 $\ket{\psi}$, $\ket{\phi}$ 二者之一，当且仅当 $\lvert \innerproduct{\psi}{\phi} \rvert \leq 2\sqrt{\varepsilon(1-\varepsilon)}$ 时，能通过一次测量以不超过 $\varepsilon \in [0, 1/2]$ 的错误概率区分 $\ket{\psi}$ 和 $\ket{\phi}$.

因此考虑在内积 $\innerproduct{\psi_x^t}{\psi_y^t}$ 上线性的度量是更方便的.

## The adversary method

为了获取敌手下界，选择矩阵 $\Gamma \in \mathbb{R}^{\lvert S \rvert \times \lvert S \rvert}$，行列由可能的黑盒输入索引. 元素 $\Gamma_{x,y}$ 刻画了区分 $x, y$ 的困难程度. 如果其满足

1. 对所有 $x, y \in S$，$\Gamma_{x, y} = \Gamma_{y, x}$;
2. 若 $f(x) = f(y)$，则 $\Gamma_{x, y} = 0$.

那么称 $\Gamma$ 为**敌手矩阵**（adversary matrix）. 

原始的敌手方法额外假设了 $\Gamma_{x, y} \geq 0$，但这个条件并非必须. 所以这种方法有时也被称为负权重敌手方法或广义敌手方法，以区别于原始的正权重敌手方法.

给定敌手矩阵，定义权重函数

\[
    W^j := \sum_{x,y \in S} \Gamma_{x,y} a_x^* a_y \innerproduct{\psi_x^j}{\psi_y^j}.
\]

而这是 $\rho^j$ 元素的简单函数. 证明思路是初始时 $W^j$ 很大，而为了计算 $f$ 必须变小，并且在进行查询时变化不大.

因为初始态不能依赖于 $x$，所以权重函数的初值为

\begin{align*}
    W^0 & = \sum_{x,y \in S} \Gamma_{x,y} a_x^* a_y \innerproduct{\psi_x^0}{\psi_y^0} \\
        & = \sum_{x,y \in S} a_x^* \Gamma_{x,y} a_y.
\end{align*}

为了使这个值尽可能的大，选择 $a$ 为 $\Gamma$ 的一个主特征向量，即特征值为 $\pm \lVert \Gamma \rVert$ 的特征向量. 因此 $\lvert W^0 \rvert = \lVert \Gamma \rVert$. 假设一个非负敌手矩阵更容易约束权重函数的终值. 最终值的约束在于当 $f(x) \neq f(y)$ 时，必须以最多为 $\varepsilon$ 的错误概率区分 $x$ 和 $y$，为了满足这一点，需要在 $t$ 次查询后，满足 $\lvert \innerproduct{\psi_x^t}{\psi_y^t} \rvert \leq 2\sqrt{\varepsilon(1-\varepsilon)}$. 在 $\Gamma$ 元素非负的情况下，有

\begin{align*}
    \lvert W^t \rvert & \leq \sum_{x,y \in S} \Gamma_{x,y} a_x^* a_y 2\sqrt{\varepsilon(1-\varepsilon)} \\
                      & = 2\sqrt{\varepsilon(1-\varepsilon)} \lVert \Gamma \rVert.
\end{align*}

求和中包含了 $f(x) = f(y)$ 的项，但这些项的贡献为零. 也隐含地使用了 Perron-Frobenius 定理，保证了存在一个非负的主特征向量.

而如果 $\Gamma$ 允许负权重，也可以通过不同的论证得到类似的结果. 通常只能证明 $\lvert W^t \rvert \leq (2\sqrt{\varepsilon(1-\varepsilon)} + 2\varepsilon) \lVert \Gamma \rVert$，但如果解释 $f: S \to \{0,1\}$ 为布尔函数，那么可以证明相同的界，利用到了以下结果，以 Frobenius 范数 $\lVert X \rVert_F^2 := \sum_{a,b} \lvert X_{a,b} \rvert^2$ 形式描述：

!!! note "Proposition"
    对任意 $X \in \mathbb{C}^{m \times n}$，$Y \in \mathbb{C}^{n \times n}$，$Z \in \mathbb{C}^{n \times m}$，有 $\lvert \op{tr}(XYZ) \rvert \leq \lVert X \rVert_F \lVert Y \rVert \lVert Z \rVert_F$.

    ???+ note "Proof"
        \begin{align*}
            \lvert \op{tr}(XYZ) \rvert & = \sum_{a, b, c} X_{a,b} Y_{b,c} Z_{c,a} \\
                                       & = \sum_a (x^a)^\dagger Y z^a, 
        \end{align*}

        其中 $(x^a)_b = X_{a,b}^*$，$(z^a)_c = Z_{c,a}$，这是向量化的重写. 因此有

        \begin{align*}
            \lvert \op{tr}(XYZ) \rvert & \leq \sum_a \lVert x^a \rVert \lVert Y z^a \rVert \\
                                       & \leq \lVert Y \rVert \sum_a \lVert x^a \rVert \lVert z^a \rVert \\
                                       & \leq \lVert Y \rVert \sqrt{\sum_a \lVert x^a \rVert^2 \sum_{a'} \lVert z^{a'} \rVert^2} \\
                                       & = \lVert Y \rVert \lVert X \rVert_F \lVert Z \rVert_F.
        \end{align*}

为了约束具有布尔输出的负权重敌手方法 $\lvert W^t \rvert$ 的上界，改写 $W^t$ 为 $\op{tr}(\Gamma V)$，其中 $V_{x, y} := a_x^* a_y \innerproduct{\psi_x^t}{\psi_y^t} \delta[f(x) \neq f(y)]$. 定义

\begin{align*}
    C & := \sum_{x \in S} a_x \Pi_{f(x)} \ket{\psi_x^t} \bra{x}, \\
    \bar{C} & := \sum_{x \in S} a_x \Pi_{1 - f(x)} \ket{\psi_x^t} \bra{x},
\end{align*}

其中 $\Pi_0$ 和 $\Pi_1$ 分别表示投影到 $f(x) = 0$ 和 $f(x) = 1$ 的子空间. 那么

\[
    (C^\dagger \bar{C})_{x,y} = a_x^* a_y \bra{\psi_x^t} (\Pi_{f(x)} \Pi_{1 - f(y)}) \ket{\psi_y^t}.
\]

因此

\begin{align*}
    (C^\dagger \bar{C} + \bar{C}^\dagger C)_{x,y} & = a_x^* a_y \bra{\psi_x^t} (\Pi_{f(x)} \Pi_{1 - f(y)} + \Pi_{1 - f(x)} \Pi_{f(y)}) \ket{\psi_y^t} \\
    & = a_x^* a_y \innerproduct{\psi_x^t}{\psi_y^t} \delta[f(x) \neq f(y)] \\
    & = V_{x,y}.
\end{align*}

所以 $V = C^\dagger \bar{C} + \bar{C}^\dagger C$. 进而有

\begin{align*}
    W^t & = \op{tr}(\Gamma (C^\dagger \bar{C} + \bar{C}^\dagger C)) \\
        & = \op{tr}(\Gamma C^\dagger \bar{C}) + \op{tr}(\Gamma \bar{C}^\dagger C).
\end{align*}

依据命题，有 $\lvert W^t \rvert \leq 2 \lVert \Gamma \rVert \lVert C \rVert_F \lVert \bar{C} \rVert_F$. 最终只需约束 $\lVert C \rVert_F$ 和 $\lVert \bar{C} \rVert_F$. 注意到 $\lVert X \rVert_F^2 = \sum_{x, y \in S} \lvert \bra{y} X \ket{x} \rvert^2$，所以有

\begin{align*}
    \lVert C \rVert_F^2 + \lVert \bar{C} \rVert_F^2 & = \sum_{x, y \in S} \lvert \bra{y} C \ket{x} \rvert^2 + \sum_{x, y \in S} \lvert \bra{y} \bar{C} \ket{x} \rvert^2 \\
    & = \sum_{x, y \in S} \lvert a_x \rvert^2 \left( \lvert \bra{y} \Pi_{f(x)} \ket{\psi_x^t} \rvert^2 + \lvert \bra{y} \Pi_{1 - f(x)} \ket{\psi_x^t} \rvert^2 \right) \\
    & = \sum_{x \in S} \lvert a_x \rvert^2 \left( \bra{\psi_x^t} \Pi_{f(x)} \ket{\psi_x^t} + \bra{\psi_x^t} \Pi_{1 - f(x)} \ket{\psi_x^t} \right) \\
    & = \sum_{x \in S} \lvert a_x \rvert^2 \bra{\psi_x^t} I \ket{\psi_x^t} \\
    & = 1.
\end{align*}

又因为算法的错误概率至多为 $\varepsilon$，所以 

\begin{align*}
    \lVert \bar{C} \rVert_F^2 & = \sum_{x, y \in S} \lvert \bra{y} \bar{C} \ket{x} \rvert^2 \\
                             & = \sum_{x \in S} \lvert a_x \rvert^2 \lVert \Pi_{1 - f(x)} \ket{\psi_x^t} \rVert^2 \\
                             & \leq \sum_{x \in S} \lvert a_x \rvert^2 \varepsilon \\
                             & = \varepsilon.
\end{align*}

从而 $\lVert C \rVert_F \lVert \bar{C} \rVert_F \leq \max_{x \in [0, \varepsilon]} \sqrt{x(1-x)} = \sqrt{\varepsilon(1-\varepsilon)}$. 也就有 $\lvert W^t \rvert \leq 2 \sqrt{\varepsilon(1-\varepsilon)} \lVert \Gamma \rVert$.

现在需要理解权重函数在算法的每一步中能减少多少. 首先有

\[
    W^{j+1} - W^j = \sum_{x,y \in S} \Gamma_{x,y} a_x^* a_y \left( \innerproduct{\psi_x^{j+1}}{\psi_y^{j+1}} - \innerproduct{\psi_x^j}{\psi_y^j} \right).
\]

而依据查询时的变化，有 $\ket{\psi_x^{j+1}} = U_{j+1} O_x \ket{\psi_x^j}$，所以态 $\{ \ket{\psi_x^{j+1}}: x \in S \}$ 的 Gram 矩阵元为

\begin{align*}
    \innerproduct{\psi_x^{j+1}}{\psi_y^{j+1}} & = \bra{\psi_x^j} O_x^\dagger U_{j+1}^\dagger U_{j+1} O_y \ket{\psi_y^j} \\
                                             & = \bra{\psi_x^j} O_x O_y \ket{\psi_y^j}.
\end{align*}

也就得到了

\[
    W^{j+1} - W^j = \sum_{x,y \in S} \Gamma_{x,y} a_x^* a_y \left( \bra{\psi_x^j} (O_x O_y - I) \ket{\psi_y^j} \right).
\]

观察到 $O_x O_y \ket{i, b} = (-1)^{b(x_i \oplus y_i)} \ket{i, b}$. 令 $P_0 = I \otimes \ket{0}\bra{0}$ 表示投影到 $b = 0$ 的投影算子，而 $P_i$ 表示投影算子 $\ket{i, 1}\bra{i, 1}$. 那么 $P_0 + \sum_{i=1}^n P_i = I$，并且 $O_x O_y = P_0 + \sum_{i = 1}^n (-1)^{x_i \oplus y_i} P_i$. 因此 $O_x O_y - I = -2 \sum_{i: x_i \neq y_i} P_i$. 代入上式，有

\[
    W^{j+1} - W^j = -2 \sum_{x,y \in S} \sum_{i: x_i \neq y_i} \Gamma_{x,y} a_x^* a_y \bra{\psi_x^j} P_i \ket{\psi_y^j}.
\]

对于 $i \in [n]$，定义矩阵 $\Gamma_i$，其元素为

\[
    (\Gamma_i)_{x,y} := \begin{cases}
        \Gamma_{x,y}, & x_i \neq y_i; \\
        0, & \text{otherwise}.
    \end{cases}
\]

定义 $Q_i = \sum_{x \in S} a_x P_i \ket{\psi_x^j} \bra{x}$，那么有

\begin{align*}
    W^{j+1} - W^j & = -2 \sum_{x, y \in S} \sum_{i=1}^n (\Gamma_i)_{x,y} a_x^* a_y \bra{\psi_x^j} P_i \ket{\psi_y^j} \\
                  & = -2 \sum_{i=1}^n \op{tr}(Q_i^\dagger \Gamma_i Q_i).
\end{align*}

利用三角不等式和上述命题，有

\begin{align*}
    \lvert W^{j+1} - W^j \rvert & \leq 2 \sum_{i=1}^n \lvert \op{tr}(Q_i^\dagger \Gamma_i Q_i) \rvert \\
                              & \leq 2 \sum_{i=1}^n \lVert \Gamma_i \rVert \lVert Q_i \rVert_F^2.
\end{align*}

又因为

\begin{align*}
    \sum_{i=1}^n \lVert Q_i \rVert_F^2 & = \sum_{i=1}^n \sum_{x,y \in S} \lvert \bra{y} Q_i \ket{x} \rvert^2 \\
                                       & = \sum_{i=1}^n \sum_{x \in S} \lvert a_x \rvert^2 \lVert P_i \ket{\psi_x^j} \rVert^2 \\
                                       & \leq \sum_{x \in S} \lvert a_x \rvert^2 \bra{\psi_x^j} I \ket{\psi_x^j} \\
                                       & = 1,
\end{align*}

所以

\[
    \lvert W^{j+1} - W^j \rvert \leq 2 \max_{i \in [n]} \lVert \Gamma_i \rVert.
\]

因为 $\lvert W^0 \rvert = \lVert \Gamma \rVert$，所以

\[
    \lvert W^t \rvert \geq \lVert \Gamma \rVert - 2 t \max_{i \in [n]} \lVert \Gamma_i \rVert.
\]

为了满足 $\lvert W^t \rvert \leq 2 \sqrt{\varepsilon(1-\varepsilon)} \lVert \Gamma \rVert$，必须有

\[
    t \geq \frac{(1 - 2 \sqrt{\varepsilon(1-\varepsilon)})}{2} \op{Adv}(f),
\]

其中

\[
    \op{Adv}(f) := \max_{\Gamma} \frac{\lVert \Gamma \rVert}{\max_{i \in [n]} \lVert \Gamma_i \rVert},
\]

最大值取遍 $f$ 的所有敌手矩阵 $\Gamma$.

## Example: Unstructured search

接下来应用该方法证明 Grover 算法的最优性. 只需考虑区分无标记项和位置未知的唯一标记项. 考虑部分函数，其中 $S$ 包含了 Hamming 重量为 $0$ 或 $1$ 的字符串，$f$ 为输入位的逻辑或. 这个问题的敌手矩阵形式为

\[
    \Gamma = \begin{pmatrix}
        0 & \gamma_1 & \cdots & \gamma_n \\
        \gamma_1 & 0 & \cdots & 0 \\
        \vdots & \vdots & \ddots & \vdots \\
        \gamma_n & 0 & \cdots & 0
    \end{pmatrix},
\]

对称性其实表明 $\gamma_1 = \gamma_2 = \cdots = \gamma_n$，这可被证明，但此处认为其是假设. 设 $\gamma_1 = \cdots = \gamma_n = 1$. 那么有

\[
    \Gamma^2 = \begin{pmatrix}
        n & 0 & \cdots & 0 \\
        0 & 1 & \cdots & 1 \\
        \vdots & \vdots & \ddots & \vdots \\
        0 & 1 & \cdots & 1
    \end{pmatrix}.
\]

即 $\lVert \Gamma^2 \rVert = n$，所以 $\lVert \Gamma \rVert = \sqrt{n}$. 此外，

\[
    \Gamma_1 = \begin{pmatrix}
        0 & 1 & 0 & \cdots & 0 \\
        1 & 0 & 0 & \cdots & 0 \\
        0 & 0 & 0 & \cdots & 0 \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & 0 & \cdots & 0
    \end{pmatrix},
\]

并且其他 $\Gamma_i$ 形式类似. 因此 $\lVert \Gamma_i \rVert = 1$. 也就是说 $\op{Adv}(\mathrm{OR}) \geq \sqrt{n}$，从而 $Q_{\varepsilon}(\mathrm{OR}) \geq \frac{(1 - 2 \sqrt{\varepsilon(1-\varepsilon)})}{2} \sqrt{n}$，这表明 Grover 算法在忽略常数因子的情况下是最优的，其用 $\frac{\pi}{4} \sqrt{n} + o(1)$ 次查询以 $1 - o(1)$ 的成功概率找到唯一标记项.