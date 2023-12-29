# Quadratic Reciprocity Law

!!! question
    Given an odd prime $p \in \mathbb{Z}$ and an integer $a$, is there an efficient way to determine if the equation $x^2 \equiv a \pmod p$ has a solution?

!!! info "Definition"
    (Legendre Symbol)  

    \[ 
        \left(\dfrac{a}{p}\right) = \begin{cases} 0 \enspace \textrm{if} \enspace a \equiv 0 \pmod p, \\ 1 \enspace \textrm{if} \enspace p \not \mid a, x^2 \equiv a \pmod p \enspace \textrm{has a solution}, \\ -1 \enspace \textrm{if} \enspace p \not \mid a, x^2 \equiv a \pmod p \enspace \textrm{has no solution}. \end{cases}
    \]

!!! success "Lemma"
    (i) If $a \equiv b \pmod p$, then $\left(\dfrac{a}{p}\right) = \left(\dfrac{b}{p}\right)$.  

    (ii) $\left(\dfrac{1}{p}\right) = 1$.
  
    (iii) (Euler)  

    \[
        \left(\dfrac{a}{p}\right) \equiv a^{\frac{p-1}{2}} \pmod p.
    \]

    (iv) $\left(\dfrac{a}{p}\right)\left(\dfrac{a}{p}\right) = \left(\dfrac{ab}{p}\right)$

    (v) Set $a = -1$, then $\left(\dfrac{-1}{p}\right) = (-1)^{\frac{p-1}{2}}$

!!! note "Propsotion"

    \[
        \left(\dfrac{2}{p}\right) \equiv (-1)^{\frac{p^2-1}{8}} \pmod p.
    \]

??? note "Proof"
    The idea is that $2$ is "almost" a square in $\mathbb{Z}[\sqrt{-1}]$.  
    By previous lemma, $\left(\dfrac{2}{p}\right) \equiv 2^{\frac{p-1}{2}} \pmod p$. Then we have 

    \[
        \left(\dfrac{2}{p}\right) \equiv (-(\sqrt{-1}) \cdot (1+\sqrt{-1})^2)^{\frac{p-1}{2}} \equiv (1+\sqrt{-1})^{p-1} \cdot (\sqrt{-1})^{-\frac{p-1}{2}} \pmod p.
    \] 

    So we have 

    \[
        (1+\sqrt{-1}) \left(\dfrac{2}{p}\right) \equiv (1+\sqrt{-1})^p \cdot (\sqrt{-1})^{-\frac{p-1}{2}} \equiv (1+ (\sqrt{-1})^p) \cdot (\sqrt{-1})^{-\frac{p-1}{2}} \pmod p.
    \]

    Note that we use $p \mid C_p^{k}, k \neq 0, k \neq p$ when we simplified $(1+\sqrt{-1})^p \equiv 1+(\sqrt{-1})^p \pmod p$.

    Then cheak the identity for the following cases: $p = 8k+1, 8k+3, 8k+5, 8k+7$.

    When $p \equiv 1 \mod 8$ or $p \equiv 7 \mod 8$, $\dfrac{p^2-1}{8}$ is even, and $\left(\dfrac{2}{p}\right) \equiv 1 \pmod p$.  
    When $p \equiv 3 \mod 8$ or $p \equiv 5 \mod 8$, $\dfrac{p^2-1}{8}$ is odd, and $\left(\dfrac{2}{p}\right) \equiv -1 \pmod p$.  
    So $\left(\dfrac{2}{p}\right) \equiv (-1)^{\frac{p^2-1}{8}} \pmod p$.

!!! note "Theorem"
    (Gauss)

    \[
        \left(\dfrac{p}{q}\right) \left(\dfrac{q}{p}\right) = (-1)^{\frac{p-1}{2} \cdot \frac{q-1}{2}}.
    \]

!!! note "Theorem"
    (Hensel's lemma) Assume $p$ is an odd prime, $f(x) \in \mathbb{Z}[x]$. If $f(x) \equiv 0 \pmod p$ has a solution $x_1$, and $f'(x_1) \not \equiv 0 \pmod p$. Then $f(x) \equiv 0 \pmod {p^n}$ has a solution. More concretely, , the solution is given inductively by  

    \[
        x_n \equiv x_{n-1}-f(x_{n-1}) \cdot f'(x_1)^{-1} \pmod {p^n}.
    \]

??? note "Proof"
    Prove by induction. Suppose

    \[
        \begin{cases} x_n \equiv x_{n-1}-f(x_{n-1}) \cdot f'(x_1)^{-1} \pmod {p^n} \ \textrm{is a solution,} \\ f'(x_n) \equiv f'(x_1) \pmod p .\end{cases}
    \]

    We have $f(x_{n+1}) \equiv 0 \pmod {p^{n+1}} \equiv 0 \pmod {p^n}$ and $f(x_n) \equiv 0 \pmod {p^n}$. Expect $x_{n+1} = x_n + p^ny_n$. Using Taylor, we have 
    
    \[
        f(x_{n+1}) = f(x_n + p^ny_n) = f(x_n) + f'(x_n) \cdot p^ny_n + \alpha \cdot p^{2n}y_n^2 \equiv f(x_n)+f'(x_n) \cdot p^ny_n \pmod {p^{n+1}}.
    \]

    Then $\dfrac{f(x_n)}{p^n} + f'(x_n) \cdot y_n \pmod p$. Obviously $y_n \equiv -\dfrac{f(x_n)}{p^n \cdot f'(x_1)} \pmod p$.  
    So $x_{n+1} \equiv x_n-f(x_n) \cdot f'(x_1)^{-1} \pmod p$.  

    And $f'(x_{n+1}) = f'(x_n+p^ny_n) = f'(x_n)+\beta \cdot p^ny_n \equiv f'(x_1) \pmod p$.

