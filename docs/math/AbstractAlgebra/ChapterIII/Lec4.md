# Hom 和 Tensor 

!!! note "定理"
    设 $A, B, C, D$ 是环 $R$ 上的模，$\varphi: A \to C, \psi: B \to D$ 是 $R$-模同态，则映射

    \[
        \theta: \operatorname{Hom}_R(A, B) \rightarrow \operatorname{Hom}_R(C, D), \quad f \mapsto \psi f \varphi
    \]

    是阿贝尔群的群同态.

通常将 $\theta$ 写作 $\operatorname{Hom}_R(\varphi, \psi)$，并且称作**由 $\varphi$ 和 $\psi$ 诱导的同态**(induced homomorphism)。注意对于同态 $\varphi_1: E \to C, \varphi_2: C \to A, \psi_1: B \to D, \psi_2: D \to F$，我们有

\begin{gather}
    \operatorname{Hom}(\varphi_1, \psi_2) \operatorname{Hom}(\varphi_2, \psi_1) = \operatorname{Hom}(\varphi_2 \varphi_1, \psi_2 \psi_1): \\
    \operatorname{Hom}_R{A, B} \to \operatorname{Hom}_R{E, F}
\end{gather}

诱导同态有两个特殊情况。如果 $B = D$ 且 $\psi = 1_B$，则诱导同态 $\operatorname{Hom}_R(\varphi, 1_B): \operatorname{Hom}_R(A, B) \to \operatorname{Hom}_R(C, B)$ 为 $f \mapsto f \varphi$，记作 $\bar{\varphi}$。如果 $A = C$ 且 $\varphi = 1_A$，则诱导同态 $\operatorname{Hom}_R(1_A, \psi): \operatorname{Hom}_R(A, B) \to \operatorname{Hom}_R(A, D)$ 为 $f \mapsto \psi f$，记作 $\bar{\psi}$。

下面考察 $\operatorname{Hom}_R$ 与正合序列相关的性质.  

!!! note "定理"
    设 $R$ 是环，则 $0 \to A \xrightarrow{\varphi} B \xrightarrow{\psi} C \to 0$ 是 $R$-模的正合序列等价于对于每个 $R$-模 $D$，序列 $0 \to \operatorname{Hom}_R(D, A) \xrightarrow{\bar{\varphi}} \operatorname{Hom}_R(D, B) \xrightarrow{\bar{\psi}} \operatorname{Hom}_R(D, C)$ 是阿贝尔群的正合序列.  

