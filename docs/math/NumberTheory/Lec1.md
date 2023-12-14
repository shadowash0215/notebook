<style>
.center {
  width: auto;
  display: table;
  margin-left: auto;
  margin-right: auto;
}
</style>

# Euclidean Algorithm and Factorization

## In $\mathbb{Z}$

**divisibility**: $a$ divides $b$ if $b = ak$ for some $k \in \mathbb{Z}$ and denoted $a \mid b$. We also call $a$ to be a **divisor** or **factor** of $b$. 

**unit**: If $a \in \mathbb{Z}$ and $a^{-1} \in \mathbb{Z}$, then $a$ is called a unit in $\mathbb{Z}$.  
The group of units in $\mathbb{Z}$ is denoted by $\mathbb{Z}^{\times}$ and $\mathbb{Z}^{\times} = \{\pm 1\}$.

**reducible &  irreducible**: $p \in \mathbb{Z}$, if $p = ab, a, b \in \mathbb{Z}$ and $a, b \notin \mathbb{Z}^{\times}$, then $p$ is reducible. Otherwise $p$ is irreducible. 

**prime**: $p \in \mathbb{Z}$ is said to be a prime if $p \mid ab$ implies $p \mid a$ or $p \mid b$. 

!!! note "Proposition"
    $p$ is a prime in $\mathbb{Z} \Leftrightarrow p$ is irreducible. 

??? note "Proof"
    ($\Rightarrow$) Proof by contradiction. If $p$ is reducible, then $p = ab, a, b \in \mathbb{Z}$ and $a, b \notin \mathbb{Z}^{\times}$, this implies that $p \mid ab$ and $ab \mid p$. $p$ is a prime, so we have $p \mid a$ or $p \mid b$. Without loss of generality, assume $p \mid a$, and for $ab \mid p$ we have $a \mid p$. This implies that $p = ua, u \in \mathbb{Z}^{\times}$, so $b \in \mathbb{Z}^{\times}$.  
    ($\Leftarrow$) 

!!! success "Lemma"
    Every $n \in \mathbb{Z}$ has an irreducible divisor.

!!! note "Collary"
    Every $n \in \mathbb{Z}$ admits a factorization into product of irreducibles.

??? note "Proof"
   Both use induction.

!!! note "Proposition"
    (Division Theorem) Given $a, b \in \mathbb{Z}, b \neq 0$, there exists unique $q, r \in \mathbb{Z}$ such that $a = bq + r, 0 \leqslant r < b$. 

**g.c.d.**: Let $a, b \in \mathbb{Z}$, the greatest common divisor, denoted by $\gcd (a, b)$, is defined to be the largest integer $m$ that is a factor of both $a$ and $b$. That is, if $n$ is a common divisor of both $a$ and $b$, then $n \mid m$. 

!!! note "Theorem"
    (Euclidean Algorithm for $\mathbb{Z}$) Given $a, b \in \mathbb{Z}, b \neq 0$. Then there exists unique 

    $$
        g_1, g_2, \ldots 
    $$

    $$
        r_1, r_2, \ldots
    $$

    such that 

    <div class="center">

    | Equation | Condition |
    |:-----------:|:----------:|
    |$a = bg_1 + r_1$|$\lvert r_1 \rvert < \lvert b \rvert$|
    |$b = r_1g_2 + r_2$|$\lvert r_2 \rvert < \lvert r_1 \rvert$|
    |$r_1 = r_2g_3 + r_3$|$\lvert r_3 \rvert < \lvert r_2 \rvert$|
    |$\cdots$|$\cdots$|
    |$r_n = r_{n + 1}g_{n + 2} + r_{n + 2}$|$r_{n + 2} = 0$|

    </div>

    Then $r_{n + 1}$ is a g.c.d. of $a, b$.

!!! success "Lemma"
    g.c.d. of $a, b$ is unique on $\mathbb{Z}^{\times}$

??? note "Proof"
    If $d, d'$ are g.c.d. of $a, b$, then $d \mid d'$ and $d' \mid d$, this implies that $d = ud', u \in \mathbb{Z}^{\times}$.

??? note "Proof"
    (For Euclidean Algorithm) We only need to prove that $gcd(a, b) = gcd(b, r_1)$, then we can use induction.  
    If $d \mid b, d \mid r$, then $d \mid a = bg_1 + r$, so $d \mid gcd(a, b)$, which means $gcd(b, r_1) \mid gcd(a, b)$;  
    Otherwise, If $d' \mid a, d' \mid b$, then $d' \mid r_1 = a - bg_1$, so $d' \mid gcd(b, r_1)$, which means $gcd(a, b) \mid gcd(b, r_1)$. So $gcd(a, b) = gcd(b, r_1)$

