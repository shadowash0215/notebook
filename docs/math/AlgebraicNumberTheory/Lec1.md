# Algebraic Integers

Consider $\mathbb{Z} \hookrightarrow \mathbb{Q} \hookrightarrow \mathbb{F}$ as a field extension with $n = [\mathbb{F} : \mathbb{Q}] = \operatorname{dim}_{\mathbb{Q}} \mathbb{F} < \infty$. The question is that, do we have $\mathbb{Z} \subset \mathcal{O}_{\mathbb{F}} \subset \mathbb{F}$ such that:

1. $\mathbb{F}$ is a field of fractions of $\mathcal{O}_{\mathbb{F}}$.  
2. $\mathcal{O}_{\mathbb{F}}$ is a ring such that $\mathbb{Z} \subset \mathcal{O}_{\mathbb{F}}$.  
3. $\mathcal{O}_{\mathbb{F}}$ is a free module over $\mathbb{Z}$ isomorphic to $\mathbb{Z}^n$.

i.e. to ﬁnd the bottom-left question mark on the following diagram: 

\tikzcd
    \mathbb{Z} \arrow[r, hook] \arrow[d, hook] & \mathbb{Q} \arrow[d, hook] \\
    ? \arrow[r, hook] & \mathbb{F}

Due to the simplicity of the structure of $\mathbb{Z}$, the third requirement is simply determining the ring structure of $\mathcal{O}_{\mathbb{F}}$ in an easier way.

## Integrality & Algebraicity

Note that $\mathbb{Z} = \{x \in \mathbb{Q} \mid x - a = 0, a \in \mathbb{Z}\}$, we can define a similar concept:

\[
    \{\alpha \in \mathbb{F} \mid f(\alpha) = 0, f \text{ is a monic polynomial with degree } n, f(x) \in \mathbb{Z}[x]\}
\]

!!! note "Theorem"
    Let $R$ be a unital commutative ring and $A \subset R$ a subring. Take $x \in R$, then the following are equivalent:

    - There exists $a_0, a_1, \ldots, a_{n-1} \in A$ such that $x^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0 = 0$;  
    - The ring $A[x]$ is a finitely generated $A$-module;  
    - There is a subring $B \subset R$ such that $A[x] \subset B \subset R$ and $B$ is a finitely generated.

    ??? note "Proof"
        $1 \Rightarrow 2 \Rightarrow 3$: Trivial.  
        $3 \Rightarrow 1$: By $3$, we have

        \[
            B = Ay_1 + Ay_2 + \cdots + Ay_n
        \]

        Hence

        \[
            x_iy_i
        \]