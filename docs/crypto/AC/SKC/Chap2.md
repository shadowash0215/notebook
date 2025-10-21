# Encryption

## Shannon ciphers and perfect security

使用共享密钥加密信息的基础机制叫做**密码**（cipher）或**加密系统**（encryption scheme）.

!!! note "Shannon cipher"
    Shannon 密码是满足如下机制的函数对 $\mathcal{E} = (E, D)$.

    - **加密函数** $E$ 接受**密钥** $k$ 和**信息**（也称明文 plaintext） $m$ 作为输入，产生的输出作为**密文**（ciphertext） $c$. 即
      
        \[
            c = E(k, m),
        \]

        称 $c$ 为 $m$ 在密钥 $k$ 下的加密.

    - **解密函数** $D$ 接受密钥 $k$ 和密文 $c$ 作为输入，产生的输出作为明文 $m$. 即

        \[
            m = D(k, c),
        \]

        称 $m$ 为 $c$ 在密钥 $k$ 下的解密.

    - 解密应当消除加密的作用，所以密码需要满足**正确性**（correctness）：

        \[
            D(k, E(k, m)) = m,
        \]

        对所有可能的密钥 $k$ 和明文 $m$ 都成立.

设 $\mathcal{K}$ 为所有可能的密钥的集合，$\mathcal{M}$ 为所有可能的明文的集合，$\mathcal{C}$ 为所有可能的密文的集合，分别被称为**密钥空间**、**明文空间**和**密文空间**. 所以可以写出以上函数的定义域和值域：

\begin{gather*}
    E: \mathcal{K} \times \mathcal{M} \to \mathcal{C}, \\
    D: \mathcal{K} \times \mathcal{C} \to \mathcal{M}.
\end{gather*}

即 $\mathcal{E}$ 定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上.

??? example
    - **一次一密**（one-time pad, OTP）密码 $\mathcal{E} = (E, D)$ 便是一个 Shannon 密码，其密钥、消息、密文都是等长的二进制串. 形式化的话，$\mathcal{E}$ 定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上，其中

        \[
            \mathcal{K} = \mathcal{M} = \mathcal{C} = \{0, 1\}^L,
        \]

        $L$ 是一个固定的正整数. 对任意的 $k \in \mathcal{K}$ 和 $m \in \mathcal{M}$, 定义加密函数为

        \[
            E(k, m) = k \oplus m;
        \]

        而对于任意的 $k \in \mathcal{K}$ 和 $c \in \mathcal{C}$, 定义解密函数为

        \[
            D(k, c) = k \oplus c.
        \]

        $\oplus$ 表示按位异或操作. 可以验证 $\mathcal{E}$ 满足正确性.

    - **可变长一次一密**（variable-length OTP）密码 $\mathcal{E} = (E, D)$ 也是一个 Shannon 密码，其中密钥为定长 $L$ 的比特串，但消息和密文都是长度至多为 $L$ 的可变长比特串. 形式化的话，$\mathcal{E}$ 定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上，其中

        \[
            \mathcal{K} = \{0, 1\}^L, \quad \mathcal{M} = \mathcal{C} = \{0, 1\}^{\le L}.
        \]

        对任意的 $k \in \mathcal{K}$ 和长度为 $l$ 的消息 $m \in \mathcal{M}$, 定义加密函数为

        \[
            E(k, m) = k[0:l-1] \oplus m;
        \]

        而对于任意的 $k \in \mathcal{K}$ 和长度为 $l$ 的密文 $c \in \mathcal{C}$, 定义解密函数为

        \[
            D(k, c) = k[0:l-1] \oplus c.
        \]

        其中 $k[0:l-1]$ 表示 $k$ 的前 $l$ 位. 可以验证 $\mathcal{E}$ 满足正确性.

    - **置换密码**（substitution cipher）$\mathcal{E} = (E, D)$ 是满足如下形式的 Shannon 密码. 设 $\Sigma$ 为一个带有空格 $ $ 的有限字母表，消息空间 $\mathcal{M}$ 和密文空间 $\mathcal{C}$ 都是长度为 $L$ 的 $\Sigma$-串，即

        \[
            \mathcal{M} = \mathcal{C} = \Sigma^L.
        \]

        密钥空间 $\mathcal{K}$ 是所有 $\Sigma$ 上的置换的集合，即任意 $k \in \mathcal{K}$ 都是 $\Sigma$ 到 $\Sigma$ 的双射，且 $\lvert \mathcal{K} \rvert = (\lvert \Sigma \rvert)!$. 

        对任意的 $k \in \mathcal{K}$ 和 $m \in \mathcal{M}$, 定义加密函数为

        \[
            E(k, m) = (k(m[0]), k(m[1]), \ldots, k(m[L-1]));
        \]

        而对于任意的 $k \in \mathcal{K}$ 和 $c \in \mathcal{C}$, 定义解密函数为

        \[
            D(k, c) = (k^{-1}(c[0]), k^{-1}(c[1]), \ldots, k^{-1}(c[L-1])).
        \]

        正确性也是自明的.

    - **加性一次一密**（additive OTP）：也可以使用模 $n$ 加法定义一种一次一密的变体，设其为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的加密系统 $\mathcal{E} = (E, D)$，其中 $\mathcal{K} = \mathcal{M} = \mathcal{C} = \{0, 1, \ldots, n-1\}$，$n$ 为某一正整数.加密函数和解密函数分别定义为

        \[
            E(k, m) = m + k \mod n, \quad D(k, c) = c - k \mod n.
        \]

        正确性自明.

记 $\mathsf{k}$ 表示随机密钥的随机变量，对消息 $m$，$E(\mathsf{k}, m)$ 表示在随机密钥 $\mathsf{k}$ 下消息 $m$ 的随机密文. 

!!! info "perfect security"
    $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的 Shannon 密码. 考虑 $\mathsf{k}$ 在 $\mathcal{K}$ 上均匀分布的情形. 如果对于任意的 $m_0, m_1 \in \mathcal{M}$ 和 $c \in \mathcal{C}$ 都有

    \[
        \Pr{E(\mathsf{k}, m_0) = c} = \Pr{E(\mathsf{k}, m_1) = c},
    \]

    则称 $\mathcal{E}$ 是**完美安全**（perfectly secure）的. 

完美安全有一系列等价定义.

!!! note "Theorem"
    设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的 Shannon 密码，以下命题等价：

    1. $\mathcal{E}$ 是完美安全的.

    2. 对每个 $c \in \mathcal{C}$，存在依赖于 $c$ 的 $N_c$，使得对于任意的 $m \in \mathcal{M}$ 都有

        \[
            \lvert \{ k \in \mathcal{K} : E(k, m) = c \} \rvert = N_c.
        \]

    3. 若 $\mathsf{k}$ 在 $\mathcal{K}$ 上均匀分布，那么对于任一 $m \in \mathcal{M}$，$E(\mathsf{k}, m)$ 都是同分布的.

    ???+ note "Proof"
        首先重新叙述第 2 个命题. 对每个 $c \in \mathcal{C}$，存在依赖于 $c$ 的值 $P_c$，使得对于任意的 $m \in \mathcal{M}$ 都有

        \[
            \Pr{E(\mathsf{k}, m) = c} = P_c.
        \]

        注意到 $P_c = \frac{N_c}{\lvert \mathcal{K} \rvert}$. 显然此描述等价于第 3 个命题.

        $(1 \Rightarrow 2)$ 设 $c \in \mathcal{C}$ 是一个固定的密文. 任意选取消息 $m_0 \in \mathcal{M}$，且 $P_c = \Pr{E(\mathsf{k}, m_0) = c}$. 依据 1 可知对任意 $m \in \mathcal{M}$ 都有 $\Pr{E(\mathsf{k}, m) = c} = \Pr{E(\mathsf{k}, m_0) = c} = P_c$. 即证明了 2.

        $(2 \Rightarrow 1)$ 考虑任意固定的 $m_0, m_1 \in \mathcal{M}$ 和 $c \in \mathcal{C}$. 依据 2 可知

        \[
            \Pr{E(\mathsf{k}, m_0) = c} = P_c = \Pr{E(\mathsf{k}, m_1) = c}.
        \]

        这便是 1.

!!! note "Theorem"
    一次一密密码是完美安全的.

    ???+ note "Proof"
        考虑 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的一次一密密码，其中 $\mathcal{K} = \mathcal{M} = \mathcal{C} = \{0, 1\}^L$. 对任意的 $m \in \mathcal{M}$ 和 $c \in \mathcal{C}$，存在唯一的 $k \in \mathcal{K}$ 满足

        \[
            E(k, m) = k \oplus m = c.
        \]

        即 $k = m \oplus c$. 所以 $\lvert \{ k \in \mathcal{K} : E(k, m) = c \} \rvert = N_c = 1$. 依据前一条定理，$\mathcal{E}$ 是完美安全的.

