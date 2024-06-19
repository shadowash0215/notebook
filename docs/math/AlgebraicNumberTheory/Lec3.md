# Dedekind Domains

## Noetherian Rings and Modules

The Noetherian property arises from the ascending chain condition. The definition and description of the property can be stated as follows:

!!! info "Definition"
    Let $R$ be a unital commutative ring, and $M$ be an $R$-module. Then the following conditions are equivalent:  
    (1) Let $\Sigma$ be a subset of $M$, and $\Sigma' \subset \Sigma$, then $\Sigma'$ has a maximal element.  
    (2) For any ascending chain of submodules $M_1 \subset M_2 \subset \cdots$, there exists $n \in \mathbb{N}$ such that $\forall m \geqslant n, M_m = M_n$.  
    (3) Every submodule of $M$ is finitely generated.    
    $M$ is called a Noetherian module if any thus every of the above properties hold. $R$ is called a Noetherian ring if it is Noetherian as an $R$-module.

    ??? info "Proof"

        (2) $\Rightarrow$ (1) If $\Sigma'$ has no maximal element, then we can construct an ascending chain $M_1 \subset M_2 \subset \cdots$ that grows infinitely, which is a contradiction.  
        (1) $\Rightarrow$ (3) Let $N$ be a submodule of $M$, and $\Sigma$ be the set of all finitely generated submodules contained in $N$. Since $0 \in \Sigma$, $\Sigma$ is nonempty, and thus has a maximal element $N_0$. If $N \neq N_0$, then there exists $x \in N \setminus N_0$, consider the submodule $N_0 + Rx$, which is finitely generated and $N_0 \subsetneq N_0 + Rx \subsetneq N$, which is a contradiction. So $N = N_0$ is finitely generated.  
        (3) $\Rightarrow$ (2) Let $M_1 \subset M_2 \subset \cdots$ be an ascending chain of submodules of $M$, let $N = \bigcup_{i=1}^{\infty} M_i$, which is a submodule of $M$, so $N$ is finitely generated. Assume $N = Rx_1 + \cdots + Rx_r$, and $x_i \in M_{n_i}$. Let $n = \operatorname{max}\{n_1, \cdots, n_r\}$, then $\forall x_i \in N, x_i \in M_n$, so $N = M_n$, and $\forall m \geqslant n, M_m = M_n$.
 
The properties of Noetherian modules are also related to short exact sequences:

!!! info "Proposition"
    (1) Let $0 \to M' \to M \to M/M' \to 0$ be a short exact sequence of $R$-modules, then the following conditions are equivalent:  
        (i) $M'$ and $M/M'$ are both Noetherian modules.  
        (ii) $M$ is a Noetherian module.  
    (2) $\oplus_{i=1}^n M_i$ is a Noetherian module if and only if each $M_i$ is a Noetherian module.

!!! note "Hilbert's Basis Theorem"
    Let $R$ be a Noetherian ring, then $R[x_1, x_2, \ldots, x_n]$ is also a Noetherian ring.(The converse is evidently true as well.)

Note that $\mathcal{O}_{\mathbb{F}}$ is trivially Noetherian as an $\mathbb{Z}$-module. Thus we are wodering if $\mathcal{O}_{\mathbb{F}}$ is a Noetherian ring itself. 

!!! note "Theorem"
    
    Assume $A$ is an integrally closed integral domain and Noetherian. $\operatorname{char}(\mathbb{F}) = 0$. Consider $[\mathbb{E} : \mathbb{F}] = n$ a field extension, then $A^{\sharp} = S(\mathbb{E}, A)$ is finitely generated as $A$ module and is Noetherian.

    ??? note "Proof"
        (i) Recall that we have already shown that $A^{\sharp}$ is a submodule of a Noetherian $A$-module $A^n$ (In Lec2), so $A^{\sharp}$ is finitely generated. So $A^{\sharp} = A[\alpha_1, \ldots, \alpha_k]$.  
        (ii) Note that $A[x_1, \ldots, x_k]$ is Noetherian according to Hilbert's Basis Theorem. And we can map the polynomial ring to $A^{\sharp}$ by $x_i \mapsto \alpha_i$. According to its universal property, the map is unique and surjective. So $A^{\sharp}$ is Noetherian.

## Dedekind Domains

!!! info "Definition"
    A Dedekind domain $A$ is an integral domain that is Noetherian, integrally closed, with its all non-zero prime ideals being maximal.

!!! example
    Every field is a Dedekind domain. $\mathbb{Z}$ is also a Dedekind domain. Actually, every PID is a Dedekind domain.

!!! note "Theorem"
    Let $A$ be a Dedekind domain with quotient field $\mathbb{F}$ of characteristic $0$. Let $[\mathbb{E} : \mathbb{F}] = n$, then $A^{\sharp}$ is a Dedekind domain and finitely generated as an $A$-module.

    ??? note "Proof"
        The proposition above implies that $A^{\sharp}$ is Noetherian. Also we have shown that $A^{\sharp}$ is integrally closed. So we only need to show that every prime ideal of $A^{\sharp}$ is maximal. 

        Consider $0 \neq \mathfrak{p} \subset A^{\sharp}$ a prime ideal. We are to show that $\mathfrak{p}$ is maximal, i.e. $A^{\sharp}/\mathfrak{p}$ is a field. To utilize the property of Dedekind domain $A$, we shall construct the intermediate field $A/A \cap \mathfrak{p}$.

        TODO

## Factorization of Ideals in Dedekind Domain

We are to factorize ideals into product of prime ideals in a Dedekind domain. However, we are to ensure that the product is inside:

!!! info "Definition"
    For an integral domain $A$ with quotient field $\mathbb{F}$. A **fractional ideal** $I$ of $A$ is a $A$-submodule of $\mathbb{F}$ s.t. there exists $0 \neq d \in A$ such that $dI \subset A$. 

Note that $I \not \subset A$ in general. If it does, then we may call it an **integral ideal** of $A$. Set

\[
    A^{-1} I(A) = \{ \text{all fractional ideals of } A \}.
\]

For all $I_1, I_2 \in A^{-1} I(A)$, it is easy to see that $I_1 I_2, I_1 + I_2 \in A^{-1} I(A)$. Also, $0, A \in A^{-1} I(A)$. Thus $(A^{-1} I(A) \setminus \{0\}, \cdot)$ is at least a monoid with identity $A$. Actually it is a group in some cases.

!!! success "Lemma"
    Let $A$ be a Dedekind domain. Then for every prime ideal $0 \neq \mathfrak{p} \subset A$ is invertible in $A^{-1} I(A)$. i.e. there exists $\mathfrak{q} \in A^{-1} I(A)$ such that $\mathfrak{p} \mathfrak{q} = A$.

    ??? success "Proof"
        Take $\mathfrak{q} = \{ x \in \mathbb{F} \mid x \mathfrak{p} \subset A \} \subset \mathbb{F}$. Note that $\mathfrak{q}$ is an $A$-module and for any $b \in \mathfrak{p}$, $b \mathfrak{q} \subset A$. Thus $\mathfrak{q} \in A^{-1} I(A)$. By definition we have $\mathfrak{p} \mathfrak{q} \subset A$ and $A \subset \mathfrak{q}$. So $\mathfrak{p} = \mathfrak{p} A \subset \mathfrak{p} \mathfrak{q} \subset A$. 

        We are to show that $\mathfrak{p} \cdot \mathfrak{q} \supset A$. Suppose not, then