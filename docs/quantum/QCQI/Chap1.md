# Fundamental Concepts

## Quantum computation

### Single qubit gates

单比特量子门均可以用 $2 \times 2$ 的酉矩阵表示，且都存在如下的分解形式：

\[
    U = e^{\i \alpha} \begin{bmatrix} e^{-\i \beta/2} & 0 \\ 0 & e^{\i \beta/2} \end{bmatrix} \begin{bmatrix} \cos(\gamma/2) & -\sin(\gamma/2) \\ \sin(\gamma/2) & \cos(\gamma/2) \end{bmatrix} \begin{bmatrix} e^{-\i \delta/2} & 0 \\ 0 & e^{\i \delta/2} \end{bmatrix}
\]

### Multiple qubit gates

以下是一个受控非门的电路图：

\qcircuit
    \lstick{\ket{A}} & \ctrl{1} & \qw &\rstick{\ket{A}} \\
    \lstick{\ket{B}} & \targ & \qw & \rstick{\ket{B \oplus A}}

而其矩阵表示为：

\[
    U_{CN} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}
\]

因为量子门的矩阵表示是酉矩阵，所以它们总是可逆的. 因而传统的异或门和与非门是无法以量子门的形式实现的.

!!! success "结论"
    任意多比特量子门都可以视作单比特量子门和受控非门的组合.

### Quantum circuits

以下是一个量子电路的例子：

\qcircuit
    & \ctrl{1} & \targ & \ctrl{1} & \qw \\
    & \targ & \ctrl{-1} & \targ & \qw

\begin{align*}
    \ket{a, b} & \to \ket{a, a \oplus b} \\
               & \to \ket{a \oplus (a \oplus b), a \oplus b} = \ket{b, a \oplus b} \\
                & \to \ket{b, b \oplus (a \oplus b)} = \ket{b, a}
\end{align*}

由此看出这其实是个交换门，量子电路表示为：

\qcircuit
    & \qswap & \qw \\
    & \qswap \qwx & \qw

量子电路是无环，无扇入，无扇出的.

事实上，对于任何一个量子门 $U$，都可以将其改造为受控的形式：

\qcircuit
    & \qw & \ctrl{1} & \qw \\
    & \qw & \multigate{2}{U} & \qw \\
    & \qw & \ghost{U} & \qw \\
    & \qw & \ghost{U} & \qw 

因而受控非门也等价于一个受控的 $X$ 门.

\qcircuit
    & \ctrl{1} & \qw \\
    & \gate{X} & \qw

下面是测量电路的例子：

\qcircuit
    \lstick{\ket{\psi}} & \qw & \meter & \cw

因为测量后得到的结果是经典的，所以测量后使用的是经典比特.

## Example: Bell states

如下电路是用于制备 Bell 态的电路：

\qcircuit
    & \gate{H} & \ctrl{1} & \qw \\
    & \qw & \targ & \qw

Bell 态可以按如下等式表示：

\[
    \ket{\beta_{xy}} = \dfrac{\ket{0, y} + (-1)^x \ket{1, \bar{y}}}{\sqrt{2}}
\]

以上电路输入 $\ket{xy}$，输出 $\ket{\beta_{xy}}$.

### Example: quantum teleportation

Alice 和 Bob 各持有 Bell 态的一个比特，Alice 想要将一个比特 $\ket{\psi}$ 传输给 Bob，但她并不知道 $\ket{\psi}$ 的具体值. 为了实现这一目标，Alice 需要将 $\ket{\psi}$ 和她持有的 Bell 态进行一系列的操作，最终将 $\ket{\psi}$ 传输给 Bob. 以下是这个过程的电路图：

\qcircuit
    \lstick{\ket{\psi}} & \qw & \qw & \ctrl{1} & \gate{H} & \meter & \control \cw \\
    \lstick{}           & \qw & \qw & \targ    & \qw      & \meter & \cwx \\
    \lstick{}           & \qw & \qw & \qw      & \qw      & \gate{X^{M_2}} \cwx & \gate{Z^{M_1}} \cwx & \rstick{\ket{\psi}} \qw
    \inputgroupv{2}{3}{.8em}{.8em}{\ket{\beta_{00}}}\\

输入态为

\begin{align*}
    \ket{\psi_0} & = \ket{\psi} \ket{\beta_{00}} \\
                 & = \dfrac{1}{\sqrt{2}} \left( \alpha \ket{0}(\ket{00} + \ket{11}) + \beta \ket{1}(\ket{00} + \ket{11}) \right).
\end{align*}

通过受控非门后，状态变为

\[
    \ket{\psi_1} = \dfrac{1}{\sqrt{2}} \left( \alpha \ket{0}(\ket{00} + \ket{11}) + \beta \ket{1}(\ket{10} + \ket{01}) \right).
\]

然后对第一个比特进行 Hadamard 变换，得到

\[
    \ket{\psi_2} = \dfrac{1}{2} \left( \alpha (\ket{0} + \ket{1})(\ket{00} + \ket{11}) + \beta (\ket{0} - \ket{1})(\ket{10} + \ket{01}) \right).
\]

可以重写为

\[
    \ket{\psi_2} = \dfrac{1}{2} \left( \ket{00}(\alpha \ket{0} + \beta \ket{1}) + \ket{01}(\alpha \ket{1} + \beta \ket{0}) + \ket{10}(\alpha \ket{0} - \beta \ket{1}) + \ket{11}(\alpha \ket{1} - \beta \ket{0}) \right).
\]