??? example
    - 可变长一次一密密码则不是完美安全的. 考虑选取了任意一个长度为 $1$ 的消息 $m_0$，以及长度为 $2$ 的消息 $m_1$. 考虑任意长度为 $1$ 的密文 $c$，以及 $\mathsf{k}$ 在 $\mathcal{K}$ 上均匀分布的情形. 则

        \[
            \Pr{E(\mathsf{k}, m_0) = c} = \frac{1}{2}, \quad \Pr{E(\mathsf{k}, m_1) = c} = 0.   
        \]

        这便是完美安全定义的一个直接反例.

        可变长一次一密密码并非完美安全的重要原因在于其泄露了消息的长度信息. 但有时也可以通过 `padding` 方法来避免这个问题.

    - 有多种方法来考虑置换密码也并非完美安全的. 选取满足以下条件的消息 $m_0, m_1 \in \mathcal{M}$：

        \[
            m_0[0] = m_1[0], \quad m_0[1] \neq m_1[1].
        \]

        那么对于任一密钥 $k \in \mathcal{K}$，若 $c = E(k, m_0)$，则 $c[0] = c[1]$；而若 $c = E(k, m_1)$，则 $c[0] \neq c[1]$. 由此可以得出，虽然 $\mathsf{k}$ 在 $\mathcal{K}$ 上均匀分布，但 $E(\mathsf{k}, m_0)$ 和 $E(\mathsf{k}, m_1)$ 并非同分布的.

        而显然，如果置换密码用于加密某些具有固定格式的消息，如英文邮件等，敌手便可以利用格式来确定某些字母表中的符号被加密成了哪些符号，从而进行频率分析攻击，这也是置换密码不完美安全的另一种体现.

    - 加性一次一密密码是完美安全的. 证明与一次一密密码类似.

接下来定义密文空间上的谓词函数 $\phi: \mathcal{C} \to \{\mathrm{True}, \mathrm{False}\}$，窃听者可以利用这些谓词函数分析密文，进而获取关于明文的信息. 但完美安全的密码便可以阻断这些分析.

!!! note "Theorem"
    设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的 Shannon 密码，$\mathsf{k}$ 在 $\mathcal{K}$ 上均匀分布. 那么 $\mathcal{E}$ 是完美安全的当且仅当对于任意的谓词函数 $\phi: \mathcal{C} \to \{\mathrm{True}, \mathrm{False}\}$ 和任意的 $m_0, m_1 \in \mathcal{M}$ 都有

    \[
        \Pr{\phi(E(\mathsf{k}, m_0))} = \Pr{\phi(E(\mathsf{k}, m_1))}.
    \]

    ???+ note "Proof"
        $(\Rightarrow)$ 设 $\mathcal{E}$ 是完美安全的. 定义 $S = \{ c \in \mathcal{C} : \phi(c) \}$. 则

        \[
            \Pr{\phi(E(\mathsf{k}, m_0))} = \sum_{c \in S} \Pr{E(\mathsf{k}, m_0) = c} = \sum_{c \in S} \Pr{E(\mathsf{k}, m_1) = c} = \Pr{\phi(E(\mathsf{k}, m_1))}.
        \]

        $(\Leftarrow)$ 假设 $\mathcal{E}$ 不是完美安全的. 则存在 $m_0, m_1 \in \mathcal{M}$ 和 $c \in \mathcal{C}$ 使得

        \[
            \Pr{E(\mathsf{k}, m_0) = c} \neq \Pr{E(\mathsf{k}, m_1) = c}.
        \]

        定义谓词函数 $\phi: \mathcal{C} \to \{\mathrm{True}, \mathrm{False}\}$ 只在 $c$ 处取 $\mathrm{True}$，其他地方取 $\mathrm{False}$. 则

        \[
            \Pr{\phi(E(\mathsf{k}, m_0))} = \Pr{E(\mathsf{k}, m_0) = c} \neq \Pr{E(\mathsf{k}, m_1) = c} = \Pr{\phi(E(\mathsf{k}, m_1))},
        \]

        这与假设矛盾.

下一个定理从另一个角度表明完美密码不揭示消息的任何信息. 考虑 $\mathsf{m}$ 为 $\mathcal{M}$ 上的任意随机变量，$\mathsf{k}$ 在 $\mathcal{K}$ 上均匀分布，且独立于 $\mathsf{m}$. 定义 $\mathsf{c} = E(\mathsf{k}, \mathsf{m})$ 为密文空间上的随机变量. 接下来的定理表明完美安全性保证了 $\mathsf{m}$ 和 $\mathsf{c}$ 独立. 而评判独立性的依据便是条件概率. 一种是对于任意以非零概率产生的密文 $c \in \mathcal{C}$ 和任意 $m \in \mathcal{M}$ 都有

\[
    \Pr{\mathsf{m} = m \mid \mathsf{c} = c} = \Pr{\mathsf{m} = m}.
\]

这意味着获取密文后并没有得到关于消息的任何信息. 另一种是对于任意以非零概率产生的消息 $m \in \mathcal{M}$ 和任意 $c \in \mathcal{C}$ 都有

\[
    \Pr{\mathsf{c} = c \mid \mathsf{m} = m} = \Pr{\mathsf{c} = c}.
\]

这意味着消息的选择并不会影响密文的分布.