!!! success "Collary"
    Assume $(a, p) = 1$, p is an odd prime. $x^2-a \equiv 0 \pmod p$ has a solution iff $x^2-a \equiv 0 \pmod {p^n}$ has a solution.

??? success "Proof"
    (i) $x_0^2-a \equiv 0 \pmod {p^n}$. Then obviously $x_0^2-a \equiv 0 \pmod p$.  
    (ii) If $x_0^2-a \equiv 0 \pmod p$, then $(x_0, p) = 1$. Then for $f(x) = x^2-a, f'(x_0) = 2x_0 \not \equiv 0 \pmod p$. By Hensel, $x^2-a \equiv 0 \pmod {p^n}$.

!!! note "Theorem"
    (Classical Chinese Remainder Theorem) Assume $(m, n) = 1$. Then for any $a, b$, 

    \[
        \begin{cases} x \equiv a \pmod m, \\ x \equiv b \pmod n \end{cases}
    \]

    has s solution.

!!! success "Collary"
    Assume $(m, n) = 1, (a, mn) = 1$. $x^2-a \equiv 0 \pmod {mn}$ has a solution iff 

    \[
        \begin{cases} x^2-a \equiv \pmod m \\ x^2-a \equiv \pmod n \end{cases}
    \]

    has a solution.

??? success "Proof"
    (i) It's obvious that $x^2-a \equiv 0 \pmod {mn} \Rightarrow \begin{cases} x^2-a \equiv \pmod m \\ x^2-a \equiv \pmod n \end{cases}$.  
    (ii)

!!! note "Theorem"
    (Special case for $p = 2$) (i) $x^2-a \equiv 0 \pmod 2$ always has a solution.  
    (ii) $x^2-a \equiv 0 \pmod 4$ has a solution implies that $a \equiv 0 \pmod 4$ or $a \equiv 1 \pmod 4$.  
    (iii) Lemma: Assume $(a, 2) = 1$($a$ is odd), $n \geqslant 3$. $x^2-a \equiv 0 \pmod {2^n}$ has a soltuion iff $a \equiv 1 \pmod 8$.

??? note "Proof"
    (iii) ($\Rightarrow$) $x_0^2-a \equiv 0 \pmod {2^n} \equiv 0 \pmod 8$, which means $a \equiv x_0^2 \pmod 8$. And $a$ is odd, so $a \equiv 1 \pmod 8$.  
    ($\Leftarrow$) Assume $a \equiv 1 \pmod 8$. If $n = 3$, then $x^2 \equiv a \pmod 8 \equiv 1 \pmod 8$, which implies that there is a solution $x_0 = 1$.  
    Prove by induction: $x^2 \equiv a \pmod {2^n}$ and $x^2 \equiv a \pmod {2^{n+1}}$. So $x_{n+1}^2-x_n^2 \equiv 0 \pmod {2^n}$, which means $(x_{n+1}-x_n)(x_{n+1}+x_n) \equiv 0 \pmod {2^n}$. Note that $(x_{n+1}-x_n)$ and $(x_{n+1}+x_n)$ has the same parity, so we only expect that $x_{n+1} = x_n+2^{n-1}y_n$.  
    Then $x_{n+1}^2 \equiv x_n^2 + 2^n \cdot x_ny_n + 2^{2n-2}y_n^2 \pmod {2^{n+1}}$. Note $n \geqslant 3$, so we have $2n-2 \geqslant n+1$. So $x_{n+1}^2 \equiv x_n^2 + 2^n \cdot x_ny_n \pmod {2^{n+1}}$.  
    We still have $x_n^2 \equiv a \pmod {2^n}$. Set $a = x_n^2 + 2^ny_n$. Then $x_{n+1}^2 \equiv a-2^ny_n+2^nx_ny_n \pmod {2^{n+1}} \equiv a-2^ny_n(x_n-1) \pmod {2^{n+1}}$. We know $x_n$ is odd, so $x_n-1$ is even. Then $x_{n+1}^2 \equiv a \pmod {2^{n+1}}$.