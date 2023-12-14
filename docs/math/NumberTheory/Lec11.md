# Primes of Arithmetic Progression

!!! note "Theorem"
    Given an integer $N > 1$ and an integer a coprime to $N$, there exists infinitely many primes $p$ such that $p \equiv a \pmod N$.

!!! tip
    Recall: Proof of infinity of primes via $\zeta(s)$.  
    Recall: Legendre Symbol $\left(\frac{a}{p}\right)$.

    \[
        \left(\dfrac{a}{p}\right) = \begin{cases} 0 \enspace \textrm{if} \enspace a \equiv 0 \pmod p, \\ 1 \enspace \textrm{if} \enspace p \not \mid a, x^2 \equiv a \pmod p \enspace \textrm{has a solution}, \\ -1 \enspace \textrm{if} \enspace p \not \mid a, x^2 \equiv a \pmod p \enspace \textrm{has no solution}. \end{cases}
    \]

!!! info "Definition"
    (Dirichlet Character)  
    A Dirichlet character mod $N$ is a function $\chi: \mathbb{Z}/N\mathbb{Z} \rightarrow \{z \in \mathbb{C} \mid \lvert z \rvert = 1\} \cup \{0\}$ such that  
    (i) $\chi(a) = 0$ iff $(a, N) \neq 1$.  
    (ii) $\chi(ab) = \chi(a)\chi(b)$ for all $a, b \in \mathbb{Z}$.  
    If $\chi(a) = 1$ for all $(a, N) = 1$, then we say $\chi$ is trivial, denoted by $\chi_0$.  

!!! success "Lemma"

    \[
        \sum_{a = 0}^{N - 1} \chi(a) = \begin{cases} \varphi(N) \enspace \textrm{if} \enspace \chi = \chi_0, \\ 0 \enspace \textrm{if} \enspace \chi \neq \chi_0. \end{cases}
    \]

!!! success "Lemma"
    Define $C_N = \{\textrm{Dirichlet Character mod } N \}$, then $\lvert C_N \rvert = \varphi(N)$.

??? success "Proof"
    For $N = p$ prime.  

    \[
        \chi: (\mathbb{Z}/p\mathbb{Z})^{\times} \rightarrow \mathbb{C}, \chi(0) = 0.
    \] 

    Set the generator of ${\mathbb{Z}/p\mathbb{Z}}^{\times}$ to be $g$. Then $\chi(g^k) = \chi(g)^k$. So $\chi$ is uniquely decided by $\chi(g)$ and $\chi(1) = 1$. According to Fermat's Little Theorem, $g^{p-1} \equiv 1 \pmod p$. So $\chi(g)^{p-1} = 1$. So $\chi(g)$ is a $p - 1$-th root of unity. So $\chi(g) \in \{e^{\frac{k}{p-1}2\pi \mathrm{i}} \mid 0 \leqslant k \leqslant p-2\}$. So $\lvert C_p \rvert = p - 1 = \varphi(p)$.

!!! success "Lemma"
    Given $a \in (\mathbb{Z}/N\mathbb{Z})^{\times}, \exists \chi \in C_N$ such that $\chi(a) \neq 1$.

!!! success "Lemma"
    Given $a$ coprime to $N$, 

    \[
        \sum_{\chi \in C_N} \chi(a) = \begin{cases} \varphi(N) \enspace \textrm{if} \enspace a = 1, \\ 0 \enspace \textrm{if} \enspace a \neq 1. \end{cases}
    \]

!!! info "Definition"
    $L(s, \chi) = \sum_{n = 1}^{\infty} \dfrac{\chi(n)}{n^s}$ is called the Dirichlet $L$-function associated to $\chi$. $L(s, \chi) = \prod_{p \textrm{ prime}} \left(1 - \chi(p)p^{-s}\right)^{-1}$. 

Obsereve that $L(s, \chi_0) = \prod_{p \textrm{ prime}} \left(1 - \chi_0(p)p^{-s}\right)^{-1} = \prod_{p \textrm{ prime} \atop p \nmid N} \left(1 - p^{-s}\right)^{-1}$, while $\zeta(s) = \prod_{p \textrm{ prime}} \left(1 - p^{-s}\right)^{-1}$. So $L(s, \chi_0) \cdot \prod_{p \mid N} \left(1 - p^{-s}\right) = \zeta(s)$. And $\lim_{s \rightarrow 1^+} L(s, \chi_0) = \infty$. 

!!! success "Prop"
    $\lim_{s \rightarrow 1^+} (s - 1) \zeta(s)$ and $\lim_{s \rightarrow 1^+} (s - 1) L(s, \chi_0)$ both exist.  

??? success "Proof"
    \begin{align}
        \zeta(s) - \frac{1}{s - 1} & = \sum_{n = 1}^{+\infty} \frac{1}{n^s} - \int_{1}^{+\infty} \frac{1}{x^s} \mathrm{d}x \\ & = \sum_{n = 1}^{+\infty} \left(\frac{1}{n^s} - \int_{n}^{n + 1} \frac{1}{x^s} \mathrm{d}x \right) \\
        \frac{1}{n^s} - \int_{n}^{n + 1} \frac{1}{x^s} \mathrm{d}x & = \frac{1}{n^s} - \frac{1}{x_0^s}, x_0 \in (n, n + 1) \\ & = \frac{1}{n^s} \left(1 - \frac{1}{(x_0/n)^s}\right) \\ & = \frac{1}{n^s} \cdot s \xi^{-s - 1} \left(\frac{x_0}{n} - 1\right) \\ & \leqslant \frac{1}{n^s} \cdot s \cdot \frac{1}{n} \\ & = \frac{s}{n^{s + 1}}. 
    \end{align}

    So $\lim_{s \rightarrow 1^+} \left(\zeta(s) - \frac{1}{s - 1}\right) = \lim_{s \rightarrow 1^+} C(s)$, then $\lim_{s \rightarrow 1^+} ((s - 1) \zeta(s) - 1) = \lim_{s \rightarrow 1^+} (s - 1) C(s)$, where $C(s)$ is a convergent series. So $\lim_{s \rightarrow 1^+} (s - 1) \zeta(s)$ exists.

