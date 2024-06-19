# 红黑树, B+ 树

## 红黑树

红黑树的定义满足以下性质：

1. 每个结点要么是红的，要么是黑的。
2. 根结点是黑的。
3. 每个叶结点（NIL 结点，空结点）是黑的。
4. 如果一个结点是红的，那么它的两个儿子都是黑的。
5. 对每个结点，从该结点到其所有后代叶结点的简单路径上，均包含相同数目的黑色结点。

### 复杂度证明

<!-- TODO -->

### 插入

=== "Case 1"

    \automata
        \node[state, black] at (-3, 0) (0) {$a$};
        \node[state, red] at (-4, -1) (2) {$b$};
        \node[state, red] at (-2, -1) (1) {$c$};
        \node[state, red] at (-5, -2) (3) {$d$};
        \node[state, red] at (3, 0) (4) {$a$};
        \node[state, black] at (2, -1) (5) {$b$};
        \node[state, black] at (4, -1) (6) {$c$};
        \node[state, red] at (1, -2) (7) {$d$};
        \draw[->] (-1, -1) -- node[above]{color $b, c$ black} node[below]{color $a$ red} (1, -1);
        \draw[-] (0) -- (1);
        \draw[-] (0) -- (2);
        \draw[-] (2) -- (3);
        \draw[-] (4) -- (5);
        \draw[-] (4) -- (6);
        \draw[-] (5) -- (7);

    将情况递归到父亲的父亲。

=== "Case 2"

    \automata
        \node[state, black] at (-3, 0) (0) {$a$};
        \node[state, red] at (-4, -1) (2) {$b$};
        \node[state, black] at (-2, -1) (1) {$c$};
        \node[state, red] at (-3, -2) (3) {$d$};
        \node[state, black] at (3, 0) (4) {$a$};
        \node[state, red] at (2, -1) (5) {$d$};
        \node[state, black] at (4, -1) (6) {$c$};
        \node[state, red] at (1, -2) (7) {$b$};
        \draw[->] (-3.7, -2.3) arc (-10: 100: 0.5);
        \draw[->] (-1, -1) -- node[above]{leftRotate($b$)} (1, -1);
        \draw[-] (0) -- (1);
        \draw[-] (0) -- (2);
        \draw[-] (2) -- (3);
        \draw[-] (4) -- (5);
        \draw[-] (4) -- (6);
        \draw[-] (5) -- (7);
        
    \automata
        \node[state, black] at (-6, 0) (0) {$a$};
        \node[state, red] at (-7, -1) (1) {$b$};
        \node[state, black] at (-5, -1) (2) {$c$};
        \node[state, red] at (-6, -2) (3) {$d$};
        \node[state, red] at (0, 0) (4) {$a$};
        \node[state, black] at (-1, -1) (5) {$b$};
        \node[state, black] at (1, -1) (6) {$c$};
        \node[state, red] at (0, -2) (7) {$d$};
        \node[state, black] at (5, 0) (8) {$b$};
        \node[state, red] at (6, -1) (9) {$a$};
        \node[state, red] at (5, -2) (10) {$d$};
        \node[state, black] at (7, -2) (11) {$c$};
        \draw[->] (-0.25, -1) arc (190: -10: 0.3);
        \draw[->] (-4, -1) -- (-2, -1);
        \draw[->] (2, -1) -- (4, -1);
        \draw[-] (0) -- (1);
        \draw[-] (0) -- (2);
        \draw[-] (1) -- (3);
        \draw[-] (4) -- (5);
        \draw[-] (4) -- (6);
        \draw[-] (5) -- (7);
        \draw[-] (8) -- (9);
        \draw[-] (9) -- (11);
        \draw[-] (9) -- (10);

=== "Case 3"

    \automata
        \node[state, black] at (-6, 0) (0) {$a$};
        \node[state, red] at (-7, -1) (1) {$b$};
        \node[state, black] at (-5, -1) (2) {$c$};
        \node[state, red] at (-8, -2) (3) {$d$};
        \node[state, red] at (0, 0) (4) {$a$};
        \node[state, black] at (-1, -1) (5) {$b$};
        \node[state, black] at (1, -1) (6) {$c$};
        \node[state, red] at (-2, -2) (7) {$d$};
        \node[state, black] at (6, 0) (8) {$b$};
        \node[state, red] at (7, -1) (9) {$a$};
        \node[state, red] at (5, -1) (10) {$d$};
        \node[state, black] at (8, -2) (11) {$c$};
        \draw[->] (-0.25, -1) arc (190: -10: 0.3);
        \draw[->] (-4, -1) -- node[above]{color $a$ red} node[below]{color $b$ black} (-2, -1);
        \draw[->] (2, -1) -- node[above]{rightRotate($a$)} (4, -1);
        \draw[-] (0) -- (1);
        \draw[-] (0) -- (2);
        \draw[-] (1) -- (3);
        \draw[-] (4) -- (5);
        \draw[-] (4) -- (6);
        \draw[-] (5) -- (7);
        \draw[-] (8) -- (9);
        \draw[-] (8) -- (10);
        \draw[-] (9) -- (11);

