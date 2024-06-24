## AVL 树

!!! info "Definition"
    **平衡树**：空二叉树是平衡的. 如果一棵二叉树的左子树和右子树的高度差的绝对值不超过 1，且左右子树都是平衡的，那么这棵二叉树就是平衡的. 空树的高度定义为 -1.

    **平衡因子**：$BF(T) = h(T.left) - h(T.right)$. 所以在 AVL 树中，平衡因子的取值范围为 $-1, 0, 1$.

AVL 树的结点定义如下：

```c
typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    int height;
} Node, *AVLTree;
```

失衡调整的措施是对树进行旋转操作，分为左旋和右旋。旋转的过程中需要对高度调整，使用到的宏有：

```c
#define HEIGHT(p) ((p) == NULL ? -1 : (((Node *)(p)))->height)
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

具体操作如下：

=== "右旋"

    ```c
    Node *rightRotate(AVLTree p) {
        AVLTreenew_p = p->left;
        p->left = new_p->right;
        new_p->right = p;
        p->height = MAX(HEIGHT(p->left), HEIGHT(p->right)) + 1;
        new_p->height = MAX(HEIGHT(new_p->left), HEIGHT(new_p->right)) + 1;
        return new_p;
    }
    ```

=== "左旋"

    ```c
    Node *leftRotate(AVLTree p) {
        AVLTreenew_p = p->right;
        p->right = new_p->left;
        new_p->left = p;
        p->height = MAX(HEIGHT(p->left), HEIGHT(p->right)) + 1;
        new_p->height = MAX(HEIGHT(new_p->left), HEIGHT(new_p->right)) + 1;
        return new_p;
    }
    ```

根据造成失衡的插入位置，可以分为四种情况，其中 "LL" 和 "RR" 只需要一次旋转，而 "LR" 和 "RL" 需要两次旋转。

=== "LL"

    ```c
    Node *LL_Rotate(AVLTree p) {
        return rightRotate(p);
    }
    ```

=== "RR"

    ```c
    Node *RR_Rotate(AVLTree p) {
        return leftRotate(p);
    }
    ```

=== "LR"

    ```c
    Node *LR_Rotate(AVLTree p) {
        p->left = leftRotate(p->left);
        return rightRotate(p);
    }
    ```

=== "RL"

    ```c
    Node *RL_Rotate(AVLTree p) {
        p->right = rightRotate(p->right);
        return leftRotate(p);
    }
    ```

AVL 树常见的操作如下：

=== "创建节点"

    ```c
    Node *CreateNode(int val) {
        Node *p = (Node *)malloc(sizeof(Node));
        p->val = val;
        p->left = p->right = NULL;
        p->height = 0;
        return p;
    }
    ```

=== "插入节点"

    ```c
    Node *Insert(AVLTree tree, int val) {
        if (tree == NULL) {
            tree = CreateNode(val);
        } else if (val < tree->val) {
            tree->left = Insert(tree->left, val);
            if (HEIGHT(tree->left) - HEIGHT(tree->right) == 2) { // 因为只插入一个节点，所以失衡必然为 2
                if (val < tree->left->val) {
                    tree = LL_Rotate(tree);
                } else {
                    tree = LR_Rotate(tree);
                }
            }
        } else if (val > tree->val) {
            tree->right = Insert(tree->right, val);
            if (HEIGHT(tree->right) - HEIGHT(tree->left) == 2) { // 因为只插入一个节点，所以失衡必然为 2
                if (val > tree->right->val) {
                    tree = RR_Rotate(tree);
                } else {
                    tree = RL_Rotate(tree);
                }
            }
        } else {
            return NULL; // 重复的节点
        }
        tree->height = MAX(HEIGHT(tree->left), HEIGHT(tree->right)) + 1;
        return tree;
    }
    ```

使用 AVL 树进行查询的时间复杂度为 $O(h)$，其中 $h$ 为树的高度。而高度为 $h$ 的 AVL 树的最少节点数目记为 $n_h$，则 $n_h = n_{h-1} + n_{h-2} + 1$，运用斐波那契数列，可以得到 $n_h = F_{h+2} - 1$. 

## Splay 树

节点定义如下：

```c
typedef struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode* parent;
} Node, *SplayTree;
```

Splay 树的基本操作也是通过旋转来实现的，左旋和右旋的操作如下：

=== "左旋"

    ```c
    void leftRotate(SplayTree p) {
        SplayTree x = p->right;
        // 将 x 的左儿子设为 p 的右儿子，更新 x 的父节点
        if(x) {
            p->right = x->left;
            if(x->left) x->left->parent = p;
            x->parent = p->parent;
        }

        if(p->parent) {
            if(p == p->parent->left) {
                p->parent->left = x;
            } else {
                p->parent->right = x;
            }
        } 
        if(x) x->left = p;
        p->parent = x;
    }
    ```
    
=== "右旋"

    ```c
    void rightRotate(SplayTree p) {
        SplayTree x = p->left;
        // 将 x 的右儿子设为 p 的左儿子，更新 x 的父节点
        if(x) {
            p->left = x->right;
            if(x->right) x->right->parent = p;
            x->parent = p->parent;
        }
        if(p->parent) {
            if(p == p->parent->left) {
                p->parent->left = x;
            } else {
                p->parent->right = x;
            }
        }
        if(x) x->right = p;
        p->parent = x;
    }
    ```

而 Splay 树有三种调整的情况：  

- **Zig**: 如果 x 是根节点，那么只需要一次旋转即可  
- **Zig-Zig**: child, parent, grandparent 三个节点在同一条链上  
- **Zig-Zag**: child, parent, grandparent 三个节点在不同的链上  

所以 splay 操作的代码如下：

```c
void splay(SplayTree p) {
    while(p->parent) {
        if (!p->parent->parent) {
            if(p->parent->left == p) rightRotate(p->parent);
            else leftRotate(p->parent);
        } else if(p->parent->left == p && p->parent->parent->left == p->parent) {
            rightRotate(p->parent->parent);
            rightRotate(p->parent);
        } else if(p->parent->right == p && p->parent->parent->right == p->parent) {
            leftRotate(p->parent->parent);
            leftRotate(p->parent);
        } else if(p->parent->left == p && p->parent->parent->right == p->parent) {
            rightRotate(p->parent);
            leftRotate(p->parent);
        } else {
            leftRotate(p->parent);
            rightRotate(p->parent);
        }
    }
}
```

Splay 树的基本操作如下：

=== "创建节点"

    ```c
    SplayTree CreateNode(int val) {
        SplayTree p = (Node *)malloc(sizeof(Node));
        p->val = val;
        p->left = p->right = p->parent = NULL;
        return p;
    }
    ```

=== "插入节点"

    ```c
    SplayTree Insert(SplayTree tree, int val) {
        if (tree == NULL) {
            tree = CreateNode(val);
        } else {
            SplayTree p = tree;
            SplayTree pre = NULL;
            while(p) {
                pre = p;
                if(val < p->val) {
                    p = p->left;
                } else if(val > p->val) {
                    p = p->right;
                } else {
                    return NULL; // 重复的节点
                }
            }

            p = CreateNode(val);
            p->parent = pre;
            if(val < pre->val) {
                pre->left = p;
            } else {
                pre->right = p;
            }
            splay(p);
            tree = p;
        }
        return tree;
    }
    ```

=== "查找节点"

    ```c
    SplayTree Search(SplayTree tree, int val) {
        SplayTree p = tree;
        while(p) {
            if(val < p->val) {
                p = p->left;
            } else if(val > p->val) {
                p = p->right;
            } else {
                splay(p);
                return p;
            }
        }
        return NULL;
    }
    ```

=== "删除节点"

    ```c
    SplayTree Delete(SplayTree tree, int val) {
        SplayTree p = Search(tree, val);
        if(p == NULL) return tree;
        if(p->left == NULL) {
            tree = p->right;
            if(tree) tree->parent = NULL;
        } else {
            SplayTree x = p->left;
            // Find the maximum node in the left subtree
            while(x->right) x = x->right;
            splay(x);
            x->right = p->right;
            if(p->right) p->right->parent = x;
            tree = x;
        }
        free(p);
        return tree;
    }
    ```

## 摊还分析

摊还分析是一种分析数据结构和算法的平块平均性能的方法。其一般要从空结构开始，如果不从空结构开始，则必须要求连续的操作数量足够大，从而抵消初始步骤中可能出现的消耗较大的操作。

以下方法的分析示例基于 Multi-Stack，其包括了三种操作：`push`, `pop`, `multipop`。`push` 和 `pop` 与平常无异， `multipop` 操作是将栈中的 $n = \operatorname{min}(k, \operatorname{Sizeof}(stack))$ 个元素弹出，其中 $k$ 为传入的参数。所以 `push` 和 `pop` 一次的代价为 1，`multipop` 一次的代价为 $n$。

### 聚合法

聚合法的想法是找出连续 $n$ 个操作中的最坏序列情况，并且排除掉不可能出现的所谓“最坏情况”。若其耗时为 $T_n$，则摊还时间为 $T_n/n$。

??? example "Multi-Stack"
    如果我们只是暴力分析最差情况，认为 `multipop` 的最差情况是每次都 `multipop` 出 $n$ 个元素，那么其时间复杂度将会达到 $O(n^2)$，这显然是不合理的，因为栈中没有那么多元素. 所以我们利用聚合法来分析其摊还时间复杂度，这里面的最坏情况是 $n - 1$ 次 `push` 和一次 $n - 1$ 个元素的 `multipop`，所以总开销为 $T_n = 2n - 2$，摊还时间复杂度为 $T_n/n = O(n)/n = O(1)$.

### 核算法

核算法的想法是截长补短，让所有操作能够保持在同一复杂度层级上，便于分析。设第 $i$ 种操作的真实成本为 $c_i$，截长补短的摊还成本为 

\[ 
    \hat{c_i} = c_i + \Delta_i.
\]

其中的 $\Delta_i$ 就表示了第 $i$ 种操作的“取长补短”。但我们还需要保证摊还成本要比平均成本来得大，这样才能确保摊还分析得到的时间复杂度是平均时间复杂度的上界，所以我们需要满足

\[
    \sum_{i=1}^n \hat{c_i} \geqslant \sum_{i=1}^n c_i, \ \forall n \in \mathbb{N}.
\]

也就是说 $\sum_{i=1}^n \Delta_i \geqslant 0$.

??? tip
    杨洋老师在课上打了一个很形象的比方。假设有一家卖汽水的小卖部，每瓶汽水 1 块钱，但你可以多花钱去买 1 瓶汽水，比如用 10 块钱，那么剩下的 9 块钱就是你的“积分”，在之后的某一天你便可以使用“积分”来买汽水而不另外付钱。同时，也要保证不赊账，也就是说你的“积分”不能为负。

??? example "Multi-Stack"
    基于核算法的思想，我们可以将每次 push 的代价设为 2，也就是说，我们预先将这个元素出栈的代价在入栈时就算在内，尽管它有可能不会出栈. 这样，每次 `pop` 和 `multipop` 的代价就是 0 了. 而因为 $\operatorname{Sizeof}(stack) \geqslant 0$，所以我们可以保证 $\sum_{i=1}^n \Delta_i \geqslant 0$。所以每种操作的代价都是 $O(1)$ 级别的，最终的摊还复杂度为 $O(n)/n = O(1)$.

### 势能法

核算法的“截长补短”想法是很好的，但通常并不那么容易实现，因为设计出一个摊还代价 $\hat{c_i}$ 并且保证 $\sum_{i=1}^n \Delta_i \geqslant 0$ 是相对困难的。因此我们希望在整个结构上能有某种度量，而非只局限在每个操作上，势能法就应运而生了。我们为整个结构定义一个势函数，其与这个结构中的某些特征量相关，便能够比较好的衡量每次操作对整个结构的影响以及相应的代价。定义第 $i$ 次操作的摊还代价为

\[
    \hat{c_i} = c_i + (\Phi(D_i) - \Phi(D_{i - 1})).  
\]

求和得到

\begin{align}
    \sum_{i=1}^n \hat{c_i} &= \sum_{i=1}^n (c_i + (\Phi(D_i) - \Phi(D_{i - 1}))) \\
    &= \sum_{i=1}^n c_i + \Phi(D_n) - \Phi(D_0).
\end{align} 

我们依然需要 $\sum_{i=1}^n \hat{c_i} \geqslant \sum_{i=1}^n c_i$，所以我们需要保证 $\Phi(D_n) - \Phi(D_0) \geqslant 0$，也就是说，我们需要保证势函数始终不比初始状态小，这点是容易做到的，因为我们可以将初始状态的势函数设为 0。

??? example "Multi-Stack"
    设 $D_i$ 为第 $i$ 次操作后的栈，势函数 $\Phi(D_i)$ 定义为栈中元素的个数. 显然栈中元素的个数不会小于 $0$，所以有 $\Phi(D_i) \geqslant \Phi(D_0)$。接下来计算每种操作的摊还代价：
    
    - `push`：$\hat{c_i} = 1 + (\Phi(D_i) - \Phi(D_{i - 1})) = 1 + 1 = 2$；  
    - `pop`：$\hat{c_i} = 1 + (\Phi(D_i) - \Phi(D_{i - 1})) = 1 + (-1) = 0$；  
    - `multipop`：$\hat{c_i} = n + (\Phi(D_i) - \Phi(D_{i - 1})) = n + (-n) = 0$.

    从而 $\sum_{i = 1}^n \hat{c_i} = \sum_{i = 1}^n O(1) = O(n)$，最终的摊还复杂度为 $O(n)/n = O(1)$.

!!! question
    Consider the following buffer management problem. Initially the buffer size (the number of blocks) is one. Each block can accommodate exactly one item. As soon as a new item arrives, check if there is an available block. If yes, put the item into the block, induced a cost of one. Otherwise, the buffer size is doubled, and then the item is able to put into. Moreover, the old items have to be moved into the new buffer so it costs $k + 1$ to make this insertion, where $k$ is the number of old items. Clearly, if there are $N$ items, the worst-case cost for one insertion can be $\Omega(N)$. To show that the average cost is $O(1)$, let us turn to the amortized analysis. To simplify the problem, assume that the buffer is full after all the $N$ items are placed. Which of the following potential functions works?
    
    1. The number of items currently in the buffer
    2. The opposite number of items currently in the buffer
    3. The number of available blocks currently in the buffer
    4. The opposite number of available blocks in the buffer

    ??? note "answer"
        设 $k_i$ 为第 $i$ 次插入前 buffer 内的元素个数，$s_i$ 为第 $i$ 次插入前 buffer 的大小，$c_i$ 为第 $i$ 次插入的实际代价，$\phi_i$ 为第 $i$ 次插入的势能. 则有：
        
        \[
            \hat{c_i} = c_i + \phi_i - \phi_{i-1}
        \]

        若插入前 buffer 没满，则 $c_i = 1$；若插入前 buffer 已满，则 $c_i = k_i + 1 = s_i + 1$.

        1. buffer 未满时，$\hat{c_i} = 1 + k_i + 1 - k_i = 2$；buffer 满时，$\hat{c_i} = k_i + 1 + k_i + 1 - k_i = k_i + 2$. 这是 $k_i$ 相关的，且我们无法估计 buffer 插满的次数，所以不合适.
        2. buffer 未满时，$\hat{c_i} = 1 + (-k_i - 1) - (-k_i) = 0$；buffer 满时，$\hat{c_i} = k_i + 1 + (-k_i - 1) - (-k_i) = k_i$. 这是 $k_i$ 相关的，且我们无法估计 buffer 插满的次数，所以不合适.
        3. buffer 未满时，$\hat{c_i} = 1 + (s_i - k_i - 1) - (s_i - k_i) = 0$；buffer 满时，$\hat{c_i} = k_i + 1 + (2s_i - k_i - 1) - (s_i - k_i) = 2s_i$. 这是 $s_i$ 相关的，且我们无法估计 buffer 插满的次数，所以不合适.
        4. buffer 未满时，$\hat{c_i} = 1 + (-s_i + k_i + 1) - (-s_i + k_i) = 2$；buffer 满时，$\hat{c_i} = k_i + 1 + (-2s_i + k_i + 1) - (-s_i + k_i) = 2$. 这是一个常数，所以合适.

        !!! warning
            此处题目做出的简化是第 $N$ 次一定插满，但更深层次的意义是中间过程的势函数均不予考虑，也就不考虑中间过程势函数小于初始状态的情况. 不能算是很合理的简化，但只能顺应题目的意思做.

### 综合应用：Splay 树操作的摊还复杂度分析

我们期望 Splay 树每个操作的摊还复杂度都是 $O(\log n)$ 级别的，而回忆 

\[
    \sum_{i=1}^n \hat{c_i} = \sum_{i=1}^n c_i + \Phi(D_n) - \Phi(D_0).
\]

所以我们期望 $\Phi(D_n)$ 是 $O(n \log n)$ 级别的。并且 Splay 树的操作是以旋转为基础的，Zig-Zig 和 Zig-Zag 操作都是旋转次数为 2，但我们并不知道这二者进行了多少次，所以希望能够在势函数中将旋转造成的开销给清除掉，以避免常数项求和引入 $O(n)$ 级别的复杂度。至于 Zig 操作，其最多可能出现 1 次，所以我们不考虑消除其旋转的开销。所以，定义 $\Phi(D_i) = \log S(D_i)$，即以 $D_i$ 为根节点的最大子树的节点个数（秩）。

而为了计算摊还复杂度时的放缩方便，我们有以下一个引理

!!! success "引理"
    若 $a + b \leqslant c$，且 $a, b$ 均为正整数，则

    \[
        \log a + \log b \leqslant 2 \log c - 2.
    \]

接下来分析三种操作的开销：

=== "Zig"

    \automata
        \node[state] at (-3, 0) (0) {$P$};
        \node[state] at (-4, -1) (1) {$X$};
        \node[state] at (-5, -2) (2) {$x$};
        \node[state] at (-3, -2) (3) {$y$};
        \node[state] at (-2, -1) (4) {$z$};
        \node[state] at (3, 0) (5) {$X$};
        \node[state] at (4, -1) (6) {$P$};
        \node[state] at (2, -1) (7) {$x$};
        \node[state] at (3, -2) (8) {$y$};
        \node[state] at (5, -2) (9) {$z$};
        \draw[->] (-1, -1) -- node[above]{single rotation} (1, -1);
        \draw[-] (0) -- (1);
        \draw[-] (1) -- (2);
        \draw[-] (1) -- (3);
        \draw[-] (0) -- (4);
        \draw[-] (5) -- (6);
        \draw[-] (5) -- (7);
        \draw[-] (6) -- (8);
        \draw[-] (6) -- (9);


    \begin{gather}
        \hat{c_i} = 1 + \operatorname{rank}_2(X) - \operatorname{rank}_1(X) + \operatorname{rank}_2(P) - \operatorname{rank}_1(P) \leqslant 1 + \operatorname{rank}_2(X) - \operatorname{rank}_1(X) \\
        (\operatorname{rank}_2(P) \leqslant \operatorname{rank}_1(P)) \\
    \end{gather}

=== "Zig-Zag"

    \automata
        \node[state] at (-3, 0) (0) {$G$};
        \node[state] at (-4, -1) (1) {$P$};
        \node[state] at (-5, -2) (2) {$x$};
        \node[state] at (-3, -2) (3) {$X$};
        \node[state] at (-2, -1) (4) {$w$};
        \node[state] at (-4, -3) (5) {$y$};
        \node[state] at (-2, -3) (6) {$z$};
        \node[state] at (4, 0) (7) {$X$};
        \node[state] at (2.5, -1) (8) {$P$};
        \node[state] at (5.5, -1) (9) {$G$};
        \node[state] at (1.3, -2.5) (10) {$x$};
        \node[state] at (3.3, -2.5) (11) {$y$};
        \node[state] at (4.7, -2.5) (12) {$z$};
        \node[state] at (6.7, -2.5) (13) {$w$};
        \draw[->] (-1, -1) -- node[above]{double rotation} (1, -1);
        \draw[-] (0) -- (1);
        \draw[-] (1) -- (2);
        \draw[-] (1) -- (3);
        \draw[-] (0) -- (4);
        \draw[-] (3) -- (5);
        \draw[-] (3) -- (6);
        \draw[-] (7) -- (8);
        \draw[-] (7) -- (9);
        \draw[-] (8) -- (10);
        \draw[-] (8) -- (11);
        \draw[-] (9) -- (12);
        \draw[-] (9) -- (13);


    \begin{align}
        \hat{c_i} &= 2 + \operatorname{rank}_2(X) - \operatorname{rank}_1(X) + \operatorname{rank}_2(P) - \operatorname{rank}_1(P) + \operatorname{rank}_2(G) - \operatorname{rank}_1(G) \\
        &= 2 + \operatorname{rank}_2(P) + \operatorname{rank}_2(G) - \operatorname{rank}_1(X) - \operatorname{rank}_1(P) \ (\operatorname{rank}_2(X) = \operatorname{rank}_1(G)) \\
        &\leqslant 2 + 2\operatorname{rank}_2(X) - 2 - \operatorname{rank}_1(X) - \operatorname{rank}_1(P) \ (\text{by the lemma}) \\
        &\leqslant 2(\operatorname{rank}_2(X) - \operatorname{rank}_1(X)) \ (\operatorname{rank}_1(P) \geqslant \operatorname{rank}_1(X))
    \end{align}

=== "Zig-Zig"

    \automata
        \node[state] at (-3, 0) (0) {$G$};
        \node[state] at (-4, -1) (1) {$P$};
        \node[state] at (-5, -2) (2) {$X$};
        \node[state] at (-6, -3) (3) {$x$};
        \node[state] at (-4, -3) (4) {$y$};
        \node[state] at (-3, -2) (5) {$z$};
        \node[state] at (-2, -1) (6) {$w$};
        \node[state] at (3, 0) (7) {$X$};
        \node[state] at (4, -1) (8) {$P$};
        \node[state] at (5, -2) (9) {$G$};
        \node[state] at (2, -1) (10) {$x$};
        \node[state] at (3, -2) (11) {$y$};
        \node[state] at (4, -3) (12) {$z$};
        \node[state] at (6, -3) (13) {$w$};
        \draw[->] (-1, -1) -- node[above]{double rotation} (1, -1);
        \draw[-] (0) -- (1);
        \draw[-] (1) -- (2);
        \draw[-] (2) -- (3);
        \draw[-] (2) -- (4);
        \draw[-] (1) -- (5);
        \draw[-] (0) -- (6);
        \draw[-] (7) -- (8);
        \draw[-] (8) -- (9);
        \draw[-] (7) -- (10);
        \draw[-] (8) -- (11);
        \draw[-] (9) -- (12);
        \draw[-] (9) -- (13);


    \begin{align}
        \hat{c_i} &= 2 + \operatorname{rank}_2(X) - \operatorname{rank}_1(X) + \operatorname{rank}_2(P) - \operatorname{rank}_1(P) + \operatorname{rank}_2(G) - \operatorname{rank}_1(G) \\
        &= 2 + \operatorname{rank}_2(P) + \operatorname{rank}_2(G) - \operatorname{rank}_1(X) - \operatorname{rank}_1(P) \ (\operatorname{rank}_2(X) = \operatorname{rank}_1(G)) \\
        &= 2 + \operatorname{rank}_2(P) - \operatorname{rank}_1(P) + (\operatorname{rank}_2(G) + \operatorname{rank}_1(X)) - 2\operatorname{rank}_1(X) \\
        &\leqslant 2 + 2\operatorname{rank}_2(X) - 2 + (\operatorname{rank}_2(P) - \operatorname{rank}_1(P)) - 2\operatorname{rank}_1(X) \ (\text{by the lemma}) \\
        &\leqslant 3(\operatorname{rank}_2(X) - \operatorname{rank}_1(X)) \ (\operatorname{rank}_2(P) - \operatorname{rank}_1(P) \leqslant \operatorname{rank}_2(X) - \operatorname{rank}_1(X))
    \end{align}

所以三种操作的摊还代价都满足 $\hat{c_i} = < 1 + 3(\operatorname{rank}_2(X) - \operatorname{rank}_1(X))$，接下来便是分析可能的旋转次数. 设树的高度为 $h$，则有旋转次数 

\[
    k = \begin{cases} h/2 & h \text{ is even} \\ (h - 1)/2 + 1 & h \text{ is odd} \end{cases}.
\]

$h$ 为偶数时为 Zig-Zig 或 Zig-Zag 操作，$h$ 为奇数时进行 $k - 1$ 次 Zig-Zig 或 Zig-Zag 操作，然后进行一次 Zig 操作. 所以最坏上界放缩为 $k$ 次 Zig-Zig 或 Zig-Zag 操作，以及最后一次 Zig 操作. 所以摊还代价求和为

\begin{align}
    \sum_{i = 1}^{k + 1} \hat{c_i} &\leqslant 1 + 3(\operatorname{rank}_{k + 1}(X) - \operatorname{rank}_k(X)) + \sum_{i = 1}^k 3(\operatorname{rank}_i(X) - \operatorname{rank}_{i - 1}(X)) \\
    &= 1 + 3(\operatorname{rank}_{k + 1}(X) - \operatorname{rank}_0(X)) = O(\log n).
\end{align}

所以最后总结出 Splay 树的搜索、插入和删除操作的摊还复杂度均为 $O(\log n)$.