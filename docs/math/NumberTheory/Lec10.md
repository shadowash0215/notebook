# Factorization in Quadratic Fields

!!! question
    Expect to construct some "ideal numbers" such that  
    (i) Ideal numbers behave like numbers;  
    (ii) Ideal numbers have unique factorization.

!!! note "Theorem"
    (Eisenstein) $f(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0 \in \mathbb{Z}[x]$.  
    If $f(x)$ has a root $\gamma \in \mathbb{Q}$, then $\gamma \in \mathbb{Z}$. And then we have $\mathbb{Z} = \{ \text{roots of monic integer polynomials in } \mathbb{Q} \}$

!!! info "Definition"
    $K = \mathbb{Q}(\sqrt{d})$, then $\mathcal{O}_K = \{ \text{roots of monic integer polynomials in } \mathbb{Q}(\sqrt{d})\}$

!!! example
    $\mathbb{Z}[\sqrt{d}] \subset \mathcal{O}_K$: 

!!! info "Definition"
    $f(x) = a_0 + a_1x + \cdots a_nx^n \in \mathbb{Z}[x]$. Define $\operatorname{\mathrm{cont}} f$ to be the g.c.d. of $a_0, a_1, \ldots, a_n$.

!!! success "Lemma"
    (Gauss) $f, g \in \mathbb{Z}[x]$, then $\operatorname{\mathrm{cont}} fg = \operatorname{\mathrm{cont}} f \cdot \operatorname{\mathrm{cont}} g$.

!!! note "Theorem"
    (Eisenstein's Criterion) $f(x) = a_0 + a_1x + \cdots + a_{n-1}x^{n-1} + x^n \in \mathbb{Z}[x]$. If $p$ is a prime in $\mathbb{Z}$, $p \mid a_j$ but $p^2 \not \mid a_0$. Then $f(x)$ is irreducible in $\mathbb{Z}[x]$.

!!! success "Collary"
    If $f(x) = a_0 + a_1x + \cdots + a_{n-1}x^{n-1} + x^n \in \mathbb{Z}[x]$ is reducible in $\mathbb{Q}[x]$, then it is reducible in $\mathbb{Z}[x]$.

!!! question
    What's $\mathcal{O}_K$($K = \mathbb{Q}(\sqrt{d})$)?
    
    \[
        \mathcal{O}_K = 
        \begin{cases}
            \mathbb{Z}[\sqrt{d}], d \not \equiv 1 \pmod 4 \\
            \mathbb{Z}[\frac{-1 + \sqrt{d}}{2}], d \equiv 1 \pmod 4 \\
        \end{cases}    
    \]
    
!!! info "Definition"
    $\alpha = x + y\sqrt{d}$, define the **conjugate** $\sigma(\alpha) = x - y\sqrt{d}$. $N(\alpha) = \alpha \cdot \sigma(\alpha) = x^2 - dy^2$, $Tr(\alpha) = \alpha + \sigma(\alpha) = 2x$.  
    Then it's obvious that $\alpha$ is the root of $x^2 - Tr(\alpha)x + N(\alpha) = 0$.

!!! success "Lemma"
    $\alpha \in \mathcal{O}_K$ iff $Tr(\alpha), N(\alpha) \in \mathbb{Z}$.

!!! info "Definition"
    An **ideal** in $\mathcal{O}_K$ is $(\alpha_1, \alpha_2, \ldots, \alpha_m) := \alpha_1 \mathcal{O}_K + \alpha_2 \mathcal{O}_K + \cdots + \alpha_m \mathcal{O}_K(\alpha_1, \alpha_2, \ldots, \alpha_m \in \mathcal{O}_K)$.  
    If $\mathfrak{a}, \mathfrak{b}$ are ideals, the $\mathfrak{a} + \mathfrak{b} = \{ \alpha + \beta \mid \alpha \in \mathfrak{a}, \beta \in \mathfrak{b} \}$, $\mathfrak{a}\mathfrak{b} = \{ \sum_{i = 1}^m \alpha_i\beta_i \mid \alpha_i \in \mathfrak{a}, \beta_i \in \mathfrak{b} \}$.  
    Operational Rule:   
    (i) $\mathfrak{a} + \mathfrak{b} = \mathfrak{b} + \mathfrak{a}$.  
    (ii) $\mathfrak{a} \cdot \mathfrak{b} = \mathfrak{b} \cdot \mathfrak{a}$.  
    (iii) $\mathfrak{a}(\mathfrak{b}\mathfrak{c}) = (\mathfrak{a}\mathfrak{b})\mathfrak{c}$.  
    (iv) $\mathfrak{a}(\mathfrak{b} + \mathfrak{c}) = \mathfrak{a}\mathfrak{b} + \mathfrak{a}\mathfrak{c}$, $(\mathfrak{b} + \mathfrak{c})\mathfrak{a} = \mathfrak{b}\mathfrak{a} + \mathfrak{c}\mathfrak{a}$.  
    (v) $\sigma(\mathfrak{a} + \mathfrak{b}) = \sigma(\mathfrak{a}) + \sigma(\mathfrak{b})$, $\sigma(\mathfrak{a}\mathfrak{b}) = \sigma(\mathfrak{a})\sigma(\mathfrak{b})$.

!!! success "Prop"
    Set $\mathfrak{a} = (a_1, a_2)$, then $\mathfrak{a} \cdot \sigma(\mathfrak{a}) = (N(a_1), N(a_2), Tr(a_1 \cdot \sigma(a_2)))$.  

??? success "Proof"
    Set d = gcd $(N(a_1), N(a_2), Tr(a_1 \cdot \sigma(a_2)))$. $\mathfrak{a} \cdot \sigma(\mathfrak{a}) = (a_1, a_2) \cdot (\sigma(a_1), \sigma(a_2)) = (N(a_1), N(a_2), a_1\sigma(a_2), a_2\sigma(a_1))$. We only need to prove that $a_1\sigma(a_2)$ and $a_2\sigma(a_1)$ are multiples of $d$, which means $\dfrac{a_1 \cdot \sigma(a_2)}{d}, \dfrac{a_2 \cdot \sigma(a_1)}{d} \in \mathcal{O}_k$.

!!! success "Prop"
    (i) $\mathfrak{a} = (a_1, \ldots, a_n)$, then $\mathfrak{a} \cdot \sigma(\mathfrak{a}) = (N(a_i), Tr(a_i \cdot \sigma(a_j)))$. So for any ideal $\mathfrak{a}$, there exists a unique positive integer $N$ such that $\mathfrak{a} \cdot \sigma(\mathfrak{a}) = (N)$. Then $N$ is defined to be the norm of $\mathfrak{a}$. $N(\mathfrak{a}) = N$.  
    (ii) $N(\mathfrak{a}) \cdot N(\mathfrak{b}) = N(\mathfrak{ab})$.  

!!! info "Definition"
    $\mathfrak{a} \mid \mathfrak{b}$ if $\mathfrak{b} \subset \mathfrak{a}$.  

!!! success "Lemma"
    (i) $(a) \mid \mathfrak{b} \rightarrow \mathfrak{b} = (a) \mathfrak{c}$ for some ideal $\mathfrak{c}$.  
    (ii) If $\mathfrak{a} \mid \mathfrak{b}$, then $\mathfrak{b} = \mathfrak{a} \cdot \mathfrak{c}$ for some ideal $\mathfrak{c}$.

!!! info "Definition"
    $\mathfrak{p}$ is prime in $\mathcal{O}_k$, if $\mathfrak{p} \neq (0)$, $\mathfrak{p} \neq (1)$ and $\mathfrak{p}$ cannot be written as $\mathfrak{p} = \mathfrak{a} \mathfrak{b}$, for $\mathfrak{a} \neq (0)$, $\mathfrak{b} \neq (0)$, $\mathfrak{a} \neq (1)$, $\mathfrak{b} \neq (1)$.

!!! success "Prop"
    (i) If $\mathfrak{p} \mid \mathfrak{ab}$, then $\mathfrak{p} \mid \mathfrak{a}$ or $\mathfrak{p} \mid \mathfrak{b}$.  
    (ii) Every ideal is a finite product of prime ideals.

!!! note "Theorem"
    (Dedekind) $k = \mathbb{Q}(\sqrt{d})$, $f(x) := \begin{cases} x^2-d , d \not \equiv 1 \pmod 4 \\ x^2 - x + \frac{1-d}{4}, d \equiv 1 \pmod 4 \end{cases}$. $f(x) = (x-\omega)(x - \bar{\omega}) \in \mathbb{C}[x]$. The way $(p)$ factorized in $\mathcal{O}_k$ depends the way $f(x)$ factorized in $\mathbb{F}_p[x]$.  
    (i) $f(x) \bmod p$ irreducible $\Rightarrow (p)$ is prime in $\mathcal{O}_k$.  
    (ii) $f(x) \equiv (x-c)(x-c') \pmod p$, $c \not \equiv c' \pmod p$, then $(p) = \mathfrak{p} \sigma(\mathfrak{p})$, $\mathfrak{p} = (p, \omega - c)$;     
    (iii) $f(x) \equiv (x-c)^2 \pmod p$, then $(p) = \mathfrak{p}^2$, $\mathfrak{p} = (p, \omega - c)$.