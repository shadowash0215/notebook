# ABY Protocol

## Arithmetic Sharing

对于一个 $l$ 位的整数 $x$，我们可以将其拆分为两个 $\mathbb{Z}_{2^l}$ 上的数之和，即对于 $x$ 的 Arithmetic Sharing $\langle x \rangle^A$ 是满足 

\[
    \langle x \rangle^A_0 + \langle x \rangle^A_1 \equiv x \pmod{2^l}
\]

的两个数，其中 $\langle x \rangle^A_0, \langle x \rangle^A_1 \in \mathbb{Z}_{2^l}$，被称为 $x$ 的两个 shared values。

share ($\operatorname{Shr}_i^A(x)$) 的过程为 $P_i$ 选择一个随机数 $r \in _R \mathbb{Z}_{2^l}$，然后计算 $\langle x \rangle^A_i = x - r \pmod{2^l}$，将 $r$ 发送给 $P_{1-i}$，$P_{1-i}$ 设定 $\langle x \rangle^A_{1-i} = r$；reconstruct ($\operatorname{Rec}_i^A(x)$) 的过程为 $P_{1-i}$ 将 $\langle x \rangle^A_{1-i}$ 发送给 $P_i$，$P_i$ 计算 $x = \langle x \rangle^A_0 + \langle x \rangle^A_1 \pmod{2^l}$。

每个 Arithmetic Circuit 都是有一系列的加法门和乘法门组成，这两个运算的操作如下：

- 加法：$\langle z \rangle^A = \langle x \rangle^A + \langle y \rangle^A$: $P_i$ 在本地计算 $\langle z \rangle^A_i = \langle x \rangle^A_i + \langle y \rangle^A_i$ 即可；

- 乘法：$\langle z \rangle^A = \langle x \rangle^A \cdot \langle y \rangle^A$: 乘法需要预先计算出一个乘法三元组，形式为 $\langle c \rangle^A = \langle a \rangle^A \cdot \langle b \rangle^A$，$P_i$ 设定 $\langle e \rangle^A_i = \langle x \rangle^A_i - \langle a \rangle^A_i$ 和 $\langle f \rangle^A_i = \langle y \rangle^A_i - \langle b \rangle^A_i$，双方都进行 $\operatorname{Rec}^A (e)$ 和 $\operatorname{Rec}^A (f)$ 操作，而后 $P_i$ 计算 $\langle z \rangle^A_i = i \cdot e \cdot f + f \cdot \langle a \rangle^A_i + e \cdot \langle b \rangle^A_i + \langle c \rangle^A_i$。  

??? note "Proof"
    \begin{align}
        \langle z \rangle^A_0 & = f \cdot \langle a \rangle^A_0 + e \cdot \langle b \rangle^A_0 + \langle c \rangle^A_0 \\
        \langle z \rangle^A_1 & = e \cdot f + f \cdot \langle a \rangle^A_1 + e \cdot \langle b \rangle^A_1 + \langle c \rangle^A_1 \\
        z & = \langle z \rangle^A_0 + \langle z \rangle^A_1 \\
        & = e \cdot f + a \cdot f + b \cdot e + c \\
        & = (x - a) \cdot (y - b) + a \cdot (y - b) + b \cdot (x - a) + a \cdot b \\
        & = x \cdot y
    \end{align}

但是乘法三元组的生成也应是以秘密分享的形式进行的，注意到

\begin{align}
    c & = a \cdot b \\
    & = (\langle a \rangle^A_0 + \langle a \rangle^A_1) \cdot (\langle b \rangle^A_0 + \langle b \rangle^A_1) \\
    & = \langle a \rangle^A_0 \cdot \langle b \rangle^A_0 + \langle a \rangle^A_0 \cdot \langle b \rangle^A_1 + \langle a \rangle^A_1 \cdot \langle b \rangle^A_0 + \langle a \rangle^A_1 \cdot \langle b \rangle^A_1
\end{align}

问题就是解决其中交叉项的计算，对应有两种方法：

