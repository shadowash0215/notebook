# Sum of Four Squares

!!! note "Theorem"
    (Lagrange) For any integer $n$, the equation $x^2+y^2+z^2+w^2 = n$ has a solution.

??? note "Proof"
    First prove that Lagrange is right for prime $p$.  


!!! info "Definition"
    (Hamiltonian Quaternion) $\mathbb{H} := \left\{\begin{pmatrix} a & b \\ -\bar{b} & \bar{a} \end{pmatrix} \mid a, b \in \mathbb{C} \right\}$

So for $x^2+y^2+z^2+w^2 = n$, define $\alpha = x+y\sqrt{-1}, \beta = z+w\sqrt{-1}$, $x^2+y^2+z^2+w^2 = \alpha \bar{\alpha} + \beta \bar{\beta} = n$. Define $\begin{pmatrix} \alpha & \beta \\ -\bar{\beta} & \bar{\alpha} \end{pmatrix} = A$. So we just solve the equation $N(A) = n$ in $\mathbb{H}.$

!!! example
    Express $310$ as a sum of four squares.  
    We can do this by expressing $10$ and $31$ as a sum of four squares. We know that $31 = 5^2 + 2^2 + 1^2 + 1^2$ and $10 = 3^2 + 1^2 + 0^2 + 0^2$. So we can write two matrices. 

    $$
        \alpha = \begin{pmatrix} 5 + 2\mathrm{i} & 1 + \mathrm{i} \\ -1 + \mathrm{i} & 5 - 2\mathrm{i} \end{pmatrix} \ \beta = \begin{pmatrix} 3 + \mathrm{i} & 0 \\ 0 & 3 - \mathrm{i} \end{pmatrix}. 
    $$

    So $N(\alpha) = 31, N(\beta) = 10$, and $N(\alpha \beta) = 310$. $\alpha \cdot \beta = \begin{pmatrix} 13 + 11\mathrm{i} & 4 + 2\mathrm{i} \\ -4 + 2\mathrm{i} & 13 - 11\mathrm{i} \end{pmatrix}$. So $310 = 13^2 + 11^2 + 4^2 + 2^2$. This is one of the solutions.