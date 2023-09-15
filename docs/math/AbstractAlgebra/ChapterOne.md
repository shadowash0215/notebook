# Chapter I Groups

## Semigroups, Monoids and Groups

**Definition 1.1.** 

**Semigroup**: A nonempty set $G$ together with a binary operation on $G$ which is 

(i) associative: $a(bc) = (ab)c$ for all $a, b, c \in G$. （结合律） 

**Monoid**: A semigroup $G$ which contains a 

(ii) (two-sided) identity element $e \in G$ such that $ae = ea = a$ for all $a \in G$. （幺元） 

**Group**: A monoid $G$ such that 

(iii) for every $a \in G$ there exists a (two-sided) inverse element $a^{-1} \in G$ such that $a^{-1}a = aa^{-1} = e$. （逆元）

A semigroup $G$ is said to be **abelian** or **commutative** if its binary operation is 

(iv) commutative: $ab = ba$ for all $a,b \in G$. （交换律）

**Order**: The cardinal number $\lvert G \rvert$.  

**Theorem 1.2.** (I) If $G$ is a monoid, then the identity element $e$ is unique.

(II) If $G$ is a group, then

(i) $c \in G$ and $cc = c \Rightarrow c = e$;

(ii) for all $a, b, c \in G$, $ab = ac \Rightarrow b = c$ and $ba = ca \Rightarrow b = c$ (left and right cancellation);

(iii) for each $a \in G$, the inverse element $a^{-1}$ is unique;

(iv) for each $a \in G$, $(a^{-1})^{-1} = a$;

(v) for $a, b \in G$, $(ab)^{-1} = b^{-1}a^{-1}$;

(vi) for $a, b \in G$ the equations $ax = b$ and $ya = b$ have unique solutions in $G$: $x = a^{-1}b$ and $y = ba^{-1}$.

**Proposition 1.3.** Let $G$ be a semigroup. Then $G$ is a group if and only if the following conditions hold:

(i) there exists an element $e \in G$ such that $ea = a$ for all $a \in G$ (left identity element);

(ii) for each $a \in G$, there exists an element $a^{-1} \in G$ such that $a^{-1}a = e$ (left inverse). 

**Remark**: An analogous result holds for "right inverses" and a "right identity." 

**Proposition 1.4.**  Let $G$ he a semigroup. Then $G$ is a group if and only if for all $a, b \in G$ the equations $ax = b$ and $ya = b$ have solutions in $G$.

**Direct product**: $G, H$ are two groups with identities $e_G, e_H$ respectively. Their direct product is the group whose underlying set is $G \times H$ and whose binary operation is given by:

$$
(a, b)(a', b') = (aa', bb'), \enspace where \enspace a, a' \in G; b, b' \in H.
$$

**Theorem 1.5.** Let $\mathbf{R}$(~) be an equivalence relation on a monoid $G$ such that $a_1$ ~ $a_2$ and $b_1$ ~ $b_2$ imply $a_1b_1$ ~ $a_2b_2$ for all $a_i,b_i \in G$. Then the set $\mathbf{G/R}$ of all equivalence classes of $G$ under $R$ is a monoid under the binary operation defined by $(\overline{a})(\overline{b}) = \overline{ab}$, where $\overline{x}$ denotes the equivalence class of $x \in G$. If $G$ is an (abelian) group, then so is $\mathbf{G/R}$.

An equivalence relation on a monoid $G$ that satisfies the hypothesis of the theorem is called a **congruence relation** on $G$.

**The (additive) group of integers modulo $m$**: $\mathbf{Z}_m = \{\overline{0}, \overline{1}, \ldots, \overline{m - 1}\}$. A commutative monoid, and $\mathbf{Q/Z}$ is called the group of rationals modulo one. 

**Meaningful product of $a_1, \ldots, a_n$**: If $n = 1$, the only meaningful product is $a_1$; else a meaningful product is defined to be any product 
of the form $(a_1\ldots a_m)(a_{m + 1}\ldots a_n)$ where $m < n$ and $(a_1\ldots a_m)$ and $(a_{m + 1}\ldots a_n)$ are meaningful products of $m$ and $n - m$ elements respectively.

