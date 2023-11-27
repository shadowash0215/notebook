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
    (1) (a) <div class="center">

    | Equation |
    |:-----------:|
    |$20 = 1 \cdot 12 + 8$|
    |$12 = 1 \cdot 8 + 4$|
    |$8 = 2 \cdot 4$|

    </div>  
    So $\gcd(a, b) = 4$.  
    (b) <div class="center">

    | Equation |
    |:-----------:|
    |$4 = 12+(-1) \cdot 8 = b+(-1)\cdot 8$|
    |$8 = 20+(-1) \cdot 12 = a+(-1)\cdot b$|

    </div>  
    So $4 = \gcd(a, b) = (-1)\cdot a+2 \cdot b, (x, y) = (-1, 2)$.

    (2) (a) <div class="center">

    | Equation |
    |:-----------:|
    |$x^3-1 = x \cdot (x^2-1)+(x-1)$|
    |$x^2-1 = (x+1) \cdot (x-1)$|

    </div>  
    So $\gcd(a(x), b(x)) = x-1$.  
    (b) $x-1 = \gcd(a(x), b(x)) = a(x)+(-x) \cdot b(x), (u(x), v(x)) = (1, -x)$.

    (3) (a) $q = 2^2 \cdot (3 \cdot 5 \cdot \cdots \cdot p)-1$. Therefore there exists $k \in \mathbb{N}$ such that $q=4k+3$. Notice that all primes are either of the form $4n+3$ or of the form $4n+1$, and
    <div class="center">

    | Equation |
    |:-----------:|
    |$(4n_1+1) \cdot (4n_2+1) = 16n_1n_2+4n_1+4n_2+1 = 4(4n_1n_2+n_1+n_2)+1 = 4k+1$|
    |$(4n_1+3) \cdot (4n_2+3) = 16n_1n_2+12n_1+12n_2+9 = 4(4n_1n_2+3n_1+3n_2+2)+1 = 4k+1$|
    |$(4n_1+1) \cdot (4n_2+3) = 16n_1n_2+12n_1+4n_2+3 = 4(4n_1n_2+3n_1+n_2)+3 = 4k+3$|

    </div>  
    which means every integer of the form $4n+3$ must have a prime divisor of the form $4n+3$. So $q$ must have a prime divisor of the form $4n+3$, which we call $p'$. Notice that for every prime $q'$ less than $p$ we have $q' \nmid q$(decided by the form of $q$). So $p' > p$.  
    (b) If there are finitely many primes of the form $4n+3$, then we denote the largest one to be $p$. So we can use this $p$ to generate a $q$. From (a) we know that there exists a prime $p' > p$ of the form $4n+3$. Contradiction. 

    (4) (a) $q = (2 \cdot 3) \cdot (5 \cdot \cdots \cdot p)-1$. Therefore there exists $k \in \mathbb{N}$ such that $q=6k+5$. Notice that all primes are either of the form $6n+1$ or of the form $6n+5$, and
    <div class="center">

    | Equation |
    |:-----------:|
    |$(6n_1+1) \cdot (6n_2+1) = 36n_1n_2+6n_1+6n_2+1 = 6(6n_1n_2+n_1+n_2)+1 = 6k+1$|
    |$(6n_1+5) \cdot (6n_2+5) = 36n_1n_2+30n_1+30n_2+25 = 6(6n_1n_2+5n_1+5n_2+4)+1 = 6k+1$|
    |$(6n_1+1) \cdot (6n_2+5) = 36n_1n_2+30n_1+6n_2+5 = 6(6n_1n_2+5n_1+n_2)+5 = 6k+5$|

    </div>  
    which means every integer of the form $6n+5$ must have a prime divisor of the form $6n+5$. So $q$ must have a prime divisor of the form $6n+5$, which we call $p'$. Notice that for every prime $q'$ less than $p$ we have $q' \nmid q$(decided by the form of $q$). So $p' > p$.  
    (b) If there are finitely many primes of the form $6n+5$, then we denote the largest one to be $p$. So we can use this $p$ to generate a $q$. From (a) we know that there exists a prime $p' > p$ of the form $6n+5$. Contradiction.

    (5) (a) Use induction and we will proof a stronger proposition. We know $F_0 = 3, F_1 = 5, F_2 = 17, F_3 = 257$. Obviously $F_0 = F_1 - 2, F_0F_1 = F_2 - 2, F_0F_1F_2 = F_3 - 2$. Then suppose 
    
    $$
        F_0F_1\cdot F_{m-1} = F_m-2
    $$

    is correct for $k=m$. We need to proof the correctness for $k=m+1$.

    $$
        F_0F_1\cdot F_{m-1}F_m = (F_m-2)F_m = (2^{2^n}-1)(2^{2^n}+1) = (2^{2^n})^2-1 = 2^{2 \cdot 2^n}-1 = 2^{2^{n+1}}-1 = F_{m+1}-2. 
    $$ 
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

    $$
        \mathbb{Z}[-2] := \{a+b\sqrt{-2} \mid a, b \in \mathbb{Z} \}.
    $$

    As in the case of $\mathbb{Z}[-1]$, we still define $N(\alpha) = \alpha \overline{\alpha}, \alpha \in \mathbb{Z}[-2]$.   
        (a) Show that $\mathbb{Z}[-2]^{\times} = \{\pm 1\}$.  
        (b) Given $\alpha, \beta \in \mathbb{Z}[-2], \beta \neq 0$, there exists $\gamma, \rho \in \mathbb{Z}[-2]$ such that 

    $$
        \alpha = \beta \gamma + \rho, \enspace N(\rho) < N(\beta).
    $$

    (4) Set $\omega = \frac{-1+\sqrt{-3}}{2}$. (Note that $\omega^2 + \omega + 1 = 0, \omega^2 = \overline{\omega}$.) Consider

    $$
        \mathbb{Z}[\omega] := \{a+b\omega \mid a, b \in \mathbb{Z} \}.
    $$

    As in the case of $\mathbb{Z}[-1]$, we still define $N(\alpha) = \alpha \overline{\alpha}, \alpha \in \mathbb{Z}[\omega]$.   
        (a) Show that $\mathbb{Z}[\omega]^{\times} = \{\pm 1, \pm \omega, \pm \omega^2\}$.  
        (b) Given $\alpha, \beta \in \mathbb{Z}[\omega], \beta \neq 0$, there exists $\gamma, \rho \in \mathbb{Z}[\omega]$ such that 

    $$
        \alpha = \beta \gamma + \rho, \enspace N(\rho) < N(\beta).
    $$

    (5) Have a guess! No details or proofs are needed (though it is still recommended to write a few words to justify your guess). We say an integer $m$ is square-free if for any $k \in \mathbb{Z}, k > 1$, $m$ is not divisible by $k^2$.  
        (a) Let $D$ be a square-free integer of the form $4n + 2$ or $4n + 3$. For which $D$ does the Division theorem (or equivalently the Euclidean algorithm) hold for $\mathbb{Z}[\sqrt{D}]$.  
        (b) Let $D$ be a square-free integer of the form $4n + 1$. For which $D$ does the Division theorem (or equivalently the Euclidean algorithm) hold for $\mathbb{Z}[\frac{-1+\sqrt{D}}{2}]$.

