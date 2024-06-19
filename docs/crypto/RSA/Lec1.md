# Misc

## Factor $N$ given $N$, $e$, $d$

!!! success "Algorithm Design"
    1. Compute $f = ed - 1$.  
    2. Express $f$ as $f = 2^s \cdot t$ with $t$ odd.  
    3. Set $i \leftarrow s$ and $a \leftarrow 2$.  
    4. Compute $b = a^t \mod N$, and if $b = 1$ then  
        - set $a$ to the next prime, and proceed to step 4.
    5. If $i \neq 1$ then
        - compute $c \leftarrow b^2 \mod N$, and if $c neq 1$ then
            - set $b \leftarrow c$ and $i \leftarrow i - 1$, and proceed to step 5.
    6. If $b = N - 1$ then
        - set $a$ to the next prime, and proceed to step 4.
    7. Compute and output $p \leftarrow \gcd(b - 1, N)$, and $q \leftarrow N / p$.

!!! note "Proof"
    In an RSA context, $N$ has no small prime factor, thus the algorithm's $a$ at step 4 will remain small enough that $\gcd(a, N) = 1$ will hold.(If it did not, $a$ would be a factor of $N$ found by trial division; a trivial modification of the algorithm additionally handles $N$ with such small factors).

    For any valid RSA triple $(N, e, d)$, it holds that $(a^e)^d \bmod N = a$ for any integer $a \in [0, n)$. Thus for any $a$ used in the algorithm, $a^{ed - 1} \bmod N = 1$ holds. That is, $a^{f} = (a^t)^{2^s} \equiv 1 \pmod N$.

    For most $N$, step 4 will quickly find an $a$ with $a^t \not\equiv 1 \pmod N$. Because $N$ is square-free, by the Chinese Remainder Theorem, an $a$ coprime to $N$ is rejected iff $a^t \pmod p = 1$ for all primes $p \mid N$. Since $t$ is odd, if $a^t \pmod p = 1$ holds for $a$, then $\tilde{a}^t \pmod p = p - 1 \neq 1$ holds for $\tilde{a} = -a \pmod p$. Thus, for $a$ coprime to $N$ chosen randomly in some large interval, the probability of $a^t \equiv 1 \pmod N$ is at most $1/2$. That is independently for each $p$, thus $a^t \not\equiv 1 \pmod N$ has probability $\geqslant 1 - 2^{-m}$ where $m \geqslant 2$ is the number of factors of $N$. Using the consecutive primes $a$ (rather than random $a$) works well in practice for random instances of the problem.

    Before each iteration of step 5, it holds $1 < b < N$ with $i \geqslant 1$, and $b^{(2^i)} \equiv 1 \pmod N$. Thus, after at most $s - 1$ computations in step 5 we reach step 6 with $b \bmod N \neq 1$ and $b^2 \bmod N = 1$. 

    Step 6 excludes the case $b = N - 1$, which is rare in practice. 

    Thus at step 7, $\gcd(b - 1, N)$ is a nontrivial factor of $N$.