!!! note "Theorem"
    设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的 Shannon 密码. 考虑满足以下性质的随机变量 $\mathsf{k}$ 和 $\mathsf{m}$：

    - $\mathsf{k}$ 在 $\mathcal{K}$ 上均匀分布.

    - $\mathsf{m}$ 为 $\mathcal{M}$ 上的任意随机变量.

    - $\mathsf{k}$ 和 $\mathsf{m}$ 独立.

    定义 $\mathsf{c} = E(\mathsf{k}, \mathsf{m})$ 为 $\mathcal{C}$ 上的随机变量. 那么：

    - 如果 $\mathcal{E}$ 是完美安全的，那么 $\mathsf{m}$ 和 $\mathsf{c}$ 独立.

    - 如果 $\mathsf{m}$ 和 $\mathsf{c}$ 独立，并且任意消息 $m \in \mathcal{M}$ 产生的概率都不为零，那么 $\mathcal{E}$ 是完美安全的.

    ???+ note "Proof"
        $(\Rightarrow)$ 设 $\mathcal{E}$ 是完美安全的. 考虑固定的 $m \in \mathcal{M}$ 和 $c \in \mathcal{C}$，希望证明

        \[
            \Pr{\mathsf{c} = c \wedge \mathsf{m} = m} = \Pr{\mathsf{c} = c} \Pr{\mathsf{m} = m}.
        \]

        首先有

        \begin{align*}
            \Pr{\mathsf{c} = c \wedge \mathsf{m} = m} &= \Pr{E(\mathsf{k}, \mathsf{m}) = c \wedge \mathsf{m} = m} \\
            &= \Pr{E(\mathsf{k}, m) = c \wedge \mathsf{m} = m} \\
            &= \Pr{E(\mathsf{k}, m) = c} \Pr{\mathsf{m} = m}.
        \end{align*}

        最后一行是因为 $\mathsf{k}$ 和 $\mathsf{m}$ 独立. 接下来便希望证明 $\Pr{E(\mathsf{k}, m) = c} = \Pr{\mathsf{c} = c}$，从而完成证明. 而依据全概率和完美安全性，有

        \begin{align*}
            \Pr{\mathsf{c} = c} &= \Pr{E(\mathsf{k}, \mathsf{m}) = c} \\
            &= \sum_{m' \in \mathcal{M}} \Pr{E(\mathsf{k}, \mathsf{m}) = c \wedge \mathsf{m} = m'} \\
            &= \sum_{m' \in \mathcal{M}} \Pr{E(\mathsf{k}, m') = c \wedge \mathsf{m} = m'} \\
            &= \sum_{m' \in \mathcal{M}} \Pr{E(\mathsf{k}, m') = c} \Pr{\mathsf{m} = m'} \\
            &= \sum_{m' \in \mathcal{M}} \Pr{E(\mathsf{k}, m) = c} \Pr{\mathsf{m} = m'} \\
            &= \Pr{E(\mathsf{k}, m) = c} \sum_{m' \in \mathcal{M}} \Pr{\mathsf{m} = m'} \\
            &= \Pr{E(\mathsf{k}, m) = c}.
        \end{align*}

        命题得证.

        $(\Leftarrow)$ 设 $\mathsf{m}$ 和 $\mathsf{c}$ 独立，且任意消息 $m \in \mathcal{M}$ 产生的概率都不为零. 设 $m \in \mathcal{M}$ 和 $c \in \mathcal{C}$，希望证明

        \[
            \Pr{E(\mathsf{k}, m) = c} = \Pr{\mathsf{c} = c}.
        \]

        由此便可以得到完美安全性. 而因为 $\Pr{\mathsf{m} = m} \neq 0$，所以

        \begin{align*}
            \Pr{E(\mathsf{k}, m) = c} \Pr{\mathsf{m} = m} &= \Pr{E(\mathsf{k}, m) = c \wedge \mathsf{m} = m} \\
            &= \Pr{E(\mathsf{k}, \mathsf{m}) = c \wedge \mathsf{m} = m} \\
            &= \Pr{\mathsf{c} = c \wedge \mathsf{m} = m} \\
            &= \Pr{\mathsf{c} = c} \Pr{\mathsf{m} = m}.
        \end{align*}

那么，代价是什么？接下来的定理将证明在完美安全的领域没有比一次一密更好的选择了，因为密钥至少需要和消息一样长. 因此，实践中几乎没法使用完美安全的密码.

!!! note "Shannon's theorem"
    设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的 Shannon 密码. 如果 $\mathcal{E}$ 是完美安全的，则 $\lvert \mathcal{K} \rvert \geq \lvert \mathcal{M} \rvert$.

    ???+ note "Proof"
        设 $\lvert \mathcal{K} \rvert < \lvert \mathcal{M} \rvert$，希望证明 $\mathcal{E}$ 不是完美安全的. 为了完成这个目标，最后会证明存在消息 $m_0, m_1 \in \mathcal{M}$ 和密文 $c \in \mathcal{C}$ 使得

        \begin{gather*}
            \Pr{E(\mathsf{k}, m_0) = c} > 0, \\
            \Pr{E(\mathsf{k}, m_1) = c} = 0.
        \end{gather*}

        任意选取 $m_0 \in \mathcal{M}$，以及 $k_0 \in \mathcal{K}$，定义 $c = E(k_0, m_0)$. 显然 $\Pr{E(\mathsf{k}, m_0) = c} > 0$. 接下来定义

        \[
            S = \{ D(k_1, c) : k_1 \in \mathcal{K} \}.
        \]

        显然

        \[
            \lvert S \rvert \leq \lvert \mathcal{K} \rvert < \lvert \mathcal{M} \rvert.
        \]

        所以可以选择 $m_1 \in \mathcal{M} \setminus S$. 接下来只需证明不存在 $k_1 \in \mathcal{K}$ 使得 $E(k_1, m_1) = c$. 假设存在这样的 $k_1$，则依据正确性，有

        \[
            D(k_1, c) = D(k_1, E(k_1, m_1)) = m_1,
        \]

        这表明 $m_1 \in S$，与 $m_1$ 的选取矛盾. 因此 $\Pr{E(\mathsf{k}, m_1) = c} = 0$. 这便证明了 $\mathcal{E}$ 不是完美安全的.

## Computational ciphers and semantic security

为了和实用性妥协，需要松弛安全性的定义. 也就是说，不再考虑所有的敌手，而只考虑**计算上可行**（computationally feasible）的敌手. 这便引出了一个稍弱的安全性定义，称为**语义安全**（semantic security）.

**计算密码**（computational cipher）$\mathcal{E} = (E, D)$ 看起来和 Shannon 密码类似，但允许加密算法为随机算法. 即对于固定的 $k$ 和 $m$，$E(k, m)$ 的结果可能是多个候选值中的一个. 将执行 $E(k, m)$ 以及将结果赋值为程序变量 $c$ 的过程记为

\[
    c \xleftarrow{\mathrm{R}} E(k, m).
\]

这个记号将会贯穿全文，在所有与随机算法相关的地方都会使用. 同理，也可以将从 $\mathcal{K}$ 中随机均匀选取一个元素赋值给程序变量 $k$ 的过程记为

\[
    k \xleftarrow{\mathrm{R}} \mathcal{K}.
\]

因为加密算法可以是随机算法，所以需要更严格的阐述正确性. 即对于任意密钥 $k \in \mathcal{K}$ 和任意消息 $m \in \mathcal{M}$，如果执行

\[
    c \xleftarrow{\mathrm{R}} E(k, m), \quad m' \leftarrow D(k, c),
\]

那么 $m' = m$ 以概率 $1$ 成立.

自此开始，当谈及密码时，均默认其为计算密码. 而如果加密函数恰为确定性函数，则称其为**确定性密码**（deterministic cipher）. 显然确定性密码是 Shannon 密码，但计算密码和 Shannon 密码互不包含.

语义安全的弱化方向在于谓词，即不再要求严格相等，而是容忍**可忽略的**（negligible）差异. 即

\[
    \lvert \Pr{\phi(E(\mathsf{k}, m_0))} - \Pr{\phi(E(\mathsf{k}, m_1))} \rvert \leq \varepsilon.
\]

仅此而已还不够，面向的对象也需要进行放宽. 上式只要求对能被高效生成的消息 $m_0, m_1$ 和能被高效计算的谓词函数 $\phi$ 成立，这里使用到的算法都可以是概率性的.

为了精确规范语义安全的定义，需要描述一个两方的攻击游戏，一方为挑战者，一方为敌手. 挑战者遵循简单固定的协议，而敌手 $\mathcal{A}$ 可以遵照任意高效的协议.

!!! danger "Attack game"
    给定定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的计算密码 $\mathcal{E} = (E, D)$，以及敌手 $\mathcal{A}$，定义两个实验，实验 $0$ 和实验 $1$.

    实验 $b$ 的流程如下：
    
    - 敌手计算等长的消息 $m_0, m_1 \in \mathcal{M}$，并将其发送给挑战者.

    - 挑战者计算 $k \xleftarrow{\mathrm{R}} \mathcal{K}$，以及 $c \xleftarrow{\mathrm{R}} E(k, m_b)$，并将 $c$ 发送给敌手.

    - 敌手输出 $\hat{b} \in \{0, 1\}$.

    \automata
        \draw (0, 0) rectangle (4, 7);
        \draw (6, 0) rectangle (9, 7);
        \node at (2, 6.5) {Challenger};
        \node at (2, 5.5) {Experiment $b$};
        \node at (2, 4.5) {$k \xleftarrow{\mathrm{R}} \mathcal{K}$};
        \node at (2, 3.5) {$c \xleftarrow{\mathrm{R}} E(k, m_b)$};
        \node at (7.5, 6.5) {$\mathcal{A}$};
        \draw[->] (6, 5) -- node[above]{$m_0, m_1 \in \mathcal{M}$} (4, 5);
        \draw[->] (4, 3) -- node[above]{$c \in \mathcal{C}$} (6, 3);
        \draw[->] (6, 1) -- node[above]{$\hat{b} \in \{0, 1\}$} (4, 1);

    对于 $b = 0, 1$，定义 $W_b$ 为 $\mathcal{A}$ 在实验 $b$ 中输出 $1$ 的事件. 进而定义 $\mathcal{A}$ 关于 $\mathcal{E}$ 的语义安全**优势**（semantic security advantage）为

    \[
        \mathrm{SS} \mathsf{adv}[\mathcal{A}, \mathcal{E}] = \lvert \Pr{W_0} - \Pr{W_1} \rvert.
    \]

!!! info "Semantic security"
    $\mathcal{E}$ 是**语义安全**的（semantically secure），如果对于任意的高效敌手 $\mathcal{A}$，$\mathcal{A}$ 关于 $\mathcal{E}$ 的语义安全优势 $\mathrm{SS} \mathsf{adv}[\mathcal{A}, \mathcal{E}]$ 是可忽略的.

    !!! tip "Remark"
        - 对随机算法的处理关键在于将其视为先生成随机数 $r$，然后将 $r$ 作为算法的一个输入，也就是所谓的**随机种子**（random seed）. 

        - 语义安全的定义中，对消息 $m_0, m_1$ 必须等长的讨论如下：

            - 消息长度的定义依赖于消息空间 $\mathcal{M}$ 的结构. 为了定义的普适性，此处选择将长度抽象化，毕竟有些消息（如数字）并没有显然的长度概念.

            - 要求 $m_0, m_1$ 等长是为了避免敌手仅仅通过消息长度来区分消息，因为密文长度通常和消息长度相关. 但这种区分并不能反应密码在保护内容方面的实际能力.

接下来是对“高效”和“可忽略”的更详尽的解释：

- 高效的敌手的运行时间是“合理”的.

- 若 $1/N$ 是可忽略的，则称 $N$ 是**超多项式**（super-polynomial）的.

- 一个**多项式约束**（poly-bounded）值是“合理”大小的，所以可以说高效敌手的运行时是多项式约束的.

!!! info "Fact"
    设 $\varepsilon, \varepsilon'$ 是两个可忽略的值，$Q, Q'$ 是两个多项式约束的值. 那么 

    - $\varepsilon + \varepsilon'$ 是可忽略的.

    - $Q + Q'$, $Q \cdot Q'$ 是多项式约束的.

    - $Q \cdot \varepsilon$ 是可忽略的.

**消息恢复攻击**（message recovery attack）是指给定密文 $c$，敌手试图恢复出消息 $m$ 的概率远优于随机猜测概率 $1/\lvert \mathcal{M} \rvert$ 的攻击. 这显然是安全性需要排除的攻击，语义安全也确实排除了这种攻击.

!!! danger "Message Recovery"
    对定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的计算密码 $\mathcal{E} = (E, D)$，以及敌手 $\mathcal{A}$，这一攻击游戏按如下流程进行：

    - 挑战者计算 $m \xleftarrow{\mathrm{R}} \mathcal{M}$，$k \xleftarrow{\mathrm{R}} \mathcal{K}$，以及 $c \xleftarrow{\mathrm{R}} E(k, m)$，并将 $c$ 发送给敌手.

    - 敌手输出 $\hat{m} \in \mathcal{M}$.

    设 $W$ 为 $\mathcal{A}$ 在该攻击游戏中成功输出 $\hat{m} = m$ 的事件. 定义 $\mathcal{A}$ 关于 $\mathcal{E}$ 的消息恢复优势（message recovery advantage）为

    \[
        \mathrm{MR} \mathsf{adv}[\mathcal{A}, \mathcal{E}] = \lvert \Pr{W} - 1/\lvert \mathcal{M} \rvert \rvert.
    \]

!!! info "security against message recovery"
    $\mathcal{E}$ 是**针对消息恢复攻击安全的**（secure against message recovery），如果对于任意的高效敌手 $\mathcal{A}$，$\mathcal{A}$ 关于 $\mathcal{E}$ 的消息恢复优势 $\mathrm{MR} \mathsf{adv}[\mathcal{A}, \mathcal{E}]$ 是可忽略的.

!!! note "Theorem"
    设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的计算密码. 如果 $\mathcal{E}$ 是语义安全的，那么 $\mathcal{E}$ 是针对消息恢复攻击安全的.

    ???+ note "Proof"
        设 $\mathcal{E}$ 是语义安全的，考虑任意高效敌手 $\mathcal{A}$，希望证明 $\mathcal{A}$ 关于 $\mathcal{E}$ 的消息恢复优势 $\mathrm{MR} \mathsf{adv}[\mathcal{A}, \mathcal{E}]$ 是可忽略的. 

        设 $p$ 为 $\mathcal{A}$ 在游戏中获胜的概率，所以优势可以写作

        \[
            \mathrm{MR} \mathsf{adv}[\mathcal{A}, \mathcal{E}] = \lvert p - 1/\lvert \mathcal{M} \rvert \rvert.
        \]

        接下来将展示如何构建一个高效敌手 $\mathcal{B}$，使得 $\mathcal{B}$ 关于 $\mathcal{E}$ 的语义安全优势满足

        \[
            \mathrm{MR} \mathsf{adv}[\mathcal{A}, \mathcal{E}] \leq \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}].
        \]

        而因为 $\mathcal{E}$ 是语义安全的，所以 $\mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}]$ 是可忽略的，从而 $\mathrm{MR} \mathsf{adv}[\mathcal{A}, \mathcal{E}]$ 也是可忽略的.

        所以只需要构建 $\mathcal{B}$ 并证明上述不等式即可完成证明，构造 $\mathcal{B}$ 的过程不需要了解 $\mathcal{A}$ 的内部细节. 

        $\mathcal{B}$ 生成两条随机消息 $m_0, m_1 \xleftarrow{\mathrm{R}} \mathcal{M}$，并将其发送给其 $\mathrm{SS}$ 挑战者，该挑战者将密文 $c \xleftarrow{\mathrm{R}} E(k, m_b)$ 发送给 $\mathcal{B}$，其中 $b \in \{0, 1\}$ 是随机选取的. $\mathcal{B}$ 将 $c$ 前递给 $\mathcal{A}$，扮演 $\mathcal{A}$ 的 $\mathrm{MR}$ 挑战者. $\mathcal{A}$ 输出 $\hat{m} \in \mathcal{M}$，$\mathcal{B}$ 检查 $\hat{m}$ 是否等于 $m_1$，如果相等则输出 $1$，否则输出 $0$.

        显然 $\mathcal{B}$ 是高效的. 对 $b = 0, 1$，定义 $p_b$ 为 $\mathcal{B}$ 的 $\mathrm{SS}$ 挑战者加密 $m_b$ 时 $\mathcal{B}$ 输出 $1$ 的概率. 依据定义，有

        \[
            \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}] = \lvert p_1 - p_0 \rvert.
        \]

        一方面，若 $c$ 是 $m_1$ 的加密结果，则 $p_1$ 即为 $\mathcal{A}$ 在 $\mathrm{MR}$ 游戏中获胜的概率 $p$，即 $p_1 = p$；另一方面，若 $c$ 是 $m_0$ 的加密结果，则 $\mathcal{A}$ 的输出独立于 $m_1$，所以 $\hat{m}$ 恰好等于 $m_1$ 的概率为 $1/\lvert \mathcal{M} \rvert$，即 $p_0 = 1/\lvert \mathcal{M} \rvert$. 综上所述，有

        \[
            \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}] = \lvert p_1 - p_0 \rvert = \lvert p - 1/\lvert \mathcal{M} \rvert \rvert = \mathrm{MR} \mathsf{adv}[\mathcal{A}, \mathcal{E}].
        \]

        同样也可以利用反证法证明，即如果 $\mathcal{E}$ 不是针对消息恢复攻击安全的，那么 $\mathcal{E}$ 也不是语义安全的. 这里不再赘述.