- 同态加密：使用 Paillier or DGK，同态性为明文加法对应密文乘法，明文乘法对应密文指数幂。对于 Paillier，选择 $r \in_R \mathbb{Z}_{2^{2l + 1 + \sigma}}$，其中 $\sigma$ statistic security parameter；对于 DGK，选择 $r \in_R \mathbb{Z}_{2^{2l + 1}}$。
    1. $P_1$ 计算 $\langle c \rangle^A_1 = \langle a \rangle^A_1 \cdot \langle b \rangle^A_1 - r \pmod{2^l}$.  
    2. $P_0$ 发送 $\operatorname{Enc}_0 (\langle a \rangle^A_0)$ 和 $\operatorname{Enc}_0 (\langle b \rangle^A_0)$ 给 $P_1$.  
    3. $P_1$ 计算 $d = \operatorname{Enc}_0(\langle a \rangle^A_0) ^ {\langle b \rangle^A_1} \cdot \operatorname{Enc}_0(\langle b \rangle^A_0) ^ {\langle a \rangle^A_1} \cdot \operatorname{Enc}_0(r)$ 后发送给 $P_0$.  
    4. $P_0$ 计算 $\langle c \rangle^A_0 = \langle a \rangle^A_0 \cdot \langle b \rangle^A_0 + \operatorname{Dec}_0(d) \pmod{2^l}$.

- OT Extension：$P_0$ 随机生成 $\langle a \rangle^A_0$ 和 $\langle b \rangle^A_0$，$P_1$ 随机生成 $\langle a \rangle^A_1$ 和 $\langle b \rangle^A_1$。以下描述如何计算 $\langle a \rangle^A_0 \cdot \langle b \rangle^A_1$，$\langle a \rangle^A_1 \cdot \langle b \rangle^A_0$ 只需要互换双方角色即可。明文传输是不安全的，所以计算的是 $\langle u \rangle^A = \langle a \rangle^A_0 \cdot \langle b \rangle^A_1$ 的 Arithmetic Sharing。  
    1. 双方参与一个 $\operatorname{C-OT}^l_l$，其中 $P_0$ 作为发送方，$P_1$ 作为接收方. 
    2. 第 $i$ 轮，$P_1$ 将 $\langle b \rangle^A_1[i]$ 作为 OT 的选择比特，$P_0$ 则输入相关性函数 $f_{\Delta_i} (x) = (\langle a \rangle^A_0 \cdot 2^i - x) \bmod 2^l$.  
    3. $P_0$ 获得输出 $(s_{i, 0}, s_{i, 1})$，其中 $s_{i, 0} \in_R \mathbb{Z}_{2^l}$，$s_{i, 1} = f_{\Delta_i} (s_{i, 0}) = (\langle a \rangle^A_0 \cdot 2^i - s_{i, 0}) \bmod 2^l$。  
    4. $P_1$ 获得输出 $s_{i, \langle b \rangle^A_1[i]} = (\langle b \rangle^A_1[i] \cdot \langle a \rangle^A_0 \cdot 2^i - s_{i, 0}) \bmod 2^l$。  
    5. $P_0$ 设定 $\langle u \rangle^A_0 = (\sum_{i = 0}^{l - l} s_{i, 0}) \bmod 2^l$，$P_1$ 设定 $\langle u \rangle^A_1 = (\sum_{i = 0}^{l - 1} s_{i, \langle b \rangle^A_1[i]}) \bmod 2^l$。

??? note "Proof"
    \begin{align}
        \langle a \rangle^A_0 \cdot \langle b \rangle^A_1 & = \langle u \rangle^A_0 + \langle u \rangle^A_1 \\
        & = \sum_{i = 0}^{l - 1} s_{i, 0} + \sum_{i = 0}^{l - 1} s_{i, \langle b \rangle^A_1[i]} \\
        & = \sum_{i = 0}^{l - 1} (s_{i, 0} + \langle b \rangle^A_1[i] \cdot \langle a \rangle^A_0 \cdot 2^i - s_{i, 0}) \\
        & = \sum_{i = 0}^{l - 1} \langle b \rangle^A_1[i] \cdot \langle a \rangle^A_0 \cdot 2^i \\
    \end{align}

    展开后就会发现这是二进制乘法的过程。

## Boolean Sharing

对于一个 1 位的 $x$，其 Boolean sharing $\langle x \rangle^B$ 是满足 $\langle x \rangle^B_0 \oplus \langle x \rangle^B_1 = x$ 的两个数，其中 $\langle x \rangle^B_0, \langle x \rangle^B_1 \in \mathbb{Z}_2.$ share 和 reconstruct 的过程与 Arithmetic Sharing 类似，只是加法操作变为了异或操作。

因为每个逻辑函数都可以用异或门和与门来表示，所以 Boolean Circuit 只需要异或门和与门即可。具体的操作如下：

- 异或：$\langle z \rangle^B = \langle x \rangle^B \oplus \langle y \rangle^B$: $P_i$ 在本地计算 $\langle z \rangle^B_i = \langle x \rangle^B_i \oplus \langle y \rangle^B_i$ 即可；  

