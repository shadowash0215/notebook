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