!!! note "Collary"
    (Bezout Theorem) For $a, b \in \mathbb{Z}, a, b \neq 0$. There exists $x, y \in \mathbb{Z}$ such that 

    $$
        ax + by = \gcd (a, b)
    $$

!!! note "Theorem"
    (Fundamental Theorem of Arithmetic) (1) Every $n \in \mathbb{Z}$ admits a unique factorization  

    $$
        n = up_1^{l_1}\cdots p_r^{l_r}
    $$

    where $p_1, p_2, \ldots, p_r$ are positive distinct primes, $l_1, l_2, \ldots, l_r$ are positive integers, $u \in \mathbb{Z}^{\times}$. 

    (2) The factorization is unique i.e if 

    $$
        n = u'g_1^{s_1}\cdots g_l^{s_l}
    $$

    is another factorization,  
    then (i) $r = l, u = u'$;
         (ii) After a permutation, $g_j = p_j, l_j = s_j, j = 1, 2, \ldots, r$. 

!!! note "Theorem"
    There are infinitly many primes in $\mathbb{Z}$.

??? note "Proof"
    \[
        \zeta(s) = \sum_{n = 1}^{\infty} \dfrac{1}{n^s}, s \in \mathbb{C}.
    \] 

    (1) $s > 1, \zeta(s)$ converges absolutly;  
    (2) $\lim_{s \to 1^+} \zeta(s)$ diverges $(\zeta(1) = \infty)$;  
    (3) $\zeta(s) = \prod_{p \textrm{ prime}} (1 + \dfrac{1}{p^s} + \dfrac{1}{p^{2s}} + \cdots) = \prod_{p} (1 - p^{-s})^{-1}$, $p$ represents prime number. This comes from the unique factorization theorem.  
    So if there are finitely many primes, then $\zeta(1) = \prod_{p \textrm{ prime}} (1 - p^{-1})^{-1}$ converges, which is a contradiction. So there are infinitly many primes in $\mathbb{Z}$.


!!! note "Theorem"
    1. (Prime Number Theorem) $\pi(x)$ ~ $\dfrac{x}{\ln x}$. 

    2. (Dirichlet Theorem in Primes of Arithmetic Progression) Assume $a, b$ are coprime. Then there exists infinitely many primes of the form $an + b$.

## In $\mathbf{F}[x]$

**irreducible**: $p(x) \in \mathbf{F}[x]$ is said to be irreducible if it cannot be written as $p(x) = p_1(x)p_2(x)$ with $\operatorname{deg} p_1(x), \operatorname{deg} p_2(x) < \operatorname{deg} p(x)$.

**divisibility**: $p(x)$ divides $a(x)$ over $\mathbf{F}$ if $a(x) = p(x)b(x)$ for some $b(x) \in \mathbf{F}[x]$ and denoted $p(x) \mid a(x)$. We also call $p(x)$ to be a **divisor** or **factor** of $a(x)$.

**prime**: $p(x)$ is prime $p(x) \mid a(x)b(x) \Rightarrow p(x) \mid a(x)$ or $p(x) \mid b(x)$.

**g.c.d.**: Let $a(x), b(x) \in \mathbf{F}[x]$, the greatest common divisor, denoted by $\gcd (a(x), b(x))$, is defined to be the largest polynomial $d(x)$ that is a factor of both $a(x)$ and $b(x)$. That is, if $n(x)$ is a common divisor of both $a(x)$ and $b(x)$, then $n(x) \mid d(x)$.

!!! note "Theorem"
    (i) (division algorithm) Given $a(x), b(x) \in \mathbf{F}[x], b(x) \neq 0$, there exists unique $q(x), r(x) \in \mathbf{F}[x]$ such that $a(x) = b(x)q(x) + r(x), \operatorname{deg} r(x) < \operatorname{deg} b(x)$.  
    (ii) (Euclidean Algorithm) Given $a(x), b(x) \in \mathbf{F}[x], b(x) \neq 0$. Then there exists unique $r_1(x), r_2(x), \ldots r_n(x) \in \mathbf{F}[x]$ such that

    \begin{gather}
        a(x) = b(x)q_1(x) + r_1(x), \operatorname{deg} r_1(x) < \operatorname{deg} b(x) \\
        b(x) = r_1(x)q_2(x) + r_2(x), \operatorname{deg} r_2(x) < \operatorname{deg} r_1(x) \\
        r_1(x) = r_2(x)q_3(x) + r_3(x), \operatorname{deg} r_3(x) < \operatorname{deg} r_2(x) \\
        \cdots \\
        r_{n - 2}(x) = r_{n - 1}(x)q_n(x) + r_n(x), \operatorname{deg} r_n(x) < \operatorname{deg} r_{n - 1}(x) \\
        r_{n - 1}(x) = r_n(x)q_{n + 1}(x) + r_{n + 1}(x), r_{n + 1}(x) = 0
    \end{gather}

    Moreover, $r_n(x)$ is a g.c.d. of $a(x), b(x)$.

