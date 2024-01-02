# Some Diophantine Equations

## 1. $x^2 + y^2 = z^2$ 

!!! note "Theorem"
    Assume $(x, y, z)$ coprime, $x$ odd, $y$ even, $x, y, z >0$, and $(x, y, z)$ is a solution of eq1. Then there exists $m, n \in \mathbb{Z}, m > n > 0$ such that  

    \[
        x = m^2-n^2, y = 2mn, z = m^2+n^2.
    \]
    ??? note "Proof"
        $z^2 = x^2+y^2 = (x+y\sqrt{-1})(x-y\sqrt{-1})$.  
        (i) If $d \mid (x+y\sqrt{-1}), d \mid (x-y\sqrt{-1})$, then $d^2 \mid (x+y\sqrt{-1})(x-y\sqrt{-1}) = z^2$. So $N(d^2) \mid N(z^2)$. $N(d)$ is odd and $N(d) \neq 2$.  
        (ii) The factoriation of 2. $2 = -\sqrt{-1}(1+\sqrt{-1})^2$ and $N(1+\sqrt{-1}) = 2$. So $(d, z) = 1$.  
        (iii) $d \mid (x+y\sqrt{-1}), d \mid (x-y\sqrt{-1}) \rightarrow d \mid 2x, d \mid 2y$. $d$ and 2 are coprime, so $d \mid x, d \mid y$. But $x, y$ are coprime, so $d$ is a unit.  
        (iv) Suppose $z$ can be factorized like this: $z = p_1 \cdots p_r$(allow repeated), then $z^2 = p_1^2 \cdots p_r ^2$. Therefore exists one permutation such that $x+y\sqrt{-1} = p_1^2 \cdots p_t^2, x-y\sqrt{-1} = p_{t+1}^2 \cdots p_r^2$. Let $x+y\sqrt{-1} = (m+n\sqrt{-1})^2 \cdot u, x-y\sqrt{-1} = (m-n\sqrt{-1})^2 \cdot u^{-1}, u \in \mathbb{Z}[\sqrt{-1}]^{\times}$. We need to discuss the choice of $u$.  
        (v) If $u = 1$, then $x = m^2-n^2, y = 2mn, z = m^2+n^2$. If $u = -1$, then $x = n^2-m^2, y = -2mn, z = m^2+n^2$, but we set $m > n > 0$. Contradiction. If $u = \sqrt{-1}$, then $x = -2mn, y = m^2-n^2$

## 2. $a^2 + b^2 = c^3$

!!! note "Theorem"
    Integer solution of $a^2+b^2=c^3$ with $(a, b) = 1$ are given by 

    \[
        a = m^3 - 3mn^2, b = 3m^2n - n^3, c = m^2 + n^2.
    \]

    where $(m, n) = 1$ and $m \not \equiv n \pmod 2$.

## 3. $y^2 = x^3-1$

??? note "Solution"
    Factorize this equation on $\mathbb{Z}[\sqrt{-1}]$.  
    $x^3 = y^2 + 1 = (y+\sqrt{-1})(y-\sqrt{-1})$.   

## 4. $y^2 = x^3-4$

## 5. $x^2 + y^2 = p$

!!! success "Lemma"
    (i) If $p \equiv 1 \pmod 4$, then $x^2 \equiv -1 \pmod p$ has a solution.  
    (ii) $x^2 \equiv -1 \pmod p$ has a solution $\Rightarrow$ $p$ is not a prime in $\mathbb{Z}[\sqrt{-1}]$.
    ??? success "Proof"
        (i) $a^{p - 1} - 1 = (a^{\frac{p - 1}{2}} - 1)(a^{\frac{p - 1}{2}} + 1)$.  
        $\bmod p$ on both side, we have $a^{p - 1} - 1 = (a^{\frac{p - 1}{2}} - 1)(a^{\frac{p - 1}{2}} + 1) \pmod p$.  
        According to Fermat's little theorem, $a^{p - 1} - 1 \equiv 0 \pmod p$ has exactly $p - 1$ solutions.  
        So $a^{\frac{p - 1}{2}} - 1 \equiv 0 \pmod p$ has exactly $\frac{p - 1}{2}$ solutions, so does $a^{\frac{p - 1}{2}} + 1 \equiv 0 \pmod p$. And then $(a^{\frac{p - 1}{4}})^2 \equiv -1 \pmod p$. So $x^2 \equiv -1 \pmod p$ has a solution if $p \equiv 1 \pmod 4$. 

        (ii) $p \mid x^2 + 1 = (x + \sqrt{-1})(x - \sqrt{-1})$. If $p$ is a prime in $\mathbb{Z}[\sqrt{-1}]$, then $p \mid (x + \sqrt{-1})$ or $p \mid (x - \sqrt{-1})$, which means $p(a + b\sqrt{-1}) = x \pm \sqrt{-1}$, then $pb = \pm 1$. But $p$ is a prime in $\mathbb{Z}. Contradiction! 

