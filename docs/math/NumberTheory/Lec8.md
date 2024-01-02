# Quadratic Gauss Sum

!!! example
    Solve $x^7-1 = 0$.  
    It's obvious that $x^7-1 = (x-1)(x^6+x^5+x^4+x^3+x^2+x+1)$. So we just need to solve $x^6+x^5+x^4+x^3+x^2+x+1 = 0$. And that means we only need to solve $x^3+x^2+x+1+x^{-1}+x^{-2}+x^{-3} = 0$. Let's set $y = x + x^{-1}$. So the equation is converted into $y^3+y^2-2y-1 = 0$.  
    We set $\omega = e^{\frac{2\pi \mathrm{i}}{3}}$ and suppose that the solutions to the equation are $y_1, y_2, y_3$. We set $t(1) = y_1+y_2+y_3$, $t(\omega) = y_1+y_2 \cdot \omega+y_3 \cdot \omega^2$, $t(\omega^2) = y_1+y_2 \cdot \omega^2+y_3 \cdot \omega$. Then we have 
    
    \[
        \begin{pmatrix} t(1) \\ t(\omega) \\ t(\omega^2) \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & \omega & \omega^2 \\ 1 & \omega^2 & \omega^4 \end{pmatrix} \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix}.
    \]

    $t(\omega) \cdot t(\omega^2) = y_1^2+y_2^2+y_3^2+(y_1y_2+y_2y_3+y_3y_1)(\omega+\omega^2) = 7$
    So $t(\omega^2) = \frac{7}{t(\omega)}$.  
    Try $t(\omega)^3 = y_1^3 + y_2^3 + y_3^3 + 6y_1y_2y_3 + 3\omega(y_1^2y_2+y_2^2y_3+y_3^2y_1) + 3\omega^2(y_1y_2^2+y_2y_3^2+y_3y_1^2)$. Set $\alpha = y_1^2y_2+y_2^2y_3+y_3^2y_1, \beta = y_1y_2^2+y_2y_3^2+y_3y_1^2$. So $t(\omega)^3 = 2 + 3\omega\alpha + 3\omega^2\beta$.  
    And we have $\alpha + \beta = -1, \alpha \cdot \beta = -12$. So $\{\alpha, \beta\} = \{-4, 3\}$.  
    Assume $\alpha = 3, \beta = -4$. $t(\omega)^3 = 14+21\omega$. Choose $\eta$ such that $\eta^3 = 14+21\omega$. $t(\omega) = \eta$, $t(\omega^2) = \frac{7}{\eta}$, $t(1) = -1$.  
    So
    
    \[
        \begin{gather} y_1 = \frac{1}{3}(-1 + \eta + \frac{7}{\eta})  \\ y_2 = \frac{1}{3}(-1 + \omega^2\eta + \frac{7}{\omega^2\eta}) \\ y_3 = \frac{1}{3}(-1 + \omega\eta + \frac{7}{\omega\eta}) \end{gather}
    \]

!!! note "Main Theorem"
    Define $\mathfrak{G}_a = \sum_{t = 0}^{p-1}(\frac{t}{p}) \omega^{at}, \omega = e^{\frac{2\pi \mathrm{i}}{p}}$. Then $\mathfrak{G}_1^2 = (-1)^{\frac{p-1}{2}}\cdot p = \begin{cases} p, p \equiv 1 \pmod 4 \\ -p, p \equiv -1 \pmod 4 \end{cases}$. And $\mathfrak{G}_1 = \begin{cases} \sqrt{p}, p \equiv 1 \pmod 4 \\ \sqrt{-p}, p \equiv -1 \pmod 4 \end{cases}$.