!!! success "Lemma"
    Irreducible polynomial is prime.

!!! note "Collary"
    (Bezout Theorem) If $d(x)$ is a g.c.d. of $a(x), b(x)$, then there exists $p(x), q(x) \in \mathbf{F}[x]$ such that 

    $$
        d(x) = a(x)p(x) + b(x)q(x).
    $$

!!! note "Theorem"
    (Unique Factorization Theorem) Every $p(x) \in \mathbf{F}[x]$ can be uniquely factorized as 

    \[
        p(x) = u \cdot p_1^{l_1}(x) \cdot p_2^{l_2}(x) \cdots p_r^{l_r}(x),
    \]

    where $u \in \mathbf{F}^{\times}, p_1(x), p_2(x), \ldots, p_r(x) \in \mathbf{F}[x]$ are irreducible polynomials, $l_1, l_2, \ldots, l_r$ are positive integers.  
    Here, uniqueness means that if 

    \[
        p(x) = u' \cdot g_1^{s_1}(x) \cdot g_2^{s_2}(x) \cdots g_m^{s_m}(x),
    \]

    then $m = r$, and there exists a relabeling of $g_1(x), g_2(x), \ldots, g_r(x)$ such that $g_i(x) = c_ip_i(x)$, $c_i \in \mathbf{F}^{\times}$, $i = 1, 2, \ldots, r$, and $l_i = s_i$, $i = 1, 2, \ldots, r$. 

## In $\mathbb{Z}[\sqrt{-1}]$

!!! example
    Let $p$ be an odd prime. For which $p$, the equation $x^2 + y^2 = p$ has an integral solution?  
    Colusion: $x^2 + y^2 = p$ has a solution iff $p = 2$ or $p \equiv 1 \pmod 4$.

**Norm**: For $\alpha \in \mathbf{Z}[\sqrt{-1}]$ defines $N(\alpha) = \lvert \alpha \rvert^2 = \alpha ·\bar{\alpha}$

**divisibility**: $\alpha$ divides $\beta$ if $\beta = \alpha \gamma$ for some $\gamma \in \mathbb{Z}[\sqrt{-1}]$ and denoted $\alpha \mid \beta$. We also call $a$ to be a **divisor** or **factor** of $b$. 

**unit**: If $u \in \mathbb{Z}[\sqrt{-1}]$ and $u^{-1} \in \mathbb{Z}[\sqrt{-1}]$, then $a$ is called a unit in $\mathbb{Z}[\sqrt{-1}]$.  
The group of units in $\mathbb{Z}[\sqrt{-1}]$ is denoted by $\mathbb{Z}[\sqrt{-1}]^{\times}$.

**reducible &  irreducible**: $p \in \mathbb{Z}[\sqrt{-1}]$, if $p = ab, a, b \in \mathbb{Z}[\sqrt{-1}]$ and $a, b \notin \mathbb{Z}[\sqrt{-1}]^{\times}$, then $p$ is reducible. Otherwise $p$ is irreducible. 

!!! success "Lemma"
    Every element can be written as a product of irreducible elements.

!!! success "Lemma"
    $\mathbb{Z}[\sqrt{-1}]^{\times} = \{\pm 1, \pm i\}$.

!!! example
    3 is irreducilbe in $\mathbf{Z}[\sqrt{-1}]$.

??? note "Proof"
    $3 = \alpha · \beta \in \mathbf{Z}[\sqrt{-1}] \Rightarrow N(3) = 3 · \bar{3} = (\alpha \beta )(\bar{\alpha \beta}) = N(\alpha)N(\beta) \Rightarrow N(\alpha)N(\beta) = 9$.

!!! success "Lemma"
    If $p$ is a prime, then $p$ is irreducible.

!!! note "Theorem"
    $\alpha, \beta \in \mathbf{Z}[\sqrt{-1}], \beta \neq 0$. Then there exists $\gamma, \rho \in \mathbf{Z}[\sqrt{-1}]$ such that

    $$
        \alpha = \beta · \gamma + \rho, 0 \leqslant N(\rho) \leqslant \dfrac{1}{2}N(\beta).
    $$