## Week 3

!!! question
    (1) Suppose that $p$ and $q$ are distinct primes. Let $a$ be a positive integer such that 

    $$
        a^p \equiv a \pmod q, \enspace a^q \equiv a \pmod p.
    $$

    Prove that 

    $$
        a^{pq} \equiv a \pmod {pq}.
    $$

    (2) What is $\phi_{\mathbb{Z}[\sqrt{-1}]}(5)$?

    (3) Prove the following statement. Integer solutions of $a^2+b^2=c^3$ with $(a, b) = 1$ are given by 

    $$
        a = m^3-3mn^2, b = 3m^2n-n^3, c = m^2+n^2
    $$

    where $(m, n) = 1, m \not \equiv n \pmod 2$.

    (4) Solve all integral solutions of the equation $y^2+4 = x^3$.

    (5) Solve all integral solutions of the equation $y^2+2 = x^3$.

## Week 4

!!! question
    (1) What is the order of $2$ in $(\mathbb{Z}/(19\mathbb{Z}))^{\times}$?  

    (2) (a) Solve all pairs of non-negative integers $(m, n)$ such that $2^m-3^n = 1$. (Hint: Try to modulo $8$ when $m \geqslant 3$.)   
    (b) Solve all pairs of non-negative integers $(m, n)$ such that $-2^m+3^n = 1$. (Hint: Try to modulo $16$ when $m \geqslant 4$.)

    (3) (a) Encode the message "ILOVEZJU" into a sequence of letters via the function $E(x) = 9x + 2 \pmod {26}$.  
    (b) If you get a message "ILOVEZJU" via the encryption function $E(x) = 9x + 2 \pmod {26}$, what is the original message sent by the encrypter?

    (4) (a) Encode the message "ILOVEZJU" via a block cipher into a sequence of letters via the function $E(X) = \begin{pmatrix} 5 & 1 \\ 4 & 3 \end{pmatrix} X \pmod {26}$.  
    (b) If you get a message "ILOVEZJU" via the encryption function $E(X) = \begin{pmatrix} 5 & 1 \\ 4 & 3 \end{pmatrix} X \pmod {26}$, what is the original message sent by the encrypter?

    (5) In the RSA method, take the public key $(m, e) = (119, 5)$ $(so \{p, q\} = \{7, 17\})$.  
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

    (1) (a) Compute $\left(\frac{3}{13}\right)$ and $\left(\frac{3}{5}\right)$.  
        (b) In general, prove that if $p \equiv \pm 1 \pmod {12}$, then $\left(\frac{3}{p}\right) = 1$; if $p \equiv \pm 5 \pmod {12}$, then $\left(\frac{3}{p}\right) = -1$. 
    
    (2) Prove that the value of $\left(\frac{5}{p}\right)$ only depends on $(p \bmod 10)$. Imitate the statement of Problem 1 (b) and classify cases.

    (3) Prove that the value of $\left(\frac{7}{p}\right)$ only depends on $(p \bmod 10)$. Imitate the statement of Problem 1 (b) and classify cases.  

    (4) Determine whether $11$ is a quadratic residue or nonresidue modulo $41$.  

    (5) Determine whether $357$ is a quadratic residue modulo $661$. (Hint: 357 is not a prime, while 661 is.)