**Standard n product** $\prod_{i = 1}^n a_i$ of $a_1, \ldots, a_n$:

$$
\prod_{i = 1}^1 a_i = a_1; \enspace and \enspace for \enspace n > 1, \prod_{i = 1}^n a_i = \left(\prod_{i = 1}^{n - 1} a_i\right)a_n.
$$

**Theorem 1.6.** (Generalized Associative Law) If $G$ is a semigroup and $a_1, \ldots,a_n \in G$, then any two meaningful products of $a_1, \ldots,a_n$ in this order are equal. 

**Corollary 1.7.** (Generalized Commutative Law) If $G$ is a commutative semigroup and $a_1, \ldots,a_n \in G$, then for any permutation $i_1, \ldots , i_n$ of $1, \ldots ,n$, $a_1a_2\cdots a_n = a_{i_1}a_{i_2}\cdots a_{i_n}$.

**Definition 1.8.** Let $G$ be a semigroup, $a \in G$ and $n \in N^*$. 

The element $a^n \in G$ is defined to be the standard $n$ product $\prod_{i = 1}^n a_i$ with $a_i = a$ for $1 \leqslant i \leqslant n$; 

If $G$ is a monoid, $a^0$ is defined to be the identity element e;

If $G$ is a group, then for each $n \in N^*$, $a^{-n}$ is defined to be $(a^{-1})^n \in G$. 

**Theorem 1.9.** If $G$ is a group (resp. semigroup. monoid) and $a \in G$, then for all $m, n \in Z$ (resp. $N^*, N$): 

(i) $a^m a^n = a^{m+n}$ (additive notation: $ma + na = (m + n)a$); 

(ii) $(a^m)^n = a^{mn}$ (additive notation: $n(ma) = mna$). 

## Homomorphisms and Subgroups

Definition 2.1. Let $G$ and $H$ be semigroups. A function $f: G \rightarrow H$ is a **homomorphism**（同态） provided

$$
f(ab) = f(a)f(b) \enspace for \enspace all \enspace a, b \in G.  
$$

If $f$ is injective as a map of sets, $f$ is said to be a **monomorphism**（单态）. If $f$ is surjective, $f$ is called an **epimorphism**（满态）. If $f$ is bijective, $f$ is called an **isomorphism**（同构）. In this case $G$ and $H$ are said to be **isomorphic** (written $G \cong H$). A homomorphism $f: G \rightarrow G$ is called an **endomorphism**（自同态）of $G$ and an isomorphism $f: G \rightarrow G$ is called an **automorphism**（自同构）of $G$.

**Definition 2.2.** Let $f: G \rightarrow H$ be a homomorphism of groups. The **kernel** of $f$ (denoted $\mathrm{Ker} f$) is $\{a \in G \enspace | \enspace f(a) = e \in H\}. If $A$ is a subset of $G$, then $f(A) = \{b \in H \enspace | \enspace b = f(a) \enspace for \enspace some \enspace a \in A \}$ is the **image** of $A$. $f(G)$ is called the image of $f$ and denoted $\mathrm{Im} f$. If $B$ is a subset of $H$, $f^{-1}(B) = \{a \in G \enspace | \enspace f(a) \in B\}$ is the **inverse image** of $B$.

**Theorem 2.3.** Let $f: G \rightarrow H$ be a homomorphism of groups. Then

(i) $f$ is a monomorphism if and only if $\mathrm{Ker} f = \{e\}$;

(ii) $f$ is an isomorphism if and only if there is a homomorphism $f^{-1} : H \rightarrow G$ such that $ff^{-1} = 1_H$ and $f^{-1}f = 1_G$.

**Definition 2.4.** Let $G$ be a group and $H$ a nonempty subset that is closed under the product in $G$. If $H$ is itself a group under the product in $G$, then $H$ is said to be a subgroup of $G$. This is denoted by $H < G$.

**Proper Subgroup**: A subgroup $H$ such that $H \neq G$, $H \neq \langle e \rangle$.

**Theorem 2.5.** Let $H$ be a nonempty subset of a group $G$. Then $H$ is a subgroup of $G$ if and only if $ab^{-1} \in H$ for all $a,b \in H$.

