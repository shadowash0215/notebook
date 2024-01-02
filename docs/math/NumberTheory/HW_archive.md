<style>
.center {
  width: auto;
  display: table;
  margin-left: auto;
  margin-right: auto;
}
</style>

# Homework Archive

## Week 1

!!! question
    (1) Set $a = 20, b = 12$.  
        (a) Use **Euclidean Algorithm** to show that $\gcd(a, b) = 4$.  
        (b) Find one pair $(x, y) \in \mathbb{Z} \times \mathbb{Z}$ such that $ax+by = 4$.

    (2) Set $a(x) = x^3-1, b(x) = x^2-1$, both regarded as polynomials over $\mathbb{Q}$.  
        (a) Use **Euclidean Algorithm** to show that $\gcd(a(x), b(x)) = x-1$.  
        (b) Find one pair $(u(x), v(x)) \in \mathbb{Q}[x] \times \mathbb{Q}[x]$ such that $a(x)u(x)+b(x)v(x) = x-1$.

    (3) Consider $q := 2^2 \cdot 3 \cdot 5 \cdot \cdots \cdot p-1$, where $p$ is an odd positive prime in $\mathbb{Z}$.  
        (a) Show that there exists a prime $p' > p$ of the form $4n+3$ such that $p' \mid q$.  
        (b) Use (a) to prove that there are infinitely many primes in $\mathbb{Z}$ of the form $4n+3$.  

    (4) Consider $q := 2 \cdot 3 \cdot 5 \cdot \cdots \cdot p-1$, where $p$ is an odd positive prime in $\mathbb{Z}$.  
        (a) Show that there exists a prime $p' > p$ of the form $6n+5$ such that $p' \mid q$.  
        (b) Use (a) to prove that there are infinitely many primes in $\mathbb{Z}$ of the form $6n+5$.

    (5) Consider the Fermat's numbers $F_n := 2^{2^n}+1 \enspace (n = 1, 2, \cdots)$.  
        (a) Let $m > k \geqslant 1$ be two positive integers. Prove that $F_k \mid F_m-2$.  
        (b) Prove that no two Fermat's numbers have a common divisor greater than 1. (Hint: Use (a)).  
        (c) Use (b) to prove the existence of infinitely many primes.

??? note "Answer"
    (1) (a) 

    \begin{gather}
        20 = 1 \cdot 12 + 8 \\
        12 = 1 \cdot 8 + 4 \\
        8 = 2 \cdot 4 + 0 \\
    \end{gather}

    So $\gcd(a, b) = 4$.  
    (b) 

    \begin{gather}
        4 = 12+(-1) \cdot 8 = b+(-1)\cdot 8 \\
        8 = 20+(-1) \cdot 12 = a+(-1)\cdot b
    \end{gather}

    So $4 = \gcd(a, b) = (-1)\cdot a+2 \cdot b, (x, y) = (-1, 2)$.

    (2) (a)

    \begin{gather}
        x^3 - 1 = x \cdot (x^2 - 1) + (x - 1) \\
        x^2 - 1 = (x + 1) \cdot (x - 1)
    \end{gather}


    So $\gcd(a(x), b(x)) = x - 1$.  
    (b) $x-1 = \gcd(a(x), b(x)) = a(x)+(-x) \cdot b(x), (u(x), v(x)) = (1, -x)$.

    (3) (a) $q = 2^2 \cdot (3 \cdot 5 \cdot \cdots \cdot p)-1$. Therefore there exists $k \in \mathbb{N}$ such that $q = 4k + 3$. Notice that all primes are either of the form $4n+3$ or of the form $4n+1$, and

    \begin{gather}
        (4n_1 + 1) \cdot (4n_2 + 1) = 16n_1n_2 + 4n_1 + 4n_2 + 1 = 4(4n_1n_2 + n_1 + n_2) + 1 = 4k + 1 \\
        (4n_1 + 3) \cdot (4n_2 + 3) = 16n_1n_2 + 12n_1 + 12n_2 + 9 = 4(4n_1n_2 + 3n_1 + 3n_2 + 2) + 1 = 4k + 1 \\
        (4n_1 + 1) \cdot (4n_2 + 3) = 16n_1n_2 + 12n_1 + 4n_2 + 3 = 4(4n_1n_2 + 3n_1+n_2) + 3 = 4k + 3 \\
    \end{gather}

    which means every integer of the form $4n+3$ must have a prime divisor of the form $4n+3$. So $q$ must have a prime divisor of the form $4n+3$, which we call $p'$. Notice that for every prime $q'$ less than $p$ we have $q' \nmid q$(decided by the form of $q$). So $p' > p$.  
    (b) If there are finitely many primes of the form $4n+3$, then we denote the largest one to be $p$. So we can use this $p$ to generate a $q$. From (a) we know that there exists a prime $p' > p$ of the form $4n+3$. Contradiction. 

    (4) (a) $q = (2 \cdot 3) \cdot (5 \cdot \cdots \cdot p)-1$. Therefore there exists $k \in \mathbb{N}$ such that $q = 6k + 5$. Notice that all primes are either of the form $6n+1$ or of the form $6n + 5$, and

    \begin{gather}
        (6n_1 + 1) \cdot (6n_2 + 1) = 36n_1n_2 + 6n_1 + 6n_2 + 1 = 6(6n_1n_2 + n_1 + n_2) + 1 = 6k + 1 \\
        (6n_1 + 5) \cdot (6n_2 + 5) = 36n_1n_2 + 30n_1 + 30n_2 + 25 = 6(6n_1n_2 + 5n_1 + 5n_2 + 4) + 1 = 6k + 1 \\
        (6n_1 + 1) \cdot (6n_2 + 5) = 36n_1n_2 + 30n_1 + 6n_2+5 = 6(6n_1n_2 + 5n_1 + n_2) + 5 = 6k + 5
    \end{gather}

    which means every integer of the form $6n+5$ must have a prime divisor of the form $6n+5$. So $q$ must have a prime divisor of the form $6n+5$, which we call $p'$. Notice that for every prime $q'$ less than $p$ we have $q' \nmid q$(decided by the form of $q$). So $p' > p$.  
    (b) If there are finitely many primes of the form $6n+5$, then we denote the largest one to be $p$. So we can use this $p$ to generate a $q$. From (a) we know that there exists a prime $p' > p$ of the form $6n+5$. Contradiction.

    (5) (a) Use induction and we will proof a stronger proposition. We know $F_0 = 3, F_1 = 5, F_2 = 17, F_3 = 257$. Obviously $F_0 = F_1 - 2, F_0F_1 = F_2 - 2, F_0F_1F_2 = F_3 - 2$. Then suppose 
    
    \[
        F_0F_1\cdot F_{m-1} = F_m-2
    \]

    is correct for $k = m$. We need to proof the correctness for $k = m + 1$.

    \begin{align}
        F_0F_1\cdot F_{m-1}F_m & = (F_m-2)F_m \\ & = (2^{2^n} - 1)(2^{2^n} + 1) \\ & = (2^{2^n})^2 - 1 \\ & = 2^{2 \cdot 2^n} - 1 \\ & = 2^{2^{n + 1}} - 1 \\ & = F_{m+1}-2. 
    \end{align}

    So it's obvious that if $m > k \geqslant 1$, then $F_k \mid F_m-2$.  
    (b) If two Fermat's number $F_k$ and $F_m(m > k \geqslant 1)$ have a common divisor $p$ great than 1, then $p \mid F_k$ and $p \mid F_m$. We know that $F_k \mid F_m-2$. So $p \mid F_m-2$ and $p \mid F_m$. Contradiction.  
    (c) From the Fundamental Theorem of Arithmetic, we know that every Fermat's number can be written in the form of products of some primes, and each two Fermat's numbers are coprime. So all the primes are distinguished. There are infinitely many Fermat's numbers, so there are infinitely many primes.

## Week 2

