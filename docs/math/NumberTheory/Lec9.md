# Pell's equation

!!! question "Pell's equation"
    Find all integer solutions to $x^2 - dy^2 = n$($d$ is square free and $d \geqslant 2$).

First consider some special cases.

!!! question
    Is there a solution to $x^2 - dy^2 = 1$?

Observe that $x^2 - dy^2 = 1$ is equivalent to $(x + y\sqrt{d})(x - y\sqrt{d}) = 1$. So we can define the norm $N(\alpha) = (x + y \sqrt{d})(x - y \sqrt{d}) = x^2 - dy^2, \alpha = x + y\sqrt{d}$. So $N(\alpha \beta) = N(\alpha)N(\beta)$.

!!! info "Definition"
    We call $x^2-dy^2 = 1$ **Standard Pell's equation**, $x^2-dy^2 = -1$ **Negative Pell's equation** and $x^2-dy^2 = n$ **Generalized Pell's equation**.

## Standard Pell's equation

!!! note "Main Theorem"
    (Lagrange) Standard Pell's equation has a non-trivial solution.

!!! success "Lemma"
    There are infinitely many postitive integers $x, y$ such that 

    \[
        \lvert x - y\sqrt{d} \rvert < \frac{1}{y}.
    \]

    ??? success "Proof"
        $\{x\}$: decimal part of $x$. $\{x\} \in [0, 1)$.  
        Consider $0, \{\sqrt{d}\}, \{2\sqrt{d}\}, \cdots, \{m\sqrt{d}\}, \cdots$. ($m$ is large enough).  
        Use Pigeonhole principle: Devide $[0, 1)$ into $m$ intervals $[\frac{i}{m}, \frac{i+1}{m})$. So there exists $\{k\sqrt{d}\}, \{l\sqrt{d}\}$ falling in the same interval. So $\lvert \{k\sqrt{d}\} - \{l\sqrt{d}\} \rvert < \frac{1}{m}(0 \leqslant l < k \leqslant m)$. Which means $\lvert (k\sqrt{d} - [k\sqrt{d}]) - (l\sqrt{d} - [l\sqrt{d}]) \rvert < \frac{1}{m}$. Set $x = [k\sqrt{d}] - [l\sqrt{d}], y = k - l$. So $\lvert x - y\sqrt{d} \rvert < \frac{1}{m} \leqslant \frac{1}{k - l} = \frac{1}{y}$. Then we can use this to generate new $m$. So there are infinitely many $x, y$ satisfying the condition.

!!! success "Collary"
    $\exists M$ such that $x^2 - dy^2 = M$ has infinitely many solutions.

    ??? success "Proof"
        Find $(x_n, y_n)$, $\lvert x_n - y_n\sqrt{d} \rvert < \frac{1}{y_n}$.  
        So we have  
        (a) $x_n = x_n - y_n\sqrt{d} + y_n\sqrt{d} < \frac{1}{y_n} + y_n\sqrt{d}$.  
        (b) $\lvert x_n^2 - dy_n^2 \rvert = \lvert x_n - y_n\sqrt{d} \rvert \cdot \lvert x_n + y_n\sqrt{d} \rvert < \frac{1}{y_n}(\frac{1}{y_n} + 2y_n\sqrt{d}) < 1 + 2\sqrt{d}$.  
        So $\exists M >0$, such that $\lvert x^2 - dy^2 \rvert = M$ has infinitely many solutions.

??? note "Proof of Main Theorem"
    $\exists M, \lvert M \rvert < 1 + 2\sqrt{d}$, such that $x^2 - dy^2 = M$ has infinitely many solutions. So we have $x_1^2 - dy_1^2 = M, x_2^2 - dy_2^2 = M$.  
    By the fitness of $\mathbb{Z}/\lvert M \rvert \mathbb{Z} \times \mathbb{Z}/\lvert M \rvert \mathbb{Z}$, we assume that 

    \[
        \begin{gather}
            x_1 \equiv x_2 \pmod {\lvert M \rvert}, x_2 = x_1 + M \cdot k \\ y_1 \equiv y_2 \pmod{\lvert M \rvert}, y_2 = y_1 + M \cdot l
        \end{gather}
    \]

    So $x_2 + y_2\sqrt{d} = x_1 + y_1\sqrt{d} + (k + l\sqrt{d})M$. And $x_1^2 - dy_1^2 = M$. So $x_2 + y_2\sqrt{d} = (x_1 + y_1\sqrt{d})(1 + (k + l\sqrt{d})(x_1 - y_1\sqrt{d}))$. Set $\gamma = 1 + (k + l\sqrt{d})(x_1 - y_1\sqrt{d})$, then $x_2 + y_2\sqrt{d} = (x_1 + y_1\sqrt{d}) \cdot \gamma$. So $N(x_2 + y_2\sqrt{d}) = N(x_1 + y_1\sqrt{d}) \cdot N(\gamma) \Rightarrow M = M \cdot N(\gamma)$, $N(\gamma) = 1$. 

!!! note "Theorem"
    (i) $N(\gamma) = 1$ has a fundamental solution $\alpha$. Every other solution is equal to $\pm \alpha^k, k \in \mathbb{Z}$.  
    (ii)  The fundamental solution is the one with $y > 0$ and minimal.

!!! success "Lemma"
    $x^2 - dy^2 = a^2 - db^2 = 1$, $(x, y) \neq (a, b), x, y, a, b > 0$. The following statements are equivalent:  
    (i) $x+y\sqrt{d} > a+b\sqrt{d}$.  
    (ii) $x > a$ and $y > b$.  
    (iii) $x > a$ or $y > b$.

## Negative Pell's equation

!!! note "Theorem"
    Consider negative Pell's equation $x^2 - dy^2 = -1$($N(\gamma) = -1$). Assume $x^2 - dy^2 = -1$ has a solution.  
    (i) There exists a fundamental solution $\gamma_1 = x_1 + y_1\sqrt{d}$, $\gamma_1 > 1$ and is minimal.  
    (ii) $N(\gamma_1) = -1 \Rightarrow N(\gamma_1^2) = 1$. Then $\gamma_1$ is the fundamental solution of $x^2 - dy^2 = 1$.  
    (iii) Every solution of $x^2 - dy^2 = -1$ has the form $\gamma = \gamma_1^{2k+1}, k \in \mathbb{Z}$.

## Generalized Pell's equation

!!! note "Theorem"
    Let $u = a + b\sqrt{d}$ be the fundamental solution of the standard Pell's equation $a^2 - d \cdot b^2 = 1$. Then for each $n \in \mathbb{Z}, n \neq 0$, every solution of $x^2 - dy^2 = n$ has the form $x + y\sqrt{d} = (x' + y' \sqrt{d} \cdot u^k)$, where 

    \begin{gather} 
        \lvert x' \rvert \leqslant \dfrac{\sqrt{\lvert n \rvert}(\sqrt{u} + \sqrt{u}^{-1})}{2} \\
        \lvert y' \rvert \leqslant \dfrac{\sqrt{\lvert n \rvert}(\sqrt{u} + \sqrt{u}^{-1})}{2\sqrt{d}}
    \end{gather}

    We also have a more precise bound for $y'$:

    \[
        \lvert y' \rvert \leqslant \dfrac{\sqrt{\lvert n \rvert}(\sqrt{u} - \sqrt{u}^{-1})}{2\sqrt{d}}
    \]

    This allows us to find the solutions of $x^2 - dy^2 = n$ with fewer trials.
    