所以根据前两个比特的测量结果便可以对应地得到 Bob 手中的比特.

\begin{gather*}
    00 \mapsto \ket{\psi_3(00)} \equiv \alpha \ket{0} + \beta \ket{1}, \\
    01 \mapsto \ket{\psi_3(01)} \equiv \alpha \ket{1} + \beta \ket{0}, \\
    10 \mapsto \ket{\psi_3(10)} \equiv \alpha \ket{0} - \beta \ket{1}, \\
    11 \mapsto \ket{\psi_3(11)} \equiv \alpha \ket{1} - \beta \ket{0}.
\end{gather*}

而根据测量结果，Bob 便可以对手中的比特进行相应的操作，从而得到 $\ket{\psi}$，也就是图上的 $Z^{M_1} X^{M_2}$ 操作.

## Quantum algorithms

### Classical computations on a quantum computer

前面提到经典逻辑电路中存在不可逆的门，而量子逻辑电路中的门都是可逆的. 但是，所有经典逻辑电路都可以被一个只含有可逆门的等价电路替代. 这里就需要介绍 Toffoli 门，它是一个三比特门，其电路图如下：

\qcircuit
    \lstick{a} & \ctrl{1} & \qw & \rstick{a} \\
    \lstick{b} & \ctrl{1} & \qw & \rstick{b} \\
    \lstick{c} & \targ & \qw & \rstick{c \oplus (a \land b)}

很显然 Tofooli 门是一个可逆门，其逆就是自身. 它可以被用来实现与非门与扇出，如下图所示：

\qcircuit
    \lstick{a} & \ctrl{1} & \qw & \rstick{a} \\
    \lstick{b} & \ctrl{1} & \qw & \rstick{b} \\
    \lstick{1} & \targ & \qw & \rstick{1 \oplus (a \land b) = \neg (a \land b)}

\qcircuit
    \lstick{1} & \ctrl{1} & \qw & \rstick{1} \\
    \lstick{a} & \ctrl{1} & \qw & \rstick{a} \\
    \lstick{0} & \targ & \qw & \rstick{a}

以上模拟的是确定性的经典逻辑电路，而概率性的电路对于量子电路也并不困难，只需制备出对应概率的量子态即可.

### Quantum parallelism

假定 $f(x): \{0, 1\} \to \{0, 1\}$ 是一个定义域和值域都是一比特的函数，在量子计算机上计算这一函数的话有如下简便的方法. 考虑初始状态为 $\ket{x, y}$，通过合适的逻辑门序列，可以将其变为 $\ket{x, y \oplus f(x)}$. 前者被称为“数据”寄存器，后者被称为“目标”寄存器. 将 $\ket{x, y} \mapsto \ket{x, y \oplus f(x)}$ 这一变换定义为 $U_f$. 容易见得 $U_f$ 是一个可逆的门，因为其逆为本身. 

考虑如下的电路：

\qcircuit
    \lstick{\dfrac{\ket{0} + \ket{1}}{\sqrt{2}}} & \multigate{1}{U_f} & \qw \\
    \lstick{\ket{0}} & \ghost{U_f} & \qw

最终得到的态为

\[
    \ket{\psi} = \dfrac{\ket{0, f(0)} + \ket{1, f(1)}}{\sqrt{2}}.
\]

便得到了一个即包含 $f(0)$ 又包含 $f(1)$ 的态，就好像同时计算了 $x$ 取两个值时的结果. 这就是量子并行性的体现.

这样的步骤通过 Hadamard 变换可以得到更一般的形式，操作便是 $n$ 个 Hadamard 门同时作用在 $n$ 个量子比特上. $n = 2$ 时得到的态为

\[
    \left( \dfrac{\ket{0} + \ket{1}}{\sqrt{2}} \right) \left( \dfrac{\ket{0} + \ket{1}}{\sqrt{2}} \right) = \dfrac{\ket{00} + \ket{01} + \ket{10} + \ket{11}}{2}.
\]

记作 $H^{\otimes 2}$. 一般地，$n$ 个 Hadamard 门作用在 $n$ 个初始态为 $\ket{0}$ 的量子比特上，得到的态为

\[
    H^{\otimes n} \ket{0}^{\otimes n} = \dfrac{1}{\sqrt{2^n}} \sum_{x = 0}^{2^n - 1} \ket{x}.
\]

$n$ 位输入 $1$ 位输出的函数 $f(x)$ 的量子并行评估就可以用类似的方法实现. 准备一个 $n+1$ 位的量子态 $\ket{0}^{\otimes n} \ket{0}$，然后通过 $H^{\otimes n} \otimes \mathbb{I}$ 变换得到

\[
    \dfrac{1}{\sqrt{2^n}} \sum_{x = 0}^{2^n - 1} \ket{x} \ket{0}.
\]

最后通过 $U_f$ 变换得到

\[
    \dfrac{1}{\sqrt{2^n}} \sum_{x = 0}^{2^n - 1} \ket{x} \ket{f(x)}.
\]