### 删除

与 BST 的删除类似，寻找前驱或后继结点替换。

- 递归到最后就是删除“叶子结点”。
- 需要维持红黑树的性质。
    - 红色：直接删除。
    - 黑色：需要在到达此结点的简单路径上添加一个黑色结点，并且不改变其余结点的 $\operatorname{bh}$。依据兄弟与叔侄关系判断

=== "Case 1"

    \automata
        \node[state, black] at (-6, 0) (0) {$a$};
        \node[state, black] at (-7, -1) (1) {$x$};
        \node[state, red] at (-5, -1) (2) {$b$};
        \node[state, black] at (-6, -2) (3) {$c$};
        \node[state, black] at (-4, -2) (4) {$d$};
        \node[state, red] at (0, 0) (5) {$a$};
        \node[state, black] at (-1, -1) (6) {$x$};
        \node[state, black] at (1, -1) (7) {$b$};
        \node[state, black] at (0, -2) (8) {$c$};
        \node[state, black] at (2, -2) (9) {$d$};
        \node[state, black] at (6, 0) (10) {$b$};
        \node[state, red] at (5, -1) (11) {$a$};
        \node[state, black] at (7, -1) (12) {$d$};
        \node[state, black] at (4, -2) (13) {$x$};
        \node[state, black] at (6, -2) (14) {$c$};
        \node(tip1) at (-7, -3){node to be deleted};
        \node(tip2) at (8, 0){node we need};
        \draw[->] (0.3, -1) arc (-10: 190: 0.3);
        \draw[->] (-4, -1) -- node[above]{color $a$ red} node[below]{color $b$ black} (-2, -1);
        \draw[->] (2, -1) -- node[above]{leftRotate($a$)} (4, -1);
        \draw[->] (1) -- (tip1);
        \draw[->] (10) -- (tip2);
        \draw[-] (0) -- (1);
        \draw[-] (0) -- (2);
        \draw[-] (2) -- (3);
        \draw[-] (2) -- (4);
        \draw[-] (5) -- (6);
        \draw[-] (5) -- (7);
        \draw[-] (7) -- (8);
        \draw[-] (7) -- (9);
        \draw[-] (10) -- (11);
        \draw[-] (10) -- (12);
        \draw[-] (11) -- (13);
        \draw[-] (11) -- (14);

    兄弟为红色，只需要花费一次旋转操作。