??? note "证明"
    $(\Rightarrow)$ 若 $0 \to A \xrightarrow{\varphi} B \xrightarrow{\psi} C \to 0$ 是正合的，我们需要证明：  
    (i) $\operatorname{Ker} \bar{\varphi} = 0$；(ii) $\operatorname{Im} \bar{\varphi} \subset \operatorname{Ker} \bar{\psi}$；(iii) $\operatorname{Ker} \bar{\psi} \subset \operatorname{Im} \bar{\varphi}$.  
    (i) $f \in \operatorname{Ker} \bar{\varphi} \Rightarrow \varphi f = 0 \Rightarrow \varphi f(x) = 0, \forall x \in D$. 因为 $0 \to A \xrightarrow{\varphi} B$ 正合，由 $\varphi$ 的单射性可知 $f(x) = 0, \forall x \in D \Rightarrow f = 0$. 从而 $\operatorname{Ker} \bar{\varphi} = 0$.  
    (ii) 由正合性可知 $\operatorname{Im} \varphi = \operatorname{Ker} \psi$，所以 $\psi \varphi = 0$，于是 $\bar{\psi} \bar{\varphi} = \overline{\psi \varphi} = 0$. 因此 $\operatorname{Im} \bar{\varphi} \subset \operatorname{Ker} \bar{\psi}$.  
    (iii) $g \in \operatorname{Ker} \bar{\psi} \Rightarrow \psi g = 0 \Rightarrow \operatorname{Im} g \subset \operatorname{Ker} \psi = \operatorname{Im} \varphi$. 因为 $\varphi$ 是单同态，从而 $\varphi: A \to \operatorname{Im} \varphi$ 是同构. 如果 $h$ 是复合映射 $D \xrightarrow{g} \operatorname{Im} g \subset \operatorname{Im} \varphi \xrightarrow{\varphi^{-1}} A$，则 $h \in \operatorname{Hom}_R(D, A)$ 且 $\bar{\varphi}(h) = \varphi h = g$. 从而 $\operatorname{Ker} \bar{\psi} \subset \operatorname{Im} \bar{\varphi}$.  
    $(\Leftarrow)$ 若对于每个 $R$-模 $D$，序列 $0 \to \operatorname{Hom}_R(D, A) \xrightarrow{\bar{\varphi}} \operatorname{Hom}_R(D, B) \xrightarrow{\bar{\psi}} \operatorname{Hom}_R(D, C)$ 是阿贝尔群的正合序列，那么：  
    (i) 取 $D = \operatorname{Ker} \varphi$，且 $i: D \to A$ 是包含映射。由 $\operatorname{Ker} \bar{\varphi} = 0$，$\bar{\varphi}(i) = \varphi i = 0$, 从而 $0 = D = \operatorname{Ker} \varphi$. 因此序列 $0 \to A \xrightarrow{\varphi} B$ 是正合的.  
    (ii) 取 $D = A$，因为 $\operatorname{Ker} \bar{\psi} = \operatorname{Im} \bar{\varphi}$，所以 $ 0 = \bar{\psi} \bar{\varphi}(1_A) = \psi \varphi = 0$. 因此 $\operatorname{Im} \varphi \subset \operatorname{Ker} \psi$.  
    (iii) 取 $D = \operatorname{Ker} \psi$，且 $j: D \to B$ 是包含映射。由于 $0 = \psi j = \bar{\psi}(j)$ 以及 $\operatorname{Ker} \bar{\psi} = \operatorname{Im} \bar{\varphi}$，所以存在 $f: D \to A$ 使得 $j = \bar{\varphi}(f) = \varphi f$. 所以对于任意 $x \in D$，有 $x = j(x) = \varphi f(x) \in \operatorname{Im} \varphi$，于是 $\operatorname{Ker} \psi = D \subset \operatorname{Im} \varphi$. 因此 $\operatorname{Ker} \psi = \operatorname{Im} \varphi$. 从而序列 $0 \to A \xrightarrow{\varphi} B \xrightarrow{\psi} C \to 0$ 是正合的.

!!! success "命题"
    设 $R$ 是环，则 $A \xrightarrow{\theta} B \xrightarrow{\zeta} C \to 0$ 是 $R$-模的正合序列等价于对于每个 $R$-模 $D$，序列 $0 \to \operatorname{Hom}_R(C, D) \xrightarrow{\bar{\zeta}} \operatorname{Hom}_R(B, D) \xrightarrow{\bar{\theta}} \operatorname{Hom}_R(A, D)$ 是阿贝尔群的正合序列.  

!!! success "命题"
    关于环 $R$ 上模的以下条件等价：  
    (i) $0 \to A \xrightarrow{\varphi} B \xrightarrow{\psi} C \to 0$ 是分裂的 $R$-模正合序列；   
    (ii) 对于每个 $R$-模 $D$，序列 $0 \to \operatorname{Hom}_R(D, A) \xrightarrow{\bar{\varphi}} \operatorname{Hom}_R(D, B) \xrightarrow{\bar{\psi}} \operatorname{Hom}_R(D, C) \to 0$ 是分裂的阿贝尔群正合序列；  
    (iii) 对于每个 $R$-模 $D$，序列 $0 \to \operatorname{Hom}_R(C, D) \xrightarrow{\bar{\psi}} \operatorname{Hom}_R(B, D) \xrightarrow{\bar{\varphi}} \operatorname{Hom}_R(A, D) \to 0$ 是分裂的阿贝尔群正合序列.

!!! note "定理"
    关于环 $R$ 上的模 $P$ 的以下条件是等价的：  
    (i) $P$ 是投射模；  
    (ii) 如果 $\psi: B \to C$ 是 $R$-模满同态，则 $\bar{\psi}: \operatorname{Hom}_R(P, B) \to \operatorname{Hom}_R(P, C)$ 是阿贝尔群的满同态；  
    (iii) 如果 $0 \to A \xrightarrow{\varphi} B \xrightarrow{\psi} C \to 0$ 是 $R$-模短正合序列，则 $0 \to \operatorname{Hom}_R(P, A) \xrightarrow{\bar{\varphi}} \operatorname{Hom}_R(P, B) \xrightarrow{\bar{\psi}} \operatorname{Hom}_R(P, C) \to 0$ 是阿贝尔群的短正合序列. 