这种以黑盒形式利用某个问题的高效敌手 $\mathcal{A}$ 构造另一个问题的高效敌手 $\mathcal{B}$ 的技术在密码学中非常常见，此处先给出一个不正式的定义. “作为黑盒使用” 的意思是 $\mathcal{B}$ 并不需要了解 $\mathcal{A}$ 的内部细节，只关注 $\mathcal{A}$ 的输入输出行为. $\mathcal{B}$ 通过一个“接口层”与 $\mathcal{A}$ 的一个运行实例交互. 虽然理想情况下希望“接口层”的计算复杂度不依赖于 $\mathcal{A}$ 的复杂度，但某种依赖是不可避免的；如果一个攻击游戏允许 $\mathcal{A}$ 与其挑战者进行多次请求，那么“接口层”的工作量显然是与 $\mathcal{A}$ 请求的次数成正比的，但不应依赖于 $\mathcal{A}$ 的运行时间.

按照以上方法进行构造得到的 $\mathcal{B}$ 称为 $\mathcal{A}$ 的一个**初等包装**（elementary wrapper），具有如下性质：

- 若 $\mathcal{B}$ 是 $\mathcal{A}$ 的一个初等包装，并且 $\mathcal{A}$ 是高效的，那么 $\mathcal{B}$ 也是高效的.

- 若 $\mathcal{C}$ 是 $\mathcal{B}$ 的一个初等包装，并且 $\mathcal{B}$ 是 $\mathcal{A}$ 的一个初等包装，那么 $\mathcal{C}$ 也是 $\mathcal{A}$ 的一个初等包装.

如果一个密码是安全的，那么不仅不应该能够恢复消息，甚至连消息的某些部分信息也不应该泄露. 接下来并不是证明一个完整的定理，而是考虑一个具体的例子.

设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的计算密码，其中 $\mathcal{M} = \{0, 1\}^L$. 对 $m \in \mathcal{M}$，若 $m$ 中 $1$ 的个数为奇数，那么 $\mathrm{parity}(m) = 1$，否则 $\mathrm{parity}(m) = 0$，即 $\mathrm{parity}(m)$ 为 $m$ 所有位的异或和. 接下来将展示，若 $\mathcal{E}$ 是语义安全的，那么即使给定一个随机消息 $m$ 的加密结果 $c$，也很难预测 $m$ 的奇偶性，即不能比随机猜测的 $1/2$ 好多少.

如果存在一个高效敌手 $\mathcal{A}$，使得其预测 $\mathrm{parity}(m)$ 的概率始终为 $1$. 进而便可以利用 $\mathcal{A}$ 构造一个 $\mathrm{SS}$ 敌手 $\mathcal{B}$，其任意生成两条信息 $m_0, m_1 \in \mathcal{M}$，使得 $\mathrm{parity}(m_0) = 0$ 且 $\mathrm{parity}(m_1) = 1$. $\mathcal{B}$ 将 $m_0, m_1$ 发送给其 $\mathrm{SS}$ 挑战者，该挑战者将密文 $c \xleftarrow{\mathrm{R}} E(k, m_b)$ 发送给 $\mathcal{B}$，而后前递给 $\mathcal{A}$. $\mathcal{A}$ 输出 $\hat{b} \in \{0, 1\}$，$\mathcal{B}$ 将 $\hat{b}$ 作为自己的输出. 显然 $\mathcal{B}$ 的 $\mathrm{SS}$ 优势为 $1$.

所以如果 $\mathcal{E}$ 是语义安全的，那么对于任意高效敌手 $\mathcal{A}$，其便不能以概率 $1$ 正确预测 $\mathrm{parity}(m)$. 但语义安全还可以做得更好：事实上不存在高效敌手 $\mathcal{A}$，使得其预测 $\mathrm{parity}(m)$ 的概率显著大于 $1/2$. 

!!! danger "parity prediction"
    设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的计算密码. 设 $\mathcal{A}$ 为一个高效敌手，攻击游戏的流程如下：

    - 挑战者计算 $m \xleftarrow{\mathrm{R}} \mathcal{M}$，$k \xleftarrow{\mathrm{R}} \mathcal{K}$，以及 $c \xleftarrow{\mathrm{R}} E(k, m)$，并将 $c$ 发送给敌手.

    - 敌手输出 $\hat{b} \in \{0, 1\}$.

    设 $W$ 为 $\mathcal{A}$ 在该攻击游戏中成功输出 $\hat{b} = \mathrm{parity}(m)$ 的事件. 定义 $\mathcal{A}$ 关于 $\mathcal{E}$ 的奇偶性预测优势（parity prediction advantage）为

    \[
        \mathrm{Parity} \mathsf{adv}[\mathcal{A}, \mathcal{E}] = \lvert \Pr{W} - 1/2 \rvert.
    \]

!!! info "parity prediction security"
    $\mathcal{E}$ 是**针对奇偶性预测攻击安全的**（secure against parity prediction），如果对于任意的高效敌手 $\mathcal{A}$，$\mathcal{A}$ 关于 $\mathcal{E}$ 的奇偶性预测优势 $\mathrm{Parity} \mathsf{adv}[\mathcal{A}, \mathcal{E}]$ 是可忽略的.

!!! note "Theorem"
    设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的计算密码. 如果 $\mathcal{E}$ 是语义安全的，那么 $\mathcal{E}$ 是针对奇偶性预测攻击安全的.

    ???+ note "Proof"
        将证明对于每个高效敌手 $\mathcal{A}$，都存在一个 $\mathcal{A}$ 的初等包装 $\mathcal{B}$，使得

        \[
            \mathrm{Parity} \mathsf{adv}[\mathcal{A}, \mathcal{E}] = \frac{1}{2} \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}].
        \]

        设 $\mathcal{A}$ 为任意高效敌手，考虑其在上述攻击游戏中的成功概率 $1/2 + \varepsilon$，所以其优势为 $\mathrm{Parity} \mathsf{adv}[\mathcal{A}, \mathcal{E}] = \varepsilon$. 

        接下来给出 $\mathcal{B}$ 的构造. $\mathcal{B}$ 随机生成消息 $m_0$，并令 $m_1 \gets m_0 \oplus (0^{L-1} || 1)$，即 $m_1$ 和 $m_0$ 相比仅翻转最低位. 因此 $m_0, m_1$ 长度相等，且 $\mathrm{parity}(m_0) \neq \mathrm{parity}(m_1)$. $\mathcal{B}$ 将 $m_0, m_1$ 发送给其 $\mathrm{SS}$ 挑战者，接收密文 $c \xleftarrow{\mathrm{R}} E(k, m_b)$，并将 $c$ 前递给 $\mathcal{A}$. $\mathcal{A}$ 输出 $\hat{b} \in \{0, 1\}$，若 $\hat{b} = \mathrm{parity}(m_0)$，则 $\mathcal{B}$ 输出 $1$，否则输出 $0$.

        对 $b = 0, 1$，定义 $p_b$ 为 $\mathcal{B}$ 的 $\mathrm{SS}$ 挑战者加密 $m_b$ 时 $\mathcal{B}$ 输出 $1$ 的概率. 依据定义，有

        \[
            \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}] = \lvert p_1 - p_0 \rvert.
        \]

        其中 $p_0 = 1/2 + \varepsilon$，$p_1 = 1/2 - \varepsilon$，因为不论是 $m_0$ 还是 $m_1$ 被加密，$m_b$ 在 $\mathcal{M}$ 上的分布都是均匀的. 综上所述，有

        \[
            \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}] = \lvert p_1 - p_0 \rvert = 2 \lvert \varepsilon \rvert = 2 \mathrm{Parity} \mathsf{adv}[\mathcal{A}, \mathcal{E}].
        \]