**Corollary 2.6.** If $G$ is a group and $\{H_i \enspace | \enspace  i \in I \}$ is a nonempty family of subgroups, then $\cap_{i \in I} H_i$ is a subgroup of $G$.

**Definition 2.7.** Let $G$ be a group and $X$ a subset of $G$. Let $\{H_i \enspace | \enspace  i \in I \}$ be the family of all subgroups of $G$ which contain $X$. Then $\cap_{i \in I} H_i$ is called the **subgroup of $G$ generated by the set** $X$ and denoted $\langle X \rangle$. 

$\langle a \rangle$: **Cyclic (sub)group** generated by $a$.

**Theorem 2.8.** If $G$ is a group and $X$ is a nonempty subset of $G$, then the subgroup $\langle X \rangle$ generated by $X$ consists of all finite products $a_1^{n_1}a_2^{n_2}\cdots a_t^{n_t} (a_i \in X; n_i \in Z)$. In particular for every $a \in G$, $\langle a \rangle = \{a^n \enspace | \enspace n \in Z\}$.

$\langle \cap_{i \in I} H_i \rangle$: The **(sub)group generated by the groups** $\{H_i \enspace | \enspace i \in I\}$.

## Cyclic Groups

**Theorem 3.1.** Every subgroup $H$ of the additive group $Z$ is cyclic. Either $H = \langle 0 \rangle$ or $H = \langle m \rangle$, where $m$ is the least positive integer in $H$. If $H \neq \langle 0 \rangle$, then $H$ is infinite.

**Theorem 3.2.** Every infinite cyclic group is isomorphic to the additive group $Z$ and every finite cyclic group of order $m$ is isomorphic to the additive group $Z_m$.

**Definition 3.3.** Let $G$ be a group and $a \in G$. The **order of $a$** is the order of the cyclic subgroup $\langle a \rangle$ and is denoted $\lvert a \rvert$.

**Theorem 3.4.** Let $G$ be a group and $a \in G$. If $a$ has infinite order, then 

(i) $a^k = e$ if and only if $k = 0$;

(ii) the elements $a^k (k \in Z)$ are all distinct. 

If $a$ has finite order $m > 0$, then

(iii) $m$ is the least positive integer such that $a^m = e$;

(iv) $a^k = e$ if and only if $m \mid k$;

(v) $a^r = a^s$ if and only if $r \equiv s \pmod m$; 

(vi) $\langle a \rangle$ consists of the distinct elements $a,a^2, \ldots , a^{m - 1},a^m = e$;

(vii) for each $k$ such that $k \mid m$, $\lvert a^k \rvert = m/k$.

**Theorem 3.5.** Every homomorphic image and every subgroup of a cyclic group $G$ is cyclic. In particular, if $H$ is a nontrivial subgroup of $G = \langle a \rangle$ and $m$ is the least positive integer such that $a^m \in H$, then $H = \langle a^m \rangle$.

**Theorem 3.6.** Let $G = \langle a \rangle$ be a cyclic group. If $G$ is infinite, then $a$ and $a^{-1}$ are the only generators of $G$.If $G$ is finite of order $m$, then $a^k$ is a generator of $G$ if and only if $(k,m) = 1$.

## Cosets and Counting

**Definition 4.1.** Let $H$ be a subgroup of a group $G$ and $a,b \in G$. $a$ is **right congruent** to $b$ **modulo $H$**, denoted $a \equiv_r b \pmod H$ if $ab^{-1} \in H$. $a$ is **left congruent** to $b$ **modulo $H$**, denoted $a \equiv_l b \pmod H$ , if $a^{-1}b \in H$.

**Theorem 4.2.** Let $H$ be a subgroup of a group $G$.

(i) Right (resp. left) congruence modulo $H$ is an equivalence relation on $G$.

(ii) The equivalence class of $a \in G$ under right (resp. left) congruence modulo $H$ is the set $Ha = \{ha \enspace | \enspace h \in H\}$ (resp. $aH = \{ah \enspace | \enspace h \in H\}$).

(iii) $\lvert Ha \rvert$ = $\lvert H \rvert$ = $\lvert aH \rvert$ for all $a \in G$.

