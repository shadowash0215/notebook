# Sum of Three Squares

!!! success "Prop"
    If $n$ is a sum of three squares, then $n$ is not of the form $4^k(8m + 7)$.

??? success "Proof"
    Set $n = x^2 + y^2 + z^2$, then proof by contradiction.  
    (i) $k = 0$, then $n = 8m + 7$ is an odd number. So $n \equiv 3 \pmod 4$, which means that $x, y, z$ are all odd. Then $x^2 \cdot y^2 \cdot z^2 \equiv 1 \pmod 8$, and $x^2 + y^2 + z^2 \equiv 3 \pmod 8$, which is a contradiction.  
    (ii) $k \geqslant 1$, then $n = x^2 + y^2 + z^2 \equiv \begin{cases} 0 \pmod 4 \text{ if } x, y, z \text{ are all even}, \\ 2 \pmod 4 \text{ if two of } x, y, z \text{ are odd}\end{cases}$

!!! info "Definition"
    Two quadratic forms are equivalent if there exists a change of variables that  
    
    \begin{gather}
        (x_1, x_2, \cdots, x_n) \leftrightarrow (y_1, y_2, \cdots, y_n) \\  
        Q \leftrightarrow Q' \\
    \end{gather}

In number theory, we need $J \in \operatorname{Gl}_n(\mathbb{Z})$ and $J^{-1} \in \operatorname{Gl}_n(\mathbb{Z})$ $(\operatorname{Gl}_n(\mathbb{Z}) = \{A = (a_{ij})_{n \times n} \mid a_{ij} \in \mathbb{Z}, \operatorname{det} A \neq 0\})$. So we can see that $\operatorname{det} J = \pm 1$.

Binary quadratic form
!!! note "Theorem"
    Every positive definite quadratic form of discriminant $d$(noted as $\operatorname{disc}(Q) = d$) has an equivalent form of the form $a_{11}x_1^2 + 2a_{12}x_1x_2 + a_{22}x_2^2$ with $2 \lvert a_{12} \rvert \leqslant a_{11} \leqslant 2 \sqrt{\frac{d}{3}}$.