!!! question
    (1) Set $\alpha = 4+5\sqrt{-1}, \beta = 4-5\sqrt{-1}$.  
        (a) Use **Euclidean Algorithm** to show that $\alpha, \beta$ are **coprime**, i.e. a greatest commom divisor of $\alpha$ and $\beta$ is a unit.  
        (b) Find one pair $(x, y) \in \mathbb{Z}[-1] \times \mathbb{Z}[-1]$ such that $\alpha x+\beta y = 1$.  

    (2) Set $\alpha = 11+3\sqrt{-1}, \beta = 1+8\sqrt{-1}$.  
        (a) Use **Euclidean Algorithm** to show that $-1+2\sqrt{-1}$ is a greatest common divisor of $\alpha$ and $\beta$.  
        (b) Find one pair $(x, y) \in \mathbb{Z}[-1] \times \mathbb{Z}[-1]$ such that $\alpha x+\beta y = -1+2\sqrt{-1}$.

    (3) Consider

    \[
        \mathbb{Z}[-2] := \{a+b\sqrt{-2} \mid a, b \in \mathbb{Z} \}.
    \]

    As in the case of $\mathbb{Z}[-1]$, we still define $N(\alpha) = \alpha \overline{\alpha}, \alpha \in \mathbb{Z}[-2]$.   
        (a) Show that $\mathbb{Z}[-2]^{\times} = \{\pm 1\}$.  
        (b) Given $\alpha, \beta \in \mathbb{Z}[-2], \beta \neq 0$, there exists $\gamma, \rho \in \mathbb{Z}[-2]$ such that 

    \[
        \alpha = \beta \gamma + \rho, \enspace N(\rho) < N(\beta).
    \]

    (4) Set $\omega = \frac{-1+\sqrt{-3}}{2}$. (Note that $\omega^2 + \omega + 1 = 0, \omega^2 = \overline{\omega}$.) Consider

    \[
        \mathbb{Z}[\omega] := \{a+b\omega \mid a, b \in \mathbb{Z} \}.
    \]

    As in the case of $\mathbb{Z}[-1]$, we still define $N(\alpha) = \alpha \overline{\alpha}, \alpha \in \mathbb{Z}[\omega]$.   
        (a) Show that $\mathbb{Z}[\omega]^{\times} = \{\pm 1, \pm \omega, \pm \omega^2\}$.  
        (b) Given $\alpha, \beta \in \mathbb{Z}[\omega], \beta \neq 0$, there exists $\gamma, \rho \in \mathbb{Z}[\omega]$ such that 

    \[
        \alpha = \beta \gamma + \rho, \enspace N(\rho) < N(\beta).
    \]

    (5) Have a guess! No details or proofs are needed (though it is still recommended to write a few words to justify your guess). We say an integer $m$ is square-free if for any $k \in \mathbb{Z}, k > 1$, $m$ is not divisible by $k^2$.  
        (a) Let $D$ be a square-free integer of the form $4n + 2$ or $4n + 3$. For which $D$ does the Division theorem (or equivalently the Euclidean algorithm) hold for $\mathbb{Z}[\sqrt{D}]$.  
        (b) Let $D$ be a square-free integer of the form $4n + 1$. For which $D$ does the Division theorem (or equivalently the Euclidean algorithm) hold for $\mathbb{Z}[\frac{-1+\sqrt{D}}{2}]$.

??? note "Answer"
    (1) (a) $\alpha = 4 + 5\sqrt{-1}, \beta = 4 - 5\sqrt{-1}$.  

    \begin{gather} 
        4 + 5\sqrt{-1} = \sqrt{-1} \cdot (4 - 5\sqrt{-1}) + (-1 + \sqrt{-1}) \\
        4 - 5\sqrt{-1} = -4 \cdot (-1 + \sqrt{-1}) + (-\sqrt{-1}) \\  
        -1 + \sqrt{-1} = (-1 - \sqrt{-1}) \cdot (-\sqrt{-1}) + 0
    \end{gather}

    So $\gcd(\alpha, \beta) = -\sqrt{-1}$, which is a unit of $\mathbb{Z}[-1]$. Then $\alpha, \beta$ are coprime.  

    (b) 

    \begin{gather}
        - \sqrt{-1} = (4 - 5\sqrt{-1}) + 4 \cdot (-1 + \sqrt{-1}) = \beta + 4 \cdot (-1 + \sqrt{-1}) \\  
        -1 + \sqrt{-1} = (4 + 5\sqrt{-1}) - \sqrt{-1} \cdot (4 - 5\sqrt{-1}) = \alpha - \sqrt{-1} \cdot \beta \\
        - \sqrt{-1} = \beta + 4 \cdot (\alpha - \sqrt{-1} \cdot \beta) = 4 \cdot \alpha + (1 - 4\sqrt{-1}) \cdot \beta \\
        1 = 4\sqrt{-1} \cdot \alpha + (4 + \sqrt{-1}) \cdot \beta
    \end{gather}

    So $(x, y) = (4\sqrt{-1}, 4 + \sqrt{-1})$.

    (2) (a) $\alpha = 11 + 3\sqrt{-1}, \beta = 1 + 8\sqrt{-1}$.

## Week 3

!!! question
    (1) Suppose that $p$ and $q$ are distinct primes. Let $a$ be a positive integer such that 

    \[
        a^p \equiv a \pmod q, \enspace a^q \equiv a \pmod p.
    \]

    Prove that 

    \[
        a^{pq} \equiv a \pmod {pq}.
    \]

    (2) What is $\phi_{\mathbb{Z}[\sqrt{-1}]}(5)$?

    (3) Prove the following statement. Integer solutions of $a^2+b^2=c^3$ with $(a, b) = 1$ are given by 

    \[
        a = m^3-3mn^2, b = 3m^2n-n^3, c = m^2+n^2
    \]

    where $(m, n) = 1, m \not \equiv n \pmod 2$.

    (4) Solve all integral solutions of the equation $y^2+4 = x^3$.

    (5) Solve all integral solutions of the equation $y^2+2 = x^3$.

??? note "Answer"
    (1) $a^p \equiv a \pmod q$, $a^q \equiv a \pmod p$. We also have $a^p \equiv a \pmod p$ and $a^q \equiv a \pmod q$ according to Fermat's little theorem. Let $a^p = mp + a = nq + a, m, n \in \mathbb{Z}$, $a^q = rp + a = sq + a, r, s \in \mathbb{Z}$, since $p$ and $q$ are distinct primes, we have $q \mid m, q \mid r, p \mid n, p \mid s$. So let $m = k_1q, r = k_2q$, then $n = k_1p, s = k_2p$. So $a^p = k_1pq + a$, $a^q = k_2pq + a$. So $a^p \equiv a^q \equiv a \pmod {pq}$, and $a^{pq} \equiv (a^p)^q \equiv a^q \equiv a \pmod {pq}$.  

    (2) $5 = (2 + \sqrt{-1})(2 - \sqrt{-1})$. If $2 + \sqrt{-1} = \alpha \beta$, then $N(\alpha)N(\beta) = N(2 + \sqrt{-1}) = 5$. Either $N(\alpha)$ or $N(\beta)$ equals 1. So $2 + \sqrt{-1}$ is a prime in $\mathbb{Z}[\sqrt{-1}]$. It follows that $2 - \sqrt{-1}$ is also a prime in $\mathbb{Z}[\sqrt{-1}]$.  
    So 

    \begin{align} 
        \phi_{\mathbb{Z}[\sqrt{-1}]}(5) & = \phi_{\mathbb{Z}[\sqrt{-1}]}((2 + \sqrt{-1})(2 - \sqrt{-1})) \\ & = \phi_{\mathbb{Z}[\sqrt{-1}]}(2 + \sqrt{-1}) \phi_{\mathbb{Z}[\sqrt{-1}]}(2 + \sqrt{-1}) \\ & = (N(2 + \sqrt{-1}) - 1) \cdot (N(2 - \sqrt{-1}) - 1) \\ & = 4 \times 4 = 16.  
    \end{align}

    (3) (i) $c^3 = a^2 + b^2 = (a + b\sqrt{-1})(a - b\sqrt{-1})$. If $d \mid a + b\sqrt{-1}$ and $d \mid a - b\sqrt{-1}$, then $d^2 \mid (a + b\sqrt{-1})(a - b\sqrt{-1}) = c^3$, so $N(d) \mid N(c^3)$. Because $(a, b) = 1$, one is even and the other is odd. So $c^3$ is odd, then $N(d)$ is odd, $N(d) \neq 2$.  
    (ii) $2 = -\sqrt{-1}(1 + \sqrt{-1})^2$ and $N(1 + \sqrt{-1}) = 2$. So $d \neq 1 + \sqrt{-1}$, then $(d, 2) = 1$.  
    (iii) $d \mid a + b\sqrt{-1}$ and $d \mid a - b\sqrt{-1}$, so $d \mid (a + b\sqrt{-1}) + (a - b\sqrt{-1}) = 2a$, $d \mid (a + b\sqrt{-1}) - (a - b\sqrt{-1}) = 2b\sqrt{-1} \Rightarrow d \mid 2b$. Because $(d, 2) = 1$, so $d \mid a, d \mid b$. But $(a, b) = 1$, so $d$ is a unit, $a + b\sqrt{-1}$ and $a - b\sqrt{-1}$ are coprime.  
    (iv) Suppose the prime factorization of $c$ is $c = p_1p_2 \cdots p_r$, where $p_i$ are primes in $\mathbb{Z}[\sqrt{-1}]$. Then $c^3 = p_1^3p_2^3 \cdots p_r^3$. Because $a + b\sqrt{-1}$ and $a - b\sqrt{-1}$ are coprime, so there exists a permunation such that $a + b\sqrt{-1} = p_1^3p_2^3 \cdots p_k^3$ and $a - b\sqrt{-1} = p_{k+1}^3p_{k+2}^3 \cdots p_r^3$. So $a + b\sqrt{-1} = (m + n\sqrt{-1})^3 \cdot u$, $a - b\sqrt{-1} = (m - n\sqrt{-1})^3 \cdot u^{-1}$, $u$ is a unit.  
    The discussion of $u$ is omitted. We set $u = 1$, then $a = m^3 - 3mn^2$, $b = 3m^2n - n^3$, $c = m^2 + n^2$. If $(m, n) \neq 1$, then $(a, b) \neq 1$. Contradiction. If $m \equiv n \pmod 2$, then $(a, b) \neq 1$. Contradiction. So $(m, n) = 1$, $m \not \equiv n \pmod 2$.  

    (4) (a) By Problem (3), first assume $(y, 2) = 1$, then we have 

    \[
        \begin{cases} y = m^3 - 3mn^2 \\ 2 = 3m^2n - n^3 \end{cases} 
    \] 
 
    where $(m, n) = 1$ and $m \not \equiv n \pmod 2$. Since $2 = n(3m^2 - n^2)$, so $n \mid 2$, $n = \pm 1, \pm 2$.  
    If $n = 1$, then $2 = 3m^2 - 1$, $m = \pm 1$. Contradiction.  
    If $n = -1$, then $2 = -3m^2 + 1$. No solution.  
    If $n = 2$, then $1 = 3m^2 - 4$. No solution.  
    If $n = -2$, then $1 = -3m^2 + 4$, $m = \pm 1$. $y = \mp 11$, $x = 5$.  
    (b) If $2 \mid y$, then $x, y$ are both even. Let $y = 2m, x = 2n$, then $4m^2 + 4 = 8n^3 \Rightarrow m^2 + 1 = 2n^3$. Factorize $m^2 + 1 = (m + \sqrt{-1})(m - \sqrt{-1}) = ()$.

    (5) $(y + \sqrt{-2})(y - \sqrt{-2}) = x^3$. Similar computation claim that $y + \sqrt{-2}$ and $y - \sqrt{-2}$ are coprime. Then $y + \sqrt{-2} = (m + n\sqrt{-2})^3 \cdot u$, $y - \sqrt{-2} = (m - n\sqrt{-2})^3 \cdot u^{-1}$, $u$ is a unit. The discussion of $u$ is omitted, we set $u = 1$. Then $y = m^3 - 6mn^2$, $1 = 3m^2n - 2n^3$. Notice that $n \mid 1$, so $n = \pm 1$.  
    If $n = 1$, then $1 = 3m^2 - 2$, $m = \pm 1 \Rightarrow y = \mp 5, x = 3$.  
    If $n = -1$, then $1 = -3m^2 - 2$. No solution.  
    Hence the solutions are $(3, 5), (3, -5)$.

