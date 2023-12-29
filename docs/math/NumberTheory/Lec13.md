# Congruent Number

!!! question
    For which $n$, is there an $x \in \mathbb{N}$ such that $x^2, x^2 \pm n$ are all squares?

!!! info "Definition"
    A positive integer $n$ is called a **congruent number** if there exists an triangle with rational sides and area $n$.

!!! note "Theorem"
    (i) $53$ is a congruent number.  
    (ii) $1$ is not a congruent number.

!!! note "Theorem"
    There is an one-to-one correspondence between $\{(a, b, c) \mid a^2 + b^2 = c^2, n = \dfrac{1}{2}ab\}$ and $\{(r, s, t) \mid s^2 -r^2 = t^2 - s^2 = n\}$, $(a, b, c) \mapsto (r, s, t) = (\dfrac{b - a}{2}, \dfrac{c}{2}, \dfrac{b + a}{2})$.

Consider a particular elliptic curve $E_n: y^2 = x^3 - n^2x = x(x - n)(x + n)$.

!!! note "Theorem"
    There exists an one-to-one correspondence between $\{(a, b, c) \mid a^2 + b^2 = c^2, n = \dfrac{1}{2}ab\}$ and $\{(x, y) \in \mathbb{Q}^2 \mid y^2 = x^3 - n^2x, y \neq 0\}$, $(a, b, c) \mapsto (x, y) = (\dfrac{nb}{c-a}, \dfrac{2n^2}{c-a})$, $(x, y) \mapsto (a, b, c) = (\dfrac{x^2 - n^2}{y}, \dfrac{2nx}{y}, \dfrac{x^2 + n^2}{y})$. 

!!! note "Theorem"
    (Mordell) We only need finitely rational solutions to $y^2 = x^3 - n^2x$ to generate all rational solutions.

!!! note "Weak BSD"
    The following conditions are equivalent:  
    (i) $y^2 = x^3 - n^2x$ has infinitely many rational solutions.  
    (ii) $\prod_{p \leqslant x} \dfrac{N_p}{p} \to +\infty$ as $x \to +\infty$. ($N_p := \text{#} \{(x, y) \in (\mathbb{Z}/p\mathbb{Z})^2 \mid y^2 = x^3 - n^2x \pmod p\} + 1$)  
    (iii) $n$ is a congruent number.

!!! note "Theorem"
    (Tunnell, 1983) Define 
    
    \begin{gather}
        f(n) = \text{#} \{(x, y, z) \in \mathbb{Z}^3 \mid x^2 + 2y^2 + 8z^2 = n\} \\
        g(n) = \text{#} \{(x, y, z) \in \mathbb{Z}^3 \mid x^2 + 2y^2 + 32z^2 = n\} \\
        h(n) = \text{#} \{(x, y, z) \in \mathbb{Z}^3 \mid x^2 + 4y^2 + 8z^2 = \dfrac{n}{2}\} \\
        k(n) = \text{#} \{(x, y, z) \in \mathbb{Z}^3 \mid x^2 + 4y^2 + 32z^2 = \dfrac{n}{2}\}
    \end{gather}

    (i) $n$ odd, congruent number $\Rightarrow$ $f(n) = 2g(n)$.  
    (ii) $n$ even, congruent number $\Rightarrow$ $h(n) = 2k(n)$.  
    (iii) Under Weak BSD, $n$ odd, $f(n) = 2g(n) \Rightarrow$ $n$ is a congruent number.  
    (iv) Under Weak BSD, $n$ even, $h(n) = 2k(n) \Rightarrow$ $n$ is a congruent number.

!!! example  
    (i) $f(1) = g(1) = 2 \Rightarrow 1$ is not a congruent number.  
    (ii) $h(2) = k(2) = 2 \Rightarrow 2$ is not a congruent number.  
    (iii) $f(5) = g(5) = 0 \Rightarrow 5$ is a congruent number.  
    (iv) Under Weak BSD, if $n$ is square free and $n \equiv 5, 6, 7 \pmod 8$, then $n$ is a congruent number.

## Appendix

??? note "Proof of $1$ is not a congruent number"
    Assume $a^2 + b^2 = c^2, \dfrac{1}{2}ab = d^2$, $a, b, c, d$ are all positive integer. $ab = 2d^2 \Rightarrow \begin{cases} a = 2k^2 \\ b = l^2 \end{cases} (a \text{ even, } b \text{ odd})$. We may assume that $a$ even, $b$ odd, $c$ odd.  
    Aim to construct a "smaller" solution.  
    $a^2 + b^2 = c^2 \Rightarrow 4k^4 + b^2 = c^2 \Rightarrow \dfrac{c + b}{2} \dfrac{c - b}{2} = k^4$, and they are coprime. Let $\dfrac{c + b}{2} = r^4$, $\dfrac{c - b}{2} = s^4$, which means $k = rs$. So $b^2 = r^4 - s^4 = l^2$, $c = r^4 + s^4$. $(r^2 - s^2)(r^2 + s^2) = l^2$, and they are coprime, so let $r^2 = 