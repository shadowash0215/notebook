# 树

## 定义

树采用的是递归定义的方式，其是节点的集合，可以是空的。若其非空，则其包含一个根节点，以及 0 个或多个子树，这些子树也是树，且是不相交的，与根节点通过边相连。

- 节点的度是其子树的个数，树的度是其所有节点中的最大度。
- 父节点是指有子树的节点，子节点是指父节点的子树的根节点，兄弟节点是指具有相同父节点的节点，而叶子节点是指度为 0 的节点。

路径是指从节点 $n_1$ 到 $n_k$ 的一个唯一序列，路径的长度是指路径上的边的个数。

- 节点的深度是指从根节点到该节点的唯一路径的长度，易知根节点的深度为 0。
- 节点的高度是指从该节点到一个叶子节点的最长路径的长度，易知叶子节点的高度为 0。而树的高度是指根节点的高度。

对于多叉树，可以将其转化为二叉树，即使用 FirstChild-NextSibling 表示法，将每个节点的第一个子节点作为其左孩子，而将其兄弟节点作为其右孩子。所以我们更多的是讨论二叉树。

## 遍历

遍历是指按照某种顺序访问树中的所有节点，比较常用的遍历的顺序分为三种：前序遍历、中序遍历和后序遍历。前序遍历是指先访问根节点，然后访问左子树，最后访问右子树；中序遍历是指先访问左子树，然后访问根节点，最后访问右子树；后序遍历是指先访问左子树，然后访问右子树，最后访问根节点。此外还有层序遍历。代码如下：

=== "PreOrder"

    ```C
    void PreOrder(Tree T) {
        if (T) {
            printf("%d ", T->data);
            PreOrder(T->left);
            PreOrder(T->right);
        }
    }
    ```

=== "InOrder"

    ```C
    void InOrder(Tree T) {
        if (T) {
            InOrder(T->left);
            printf("%d ", T->data);
            InOrder(T->right);
        }
    }
    ```

=== "PostOrder"

    ```C
    void PostOrder(Tree T) {
        if (T) {
            PostOrder(T->left);
            PostOrder(T->right);
            printf("%d ", T->data);
        }
    }
    ```

=== "LevelOrder"

    ```C
    void LevelOrder(Tree T) {
        Queue Q = CreateQueue();
        Enqueue(Q, T);
        while (!IsEmpty(Q)) {
            Tree tmp = Dequeue(Q);
            printf("%d ", tmp->data);
            if (tmp->left) Enqueue(Q, tmp->left);
            if (tmp->right) Enqueue(Q, tmp->right);
        }
    }
    ```

## 二叉树

二叉树是每个节点最多有两个子树的树结构，其子树有左右之分，其次序不能任意颠倒。二叉树的定义如下：

```C
typedef struct Node {
    int data;
    struct Node *left;
    struct Node *right;
} *Tree;
```

二叉树有如下的一些性质：其第 $i$ 层的节点数最多为 $2^{i - 1}, i \leqslant 1$，层数为 $k$ 的二叉树节点数最多为 $2^k - 1, k \geqslant 1$。对任意的非零二叉树，其满足 $n_0 = n_2 + 1$，$n_0$ 为叶节点数目，$n_2$ 为度为 2 的节点数目。

## 二叉搜索树

在应用中我们更多地使用二叉搜索树，其满足以下的性质：  
(i) 所有节点都有一以整数表示的键值，且互不相同；  
(ii) 所有左子树中节点的键值都小于根的键值；  
(iii) 所有右子树中节点的键值都大于根的键值；  
(iv) 左右子树也都是二叉搜索树。

二叉搜索树的基本操作：

=== "CreateTree"

    ```C
    Tree CreateTree(int data) {
        Tree T = (Tree)malloc(sizeof(struct Node));
        T->data = data;
        T->left = T->right = NULL;
        return T;
    }
    ```

=== "Find"

    ```C
    Tree Find(Tree T, int data) {
        if (!T) return NULL;
        if (data < T->data) return Find(T->left, data);
        else if (data > T->data) return Find(T->right, data);
        else return T;
    }

    Tree Iter_Find(Tree T, int data) {
        while (T) {
            if (data < T->data) T = T->left;
            else if (data > T->data) T = T->right;
            else return T;
        }
        return NULL;
    }
    ```

=== "FindMin"

    ```C
    Tree FindMin(Tree T) {
        if (!T) return NULL;
        else if (!T->left) return T;
        else return FindMin(T->left);
    }
    ```

=== "FindMax"

    ```C
    Tree FindMax(Tree T) {
        if (!T) return NULL;
        else if (!T->right) return T;
        else return FindMax(T->right);
    }
    ```

=== "Insert"

    ```C
    Tree Insert(Tree T, int data) {
        if (!T) {
            T = (Tree)malloc(sizeof(struct Node));
            T->data = data;
            T->left = T->right = NULL;
        } else if (data < T->data) T->left = Insert(T->left, data);
        else if (data > T->data) T->right = Insert(T->right, data);
        return T;
    }
    ```

=== "Delete"

    ```C
    Tree Delete(Tree T, int data) {
        if (!T) return NULL;
        else if (data < T->data) T->left = Delete(T->left, data);
        else if (data > T->data) T->right = Delete(T->right, data);
        else {
            if (T->left && T->right) {
                Tree tmp = FindMin(T->right);
                T->data = tmp->data;
                T->right = Delete(T->right, T->data);
            } else {
                Tree tmp = T;
                if (!T->left) T = T->right;
                else if (!T->right) T = T->left;
                free(tmp);
            }
        }
        return T;
    }
    ```

## 线索二叉树

线索二叉树的出现是为了优化二叉树的遍历，其是在二叉树的基础上增加了指向前驱和后继的指针。线索二叉树的定义如下：

```C
typedef struct Node {
    int data;
    struct Node *left;
    struct Node *right;
    int ltag, rtag;
} *Tree;
```

下面以中序线索二叉树为例，将一棵二叉树转化为线索二叉树：

```C
void InThread(Tree T, Tree &pre) {
    if (T) {
        InThread(T->left, pre);
        if (!T->left) {
            T->ltag = 1;
            T->left = pre;
        }
        if (pre && !pre->right) {
            pre->rtag = 1;
            pre->right = T;
        }
        pre = T;
        InThread(T->right, pre);
    }
}

void CreateInThread(Tree T) {
    Tree pre = NULL;
    if (T) {
        InThread(T, pre);
        pre->right = NULL;
        pre->rtag = 1;
    }
}
```

线索二叉树寻找前驱和后继的操作：

=== "InPre"

    ```C
    Tree InPre(Tree T) {
        if (T->ltag) return T->left;
        else {
            Tree tmp = T->left;
            while (!tmp->rtag) tmp = tmp->right;
            return tmp;
        }
    }
    ```

=== "InNext"

    ```C
    Tree InNext(Tree T) {
        if (T->rtag) return T->right;
        else {
            Tree tmp = T->right;
            while (!tmp->ltag) tmp = tmp->left;
            return tmp;
        }
    }
    ```

线索二叉树的遍历：

=== "InFirst"

    ```C
    Tree InFirst(Tree T) {
        Tree tmp = T;
        if (!tmp) return NULL;
        while (!tmp->ltag) tmp = tmp->left;
        return tmp;
    }
    ```
=== "InOrder"

    ```C
    void InOrder(Tree T) {
        for (Tree tmp = InFirst(T); tmp; tmp = InNext(tmp)) {
            printf("%d ", tmp->data);
        }
    }
    ```