不过，如果对以上结果进行测量的话，只能得到其中一个 $x$ 对应的 $f(x)$ 的值. 所以需要能够从类似叠加态 $\dfrac{1}{\sqrt{2^n}} \sum_{x = 0}^{2^n - 1} \ket{x} \ket{f(x)}$ 中提取出 $f(x)$ 的信息，也就是接下来的讨论重点.

### Deutsch's algorithm

下面的电路图通过实现了 Deutsch 算法，来展示量子电路是如何胜过经典电路的.

\qcircuit
    \lstick{\ket{0}} & \gate{H} & \multigate{1}{U_f} & \gate{H} & \meter \\
    \lstick{\ket{1}} & \gate{H} & \ghost{U_f} & \qw & \qw

输入态为 $\ket{\psi_0} = \ket{01}$，经过 Hadamard 变换后得到

\[
    \ket{\psi_1} = \left( \dfrac{\ket{0} + \ket{1}}{\sqrt{2}} \right) \left( \dfrac{\ket{0} - \ket{1}}{\sqrt{2}} \right).
\]

考虑如果对 $\ket{x}(\ket{0} - \ket{1})/\sqrt{2}$ 进行 $U_f$ 变换，将会得到 $(-1)^{f(x)} \ket{x}(\ket{0} - \ket{1})/\sqrt{2}$. 所以 $\ket{\psi_1}$ 经过 $U_f$ 变换后得到

\[
    \ket{\psi_2} = \begin{cases}
        \pm \left( \dfrac{\ket{0} + \ket{1}}{\sqrt{2}} \right) \left( \dfrac{\ket{0} - \ket{1}}{\sqrt{2}} \right) & \text{if } f(0) = f(1), \\
        \pm \left( \dfrac{\ket{0} - \ket{1}}{\sqrt{2}} \right) \left( \dfrac{\ket{0} - \ket{1}}{\sqrt{2}} \right) & \text{if } f(0) \neq f(1).
    \end{cases}
\]

再次经过 Hadamard 变换后得到

\[
    \ket{\psi_3} = \begin{cases}
        \pm \ket{0}\left( \dfrac{\ket{0} - \ket{1}}{\sqrt{2}} \right) & \text{if } f(0) = f(1), \\
        \pm \ket{1}\left( \dfrac{\ket{0} - \ket{1}}{\sqrt{2}} \right) & \text{if } f(0) \neq f(1).
    \end{cases}
\]

而考虑到当 $f(0) = f(1)$ 时，$f(0) \oplus f(1) = 0$，而当 $f(0) \neq f(1)$ 时，$f(0) \oplus f(1) = 1$，所以可以将上式重写为

\[
    \ket{\psi_3} = \pm \ket{f(0) \oplus f(1)} \left( \dfrac{\ket{0} - \ket{1}}{\sqrt{2}} \right).
\]

最后测量第一个比特，便可以得到 $f(0) \oplus f(1)$ 的值. 也就是说，通过一次查询便可以得到 $f(x)$ 的一个全局性质. 

### The Deutsch–Jozsa algorithm

Deutsch 算法实际上是 Deutsch-Jozsa 算法的特例，其用来解决所谓的 Deutsch 问题. 问题描述如下：给定一个函数 $f: \{0, 1\}^n \to \{0, 1\}$，判断 $f$ 是一个常函数还是一个平衡函数. 常函数指的是 $f(x) = 0$ 或 $f(x) = 1$，而平衡函数指的是 $f(x)$ 在 $x$ 取值范围内的一半为 $0$，另一半为 $1$. 最坏的情况下，经典计算机需要查询 $2^{n-1} + 1$ 次才能确定 $f$ 的性质. 而量子计算机只需要一次查询便可以得到 $f$ 的性质，其电路图如下：

\qcircuit
    \lstick{\ket{0}} & {/^n} \qw & \gate{H^{\otimes n}} & \multigate{1}{U_f} & \gate{H^{\otimes n}} & \meter \\
    \lstick{\ket{1}} & \qw & \gate{H} & \ghost{U_f} & \qw & \qw

输入态为 $\ket{\psi_0} = \ket{0}^{\otimes n} \ket{1}$，经过 Hadamard 变换后得到

\[
    \ket{\psi_1} = \sum_{x = 0}^{2^n - 1} \dfrac{\ket{x}}{\sqrt{2^n}} \dfrac{\ket{0} - \ket{1}}{\sqrt{2}}.
\]

再经过 $U_f$ 变换后得到

\[
    \ket{\psi_2} = \sum_{x = 0}^{2^n - 1} \dfrac{(-1)^{f(x)} \ket{x}}{\sqrt{2^n}} \dfrac{\ket{0} - \ket{1}}{\sqrt{2}}.
\]

接下来便是计算 $H^{\otimes n} \ket{x}$ 的结果. 由于 $n = 1$ 时有 $H\ket{x} = (-1)^{xz} \ket{z}/\sqrt{2}$，所以有

\[
    H^{\otimes n} \ket{x_1, \ldots, x_n} = \dfrac{1}{\sqrt{2^n}} \sum_{z_1, \ldots, z_n} (-1)^{x_1 z_1 + \cdots + x_n z_n} \ket{z_1, \ldots, z_n}.
\]

可以简记为

\[
    H^{\otimes n} \ket{x} = \dfrac{1}{\sqrt{2^n}} \sum_{z = 0}^{2^n - 1} (-1)^{x \cdot z} \ket{z}.
\]