## Week 4

!!! question
    (1) What is the order of $2$ in $(\mathbb{Z}/(19\mathbb{Z}))^{\times}$?  

    (2) (a) Solve all pairs of non-negative integers $(m, n)$ such that $2^m-3^n = 1$. (Hint: Try to modulo $8$ when $m \geqslant 3$.)   
    (b) Solve all pairs of non-negative integers $(m, n)$ such that $-2^m+3^n = 1$. (Hint: Try to modulo $16$ when $m \geqslant 4$.)

    (3) (a) Encode the message "ILOVEZJU" into a sequence of letters via the function $E(x) = 9x + 2 \pmod {26}$.  
    (b) If you get a message "ILOVEZJU" via the encryption function $E(x) = 9x + 2 \pmod {26}$, what is the original message sent by the encrypter?

    (4) (a) Encode the message "ILOVEZJU" via a block cipher into a sequence of letters via the function $E(X) = \begin{pmatrix} 5 & 1 \\ 4 & 3 \end{pmatrix} X \pmod {26}$.  
    (b) If you get a message "ILOVEZJU" via the encryption function $E(X) = \begin{pmatrix} 5 & 1 \\ 4 & 3 \end{pmatrix} X \pmod {26}$, what is the original message sent by the encrypter?

    (5) In the RSA method, take the public key $(m, e) = (119, 5)$ (so $\{p, q\} = \{7, 17\}$).  
    (a) Encode the message "ILOVEZJU" into a sequence of numbers.  
    (b) If you get the message "ILOVEZJU", what is the original sequence of numbers sent by the encrypter?

## Week 5

!!! question
    In this homework, $\omega = \dfrac{-1+\sqrt{-3}}{2}$. Recall that $\mathbb{Z}[\omega] := \{a+b\omega \mid a, b \in \mathbb{Z}\}$. All the units in $\mathbb{Z}[\omega]$ were computed in Homework 2. The norm in $\mathbb{Z}[\omega]$ is still defined to be $N(\alpha) := \alpha \overline{\alpha}$. Let $p > 0$ be a prime in $\mathbb{Z}$.  
    
    (1) Prove that if $p \equiv 1 \pmod 3$, $x^2+x+1 \equiv 0 \pmod p$ has a solution. (Hint: Use order of units, see the proof above Lecture 05 Theorem 1.8)  

    (2) Use Problem 1 to prove that when $p \equiv 1 \pmod 3$, $p$ is not a prime in $\mathbb{Z}[\omega]$. (Hint: Imitate the proof of Lecture 04 Lemma 3.3)

    (3) If $p \equiv 2 \pmod 3$, prove that $p$ stays as a prime in $\mathbb{Z}[\omega]$. (Hint: Imitate the proof of Lecture 06 Lemma 1.3)

    (4) What is the factorization of $3$ in $\mathbb{Z}[\omega]$?  

    (5) If $\mathfrak{p} \in \mathbb{Z}[\omega]$ is a prime and $\mathfrak{p} \not \in \mathbb{Z}$, prove that $N(\mathfrak{p}) = 3$ or $N(\mathfrak{p})$ is a prime congruent to $1$ modulo $3$. (Hint: Imitate the proof of Lecture 06 Lemma 1.2)

## Week 6

!!! question
    As usual, $p$ is an odd prime in $\mathbb{Z}$.  

    (1) (a) Compute $\left(\dfrac{3}{13}\right)$ and $\left(\dfrac{3}{5}\right)$.  
        (b) In general, prove that if $p \equiv \pm 1 \pmod {12}$, then $\left(\dfrac{3}{p}\right) = 1$; if $p \equiv \pm 5 \pmod {12}$, then $\left(\dfrac{3}{p}\right) = -1$. 
    
    (2) Prove that the value of $\left(\dfrac{5}{p}\right)$ only depends on $(p \bmod 10)$. Imitate the statement of Problem 1 (b) and classify cases.

    (3) Prove that the value of $\left(\dfrac{7}{p}\right)$ only depends on $(p \bmod 28)$. Imitate the statement of Problem 1 (b) and classify cases.  

    (4) Determine whether $11$ is a quadratic residue or nonresidue modulo $41$.  

    (5) Determine whether $357$ is a quadratic residue modulo $661$. (Hint: 357 is not a prime, while 661 is.)