??? note "Proof"
    $Q'(x_1', x_2') = (x_1', x_2') \cdot A' \cdot \begin{pmatrix} x_1' \\ x_2' \end{pmatrix}$.  
    (i) $a_{11} :=$ minimal positive integer represented by $Q'$, thus there exists $r_1, r_2$ such that $a_{11} = Q'(r_1, r_2)$, and $\gcd(r_1, r_2) = 1$. According to the Bézout's theorem, there exists $s_1, s_2$ such that $r_1s_2 - r_2s_1 = 1$.  
    (ii) Set $J_t = \begin{pmatrix} r_1 & s_1 + r_1t \\ r_2 & s_2 + r_2t \end{pmatrix}$, then $J_t^{T} A' J_t = \begin{pmatrix} a_{11} & a_{12} \\ a_{12} & a_{22} \end{pmatrix} = A$. $a_{12} = \tilde{a}_{12} + a_{11}t$, and $\tilde{a}_{12} = a_{11}'r_1s_1 + a_{12}'(r_1s_2 + r_2s_1) + a_{22}'r_2s_2$, $a_{22} = Q'(s_1 + r_1t, s_2 + r_2t) \geqslant a_{11}$.  
    (iii) Choose $t$ such that $\lvert a_{12} \rvert = \lvert \tilde{a}_{12} + a_{11}t \rvert \leqslant \dfrac{a_{11}}{2}$. $\operatorname{disc}(Q) = \operatorname{disc}(Q') = \operatorname{det} A' = \operatorname{det} A = a_{11}a_{22} - a_{12}^2 = d$, and $a_{11}^2 \leqslant a_{11}a_{22} = d + a_{12}^2 \leqslant d + \dfrac{a_{11}^2}{4}$, so $a_{11} \leqslant 2 \sqrt{\frac{d}{3}}$.

!!! success "Lemma"
    A tenary quadratic form $Q$ with its matrix $A_Q$, and its dicriminant $\operatorname{disc}(Q) = \operatorname{det} A_Q = d$. Define 
    
    \[
        A^* = \begin{pmatrix} a_{11}a_{22} - a_{12}^2 & a_{11}a_{23} - a_{12}a_{13} \\ a_{11}a_{23} - a_{12}a_{13} & a_{22}a_{33} - a_{13}^2 \end{pmatrix},
    \] 
    
    then $a_{11}Q(x_1, x_2, x_3) = (a_{11}x_1 + a_{12}x_2 + a_{13}x_3)^2 + Q_{A^*}(x_2, x_3)$, with $\operatorname{disc}(Q_{A^*}) = \operatorname{det} A^* = a_{11}d$. Moreover, $Q_{A^*}$ is positive definite if $Q$ is positive definite.

!!! success "Lemma"
    $Q'$ is a tenary quadratic form with its dicriminant $\operatorname{disc}(Q') = \operatorname{det} A_{Q'} = d$. Then it is equivalent to a form $Q$ with $2 \cdot \operatorname{max} \{\lvert a_{12} \rvert, \lvert a_{13} \rvert\} \leqslant a_{11} \leqslant \dfrac{4}{3} \sqrt[3]{d}$.

!!! info "Definition"
    (Jacobi Symbol) Recall Legendre symbol 

    \[
        \left( \dfrac{a}{p} \right) = \begin{cases} 1 \text{ if } a \text{ is a quadratic residue modulo } p, \\ -1 \text{ if } a \text{ is a quadratic non-residue modulo } p, \\ 0 \text{ if } p \mid a. \end{cases}
    \]

    Then Jacobi symbol is defined as $\left( \dfrac{a}{n} \right) = \prod_{i = 1}^k \left( \dfrac{a}{p_i} \right)^{e_i}$, where $n = p_1^{e_1} \cdots p_k^{e_k}$, and $p_i$ are distinct odd primes.

!!! success "Prop"
    (Quadratic Reciprocity)  
    (i) If $(m, n) = 1$ and $m, n$ are both positive odd integers, then 

    \[
        \left( \dfrac{m}{n} \right) \left( \dfrac{n}{m} \right) = (-1)^{\frac{m - 1}{2} \frac{n - 1}{2}}.
    \]

    (ii) $\left( \dfrac{2}{n} \right) = (-1)^{\frac{n^2 - 1}{8}}$.

!!! success "Lemma"
    Let $n > 1, d > 0 \in \mathbb{Z}$ such that $x^2 + d \equiv 0 \pmod {dn - 1}$ has a solution. Then $n$ is a sum of three squares.

??? success "Proof"
    $a_{12}^2 + d \equiv 0 \pmod {dn - 1} \Rightarrow a_{12}^2 + d = a_{11}(dn - 1) = a_{11}a_{22}$.  
    Construct matrix $A = \begin{pmatrix} a_{11} & a_{12} & 1 \\ a_{12} & a_{22} & 0 \\ 1 & 0 & n \end{pmatrix}$, then $\operatorname{det} A = 1$. So $Q_A$ is positive definite quadratic form with $\operatorname{disc} (Q_1) = 1$. Then $Q_A \sim x^2 + y^2 + z^2$, and $n = \begin{pmatrix} 0 \ 0 \ 1 \end{pmatrix} A \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \Rightarrow n = x^2 + y^2 + z^2$ for some $x, y, z$.

??? note "Proof of Theorem on Sum of Three Squares"
    (i) $n \equiv 2 \pmod 4$, so $(4n, n - 1) = 1$. Then there exists a prime $p \equiv n - 1 \pmod {4n}$. Set $p = 4n \cdot j + (n - 1) = (4j + 1) n - 1$, then $(4j + 1)n - 1$ is the form $dn - 1$, and $p \equiv 1 \pmod 4$. Calculate the Jacobi symbol $\left( \dfrac{-d}{p} \right) = \left( \dfrac{d}{p} \right) = \left( \dfrac{p}{d} \right) = \left( \dfrac{-1}{d} \right) = 1$. Then According to the lemma, $n$ can be written as the sum of three squares.  
    (ii) $n$ odd, $n \not \equiv 7 \pmod 8$. Set $c = 2 + (-1)^{\frac{n - 1}{2}}$, then $c \equiv -n \pmod 4$, and $\dfrac{cn - 1}{2} \equiv 1 \pmod 2$. Note that $(4n, \dfrac{cn - 1}{2}) = 1$