=== "Case 2"

    \automata
        \node[state, blue] at (-6, 1) (0) {$a$};
        \node[state, black] at (-7, 0) (1) {$x$};
        \node[state, black] at (-5, 0) (2) {$b$};
        \node[state, black] at (-6, -1) (3) {$c$};
        \node[state, black] at (-4, -1) (4) {$d$};
        \node[state, red] at (0, 3) (5) {$a$};
        \node[state, black] at (-1, 2) (6) {$x$};
        \node[state, black] at (1, 2) (7) {$b$};
        \node[state, black] at (0, 1) (8) {$c$};
        \node[state, black] at (2, 1) (9) {$d$};
        \node[state, black] at (6, 3) (10) {$a$};
        \node[state, black] at (5, 2) (11) {$x$};
        \node[state, red] at (7, 2) (12) {$b$};
        \node[state, black] at (6, 1) (13) {$c$};
        \node[state, black] at (8, 1) (14) {$d$};
        \node[state, black] at (0, -1) (15) {$a$};
        \node[state, black] at (-1, -2) (16) {$x$};
        \node[state, black] at (1, -2) (17) {$b$};
        \node[state, black] at (0, -3) (18) {$c$};
        \node[state, black] at (2, -3) (19) {$d$};
        \node[state, black] at (6, -1) (20) {$a$};
        \node[state, black] at (5, -2) (21) {$x$};
        \node[state, red] at (7, -2) (22) {$b$};
        \node[state, black] at (6, -3) (23) {$c$};
        \node[state, black] at (8, -3) (24) {$d$};
        \node(tip1) at (-7, -2){black $\times 2$};
        \node(tip2) at (8, -1){black $\times 2$};
        \node(tip3) at (10, -2) {$other \ cases$};
        \node(tip4) at (8, 3){node we need};
        \node[rotate = 270] at (-1.9, 0) {$\underbrace{\hspace{6cm}}$};
        \draw[->] (-4, 0) -- (-2, 0);
        \draw[->] (2, 2) -- node[above]{color $a$ black} node[below]{color $b$ red} (4, 2);
        \draw[->] (2, -2) -- node[above]{color $a$ black} node[below]{color $b$ red} (4, -2);
        \draw[->] (1) -- (tip1);
        \draw[->] (20) -- (tip2);
        \draw[->] (8, -2) -- (tip3);
        \draw[->] (10) -- (tip4);
        \draw[-] (0) -- (1);
        \draw[-] (0) -- (2);
        \draw[-] (2) -- (3);
        \draw[-] (2) -- (4);
        \draw[-] (5) -- (6);
        \draw[-] (5) -- (7);
        \draw[-] (7) -- (8);
        \draw[-] (7) -- (9);
        \draw[-] (10) -- (11);
        \draw[-] (10) -- (12);
        \draw[-] (12) -- (13);
        \draw[-] (12) -- (14);
        \draw[-] (15) -- (16);
        \draw[-] (15) -- (17);
        \draw[-] (17) -- (18);
        \draw[-] (17) -- (19);
        \draw[-] (20) -- (21);
        \draw[-] (20) -- (22);
        \draw[-] (22) -- (23);
        \draw[-] (22) -- (24);

    兄弟为黑色，且两个侄子也都是黑色，“将自己和兄弟的黑色传给父亲”。如果父亲是红色，则将父亲变为黑色，兄弟变为红色；如果父亲是黑色，则兄弟变为红色，并将情况递归到父亲。无需旋转。

=== "Case 3"

    \automata
        \node[state, blue] at (-6, 0) (0) {$a$};
        \node[state, black] at (-7, -1) (1) {$x$};
        \node[state, black] at (-5, -1) (2) {$b$};
        \node[state, red] at (-6, -2) (3) {$c$};
        \node[state, black] at (-4, -2) (4) {$d$};
        \node[state, blue] at (0, 0) (5) {$a$};
        \node[state, black] at (-1, -1) (6) {$x$};
        \node[state, red] at (1, -1) (7) {$b$};
        \node[state, black] at (0, -2) (8) {$c$};
        \node[state, black] at (2, -2) (9) {$d$};
        \node[state, blue] at (6, 0) (10) {$a$};
        \node[state, black] at (5, -1) (11) {$x$};
        \node[state, black] at (7, -1) (12) {$c$};
        \node[state, red] at (8, -2) (13) {$b$};
        \node[state, black] at (9, -3) (14) {$d$};
        \node(tip) at (10, -1){$Case \ 4$};
        \draw[->] (0.75, -2) arc (190: -10: 0.3);
        \draw[->] (-4, -1) -- node[above]{color $b$ red} node[below]{color $c$ black} (-2, -1);
        \draw[->] (2, -1) -- node[above]{rightRotate($b$)} (4, -1);
        \draw[->] (8, -1) -- (tip);
        \draw[-] (0) -- (1);
        \draw[-] (0) -- (2);
        \draw[-] (2) -- (3);
        \draw[-] (2) -- (4);
        \draw[-] (5) -- (6);
        \draw[-] (5) -- (7);
        \draw[-] (7) -- (8);
        \draw[-] (7) -- (9);
        \draw[-] (10) -- (11);
        \draw[-] (10) -- (12);
        \draw[-] (12) -- (13);
        \draw[-] (13) -- (14);

    兄弟为黑色，近侄子为红色，远侄子为黑色，“这样没法传黑色”。需要先将近侄子变为黑色，兄弟变为红色，然后进行一次右旋转，转变为 Case 4。（近侄子和兄弟的颜色变化不会影响内部的 $\operatorname{bh}$）