其中 $x \cdot z$ 表示 $x$ 和 $z$ 的二进制表示的内积. 所以最终得到的态为

\[
    \ket{\psi_3} = \sum_{x = 0}^{2^n - 1} \sum_{z = 0}^{2^n - 1} \dfrac{(-1)^{f(x) + x \cdot z} \ket{z}}{2^n} \dfrac{\ket{0} - \ket{1}}{\sqrt{2}}.
\]

考虑 $\ket{0}^{\otimes n}$ 的振幅，其为 $\sum_x (-1)^{f(x)} / 2^n$. $f$ 为常函数时，其为 $1$ 或 $-1$，而 $f$ 为平衡函数时，其为 $0$. 所以最后测量前 $n$ 个比特，如果全为 $0$，则 $f$ 为常函数，否则 $f$ 为平衡函数.

### Quantum algorithms summarized

#### Quantum algorithms based upon the Fourier transform

离散傅里叶变换的形式如下所示：

\[
    y_k = \dfrac{1}{\sqrt{N}} \sum_{j = 0}^{N - 1} x_j e^{2\pi \i j k / N}.
\]

量子形式的傅里叶变换如下：

\[
    \ket{j} \to \dfrac{1}{\sqrt{2^n}} \sum_{k = 0}^{2^n - 1} e^{2\pi \i j k / 2^n} \ket{k}.
\]