!!! example
    !!! question  
        For which $p > 3$, $x^2 + x + 1 \equiv 0 \pmod p$ has a solution?
    $x^2 + x + 1 \equiv 0 \pmod p$ has a solution $\Leftrightarrow$ there exists $a, a^3 - 1 \equiv 0 \pmod p$ , and according to Fermat's little theorem, $a^{p - 1} - 1 \equiv 0 \pmod p$.  
    If $3 \not \mid p - 1$, then according to Bezout's theorem, there exists $u, v \in \mathbb{Z}$ such that $3u + (p - 1)v = 1$. So $a^1 = a^{3u + (p - 1)v} = a^{3u} \cdot a^{(p - 1)v} \equiv a^{3u} \equiv 1 \pmod p$. Contradiction!  
    If $3 \mid p - 1$:  
    !!! note "Theorem"
        If $p$ is a prime, then $(\mathbb{Z}/p\mathbb{Z})^{\times}$ has a geneartor $g$. (The proof is in Lec4)
    Then is obvious that $a = g^{\frac{p - 1}{3}}$ is a solution of $x^3 - 1 \equiv 0 \pmod p$.  
    So $x^2 + x + 1 \equiv 0 \pmod p$ has a solution iff $3 \mid p - 1$. 

    Actually, this example is related to the cyclotomic polynomial $\Phi_p(x)$. $\Phi_3(x) = x^2 + x + 1$ has a root in $\mathbb{Z}/p\mathbb{Z}$ iff $3 \mid p - 1$. Then we can consider that $\Phi_p(x)$ has a root in $\mathbb{Z}/q\mathbb{Z}$ iff $p \mid q - 1$. And $\Phi_4(x) = x^2 + 1$ has a root in $\mathbb{Z}/p\mathbb{Z}$ iff $4 \mid p - 1$, which means $p \equiv 1 \pmod 4$, is the lemma we proved before.

!!! note "Theorem"
    Let $p$ be an odd prime.  
    (i) $x^2 + y^2 = p$ has a solution iff $p \equiv 1 \pmod 4$.  
    (ii) Up to sign and order, the solution, if exists, must be unique.
    ??? note "Proof"
        (i) ($\Rightarrow$) Because $p$ is an odd prime, so $x, y$ are one odd and one even. Without loss of generality, we assume $x$ is odd and $y$ is even, then $x^2 \equiv 1 \pmod 4, y^2 \equiv 0 \pmod 4$. So $x^2 + y^2 = p \equiv 1 \pmod 4$.  
        ($\Leftarrow$) If $p \equiv 1 \pmod 4$, then $x^2 \equiv -1 \pmod p$ has a solution. So $p$ is not a prime in $\mathbb{Z}[\sqrt{-1}]$. Thus, $p$ is reducible in $\mathbb{Z}[\sqrt{-1}]$. Suppose $p = \alpha \beta$, $\alpha, \beta \not \in \mathbb{Z}[\sqrt{-1}]^{\times}$. Then $p^2 = N(p) = N(\alpha)N(\beta)$. So $N(\alpha) = N(\beta) = p$. Thus we know $\beta = \overline{\alpha}$, so suppose $\alpha = x + y\sqrt{-1}$, then $\beta = x - y\sqrt{-1}$. So $x^2 + y^2 = p$.