=== "Case 4"

    \automata
        \node[state, blue] at (-7, 0) (0) {$a$};
        \node[state, black] at (-8, -1) (1) {$x$};
        \node[state, black] at (-6, -1) (2) {$b$};
        \node[state, blue] at (-7, -2) (3) {$c$};
        \node[state, red] at (-5, -2) (4) {$d$};
        \node[state, black] at (0, 0) (5) {$a$};
        \node[state, black] at (-1, -1) (6) {$x$};
        \node[state, blue] at (1, -1) (7) {$b$};
        \node[state, blue] at (0, -2) (8) {$c$};
        \node[state, black] at (2, -2) (9) {$d$};
        \node[state, blue] at (6, 0) (10) {$b$};
        \node[state, black] at (5, -1) (11) {$a$};
        \node[state, black] at (7, -1) (12) {$d$};
        \node[state, black] at (4, -2) (13) {$x$};
        \node[state, blue] at (6, -2) (14) {$c$};
        \node(tip) at (4, 0){node we need};
        \draw[->] (0.3, -1) arc (-10: 190: 0.3);
        \draw[->] (-5, -1) -- node[above]{exchange $a.color$, $b.color$} node[below]{color $d$ black} (-2, -1);
        \draw[->] (2, -1) -- node[above]{leftRotate($a$)} (4, -1);
        \draw[->] (11) -- (tip);
        \draw[-] (0) -- (1);
        \draw[-] (0) -- (2);
        \draw[-] (2) -- (3);
        \draw[-] (2) -- (4);
        \draw[-] (5) -- (6);
        \draw[-] (5) -- (7);
        \draw[-] (7) -- (8);
        \draw[-] (7) -- (9);
        \draw[-] (10) -- (11);
        \draw[-] (10) -- (12);
        \draw[-] (11) -- (13);
        \draw[-] (11) -- (14);

    兄弟为黑色，远侄子为红色，“最复杂的一种情况”。因为常规思路是哪里不平衡需要减轻其不平衡程度，但是这里的反而先加重了，因为最后会将“叶子结点”删去，需要有结点去平衡其删除后的影响。首先将父亲和兄弟的颜色互换，并且将远侄子变为黑色。然后对父亲进行一次左旋。注意到 $\operatorname{bh}(c) = \operatorname{bh}(d) = 0$，且 $\operatorname{bh}(b) = 1$，所以左旋后的树各结点的 $\operatorname{bh}$ 不变。

## B+ 树

B+ 树是一种多路搜索树，其定义满足以下性质：

- 根结点要么是叶子结点，要么有 $2$ 到 $M$ 个子结点，其中 $M$ 是树的阶数；
- 除根结点外的所有非叶子结点有 $\lceil M/2 \rceil$ 到 $M$ 个子结点；
- 所有叶子结点拥有相同的深度。（假设所有的非根的叶子结点也有 $\lceil M/2 \rceil$ 到 $M$ 个子结点，子结点指键值）

### 插入

=== "头文件定义"

    ```c
    #ifndef _BP_TREE_H_
    #define _BP_TREE_H_
    #define MAX 3
    #define MAXN 10005
    typedef struct node *Tree;
    typedef struct node
    {
        int size;
        int isLeaf;
        int key[MAX + 1];
        Tree parent;
        Tree child[MAX + 1];
    } Node;
    int InsertValue(Tree p, int key);
    Tree InsertLeaf(Tree root, int key);
    Tree SplitLeaf(Tree p, Tree parent, Tree root, int key);
    Tree InsertInternal(Tree p, Tree Lefttree, Tree Righttree, Tree root, int key);
    void PrintTree(Tree root);
    #endif
    ```

=== "插入键值并返回插入位置"

    ```c
    int InsertValue(Tree p, int key) {
        int i = 0;
        while (i < p->size && key > p->key[i]) {
            i++;
        }
        if (key == p->key[i]) {
            printf("Key %d is duplicated\n", key);
            return -1;
        };
        for (int j = p->size; j > i; j--) {
            p->key[j] = p->key[j - 1];
        }
        p->key[i] = key;
        p->size++;
        return i;
    }
    ```

=== "叶结点插入"

    ```c
    Tree InsertLeaf(Tree root, int key) {
        if (!root) {
            root = (Tree)malloc(sizeof(Node));
            root->size = 1;
            root->isLeaf = 1;
            root->key[0] = key;
            root->parent = NULL;
            for (int i = 0; i < MAX; i++) {
                root->child[i] = NULL;
            }
        } else {
            Tree p = root;
            Tree parent = NULL;
            while (!p->isLeaf) {
                parent = p;
                for (int i = 0; i < p->size; i++) {
                    if (key < p->key[i]) {
                        p = p->child[i];
                        break;
                    }
                    if (i == p->size - 1) {
                        p = p->child[i + 1];
                        break;
                    }
                }
            }
            if (p->size < MAX) {
                if (InsertValue(p, key) == -1) {
                    return root;
                }
                p->parent = parent;
            } else {
                root = SplitLeaf(p, parent, root, key);
            }
        }
        return root;
    }
    ```