接下来将用一个轮盘赌的示例来证明一个利用语义安全密码构建的更大的系统的安全性. 玩家首先给庄家一块钱，然后进行选择两种之一的方式下注：

- “大或小”

- “奇或偶”

下注完成后，庄家随机选择 $r \in \{0, 1, \ldots, 36\}$，若 $r \neq 0$，且以下条件满足之一：

- 玩家选择了“大”且 $r > 18$；

- 玩家选择了“小”且 $r \leq 18$；

- 玩家选择了“奇”且 $r$ 为奇数；

- 玩家选择了“偶”且 $r$ 为偶数.

则玩家获胜，收获两块钱，净利润为一块钱；否则输掉先前给庄家的一块钱. 显然庄家是有优势的，因为玩家获胜的概率实际为 $18/37 \approx 48.65 \%$. 

现在假定这一游戏是在网络上进行的，庄家会先公开 $r$ 的加密，玩家自然会对其分析，以求增加获胜的概率. 但如果庄家使用了语义安全的密码，那玩家的分析实际上是无用功. 设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的语义安全的密码，$\mathcal{M} = \{0, 1, \ldots, 36\}$. 此后称玩家为 $\mathcal{A}$，并且假定其策略可以建模为一个高效算法. 整个游戏过程如下图所示：

\automata
    \draw (0, 0) rectangle (4, 7);
    \draw (6, 0) rectangle (10, 7);
    \node at (2, 6.5) {House};
    \node[align=left] at (2, 5.5) {$r \xleftarrow{\mathrm{R}} \mathcal{M}$};
    \node[align=left] at (2, 4.5) {$k \xleftarrow{\mathrm{R}} \mathcal{K}$};
    \node[align=left] at (2, 3.5) {$c \xleftarrow{\mathrm{R}} E(k, r)$};
    \node at (2, 0.5) {$outcome \gets W(r, bet)$};
    \node at (8, 6.5) {$\mathcal{A}$};
    \draw[->] (4, 5) -- node[above]{$c \in \mathcal{C}$} (6, 5);
    \draw[->] (6, 3) -- node[above]{$bet$} (4, 3);
    \draw[->] (2, 0) -- node[right]{$outcome$} (2, -2);

其中 $W$ 是评估函数，如果 $W(r, bet) = 1$，则玩家获胜，否则玩家失败. 进而定义优势

\[
    \mathrm{IR}\mathsf{adv}[\mathcal{A}] = \lvert \Pr{W(r, bet) = 1} - 18/37 \rvert.
\]

$\mathrm{IR}$ 为 Internet Roulette 的缩写. 

所以目标是证明如下的定理：

!!! note "Theorem"
    若 $\mathcal{E}$ 是语义安全的，那么对于任意高效玩家 $\mathcal{A}$，$\mathrm{IR}\mathsf{adv}[\mathcal{A}]$ 是可忽略的.

    ???+ note "Proof"
        目标是构造出初等包装 $\mathcal{B}$，使得

        \[
            \mathrm{IR}\mathsf{adv}[\mathcal{A}] = \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}].
        \]

        先考虑一个理想化的版本. 这个版本庄家并不发布真实值 $r$ 的加密结果 $c$，而是发布一个“虚拟值” $0$ 的加密结果. 但庄家依然会需要一个 $r$ 来决定输赢. 记 $p_0$ 为玩家在真实游戏中获胜的概率，$p_1$ 为玩家在理想化游戏中获胜的概率. $\mathcal{B}$ 的构造如下：

        \automata
            \draw (0, 0) rectangle (3, 5);
            \node at (1.5, 4.5) {Challenger};
            \node at (1.5, 4) {(Experiment $b$)};
            \node at (1.5, 3) {$k \xleftarrow{\mathrm{R}} \mathcal{K}$};
            \node at (1.5, 2.5) {$c \xleftarrow{\mathrm{R}} E(k, m_b)$};
            \draw[dashed] (5, -0.5) rectangle (12, 5.5);
            \draw (8, 1) rectangle (11, 5);
            \node at (6.5, 5) {$\mathcal{B}$};
            \node at (6.5, 4.5) {$r \xleftarrow{\mathrm{R}} \mathcal{M}$};
            \node at (6.5, 4) {$m_0 \gets r$};
            \node at (6.5, 3.5) {$m_1 \gets 0$};
            \node at (6.5, 1.5) {$\hat{b} \gets W(r, bet)$};
            \node at (9.5, 4.5) {$\mathcal{A}$};
            \draw[->] (8, 2) -- node[above]{$bet$} (7.2, 2);
            \draw[->] (7.2, 2) -- (7.2, 1.7);
            \draw[->] (5, 3.5) -- node[above]{$m_0, m_1$} (3, 3.5);
            \draw[->] (3, 2.5) -- node[above]{$c$} (8, 2.5);
            \draw[->] (5, 1.5) -- node[above]{$\hat{b}$} (3, 1.5);

        所以如果 $\mathcal{B}$ 处于实验 $0$，那么 $\Pr{\hat{b} = 1} = p_0$；而如果 $\mathcal{B}$ 处于实验 $1$，那么 $\Pr{\hat{b} = 1} = p_1$. 进而有

        \[
            \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}] = \lvert p_1 - p_0 \rvert.
        \]

        而显然，无论 $\mathcal{A}$ 采用何种策略，$p_1 = 18/37$ 恒成立，因为 $c$ 与 $r$ 独立；而 $p_0$ 则是 $\mathcal{A}$ 在真实游戏中获胜的概率. 所以有

        \[
            \mathrm{IR} \mathsf{adv}[\mathcal{A}] = \lvert p_0 - 18/37 \rvert = \lvert p_0 - p_1 \rvert = \mathrm{SS} \mathsf{adv}[\mathcal{B}, \mathcal{E}].
        \]

在实际运用语义安全的属性时，通常会运用另一种特征描述，接下来将会定义一个新的攻击游戏. 该游戏和语义安全的攻击游戏类似.

!!! danger "semantic security: bit-guessing version"
    给定定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的计算密码 $\mathcal{E} = (E, D)$，以及敌手 $\mathcal{A}$，攻击游戏按如下流程进行：

    - 敌手计算等长的消息 $m_0, m_1 \in \mathcal{M}$，并将其发送给挑战者.

    - 挑战者随机选取 $b \xleftarrow{\mathrm{R}} \{0, 1\}$，计算 $k \xleftarrow{\mathrm{R}} \mathcal{K}$，以及 $c \xleftarrow{\mathrm{R}} E(k, m_b)$，并将 $c$ 发送给敌手.

    - 敌手输出 $\hat{b} \in \{0, 1\}$.

    如果 $\hat{b} = b$，则称 $\mathcal{A}$ 获胜.

    \automata
        \draw (0, 0) rectangle (3, 5);
        \draw (5, 0) rectangle (8, 5);
        \node at (1.5, 4.5) {Challenger};
        \node at (1.5, 3.5) {$b \xleftarrow{\mathrm{R}} \{0, 1\}$};
        \node at (1.5, 3) {$k \xleftarrow{\mathrm{R}} \mathcal{K}$};
        \node at (1.5, 2.5) {$c \xleftarrow{\mathrm{R}} E(k, m_b)$};
        \node at (5.5, 4.5) {$\mathcal{A}$};
        \draw[->] (5, 4) -- node[above]{$m_0, m_1 \in \mathcal{M}$} (3, 4);
        \draw[->] (3, 3) -- node[above]{$c \in \mathcal{C}$} (5, 3);
        \draw[->] (5, 2) -- node[above]{$\hat{b} \in \{0, 1\}$} (3, 2);

此处只有一个实验，敌手的目标是使得其猜测 $b$ 的准确度远高于随机猜测的 $1/2$. 记 $W$ 为 $\mathcal{A}$ 获胜的事件. 定义 $\mathcal{A}$ 关于 $\mathcal{E}$ 的位猜测语义安全优势为

\[
    \mathrm{SS} \mathsf{adv}^*[\mathcal{A}, \mathcal{E}] = \lvert \Pr{W} - 1/2 \rvert.
\]

那么有

