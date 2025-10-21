# Quantum algorithms for number fields

## Pell's equation

## Some basic algebraic number theory

大部分可以参考 [Math-NumberTheory-Pell's Equation](https://note.shad0wash.cc/math/NumberTheory/Lec9/)

定义 $R := \ln(x_1 + y_1\sqrt{d})$ 为基本解的**调节数** (regulator)，因为基本解的大小上界为 $2^{O(\sqrt{d}\log d)}$，所以 $R = O(\sqrt{d}\log d)$，因此记录 $\lceil R \rceil$ 需要 $O(\log d)$ 位. 而存在一个经典算法，在给定 $R$ 的整数部分的情况下，可以在 $\op{poly}(\log d, n)$ 时间内计算出 $R$ 的 $n$ 位小数. 因此只需要提供一个能在 $\op{poly}(\log d)$ 时间内计算 $R$ 整数部分的算法即可. 在广义 Riemann 猜想下，最著名的经典算法的复杂度为 $2^{O(\sqrt{\log d \log\log d})}$；而在不做任何假设的情况下，复杂度为 $O(d^{1/4} \op{poly} \log d)$.

## A periodic function for the units of $\mathbb{Z}[\sqrt{d}]$

将环元素 $\xi \in \mathbb{Z}[\sqrt{d}]$ 映射到主理想 $\xi R$ 的函数是周期性的，并且周期性对应于 $\mathbb{Z}[\sqrt{d}]$ 中的单位. 具体来说有以下定理：

!!! note "Proposition"
    $\xi \mathbb{Z}[\sqrt{d}] = \zeta \mathbb{Z}[\sqrt{d}]$ 当且仅当存在单位 $\varepsilon$ 使得 $\xi = \varepsilon \zeta$.

    ???+ note "Proof"
        $(\Leftarrow)$ 如果 $\varepsilon$ 是单位，那么 $\xi \mathbb{Z}[\sqrt{d}] = \varepsilon \zeta \mathbb{Z}[\sqrt{d}] = \zeta \mathbb{Z}[\sqrt{d}]$.

        $(\Rightarrow)$ 假设 $\xi \mathbb{Z}[\sqrt{d}] = \zeta \mathbb{Z}[\sqrt{d}]$，因为 $1 \in \mathbb{Z}[\sqrt{d}]$，所以 $\xi \in \xi \mathbb{Z}[\sqrt{d}] = \zeta \mathbb{Z}[\sqrt{d}]$，所以存在 $\mu \in \mathbb{Z}[\sqrt{d}]$ 使得 $\xi = \zeta \mu$；同理，存在 $\nu \in \mathbb{Z}[\sqrt{d}]$ 使得 $\zeta = \xi \nu$，因此 $\xi = \zeta \mu = \xi \nu \mu$，所以 $\nu \mu = 1$，$\mu$ 和 $\nu$ 都是单位.

所以函数 $g(\xi) = \xi \mathbb{Z}[\sqrt{d}]$ 是乘法周期性的，周期为 $\varepsilon_1$. 换言之，令 $\xi = e^z$，那么函数

\[
    h(z) = e^z \mathbb{Z}[\sqrt{d}]
\]

便是加法周期性的，周期为 $R$. 但这个函数的取值并不能被有效地表示出来，所以 Hallgren 利用约化理想的概念以及测量主理想距离的技术定义一个更合适的周期函数. 因为约化主理想的个数实际上只有 $O(d)$ 个，所以可以用 $\op{poly}(\log d)$ 位来表示.

Hallgren 还定义了测量主理想和单位理想距离的函数 $\delta$，其定义如下：

\[
    \delta(\xi \mathbb{Z}[\sqrt{d}]) := \ln \left\lvert \frac{\xi}{\bar{\xi}} \right\rvert \mod R.
\]

注意到 $\delta(1 \mathbb{Z}[\sqrt{d}]) = \ln \left \lvert 1/1 \right \rvert \mod R = 0$，并且对于任意单位 $\varepsilon$ 有

\[
    \delta(\varepsilon \mathbb{Z}[\sqrt{d}]) = \ln \left\lvert \frac{\varepsilon}{\bar{\varepsilon}} \right\rvert \mod R = \ln \left\lvert \frac{\varepsilon}{\varepsilon^{-1}} \right\rvert \mod R = 2\ln \left\lvert \varepsilon \right\rvert \mod R = 0.
\]

所以该距离函数不依赖于选择的主理想代表元. 利用这个距离定义可以证明所有的约化理想的距离都不太远，因此任何非约化理想附近都有一个约化理想. Hallgren 算法中的周期函数 $f(z)$ 定义为：在距离不超过 $z$ 的所有约化主理想中，与单位理想距离最大的那个约化主理想，并且记录差值 $z - \delta(\xi \mathbb{Z}[\sqrt{d}]) \mod R$ 以确保每个周期内函数都是一一对应的.