=== "叶结点分裂"

    ```c
    Tree SplitLeaf(Tree p, Tree parent, Tree root, int key) {
        Tree LeftTree = (Tree)malloc(sizeof(Node));
        Tree RightTree = (Tree)malloc(sizeof(Node));
        if (InsertValue(p, key) == -1) {
            return root;
        }
        LeftTree->size = (MAX + 1) / 2;
        RightTree->size = MAX + 1 - (MAX + 1) / 2;
        LeftTree->isLeaf = RightTree->isLeaf = 1;
        for (int i = 0; i < LeftTree->size; i++) {
            LeftTree->key[i] = p->key[i];
        }
        for (int i = 0; i < RightTree->size; i++) {
            RightTree->key[i] = p->key[i + LeftTree->size];
        }
        if (p == root) {
            Tree newRoot = (Tree)malloc(sizeof(Node));
            newRoot->size = 1;
            newRoot->key[0] = RightTree->key[0];
            newRoot->isLeaf = 0;
            newRoot->child[0] = LeftTree;
            newRoot->child[1] = RightTree;
            root = newRoot;
            LeftTree->parent = RightTree->parent = newRoot;
        } else {
            root = InsertInternal(parent, LeftTree, RightTree, root, RightTree->key[0]);
        }
        return root;
    }
    ```

=== "内部结点插入（含分裂）"

    ```c
    Tree InsertInternal(Tree p, Tree LeftTree, Tree RightTree, Tree root, int key) {
        if (p->size < MAX - 1) { // insert directly
            int i = InsertValue(p, key);
            if (i == -1) {
                return root;
            }
            for (int j = p->size; j > i + 1; j--) {
                p->child[j] = p->child[j - 1];
            }
            p->child[i] = LeftTree;
            p->child[i + 1] = RightTree;
            LeftTree->parent = RightTree->parent = p;
        } else { // split internal
            Tree LeftChild = (Tree)malloc(sizeof(Node));
            Tree RightChild = (Tree)malloc(sizeof(Node));
            Tree ptrarray[MAX + 1];
            for(int i = 0; i < MAX + 1; i++) {
                ptrarray[i] = NULL;
            }
            for(int i = 0; i < MAX + 1; i++) {
                ptrarray[i] = p->child[i];
            }
            int i = InsertValue(p, key);
            if (i == -1) {
                return root;
            }
            for (int j = MAX + 1; j > i + 1; j--) {
                ptrarray[j] = ptrarray[j - 1];
            }
            ptrarray[i] = LeftTree;
            ptrarray[i + 1] = RightTree;
            LeftChild->isLeaf = RightChild->isLeaf = 0;
            // the size is number of children - 1
            LeftChild->size = (MAX + 1) / 2 - 1;
            RightChild->size = (MAX + 1) - (MAX + 1) / 2 - 1;
            // note that the most left branch of right child dose not need a key
            for (int i = 0; i < LeftChild->size; i++) {
                LeftChild->key[i] = p->key[i];
            }
            for (int i = 0; i < RightChild->size; i++) {
                RightChild->key[i] = p->key[i + LeftChild->size + 1];
            }
            for (int i = 0; i < LeftChild->size + 1; i++) {
                LeftChild->child[i] = ptrarray[i];
                LeftChild->child[i]->parent = LeftChild;
            }
            for (int i = 0; i < RightChild->size + 1; i++) {
                RightChild->child[i] = ptrarray[i + LeftChild->size + 1];
                RightChild->child[i]->parent = RightChild;
            }
            if (p == root) {
                Tree newRoot = (Tree)malloc(sizeof(Node));
                newRoot->size = 1;
                newRoot->key[0] = p->key[LeftChild->size];
                newRoot->isLeaf = 0;
                newRoot->child[0] = LeftChild;
                newRoot->child[1] = RightChild;
                root = newRoot;
                LeftChild->parent = RightChild->parent = newRoot;
            } else {
                root = InsertInternal(p->parent, LeftChild, RightChild, root, p->key[LeftChild->size]);
            }
        }
        return root;
    }
    ```