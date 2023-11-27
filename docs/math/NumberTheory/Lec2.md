# Modular Arithmetic

## In $\mathbb{Z}$ 

**$\mathbb{Z}/n\mathbb{Z}$**: The set of integers $\bmod n$. And its unit set $\mathbb{Z}/n\mathbb{Z}^{\times} = \{a \in \mathbb{Z}/n\mathbb{Z} \mid a·b = 1$  for some $b \in \mathbb{Z}/n\mathbb{Z}\} = \{a \in \mathbb{Z}/n\mathbb{Z} \mid$ $a$ coprime to $n\}$.

**Euler phi-function**: $\phi_{\mathbb{Z}}(n) :=$ #$(\mathbb{Z}/n\mathbb{Z})^{\times}$

!!! note "Theorem"
    For $n = p_1^{l_1}\cdots p_r^{l_r}$, we have 
    $\phi_{\mathbb{Z}}(n) = \prod_{j = 1}^{r} p_j^{l_j - 1}(p_j - 1) = p_1^{l_1 - 1}(p_1 - 1)·p_2^{l_2 - 1}(p_2 - 1)\cdots p_r^{l_r - 1}(p_r - 1)$. 

!!! success "Lemma"
    1. If $p$ is a prime, then $\phi_{\mathbb{Z}}(p^l) = p^{l - 1}(p - 1)$.

    2. If $m, n$ are coprime, then $\phi_{\mathbb{Z}}(mn) = \phi_{\mathbb{Z}}(m)\phi_{\mathbb{Z}}(n)$.

??? note "Proof"
    2. Consider the map:

    $$
        f: \mathbb{Z}/mn\mathbb{Z} \rightarrow \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}, g \bmod {mn} \mapsto (g \bmod m, g \bmod n). 
    $$

!!! note "Theorem"
    (Euler Theorem)

## In $\mathbb{Z}[\sqrt{-1}]$

**Congruence**: $\alpha, \beta, \gamma \in \mathbf{Z}[\sqrt{-1}]$, say $\alpha \equiv \beta \pmod \gamma$ if $\gamma \mid \alpha - \beta$.  
If $\alpha \equiv \beta, \alpha' \equiv \beta' \pmod \gamma$, then $\alpha + \alpha' \equiv \beta + \beta' \pmod \gamma, \alpha · \alpha' \equiv \beta · \beta' \pmod \gamma$. 

**$\mathbb{Z}[\sqrt{-1}]/(\alpha)$**: $\mathbf{Z}[\sqrt{-1}]/\alpha \mathbf{Z}[\sqrt{-1}]$ for convinence.

!!! note "Theorem"
    (Fermat's little Theorem in $\mathbb{Z}[\sqrt{-1}]$) $p$ is a prime in $\mathbb{Z}[\sqrt{-1}]$, $n(p) :=$ # $\{$ Guassian integers \mod $p \}$. $\alpha \in \mathbb{Z}[\sqrt{-1}]$ coprime to $p$. Then 

    $$
        \alpha^{n(p)-1} \equiv 1 \pmod p.
    $$

??? note "Proof"
    Define $\beta_1, \ldots, \beta_r$: all representatives of Gaussian integers mod $p$, and let $\beta_r = 0$. Then we can prove that $\alpha \beta_1, \ldots, \alpha \beta_r$ are also representatives of Gaussian integers mod $p$

!!! note "Theorem"
    Define $n(\alpha) =$ # $\{$ Gaussian integers mod $\alpha \}$. If $\alpha \neq 0$, then $N(\alpha) = n(\alpha) = \alpha \cdot \overline{\alpha}$.

!!! success "Lemma"
    1. If $m \in \mathbb{Z}$, then $n(m) = N(m) = m^2$;  
    2. $n(\alpha) = n(\overline{\alpha})$;
    3. $n(\alpha \beta) = n(\alpha) \cdot n(\beta)$.

??? success "Proof"
    We need to find a bijection $f: \mathbb{Z}[\sqrt{-1}]/\alpha \beta \rightarrow \mathbb{Z}[\sqrt{-1}]/\alpha \times \mathbb{Z}[\sqrt{-1}]/\beta$.  
    Let $\mathbb{Z}[\sqrt{-1}]/\alpha = \{x_1, x_2, \ldots, x_r\}$, $\mathbb{Z}[\sqrt{-1}]/\beta = \{y_1, y_2, \ldots, y_s\}$. $\forall z \in \mathbb{Z}[\sqrt{-1}], \exists ! x_j$ such that $z \equiv x_j \pmod \alpha$. Write $z - x_j = \alpha \cdot t$. Then $\exists ! y_l$ such that $t \equiv y_l \pmod \beta$.

??? note "Proof"
    We only need to prove that $N^2(\alpha) = n^2(\alpha)$ because $N(\alpha)$ and $n(\alpha) \in \mathbb{N}$.  
    $n^2(\alpha) = n(\alpha) \cdot n(\overline{\alpha}) = n(\alpha \cdot \overline{\alpha}) = N(\alpha \cdot \overline{\alpha}) = N(\alpha) \cdot N(\overline{\alpha}) = N^2(\alpha)$. So $N(\alpha) = n(\alpha)$.

Define Euler phi-function in $\mathbb{Z}[\sqrt{-1}]$: $\phi_{\mathbb{Z}[\sqrt{-1}]}(\alpha) :=$ #$(\mathbb{Z}[\sqrt{-1}]/\alpha)^{\times}$.

!!! success "Lemma"
    1. If $p$ is a prime, then $\phi_{\mathbb{Z}[\sqrt{-1}]}(p^l) = N(p)^{l-1}(N(p)-1)$  
    
    2. If $\alpha, \beta$ are coprime, then $\phi_{\mathbb{Z}[\sqrt{-1}]}(\alpha \beta) = \phi_{\mathbb{Z}[\sqrt{-1}]}(\alpha)\phi_{\mathbb{Z}[\sqrt{-1}]}(\beta)$

!!! note "Theorem"
    (Euler Theorem in $\mathbb{Z}[\sqrt{-1}]$)