!!! success "命题"
    关于环 $R$ 上的模 $J$ 的以下条件是等价的：  
    (i) $J$ 是内射模；  
    (ii) 如果 $\theta: A \to B$ 是 $R$-模单同态，则 $\bar{\theta}: \operatorname{Hom}_R(B, J) \to \operatorname{Hom}_R(A, J)$ 是阿贝尔群的满同态；  
    (iii) 如果 $0 \to A \xrightarrow{\theta} B \xrightarrow{\zeta} C \to 0$ 是 $R$-模短正合序列，则 $0 \to \operatorname{Hom}_R(C, J) \xrightarrow{\bar{\zeta}} \operatorname{Hom}_R(B, J) \xrightarrow{\bar{\theta}} \operatorname{Hom}_R(A, J) \to 0$ 是阿贝尔群的短正合序列.

!!! note "定理"
    设 $A$, $B$, $\{A_i \mid i \in I\}$, $\{B_j \mid j \in J\}$ 均是环 $R$上的模，则有如下的阿贝尔群同构：  
    (i) $\operatorname{Hom}_R(\sum_{i \in I} A_i, B) \cong \prod_{i \in I} \operatorname{Hom}_R(A_i, B)$；  
    (ii) $\operatorname{Hom}_R(A, \sum_{j \in J} B_j) \cong \prod_{j \in J} \operatorname{Hom}_R(A, B_j)$.

!!! info "定义"
    设 $R$ 和 $S$ 均是环，阿贝尔群 $A$ 被称作 **$R$-$S$ 双重模**(bimodule)，如果 $A$ 同时是左 $R$-模和右 $S$-模，且对于任意 $r \in R, s \in S, a \in A$，有 $r(as) = (ra)s$. 有时写作 $_R A_S$ 以表示 $A$ 是 $R$-$S$ 双重模. 类似地，用 $_R B$ 表示 $B$ 是左 $R$-模，用 $C_S$ 表示 $C$ 是右 $S$-模.  

!!! note "定理"
    设 $R$ 和 $S$ 是环，$_R A$, $_R B_S$, $_R C_S$ 和 $D_S$ 如上所述，则：  
    (i) $\operatorname{Hom}_R(A, B)$ 是右 $S$-模，其中 $S$ 的作用为 $(fs)(a) = (f(a))s, s \in S, a \in A, f \in \operatorname{Hom}_R(A, B)$；  
    (ii) 如果 $\varphi: A \to A'$ 是左 $R$-模同态，则诱导映射 $\bar{\varphi}: \operatorname{Hom}_R(A', B) \to \operatorname{Hom}_R(A, B)$ 是右 $S$-模同态；  
    (iii) $\operatorname{Hom}_R(C, D)$ 是左 $S$-模，其中 $R$ 的作用为 $(sg)(c) = (g(cs)), s \in S, c \in C, f \in \operatorname{Hom}_R(C, D)$；  
    (iv) 如果 $\psi: D \to D'$ 是左 $R$-模同态，则诱导映射 $\bar{\psi}: \operatorname{Hom}_R(C, D) \to \operatorname{Hom}_R(C, D')$ 是左 $R$-模同态.

!!! note "定理"
    若 $A$ 是含幺环 $R$ 上的幺作用左 $R$-模，则有左 $R$-模同构 $A \cong \operatorname{Hom}_R(R, A)$.  

??? note "证明"
    因为 $R$ 是 $R$-$R$ 双重模，由上给出 $\operatorname{Hom}_R(R, A)$ 的左 $R$-模结构，验证映射  

    \[
        \varphi: \operatorname{Hom}_R(R, A) \to A, \quad f \mapsto f(1_R)
    \]

    是 $R$-模同态. 定义映射 $\psi: A \to \operatorname{Hom}_R(R, A), a \mapsto f_a$，其中 $f_a(r) = ra$. 验证 $\psi$ 是良定义的，并且是 $R$-模同态，且 $\varphi \psi = 1_A, \psi \varphi = 1_{\operatorname{Hom}_R(R, A)}$，从而 $\varphi$ 是 $R$-模同构.

令 $A$ 是环 $R$ 上的左 $R$-模，因为 $R$ 是 $R$-$R$ 双重模，由上可知 $\operatorname{Hom}_R(A, R)$ 是右 $R$-模，称作 $A$ 的**对偶模**(dual module)，并表示为 $A^*$. $A^*$ 中的元素也被称作**线性泛函**(linear functional)。类似地，如果 $B$ 是右 $R$-模，则 $B$ 的对偶模 $B^*$ 是左 $R$-模 $\operatorname{Hom}_R(B, R)$.