!!! note "Theorem"
    对任意密码 $\mathcal{E}$ 和任意敌手 $\mathcal{A}$，都有

    \[
        \mathrm{SS} \mathsf{adv}[\mathcal{A}, \mathcal{E}] = 2 \mathrm{SS} \mathsf{adv}^*[\mathcal{A}, \mathcal{E}].
    \]

    ???+ note "Proof"
        设 $p_0$ 为先前版本的游戏中当 $b = 0$ 时 $\mathcal{A}$ 输出 $1$ 的概率，$p_1$ 为当 $b = 1$ 时 $\mathcal{A}$ 输出 $1$ 的概率. 依据条件概率，有

        \begin{gather*}
            \Pr{\hat{b} = 1 \vert b = 0} = p_0, \\
            \Pr{\hat{b} = 1 \vert b = 1} = p_1, \\
        \end{gather*}

        接下来是简单的计算.

        \begin{align*}
            \Pr{\hat{b} = b} &= \Pr{\hat{b} = b \vert b = 0} \Pr{b = 0} + \Pr{\hat{b} = b \vert b = 1} \Pr{b = 1} \\
                             &= \frac{1}{2} \Pr{\hat{b} = 0 \vert b = 0} + \frac{1}{2} \Pr{\hat{b} = 1 \vert b = 1} \\
                             &= \frac{1}{2} ((1 - \Pr{\hat{b} = 1 \vert b = 0}) + \Pr{\hat{b} = 1 \vert b = 1}) \\
                             &= \frac{1}{2} (1 - p_0 + p_1) \\
        \end{align*}

        进而

        \[
            \mathrm{SS} \mathsf{adv}^*[\mathcal{A}, \mathcal{E}] = \lvert \Pr{\hat{b} = b} - 1/2 \rvert = \frac{1}{2} \lvert p_1 - p_0 \rvert = \frac{1}{2} \mathrm{SS} \mathsf{adv}[\mathcal{A}, \mathcal{E}].
        \]

推而广之，考虑某个密码系统 $\mathcal{S}$ 上的某个安全性质 $\mathrm{X}$，其攻击游戏包含实验 $0$ 和实验 $1$，其中敌手 $\mathcal{A}$ 的协议是一致的. 对于 $b = 0, 1$，定义事件 $W_b$ 为 $\mathcal{A}$ 在实验 $b$ 中输出 $1$ 的事件，进而定义 $\mathcal{A}$ 关于 $\mathcal{S}$ 的 $\mathrm{X}$ 优势为

\[
    \mathrm{X} \mathsf{adv}[\mathcal{A}, \mathcal{S}] = \lvert \Pr{W_0} - \Pr{W_1} \rvert.
\]

类似地，可以定义该攻击游戏的位猜测版本，事件 $W$ 为 $\mathcal{A}$ 在该攻击游戏中成功输出 $\hat{b} = b$ 的事件，对应的位猜测优势为

\[
    \mathrm{X} \mathsf{adv}^*[\mathcal{A}, \mathcal{S}] = \lvert \Pr{W} - 1/2 \rvert.
\]

利用类似的计算过程就能得到

\[
    \mathrm{X} \mathsf{adv}[\mathcal{A}, \mathcal{S}] = 2 \mathrm{X} \mathsf{adv}^*[\mathcal{A}, \mathcal{S}].
\]

## Mathematical details

接下来将给所有暧昧的术语给出数学上的细节定义.

!!! info "negligible"
    函数 $f: \mathbb{Z}_{\geq 1} \to \mathbb{R}$ 是**可忽略的**（negligible），如果对于任意 $c \in \mathbb{R}_{>0}$，总存在 $n_0 \in \mathbb{Z}_{\geq 1}$，使得对于任意 $n > n_0$，都有 $\lvert f(n) \rvert < 1/n^c$.

!!! note "Theorem"
    函数 $f: \mathbb{Z}_{\geq 1} \to \mathbb{R}$ 是可忽略的，当且仅当对于任意 $c > 0$，
    
    \[
        \lim_{n \to \infty} n^c f(n) = 0
    \]

一旦有了可忽略的定义，便可以定义超多项式函数.

!!! info "super-polynomial"
    函数 $f: \mathbb{Z}_{\geq 1} \to \mathbb{R}$ 是**超多项式的**（super-polynomial），如果 $1/f$ 是可忽略的.

多项式约束函数的定义是自然的，具体的数学定义如下.

!!! info "poly-bounded"
    函数 $f: \mathbb{Z}_{\geq 1} \to \mathbb{R}$ 是**多项式约束的**（poly-bounded），如果存在 $c, d \in \mathbb{R}_{>0}$，使得对于任意 $n > d$，都有 $\lvert f(n) \rvert < n^c + d$.

注意到如果 $f$ 是多项式约束的，那么 $1/f$ 就不能是可忽略的.

在计算密码的部分，我们只是说计算密码 $\mathcal{E} = (E, D)$ 是定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的. 但在实际的数学模型中，$\mathcal{E}$ 实际上是和密钥空间族，消息空间族，以及密文空间族相关联的. 这些空间族都是参数化的，由**安全参数**（security parameter）$\lambda \in \mathbb{Z}_{> 0}$ 和**系统参数**（system parameter）$\Lambda \in \{0, 1\}^L, \exists L$ 索引，即应当写作