??? note "Answer"
    (a) $\left(\dfrac{3}{13}\right) = (-1)^{\dfrac{3 - 1}{2} \cdot \dfrac{13 - 1}{2}}\left(\dfrac{13}{3}\right) = \left(\dfrac{1}{3}\right) = 1$, $\left(\dfrac{3}{5}\right) = (-1)^{\dfrac{3 - 1}{2} \cdot \dfrac{5 - 1}{2}}\left(\dfrac{5}{3}\right) = \left(\dfrac{2}{3}\right) = (-1)^{\dfrac{3^2 - 1}{8}} = -1$.  
    (b) Notice that $\left(\dfrac{3}{p}\right) = (-1)^{\dfrac{3 - 1}{2} \cdot \dfrac{p - 1}{2}}\left(\dfrac{p \bmod 3}{3}\right) = (-1)^{\dfrac{p - 1}{2}}\left(\dfrac{p \bmod 3}{3}\right)$.  
    If $p \equiv 1 \pmod {12}$, then $p = 12k + 1, k \in \mathbb{Z}$. $p \equiv 1 \pmod 3$, so $\left(\dfrac{p \bmod 3}{3}\right) = 1$. Then $\left(\dfrac{3}{p}\right) = (-1)^{\dfrac{p - 1}{2}} = 1$.  
    If $p \equiv -1 \pmod {12}$, then $p = 12k - 1, k \in \mathbb{Z}$. $p \equiv 2 \pmod 3$, so $\left(\dfrac{p \bmod 3}{3}\right) = -1$. Then $\left(\dfrac{3}{p}\right) = (-1)^{\dfrac{p + 1}{2}} = 1$.  
    If $p \equiv 5 \pmod {12}$, then $p = 12k + 5, k \in \mathbb{Z}$. $p \equiv 2 \pmod 3$, so $\left(\dfrac{p \bmod 3}{3}\right) = -1$. Then $\left(\dfrac{3}{p}\right) = (-1)^{\dfrac{p + 1}{2}} = -1$.  
    If $p \equiv -5 \pmod {12}$, then $p = 12k - 5, k \in \mathbb{Z}$. $p \equiv 1 \pmod 3$, so $\left(\dfrac{p \bmod 3}{3}\right) = 1$. Then $\left(\dfrac{3}{p}\right) = (-1)^{\dfrac{p - 1}{2}} = -1$.  

    (2) $\left(\dfrac{5}{p}\right) = (-1)^{\dfrac{5 - 1}{2} \cdot \dfrac{p - 1}{2}}\left(\dfrac{p \bmod 5}{5}\right) = \left(\dfrac{p \bmod 5}{5}\right)$. We consider $p$ as a odd prime, thus $p$ and 5 are coprime. And we know that 

    \begin{gather} 
        \left(\dfrac{1}{5}\right) = 1, \\
        \left(\dfrac{-1}{5}\right) = (-1)^{\dfrac{5 - 1}{2}} = 1, \\
        \left(\dfrac{2}{5}\right) = (-1)^{\dfrac{5^2 - 1}{8}} = -1, \\ 
        \left(\dfrac{-2}{5}\right) = \left(\dfrac{2}{5}\right) \cdot \left(\dfrac{-1}{5}\right) = -1.
    \end{gather}

    However, if we only consider $p \bmod 5$, then $\dfrac{p - 1}{2}$ might not be an integer. So we need to consider $p \bmod 10$. Remember $p$ is an odd prime, then there are only 4 cases: $p \equiv 1 \pmod {10}, p \equiv 3 \pmod {10}, p \equiv -3 \pmod {10}, p \equiv -1 \pmod {10}$.  
    If $p \equiv 1 \pmod {10}$, then $\left(\dfrac{p \bmod 5}{5}\right) = \left(\dfrac{1}{5}\right) = 1$.  
    If $p \equiv -1 \pmod {10}$, then $\left(\dfrac{p \bmod 5}{5}\right) = \left(\dfrac{-1}{5}\right) = 1$.  
    If $p \equiv 3 \pmod {10}$, then $\left(\dfrac{p \bmod 5}{5}\right) = \left(\dfrac{3}{5}\right) = \left(\dfrac{-2}{5}\right) = -1$.  
    If $p \equiv -3 \pmod {10}$, then $\left(\dfrac{p \bmod 5}{5}\right) = \left(\dfrac{-3}{5}\right) = \left(\dfrac{2}{5}\right) = -1$.  
    Generaily speaking, $\left(\dfrac{5}{p}\right)$ only depends on $(p \bmod 10)$, and 

    \[
        \left(\dfrac{5}{p}\right) = \begin{cases} 1, & p \equiv \pm 1 \pmod {10} \\ -1, & p \equiv \pm 3 \pmod {10} \end{cases}
    \]

    (3) $\left(\dfrac{7}{p}\right) = (-1)^{\dfrac{7 - 1}{2} \cdot \dfrac{p - 1}{2}}\left(\dfrac{p \bmod 7}{7}\right) = (-1)^{3 \cdot \dfrac{p - 1}{2}}\left(\dfrac{p \bmod 7}{7}\right) = (-1)^{\dfrac{p - 1}{2}}\left(\dfrac{p \bmod 7}{7}\right)$.  
    Like Problem 1 (b), not only do we need to let $\dfrac{p - 1}{2}$ be an integer, but also we need to consider its parity. So we need to consider the result of $p \bmod 28$. And notice that $p$ and 7 are coprime.  
    If $p \equiv 1 \pmod {28}$, then $p \equiv 1 \pmod 7$, $\dfrac{p - 1}{2}$ is even, so $\left(\dfrac{7}{p}\right) = 1$.  
    If $p \equiv -1 \pmod {28}$, then $p \equiv -1 \pmod 7$, $\dfrac{p - 1}{2}$ is odd, so $\left(\dfrac{7}{p}\right) = (-1) \cdot (-1)^{\dfrac{7 - 1}{2}} = 1$.  
    If $p \equiv 3 \pmod {28}$, then $p \equiv 3 \pmod 7$, $\dfrac{p - 1}{2}$ is odd, so $\left(\dfrac{7}{p}\right) = (-1) \cdot \left(\dfrac{-4}{7}\right) = (-1) \cdot (-1)^{\dfrac{7 - 1}{2}} \cdot \left(\dfrac{4}{7}\right) = 1$.  
    If $p \equiv -3 \pmod {28}$, then $p \equiv 4 \pmod 7$, $\dfrac{p - 1}{2}$ is even, so $\left(\dfrac{7}{p}\right) = \left(\dfrac{4}{7}\right) = 1$.  
    If $p \equiv 5 \pmod {28}$, then $p \equiv 5 \pmod 7$, $\dfrac{p - 1}{2}$ is even, so $\left(\dfrac{7}{p}\right) = \left(\dfrac{5}{7}\right) = \left(\dfrac{-2}{7}\right) = (-1)^{\dfrac{7^2 - 1}{8}} \cdot (-1)^{\dfrac{7 - 1}{2}} = -1$.   
    If $p \equiv -5 \pmod {28}$, then $p \equiv 2 \pmod 7$, $\dfrac{p - 1}{2}$ is odd, so $\left(\dfrac{7}{p}\right) = (-1) \cdot \left(\dfrac{2}{7}\right) = (-1) \cdot (-1)^{\dfrac{7^2 - 1}{8}} = -1$.  
    If $p \equiv 9 \pmod {28}$, then $p \equiv 2 \pmod 7$, $\dfrac{p - 1}{2}$ is even, so $\left(\dfrac{7}{p}\right) = \left(\dfrac{2}{7}\right) = 1$.  
    If $p \equiv -9 \pmod {28}$, then $p \equiv 5 \pmod 7$, $\dfrac{p - 1}{2}$ is odd, so $\left(\dfrac{7}{p}\right) = (-1) \cdot \left(\dfrac{5}{7}\right) = 1$.  
    If $p \equiv 11 \pmod {28}$, then $p \equiv 4 \pmod 7$, $\dfrac{p - 1}{2}$ is odd, so $\left(\dfrac{7}{p}\right) = (-1) \cdot \left(\dfrac{4}{7}\right) = -1$.  
    If $p \equiv -11 \pmod {28}$, then $p \equiv 3 \pmod 7$, $\dfrac{p - 1}{2}$ is even, so $\left(\dfrac{7}{p}\right) = \left(\dfrac{3}{7}\right) = -1$. 
    If $p \equiv 13 \pmod {28}$, then $p \equiv -1 \pmod 7$, $\dfrac{p - 1}{2}$ is even, so $\left(\dfrac{7}{p}\right) = \left(\dfrac{-1}{7}\right) = -1$.  
    If $p \equiv -13 \pmod {28}$, then $p \equiv 1 \pmod 7$, $\dfrac{p - 1}{2}$ is odd, so $\left(\dfrac{7}{p}\right) = -1$.  
    Generaily speaking, $\left(\dfrac{7}{p}\right)$ only depends on $(p \bmod 28)$, and  

    \[
        \left(\dfrac{7}{p}\right) = \begin{cases} 1, & p \equiv \pm 1, \pm 3, \pm 9, \pmod {28} \\ -1, & p \equiv \pm 5, \pm 11, \pm 13 \pmod {28} \end{cases}
    \]

    (4) 

    \begin{align}
        \left(\dfrac{11}{41}\right) & = (-1)^{\dfrac{11 - 1}{2} \cdot \dfrac{41 - 1}{2}}\left(\dfrac{41}{11}\right) \\ & = \left(\dfrac{8}{11}\right) \\ & = \left(\dfrac{2}{11}\right) \cdot \left(\dfrac{4}{11}\right) \\ & = (-1)^{\dfrac{11^2 - 1}{8}} = -1
    \end{align}

    So $11$ is a quadratic nonresidue modulo $41$.  

    (5) Factorize $357 = 3 \times 7 \times 17$. $\left(\dfrac{357}{661}\right) = \left(\dfrac{3}{661}\right) \cdot \left(\dfrac{7}{661}\right) \cdot \left(\dfrac{17}{661}\right)$.  

    \begin{gather}
        \left(\dfrac{3}{661}\right) = (-1)^{\dfrac{3 - 1}{2} \cdot \dfrac{661 - 1}{2}}\left(\dfrac{661}{3}\right) = \left(\dfrac{1}{3}\right) = 1, \\
        \left(\dfrac{7}{661}\right) = (-1)^{\dfrac{7 - 1}{2} \cdot \dfrac{661 - 1}{2}}\left(\dfrac{661}{7}\right) = \left(\dfrac{3}{7}\right) = -1, \\  
        \left(\dfrac{17}{661}\right) = (-1)^{\dfrac{17 - 1}{2} \cdot \dfrac{661 - 1}{2}}\left(\dfrac{661}{17}\right) = \left(\dfrac{-2}{17}\right) = (-1)^{\dfrac{17^2 - 1}{8}} \cdot (-1)^{\dfrac{17 - 1}{2}} = 1.
    \end{gather}

    So $\left(\dfrac{357}{661}\right) = -1$. $357$ is a quadratic nonresidue modulo $661$.

