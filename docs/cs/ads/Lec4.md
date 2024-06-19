# 左式堆, 斜堆

## 左式堆

### 左式堆的理论基础

左式堆(Leftist heap)是一种二叉堆, 但是它放弃了完全二叉树的性质，而是整体向左倾斜. 为了将这种形象化的倾斜性质量化，我们定义一个节点的零路径长(Null Path Length, NPL):

!!! info "defination"
    把任一节点 $X$ 的零路径长 $\operatorname{NPL}(X)$ 定义为从 $X$ 到一个没有两个儿子的节点的最短路径的长. 因此，具有一个儿子的节点的 $\operatorname{NPL}$ 为 0，并且规定 $\operatorname{NPL}(\text{NULL}) = -1$. 并且每个节点的零路径长满足 $\operatorname{NPL}(X) = \operatorname{min}(\operatorname{NPL}(X->left), \operatorname{NPL}(X->right)) + 1$.

相应地，左式堆满足以下特性:

!!! info "defination"
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