The set $Ha$ is called a **right coset** of $H$ in $G$ and $aH$ is called a **left coset** of $H$ in $G$.

**Corollary 4.3.** Let $H$ be a subgroup of a group $G$.

(i) $G$ is the union of the right (resp. left) cosets of $H$ in $G$.

(ii) Two right (resp. left) cosets of $H$ in $G$ are either disjoint or equal. 

(iii) For all $a,b \in G$, $Ha = Hb \Leftrightarrow  ab^{-1} \in H$ and $aH = bH \Leftrightarrow a^{-1}b \in H$.

(iv) If $\mathfrak{R}$ is the set of distinct right cosets of $H$ in $G$ and $\mathfrak{L}$ is the set of distinct left 
cosets of $H$ in $G$, then $\lvert \mathfrak{R} \rvert = \lvert \mathfrak{L} \rvert$.

**Definition 4.4.** Let $H$ be a subgroup of a group $G$. The **index** of $H$ in $G$, denoted $[G:H]$, is the cardinal number of the set of distinct right (resp.left) cosets of $H$ in $G$.

**Theorem 4.5.** If $K,H,G$ are groups with $K < H < G$, then $[G:K] = [G:H][H:K]$. If any two of these indices are finite, then so is the third.

**Corollary 4.6.** (Lagrange). If $H$ is a subgroup of a group $G$, then $\lvert G \rvert = [G:H]\lvert H \rvert$. In particular if $G$ is finite, the order $\lvert a \rvert$ of $a \in G$ divides $\lvert G \rvert$.

**Theorem 4.7.** Let $H$ and $K$ be finite subgroups of a group $G$. Then $\lvert HK \rvert = \lvert H \rvert \lvert K \rvert / \lvert H \cap K \rvert$.

**Proposition 4.8.** If $H$ and $K$ are subgroups of a group $G$, then $[H:H \cap K] \leqslant [G:K]$. If $[G:K]$ is finite, then $[H:H \cap K] = [G:K]$ if and only if $G = KH$.

**Proposition 4.9.** Let $H$ and $K$ be subgroups of finite index of a group $G$. Then $[G:H \cap K]$ is finite and $[G:H \cap K] \leqslant [G:H][G:K]$. Furthermore, $[G:H \cap K] = [G:H][G:K]$ if and only if $G = HK$.

## Normality, Quotient Groups and Homomorphisms

**Theorem 5.1.** If $N$ is a subgroup of a group $G$, then the following conditions are eqUivalent.

(i) Left and right congruence modulo $N$ coincide (that is, define the same equivalence relation on $G$);

(ii) every left coset of $N$ in $G$ is a right coset of $N$ in $G$;

(iii) $aN = Na$ for all $a \in G$;

(iv) for all $a \in G$, $aNa^{-1} \in N$, where $aNa^{-1} = \{ana^{-1} \enspace | \enspace n \in N\}$;

(v) for all $a \in G$, $aNa^{-1} = N$.

**Definition 5.2.** A subgroup $N$ of a group $G$ which satisfies the equivalent conditions of Theorem 5.1 is said to be **normal** in $G$ (or a **normal subgroup** of $G$); we write $N \triangleleft G$ if $N$ is normal in $G$.

**Theorem 5.3.** Let $K$ and $N$ be subgroups of a group $G$ with $N$ normal in $G$. Then

(i) $N \cap K$ is a normal subgroup of $K$; 

(ii) $N$ is a normal subgroup of $N \vee K$; 

(iii) $NK = N \vee K = KN$;

(iv) if $K$ is normal in $G$ and $K \cap N = \langle e \rangle$, then $nk = kn$ for all $k \in K$ and $n \in N$.

**Theorem 5.4.** (Quotient Group/Factor Group) If $N$ is a normal subgroup of a group $G$ and $G/N$ is the set of all (left) cosets of $N$ in $G$, then $G/N$ is a group of order $[G:N]$ under the binary operation given by $(aN)(bN) = abN$.

**Theorem 5.5.** If $f: G \rightarrow H$ is a homomorphism of groups, then the kernel of $f$ is a normal subgroup of $G$. Conversely, if $N$ is a normal subgroup of $G$, then the map $\pi : G \rightarrow G/N$ given by $\pi (a) = aN$ is an epimorphism with its kernel $N$.（$\pi$ 称为典范商映射）