- 与：$\langle z \rangle^B = \langle x \rangle^B \land \langle y \rangle^B$: 同样需要一个乘法三元组，$P_i$ 设定 $\langle e \rangle^B_i = \langle x \rangle^B_i \oplus \langle a \rangle^B_i$ 和 $\langle f \rangle^B_i = \langle y \rangle^B_i \oplus \langle b \rangle^B_i$，双方都进行 $\operatorname{Rec}^B (e)$ 和 $\operatorname{Rec}^B (f)$ 操作，而后 $P_i$ 计算 $\langle z \rangle^B_i = i \cdot e \cdot f \oplus f \cdot \langle a \rangle^B_i \oplus e \cdot \langle b \rangle^B_i \oplus \langle c \rangle^B_i$。

    不过此处的乘法三元组可以使用 $\operatorname{R-OT}_1^2$ 来生成。首先来看如何随机生成满足 $a \land b = u \oplus v$ 的 $(a, u), (b, v)$：

    1. $R$ 随机选择 $a \in_R \mathbb{Z}_2$.  
    2. $S$ 和 $R$ 进行 $\operatorname{R-OT}_1^1$，$R$ 将 $a$ 作为选择比特.  
    3. $S$ 得到 bits $x_0, x_1$，$R$ 得到 $x_a$.  
    4. $R$ 设定 $u = x_a$, $S$ 设定 $b = x_0 \oplus x_1$ 和 $v = x_0$，注意到 $a \land b = a \land (x_0 \oplus x_1) = (a \land (x_0 \oplus x_1) \oplus x_0) \oplus x_0 = x_a \oplus x_0 = u \oplus v$.

    所以第一次 $\operatorname{R-OT}_1^1$ 由 $P_0$ 作为接收方，$P_1$ 作为发送方，得到 $(a_0, u_0), (b_1, v_1)$；第二次 $\operatorname{R-OT}_1^1$ 由 $P_1$ 作为接收方，$P_0$ 作为发送方，得到 $(b_0, v_0), (a_1, u_1)$。$P_i$ 设定 $c_i = (a_i \land b_i) \oplus u_i \oplus v_i$。

## Yao Sharing

Garbler 将函数表示为一个 Boolean Circuit，并且对每根导线 $w$ 都生成两个键值 $(k_0^w, k_1^w)$，$k_0^w, k_1^w \in \{0, 1\}^\kappa$，然后 garbler 使用加密函数 $\operatorname{Gb}$ 加密输入在所有取值组合下所得到的输出，作为混淆表 $T$ 的内容。然后 Garbler 将 Garbled Circuit 发送给 Evaluator，Evaluator 迭代地解密混淆表中的内容，直到得到输出。

假定 $P_0$ 作为 Garbler，$P_1$ 作为 Evaluator，这里使用了 free-XOR 和 point-and-permute 两种优化技术，具体的操作如下：

1. Garbler 选择一个全局的 $\kappa$ 位二进制串 $R$，并且 $R[0] = 1$.  
2. 对每一根导线 $w$，$k_0^w \in \{0, 1\}^\kappa$ 随机生成，$k_1^w = k_0^w \oplus R$，二者的 LSB 满足 $k_1^w[0] = 1 - k_0^w[0]$，被称为 Permutation Bit.

因为 $P_0$ 持有导线 $w$ 的两个键值，而 $P_1$ 是根据输入值 $x$ 来选择对应的键值，所以 Yao Sharing 的 Shared values 为 $\langle x \rangle^Y_0 = k_0, \langle x \rangle^Y_1 = k_x = k_0 \oplus (R \land x)$.

Share 的过程与前面不同，需要区分 $P_0$ 和 $P_1$ 的角色：

- $\operatorname{Shr}^Y_0 (x)$: 采样 $\langle x \rangle^Y_0 \in_R \{0, 1\}^\kappa$，发送 $k_x = \langle x \rangle^Y_0 \oplus (R \land x)$ 给 $P_1$.  
- $\operatorname{Shr}^Y_1 (x)$: 双方参与 $C-OT^1_\kappa$，$P_0$ 作为发送方，输入关联函数 $f(x) = x \oplus R$，得到 $(k_0, k_1)$，$P_1$ 作为接收方，得到 $\langle x \rangle^Y_1 = k_x$.

Reconstruct ($\operatorname{Rec}^Y_i (x)$) 的过程为 $P_{1-i}$ 将其 Permutation Bit $\pi = \langle x \rangle^Y_{1-i}[0]$ 发送给 $P_i$，$P_i$ 计算 $x = \pi \oplus \langle x \rangle^Y_i[0]$。