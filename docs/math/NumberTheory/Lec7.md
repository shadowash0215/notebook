# Sum of Four Squares

!!! note "Theorem"
    Let $p$ be a prime, for all $a \in \mathbb{Z}$, the equation $x^2 + y^2 \equiv a \pmod p$ has a solution.

    ??? note "Proof"
        If $p = 2$, it's obvious.  
        If $p$ is odd, then notice that there are $\frac{p+1}{2}$ quadratic residues and $\frac{p-1}{2}$ quadratic non-residues in $\mathbb{Z}/p\mathbb{Z}$. The set of quadratic residues is called $S$, $\lvert S \rvert = \frac{p + 1}{2}$. Set $S' = \{a - z \mid z \in S\}$, $\lvert S' \rvert = \frac{p + 1}{2}$. Then $\lvert S \rvert + \lvert S' \rvert = p + 1 > p$, which means $S \cap S' \neq \varnothing$. So there exists $x^2 \in S$, $a - y^2 \in S'$, such that $x^2 \equiv a - y^2 \pmod p$. So $x^2 + y^2 \equiv a \pmod p$.

!!! note "Theorem"
    (Lagrange) For any integer $n$, the equation $x^2+y^2+z^2+w^2 = n$ has a solution.

    ??? note "Proof"
        First prove that Lagrange is right for prime $p$.  


!!! info "Definition"
    (Hamiltonian Quaternion) $\mathbb{H} := \left\{\begin{pmatrix} a & b \\ -\bar{b} & \bar{a} \end{pmatrix} \mid a, b \in \mathbb{C} \right\}$

So for $x^2 + y^2 + z^2 + w^2 = n$, define $\alpha = x+y\sqrt{-1}, \beta = z+w\sqrt{-1}$, $x^2+y^2+z^2+w^2 = \alpha \bar{\alpha} + \beta \bar{\beta} = n$. Define $\begin{pmatrix} \alpha & \beta \\ -\bar{\beta} & \bar{\alpha} \end{pmatrix} = A$. So we just solve the equation $N(A) = n$ in $\mathbb{H}.$

!!! example
    Express $310$ as a sum of four squares.  
    We can do this by expressing $10$ and $31$ as a sum of four squares. We know that $31 = 5^2 + 2^2 + 1^2 + 1^2$ and $10 = 3^2 + 1^2 + 0^2 + 0^2$. So we can write two matrices. 

    \[
        \alpha = \begin{pmatrix} 5 + 2\mathrm{i} & 1 + \mathrm{i} \\ -1 + \mathrm{i} & 5 - 2\mathrm{i} \end{pmatrix} \ \beta = \begin{pmatrix} 3 + \mathrm{i} & 0 \\ 0 & 3 - \mathrm{i} \end{pmatrix}. 
    \]

    So $N(\alpha) = 31, N(\beta) = 10$, and $N(\alpha \beta) = 310$. $\alpha \cdot \beta = \begin{pmatrix} 13 + 11\mathrm{i} & 4 + 2\mathrm{i} \\ -4 + 2\mathrm{i} & 13 - 11\mathrm{i} \end{pmatrix}$. So $310 = 13^2 + 11^2 + 4^2 + 2^2$. This is one of the solutions.