## Week 7

!!! question
    (1) Is $7$ a quadratic residue modulo $11^2$?  

    (2) Is $11$ a quadratic residue modulo $13^2 \times 17^3$?

    (3) Is $19$ a quadratic residue modulo $2^{10}$?

    (4) Is $97$ a quadratic residue modulo $2^4 \times 3^3 \times 5^2$?

    (5) Is $72$ a quadratic residue modulo $2^5 \times 3^5 \times 5^5$?

## Week 8

!!! question
    $p$ is an odd prime as usual. Let $S$ be the set of nonzero squares (i.e. nonzero quadratic residues) in $\mathbb{Z}/p\mathbb{Z}$.  

    (1) (a) Express $31$ and $10$ as a sum of four squares.
        (b) Express $310$ as a sum of four squares.

    (2) By an integral quaternion, we mean $\alpha = \begin{pmatrix} a + b\mathrm{i} & c + d\mathrm{i} \\ −c + d\mathrm{i} & a − b\mathrm{i} \end{pmatrix}$ with $a, b, c, d \in \mathbb{Z}$. Prove that for any integral quaternion $\alpha$ and $\beta \neq 0$, there exists $\gamma$ such that 
    
    \[
        N(\alpha − \beta \gamma) < N(\beta).
    \]

    (3) Prove that if $p \equiv −1 \pmod 4$, then  
    (a) $\mathbb{Z}/p\mathbb{Z} = \{0\} \cup S \cup -S$.  
    (b) $\sum_{a \in S} \sin \frac{2a\pi}{p} = \frac{\sqrt{p}}{2}$.  

    (4) Prove that if $p \equiv 1 \pmod 4$, then 
    
    $$
        \sum_{a \in S} \cos \frac{2a\pi}{p} = \frac{\sqrt{p}-1}{2}.
    $$

    (5) Compute $\cos \frac{2\pi}{13} + \cos \frac{6\pi}{13} + \cos \frac{8\pi}{13}$ (Hint: Use Problem 4.)