## Week 7

!!! question
    (1) Is $7$ a quadratic residue modulo $11^2$?  

    (2) Is $11$ a quadratic residue modulo $13^2 \times 17^3$?

    (3) Is $19$ a quadratic residue modulo $2^{10}$?

    (4) Is $97$ a quadratic residue modulo $2^4 \times 3^3 \times 5^2$?

    (5) Is $72$ a quadratic residue modulo $2^5 \times 3^5 \times 5^5$?


??? note "Answer"
    (1) According to Hensel's lemma, we only need to check whether $7$ is a quadratic residue modulo $11$. 
    
    \[
        \left(\frac{7}{11}\right) = (-1)^{\dfrac{7 - 1}{2} \cdot \dfrac{11 - 1}{2}}\left(\frac{11}{7}\right) = -\left(\frac{4}{7}\right) = -1.
    \]

    So $7$ is not a quadratic residue modulo $11$, and so is modulo $11^2$.  

    (2) $(13^2, 17^3) = 1$, $(7, 13^2 \times 17^3) = 1$, so according to Chinese Remainder Theorem, $x^2 - 7 \equiv 0 \pmod {13^2 \times 17^3}$ has a solution if and only if $\begin{cases} x^2 - 7 \equiv 0 \pmod {13^2} \\ x^2 - 7 \equiv 0 \pmod {17^3} \end{cases}$ has a solution, which is equivalent to $\begin{cases} x^2 - 7 \equiv 0 \pmod {13} \\ x^2 - 7 \equiv 0 \pmod {17} \end{cases}$ has a solution.

    \[
        \left(\frac{7}{13}\right) = (-1)^{\dfrac{7 - 1}{2} \cdot \dfrac{13 - 1}{2}}\left(\frac{13}{7}\right) = \left(\frac{-1}{7}\right) = (-1)^{\dfrac{7 - 1}{2}} = -1
    \]

    So $11$ is not a quadratic residue modulo $13^2 \times 17^3$.  

    (3) $(19, 2^{10}) = 1$, $19 \equiv 3 \pmod 8$. So $19$ is not a quadratic residue modulo $2^{10}$.  

    (4) $(97, 2^4 \times 3^3 \times 5^2) = 1$, $(2^4, 3^3) = (2^4, 5^2) = (3^3, 5^2) = 1$. So $x^2 -97 \equiv 0 \pmod {2^4 \times 3^3 \times 5^2}$ has a solution if and only if $\begin{cases} x^2 - 97 \equiv 0 \pmod {2^4} \\ x^2 - 97 \equiv 0 \pmod {3^3} \\ x^2 - 97 \equiv 0 \pmod {5^2} \end{cases}$ has a solution. $(97, 2) = 1$, $(97, 3) = 1$, $(97, 5) = 1$, and $97 \equiv 1 \pmod 8$. Thus it is equivalent to $\begin{cases} x^2 - 97 \equiv 0 \pmod {3} \\ x^2 - 97 \equiv 0 \pmod {5} \end{cases}$ has a solution.

    \[
        \left(\frac{97}{3}\right) = \left(\frac{1}{3}\right) = 1, \left(\frac{97}{5}\right) = \left(\frac{2}{5}\right) = (-1)^{\frac{5^2 - 1}{8}} = -1.
    \]

    (5) $72 = 2^3 \times 3^2$. So the equation is $x^2 - 2^3 \times 3^2 \equiv 0 \pmod {2^5 \times 3^5 \times 5^5}$. So we need $x \equiv 0 \pmod 3$, $9 \mid x^2 - 2^3 \times 3^2$. Set $x = 3x_1$, then 
    
    \[
        9(x_1^2 - 2^3) \equiv 0 \pmod {2^5 \times 3^5 \times 5^5} \Rightarrow x_1^2 - 2^3 \equiv 0 \pmod {2^5 \times 3^3 \times 5^5}
    \]

    As the same, we have $x_1 \equiv 0 \pmod 2$, $4 \mid x_1^2 - 2^3$. Set $x_1 = 2x_2$, then we have $x_2^2 - 2 \equiv 0 \pmod {2^3 \times 3^3 \times 5^5}$.  

    Obviously $2 \mid x_2$, but $4 \nmid x_2^2 - 2$. So there is no solution. $72$ is not a quadratic residue modulo $2^5 \times 3^5 \times 5^5$.

## Week 8

!!! question
    $p$ is an odd prime as usual. Let $S$ be the set of nonzero squares (i.e. nonzero quadratic residues) in $\mathbb{Z}/p\mathbb{Z}$.  

    (1) (a) Express $31$ and $10$ as a sum of four squares.  
        (b) Express $310$ as a sum of four squares.

    (2) By an integral quaternion, we mean $\alpha = \begin{pmatrix} a + b\mathrm{i} & c + d\mathrm{i} \\ −c + d\mathrm{i} & a − b\mathrm{i} \end{pmatrix}$ with $a, b, c, d \in \mathbb{Z}$. Prove that for any integral quaternion $\alpha$ and $\beta \neq 0$, there exists $\gamma$ such that 
    
    \[
        N(\alpha − \beta \gamma) \leqslant N(\beta).
    \]

    (3) Prove that if $p \equiv −1 \pmod 4$, then  
    (a) $\mathbb{Z}/p\mathbb{Z} = \{0\} \cup S \cup -S$.  
    (b) $\sum_{a \in S} \sin \frac{2a\pi}{p} = \frac{\sqrt{p}}{2}$.  

    (4) Prove that if $p \equiv 1 \pmod 4$, then 
    
    $$
        \sum_{a \in S} \cos \frac{2a\pi}{p} = \frac{\sqrt{p}-1}{2}.
    $$

    (5) Compute $\cos \frac{2\pi}{13} + \cos \frac{6\pi}{13} + \cos \frac{8\pi}{13}$ (Hint: Use Problem 4.)


