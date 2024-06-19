# 图

## 定义

$G(V, E)$ 表示一个图，其中 $V$ 表示顶点集合，$E$ 表示边集合。

- 对于无向图，$E$ 中的元素为无序对 $(v_i, v_j)$，表示顶点 $v_i$ 和 $v_j$ 之间存在一条边。
- 对于有向图，$E$ 中的元素为有序对 $\langle v_i, v_j \rangle$，表示顶点 $v_i$ 到 $v_j$ 之间存在一条边。
- 自环和重边都是不允许的。

**完全图**是指同等节点数量下拥有最多边数的图。

无向图中节点 $v_i, v_j$ 被称为**邻接**的，当且仅当 $(v_i, v_j) \in E$。有向图中节点 $v_i$ 被称为邻接到 $v_j$，或 $v_j$ 从 $v_i$ 邻接而来，当且仅当 $\langle v_i, v_j \rangle \in E$。

**子图** $G'$ 满足 $V(G') \subset V(G)$ 且 $E(G') \subset E(G)$。

$G$ 中从 $v_p$ 到 $v_q$ 的一条**路径**是指一串序列 $\{v_p, v_{i1}, v_{i2}, \ldots, v_{in}, v_q\}$，满足 $(v_{i1}, v_{i2}), (v_{i2}, v_{i3}), \ldots, (v_{in-1}, v_{in}) \in E$（无向图）或 $\langle v_{i1}, v_{i2} \rangle, \langle v_{i2}, v_{i3} \rangle, \ldots, \langle v_{in-1}, v_{in} \rangle \in E$（有向图）。

- 路径的长度指路径中边的数量。
- 简单路径是指路径中不包含重复节点的路径。
- 环是指起点和终点相同的路径。
- 无向图中 $v_i$ 和 $v_j$ 被称为**连通**的，当且仅当 $G$ 中存在一条从 $v_i$ 到 $v_j$ 的路径。
- 无向图 $G$ 被称为**连通图**，当且仅当 $G$ 中任意两个节点都是连通的。
- 无向图的**联通成分**是指无向图的极大连通子图。
- 有向图中 $v_i$ 和 $v_j$ 被称为**强连通**的，当且仅当 $G$ 中存在一条从 $v_i$ 到 $v_j$ 的路径和一条从 $v_j$ 到 $v_i$ 的路径。
- 有向图 $G$ 被称为**强连通图**，当且仅当 $G$ 中任意两个节点都是强连通的。有向图的**强连通成分**是指有向图的极大强连通子图。
- 有向图 $G$ 被称为**弱连通图**，当且仅当 $G$ 的基础图（去掉所有边的方向）是连通图。

所以树是联通且无环的无向图，而 DAG 是无环的有向图。

节点 $v_i$ 的**度**是指与 $v_i$ 相邻接的边的数量。

- 无向图中所有节点的度的和等于边的数量的两倍。
- 有向图中节点 $v_i$ 的**入度**是指以 $v_i$ 为终点的边的数量，**出度**是指以 $v_i$ 为起点的边的数量。
- 有向图中所有节点的入度的和等于出度的和，也等于边的数量。

## 表示方式

=== "adjacency matrix"

    ```c
    #define MaxN 100
    int G[MaxN][MaxN];
    ```

=== "adjacency list"

    ```c 
    typedef struct ArcNode { // 边节点
        int adjvex; // 顶点下标
        int weight; // 权值
        struct ArcNode *nextarc; // 指向下一个邻接点
    } ArcNode;
    
    typedef struct VNode { // 顶点节点
        int data; // 顶点信息
        ArcNode *firstarc; // 指向第一个邻接点
    } VNode, AdjList[MaxN];

    typedef struct {
        AdjList vertices; // 邻接表
        int vexnum, arcnum; // 顶点数和边数
    } ALGraph;

    /*Vnode 是起始节点，最后的实现效果是类似 0-->1-->2-->3-->4-->5-->NULL
    其中 0 是 VNode，firstarc 指向 0 到 1 的边，1 是第一个 ArcNode 的 adjvex，其 nextarc 指向 1 到 2 的边*/
    ```

## 建图

=== "adjacency matrix"

    ```c
    #define MaxN 100
    int G[MaxN][MaxN];
    int n, e;

    void BuildGraph() {
        scanf("%d %d", &n, &e);
        for (int i = 0; i < e; i++) {
            int u, v;
            scanf("%d %d %d", &u, &v, &w);
            G[u][v] = w;
            G[v][u] = w;
        }
    }
    ```

=== "adjacency list"

    ```c
    void BuildGraph(ALGraph *G) { // 建立无向图的邻接表
        scanf("%d %d", &G->vexnum, &G->arcnum); // 读入顶点数和边数
        for (int i = 1; i <= G->vexnum; i++) {
            scanf("%d", &G->vertices[i].data); // 读入顶点信息
            G->vertices[i].firstarc = NULL; // 初始化邻接表
        }
        for (int i = 0; i < G->arcnum; i++) {
            int u, v, w; // 读入边的信息
            scanf("%d %d %d", &u, &v, &w); 
            ArcNode *arc = (ArcNode *)malloc(sizeof(ArcNode));
            arc->adjvex = v;  // 邻接点下标
            arc->weight = w; // 权值
            arc->nextarc = G->vertices[u].firstarc; // 插入到表头
            G->vertices[u].firstarc = arc; // 更新表头

            arc = (ArcNode *)malloc(sizeof(ArcNode));
            arc->adjvex = u;  // 邻接点下标
            arc->weight = w; // 权值
            arc->nextarc = G->vertices[v].firstarc; // 插入到表头
            G->vertices[v].firstarc = arc; // 更新表头
        }   
    }
    ```

## 拓扑排序

AOV 网络的节点表示活动，边表示活动之间的先后关系。

- 可以实现的 AOV 网络一定是 DAG。
- 若存在一条从 $v_i$ 到 $v_j$ 的路径，则称 $v_i$ 是 $v_j$ 的**前驱**，$v_j$ 是 $v_i$ 的**后继**。
- 若存在边 $\langle v_i, v_j \rangle$，则称 $v_i$ 是 $v_j$ 的**直接前驱**，$v_j$ 是 $v_i$ 的**直接后继**。
- 偏序关系满足传递性和**反自反性**（注意这里和数学上的定义不一样）。
- 拓扑排序是指将所有节点排成一个序列，使得所有的偏序关系都被满足。也就是说，如果 $v_i$ 是 $v_j$ 的前驱，则 $v_i$ 在序列中出现在 $v_j$ 之前。

```C

void TopologicalSort(ALGraph *G) {
    int indegree[MaxN] = {0}; // 入度数组
    for (int i = 1; i <= G->vexnum; i++) { // 初始化入度数组
        for (ArcNode *arc = G->vertices[i].firstarc; arc; arc = arc->nextarc) {
            indegree[arc->adjvex]++;
        }
    }
    Queue Q = CreateQueue(MaxN); // 创建队列
    for (int i = 1; i <= G->vexnum; i++) { // 将入度为 0 的节点入队
        if (!indegree[i]) {
            Enqueue(Q, i);
        }
    }
    int cnt = 0; // 计数器
    while (!IsEmpty(Q)) {
        int v = Dequeue(Q); // 出队
        printf("%d ", v); // 输出
        cnt++;
        for (ArcNode *arc = G->vertices[v].firstarc; arc; arc = arc->nextarc) { // 将所有邻接点的入度减一
            int w = arc->adjvex;
            if (--indegree[w] == 0) { // 若入度为 0，则入队
                Enqueue(Q, w);
            }
        }
    }
    if (cnt != G->vexnum) { // 若计数器不等于顶点数，则说明存在环
        printf("Graph has a cycle");
    }
    free(Q);
}
```

## 最短路径

- 单源最短路径：给定图 $G$ 和源节点 $s$，求 $s$ 到 $G$ 中所有节点的最短路径。
    - 无向无权图：使用 BFS。
    - 无向正权图：使用 Dijkstra 算法。

```C

void Dijkstra(ALGraph *G, int src) {
    int dist[MaxN] = {0}; // 距离数组
    int visited[MaxN] = {0}; // 访问数组
    for (int i = 1; i <= G->vexnum; i++) { // 初始化
        dist[i] = INT_MAX;
    }
    dist[src] = 0;
    visited[src] = 1;
    for (ArcNode *arc = G->vertices[src].firstarc; arc; arc = arc->nextarc) { // 初始化 dist
        dist[arc->adjvex] = arc->weight;
    }
    for (int i = 1; i < G->vexnum; i++) { // 循环 n-1 次
        int min = INT_MAX, v = -1;
        for (int j = 1; j <= G->vexnum; j++) { // 找到未访问节点中距离最小的节点
            if (!visited[j] && dist[j] < min) {
                min = dist[j];
                v = j;
            }
        }
        if (v == -1) { // 若找不到，则说明剩下的节点都不可达
            break;
        }
        visited[v] = 1;
        for (ArcNode *arc = G->vertices[v].firstarc; arc; arc = arc->nextarc) { // 更新 dist
            int w = arc->adjvex;
            if (!visited[w] && dist[v] + arc->weight < dist[w]) {
                dist[w] = dist[v] + arc->weight;
            }
        }
    }
}
```

AOE 网络的节点表示事件，边表示活动。

- 每个节点有两个属性：最早开始时间 $EC[v]$ 和最晚开始时间 $LC[v]$。
- 每条边有一个活动持续时间，也就是权值 $C$，还有一个松弛时间 $L$。
- 计算：
    - $EC[w] = \max\{EC[v] + C(v, w)\}$
    - $LC[v] = \min\{LC[w] - C(v, w)\}$
    - $L = LC[v] - EC[v] - C(v, w)$
- 若 $L = 0$，则称该活动为**关键活动**。

## 网络流

- 最大流：给定一个有向图 $G$，其中每条边都有一个容量 $c$，求从源节点 $s$ 到汇节点 $t$ 的最大流量
- 求解方法为建立残余网络，设 $f$ 是当前流量，$c$ 是容量，则残余网络中的边的权为：

\[
    c_f(u, v) = \begin{cases} c(u, v) - f(u, v) & \text{if } (u, v) \in E \\ f(v, u) & \text{if } (v, u) \in E \\ 0 & \text{otherwise } \end{cases}
\]

- 从残余网络中找到一条从 $s$ 到 $t$ 的简单路径，称为**增广路径**
- 增广路径的流量为路径上的最小容量，创建新的残余网络，更新流量，直到不存在增广路径

```C

int EdmondsKarp(int s, int t) {
    int maxflow = 0;
    while (BFS(s, t)) {
        int min = INT_MAX;
        for (int v = t; v != s; v = pre[v]) { // 找到增广路径上的最小容量
            min = min < G[pre[v]][v] ? min : G[pre[v]][v];
        }
        maxflow += min;
        for (int v = t; v != s; v = pre[v]) { // 更新残余网络
            G[pre[v]][v] -= min;
            G[v][pre[v]] += min;
        }
    }
    return maxflow;
}
```

## 最小生成树

- 给定一个无向图 $G$，求一个子图 $T$，使得 $T$ 是 $G$ 的生成树，包含 $G$ 的所有节点，且 $T$ 的所有边的权值之和最小。
- Prim 算法：从一个节点开始，每次选择一个与当前生成树距离最小且不会产生环的节点加入生成树。
- Kruskal 算法：每次选择一条权值最小且不会产生环的边加入生成树。

=== "Prim"

    ```C

    void Prim(ALGraph *G, int src) {
        int dist[MaxN] = {0}; // 距离数组
        int visited[MaxN] = {0}; // 访问数组
        for (int i = 1; i <= G->vexnum; i++) { // 初始化
            dist[i] = INT_MAX;
        }
        dist[src] = 0;
        visited[src] = 1;
        for (ArcNode *arc = G->vertices[src].firstarc; arc; arc = arc->nextarc) { // 初始化 dist
            dist[arc->adjvex] = arc->weight;
        }
        for (int i = 1; i < G->vexnum; i++) { // 循环 n-1 次
            int min = INT_MAX, v = -1;
            for (int j = 1; j <= G->vexnum; j++) { // 找到未访问节点中距离最小的节点
                if (!visited[j] && dist[j] < min) {
                    min = dist[j];
                    v = j;
                }
            }
            if (v == -1) { // 若找不到，则说明剩下的节点都不可达
                break;
            }
            visited[v] = 1;
            for (ArcNode *arc = G->vertices[v].firstarc; arc; arc = arc->nextarc) { // 更新 dist
                int w = arc->adjvex;
                if (!visited[w] && arc->weight < dist[w]) {
                    dist[w] = arc->weight;
                }
            }
        }
    }
    ```

=== "Kruskal"

    ```C
    /* 使用并查集维护，先将所有边按权值排序，然后从小到大加入生成树，
    若两个端点不在同一个集合中，则将两个集合合并，将边加入生成树 */

    typedef struct {
        int u, v, w; // 起点、终点、权值
    } Edge;

    int cmp(const void *a, const void *b) {
        return ((Edge *)a)->w - ((Edge *)b)->w;
    }

    void Kruskal(ALGraph *G) {
        Edge edges[MaxN * MaxN];
        int cnt = 0;
        for (int i = 1; i <= G->vexnum; i++) { // 将所有边存入数组
            for (ArcNode *arc = G->vertices[i].firstarc; arc; arc = arc->nextarc) {
                edges[cnt].u = i;
                edges[cnt].v = arc->adjvex;
                edges[cnt].w = arc->weight;
                cnt++;
            }
        }
        qsort(edges, cnt, sizeof(Edge), cmp); // 按权值排序
        int parent[MaxN] = {0}; // 并查集
        for (int i = 1; i <= G->vexnum; i++) {
            parent[i] = i;
        }
        for (int i = 0; i < cnt; i++) {
            int u = edges[i].u, v = edges[i].v;
            if (Find(parent, u) != Find(parent, v)) { // 若不会产生环，则加入生成树
                Union(parent, u, v);
            }
        }
    }
    ```

## BFS & DFS

### BFS

=== "adjacency matrix"

    ```c
    #define MaxN 100
    int G[MaxN][MaxN];
    int pre[MaxN];
    int visited[MaxN];

    void BFS(int src, int dst) {
        int queue[MaxN] = {0};
        int front = 0, rear = 0;
        queue[rear++] = src;
        visited[src] = 1;
        while (front < rear) {
            int v = queue[front++];
            for (int w = 0; w < MaxN; w++) {
                if (G[v][w] && !visited[w]) {
                    queue[rear++] = w;
                    visited[w] = 1;
                    pre[w] = v;
                    if (w == dst) {
                        return;
                    }
                }
            }
        }
    }
    ```

=== "adjacency list"

    ```c
    #define MaxN 100
    int visited[MaxN];
    int pre[MaxN];

    void BFS(ALGraph *G, int src, int dst) {
        int queue[MaxN] = {0};
        int front = 0, rear = 0;
        queue[rear++] = src;
        visited[src] = 1;
        while (front < rear) {
            int v = queue[front++];
            for (ArcNode *arc = G->vertices[v].firstarc; arc; arc = arc->nextarc) { //访问该节点下的所有邻接点
                int w = arc->adjvex;
                if (!visited[w]) {
                    pre[w] = v;
                    queue[rear++] = w;
                    visited[w] = 1;
                    if (w == dst) {
                        return;
                    }
                }
            }
        }
    }
    ```

### DFS

=== "adjacency matrix"

    ```c
    #define MaxN 100
    int G[MaxN][MaxN];
    int pre[MaxN];
    int visited[MaxN];

    void DFS(int v, int dst) {
        visited[v] = 1;
        for (int w = 0; w < MaxN; w++) {
            if (G[v][w] && !visited[w]) {
                pre[w] = v;
                DFS(w, dst);
                if (w == dst) {
                    return;
                }
            }
        }
    }
    ```

=== "adjacency list"

    ```c

    #define MaxN 100
    int visited[MaxN];
    int pre[MaxN];

    void DFS(ALGraph *G, int v, int dst) {
        visited[v] = 1;
        for (ArcNode *arc = G->vertices[v].firstarc; arc; arc = arc->nextarc) {
            int w = arc->adjvex;
            if (!visited[w]) {
                pre[w] = v;
                DFS(G, w, dst);
                if (w == dst) {
                    return;
                }
            }
        }
    }
    ```    

- 双连通性
    - 如果去掉一个节点，图不再连通，则称该节点为**割点**。
    - 如果图 $G$ 是连通图，且没有**割点**，则称 $G$ 是**双连通图**。
    - **双联通分量** 是指图的极大双连通子图。
    - Tarjan 算法：使用 DFS
        - dfn[x] 表示 x 节点被第一次访问的时间戳，从 0 开始计数
        - 追溯值 low[x] 
            - 初始值为 dfn[x]
            - 若 $\langle x, y \rangle$ 是树边，则 low[x] = min(low[x], low[y])
            - 若 $\langle x, y \rangle$ 不是树边，则 low[x] = min(low[x], dfn[y])
    - 求割点：
        - 对于根节点，若其有两个或两个以上的子节点，则根节点为割点。
        - 对于非根节点，若其有一个子节点 $v$，且 $dfn[u] \leqslant low[v]$，则 $u$ 为割点。

```c
void FindCut(ALGraph *G, int v) {
    int child = 0;
    visited[v] = 1;
    dfn[v] = low[v] = ++cnt;
    for (ArcNode *arc = G->vertices[v].firstarc; arc; arc = arc->nextarc) {
        int w = arc->adjvex;
        if (!visited[w]) {
            child++;
            FindCut(G, w);
            low[v] = min(low[v], low[w]);
            if (v != 1 && dfn[v] <= low[w]) {
                printf("%d ", v);
            }
        } else {
            low[v] = min(low[v], dfn[w]);
        }
    }
    if (v == 1 && child >= 2) {
        printf("%d ", v);
    }
}
```

- 求强连通分量：
    - 主体上使用 Tarjan 算法，但是需要对每个节点记录其所属的联通分量。
    - 维护一个栈，每次访问一个节点时，将其入栈，当找到一个联通分量时，将栈中的节点出栈，直到找到该联通分量的根节点。

```c
#define MaxN 100
int dfn[MaxN], low[MaxN]; // 时间戳和追溯值
int instack[MaxN], stack[MaxN]; //栈
int scc[MaxN]; // 所属联通分量
int cnt, cscc = 0; // 时间戳、联通分量计数
int top = 0; // 栈顶

int min(int a, int b) {
    return a < b ? a : b;
}

void Tarjan(ALGraph *G, int v) {
    dfn[v] = low[v] = ++cnt;
    instack[v] = 1;
    stack[top++] = v;
    visited[v] = 1;
    for (ArcNode *arc = G->vertices[v].firstarc; arc; arc = arc->nextarc) {
        int w = arc->adjvex;
        if (!dfn[w]) {
            Tarjan(G, w);
            low[v] = min(low[v], low[w]);
        } else if (instack[w]) {
            low[v] = min(low[v], dfn[w]);
        }
    }
    if (dfn[v] == low[v]) {
        cscc++;
        while (stack[top] != v) {
            scc[stack[top]] = cscc;
            instack[stack[top]] = 0;
            top--;
        }
        scc[stack[top]] = cscc;
        instack[stack[top]] = 0;
        top--;
    }
}

void FindSCC(ALGraph *G) {
    for (int i = 1; i <= G->vexnum; i++) {
        if (!dfn[i]) {
            Tarjan(G, i);
        }
    }
}
```

- 求欧拉回路和欧拉路径：
    - 欧拉回路为包含所有边的简单环，欧拉路径为包含所有边的简单路径。
    - 无向图
        - 无向图 $G$ 存在欧拉回路的充要条件是 $G$ 是连通的且所有节点的度为偶数。
        - 无向图 $G$ 存在欧拉路径的充要条件是 $G$ 是连通的且有且仅有两个节点的度为奇数。
    - 有向图
        - 有向图 $G$ 存在欧拉回路的充要条件是 $G$ 是弱连通的且所有节点的入度等于出度。
        - 有向图 $G$ 存在欧拉路径的充要条件是 $G$ 是若连通的且有且仅有两个节点，其中一个的入度比出度大 1，另一个的入度比出度小 1，其余节点的入度等于出度。
    - Hierholzer 算法：从任意节点开始，每次选择一个未访问的节点，沿着一条未访问的边访问，直到回到起点，将这条路径加入欧拉回路，然后从这条路径上的某个节点开始，重复上述过程，直到所有边都被访问。