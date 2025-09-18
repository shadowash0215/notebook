# 同态加密的定义

!!! info "定义"
    一个同态加密系统由四部分组成：  
    1. 密钥生成：$\operatorname{KeyGen}(\lambda) \rightarrow (\text{pk}, \text{sk})$;  
    2. 加密：$\operatorname{Enc}(\text{pk}, \text{pt}) \rightarrow \text{ct}$;  
    3. 解密：$\operatorname{Dec}(\text{sk}, \text{ct}) \rightarrow \text{pt}$;  
    4. 评估函数：$\operatorname{Eval}(\text{pk}, \Pi, \text{ct}_1, \text{ct}_2, \ldots) \rightarrow \text{ct}_1', \text{ct}_2', \ldots$, 其会对输入密文应用函数 $\Pi$，并输出新的密文。

评估函数是同态加密系统的核心，也是其与传统加密系统的区别所在。同样，同态加密系统也需要满足如下的性质：

!!! info "定义"
    （正确性）同态加密系统被称为对操作 $\Pi$ 是正确的，如果其满足以下两个性质：  
    
    - 能够正确解密未被评估函数处理的密文（这样的密文被称为 fresh 的），即  

    \[
        \operatorname{Pr}[\operatorname{Dec}(\text{sk}, \operatorname{Enc}(\text{pk}, \text{pt})) = \text{pt}] = 1.
    \]

    - 能够正确解密被评估函数处理的密文，即  

    \[
        \operatorname{Pr}[\operatorname{Dec}(\text{sk}, \operatorname{Eval}(\text{pk}, \Pi, \text{ct}_1, \text{ct}_2, \ldots)) = \Pi(\text{pt}_1, \text{pt}_2, \ldots)] = 1, 
    \]

    其中 $\text{ct}_i = \operatorname{Enc}(\text{pk}, \text{pt}_i)$。

不过注意 $\Pi$ 的参数是明文，但是 $\operatorname{Eval}$ 的参数是密文，所以评估函数会执行需要执行与 $\Pi$ 相对应密文操作。

自然，作为一种加密系统，同态加密系统也需要满足传统加密系统的安全性要求，比如 CPA 安全性、CCA 安全性等。

- 选择明文攻击（CPA）：攻击者可以选择两个明文 $m_0, m_1$，并获得密文 $c = \operatorname{Enc}(m_b)$，攻击者需要根据 $c$ 判断 $b$ 的值。  
- 选择密文攻击（CCA）：攻击者可以发送任意数量的密文 $c_i$，并获得解密结果 $m_i = \operatorname{Dec}(c_i)$，以帮助攻击者破解密文。其可以分为 CCA1 和 CCA2 两种，前者只允许在选择明文前进行攻击，后者则允许在选择明文后进行攻击。也就是说，在后者的情形下，攻击者可以根据已知的密文进行有关联的密文构建，来获取更多的信息。

对于选择明文攻击，因为公钥是公开的，所以攻击者可以使用任意算法 $A(\text{pk}, \text{ct}) \to \{0, 1\}$ 来判断密文的真实明文。如果对于任何一个多项式时间函数 $A$，都有

\[
    \lvert \operatorname{Pr}[A(\text{pk}, \text{ct}_0) = 1] - \operatorname{Pr}[A(\text{pk}, \text{ct}_1) = 1] \rvert < \varepsilon,
\]

也就是说，攻击者没有一个概率多项式时间算法可以