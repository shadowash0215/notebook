# Sum of Two Squares

!!! note "Theorem"
    (The primes in $\mathbb{Z}[\sqrt{-1}]$)  
    (i) 2 is a prime in $\mathbb{Z}$, $2 = (1+\sqrt{-1})^2 \cdot (-\sqrt{-1})$.  
    (ii) If $p \equiv 3 \pmod 4$ is a prime in $\mathbb{Z}$, then $p$ stays as a prime in $\mathbb{Z}[\sqrt{-1}]$.  
    (iii) If $p \equiv 1 \pmod 4$ is a prime in $\mathbb{Z}$, then $p = \mathcal{p} \cdot \bar{\mathcal{p}}$, $\mathcal{p}$ and $\bar{\mathcal{p}}$ are primes in $\mathbb{Z}[\sqrt{-1}]$.  
    (iv) All primes in $\mathbb{Z}[\sqrt{-1}]$ are listed above.

!!! success "Lemma"
    (i) If $p$ is a prime in $\mathbb{Z}[\sqrt{-1}]$, but $p \not \in \mathbb{Z}, p \not \in i\mathbb{Z}$. Then $N(p)$ is a prime congruent to $1 \bmod 4$ or $N(p) = 2$.

    (ii) If $p \neq 2, p \in \mathbb{Z}$. Then $p$ is a prime $\mathbb{Z}[\sqrt{-1}]$ iff $p \equiv 3 \pmod 4$.

??? success "Proof"
    (i) $N(p) = p \cdot \bar{p} \in \mathbb{Z}$. According to the factorization in $\mathbb{Z}$, we have $N(p) = p_1^{r_1}p_2^{r_2}\cdots p_k^{r_k}$. So $p \mid p_1^{r_1}p_2^{r_2}\cdots p_k^{r_k}$ in $\mathbb{Z}[\sqrt{-1}]$.  
    Without loss of generality, $p \mid p_1$, then we have $p_1 = p \cdot \alpha, \alpha \in \mathbb{Z}[\sqrt{-1}]$. $p_1^2 = N(p_1) = N(p) \cdot N(\alpha)$, $N(p) \neq p_1^2$ because $p \not \in \mathbb{Z}, p \not \in i\mathbb{Z}$. So $N(p) = p_1$. $\alpha = \dfrac{p_1}{p} = \dfrac{p_1 \cdot \bar{p}}{p \cdot \bar{p}} = \bar{p}$, which means $p_1 = p \cdot \bar{p}$. $p_1 = p \cdot \bar{p}$, $N(p) = p \cdot \bar{p} = p_1$.  
    Let $p = x+y\sqrt{-1}$. If $N(p) = 2$, it's true. If $N(p) \neq 2$, then $p_1 = x^2+y^2$, $p_1 = N(p) \equiv 1 \pmod 4$.

    (ii) If $p \equiv 1 \pmod 4$, then $p = x^2+y^2$ has a solution $p = (x+y\sqrt{-1})(x-y\sqrt{-1})$.  
    It remains to prove that $p \equiv 3 \pmod 4 \Rightarrow p$ is a prime in $\mathbb{Z}[\sqrt{-1}]$. If $p$ were not a prime, then $p = \alpha \cdot \beta$ for some $\alpha, \beta \not \in (\mathbb{Z}[\sqrt{-1}])^{\times}$. Then $p^2 = N(p) = N(\alpha)N(\beta)$, $N(\alpha) = p$, $\beta = \bar{\alpha}$, $p = x^2+y^2$. Contradiction!

!!! note "Theorem"
    $n = p_1^{r_1}\cdots p_k^{r_k}$(unique factorization in $\mathbb{Z}$). Then $x^2+y^2 = n$ has a solution iff $r_j$ is even whenever $p_j \equiv 3 \pmod 4$.

!!! success "Lemma"
    If $x_1^2+y_1^2 = n_1, x_2^2+y_2^2 = n_2$, then $(x_1x_2+y_1y_2)^2+(x_1y_2-x_2y_1)^2 = n_1n_2$.

??? note "Proof"
    $(\Leftarrow)$ If $r_j$ is even whenever $p_j \equiv 3 \pmod 4$, then $x^2+y^2 = n$ has a solution by previons lemma.  
    $(\Rightarrow)$ If $x^2+y^2 = n$ has a solution $(x_0, y_0)$, $p_j \equiv 3 \pmod 4$. We need to prove $r_j$ is even. $p_j \mid n = (x_0+y_0\sqrt{-1})(x_0-y_0\sqrt{-1})$. Recall that $p_j \equiv 3 \pmod 4 \Rightarrow p_j$ is a prime in $\mathbb{Z}[\sqrt{-1}]$. $p_j \mid x_0+y_0\sqrt{-1} \Rightarrow p_j \mid x_0, p_j \mid y_0$. Then $p_j^2 \mid n$, which means $x^2+y^2 = \dfrac{n}{p_j^2}$ has a solution $(\dfrac{x_0}{p_j}, \dfrac{y_0}{p_j})$.  
    Prood by induction. Induction hypothesis: For all integer $k < n$, if $x^2+y^2 = k$ has a solution, then $r_j \equiv 0 \pmod 2$ whenever $p_j \equiv 3 \pmod 4$. By induction hypothesis, the exponent of $p_j$ in the factorization of $\dfrac{n}{p_j^2}$ is even. Then the exponent of $p_j$ in the factorization of $n$ is even.

!!! success "Lemma"
    $x^2+y^2 = n$ has a solution $\alpha = x_0+y_0\sqrt{-1}$. Then in $\alpha, -\alpha, \sqrt{-1}\alpha, -\sqrt{-1}\alpha$, there exists a unique solution such that real part $> 0$, imaginary part $\geqslant 0$.

