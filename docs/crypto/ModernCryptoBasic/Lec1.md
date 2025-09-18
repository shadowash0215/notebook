# Defining Security

现代密码学着重于三方面：

- 定义：安全性的数学定义；  
- 构造：如何构造安全的密码系统；  
- 证明：如何证明密码系统的安全性。

## Pseudo-random Functions and Permutations

首先要讨论的是伪随机数函数，对于对称加密来说这是一个基础的概念，简称为 PRF(pseudo-random
function)。

依然尝试采取 Cryptography Game 的方式来进行描述，如下图所示：

\automata
    \draw (4, 0) rectangle (8, -4);
    \node at (6, -2) {A};
    \node[align=left, right] at (0, 0) {$b \gets \{0, 1\}$};
    \node[align=left, right] at (0, -1.5em) {$F$};
    \draw[->] (1, -1.5em) -- (4, -1.5em);
    \node[align=left, right] at (0, -3em) {$x \gets D$};
    \node[align=left, right] at (0, -4.5em) {If $b = 0$ then $y \gets C$};
    \node[align=left, right] at (0, -6em) {If $b = 1$ then $y \gets F(x)$};
    \node[align=left, right] at (0, -7.5em) {$x, y$};
    \draw[->] (1, -7.5em) -- (4, -7.5em);
    \node[align=left, right] at (0, -9em) {$b'$};
    \draw[->] (4, -9em) -- (1, -9em);
    \node[align=left, right] at (0, -10.5em) {Win if $b = b'$};

!!! note "Kerckhoffs's principle"
    A cryptographic system should be secure even if everything about the system, except the key, is public knowledge.

也就是说，我们不能依赖于 PRF 本身的保密性，而是依赖于密钥的保密性，所以我们需要一族 PRF $\{F_k\}$，选取依赖于密钥 $k$。改进后的 Cryptography Game 如下：

\automata
    \draw (4, 0) rectangle (8, -4);
    \node at (6, -2) {A};
    \node[align=left, right] at (0, 0) {$\{F_k\}_K$};
    \draw[->] (1.1, 0) -- (4, 0);
    \node[align=left, right] at (0, -1.5em) {$b \gets \{0, 1\}, k \gets K$};
    \node[align=left, right] at (0, -3em) {$x \gets D$};
    \node[align=left, right] at (0, -4.5em) {If $b = 0$ then $y \gets C$};
    \node[align=left, right] at (0, -6em) {If $b = 1$ then $y \gets F_k(x)$};
    \node[align=left, right] at (0, -7.5em) {$x, y$};
    \draw[->] (1, -7.5em) -- (4, -7.5em);
    \node[align=left, right] at (0, -9em) {$b'$};
    \draw[->] (4, -9em) -- (1, -9em);
    \node[align=left, right] at (0, -10.5em) {Win if $b = b'$};

但这个 Game 依然有问题，它的难度太大了，并且存在 $K = D = C = \{0, 1\}^n$，$F_k(x) = k \oplus x$ 这种即使对手全知全能也无法区分的情况。所以在 Game 中我们赋予对手可以多次请求 $x$ 的能力，答案由 Oracle 给出。

\automata
    \draw (4, 0) rectangle (8, -4);
    \node at (6, -2) {A};
    \node[align=left, right] at (11, 1.5em) {$\mathcal{L} \gets \{\}$};
    \node[align=left, right] at (0, -1.5em) {$\{F_k\}_K$};
    \draw[->] (1.5, -1.5em) -- (4, -1.5em);
    \node[align=left, right] at (7, -1.5em) {$x \in D$};
    \draw[->] (8, -1.5em) -- node[above]{$\mathcal{O}_{F_k}$} (11, -1.5em);
    \node[align=left, right] at (11, -1.5em) {If $\exists (x, y') \in \mathcal{L}$ then $y \gets y'$};
    \node[align=left, right] at (0, -3em) {$b \gets \{0, 1\}$};
    \node[align=left, right] at (11, -3em) {else if $b = 0$ then $y \gets C$};
    \node[align=left, right] at (0, -4.5em) {$k \gets K$};
    \node[align=left, right] at (11, -4.5em) {else $y \gets F_k(x)$};
    \node[align=left, right] at (11, -6em) {$\mathcal{L} \gets \mathcal{L} \cup (x, y)$};
    \node[align=left, right] at (11, -7.5em) {$y$};
    \draw[->] (11, -7.5em) -- (8, -7.5em);
    \node[align=left, right] at (0, -9em) {$b'$};
    \draw[->] (4, -9em) -- (1, -9em);
    \node[align=left, right] at (0, -10.5em) {Win if $b = b'$};

$\mathcal{L}$ 是为了避免在 $b = 0$ 时，若对手重复请求相同的 $x$ 输出结果不一致的情况。这个 Game 的 Advantage 定义如下：

\[
    \operatorname{Adv}^{\mathsf{PRF}}_{\{F_k\}_K}(A) = 2 \cdot \left\lvert \Pr{A^{\mathcal{O}_{F_k}} \text{ wins}} - \frac{1}{2} \right\rvert.
\]

!!! success "引理"
    设 $A$ 是一个 PRF Game 的对手，$b'$ 是 $A$ 所选择的 bit 而 $b$ 是真实的 bit，那么有

    \[
        \operatorname{Adv}^{\mathsf{PRF}}_{\{F_k\}_K}(A) = \left\lvert \Pr{b' = 1 \mid b = 1} - \Pr{b' = 1 \mid b = 0} \right\rvert.
    \]

与 PRF 相关的还有 PRP(pseudo-random permutation)，其定义域和陪域都是 $D$，并且函数是双射。PRP Game 的定义与 PRF Game 类似，如下：

\automata
    \draw (4, 0) rectangle (8, -4);
    \node at (6, -2) {A};
    \node[align=left, right] at (11, 1.5em) {$\mathcal{L} \gets \{\}$};
    \node[align=left, right] at (0, -1.5em) {$\{F_k\}_K$};
    \draw[->] (1.5, -1.5em) -- (4, -1.5em);
    \node[align=left, right] at (7, -1.5em) {$x \in D$};
    \draw[->] (8, -1.5em) -- node[above]{$\mathcal{O}_{F_k}$} (11, -1.5em);
    \node[align=left, right] at (11, -1.5em) {If $\exists (x, y') \in \mathcal{L}$ then $y \gets y'$};
    \node[align=left, right] at (0, -3em) {$b \gets \{0, 1\}$};
    \node[align=left, right] at (11, -3em) {else if $b = 1$ then $y \gets F_k(x)$};
    \node[align=left, right] at (0, -4.5em) {$k \gets K$};
    \node[align=left, right] at (11, -4.5em) {else repeat $y \gets D$ until $\not \exists (x', y) \in \mathcal{L}$};
    \node[align=left, right] at (11, -6em) {$\mathcal{L} \gets \mathcal{L} \cup (x, y)$};
    \node[align=left, right] at (11, -7.5em) {$y$};
    \draw[->] (11, -7.5em) -- (8, -7.5em);
    \node[align=left, right] at (0, -9em) {$b'$};
    \draw[->] (4, -9em) -- (1, -9em);
    \node[align=left, right] at (0, -10.5em) {Win if $b = b'$};

显然这个 Game 的 Advantage 定义与 PRF Game 的类似，如下：

\[
    \operatorname{Adv}^{\mathsf{PRP}}_{\{F_k\}_K}(A) = 2 \cdot \left\lvert \Pr{A^{\mathcal{O}_{F_k}} \text{ wins}} - \frac{1}{2} \right\rvert.
\]

而因为排列是可逆的，所以也可以定义一个 Game，其中的 Oracle 给出了敌手请求元素的逆元素。所以 PRP Game 的 Advantage 也可以定义为

\[
    \operatorname{Adv}^{\mathsf{PRP}}_{\{F_k\}_K}(A) = 2 \cdot \left\lvert \Pr{A^{\mathcal{O}_{F_k}, \mathcal{O}_{F_k^{-1}}} \text{ wins}} - \frac{1}{2} \right\rvert.
\]

这样的一个问题便自然而然地产生了：在定义域和陪域一致的情况下，一个敌手能够区分 PRF 和 PRP 吗？首先我们需要定义什么叫“区分”，因为敌手在这两个 Game 中的行为是一样的，均是输出一个 bit，所以我们认为的区分应当是这两者的 Advantage 的差异，也就是对

\[
    \left\lvert \operatorname{Adv}^{\mathsf{PRF}}_{\{F_k\}_K}(A; q) - \operatorname{Adv}^{\mathsf{PRP}}_{\{F_k\}_K}(A; q) \right\rvert,
\]

进行分析。

!!! success "PRP-PRF Switching Lemma"
    设 $A$ 是一敌手，$\{F_k\}_K$ 是一族伪随机置换，定义域和陪域均为 $D$，那么有  

    \[
        \left\lvert \operatorname{Adv}^{\mathsf{PRF}}_{\{F_k\}_K}(A; q) - \operatorname{Adv}^{\mathsf{PRP}}_{\{F_k\}_K}(A; q) \right\rvert < \frac{q^2}{\lvert D \rvert},
    \]

    其中 $q$ 是敌手的查询次数。

    ??? success "Proof"
        设 $A$ 在 PRF Game 中，记 $E$ 为 Oracle 对两个不同输入值返回了相同输出值的事件，那么有

        \begin{align}
            \Pr{A \text{ wins the } \mathsf{PRF} \text{ Game}} & = \Pr{A \text{ wins the } \mathsf{PRF} \text{ Game} \mid E} \cdot \Pr{E} \\ & + \Pr{A \text{ wins the } \mathsf{PRF} \text{ Game} \mid \neg E} \cdot \Pr{\neg E} \\
            & \leqslant \Pr{E} + \Pr{A \text{ wins the } \mathsf{PRF} \text{ Game} \mid \neg E} \\
            & = \Pr{E} + \Pr{A \text{ wins the } \mathsf{PRP} \text{ Game} \mid \neg E}.
        \end{align}

        而根据生日攻击，$\Pr{E} \leqslant q^2 / 2 \lvert D \rvert$。不失一般性，假定 $A$ 胜利的概率至少为 $1/2$：

        \begin{align}
            & \left\lvert \operatorname{Adv}^{\mathsf{PRF}}_{\{F_k\}_K}(A; q) - \operatorname{Adv}^{\mathsf{PRP}}_{\{F_k\}_K}(A; q) \right\rvert \\ = & \left\lvert 2 \cdot \left\lvert \Pr{A \text{ wins the } \mathsf{PRF} \text{ Game}} - \frac{1}{2} \right\rvert - 2 \cdot \left\lvert \Pr{A \text{ wins the } \mathsf{PRP} \text{ Game}} - \frac{1}{2} \right\rvert \right\rvert \\
            = & \left\lvert 2 \cdot \Pr{A \text{ wins the } \mathsf{PRF} \text{ Game}} - 1 - 2 \cdot \Pr{A \text{ wins the } \mathsf{PRP} \text{ Game}} + 1 \right\rvert \\
            \leqslant & 2 \cdot \Pr{E} \\
            \leqslant & \frac{q^2}{\lvert D \rvert}.
        \end{align}

## One-Way Functions and Trapdoor One-Way Functions

离散对数问题实际上就是一种单向函数，给敌手一个公开的函数，并要求其进行逆向的操作，如离散对数问题中为给出 $f(x) = g^x$ 要求其求出 $x$。对应的 Game 如下：

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, -1.5em) {$F$};
    \draw[->] (1, -1.5em) -- (4, -1.5em);
    \node[align=left, right] at (0, -3em) {$x \gets D$};
    \node[align=left, right] at (0, -4.5em) {$h \gets F(x)$};
    \draw[->] (2, -4.5em) -- (4, -4.5em);
    \node[align=left, right] at (0, -6em) {$x'$};
    \draw[->] (4, -6em) -- (0.5, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $F(x') = h$};

这个 Game 的 Advantage 定义如下：

\[
    \operatorname{Adv}^{\mathsf{OWF}}_F(A) = \Pr{A \text{ wins the } \mathsf{OWF} \text{ game}}.
\]

再考虑 RSA 问题，这其中的单向函数是 $F_{N, e} (x) = x^e \pmod N$，但这其中存在一个值 $d$ 使得这个函数能够被高效地逆向，这种函数称为陷门单向函数，这里的 $d$ 就是陷门。

## Security of Encryption

现在我们来定义对称加密算法和公钥加密算法的安全性，有以下三点需要定义：  

- 敌手的目标；
- 允许的攻击类型；
- 计算模型。

第一点对应的是 Game 的胜利条件，第二点对应的是敌手能够获取的 Oracle 类型，第三点略微复杂，最后阐述。

为了进行定义，先给出一些符号定义，$\mathbb{P}$ 为明文空间，$\mathbb{C}$ 为密文空间，$\mathbb{K}$ 为密钥空间。对于对称加密，记 $k \in \mathbb{K}$ 为密钥；而对于公钥加密，记密钥对为 $(\mathfrak{pt}, \mathfrak{st})$，其中 $\mathfrak{pt}$ 为公钥，$\mathfrak{st}$ 为私钥。而密钥生成的记号分别记作 $k \gets \operatorname{KeyGen}()$ 和 $(\mathfrak{pt}, \mathfrak{st}) \gets \operatorname{KeyGen}()$。加密为 $c \gets e_k (m)$ 和 $c \gets e_{\mathfrak{pt}} (m)$，解密为 $m \gets d_k (c)$ 和 $m \gets d_{\mathfrak{st}} (c)$。并且我们假定解密算法始终是有效的，也就是说，对于对称加密而言，

\[
    \forall k \in \mathbb{K}, \forall m \in \mathbb{P}, d_k (e_k (m)) = m.
\]

对于公钥加密而言是类似的。

### One-Way Security

出于不希望敌手获得特定密文对应的明文的考虑，单向安全性（one-way security）的提出是非常自然的。对于对称加密而言，其基本形式可以用如下的 Game 来描述：

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, -1.5em) {$k \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (0, -3em) {$m^* \gets \mathbb{P}$};
    \node[align=left, right] at (0, -4.5em) {$c^* \gets e_k (m^*)$};
    \draw[->] (2, -4.5em) -- (4, -4.5em);
    \node[align=left, right] at (0, -6em) {$m_0$};
    \draw[->] (4, -6em) -- (1, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $m_0 = m^*$};

等价的，对于公钥加密，其 Game 可以描述为：

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, 0) {$\mathfrak{pt}, \mathfrak{st} \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (0, -1.5em) {$\mathfrak{pt}$};
    \draw[->] (1, -1.5em) -- (4, -1.5em);
    \node[align=left, right] at (0, -3em) {$m^* \gets \mathbb{P}$};
    \node[align=left, right] at (0, -4.5em) {$c^* \gets e_\mathfrak{pt} (m^*)$};
    \draw[->] (2, -4.5em) -- (4, -4.5em);
    \node[align=left, right] at (0, -6em) {$m_0$};
    \draw[->] (4, -6em) -- (1, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $m_0 = m^*$};

称 $c^*$ 为 Challenge ciphertext，这样的攻击为被动攻击（passive attack），上述的两个 Game 记为 $\mathsf{OW-PASS}$. 自然，其对于密码系统 $\Pi$ 的 Advantage 定义为 $\operatorname{Adv}^{\mathsf{OW-PASS}}_\Pi (A) = \Pr{A \text{ wins}}$。

显然这是一个比较弱的安全性定义，因为敌手没有任何可以利用的 Oracle。所以一般来说，即使是最低要求的 Game，我们也会给敌手一个加密 Oracle。这样的攻击被称为**选择明文攻击**（chosen-plaintext attack），因为我们给了敌手一个加密的黑盒，但没有解密的黑盒。对于对称加密而言，其 Game 可以描述为：

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, -1.5em) {$k \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (5.9, -1.5em) {$m \in \mathbb{P}$};
    \node[align=left, right] at (0, -3em) {$m^* \gets \mathbb{P}$};
    \node[align=left, right] at (0, -4.5em) {$c^* \gets e_k (m^*)$};
    \draw[->] (2, -4.5em) -- (4, -4.5em);
    \node[align=left, right] at (0, -6em) {$m_0$};
    \draw[->] (4, -6em) -- (1, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $m_0 = m^*$};
    \draw[->] (7, -1.5em) -- node[above]{$\mathcal{O}_{e_k}$} (8.5, -1.5em);
    \node[align=left, right] at (8.6, -2em) {$c \gets e_k (m)$};
    \draw[->] (8.5, -2.5em) -- (7, -2.5em);

如此的 Game 记为 $\mathsf{OW-CPA}$，而注意到对于公钥加密而言，拥有公钥便可以进行加密，所以其 $\mathsf{OW-CPA}$ Game 和 $\mathsf{OW-PASS}$ Game 是一样的。$\mathsf{OW-CPA}$ 的 Advantage 定义也与 $\mathsf{OW-PASS}$ 类似，为 $\operatorname{Adv}^{\mathsf{OW-CPA}}_\Pi (A) = \Pr{A \text{ wins}}$。

更复杂的攻击是**选择密文攻击**（chosen-ciphertext attack），在这种攻击中，敌手同时拥有加密和解密的 Oracle，不过显然我们要求其不能够解密 Challenge ciphertext。Game 的描述如下：

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, -1.5em) {$k \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (0, -3em) {$m^* \gets \mathbb{P}$};
    \node[align=left, right] at (0, -4.5em) {$c^* \gets e_k (m^*)$};
    \draw[->] (2, -4.5em) -- (4, -4.5em);
    \node[align=left, right] at (0, -6em) {$m_0$};
    \draw[->] (4, -6em) -- (1, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $m_0 = m^*$};
    \node[align=left, right] at (5.9, -1.5em) {$m \in \mathbb{P}$};
    \draw[->] (7, -1.5em) -- node[above]{$\mathcal{O}_{e_k}$} (8.5, -1.5em);
    \node[align=left, right] at (8.6, -2em) {$c \gets e_k (m)$};
    \draw[->] (8.5, -2.5em) -- (7, -2.5em);
    \node[align=left, right] at (5.9, -6em) {$c \in \mathbb{C}$};
    \draw[->] (7, -6em) -- node[above]{$\mathcal{O}_{d_k}$} (8.5, -6em);
    \node[align=left, right] at (8.6, -6em) {If $c = c^* \to$ abort};
    \node[align=left, right] at (8.6, -7.5em) {$m \gets d_k (c)$};
    \draw[->] (8.5, -7.5em) -- (7, -7.5em); 

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, 0) {$\mathfrak{pt}, \mathfrak{st} \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (0, -1.5em) {$\mathfrak{pt}$};
    \draw[->] (1, -1.5em) -- (4, -1.5em);
    \node[align=left, right] at (0, -3em) {$m^* \gets \mathbb{P}$};
    \node[align=left, right] at (0, -4.5em) {$c^* \gets e_\mathfrak{pt} (m^*)$};
    \draw[->] (2.2, -4.5em) -- (4, -4.5em);
    \node[align=left, right] at (0, -6em) {$m_0$};
    \draw[->] (4, -6em) -- (1, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $m_0 = m^*$};
    \node[align=left, right] at (5.9, -6em) {$c \in \mathbb{C}$};
    \draw[->] (7, -6em) -- node[above]{$\mathcal{O}_{d_\mathfrak{pt}}$} (8.5, -6em);
    \node[align=left, right] at (8.6, -6em) {If $c = c^* \to$ abort};
    \node[align=left, right] at (8.6, -7.5em) {$m \gets d_\mathfrak{pt} (c)$};
    \draw[->] (8.5, -7.5em) -- (7, -7.5em); 

这样的 Game 记为 $\mathsf{OW-CCA}$，Advantage 定义为 $\operatorname{Adv}^{\mathsf{OW-CCA}}_\Pi (A) = \Pr{A \text{ wins}}$。

但单向安全性太“暴力”了，它要求敌手能直接破解密文，而无法衡量敌手可以攻破的程度。但在实际中，攻破一部分密文也是十分重要的，所以我们需要有能够衡量敌手无法获得任何与明文相关的信息的安全性定义。

### Perfect Security

Perfect security，又称 information-theoretic security，是一种非常强的安全性定义，它描述的是即便敌手拥有无限的计算能力，也无法获得任何关于明文的信息，这其实就和 Perfect Secrecy 是一样的。

!!! info "Definition"
    (Perfect Secrecy) 一个密码系统拥有 perfect secrecy，如果对于所有的明文 $m \in \mathbb{P}$ 和所有的密文 $c \in \mathbb{C}$，有

    \[
        \Pr{P = m \mid C = c} = \Pr{P = m},
    \]

另一个描述 perfect secrecy 的方式如下：

!!! success "Lemma"
    一个密码系统拥有 perfect secrecy，如果对于所有的明文 $m \in \mathbb{P}$ 和所有的密文 $c \in \mathbb{C}$，有

    \[
        \Pr{C = c \mid P = m} = \Pr{C = c}.
    \]

Perfect secrecy 的一个重要性质是，对于任何的密码系统，其密钥空间至少要和密文空间一样大。事实上，我们有如下的定理：

!!! success "Lemma"
    若一个密码系统拥有 perfect secrecy，那么有

    \[
        \# \mathbb{K} \geqslant \# \mathbb{C} \geqslant \# \mathbb{P}.
    \]

    ??? success "Proof"
        首先 $\# \mathbb{C} \geqslant \# \mathbb{P}$ 是显然的，因为加密算法一定是一个单射。  
        假定所有密文都有可能出现，也就是 $\forall c \in \mathbb{C}, \Pr{C = c} > 0$，那么对于任意明文 $m \in \mathbb{P}$，有

        \[
            \Pr{C = c \mid P = m} = \Pr{C = c} > 0,
        \]

        而对于任一明文 $m$，这就意味着对于任意的密文 $c$，都存在着密钥 $k$ 使得 $e_k (m) = c$，所以 $\# \mathbb{K} \geqslant \# \mathbb{C}$。

接下来便是 Shannon's Theorem，其给出了 perfect secrecy 的一个充要条件：

!!! note "Theorem"
    设 $(\mathbb{P}, \mathbb{C}, \mathbb{K}, e_k (\cdot), d_k (\cdot))$ 是一个密码系统，并且 $\# \mathbb{K} = \# \mathbb{C} = \# \mathbb{P}$。那么这个密码系统拥有 perfect secrecy 当且仅当：

    - 每个密钥 $k$ 被使用的概率相同，均为 $1 / \# \mathbb{K}$；
    - 对于每个明文 $m$ 和密文 $c$，存在唯一的密钥 $k$ 使得 $e_k (m) = c$。

问题在于公钥加密中，某个公钥会被使用多次，而非一次一密；并且在现代密码学中会追求使用较小的密钥去加密大量的明文。所以 perfect security 是一个过于严格的安全性定义，而且在实际中很难实现。

### Semantic Security

语义安全性（semantic security）是一个类似于 perfect security 的安全性定义，但是其要求敌手只有多项式时间的计算能力。正式来说，对于所有明文空间上的概率分布，如果敌手可以在多项式时间内计算出给定密文对应的明文，那么其也可以在没有密文的情况下计算出这一明文。也就是说，是否拥有密文对于敌手计算明文没有任何帮助。

以下是一个用于说明的简化定义. 假定我们希望计算的信息在明文空间中是一个比特，也就是说存在函数 $g : M \to \{0, 1\}$，并且假定在整个明文空间上有

\[
    \Pr{g(m) = 1} = \Pr{g(m) = 0} = \frac{1}{2}.
\]

此外，还有明文和密文长度相等.

将敌手建模为一个算法 $S$，其输入为密文 $c$，并且是使用对称密钥 $k$ 进行的加密. 其会尝试对密文 $c$ 关联的明文生成一个在函数 $g$ 上的评估，因而 $S$ 的输出就是一个比特，对应于 $g(m)$ 的值. 

敌手如果产生正确输出的概率高于 $1/2$，就被视为成功. 因为敌手在没有密文的情况下也可以进行猜测，所以我们认为一个成功的敌手应当能够在得到密文之后做的更好. 所以 $S$ 的优势定义为

\[
    \operatorname{Adv}^{\mathsf{SEM}}_\Pi (S) = 2 \cdot \left\lvert \Pr{S(c) = g(d_k (c))} - \frac{1}{2} \right\rvert.
\]

一个方案被称为是语义安全的，如果对于所有的多项式时间敌手 $S$，其优势都是可以忽略的. 

### IND Security

语义安全的缺点在于验证给定的加密方案具有语义安全是困难的. 因而，多项式安全（Polynomial Security），有时也称加密的不可区分性，或是不可区分安全性（indistinguishability security），被提出，其是一个容易验证的安全性定义. 幸运的是，语义安全和多项式安全是等价的. 所以，如果要说明一个加密方案是语义安全的，只需要证明其是多项式安全的即可.

!!! note "Definition"
    (IND Security) 一个密码系统拥有不可区分安全性，如果不存在敌手赢得以下 Game 的概率超过 $1/2$. 敌手会以两阶段运行：

    - **搜寻**：在搜寻阶段，敌手产生两个等长的明文 $m_0, m_1$.

    - **猜测**：在猜测阶段，敌手接收到一个密文 $c^*$，其由 $m_b$ 加密而来. 敌手的目标是猜测 $b$ 的值，并且正确的概率高于 $1/2$.

类似于单向安全性，也可以定义 $\mathsf{IND-PASS}$，$\mathsf{IND-CPA}$ 和 $\mathsf{IND-CCA}$. 以下是 $\mathsf{IND-CCA}$ 的 Game 描述：

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, -1.5em) {$k \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (0, -3em) {$b \gets \{0, 1\}$};
    \node[align=left, right] at (0, -6em) {$b'$};
    \draw[->] (4, -6em) -- (1, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $b' = b$};
    \node[align=left, right] at (5.1, -1em) {$m_0, m_1 \in \mathbb{P}$};
    \draw[->] (7, -1em) -- node[above]{$\mathcal{O}_{\mathsf{LR}}$} (8.5, -1em);
    \node[align=left, right] at (8.6, -1.5em) {$c^* \gets e_k (m_b)$};
    \draw[->] (8.5, -2em) -- (7, -2em);
    \node[align=left, right] at (5.9, -3.5em) {$m \in \mathbb{P}$};
    \draw[->] (7, -3.5em) -- node[above]{$\mathcal{O}_{e_k}$} (8.5, -3.5em);
    \node[align=left, right] at (8.6, -4em) {$c \gets e_k (m)$};
    \draw[->] (8.5, -4.5em) -- (7, -4.5em);
    \node[align=left, right] at (5.9, -6.5em) {$c \in \mathbb{C}$};
    \draw[->] (7, -6.5em) -- node[above]{$\mathcal{O}_{d_k}$} (8.5, -6.5em);
    \node[align=left, right] at (8.6, -6.5em) {If $c = c^* \to$ abort};
    \node[align=left, right] at (8.6, -8em) {$m \gets d_k (c)$};
    \draw[->] (8.5, -8em) -- (7, -8em); 

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, 0) {$\mathfrak{pt}, \mathfrak{st} \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (0, -1.5em) {$\mathfrak{pt}$};
    \draw[->] (1, -1.5em) -- (4, -1.5em);
    \node[align=left, right] at (0, -3em) {$b \gets \{0, 1\}$};
    \node[align=left, right] at (0, -6em) {$b'$};
    \draw[->] (4, -6em) -- (1, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $b' = b$};
    \node[align=left, right] at (5.1, -1.5em) {$m_0, m_1 \in \mathbb{P}$};
    \draw[->] (7, -1.5em) -- node[above]{$\mathcal{O}_{\mathsf{LR}}$} (8.5, -1.5em);
    \node[align=left, right] at (8.6, -2em) {$c^* \gets e_\mathfrak{pt} (m_b)$};
    \draw[->] (8.5, -2.5em) -- (7, -2.5em);
    \node[align=left, right] at (5.9, -6em) {$c \in \mathbb{C}$};
    \draw[->] (7, -6em) -- node[above]{$\mathcal{O}_{d_\mathfrak{st}}$} (8.5, -6em);
    \node[align=left, right] at (8.6, -6em) {If $c = c^* \to$ abort};
    \node[align=left, right] at (8.6, -7.5em) {$m \gets d_\mathfrak{st} (c)$};
    \draw[->] (8.5, -7.5em) -- (7, -7.5em);

$\mathcal{O}_{\mathsf{LR}}$ 根据 $b$ 的值选择加密 $m_0$ 还是 $m_1$，并将结果返回给敌手. 允许敌手在调用 $\mathcal{O}_{\mathsf{LR}}$ 之前和之后多次调用加密和解密 Oracle，但如果 $\mathcal{O}_{\mathsf{LR}}$ 输出了已经被敌手传递给解密 Oracle 的密文，那么也应该终止游戏.

因为 $A$ 总可以简单猜测 $b$ 的值，所以 $A$ 的 Advantage 定义为

\[
    \operatorname{Adv}^{\mathsf{IND-PASS}}_\Pi (A) = 2 \cdot \left\lvert \Pr{A \text{ wins}} - \frac{1}{2} \right\rvert,
\]

而显然，满足 $\mathsf{IND-CPA}$ 的加密函数都必然是概率性的，否则敌手只需要将其中的一个明文传递给加密 Oracle，然后比较密文就可以确定 $b$ 的值.

!!! note "Definition"
    对称[公钥]加密算法被称为安全的，如果其在选择密文攻击下是语义安全的. 即对任意多项式时间敌手 $A$，$\operatorname{Adv}^{\mathsf{SEM-CCA}}_\Pi (A)$ 是可以忽略的.

但前面说过，语义安全和多项式安全是等价的，所以我们也可以说：

!!! note "Definition"
    对称[公钥]加密算法被称为安全的，如果其是 $\mathsf{IND-CCA}$ 安全的. 即对任意多项式时间敌手 $A$，$\operatorname{Adv}^{\mathsf{IND-CCA}}_\Pi (A)$ 是可以忽略的.

!!! note "Theorem"
    一个 $\mathsf{IND-PASS}$ 安全的系统在面对被动敌手时是语义安全的. 

    ???+ note "Proof"
        反证法. 假设存在算法 $S$，使得 $\operatorname{Adv}^{\mathsf{SEM}}_\Pi (S) > \varepsilon$，但这个系统本身是 $\mathsf{IND-PASS}$ 安全的. 那么我们可以构造一个敌手 $A$，其使用 $S$ 作为 Oracle. 

        搜寻阶段 $A$ 输出 $m_0, m_1$ 使得 $g(m_0) \neq g(m_1)$，这是容易做到的，因为 $g$ 的输出在整个消息空间上是均匀分布的.

        猜测阶段 $A$ 接收到 $c_b$，并将其传递给 $S$，$S$ 便会返回关于 $g(m_b)$ 的最佳猜测，再通过去和 $g(m_0)$, $g(m_1)$ 比较，$A$ 就可以猜测出 $b$ 的值. 进而有

        \[
            \operatorname{Adv}^{\mathsf{IND-PASS}}_\Pi (A) = \operatorname{Adv}^{\mathsf{SEM}}_\Pi (S) > \varepsilon,
        \]

        矛盾.

设 $\Pi$ 是一个对称加密算法，那么有

\[
    \Pi \text{ is } \mathsf{IND-CCA} \Rightarrow \Pi \text{ is } \mathsf{IND-CPA} \Rightarrow \Pi \text{ is } \mathsf{IND-PASS}.
\]

因为从左到右限制了敌手可以调用的 Oracle 类型. 但同样也有

\[
    \Pi \text{ is } \mathsf{IND-XXX} \Rightarrow \Pi \text{ is } \mathsf{OW-XXX},
\]

其中 $\mathsf{XXX} \in \{\mathsf{PASS}, \mathsf{CPA}, \mathsf{CCA}\}$，因为如果敌手可以破解单向安全，那么可以将其作为**子程序**（subroutine）来破解多项式安全. 以下图片以 $\mathsf{CCA}$ 为例说明了这个过程：

\automata
    \draw (3, 0) rectangle (10, -5);
    \node at (3.5, -0.3) {B};
    \node[align=left, right] at (0, -1.5em) {$k \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (0, -3em) {$b \gets \{0, 1\}$};
    \node[align=left, right] at (0, -12em) {$b'$};
    \draw[->] (3, -12em) -- (0.5, -12em);
    \node[align=left, right] at (8, -1.5em) {$m_0, m_1 \gets \mathbb{P}$};
    \draw[->] (10, -1.5em) -- node[above]{$\mathcal{O}_{\mathsf{LR}}$} (11.5, -1.5em);
    \draw[->] (11.5, -2.5em) -- (10, -2.5em);
    \draw[->] (10, -2.5em) -- (5.3, -2.5em);
    \draw[->] (5.3, -2.5em) -- (5.3, -2.5);
    \draw[->] (5.3, -2.5) -- (5.8, -2.5);
    \draw (5.8, -2.3) rectangle (8.3, -4.8);
    \node at (7.05, -3.55) {A};
    \node[align=left, right] at (6, -12em) {$m'$};
    \node[align=left, right] at (3.2, -5em) {$b' = 1$};
    \node[align=left, right] at (3.2, -6.5em) {if $m' = m_0$};
    \node[align=left, right] at (3.2, -8em) {$b' = 0$};
    \draw[->] (5.8, -12em) -- (5.1, -12em);
    \draw[->] (5.1, -12em) -- (5.1, -2em);
    \draw[->] (5.1, -2em) -- (4, -2em);
    \draw[->] (4, -2em) -- (4, -4.5em);
    \draw[->] (4, -8.5em) -- (4, -12em);
    \draw[->] (4, -12em) -- (3, -12em);
    \draw[->] (8.3, -2.5) -- node[above]{$\mathcal{O}_{e_k}$} (9, -2.5);
    \draw[->] (9, -2.5) -- (9, -5em);
    \draw[->] (9, -5em) -- (10, -5em);
    \draw[->] (10, -5em) -- node[above]{$\mathcal{O}_{e_k}$} (11.5, -5em);
    \draw[->] (11.5, -6.5em) -- (10, -6.5em);
    \draw[->] (10, -6.5em) -- (9.3, -6.5em);
    \draw[->] (9.3, -6.5em) -- (9.3, -2.8);
    \draw[->] (9.3, -2.8) -- (8.3, -2.8);
    \draw[->] (8.3, -4.5) -- node[above]{$\mathcal{O}_{d_k}$} (9, -4.5);
    \draw[->] (9, -4.5) -- (9, -11em);
    \draw[->] (9, -11em) -- (10, -11em);
    \draw[->] (10, -11em) -- node[above]{$\mathcal{O}_{d_k}$} (11.5, -11em);
    \draw[->] (11.5, -12em) -- (10, -12em);
    \draw[->] (10, -12em) -- (9.3, -12em);
    \draw[->] (9.3, -12em) -- (9.3, -4.8);
    \draw[->] (9.3, -4.8) -- (8.3, -4.8);

整个流程为：

- $m_0, m_1 \gets \mathbb{P}$ 

- 调用 $\mathcal{O}_{\mathsf{LR}}(m_0, m_1)$ 得到 $c^*$

- 调用以 $c^*$ 为输入的 $A$

- 如果 $A$ 做了加密 Oracle 调用，那么就将请求传递给 $\mathcal{O}_{e_k}$ 并将结果返回给 $A$

- 如果 $A$ 做了一个解密 Oracle 调用，那么就将请求传递给 $\mathcal{O}_{d_k}$ 并将结果返回给 $A$

- 最终 $A$ 会输出一个明文 $m'$

- 如果 $m' = m_0$，则设置 $b' = 0$，否则设置 $b' = 1$

- 输出 $b'$

所以以上过程利用了一个能攻破 $\mathsf{OW-CCA}$ 的敌手 $A$ 构造了一个能攻破 $\mathsf{IND-CCA}$ 的敌手 $B$，进而就有

\[
    \operatorname{Adv}^{\mathsf{OW-CCA}}_\Pi (A) \leqslant \operatorname{Adv}^{\mathsf{IND-CCA}}_\Pi (B).
\]

因为对 $A$ 并没有做限制，所以这对任意的 $A$ 都成立. 因而如果 $\Pi$ 是 $\mathsf{IND-CCA}$ 安全的，那么 $\Pi$ 也是 $\mathsf{OW-CCA}$ 安全的.

## Other Notions of Security

### Many Time Security

如果在 $\mathsf{IND}$ 博弈中，允许敌手多次调用 $\mathcal{O}_{\mathsf{LR}}$，那么我们就得到了多次安全性（many-time security）. 以被动攻击为例，其 Advantage 记为 $\operatorname{Adv}^{m-\mathsf{IND-PASS}}_\Pi (A)$. 自然，在 $\mathsf{CCA}$ 下需要修改解密 Oracle 的限制，使得其在接收到任何 $\mathcal{O}_{\mathsf{LR}}$ 输出的密文时都终止游戏.

在对称加密的情形下便不需要加密 Oracle 了，因为可以利用 $\mathcal{O}_{\mathsf{LR}}(m, m) = \mathcal{O}_{e_k}(m)$ 来模拟，所以 $m-\mathsf{IND-PASS}$ 和 $m-\mathsf{IND-CPA}$ 是等价的. 自然有

\[
    \Pi \text{ is } m-\mathsf{IND-XXX} \Rightarrow \Pi \text{ is } \mathsf{IND-XXX}.
\]

!!! note "Theorem"
    设 $A$ 为对称加密系统 $\Pi$ 的一个多项式时间 $\mathsf{IND-XXX}$ 敌手，那么存在一个多项式时间的 $m-\mathsf{IND-XXX}$ 敌手 $B$，使得

    \[
        \operatorname{Adv}^{\mathsf{IND-XXX}}_\Pi (A) = \operatorname{Adv}^{m-\mathsf{IND-XXX}}_\Pi (B).
    \]

!!! note "Theorem"
    设 $A$ 为对称加密系统 $\Pi$ 的一个多项式时间 $m-\mathsf{IND-XXX}$ 敌手，向 $\mathcal{O}_{\mathsf{LR}}$ 进行了 $q_\mathsf{LR}$ 次调用，那么存在一个多项式时间的 $\mathsf{IND-XXX}$ 敌手 $B$，使得

    \[
        \operatorname{Adv}^{m-\mathsf{IND-XXX}}_\Pi (A) \leqslant q_\mathsf{LR} \cdot \operatorname{Adv}^{\mathsf{IND-XXX}}_\Pi (B).
    \]

所以 $\mathsf{IND-XXX}$ 安全性并不能直接推出 $m-\mathsf{IND-XXX}$ 安全性，还需要考虑 $\mathcal{O}_{\mathsf{LR}}$ 被调用的次数.

### Real-or-Random

Real-or-Random（ROR）是一种和 $\mathsf{IND}$ 类似的安全性定义，不过需要将之前的 $\mathcal{O}_{\mathsf{LR}}$ Oracle 替换为 $\mathcal{O}_{\mathsf{ROR}}$ Oracle. 该 Oracle 会接收一个明文 $m$，并且随机选择一个比特 $b$，如果 $b = 1$，那么就返回 $e_k (m)$，否则就随机选取一个和 $m$ 等长的明文 $m'$，并返回 $e_k (m')$. 其也可以被调用多次. 以下为 $\mathsf{RoR-CCA}$ 的 Game 描述：

\automata
    \draw (4, 0) rectangle (7, -3);
    \node at (5.5, -1.5) {A};
    \node[align=left, right] at (0, -1.5em) {$k \gets \operatorname{KeyGen}()$};
    \node[align=left, right] at (0, -3em) {$b \gets \{0, 1\}$};
    \node[align=left, right] at (0, -6em) {$b'$};
    \draw[->] (4, -6em) -- (1, -6em);
    \node[align=left, right] at (0, -7.5em) {Win if $b' = b$};
    \node[align=left, right] at (5.9, -1em) {$m \in \mathbb{P}$};
    \draw[->] (7, -1em) -- node[above]{$\mathcal{O}_{\mathsf{RoR}}$} (8.5, -1em);
    \node[align=left, right] at (8.6, -0.5em) {If $b = 0$ then $m' \gets \{0,1\}^{|m|}$};
    \node[align=left, right] at (8.6, -1.5em) {else $m' \gets m$};
    \node[align=left, right] at (8.6, -2.5em) {$c^* \gets e_k (m')$};
    \draw[->] (8.5, -2.5em) -- (7, -2.5em);
    \node[align=left, right] at (5.9, -4em) {$m \in \mathbb{P}$};
    \draw[->] (7, -4em) -- node[above]{$\mathcal{O}_{e_k}$} (8.5, -4em);
    \node[align=left, right] at (8.6, -4.5em) {$c \gets e_k (m)$};
    \draw[->] (8.5, -5em) -- (7, -5em);
    \node[align=left, right] at (5.9, -7em) {$c \in \mathbb{C}$};
    \draw[->] (7, -7em) -- node[above]{$\mathcal{O}_{d_k}$} (8.5, -7em);
    \node[align=left, right] at (8.6, -7em) {If $c = c^* \to$ abort};
    \node[align=left, right] at (8.6, -8em) {$m \gets d_k (c)$};
    \draw[->] (8.5, -8em) -- (7, -8em); 

!!! note "Theorem"
    满足 $\mathsf{IND-CCA}$ 安全性的对称加密方案也满足 $\mathsf{RoR-CCA}$ 安全性. 如果 $A$ 是 $\Pi$ 的一个 $\mathsf{RoR-CCA}$ 敌手，那么存在一个 $\Pi$ 的 $\mathsf{IND-CCA}$ 敌手 $B$，使得

    \[
        \operatorname{Adv}^{\mathsf{RoR-CCA}}_\Pi (A) = \operatorname{Adv}^{\mathsf{IND-CCA}}_\Pi (B).
    \]

    ???+ note "Proof"
        依然是反证法，利用能攻破 $\mathsf{RoR-CCA}$ 的敌手 $A$ 构造一个能攻破 $\mathsf{IND-CCA}$ 的敌手 $B$. 如下所示

        \automata
            \draw (3, 0) rectangle (10, -5);
            \node at (3.5, -0.3) {B};
            \node[align=left, right] at (0, -1.5em) {$k \gets \operatorname{KeyGen}()$};
            \node[align=left, right] at (0, -3em) {$b \gets \{0, 1\}$};
            \node[align=left, right] at (0, -12em) {$b'$};
            \draw[->] (3, -12em) -- (0.5, -12em);
            \node[align=left, right] at (7, -1.5em) {$m_0 \in \mathbb{P}$};
            \draw[->] (8.3, -1.5em) -- (10, -1.5em);
            \draw[->] (10, -1.5em) -- node[above]{$\mathcal{O}_{\mathsf{LR}}$} (11.5, -1.5em);
            \draw[->] (11.5, -2.5em) -- (10, -2.5em);
            \draw[->] (10, -2.5em) -- (9.5, -2.5em);
            \draw[->] (9.5, -2.5em) -- (9.5, -2.8);
            \draw[->] (9.5, -2.8) -- (8.3, -2.8);
            \draw (5.8, -2.3) rectangle (8.3, -4.8);
            \node at (7.05, -3.55) {A};
            \node[align=left, right] at (7, -2.5) {$m_1 \in \mathbb{P}$};
            \draw[->] (8.3, -2.5) -- node[above]{$\mathcal{O}_{\mathsf{RoR}}$} (9.3, -2.5);
            \draw[->] (9.3, -2.5) -- (9.3, -1.5em);
            \node[align=left, right] at (6, -12em) {$b'$};
            \draw[->] (5.8, -12em) -- (3, -12em);
            \draw[->] (8.3, -3.5) -- node[above]{$\mathcal{O}_{e_k}$} (10, -3.5);
            \draw[->] (10, -3.5) -- node[above]{$\mathcal{O}_{e_k}$} (11.5, -3.5);
            \draw[->] (11.5, -3.8) -- (10, -3.8);
            \draw[->] (10, -3.8) -- (8.3, -3.8);
            \draw[->] (8.3, -4.5) -- node[above]{$\mathcal{O}_{d_k}$} (10, -4.5);
            \draw[->] (10, -4.5) -- node[above]{$\mathcal{O}_{d_k}$} (11.5, -4.5);
            \draw[->] (11.5, -4.8) -- (10, -4.8);
            \draw[->] (10, -4.8) -- (8.3, -4.8);

        关于 Advantage 的论述是显然的，因为 $B$ 完美模拟了 $A$ 运行的环境， $A$ 根本无法区分他究竟是在和一个正常的挑战者交互还是在 $B$ 的控制下交互.

问题来到 $\mathsf{RoR}$ 到 $\mathsf{IND}$ 的方向. 事实上，虽然是肯定的，但是会损失一个因子. 

!!! note "Theorem"
    一个 $\mathsf{RoR-CCA}$ 安全的对称加密方案也是 $\mathsf{IND-CCA}$ 安全的. 如果 $A$ 是 $\Pi$ 的一个 $\mathsf{IND-CCA}$ 敌手，那么存在一个 $\Pi$ 的 $\mathsf{RoR-CCA}$ 敌手 $B$，使得

    \[
        \operatorname{Adv}^{\mathsf{IND-CCA}}_\Pi (A) = 2 \cdot \operatorname{Adv}^{\mathsf{RoR-CCA}}_\Pi (B).
    \]

    ???+ note "Proof"
        只给出 $B$ 的叙述性构造.

        - 调用 $A$

        - 如果 $A$ 调用 $\mathcal{O}_{e_k}$，则前递给 $B$ 的 $\mathcal{O}_{e_k}$ 并将结果返回给 $A$

        - 如果 $A$ 调用 $\mathcal{O}_{d_k}$，则前递给 $B$ 的 $\mathcal{O}_{d_k}$ 并将结果返回给 $A$

        - 当 $A$ 调用 $\mathcal{O}_{\mathsf{LR}}$ 时，$B$ 随机选择一个比特 $t \in \{0, 1\}$，并将 $m_t$ 传递给 $B$ 的 $\mathcal{O}_{\mathsf{RoR}}$，而后将结果返回给 $A$

        - 当 $A$ 输出 $b'$ 终止时，若 $t = b'$，则输出 $1$，否则输出 $0$

        当 $b = 0$ 时，$\mathcal{O}_{\mathsf{RoR}}$ 总是返回随机密文，所以 $A$ 没有关于 $m_0$ 和 $m_1$ 中哪个被加密的信息，其做不到比随机猜测更好，成功概率为 $1/2$.

        当 $b = 1$ 时，$\mathcal{O}_{\mathsf{RoR}}$ 将返回 $m_t$ 的有效加密，此时便实现了敌手 $A$ 运行环境的完美模拟. 

        利用条件概率分类讨论有：

        \begin{align*}
            \operatorname{Adv}^{\mathsf{RoR-CCA}}_\Pi (B) &= 2 \cdot \left\lvert \Pr{B \text{ wins}} - \frac{1}{2} \right\rvert \\
                                                          &= 2 \cdot \left\lvert \Pr{B \text{ wins} \mid b = 1} \cdot \Pr{b = 1} + \Pr{B \text{ wins} \mid b = 0} \cdot \Pr{b = 0} - \frac{1}{2} \right\rvert \\
                                                          &= 2 \cdot \left\lvert \Pr{A \text{ wins}} \cdot \Pr{b = 1} + \Pr{b' \neq t} \cdot \Pr{b = 0} - \frac{1}{2} \right\rvert \\
                                                          &= 2 \cdot \left\lvert \Pr{A \text{ wins}} \cdot \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} - \frac{1}{2} \right\rvert \\
                                                          &= \left\lvert \Pr{A \text{ wins}} - \frac{1}{2} \right\rvert \\
                                                          &= \frac{1}{2} \cdot \operatorname{Adv}^{\mathsf{IND-CCA}}_\Pi (A).
        \end{align*}

### Lunchtime Attacks

有时 $\mathsf{CCA}$ 也会被称为自适应选择密文攻击，因为其可以构造和挑战密文相关的解密查询. 而午餐时间攻击类似于 $\mathsf{CCA}$，但其只允许在搜寻阶段调用解密 Oracle. 