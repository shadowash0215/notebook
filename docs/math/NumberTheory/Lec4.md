<style>
.center {
  width: auto;
  display: table;
  margin-left: auto;
  margin-right: auto;
}
</style>

# Order of units & Application in cryptography

!!! info "Definition"
    $x \in \mathbb{Z}/n\mathbb{Z}^{\times}$, the order of $x$ is the smallest positive integer $r$ such that $x^r \equiv 1 \pmod n$. 

!!! example
    $n = 15, \varphi(15) = 8$. By Euler, $x^8 \equiv 1 \pmod {15}$ if $(x, 15) = 1$.  
    But we have 
    <div class="center">
    <table border='1'>
        <tr>
            <td align='center'>$x\text{ \ }k$</td> 
            <td>$1$</td> 
            <td>$2$</td> 
            <td>$3$</td>
            <td>$4$</td> 
        </tr>
        <tr>
            <td align='center'> 1 </td>
            <td> 1 </td>
            <td> * </td>
            <td> * </td>
            <td> * </td>
        </tr>
        <tr>
            <td align='center'> 2 </td>
            <td> 2 </td>
            <td> 4 </td>
            <td> 8 </td>
            <td> 1 </td>
        </tr>
        <tr>
            <td align='center'> 4 </td>
            <td> 4 </td>
            <td> 1 </td>
            <td> 4 </td>
            <td> 1 </td>
        </tr>
        <tr>
            <td align='center'> 7 </td>
            <td> 7 </td>
            <td> 4 </td>
            <td> 13 </td>
            <td> 1 </td>
        </tr>
        <tr>
            <td align='center'> 8 </td>
            <td> 8 </td>
            <td> 4 </td>
            <td> 2 </td>
            <td> 1 </td>
        </tr>
        <tr>
            <td align='center'> 11 </td>
            <td> 11 </td>
            <td> 1 </td>
            <td> * </td>
            <td> * </td>
        </tr>
        <tr>
            <td align='center'> 13 </td>
            <td> 13 </td>
            <td> 4 </td>
            <td> 7 </td>
            <td> 1 </td>
        </tr>
        <tr> 
            <td align='center'> 14 </td>
            <td> 14 </td>
            <td> 1 </td>
            <td> * </td>
            <td> * </td>
    </table>
    </div>

    So Euler's theorem is not a sufficient condition for the order of $x$.

!!! note "Theorem"
    $n \in \mathbb{Z}, n \geqslant 1, a \in (\mathbb{Z}/n\mathbb{Z})^{\times}$, $k$ is the order $a$. If $a^m \equiv 1 \pmod n$, then $k \mid m$.

    !!! success "Collary"
        $k \mid \varphi(n)$.

    ??? note "Proof"
        Consider $m = q \cdot k + r, 0 \leqslant r < k$, then 

        \[
            a^r = a^{m - q \cdot k} = a^{m} \cdot (a^{k})^{-q} \equiv 1 \pmod n.
        \]

        But $k$ is the smallest positive integer such that $a^k \equiv 1 \pmod n$, so $r = 0$, $k \mid m$.

!!! success "Lemma"
    (i) $x^{p - 1} - 1 \equiv (x-1)(x-2)\cdots(x-(p-1)) \pmod p$ as polynomials.

    (ii) $x$ coprime to $n$, order $r$, $y$ coprime to $n$, order $s$. If $(r, s) = 1$, then the order of $xy$ is $rs$.

    ??? success "Proof"
        (i) By Fermat, $x^{p - 1} \equiv 1 \pmod p$ has $p-1$ roots $1, 2, \ldots, p-1$. It's the same as $(x - 1)(x - 2) \cdots (x - (p - 1))$. So $x^{p - 1} - 1 \equiv c \cdot (x - 1)(x - 2)\cdots(x - (p - 1)) \pmod p$. Compare the coffient of $x^{p -1 }$, $c = 1$.

        (ii) $x^r \equiv 1 \pmod n, y^s \equiv 1 \pmod n$, then $(xy)^{rs} \equiv 1 \pmod n$. If $d$ is the order of $xy$, then $d \mid rs$. So we only need to prove that $rs \mid d$.  
        $(xy)^d \equiv 1 \pmod n$. $y^{rd} \equiv y^{rd} \cdot x^{rd} \equiv (xy)^{rd} \equiv 1 \pmod n$, which means $s \mid rd$. As $(r, s) = 1$, we have $s \mid d$.  
        Reverse $x, y$, and we have $r \mid d$. So $rs \mid d$, $d = rs$.

!!! note "Theorem"
    If $p$ is a prime, then $(\mathbb{Z}/p\mathbb{Z})^{\times}$ has a generator $g$.
    ??? note "Proof"
        $p - 1 = q_1^{n_1}\cdots q_l^{n_l}$ is the unique factorization of $p-1$ in $\mathbb{Z}$.  
        If we can find $x_j$ of order $q_j^{n_j}$, then $x_1x_2\cdots x_l$ has order $q_1^{n_1}\cdots q_l^{n_l} = p - 1$.  
        $x^{q_1^{n_1}} - 1 \mid x^{p - 1} - 1$. ($y^k - 1 = (y -1 )(y^{k - 1}+ y ^{k - 2} + \cdots + y + 1)$, and let $y = x^{q_1^{n_1}}$) So $x^{p - 1} - 1 = (x^{q_1^{n_1}} - 1) \cdot g_1(x)$.  
        $\bmod p$, we have $x^{p - 1} - 1 \equiv (x^{q_1^{n_1}} - 1) \cdot g_1(x) \pmod p$. $x^{p - 1} - 1$ has distinct roots $1, 2, \ldots, p - 1$(By Fermat). Because a $\operatorname{deg} n$ polynomial equation has exactly $n$ roots, then $x^{q_1^{n_1}} - 1$ has exactly $q_1^{n_1}$ distinct roots.  
        Similary, $x^{q_1^{n_1 - 1}}$ has exactly $q_1^{n_1 - 1}$ distinct roots. Because $q_1^{n_1} > q_1^{n_1 - 1}, q_1 > 1$, then there exists $x_1$ such that $x_1^{q_1^{n_1}} \equiv 1 \pmod p$, but $x_1^{q_1^{n_1 - 1}} \not \equiv 1 \pmod p$. So the order of $x_1$ is $q_1^{n_1}$.  
        As the same, we can find $x_j$ of order $q_j^{n_j}$, then $g = x_1x_2 \cdots x_l$ has order $p - 1$. $g$ is the generator.

!!! note "Theorem"
    (Wilson's theorem, not very useful) $p$ is a prime, then $(p - 1)! \equiv -1 \pmod p$.
    ??? note "Proof"
        Remember $x^{p - 1} - 1 \equiv (x - 1)(x - 2)\cdots(x - (p - 1)) \pmod p$. Set $x = p$, then $(p - 1)! \equiv -1 \pmod p$.