??? tip "量子傅里叶变换的酉性证明"
    验证保持内积即可. 即 $\bra{j'} U^\dagger U \ket{j} = \delta_{jj'}$.

    \begin{align*}
        \bra{j'} U^\dagger U \ket{j} & = \left(\dfrac{1}{\sqrt{2^n}} \sum_{k' = 0}^{2^n - 1} e^{2\pi \i j' k' / 2^n} \ket{k'}\right)^\dagger \left(\dfrac{1}{\sqrt{2^n}} \sum_{k = 0}^{2^n - 1} e^{2\pi \i j k / 2^n} \ket{k}\right) \\
        & = \dfrac{1}{2^n} \sum_{k' = 0}^{2^n - 1} \sum_{k = 0}^{2^n - 1} e^{2\pi \i (jk - j'k') / 2^n} \innerproduct{k'}{k}
    \end{align*}

    因为 $\innerproduct{k'}{k} = \delta_{kk'}$，所以上式可以化简为

    \[
        \dfrac{1}{2^n} \sum_{k = 0}^{2^n - 1} e^{2\pi \i (j - j')k / 2^n} = \delta_{jj'}.
    \]

    1. $j = j'$ 时，上式即为 $\dfrac{1}{2^n} \sum_{k = 0}^{2^n - 1} 1 = 1$.

    2. $j \neq j'$ 时，令 $\omega = e^{2\pi \i/2^n}$，则上式包含一个等比数列求和：

        \[
            \sum_{k = 0}^{2^n - 1} \omega^{(j - j')k} = \dfrac{1 - \omega^{(j - j')2^n}}{1 - \omega^{j - j'}}.
        \]

        而 $\omega^{2^n} = 1$，所以上式为 $0$.

    综上，量子傅里叶变换是酉的.

如果将量子傅里叶变换应用到一个叠加态 $\sum_{j = 0}^{2^n - 1} x_j \ket{j}$ 上，那么得到的态为

\[
    \sum_{j = 0}^{2^n - 1} x_j \ket{j} \to \dfrac{1}{\sqrt{2^n}} \sum_{k = 0}^{2^n - 1} \left( \sum_{j = 0}^{2^n - 1} x_j e^{2\pi \i j k / 2^n} \right) \ket{k} = \dfrac{1}{\sqrt{2^n}} \sum_{k = 0}^{2^n - 1} y_k \ket{k}.
\]

这和离散傅里叶变换的形式是一致的. 

经典的快速傅里叶变换需要花费 $N \log(N) = n \cdot 2^n$ 步，而量子傅里叶变换可以在 $\log^2(N) = n^2$ 步完成. 

量子傅里叶变换可以用于解决许多问题，包括 Deutsch 问题，用于离散对数和质因数分解的 Shor 算法，以及阿贝尔稳定化子问题，并被推广到了隐藏子群问题.

!!! question "隐藏子群问题"
    设函数 $f$ 从有限生成群 $G$ 映射到有限集合 $X$，满足其在子群 $K$ 的陪集上是常数，并且在不同的赔集上是不同的. 给定一个量子黑盒，其可以执行酉变换 $U \ket{g} \ket{x} = \ket{g} \ket{x \oplus f(g)}$，其中 $g \in G$，$x \in X$，$\oplus$ 是 $X$ 上良定义的二元运算. 问题是找到子群 $K$ 的生成集合.

#### Quantum search algorithms

量子搜索算法则是完全不同的一方面，其专注于解决以下的问题：给定搜索空间，大小为 $N$，并且没有其中的信息的结构的先验知识，希望能够找到一个满足特定性质的元素. 经典搜索算法需要 $O(N)$ 步，而量子搜索算法只需要 $O(\sqrt{N})$ 步.

#### Quantum simulation

!!! warning
    这部分直接机翻了.

模拟自然存在的量子力学系统是量子计算机明显具有优势的任务领域，而经典计算机被认为在这方面存在巨大困难. 经典计算机难以模拟一般量子系统的原因，与它们难以模拟量子计算机的原因本质相同：描述量子系统所需的复数量通常会随系统规模呈指数级增长（而非经典系统中的线性增长）. 一般而言，在经典计算机上存储一个包含 $n$ 个独立组件的量子系统状态，需要约 $c^n$ 比特的内存（其中 $c$ 是与模拟系统细节及精度要求相关的常数）. 

相比之下，量子计算机可以使用 $kn$ 个量子比特进行模拟（其中 $k$ 是取决于模拟系统细节的常数）. 这使得量子计算机能够高效模拟那些被认为经典计算机无法高效模拟的量子力学系统. 但需特别注意：尽管量子计算机能以远超经典计算机的效率模拟许多量子系统，但这并不意味我们能直接获取所需的全部系统信息. 当测量时，$kn$ 个量子比特的模拟会坍缩到确定态，仅给出 $kn$ 比特的信息；波函数中蕴含的 $c^n$ 比特"隐藏信息"无法被完全获取. 因此，实现有效量子模拟的关键在于开发系统化的信息提取方法，而目前对此仅有部分理解. 

尽管存在这一限制，量子模拟仍可能成为量子计算机的重要应用方向. 量子系统模拟是许多领域的关键问题，尤其是在量子化学中——经典计算机的计算限制使得即使模拟中等尺寸分子的行为也极为困难，更不用说许多重要生物系统中存在的超大分子. 因此，实现更快速、更精确的此类系统模拟，可能对量子现象至关重要的其他领域（如材料科学、药物研发等）产生积极的推动作用. 

未来，我们或许会发现某种自然界的物理现象无法被量子计算机高效模拟. 这绝非坏消息，反而是令人振奋的！至少，这将推动我们扩展现有的计算模型以容纳新现象，并提升计算模型的潜力使其超越现有的量子计算框架. 同时，此类现象很可能伴随着极其有趣的新物理效应！

量子模拟的另一重要应用是作为理解其他量子算法的通用方法，例如在第 6.2 节中，我们将解释量子搜索算法如何被视作某个量子模拟问题的解. 通过这种视角，量子搜索算法的本质起源将变得清晰可辨. 

最后，量子模拟还催生了一个与摩尔定律相关且充满乐观主义的“量子推论”. 回顾摩尔定律：在成本不变的情况下，经典计算机的性能每两年左右翻倍. 但若用经典计算机模拟量子系统，当向被模拟系统添加一个量子比特（或更大系统）时，经典计算机存储量子态所需内存将翻倍甚至更多，模拟动力学所需时间也呈类似或更快的增长. 由此产生的量子推论指出：只要量子计算机每两年增加一个量子比特，其性能就能与经典计算机保持同步. 尽管此推论不宜过度严肃看待（因量子计算相比经典计算的确切优势尚未完全明确），但它生动地解释了为何我们应关注量子计算机，并期待其未来至少在某些应用中超越最强经典计算机. 

#### The power of quantum computation

!!! success "结论"
    基于量子并行性的简单变体无法解决所有 $\mathsf{NP}$ 问题.

定义 $\mathsf{BQP}$ 为包含了所有能在多项式时间内被量子计算机解决的，并且能够容忍有界的错误概率的，问题的复杂类.（实际上这让 $\mathsf{BQP}$ 更类似于 $\mathsf{BPP}$，而非 $\mathsf{P}$，不过在接下来的讨论中将其忽略，并认为其类似于 $\mathsf{P}$）. 已知的结论包括了量子计算机可以在多项式时间内解决 $\mathsf{P}$ 类问题，但是不能解决 $\mathsf{PSPACE}$ 外的问题. 因而，如果证明出量子计算机严格强于经典计算机，那么 $\mathsf{P}$ 便不等于 $\mathsf{PSPACE}$. 但后者已经被尝试证明了很多年，仍没有结果，这也就意味着量子计算机是否严格强于经典计算机很可能相当困难.

## Experimental quantum information processing

### The Stern-Gerlach experiment

原始实验使用的是银原子束，为了方便介绍，这里描述的实际是氢原子的实验. 

氢原子包含一个质子和一个电子，因为电子的运动会产生磁矩，所以氢原子也有磁矩，并且轴向相对于旋转电子的轴向，类似于小棒状磁体. 而小棒状磁体通过磁场的话会被偏转，也就是实验观察的现象.

原子如何偏转取决于两点，一是原子的磁偶极矩，二是 Stern-Gerlach 装置生成的磁场强度. 通过适当的控制 Stern-Gerlach 装置生成的磁场，可以做到让原子的偏转量取决于其磁偶极矩的 $\hat{z}$ 方向的分量，其中 $\hat{z}$ 是某个固定的外部轴.

而实验进行后，有两个出人意料的结果浮出水面. 首先，因为热原子束离开加热炉时，原子的磁偶极矩应当是各向随机分布的，所以预期能在 Stern-Gerlach 装置中看见各个角度的原子的连续分布. 然而，实际观测到的是原子以一组离散的角度出射. 物理学家通过假设原子的磁偶极矩是**量子化**的成功解释了这一现象.

第二个结果便是该实验中观察到的峰的数量. 选用氢原子的原因之一是它的磁偶极矩为零，经典情况下这对应无电子绕轨旋转，但在当时的量子力学基础下这也是可以被接受的. 而正因为氢原子的磁偶极矩为零，预期上只会看到一束没有被偏转的原子束. 但事实上观察到了两束原子，一束被向上偏转，另一束被向下偏转.

这一令人困惑的“分裂成两束”的现象，最终通过假设氢原子中的电子和一个称为**自旋**的量相关联才得以解决. 人们假设，除了电子轨道运动的贡献外，电子的自旋还会对氢原子的磁偶极矩产生额外的影响.

\automata
    \draw (0, 0) rectangle (2, 4);
    \node at (1, 2) {$oven$};
    \draw[->] (2, 2) -- (3, 2);
    \draw (3, 0) rectangle (5, 4);
    \node at (4, 2) {Z};
    \draw[->] (5, 3) -- (6, 3);
    \draw[->] (5, 1) -- (6, 1);
    \node at (6.5, 3) {$\left| +Z \rangle \right.$};
    \node at (6.5, 1) {$\left| -Z \rangle \right.$};

上图是原始的 Stern–Gerlach 实验示意图. 而为了进一步探究自旋的描述，将两个 Stern–Gerlach 装置级联，然后将第二个装置侧向倾斜，使其磁场沿着 $\hat{x}$ 轴方向偏转原子，并且阻挡 $\ket{-Z}$ 的原子束. 这样，只有 $\ket{+Z}$ 的原子束能够通过第二个装置. 最终在输出端放置探测器测量.

\automata
    \draw (0, 0) rectangle (2, 4);
    \node at (1, 2) {$oven$};
    \draw[->] (2, 2) -- (3, 2);
    \draw (3, 0) rectangle (5, 4);
    \node at (4, 2) {Z};
    \draw[->] (5, 3) -- (6, 3);
    \draw[->] (5, 1) -- (6, 1);
    \node at (6.5, 3) {$\left| +Z \rangle \right.$};
    \node at (6.5, 1) {$\left| -Z \rangle \right.$};
    \draw[->] (7, 3) -- (8, 3);
    \node at (7.5, 1) {Block};
    \draw (8, 0) rectangle (10, 4);
    \node at (9, 2) {X};
    \draw[->] (10, 3) -- (11, 3);
    \draw[->] (10, 1) -- (11, 1);
    \node at (11.5, 3) {$\left| +X \rangle \right.$};
    \node at (11.5, 1) {$\left| -X \rangle \right.$};

经典的指向 $\hat{z}$ 方向的磁偶极矩没有 $\hat{x}$ 方向上的净磁矩，所以最后的输出结果期望是一个中心峰. 但事实上实验观察到了两个峰，并且强度一致. 所以可能原子在每个轴上都独立地有一个确定的磁偶极矩，每个通过第二个装置的原子束都可以用 $\ket{+Z} \ket{+X}$ 或 $\ket{-Z} \ket{-X}$ 来描述. 

下图是另一个用于验证假设的实验：

\automata
    \draw (0, 0) rectangle (2, 4);
    \node at (1, 2) {$oven$};
    \draw[->] (2, 2) -- (3, 2);
    \draw (3, 0) rectangle (5, 4);
    \node at (4, 2) {Z};
    \draw[->] (5, 3) -- (6, 3);
    \draw[->] (5, 1) -- (6, 1);
    \node at (6.5, 3) {$\left| +Z \rangle \right.$};
    \node at (6.5, 1) {$\left| -Z \rangle \right.$};
    \draw[->] (7, 3) -- (8, 3);
    \node at (7.5, 1) {Block};
    \draw (8, 0) rectangle (10, 4);
    \node at (9, 2) {X};
    \draw[->] (10, 3) -- (11, 3);
    \draw[->] (10, 1) -- (11, 1);
    \node at (11.5, 3) {$\left| +X \rangle \right.$};
    \node at (11.5, 1) {$\left| -X \rangle \right.$};
    \draw[->] (12, 3) -- (13, 3);
    \node at (12.5, 1) {Block};
    \draw (13, 0) rectangle (15, 4);
    \node at (14, 2) {Z};
    \draw[->] (15, 3) -- (16, 3);
    \draw[->] (15, 1) -- (16, 1);
    \node at (16.5, 3) {$\left| +Z \rangle \right.$};
    \node at (16.5, 1) {$\left| -Z \rangle \right.$};

这个实验将一束先前输出的原子束输入到了第二个沿 $\hat{z}$ 方向偏转的 Stern-Gerlach 装置中. 如果这些原子依然保持 $\ket{+Z}$ 的轴向，那么输出应当只有一个峰. 但实际上再次观察到了两个峰，并且强度一致. 结果与经典预期相反，表明自旋为 $\ket{+Z}$ 的原子束在由等比例的 $\ket{+X}$ 和 $\ket{-X}$ 组成，而 $\ket{+X}$ 的原子束又由等比例的 $\ket{+Z}$ 和 $\ket{-Z}$ 组成. 即使 Stern-Gerlach 装置的磁场方向发生了变化，比如沿着 $\hat{y}$ 方向，也会得到类似的结果.

量子比特模型提供了一个对实验结果的简单解释. 考虑

\begin{align*}
    \ket{+Z} & \from \ket{0}, \\
    \ket{-Z} & \from \ket{1}, \\
    \ket{+X} & \from \dfrac{\ket{0} + \ket{1}}{\sqrt{2}}, \\
    \ket{-X} & \from \dfrac{\ket{0} - \ket{1}}{\sqrt{2}}.
\end{align*}

级联 Stern-Gerlach 装置的实验结果可以用量子比特模型描述为 $\hat{z}$ 方向偏转的 Stern-Gerlach 装置在 $\ket{0}$ 和 $\ket{1}$ 这组计算基上进行测量，而 $\hat{x}$ 方向偏转的 Stern-Gerlach 装置在 $\dfrac{\ket{0} + \ket{1}}{\sqrt{2}}$ 和 $\dfrac{\ket{0} - \ket{1}}{\sqrt{2}}$ 这组计算基上进行测量.

这个例子证明了量子比特是一个可信的用来给自然中的系统建模的方式，并且我们认为量子比特能够描述所有物理系统.

### Prospects for practical quantum information processing

存在两种可能的原则性障碍组织我们进行某种形式的量子信息处理，一是量子噪声，二是量子力学本身存在错误.

量子噪声方面，其被量子计算阈值定理限制. 该定理大致可以表述为，只要量子计算机中的噪声水平低于某个阈值，那么量子纠错编码就可以进一步将其压制，并且理论上可以趋近于零，而只需付出一些微小的计算复杂度代价. 

量子力学方面则是对世界描述正确性验证的兴趣之激励.

- 小规模应用：量子态层析和量子过程层析，小规模量子通信原语

- 中等规模应用：量子系统模拟

- 大规模应用：大数分解、离散对数求解和量子搜索

- 量子信息处理方法：基于光学技术的方案，原子囚禁技术和核磁共振技术

## Quantum information

量子信息理论的基本目标：

1. 识别量子力学中静态资源的基本类别. 一个例子是量子比特，另一个则是经典比特. 另一个基本类别的静态资源示例是两方共享的 Bell 态.

2. 识别量子力学中动态过程的基本类别. 一个简单的例子是内存，即在一段时间内存储量子态的能力. 更复杂的例子包括 Alice 和 Bob 之间的量子信息传输，复制（或尝试复制）量子态，以及保护量子信息处理免受噪声影响的过程.

3. 量化执行基本动态过程时产生的资源权衡. 例如：在使用噪声通信信道时，两方之间可靠传输量子信息所需的最小资源是什么？

### Quantum information theory: example problems

#### Classical information through quantum channels

经典信息论的重要结果是 Shannon 的无噪信道编码定理和有噪信道编码定理. 无噪信道编码定理量化了存储信息源发出的信息所需的比特数，而有噪信道编码定理则量化了在噪声通信信道中能够可靠传输的信息量.

那么，信源是什么呢？如何定义信源是经典和量子信息论中重要的问题，之后还要重复检查多次. 首先给出一个临时的定义：一个经典信源可以用一组概率 $p_j, j = 1, \ldots, d$ 来描述. 每次使用信源都会使得 $j$ 对应的字符被传输，选择到 $j$ 的概率为 $p_j，并且每次传输都是独立的. 

Shannon 的无噪信道编码定理量化了压缩方案能够工作的极限，更准确地说，用概率组 $\{p_j\}$ 描述的经典信源可以被压缩到平均每次信源使用仅需 $H(p_j)$ 比特表示，其中 $H(p_j) = -\sum_j p_j \log_2 p_j$ 是 Shannon 熵，并且如果尝试使用少于 $H(p_j)$ 比特来表示信源的话，解压时出错的概率会相当高.

Shannon 的无噪信道编码定理为信息论的三大目标提供了一个经典范例：

- 识别静态资源：比特和信源

- 定义动态过程：两阶段动态过程，压缩信息源和解压以恢复信息源

- 量化资源消耗：找到最优数据压缩方案所需资源量的定量标准

而 Shannon 的有噪信道编码定理则量化了有噪信道中可靠传输信息的极限. 这可能是两地通过有噪信道通信，或是两个时间段之间通过有噪信道传输信息. 统一的想法是使用纠错码编码信息，使得传输时引入的噪声可以在另一端被纠正，而做到这点则需要引入冗余. 例如，假定有噪信道传输的是单比特，而为了确保可靠传输需要使用两比特编码，那么这个信道的容量就是 $1/2$ 比特. 

Shannon 的有噪信道编码定理同样达成了信息论的三大目标：

- 识别静态资源：比特和信源

- 定义动态过程：信道噪声作为主过程，还包括对抗噪声的编码和解码过程

- 量化资源消耗：在固定噪声模型下，给出了可靠信息传输所需的最小冗余量

以上两个定理 Shannon 仅考虑了使用经典系统存储信息源的输出. 那么，对于量子信息论而言，若将存储介质改为用量子态作为载体传输经典信息，会发生什么？事实上，在无噪信道中传输信息时，量子比特并不能显著减少所需的通信资源量.

自然而然，接下来考虑的是在有噪信道中传输信息. 理想情况下，应当会得到一个能够量化信道传输信息的容量的结果. 然而，评估容量因为好些个原因而变得复杂. 因为整个过程发生在连续的空间中，量子力学会给出多种噪声的模型，并且如何改造经典纠错码以对抗这些噪声也尚不明朗.

#### Quantum information through quantum channels

量子态本身也是静态资源. 接下来主要介绍 Shannon 定理的量子版本，其中包括了量子态的压缩和解压缩.

第一个问题是如何定义量子信源. 类似于经典信源，量子信源也有几种定义方式，不过为了方便还是采用一种临时的定义：量子信源可以用一个概率组 $\{p_j\}$ 和对应的量子态 $\ket{\psi_j}$ 来描述. 每次使用信源都会使得以 $p_j$ 的概率产生 $\ket{\psi_j}$，并且每次传输都是独立的.

那么是否有可能压缩这一量子力学信源的输出呢？考虑这样的一个例子：

!!! example
    一个单量子比特源，产生 $\ket{0}$ 的概率为 $p$，产生 $\ket{1}$ 的概率为 $1 - p$. 这与经典信源的对应情况几乎没有区别，所以只需要 $H(p, 1 - p)$ 量子比特来表示这个信源的输出.

    但如果考虑其产生 $\ket{0}$ 和 $\ket{+}$ 的概率分别为 $p$ 和 $1 - p$ 呢？因为无法区分 $\ket{0}$ 和 $\ket{+}$，经典的压缩方案不再适用.

所以情况是压缩方案依然可行，但是未必是无错误的. 为了衡量压缩解压缩造成的扭曲，我们引入了保真率这一概念.

Schumacher 的无噪信道编码定理量化了限制保真率接近于 1 的情况下进行量子压缩所需要的资源. 如果信源产生的是正交的量子态的话，Schumacher 的定理表明压缩不会超过经典极限 $H(P_j)$. 而在非正交的情况下，答案就不是 Shannon 熵，而是所谓的 von Neumann 熵. 当量子态都是正交的时，von Neumann 熵的数值于 Shannon 熵相同，而在非正交的情况下，von Neumann 熵会严格小于 Shannon 熵.

这种资源需求的减少其实很容易理解. 以上面的例子进行计算，假定信源产生 $\ket{0}$ 和 $\ket{+}$ 的概率分别为 $p$ 和 $1 - p$，并且使用了 $n$ 次，$n$ 是一个很大的数. 那么依据大数定律，信源很可能传输了 $np$ 个 $\ket{0}$ 和 $n(1 - p)$ 个 $\ket{+}$，忽略重排的情况下，也就是有如下的量子态：

\[
    \ket{0}^{\otimes np} \left( \dfrac{\ket{0} + \ket{1}}{\sqrt{2}} \right)^{\otimes n(1 - p)}.
\]

而 $n(1 - p)$ 也是一个很大的数，所以 $\ket{+}^{\otimes n(1 - p)}$ 的展开式可以用如下的近似表示：

\[
    \left( \dfrac{\ket{0} + \ket{1}}{\sqrt{2}} \right)^{\otimes n(1 - p)} \approx \ket{0}^{\otimes n(1 - p)/2} \ket{1}^{\otimes n(1 - p)/2}.
\]

源传输的总态也就可以近似为

\[
    \ket{0}^{\otimes n(1 + p)/2} \ket{1}^{\otimes n(1 - p)/2}.
\]

那么这样的态有多少个呢？根据二项式定理，这样的态有 $\binom{n}{n(1 + p)/2}$ 个，根据 Stirling 近似，这个数值为 $N = 2^{n H((1 + p)/2, (1 - p)/2)}$，其中 $H$ 是熵函数. 

一种简单的压缩方案如下：

1. 将所有符合如上条件的态记为 $\ket{c_1}, \ldots, \ket{c_N}$.

2. 对源传输的 $n$ 个量子比特进行酉变换，将每个态 $\ket{c_j}$ 映射到

    \[
        \ket{j}\ket{0}^{\otimes n - n H((1 + p)/2, (1 - p)/2)}.
    \]

    其中 $j$ 是一个长度为 $n H((1 + p)/2, (1 - p)/2)$ 的数.

3. 丢弃最后的 $n - n H((1 + p)/2, (1 - p)/2)$ 个量子比特，得到压缩后的态，只需要 $n H((1 + p)/2, (1 - p)/2)$ 个量子比特.

4. 解压缩时，对每个态追加 $n - n H((1 + p)/2, (1 - p)/2)$ 个 $\ket{0}$，然后对每个态进行逆酉变换.

这只是个简单的示例，Schumacher 的定理事实上能做的更好. 究其本源，其实是利用了 $\ket{0}$ 和 $\ket{+}$ 并不正交，因而会产生一定的冗余.

Schumacher 的无噪信道编码定理类似于 Shannon 的无噪信道编码定理. 下一步便是考虑 Shannon 的有噪信道编码定理的量子版本，这一部分运用了量子纠错码的理论，但是尚未得到令人满意的结果.

#### Quantum distinguishability

目前为止，我们考虑的所有动态过程在经典情况和量子情况中都有出现. 但是，例如量子态等新种类信息的引入扩展了动态过程的类别. 一个例子便是量子态的区分.

非正交量子态的不可区分性是量子计算和量子信息的核心. 这是断言量子态包含隐藏信息的本质，因而在量子算法和量子密码学中扮演着重要角色. 量子信息论的一个重要问题便是如何量化非正交量子态的区分.

1. 区分任意量子态意味着超光速通信. 

2. 量子态不可区分也有其益处，如量子货币.

#### Creation and transformation of entanglement

纠缠态也是一个基本的静态资源. 创建纠缠是量子信息论中一个简单的动态过程，第二个动态过程是纠缠的转换.