**Theorem 5.6.** If $f: G \rightarrow H$ is a homomorphism of groups and $N$ is a normal subgroup of $G$ contained in the kernel of $f$, then there is a unique homomorphism $\overline{f}: G/N \rightarrow H$ such that $\overline{f}(aN) = f(a)$ for all $a \in G$. $\mathrm{Im} f = \mathrm{Im} \overline{f}$ and $\mathrm{Ker} \overline{f} = (\mathrm{Ker} f)/N$. $\overline{f}$ is an isomorphism if and only if $f$ is an epimorphism and $N = \mathrm{Ker} f$.

**Corollary 5.7.** (First Isomorphism Theorem) If $f: G \rightarrow H$ is a homomorphism of groups, then $f$ induces an isomorphism $G/ \mathrm{Ker} f \cong \mathrm{Im} f$.

**Corollary 5.8.** If $f: G \rightarrow H$ is a homomorphism of groups, $N \triangleleft G$, $M \triangleleft H$, and $f(N) < M$, then $f$ induces a homomorphism $\overline{f}: G/N \rightarrow H/M$, given by $aN \mapsto f(a)M$. $\overline{f}$ is an isomorphism if and only if $\mathrm{Im} f \vee M = H$ and $f^{-1}(M) \subset N$. In particular if $f$ is an epimorphism such that $f(N) = M$ and $\mathrm{Ker} f \subset N$, then $\overline{f}$ is an isomorphism. 

**Corollary 5.9.** (Second Isomorphism Theorem) If $K$ and $N$ are subgroups of a group $G$, with $N$ normal in $G$, then $K/(N \cap K) \cong NK/N$.

**Corollary 5.10.** (Third Isomorphism Theorem). If $H$ and $K$ are normal subgroups of a group $G$ such that $K < H$, then $H/K$ is a normal subgroup of $G/K$ and $(G/K)/(H/K) \cong G/H$.

**Theorem 5.11.** If $f: G \rightarrow H$ is an epimorphism of groups, then the assignment $K \mapsto f(K)$ defines a one-to-one correspondence between the set $S_f(G)$ of all subgroups $K$ of $G$ which contain $\mathrm{Ker} f$ and the set $S(H)$ of all subgroups of $H$. Under this correspondence normal subgroups correspond to normal subgroups.

**Corollary 5.12.** If $N$ is a normal subgroup of a group $G$, then every subgroup of $G/N$ is of the form $K/N$, where $K$ is a subgroup of $G$ that contains $N$. Furthermore, $K/N$ is normal in $G/N$ if and only if $K$ is normal in $G$.

## Symmetric, Alternating and Dihedral Groups

**Definition 6.1.** Let $i_1,i_2, \ldots , i_r, (r \leqslant n)$ be distinct elements of $I_n = \{1,2, \ldots, n\}$. Then $(i_1i_2\cdots i_r)$ denotes the permutation that maps it $i_1 \mapsto i_2, i_2 \mapsto i_3, i_3 \mapsto i_4 , \ldots , i_{r - 1} \mapsto i_r$ and $i_r \mapsto i_1$ and maps every other element of $I_n$ onto itself. $(i_1i_2\cdots i_r)$ is called a **cycle** of length $r$ or an $r$-cycle; a 2-cycle is called a **transposition**. 

**Definition 6.2.** The permutations $\sigma_1, \sigma_2, \ldots , \sigma_r$ of $S_n$ are said to be **disjoint** provided that for each $1 \leqslant i \leqslant r$, and every $k \in I_n$, $\sigma_i(k) \neq k$ implies $\sigma_j(k) = k$ for all $j \neq i$.

It is easy to see that $\tau \sigma = \sigma \tau$ whenever $\sigma $ and $\tau $ are disjoint.

**Theorem 6.3.** Every nonidentity permutation in $S_n$ is uniquely (up to the order of the factors) a product of disjoint cycles, each of which has length at least 2.

**Corollary 6.4.** The order of a permutation $\sigma \in S_n$ is the least common multiple of the orders of its disjoint cycles. 