!!! success "Prop"
    $\lim_{s \rightarrow 1^+} L(s, \chi)$ exists if $\chi \neq \chi_0$.

!!! tip "Fact"
    $L'(s, \chi)$ exists.

!!! note "Formal Proof of Dirichlet's Theorem"
    \[
        L(s, \chi) = \prod_{p \textrm{ prime}} \left(1 - \chi(p)p^{-s}\right)^{-1},
    \]

    so

    \[
        \ln L(s, \chi) =  \sum_{p \textrm{ prime}} -\ln \left(1 - \chi(p)p^{-s}\right)
    \]

    Use Taylor expansion, $- \ln (1 - x) = \sum_{n = 1}^{+\infty} \frac{x^n}{n}$, so
    
    \[
        \ln L(s, \chi) = \sum_{p \textrm{ prime}} \sum_{m = 1}^{+\infty} \frac{\chi(p)^m}{mp^{ms}}.
    \]

    Then
    
    \[ 
        - \frac{L'(s, \chi)}{L(s, \chi)} = \sum_{p \textrm{ prime}} \sum_{m = 1}^{+\infty} \frac{\ln p}{\chi(p)^m p^{ms}} = \sum_{p \textrm{ prime}} \frac{\ln p}{\chi(p) p^s} + \sum_{p \textrm{ prime}} \sum_{m = 2}^{+\infty} \frac{\ln p}{\chi(p)^m p^{ms}}.
    \]

    \[
        - \chi(a) \frac{L'(s, \chi)}{L(s, \chi)} = \sum_{p \textrm{ prime}} \chi(a) \frac{\ln p}{\chi(p) p^s} + \sum_{p \textrm{ prime}} \sum_{m = 2}^{+\infty} \chi(a) \frac{\ln p}{\chi(p)^m p^{ms}}.
    \]

    Sum both sides over all the $\chi \in C_N$, we get
    
    \begin{align}
        \textrm{LHS} & = \sum_{\chi \in C_N} - \chi(a) \frac{L'(s, \chi)}{L(s, \chi)} \\
        \textrm{RHS} & = \sum_{\chi \in C_N} \sum_{p \textrm{ prime}} \chi(ap^{-1}) \frac{\ln p}{p^s} + \sum_{\chi \in C_N} \sum_{p \textrm{ prime}} \sum_{m = 2}^{+\infty} \chi(a) \frac{\ln p}{\chi(p)^m p^{ms}}. \\ & = \varphi(N) \sum_{p \equiv a \pmod N} \frac{\ln p}{p^s} + \sum_{\chi \in C_N} \sum_{p \textrm{ prime}} \sum_{m = 2}^{+\infty} \chi(a) \frac{\ln p}{\chi(p)^m p^{ms}}.
    \end{align}

    The second term on the RHS

    \[
        \sum_{\chi \in C_N} \sum_{p \textrm{ prime}} \sum_{m = 2}^{+\infty} \chi(a) \frac{\ln p}{\chi(p)^m p^{ms}} \leqslant \sum_{n = 2}^{+\infty} \frac{\ln n}{n^{2s}}(1 - \frac{1}{n^{-s}})^{-1} < +\infty
    \]

    \[
        \textrm{LHS} = - \frac{L'(s, \chi_0)}{L(s, \chi_0)} - \sum_{\chi \neq \chi_0} \chi(a) \frac{L'(s, \chi)}{L(s, \chi)}.
    \]

    It remains to prove $L(1, \chi) \neq 0$ when $\chi \neq \chi_0$.  
    Proof when $\chi^2 \neq \chi_0$.  
    If $L(1, \chi) = 0$, then it should have a form like $(s - 1) g(s)$.

    \begin{align}
        \lambda(s) & := L(s, \chi_0)^3 \cdot L(s, \chi)^4 \cdot L(s, \chi^2) \\ & = \prod_{p} \frac{1}{1 - p^{-s}} \cdot \prod_{p} (\frac{1}{1 - \chi(p)p^{-s}})^4 \cdot \prod_{p} \frac{1}{1 - \chi^2(p)p^{-s}} \\ & = \mathrm{exp}\left( \sum_{m, p} \frac{3 + 4 \chi(p)^m + \chi(p^{2m})}{m \cdot p^{ms}}\right)
    \end{align}

    \[
        \lvert \lambda(s) \rvert = \lvert \mathrm{exp}\left( \sum_{m, p} \frac{3 + 4 cos \theta_{m, p} + cos 2\theta_{m, p}}{m \cdot p^{ms}}\right) \rvert \Rightarrow \lambda(s) \neq 0 \Rightarrow \lim_{s \to 1^+} \lambda(s) \neq 0.
    \]

    Where $\theta_{m, p} = \arg \chi(p)^m$.

    Then 

    \[
        \lim_{s \to 1^+} \lambda(s) = \lim_{s \to 1^+} L(s, \chi_0)^3 \cdot L(s, \chi)^4 \cdot L(s, \chi^2) = \lim_{s \to 1^+} (\frac{1}{s - 1})^3 \cdot (s - 1)^4 \cdot L(s, \chi^2) = 0.
    \]

    Which is a contradiction.

    