# 左式堆, 斜堆

## 左式堆

### 左式堆的理论基础

左式堆(Leftist heap)是一种二叉堆, 但是它放弃了完全二叉树的性质，而是整体向左倾斜. 为了将这种形象化的倾斜性质量化，我们定义一个节点的零路径长(Null Path Length, NPL):

!!! info "Definition"
    把任一节点 $X$ 的零路径长 $\operatorname{NPL}(X)$ 定义为从 $X$ 到一个没有两个儿子的节点的最短路径的长. 因此，具有一个儿子的节点的 $\operatorname{NPL}$ 为 0，并且规定 $\operatorname{NPL}(\text{NULL}) = -1$. 并且每个节点的零路径长满足 $\operatorname{NPL}(X) = \operatorname{min}(\operatorname{NPL}(X->left), \operatorname{NPL}(X->right)) + 1$.

相应地，左式堆满足以下特性:

!!! info "Definition"
    对任一左式堆中的节点 $X$，其左儿子的 $\operatorname{NPL}$ 至少和右儿子的 $\operatorname{NPL}$ 一样大. 

!!! note "theorem"
    在右路径上有 $r$ 个节点的左式堆至少有 $2^r - 1$ 个结点.（右路径指从根节点到最右边的叶子节点的路径）

### 左式堆的操作

=== "节点定义"

    ```c
    typedef struct node *LeftistHeap;

    typedef struct node {
        int key;
        int npl;
        struct node *left;
        struct node *right;
    } Node;
    ```

=== "递归合并"

    ```c
    LeftistHeap merge_recursive(LeftistHeap h1, LeftistHeap h2) {
        if (h1 == NULL) return h2;
        if (h2 == NULL) return h1;
        // make sure that h1->key <= h2->key always holds
        if (h1->key > h2->key) {
            LeftistHeap temp = h1;
            h1 = h2;
            h2 = temp;
        }
        h1->right = merge_recursive(h1->right, h2);
        /* swap left and right if necessary
        in case that the left child is NULL */
        if (h1->left == NULL) {
            h1->left = h1->right;
            h1->right = NULL;
        } else {
            if (h1->left->npl < h1->right->npl) {
                LeftistHeap temp = h1->left;
                h1->left = h1->right;
                h1->right = temp;
            }
            h1->npl = h1->right->npl + 1;
        }
        return h1;
    }
    ```

=== "迭代合并"

    ```c
    void npl_update(LeftistHeap h) {
        if (h == NULL) return;
        h->npl = h->right == NULL ? 0 : h->right->npl + 1;
    }

    LeftistHeap merge_iterative(LeftistHeap h1, LeftistHeap h2) {
        if (h1 == NULL) return h2;
        if (h2 == NULL) return h1;
        LeftistHeap stack[MAX_STACK_SIZE] = {NULL};
        int top = -1;
        LeftistHeap h = NULL;
        LeftistHeap *p = &h;
        while (h1 != NULL && h2 != NULL) {
            if (h1->key > h2->key) {
                LeftistHeap temp = h1;
                h1 = h2;
                h2 = temp;
            }
            stack[++top] = h1;
            *p = h1;
            p = &h1->right;
            LeftistHeap next = h1->right;
            h1->right = h2;
            h1 = next;
        }
        *p = h1 == NULL ? h2 : h1;
        while (top >= 0) {
            npl_update(stack[top--]);
        }
        return h;
    }
    ```

## 斜堆

斜堆就不再需要维护 $\operatorname{NPL}$ 了，每轮合并采取的操作如下：

1. Base case: $H$ 与 NULL 连接时，$H$ 的右路径上除了最大结点之外都必须交换其左右孩子。

2. 递归步骤: 若 $H_1$ 的根结点小于 $H_2$，则将 $H_1$ 的左孩子换到右孩子的位置，然后把新合并的插入在 $H_1$ 的左子
树上。

### 斜堆的摊还分析

!!! info "Definition"
    称一个结点 $P$ 是**重的（heavy）**，如果它的右子树结点个数至少是 $P$ 所有后代的一半（后代包括 $P$ 本身）。反之，称 $P$ 是**轻的（light）**。

!!! success "Lemma"
    对于右路径上有 $l$ 个轻结点的斜堆，整个斜堆至少有 $2^l - 1$ 个结点。也就是说，拥有 $n$ 个结点的斜堆的右路径上的轻结点个数为 $O(\log n)$。

这就意味着，斜堆的右路径上的轻结点个数总不会太多，是可以被控制住的。

!!! note "Theorem"
    若斜堆 $H_1$ 和 $H_2$ 分别有 $n_1$ 和 $n_2$ 个结点，则合并 $H_1$ 和 $H_2$ 的摊还时间复杂度为 $O(\log n)$，其中 $n = n_1 + n_2$.

    ??? note "Proof"
        定义势函数 $\Phi(H_i)$ 等于堆 $H_i$ 的重结点的个数，并设 $H_3$ 为合并后的新堆。设 $H_i(i = 1, 2)$ 的右路径上的轻结点数量为 $l_i$，重结点数量为 $h_i$，所以真实合并操作的最坏代价为 $c_i = l_1 + l_2 + h_1 + h_2$，也就是所有的操作都在右路径上完成，因此根据摊还分析我们知道摊还代价为 
        
        \[
            \hat{c_i} = c_i + \Phi(H_3) - (\Phi(H_1) + \Phi(H_2)).
        \]

        在合并之前我们也可以记

        \[
            \Phi(H_1) + \Phi(H_2) = h_1 + h_2 + h,
        \]

        其中 h 表示不在右路径上的重结点个数。那么为了计算势函数的变化，我们需要考虑究竟哪一部分的会发生变化，事实上有如下两点：

        1. 只有在 $H_1$ 和 $H_2$ 右路径上的结点才可能改变轻重状态；
        2. $H_1$ 和 $H_2$ 右路径上的重结点在合并后一定会变成轻结点，这是因为右路径上结点一定会交换左右子树，并且后续所有结点也都会继续插入在左子树上，但轻结点未必会变为重结点。

        所以 $h$ 保持不变，$h_1 + h_2$ 个重结点转变为轻结点，$l_1 + l_2$ 个轻结点未必变重，所以有

        \[
            \Phi(H_3) \leqslant h + l_1 + l_2,
        \]

        代入可得

        \[
            \hat{c_i} \leqslant (l_1 + l_2 + h_1 + h_2) + (l_1 + l_2 + h) − (h_1 + h_2 + h) = 2(l_1 + l_2). 
        \]

        而 $l_1 + l_2 = O(\log n_1 + \log n_2)= O(\log(n_1 + n_2)) = O(\log n)$，并且注意到初始（空堆）势函数一定为 0，且之后总是非负的，所以这一势函数定义满足要求，证明完成。