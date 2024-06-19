# 并查集

并查集是一种树形的数据结构，用于处理一些不相交集合的合并及查询问题。

- 合并：将一棵树的根节点作为另一棵树的根节点的子节点。
- 查询：判断两个节点是否在同一棵树上，即判断两个节点的根节点是否相同。

一般来说，我们可以用数组来表示一棵树，数组的下标表示节点，数组的值表示父节点。

但是直接合并两棵树的根节点会导致树的高度变高，从而影响查询效率。因此我们需要对树进行优化，使得树的高度尽可能的低。以下是三种优化方法：

- 按大小合并：将节点数较少的树的根节点作为节点数较多的树的根节点的子节点。
- 按秩合并：将高度较小的树的根节点作为高度较大的树的根节点的子节点。
- 路径压缩：在查询的过程中，将节点的父节点直接设为根节点。

按大小合并时需要将根节点的值设为负数，表示该树的节点数。实现代码如下：

=== "Init"

    ```c
    void Init(int n) {
        for (int i = 0; i < n; i++) {
            parent[i] = -1;
        }
    }
    ```

=== "Find"

    ```c
    int Find(int x) {
        if (parent[x] < 0) {
            return x;
        } else {
            return parent[x] = Find(parent[x]); /* 路径压缩 */
        }
    }
    ```

=== "Union"

    ```c
    void Union(int x, int y) {
        int root1 = Find(x);
        int root2 = Find(y);
        if (root1 == root2) {
            return;
        }
        if (parent[root1] < parent[root2]) {
            parent[root1] += parent[root2];
            parent[root2] = root1;
        } else {
            parent[root2] += parent[root1];
            parent[root1] = root2;
        }
    }
    ```

按大小压缩形成的拥有 $N$ 个节点的树的高度不会超过 $\log_2 N + 1$，因此进行 $N$ 次 Union 操作和 $M$ 次 Find 操作的时间复杂度为 $O(N + M\log_2 N)$。

按秩合并时需要利用数组记录每个节点的高度，实现代码如下：

=== "Init"

    ```c
    void Init(int n) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }
    ```

=== "Find"

    ```c
    int Find(int x) {
        if (parent[x] == x) {
            return x;
        } else {
            return Find(parent[x]);
        }
    }
    ```

=== "Union"

    ```c
    void Union(int x, int y) {
        int root1 = Find(x);
        int root2 = Find(y);
        if (root1 == root2) {
            return;
        }
        if (rank[root1] < rank[root2]) {
            parent[root1] = root2;
        } else {
            parent[root2] = root1;
            if (rank[root1] == rank[root2]) {
                rank[root1]++;
            }
        }
    }
    ```

按秩合并不建议和路径压缩一起使用，因为路径压缩会改变树的高度，从而使得秩的信息失效。