??? note "Answer"
    (1) (a) $31 = 25 + 4 + 1 + 1 = 5^2 + 2^2 + 1^2 + 1^2$, $10 = 9 + 1 = 3^2 + 1^2 + 0^2 + 0^2$. So we can construct two matrices  

    \[
        \alpha = \begin{pmatrix} 5 + 2\mathrm{i} & 1 + \mathrm{i} \\ −1 + \mathrm{i} & 5 − 2\mathrm{i} \end{pmatrix}, \ \beta = \begin{pmatrix} 3 + \mathrm{i} & 0 \\ 0 & 3 − \mathrm{i} \end{pmatrix}
    \]

    $N(\alpha) = 31, N(\beta) = 10$. So $N(\alpha \beta) = N(\alpha)N(\beta) = 310$. 
    
    \[
        \alpha \cdot \beta = \begin{pmatrix} 5 + 2\mathrm{i} & 1 + \mathrm{i} \\ −1 + \mathrm{i} & 5 − 2\mathrm{i} \end{pmatrix} \cdot \begin{pmatrix} 3 + \mathrm{i} & 0 \\ 0 & 3 − \mathrm{i} \end{pmatrix} = \begin{pmatrix} 13 + 11\mathrm{i} & 4 + 2\mathrm{i} \\ −4 + 2\mathrm{i} & 13 − 11\mathrm{i} \end{pmatrix}
    \]

    So $310 = 13^2 + 11^2 + 4^2 + 2^2$.

    (2) $\beta \neq 0$, so $\beta$ has an inverse $\beta^{-1}$. Thus $N(\alpha - \beta \gamma) \leqslant N(\beta)$ is equivalent to $N(\beta^{-1} \alpha - \gamma) \leqslant N(E) = 1$. Set $\alpha = \begin{pmatrix} a + b\mathrm{i} & c + d\mathrm{i} \\ −c + d\mathrm{i} & a − b\mathrm{i} \end{pmatrix}$, $a, b, c, d \in \mathbb{Z}$, and $\beta^{-1} = \begin{pmatrix} p + q\mathrm{i} & r + s\mathrm{i} \\ −r + s\mathrm{i} & p − q\mathrm{i} \end{pmatrix}$, $p, q, r, s \in \mathbb{Q}$. Then we have

    \[
        \beta^{-1} \alpha = \begin{pmatrix} x + y\mathrm{i} & z + w\mathrm{i} \\ −z + w\mathrm{i} & x − y\mathrm{i} \end{pmatrix},
    \]

    where 

    \[
        \begin{cases} x = pa - qb - rc - sd \\ y = pb + qa + rd - sc \\ z = pc - qd + ra + sb \\ w = pd + qc - rb + sa \end{cases}
    \]

    Obviously $x, y, z, w \in \mathbb{Q}$, and we suppose that the closest integers to $x, y, z, w$ are $x_1, y_1, z_1, w_1$. We set $x_0 = x - x_1, y_0 = y - y_1, z_0 = z - z_1, w_0 = w - w_1$, then we have $-\frac{1}{2} \leqslant x_0, y_0, z_0, w_0 \leqslant \frac{1}{2}$. So we can construct $\gamma = \begin{pmatrix} x_1 + y_1\mathrm{i} & z_1 + w_1\mathrm{i} \\ −z_1 + w_1\mathrm{i} & x_1 − y_1\mathrm{i} \end{pmatrix}$, and $\beta^{-1} \alpha - \gamma = \begin{pmatrix} x_0 + y_0\mathrm{i} & z_0 + w_0\mathrm{i} \\ −z_0 + w_0\mathrm{i} & x_0 − y_0\mathrm{i} \end{pmatrix}$, and we have $N(\beta^{-1} \alpha - \gamma) = x_0^2 + y_0^2 + z_0^2 + w_0^2 \leqslant \frac{1}{4} + \frac{1}{4} + \frac{1}{4} + \frac{1}{4} = 1$. Thus we have $N(\alpha - \beta \gamma) \leqslant N(\beta)$.  

    (3)

    (3) (a) $\mathbb{Z}/p\mathbb{Z} = \{0, 1, \ldots, p - 1\}$ and we know $\left(\dfrac{q}{p}\right) = \left(\dfrac{q \pmod p}{q}\right)$. So we only consider $\alpha \in \mathbb{Z}/p\mathbb{Z}$, and we only need to prove that if $\alpha \neq 0$, $\alpha \notin S$, then $\alpha \in -S$.  
    $\alpha \neq 0$, $\alpha \notin S$, which means $\left(\dfrac{\alpha}{p}\right) = -1$. And $\left(\dfrac{-1}{p}\right) \cdot \left(\dfrac{\alpha}{p}\right) = \left(\dfrac{-\alpha}{p}\right) = (-1)^{\frac{p - 1}{2}} \cdot (-1) = (-1)^{\frac{p + 1}{2}}$. Because $p \equiv -1 \pmod 4$, so $p = 4k - 1, k \in \mathbb{Z}$. $(-1)^{\frac{p + 1}{2}} = (-1)^{2k} = 1$. So $\left(\dfrac{-\alpha}{p}\right) = 1$, which means $-\alpha \in S$. So $\alpha \in -S$. We can conclude that $\mathbb{Z}/p\mathbb{Z} = \{0\} \cup S \cup -S$.  
    (b) $\mathfrak{G}_1^2 = -p, p \equiv -1 \pmod 4$, so $\mathfrak{G}_1 = \mathrm{i} \sqrt{p}$. And we know 

    \begin{align}
        \mathfrak{G}_1 & = \sum_{t = 0}^{p - 1} \left(\dfrac{t}{p}\right) \omega^t \\
        & = \sum_{\alpha \in S} e^{\frac{2\pi \mathrm{i} \alpha}{p}} + \sum_{\beta \in -S} (-1) e^{\frac{2\pi \mathrm{i} \beta}{p}} \\ & = \sum_{\alpha \in S} (e^{\frac{2\pi \mathrm{i} \alpha}{p}} - e^{-\frac{2\pi \mathrm{i} \alpha}{p}}) \\ & = 2 \sum_{\alpha \in S} \mathrm{i} \sin \dfrac{2\pi \alpha}{p} = \mathrm{i} \sqrt{p}
    \end{align} 

    So $\sum_{\alpha \in S} \sin \dfrac{2\pi \alpha}{p} = \dfrac{\sqrt{p}}{2}$.  

    (4) $p \equiv 1 \pmod 4$, $(-1)^{\frac{p - 1}{2}} = 1$ and $\mathfrak{G}_1^2 = p$. So if $\alpha \in S$, then $-\alpha \in S$, and $\mathfrak{G}_1 = \sqrt{p}$. We also know that $\mathfrak{G}_1 = \sum_{k = 0}^{p - 1} \left(\dfrac{k}{p}\right) e^{\frac{2\pi \mathrm{i} k}{p}} = \sum_{k = 0}^{p - 1} \left(\dfrac{k}{p}\right) (\cos \dfrac{2\pi k}{p} + \mathrm{i} \sin \dfrac{2\pi k}{p})$, so $\sum_{k = 0}^{p - 1} \left(\dfrac{k}{p}\right) \sin \dfrac{2\pi k}{p} = 0$ and $\sum_{k = 0}^{p - 1} \left(\dfrac{k}{p}\right) \cos \dfrac{2\pi k}{p} = \sqrt{p}$. Thus we have $\sum_{\alpha \in S} \cos \dfrac{2\pi \alpha}{p} - \sum_{\alpha \notin S} \cos \dfrac{2\pi \alpha}{p} = \sqrt{p}$. Now it is obvious that we need to prove $\sum_{\alpha \in S} \cos \dfrac{2\pi \alpha}{p} + \sum_{\alpha \notin S} \cos \dfrac{2\pi \alpha}{p} = -1$.  
    Consider $\sum_{k = 0}^{p - 1} e^{\frac{2\pi \mathrm{i} k}{p}} = 0$. So $\sum_{k = 1}^{p - 1} e^{\frac{2\pi \mathrm{i} k}{p}} = -1$, which means $\sum_{k = 1}^{p - 1} (\cos \dfrac{2\pi k}{p} + \mathrm{i} \sin \dfrac{2\pi k}{p}) = -1$. So $\sum_{k = 1}^{p - 1} \cos \dfrac{2\pi k}{p} = -1$. Thus $\sum_{\alpha \in S} \cos \dfrac{2\pi \alpha}{p} + \sum_{\alpha \notin S} \cos \dfrac{2\pi \alpha}{p} = -1$. Then we conclude that $\sum_{\alpha \in S} \cos \dfrac{2\pi \alpha}{p} = \dfrac{\sqrt{p} - 1}{2}$.

    (5) For $t \in \mathrm{Z}/13\mathrm{Z}$, 
    
    \begin{gather}
        \left(\dfrac{1}{13}\right) = 1 \\ 
        \left(\dfrac{2}{13}\right) = (-1)^{\frac{13^2 - 1}{8}} = -1 \\
        \left(\dfrac{3}{13}\right) = \left(\dfrac{16}{13}\right) = 1 \\
        \left(\dfrac{4}{13}\right) = 1 \\
        \left(\dfrac{5}{13}\right) = (-1)^{\frac{5 - 1}{2} \cdot \frac{13 - 1}{2}} \left(\dfrac{13}{5}\right) = \left(\dfrac{3}{5}\right) = \left(\dfrac{-2}{5}\right) = (-1)^{\frac{5 - 1}{2}} \cdot (-1) ^{\frac{5^2 - 1}{8}} = -1 \\
        \left(\dfrac{6}{13}\right) = \left(\dfrac{2}{13}\right) \cdot \left(\dfrac{3}{13}\right) = -1 \\
        \left(\dfrac{7}{13}\right) = \left(\dfrac{-6}{13}\right) = (-1)^{\frac{13 - 1}{2}} \cdot \left(\dfrac{6}{13}\right) = -1 \\  
        \left(\dfrac{8}{13}\right) = \left(\dfrac{-5}{13}\right) = (-1)^{\frac{13 - 1}{2}} \cdot \left(\dfrac{5}{13}\right) = -1 \\  
        \left(\dfrac{9}{13}\right) = 1 \\
        \left(\dfrac{10}{13}\right) = \left(\dfrac{-3}{13}\right) = (-1)^{\frac{13 - 1}{2}} \cdot \left(\dfrac{3}{13}\right) = -1 \\  
        \left(\dfrac{11}{13}\right) = \left(\dfrac{-2}{13}\right) = (-1)^{\frac{13 - 1}{2}} \cdot \left(\dfrac{2}{13}\right) = -1 \\
        \left(\dfrac{12}{13}\right) = \left(\dfrac{-1}{13}\right) = 1
    \end{gather}

    \begin{align}
        \sum_{\alpha \in S} \cos \dfrac{2\pi \alpha}{13} & = \cos \dfrac{2\pi}{13} + \cos \dfrac{6\pi}{13} + \cos \dfrac{8\pi}{13} + \cos \dfrac{18\pi}{13} + \cos \dfrac{20\pi}{13} + \cos \dfrac{24\pi}{13} \\ & = 2(\cos \dfrac{2\pi}{13} + \cos \dfrac{6\pi}{13} + \cos \dfrac{8\pi}{13}) = \dfrac{\sqrt{13} - 1}{2}
    \end{align}

    So $\cos \dfrac{2\pi}{13} + \cos \dfrac{6\pi}{13} + \cos \dfrac{8\pi}{13} = \dfrac{\sqrt{13} - 1}{4}$.