??? note "Proof"
    $$
    \dfrac{\alpha}{\beta} = \dfrac{\alpha · \bar{\beta}}{\beta · \bar{\beta}} = \dfrac{\alpha · \bar{\beta}}{N(\beta)}
    $$

    Let $\alpha \cdot \bar{\beta} = m+n\sqrt{-1}, m, n \in \mathbb{Z}.$Notice that $N(\beta)$ is a positive integer such that 

    $$
        m = N(\beta) · m_1 + r, m_1, r \in \mathbf{Z}, \lvert r \rvert \leqslant \dfrac{1}{2}N(\beta).
    $$

    $$
        n = N(\beta) · n_1 + s, n_1, s \in \mathbf{Z}, \lvert s \rvert \leqslant \dfrac{1}{2}N(\beta).
    $$

    So

    $$
        \dfrac{\alpha}{\beta} = \dfrac{m + n\sqrt{-1}}{N(\beta)} = m_1 + n_1\sqrt{-1} + \dfrac{r + s\sqrt{-1}}{N(\beta)}
    $$

    Define $\gamma = m_1 + n_1\sqrt{-1}, \dfrac{\rho}{\beta} = \dfrac{r + s\sqrt{-1}}{N(\beta)}$. Then

    $$
        \dfrac{\rho}{\beta} = \dfrac{r + s\sqrt{-1}}{N(\beta)} = \dfrac{r + s\sqrt{-1}}{\beta · \bar{\beta}} \Rightarrow \bar{\beta} · \rho = r + s\sqrt{-1} \Rightarrow N(\beta)N(\rho) = r^2 + s^2 \leqslant \dfrac{1}{2}N(\beta)^2.
    $$

    So 

    $$
        N(\rho) \leqslant \dfrac{1}{2}N(\beta).
    $$

!!! note "Theorem"
    (Euclidean Algorithm) $\alpha, \beta \in \mathbf{Z}[\sqrt{-1}], \beta \neq 0$, then

    <div class="center">

    | Equation | Condition |
    |:-----------:|:----------:|
    |$\alpha = \beta \gamma_1 + \delta_1$|$N(\delta_1) < N(\beta)$|
    |$\beta = \delta_1 \gamma_2 + \delta_2$|$N(\delta_2) < N(\delta_1)$|
    |$\delta_1 = \delta_2 \gamma_3 + \delta_3$|$N(\delta_3) < N(\delta_2)$|
    |$\cdots$|$\cdots$|
    |$\delta_n = \delta_{n + 1} \gamma_{n + 2} + \delta_{n + 2}$|$\delta_{n + 2} = 0$|

    </div>

    So $\delta_{n + 1}$ is a g.c.d. of $\alpha, \beta$.

**Coprime**: If g.c.d. of $\alpha, \beta$ is a unit then we say $\alpha, \beta$ are coprime.

!!! note "Collary"
    (Bezout) If d is a g.c.d. of $\alpha, \beta$, then there exists $u, v \in \mathbf{Z}[\sqrt{-1}]$ such that 

    $$
        u\alpha + v\beta = d.
    $$

    In particular, if $\alpha, \beta$ are coprime. Then $\exists u, v$ such that

    $$
        u\alpha + v\beta = 1.
    $$

!!! note "Theorem"
    $p$ is prime $\Leftrightarrow$ $p$ is irreducible.

??? note "Proof"
    ($\Rightarrow$) Proof by contradiction. If $p$ is reducible, then $p = \alpha \beta, \alpha, \beta \in \mathbb{Z}[\sqrt{-1}]$ and $\alpha, \beta \notin \mathbb{Z}[\sqrt{-1}]^{\times}$, this implies that $p \mid \alpha \beta$ and $\alpha \beta \mid p$. $p$ is a prime, so we have $p \mid \alpha$ or $p \mid \beta$, then we have $N(p) \mid N(\alpha)$ or $N(p) \mid N(\beta)$. For $\alpha \beta = p$ we have $N(\alpha)N(\beta) = N(p)$. This implies that $N(\alpha) \mid N(p)$ and $N(\beta) \mid N(p)$, so we have $N(\alpha) = N(p)$ or $N(\beta) = N(p)$, which means $\alpha$ or $\beta$ is a unit.  
    ($\Leftarrow$) Assume that $p$ is irreducible. Let $\alpha, \beta \in \mathbb{Z}[\sqrt{-1}]$ with $p \mid \alpha \beta$. We need to prove that $p \mid \alpha$ or $p \mid \beta$. Without loss of generality, we set $p \not \mid \alpha$. Since any $\gcd(p, \alpha) \mid p$, the irreducibility of $p$ implies that $\gcd(p, \alpha) \in \mathbb{Z}[\sqrt{-1}]^{\times}$. According to Bezout theorem, there exists $x, y \in \mathbb{Z}[\sqrt{-1}]$ such that $px+\alpha y = 1$. Hence $\beta = \beta(px+\alpha y) = p \cdot \beta x + \alpha \beta \cdot y$ is a multiple of $p$.