\[
    \{\mathcal{K}_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \{\mathcal{M}_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \{\mathcal{C}_{\lambda, \Lambda}\}_{\lambda, \Lambda}.
\]

当 $\mathcal{E}$ 被部署时，安全参数 $\lambda$ 就已被确定，一般来说，其值越大越安全；但相应的，密钥尺寸也会增大，导致加密和解密的计算量增大，速度变慢. 安全参数确定后，便会使用该密码特定的算法生成系统参数 $\Lambda$，进而和 $\lambda$ 一起给出该密码的一个固定实例的详细描述，且

\[
    (\mathcal{K}, \mathcal{M}, \mathcal{C}) = (\mathcal{K}_{\lambda, \Lambda}, \mathcal{M}_{\lambda, \Lambda}, \mathcal{C}_{\lambda, \Lambda}).
\]

$\lambda$ 和 $\Lambda$ 的值会被公开.

接下来讨论高效算法，此处考虑 $\mathcal{A}$ 接收安全参数 $\lambda$ 作为输入，其余参数的总长度都是被 $\lambda$ 多项式约束的. 基础上希望 $\mathcal{A}$ 的运行时间也是被 $\lambda$ 多项式约束的，但如果 $\mathcal{A}$ 是概率性的就会变得复杂.

!!! info "efficient algorithm"
    设 $\mathcal{A}$ 为一个概率性算法，接收 $\lambda \in \mathbb{Z}_{\geq 1}$ 作为输入，其余参数都编码为二进制串 $x \in \{0, 1\}^{\leq p(\lambda)}$，其中 $p$ 为某个固定多项式. 称 $\mathcal{A}$ 是**高效算法**（efficient algorithm），如果存在某个多项式约束函数 $t$ 和某个可忽略函数 $\varepsilon$，使得对于任意 $\lambda \in \mathbb{Z}_{\geq 1}$ 和任意 $x \in \{0, 1\}^{\leq p(\lambda)}$，$\mathcal{A}$ 以 $(\lambda, x)$ 作为输入时的运行时间达到 $t(\lambda)$ 的概率至多为 $\varepsilon(\lambda)$.

继续关注由安全参数和系统参数参数化的密码系统的基本要求，并且给出一部分术语的定义. 记 $\mathrm{Supp}(P(\lambda))$ 为分布 $P(\lambda)$ 的支撑集，即算法 $P$ 在输入 $\lambda$ 时可能输出的所有值的集合.

!!! info "system parameterization"
    **系统参数化**（system parameterization）是指一个高效的随机算法 $P$，其接收安全参数 $\lambda \in \mathbb{Z}_{\geq 1}$ 作为输入，并输出一个比特串 $\Lambda$，称为系统参数，且长度总是被 $\lambda$ 的某个多项式约束. 同时定义以下术语：

    - 若一个比特串的有限集合族 $\mathbf{S} = \{\mathcal{S}_{\lambda, \Lambda}\}_{\lambda, \Lambda}$，其中 $\lambda$ 遍历 $\mathbb{Z}_{\geq 1}$，$\Lambda$ 遍历 $\mathrm{Supp}(P(\lambda))$，满足任一集合 $\mathcal{S}_{\lambda, \Lambda}$ 中的所有比特串的长度都被 $\lambda$ 的某个多项式 $p$ 约束，那么称 $\mathbf{S}$ 为**$P$ 系统参数化的空间族**（family of spaces with system parameterization $P$）.

    - 若存在一个高效确定性算法，其接收 $\lambda \in \mathbb{Z}_{\geq 1}$，$\Lambda \in \mathrm{Supp}(P(\lambda))$ 以及 $s \in \{0, 1\}^{\leq p(\lambda)}$ 作为输入，可以判定 $s \in \mathcal{S}_{\lambda, \Lambda}$，那么称 $\mathbf{S}$ 为**高效可识别的**（efficiently recognizable）.

    - 若存在一个高效随机算法，其接收 $\lambda \in \mathbb{Z}_{\geq 1}$ 和 $\Lambda \in \mathrm{Supp}(P(\lambda))$ 作为输入，可以输出 $\mathcal{S}_{\lambda, \Lambda}$ 上的均匀随机元素，那么称 $\mathbf{S}$ 为**高效可采样的**（efficiently sampleable）.

    - 若存在一个高效确定性算法，其接收 $\lambda \in \mathbb{Z}_{\geq 1}$，$\Lambda \in \mathrm{Supp}(P(\lambda))$ 以及 $s \in \mathcal{S}_{\lambda, \Lambda}$ 作为输入，可以输出一个非负整数，那么称 $\mathbf{S}$ 具有一个**有效长度函数**（effective length function，输出的非负整数称为 $s$ 的**长度**）.

终于，现在可以陈述计算密码的正式且完备的定义.

!!! info "Computational cipher"
    计算密码由一对高效算法 $(E, D)$ 以及三个 $P$ 系统参数化的空间族

    \[
        \mathbf{K} = \{\mathcal{K}_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \quad \mathbf{M} = \{\mathcal{M}_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \quad \mathbf{C} = \{\mathcal{C}_{\lambda, \Lambda}\}_{\lambda, \Lambda}
    \]

    构成，满足

    1. $\mathbf{K}, \mathbf{M}, \mathbf{C}$ 都是高效可识别的；

    2. $\mathbf{K}$ 是高效可采样的；

    3. $\mathbf{M}$ 具有有效长度函数；

    4. $E$ 是一个高效的随机算法，其接收 $\lambda \in \mathbb{Z}_{\geq 1}$，$\Lambda \in \mathrm{Supp}(P(\lambda))$，$k \in \mathcal{K}_{\lambda, \Lambda}$ 以及 $m \in \mathcal{M}_{\lambda, \Lambda}$ 作为输入，总是输出 $\mathcal{C}_{\lambda, \Lambda}$ 上的一个元素；

    5. $D$ 是一个高效的确定性算法，其接收 $\lambda \in \mathbb{Z}_{\geq 1}$，$\Lambda \in \mathrm{Supp}(P(\lambda))$，$k \in \mathcal{K}_{\lambda, \Lambda}$ 以及 $c \in \mathcal{C}_{\lambda, \Lambda}$ 作为输入，要么输出 $\mathcal{M}_{\lambda, \Lambda}$ 上的一个元素，要么输出特殊符号 $\perp \not \in \mathcal{M}_{\lambda, \Lambda}$；

    6. 对于任意 $\lambda \in \mathbb{Z}_{\geq 1}$，$\Lambda \in \mathrm{Supp}(P(\lambda))$，$k \in \mathcal{K}_{\lambda, \Lambda}$，$m \in \mathcal{M}_{\lambda, \Lambda}$ 以及 $c \in \mathrm{Supp}(E(\lambda, \Lambda; k, m))$，都有 $D(\lambda, \Lambda; k, c) = m$.

    注意到加密和解密算法中都使用了 $\lambda$ 和 $\Lambda$ 作为辅助输入，所以对于先前定义的加密和解密算法，实际上是在谈论 $E(\lambda, \Lambda; \cdots)$ 和 $D(\lambda, \Lambda; \cdots)$.

为了建模敌手与挑战者之间的不同类型的交互，接下来引入**交互机**（interactive machine）的概念. 在交互机 $M$ 启动前，它总会获取安全参数 $\lambda$，其写在一个特殊的缓冲区中. 交互机 $M$ 有两个特殊的缓冲区，分别称为**输入消息缓冲区**（incoming message buffer）和**输出消息缓冲区**（outgoing message buffer）. $M$ 可能会被多次调用，但每次调用的流程都是类似的：向 $M$ 的输入消息缓冲区写入一个消息，$M$ 读取该消息，并进行计算，更新内部状态，然后将一个消息写入其输出消息缓冲区，结束该次调用. 可以假设 $M$ 在最后一条输出消息中包含某种特殊信号来表明其已经结束运行，并且会忽略任何后续对它的调用；并且假设输入输出消息的长度总是定长，这有助于简化部分技术. 

那么自然需要考虑 $M$ 的总运行时间，这对应其发出停机信号前的所有调用的总步骤数，显然这不仅仅依赖于 $M$ 和其随机选择，同样依赖于其运行的环境.

!!! info "efficient interactive machine"
    称 $M$ 为**高效交互机**（efficient interactive machine），如果存在某个多项式约束函数 $t$ 和某个可忽略函数 $\varepsilon$，使得在任意环境下 $M$ 的总运行时间达到 $t(\lambda)$ 的概率至多为 $\varepsilon(\lambda)$.

这其实就对应与高效敌手的定义，我们自然的将敌手建模为一个交互机，高效交互机自然对应于高效敌手. 

自然的，也可以将两个交互机 $M$ 和 $M'$ 组合成一个新的交互机 $M'' = \langle M', M \rangle$. 环境发送给 $M''$ 总是路由到 $M'$ 的输入消息缓冲区，$M'$ 可以向环境发送消息，或者向 $M$ 发送消息，后一种情况下 $M$ 的输出消息会被发回给 $M'$. 假设如果 $M$ 停止运行，$M'$ 将不再向其发送任何消息. 所以整个 $M''$ 的调用流程为：环境向 $M'$ 发送消息，$M'$ 处理该消息，并可能与 $M$ 进行若干次交互，最后 $M'$ 将一个消息发送回环境，宣告本次调用结束. 称 $M'$ 为开放机器（open machine），$M$ 为封闭机器（closed machine）.

一种显然的对应是挑战者和敌手共同组成的系统，挑战者是开放机器，敌手是封闭机器. 而另一种对应是规约中的初等包装，这里的思路是将接口层 $M'$ 和 $M = \op{Instance}(\mathcal{A})$ 组合形成复合交互机 $M'' = \op{Instance}(\mathcal{B}) = \langle M', M \rangle$. 定义如下：

!!! info "elementary wrapper"
    一个交互机 $M'$ 被称为**高效接口**（efficient interface），如果存在一个多项式约束函数 $t$ 和一个可忽略函数 $\varepsilon$，使得对于任意 $M$，在任意环境下执行复合交互机 $\langle M', M \rangle$ 时，总保有以下性质：

    在 $\langle M', M \rangle$ 运行的任何时点，$I$ 为此时 $M'$ 和 $M$ 的交互次数，$T$ 为 $M'$ 的总运行时间，那么 $T > t(\lambda + I)$ 的概率至多为 $\varepsilon(\lambda)$.

    若 $M'$ 是高效接口，那么对于任意交互机 $M$，称复合交互机 $\langle M', M \rangle$ 为 $M$ 关于 $M'$ 的**初等包装**（elementary wrapper）.

在这种定义下，初等包装的性质便不言自明.

目前的攻击游戏下，敌手都只会进行固定次数的查询. 但之后的部分攻击游戏中会允许敌手进行多次查询，且可以没有先验的限制. 但若 $\mathcal{A}$ 是高效的，查询次数便必然会被某个多项式约束的值 $Q$ 所限制. 所以方便的做法是提前告知初等包装 $\mathcal{B}$ $\mathcal{A}$ 的查询次数上限 $Q$，可以设置为 $\mathcal{A}$ 先向 $\mathcal{B}$ 发送 $Q$ 条特殊消息来通知 $\mathcal{B}$ 这一上限. 这样 $\mathcal{B}$ 不仅可以使用 $Q$，其运行时间也可以依赖于它.

在引入安全参数之后，敌手优势实际上是关于 $\lambda$ 的函数 $\mathrm{Adv}(\lambda)$. 对于每个 $\lambda$，都会得到一个不同的概率空间，安全性则意味着对每个高效的敌手，函数 $\mathrm{Adv}(\lambda)$ 都是可忽略的. 

在语义安全的攻击游戏中，挑战者和敌手实际上都接受 $\lambda$ 作为输入，但挑战者先开始交互，它需要生成系统参数发送给敌手. 之后的流程便和先前的定义类似了. 完整的攻击游戏如下：

\automata
    \draw (0, 0) rectangle (3, 5);
    \draw (5.3, 0) rectangle (8, 5);
    \node at (1.5, 4.5) {Challenger};
    \node at (1.5, 4) {(Experiment $b$)};
    \node at (1.5, 3.5) {$\Lambda \xleftarrow{\mathrm{R}} P(\lambda)$};
    \node at (1.5, 2.5) {$k \xleftarrow{\mathrm{R}} \mathcal{K}_{\lambda, \Lambda}$};
    \node at (1.5, 2) {$c \xleftarrow{\mathrm{R}} E(\lambda, \Lambda; k, m_b)$};
    \node at (5.5, 4.5) {$\mathcal{A}$};
    \draw[-] (4, 7) -- node[right]{$\lambda$} (4, 6);
    \draw[-] (1.5, 6) -- (6.5, 6);
    \draw[->] (1.5, 6) -- (1.5, 5);
    \draw[->] (6.5, 6) -- (6.5, 5);
    \draw[->] (3, 4) -- node[above]{$\Lambda$} (5.3, 4);
    \draw[->] (5.3, 3) -- node[above]{$m_0, m_1 \in \mathcal{M}_{\lambda, \Lambda}$} (3, 3);
    \draw[->] (3, 2) -- node[above]{$c$} (5.3, 2);
    \draw[->] (5.3, 1) -- node[above]{$\hat{b} \in \{0, 1\}$} (3, 1);

## A fun application: anonymous routing

语义安全密码也可以用于匿名路由，利用混合服务便可以解决被他人监视的问题. 设 Carol 是服务供应商，其与 $A_1, \ldots, A_n$ 分别有共享密钥 $k_1, \ldots, k_n$. $A_i$ 会向 Carol 发送消息 $c_i = E(k_i, \langle destination_i, m_i \rangle)$，其中 $\mathcal{E} = (E, D)$ 是语义安全密码. Carol 收集所有 $n$ 条消息，对应解密后以随机顺序发送至各自的目的地. 观察者只能看到 $n$ 条消息流入 Carol，和 $n$ 条消息流出 Carol，但无法判断其中哪条是 Alice 的消息. 称此时 Alice 的**匿名集**（anonymity set）大小为 $n$. 

这样排除了观察者，但 Carol 仍然可以看到 Alice 的消息，为了排除这一影响，Alice 使用多个混合服务. 以两个服务为例，分别记作 Carol 和 David，对应密钥为 $k_c$ 和 $k_d$. 为了将消息发送给 Bob，Alice 会构建嵌套密文

\[
    c_2 = E(k_c, E(k_d, m)).
\]

而嵌入路由信息后变为

\[
    c_2 = E(k_c, \langle \mathsf{David}, c_1 \rangle), \quad c_1 = E(k_d, \langle \mathsf{Bob}, m \rangle).
\]

整个过程也被称为**洋葱路由**（onion routing）. 这种情况下单独的 Carol 和 David 都无法知道是谁向 Bob 发送了消息，但如果二者串通便一目了然. 因此 Alice 可以寻求使用更多的混合服务，只要一个混合服务节点不与其他节点串通，Alice 的匿名性就能得到保障. 不过这里依然有一个问题，即 Alice 与 David 建立密钥 $k_d$ 时不能暴露自己的身份，这将在之后的部分讨论.

接下来是证明安全性. 设 $\mathcal{E} = (E, D)$ 为定义在 $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ 上的密码，定义 **$n$-路嵌套密码**（$n$-way nested cipher）$\mathcal{E}_n = (E_n, D_n)$ 如下：

\[
    E_n((k_1, \ldots, k_n), m) = E(k_n, E(k_{n-1}, \cdots, E(k_1, m)\cdots)), 
\]

解密时密钥顺序相反：

\[
    D_n((k_1, \ldots, k_n), c) = D(k_1, D(k_2, \cdots, D(k_n, c)\cdots)).
\]

希望证明若 $\mathcal{E}$ 是语义安全的，那么即使敌手拥有 $n-1$ 个密钥，$\mathcal{E}_n$ 依然是语义安全的. 定义实验 $b$，其中 $b = 0, 1$：

- 敌手向挑战者发送 $(m_0, m_1, d)$，其中 $m_0, m_1 \in \mathcal{M}$ 为等长消息，$1 \leq d \leq n$.

- 挑战者选取 $n$ 个密钥 $k_1, \ldots, k_n \xleftarrow{\mathrm{R}} \mathcal{K}$，计算 $c \xleftarrow{\mathrm{R}} E_n((k_1, \ldots, k_n), m_b)$，并将 $(c, k_1, \ldots, k_{d-1}, k_{d+1}, \ldots, k_n)$ 发送给敌手.

- 敌手输出 $\hat{b} \in \{0, 1\}$.

定义该游戏中敌手的优势为

\[
    \mathrm{NE}^{(n)}\mathsf{adv}[\mathcal{A}, \mathcal{E}] = \lvert \Pr{W_0} - \Pr{W_1} \rvert,
\]

其中 $W_b$ 为敌手在实验 $b$ 中输出 $\hat{b} = 1$ 的事件. 

!!! note "Theorem"
    对任意常数 $n > 0$，若 $\mathcal{E}$ 是语义安全的，n那么对于任意高效敌手 $\mathcal{A}$，$\mathrm{NE}^{(n)}\mathsf{adv}[\mathcal{A}, \mathcal{E}]$ 是可忽略的.

## Exercises

1. *(multiplicative one-time pad).* We may also define a “multiplication mod $p$” variation of the one-time pad. This is a cipher $\mathcal{E} = (E, D)$, defined over $(\mathcal{K}, \mathcal{M}, \mathcal{C})$, where $\mathcal{K} = \mathcal{M} = \mathcal{C} = \{1, 2, \ldots, p-1\}$, where $p$ is prime. Encryption and decryption are defined as follows:

    \[
        E(k, m) := (k \cdot m) \bmod{p}, \quad D(k, c) := (k^{-1} \cdot c) \bmod{p}.
    \]

    Here $k^{-1}$ denotes the multiplicative inverse of $k$ modulo $p$. Verify the correctness property for this cipher and prove that it is perfectly secure.

    \begin{align*}
        D(k, E(k, m)) &= D(k, (k \cdot m) \bmod{p}) \\
                     &= (k^{-1} \cdot (k \cdot m \bmod{p})) \bmod{p} \\
                     &= ((k^{-1} \cdot k) \cdot m) \bmod{p} \\
                     &= 1 \cdot m \bmod{p} = m.
    \end{align*}

    因为 $p$ 是素数，所以 $\langle \{1, 2, \ldots, p-1\}, \cdot \rangle$ 是一个乘法群. 对于固定的 $m, c \in \{1, 2, \ldots, p-1\}$，存在唯一的 $k = (c \cdot m^{-1}) \bmod{p}$ 使得 $E(k, m) = c$. 所以

    \[
        \lvert \{k \in \mathcal{K} : E(k, m) = c\} \rvert = 1 = N_c,
    \]

    其为常数，与 $m$ 无关，该密码是完美安全的.

2. *(A good substitution cipher).* Consider a variant of the substitution cipher $\mathcal{E} = (E, D)$ defined in Example 2.3 where every symbol of the message is encrypted using an *independent* permutation. That is, let $\mathcal{M} = \mathcal{C} = \Sigma^L$ for some a finite alphabet of symbols $\Sigma$ and some $L$. Let the key space be $\mathcal{K} = S^L$, where $S$ is the set of all permutations on $\Sigma$. The encryption algorithm $E(k, m)$ is defined as

    \[
        E(k, m) := (k[0](m[0]), k[1](m[1]), \ldots, k[L-1](m[L-1]))
    \]

    Show that $\mathcal{E}$ is perfectly secure.

    要求上为对 $i = 0, 1, \ldots, L-1$ 均有

    \[
        k[i](m[i]) = c[i].
    \]

    设 $n = \lvert \Sigma \rvert$，那么对于每个 $k[i]$ 的要求只有将 $m[i]$ 映射为 $c[i]$，其余 $n-1$ 个元素可以任意映射，所以 $k[i]$ 有 $(n-1)!$ 种选择. 因为各个 $k[i]$ 独立，所以满足要求的密钥总数为

    \[
        \lvert \{k \in \mathcal{K} : E(k, m) = c\} \rvert = ((n-1)!)^L = N_c,
    \]

    其为常数，与 $m$ 无关，该密码是完美安全的.

3. *(A broken one-time pad).* Consider a variant of the one time pad with message space $\{0, 1\}^L$ where key space $\mathcal{K}$ is restricted to all $L$-bit strings with an even number of 1’s. Give an efficient adversary whose semantic security advantage is 1.

    考虑随机生成 $m_0$ 而令 $m_1 \gets m_0 \oplus (0^{L-1} || 1)$，所以 $\mathrm{parity}(m_0) \neq \mathrm{parity}(m_1)$. 而因为 $c = k \oplus m_b$，且 $\mathrm{parity}(k) = 0$，所以 $\mathrm{parity}(c) = \mathrm{parity}(m_b)$. 若 $\mathrm{parity}(c) = \mathrm{parity}(m_0)$，则输出 $\hat{b} = 1$，否则输出 $\hat{b} = 0$. 定义 $W_b$ 为敌手在实验 $b$ 中输出 $\hat{b} = 1$ 的事件，那么 $\Pr{W_0} = 1$，$\Pr{W_1} = 0$，所以 $\mathrm{SS} \mathsf{adv}[\mathcal{A}, \mathcal{E}] = 1$.

4. *(Encryption chain).* Let $\mathcal{E} = (E, D)$ be a cipher defined over $(\mathcal{K}, \mathcal{M}, \mathcal{C})$ where $\mathcal{K} = \mathcal{M}$. Let $\mathcal{E}' = (E', D')$ be a cipher where encryption is defined as

    \[
        E'((k_1, k_2), m) := (E(k_1, k_2), E(k_2, m)) \in \mathcal{C}^2.
    \]

    Show that if $\mathcal{E}$ is perfectly secure then so is $\mathcal{E}'$. Exercise 3.2 describes an application for this encryption scheme.

    因为 $\mathcal{E}$ 是完美安全的，所以对于任意 $m, c \in \mathcal{M}$，都有

    \[
        \lvert \{k \in \mathcal{K} : E(k, m) = c\} \rvert = N_c.
    \]

    进而考虑固定的 $k_2 \in \mathcal{K}$ 有

    \[
        \lvert \{k_1 \in \mathcal{K} : E(k_1, k_2) = c_1\} \rvert = N_{c_1}.
    \]

    而考虑固定的 $m \in \mathcal{M}$ 有

    \[
        \lvert \{k_2 \in \mathcal{K} : E(k_2, m) = c_2\} \rvert = N_{c_2}.
    \]

    所以对于固定密文 $c = (c_1, c_2) \in \mathcal{C}^2$ 以及固定消息 $m \in \mathcal{M}$，有

    \begin{align*}
        & \lvert \{(k_1, k_2) \in \mathcal{K}^2 : E'((k_1, k_2), m) = c\} \rvert \\
        = & \lvert \{(k_1, k_2) \in \mathcal{K}^2 : E(k_1, k_2) = c_1 \cap E(k_2, m) = c_2\} \rvert \\
        = & N_{c_1} \cdot N_{c_2} = N_c.
    \end{align*}

    其与 $m$ 无关，该密码是完美安全的.

5. *(A stronger impossibility result).* This exercise generalizes Shannon’s theorem (Theorem 2.5). Let $\mathcal{E}$ be a cipher defined over $(\mathcal{K}, \mathcal{M}, \mathcal{C})$. Suppose that $\mathrm{SS} \mathsf{adv}[\mathcal{A}, \mathcal{E}] \leq \varepsilon$ for all adversaries $\mathcal{A}$, even including computationally unbounded ones. Show that $\lvert \mathcal{K} \rvert \geq (1 - \varepsilon) \lvert \mathcal{M} \rvert$.

    模仿证明的话，应该就是若 $\lvert \mathcal{K} \rvert < (1 - \varepsilon) \lvert \mathcal{M} \rvert$，那么存在某个敌手 $\mathcal{A}$ 使得 $\mathrm{SS} \mathsf{adv}[\mathcal{A}, \mathcal{E}] > \varepsilon$. 

    首先任意选取 $m_0 \in \mathcal{M}$，定义谓词函数 $\phi$ 满足

    \[
        \phi(c) = \begin{cases} 1, & \exists k_1 \in \mathcal{K}, D(k_1, c) = m_0; \\ 0, & \text{otherwise}. \end{cases}
    \]

    所以

    \[
        \Pr{\phi(E(\mathbf{k}, m_0))} = 1,
    \]

    