## Week 9

!!! question
    (1) What is the fundamental solution of $x^2−3y^2 = 1$? Based on the fundamental solution, write down two other solutions of this Pell's equation.  

    (2) By a triangular-square number, we mean a positive integer $N$ which is both a square(i.e. $N = m^2, m \in \mathbb{Z}$) and can be written as $N = \dfrac{n(n+1)}{2}$ for some positive integer $n$. Do some numerical experiments and find at least one triangular-square number greater than 1.  

    (3) Use the Pell's equation $x^2−2y^2 = 1$ to prove that there are infinitely many triangular-square numbers. Write down a third triangular-square number different from 1 and the number you provide in Problem 2.

    (4) In the Tetryakov Gallery in Moscow, there is a painting of Bogdanov-Belsky (1895) showing that a group of children are computing 

    \[
        \dfrac{1}{365}(10^2 + 11^2 + 12^2 + 13^3 + 14^2)
    \]

    A somewhat coincidence we notice is that

    \[
        10^2 + 11^2 + 12^2 = 13^2 + 14^2.
    \]

    Prove that this is not a coincidence: there exist infinitely many positive integers $a, b$ satisfying the equation:  

    \[
        a^2 + (a + 1)^2 = b^2 + (b + 1)^2 + (b + 2)^2.
    \]

    (Hint: try to relate the above equation to the generalized Pell's equation: $x^2 −6y^2 = 3$.)

    (5)  Given a triangle with sides $a, b, c,$ Heron's formula says that the area of this triangle is equal to

    \[
        A = \sqrt{s(s - a)(s - b)(s - c)}, \qquad s = \dfrac{1}{2}(a + b + c).
    \]

    Prove that there are infinitely many triangles with integral sides $a − 1, a, a + 1$ (i.e. $a \geqslant 3$ is an integer) and integral area $A$ (i.e. $A \in \mathbb{Z}$.) Find at least one such triangle and its area. (Hint: relate this problem to the Pell's equation $x^2 − 3y^2 = 1$.)

??? note "Answer"
    (1) The fundamental solution of equation $x^2 - 3y^2 = 1$ is $(2, 1)$, or $\alpha = 2 + \sqrt{3}$. We know that $\pm \alpha^k, k \in \mathbb{Z}$ are all the solutions, so $\alpha^2 = 7 + 4\sqrt{3}$, $\alpha^4 = 97 + 56\sqrt{3}$ are both solutions.  

    (2) $N = \dfrac{n(n + 1)}{2}$, which means $n^2 + n - 2N = 0$. The positive solution to this equation is $n = \dfrac{\sqrt{8N + 1} - 1}{2}$. So we need not only $N$, but also $8N + 1$ are squares. We can find that when $N = 36$, $8N + 1 = 289 = 17^2$. So $N = 36$ is a triangular-square number.  

    (3) The fundamental solution of equation $x^2 - 2y^2 = 1$ is $(3, 2)$, or $\alpha = 3 + 2\sqrt{2}$. We know triangle-square numbers satisfy that if $N = M^2, M \in \mathbb{Z}$, then $K = 8N + 1 = 8M^2 + 1 = P^2, P \in \mathbb{Z}$.   
    We can see more clearly if we transform the equation into $P^2 - 8M^2 = 1$ and consider it as square-free, which means $x = P, y = 2M$, then $x^2 - 2y^2 = 1$. So what we are looking for is $\left(\dfrac{y}{2}\right)^2$, where $y$ is the solution to the Pell's equation $x^2 - 2y^2 = 1$. The fundamental solution is $\alpha = 3 + 2\sqrt{2}$, and $\alpha^2 = 17 + 12\sqrt{2}$, which corresponds to $6^2 = 36$.   
    We need to find another solution. $\alpha^4 = 577 + 408\sqrt{2}$, so $204^2 = 41616$ is also a triangular-square number.  

    (4) Consider the equation $a^2 + (a + 1)^2 = b^2 + (b + 1)^2 + (b + 2)^2$. We have 

    \begin{gather}
        2a^2 + 2a + 1 = 3b^2 + 6b + 5 \\
        4a^2 + 4a + 2 = 6b^2 + 12b + 10 \\
        (2a + 1)^2 = 6(b + 1)^2 + 3 \\
        (2a + 1)^2 - 6(b + 1)^2 = 3
    \end{gather}

    Let $x = 2a + 1, y = b + 1$, then we have $x^2 - 6y^2 = 3$. We need to prove the generalized Pell's equation $x^2 - 6y^2 = 3$ has infinitely many solutions with $x$ odd.  
    Obviously, $(3, 1)$ is a solution, and $(5, 2)$ is the fundamental solution to the standard Pell's equation $x^2 - 6y^2 = 1$. So $\gamma_0 = 3 + \sqrt{6}$, $\alpha = 5 + 2\sqrt{6}$. All the solution to equation $N(\gamma) = 3$ has the form $\gamma = \gamma_0 \alpha^k = (3 + \sqrt{6})(5 + 2\sqrt{6})^k$. Consider when $k = 2^m$, then $\gamma = (3 + \sqrt{6})(5 + 2\sqrt{6})^{2^m} = (3 + \sqrt{6})(49 + 20\sqrt{6})^{2^{m - 1}}$. $3, 49, 1$ are all odd, and $20$ is even. So if $m = 1$, then $3 \times 49 + 20 \times 1 \times 6$ is odd. Consider $(p + q\sqrt{6})^2$, with $p$ odd, then its integer part is $p^2 + 6q^2$, which is odd. So the integer part of $(49 + 20\sqrt{6})^{2^{m - 1}}$ is odd, and the integer part of $\gamma$ is also odd. Since there are infinitely many $m$, so there are infinitely many solutions to the generalized Pell's equation $x^2 - 6y^2 = 3$ with $x$ odd.  

    (5) Consider if the equation holds, we have $A^2 = s(s - (a - 1))(s - a)(s - (a + 1))$, and $s = \dfrac{1}{2}((a - 1) + a + (a + 1)) = \dfrac{3a}{2}$. So $16A^2 = 3a(a + 2)a(a - 2) = 3a^2(a^2 - 4)$. Let $a = 2t$, then $16A^2 = 12t^2(4t^2 - 4) = 48t^2(t^2 - 1)$. So $A^2 = 3t^2(t^2 - 1)$, and let $A = 3s$, then $3s^2 = t^2(t^2 - 1)$.  
    Here comes the important part: divide the equation by $t^2$, we have $3\left(\dfrac{s}{t}\right)^2 = t^2 - 1$. Let $x = t$, $y = \dfrac{s}{t}$, then we have $x^2 - 3y^2 = 1$. We know this standard Pell's equation has infinitely many solutions, so there are infinitely many triangles with integral sides $a - 1, a, a + 1$ and integral area $A$.  
    The fundamental solution of $x^2 - 3y^2 = 1$ is $(2, 1)$, $\alpha = 2 + \sqrt{3}$. So $t = x = 2, s = t \cdot y = 2$, and $A = 3s = 6$, $a = 2t = 4$. So the triangle is $(3, 4, 5)$, and its area is $6$.


## Week 10

!!! question
    Feel free to use a calculator in the following problems. The problems are designed to enhance your understanding on the lecture materials, though the numerical computations are quite messy.

    (1) Let $a, b, x, y$ be positive integers satisfying 

    \[
        x^2 − dy^2 = a^2 − db^2 = −1.
    \]

    Prove that the following statements are equivalent:  
    (a) $a + b\sqrt{d} < x + y\sqrt{d}$;  
    (b) $a < x$ and $b < y$;  
    (c) $a < x$ or $b < y$.

    (2) Assume the existence of a fundamental solution of $x^2−dy^2 = −1$. Say $\beta = x_1+y_1\sqrt{d}$ is the fundamental solution. Prove that all the solutions $(x^n, y^n)$ come from 'comparing coefficients':

    \[
        x_n + y_n\sqrt{d} = \pm (x_1 + y_1\sqrt{d})^{2n+1}.
    \]

    (3) In class, we gave an explanation of $\sqrt{−1}$ via matrices. The following provides an analogue of this perspective. Let $(x_1, y_1)$ be the fundamental solution of the Pell's equation $x^2 − dy^2 = −1$. Prove that $(x_n, y_n)$ provided by the recursive formula  

    \[
        \begin{pmatrix} x_n \\ y_n \end{pmatrix} = \begin{pmatrix} x_1 & dy_1 \\ y_1 & x_1 \end{pmatrix}  \begin{pmatrix} x_{n - 1} \\ y_{n - 11} \end{pmatrix}
    \]

    satisfies $x_n^2 - dy_n^2 = (-1)^n$.  

    (4) Completely solve the generalized Pell's equation $x^2−7y^2 = 57$. (Hint: Take as granted that $u = 8 + 3\sqrt{7}$ is a fundamental solution of the standard Pell's equation.)  

    (5) Prove that $x^2−37y^2 = 11$ has no solution. (Hint: Take as granted that $u = 73 + 12\sqrt{37}$ is a fundamental solution of the standard Pell's equation.)

## Week 11

!!! question
    In this Problem set, $d$ is a square-free integer not equal to $0$ or $1$. $K = \mathbb{Q}(\sqrt{d})$.

    (1) In this problem, $d = −23$, $\mathfrak{a} = (2, \dfrac{1 + \sqrt{-23}}{2})$.  
    (a) Prove that $N(\mathfrak{a}) = 2$.  
    (b) Use (a) to prove that $\mathfrak{a}$ cannot be generated by one element, i.e. there is no $\alpha \in \mathcal{O}_K$ with $\mathfrak{a} = (\alpha)$.

    (2)  Assume that $\alpha \in \mathcal{O}_K,$ $a, b$ are coprime positive integers such that they satisfy $\lvert N(\alpha) \rvert = ab$. Prove that 

    \[
        (a, \alpha)(b, \alpha) = (\alpha).
    \]

    (3) Prove the factorization of $(2)$ into product of prime ideals in $\mathcal{O}_K$:  

    \[
        (2) = \begin{cases} (2) \text{ if } d \equiv 5 \pmod 8 \\
        (2, \dfrac{1 + \sqrt{d}}{2})(2, \dfrac{1 − \sqrt{d}}{2}) \text{ if } d \equiv 1 \pmod 8 \\
        (2, 1 + \sqrt{d})^2 \text{ if } d \equiv 3 \pmod 4 \\ 
        (2, \sqrt{d})^2 \text{ if } d \equiv 2 \pmod 4 \end{cases}
    \]

    (4) (a) Prove that when $d = -163$, $(11)$ stays as a prime ideal in $\mathcal{O}_K$.  
    (b) Prove that when $d = 7$, (3) splits into a product of $(3, 1 + \sqrt{7})(3, 1 − \sqrt{7})$.  

    (5) Set $d = 366$. Factorize $(6)$ into a product of prime ideals in $\mathcal{O}_K$. (Hint: First factorize $(6) = (2)(3)$)

??? note "Answer"
    (1) (a) $\mathfrak{a} = (2, \dfrac{1 + \sqrt{-23}}{2})$, $N(\mathfrak{a}) = \gcd(N(2), N(\dfrac{1 + \sqrt{-23}}{2}), Tr(2 \cdot \dfrac{1 + \sqrt{-23}}{2})) = \gcd(4, 6, 2) = 2$.  
    (b) $\mathfrak{a} \cdot \sigma (\mathfrak{a}) = (2)$. If $\mathfrak{a}$ is generated by only one element, which means $\mathfrak{a} = (\alpha)$, then we have $(\alpha) \cdot (\sigma(\alpha)) = (2)$, which means if $\alpha = \dfrac{-a + b\sqrt{-23}}{2}$ $(\mathcal{O}_K = \mathbb{Z}[\dfrac{-1 + \sqrt{-23}}{2}])$ for $-23 \equiv 1 \pmod 4$, then $\dfrac{a^2 + 23b^2}{4} = 2 \Rightarrow a^2 + 23b^2 = 8$. However, there is no integer solution. So $\mathfrak{a}$ cannot be generated by one element.  

    (2) $(a, \alpha)(b, \alpha) = (ab, a\alpha, b\alpha, \alpha^2) = (N(\alpha), a\alpha, b\alpha, \alpha^2) = (\alpha \cdot \sigma(\alpha), a\alpha, b\alpha, \alpha^2)$. Consider $a, b$ are coprime, so $\gcd(a\alpha, b\alpha) = \alpha$, and $\alpha \cdot \sigma(\alpha), \alpha^2$ are all multiples of $\alpha$. So $(a, \alpha)(b, \alpha) = (\alpha)$.  

    (3) (a) If $d \equiv 5 \pmod 8$, then we can write $d = 8k + 5$. And we have $d \equiv 1 \pmod 4$, so the criterion polynomial $f(x) = x^2 - x + \frac{1-d}{4} = x^2 - x - 2k - 1$, which is irreducible in $\mathbb{Z}_2[x]$. So $(2)$ stays as a prime ideal in $\mathcal{O}_K$.  
    (b) If $d \equiv 1 \pmod 8$, then we can write $d = 8k + 1$. And we have $d \equiv 1 \pmod 4$, so the criterion polynomial $f(x) = x^2 - x + \frac{1-d}{4} = (x + \frac{-1 - \sqrt{d}}{2})(x + \frac{-1 + \sqrt{d}}{2}) = x^2 - x - 2k$, and $\omega = \frac{1 + \sqrt{d}}{2}$. $f(x) \equiv x(x - 1) \pmod 2$, which means $c = 0$, $c' = 1(0 \not \equiv 1 \pmod 2)$. So $\mathfrak{p} = (2, \frac{1 + \sqrt{d}}{2} - 0) = (2, \frac{1 + \sqrt{d}}{2})$, $\sigma(\mathfrak{p}) = (2, \frac{1 - \sqrt{d}}{2})$. So $(2) = \mathfrak{p} \cdot \sigma(\mathfrak{p}) = (2, \frac{1 + \sqrt{d}}{2})(2, \frac{1 - \sqrt{d}}{2})$.  
    (c) If $d \equiv 3 \pmod 4$, then we can write $d = 4k + 3$. And the criterion polynomial $f(x) = x^2 - d = (x - \sqrt{d})(x + \sqrt{d}) = x^2 - 4k - 3$, with $\omega = \sqrt{d}$. $f(x) \equiv x^2 + 2x + 1 = (x + 1)^2 \pmod 2$, which means $c = -1$. So $\mathfrak{p} = (2, 1 + \sqrt{d})$. $(p) = \mathfrak{p}^2 = (2, 1 + \sqrt{d})^2$.  
    (d) If $d \equiv 2 \pmod 4$, then we can write $d = 4k + 2$. And the criterion polynomial $f(x) = x^2 - d = (x - \sqrt{d})(x + \sqrt{d}) = x^2 - 4k - 2$, with $\omega = \sqrt{d}$. $f(x) \equiv x^2 \pmod 2$, which means $c = 0$. So $\mathfrak{p} = (2, \sqrt{d})$. $(p) = \mathfrak{p}^2 = (2, \sqrt{d})^2$.  

    (4) (a) $d = -163 \equiv 1 \pmod 4$. The criterion polynomial $f(x) = x^2 - x + 41$. $f(x) \equiv x^2 - x - 3 \pmod 11$, which is irreducible in $\mathbb{Z}_{11}[x]$. So $(11)$ stays as a prime ideal in $\mathcal{O}_K$.  
    (b) $d = 7 \equiv 3 \pmod 4$. The criterion polynomial $f(x) = x^2 - 7 = (x - \sqrt{7})(x + \sqrt{7})$, with $\omega = \sqrt{7}$. $f(x) \equiv x^2 - 1 = (x - 1)(x + 1) \pmod 3$, with $c = 1$, $c' = -1$. We have $\mathfrak{p} = (3, 1 + \sqrt{7})$, $\sigma(\mathfrak{p}) = (3, 1 - \sqrt{7})$. So $(3) = \mathfrak{p} \cdot \sigma(\mathfrak{p}) = (3, 1 + \sqrt{7})(3, 1 - \sqrt{7})$.  

    (5) $d = 366 \equiv 2 \pmod 4$. $(6) = (2)(3)$. From (3) we know $(2)$ can be factorized into $(2, \sqrt{366})^2$. And for $(3)$, the criterion polynomial $f(x) = x^2 - 366 = (x - \sqrt{366})(x + \sqrt{366})$, with $\omega = \sqrt{366}$. $f(x) \equiv x^2 \pmod 3$, which means $c = 0$. We have $\mathfrak{p} = (3, \sqrt{366})$ and $(3) = \mathfrak{p}^2 = (3, \sqrt{366})^2$. So $(6) = (2)(3) = (2, \sqrt{366})^2(3, \sqrt{366})^2$.