!!! success "Lemma"
    (i) 
    
    \[ 
        \sum_{t = 0}^{p-1} \omega^{at} = \begin{cases} p, \ p \mid a \\ 0, \ p \not \mid a \end{cases}
    \]

    (ii) Consider $\chi: \mathbb{Z}/p\mathbb{Z} \rightarrow \mathbb{C} - \{0\}$.  
        (a) $\chi(a + b) = \chi(a) \chi(b)$.  
        (b) $\chi \neq 1 \Rightarrow \sum_{a = 0}^{p-1} \chi(a) = 0$.

    (iii) $\sum_{t = 1}^{p-1}\left(\frac{t}{p}\right) = 0$.  

    (iv) $\mathfrak{G}_a = \left(\frac{a}{p}\right)\mathfrak{G}_1$.

    ??? success "Proof"
        (i) If $p \mid a$, then $\omega^{at} = 1$. So $\sum_{t = 0}^{p-1} \omega^{at} = p$.  
        If $p \not \mid a$, then $\omega^{at} \neq 1$. So $\sum_{t = 0}^{p-1} \omega^{at} = \dfrac{\omega^{ap} - 1}{\omega^a - 1} = 0$.  

        (ii) (b) $\sum_{a = 0}^{p-1} \chi(a + b) = \chi(b) \sum_{a = 0}^{p-1} \chi(a)$, and $\sum_{a = 0}^{p-1} \chi(a + b) = \sum_{a = 0}^{p-1} \chi(a)$. So $(\chi(b) - 1) \sum_{a = 0}^{p-1} \chi(a) = 0$. Let $\chi(b) \neq 1$, we have $\sum_{a = 0}^{p-1} \chi(a) = 0$.  

        (iii) Set $\chi(a) = \left(\frac{a}{p}\right)$. So $\sum_{t = 1}^{p-1}\left(\frac{at}{p}\right) = \chi(a) \sum_{t = 1}^{p-1}\left(\frac{t}{p}\right) = \sum_{t = 1}^{p-1}\left(\frac{t}{p}\right)$. $(a \not \mid p)$ Set $\chi(a) \neq 1 \Rightarrow \sum_{t = 1}^{p-1}\left(\frac{t}{p}\right) = 0$.

        (iv) (a) $p \mid a$, $\mathfrak{G}_a = \sum_{t = 0}^{p-1}(\frac{t}{p})\omega^{at} = 0 = \left(\frac{a}{p}\right)\mathfrak{G}_1$.  
            (b) $p \not \mid a$, $\mathfrak{G}_a = \sum_{t = 0}^{p-1}(\frac{t}{p})\omega^{at}$. So $a^{-1}$ exists. Let $t \mapsto a^{-1}t$, we have $\mathfrak{G}_a = \sum_{t = 0}^{p-1}(\frac{a^{-1}t}{p})\omega^{t} = \left(\frac{a}{p}\right)\mathfrak{G}_1$. $(\left(\frac{a^{-1}}{p}\right) \cdot \left(\frac{a}{p}\right) = 1)$

??? note "Proof of Main Theorem"
    (a) If $p \not \mid a, \mathfrak{G}_a \cdot \mathfrak{G}_{-a} = \left(\frac{a}{p}\right)\mathfrak{G}_1 \cdot \left(\frac{-a}{p}\right)\mathfrak{G}_1 = (-1)^{\frac{p-1}{2}}\mathfrak{G}_1^2$.  
    (b) If $p \mid a, \mathfrak{G}_a = 0$.  
    Sum them up, we have $\sum_{a = 0}^{p-1} \mathfrak{G}_a \cdot \mathfrak{G}_{-a} = (-1)^{\frac{p-1}{2}}\cdot (p-1) \cdot \mathfrak{G}_1^2$.   
    Then we consider calculating $\sum_{a = 0}^{p-1} \mathfrak{G}_a \cdot \mathfrak{G}_{-a}$. $\mathfrak{G}_a \cdot \mathfrak{G}_{-a} = \sum_{x = 0}^{p-1} \sum_{y = 0}^{p-1} \left(\frac{x}{p}\right) \left(\frac{y}{p}\right) \omega^{a(x-y)}$.

    \begin{align}
        \sum_{a = 0}^{p-1} \mathfrak{G}_a \cdot \mathfrak{G}_{-a} & = \sum_{x = 0}^{p-1} \sum_{y = 0}^{p-1} \left(\frac{x}{p}\right) \left(\frac{y}{p}\right) \sum_{a = 0}^{p-1} \omega^{a(x-y)} \\ &=\sum_{x, y} \left(\frac{x}{p}\right) \left(\frac{y}{p}\right) \sum_{a = 0}^{p - 1} \delta_{x, y} \\ &= \sum_{x = 0}^{p-1} p \cdot \left(\frac{x^2}{p}\right) \cdot 1 = p(p-1)
    \end{align}

    Then $p(p-1) = (-1)^{\frac{p-1}{2}}\cdot (p-1) \cdot \mathfrak{G}_1^2$. So $\mathfrak{G}_1^2 = (-1)^{\frac{p-1}{2}}\cdot p$.

!!! success "Collary"
    $\pm \sqrt{\pm p} = \mathbb{Q}$-linear combination of $e^{\mathrm{i}\frac{2\pi}{p}}$.
