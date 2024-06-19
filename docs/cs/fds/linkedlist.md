# 链表

## 单向链表

数据结构如下定义：

```c
typedef struct node* List;
typedef struct node {
    int data;
    struct node *next;
} Node;
```

有如下操作：

=== "CreateList"

    ```c
    List CreateList(int n) {
        List L = (List)malloc(sizeof(Node));
        L->next = NULL;
        List p = L;
        for (int i = 0; i < n; i++) {
            List temp = (List)malloc(sizeof(Node));
            scanf("%d", &temp->data);
            temp->next = NULL;
            p->next = temp;
            p = temp;
        }
        return L;
    }
    ```

=== "Insert"

    ```c
    void Insert(int x, int i, List L) {
        List p = L;
        for (int j = 0; j < i - 1; j++) { /* 找到第 i 个节点的前一个节点 */
            p = p->next;
        }
        List temp = (List)malloc(sizeof(Node));
        temp->data = x;
        temp->next = p->next;
        p->next = temp;
    }
    ```

=== "Delete"

    ```c
    void Delete(int i, List L) {
        List p = L;
        for (int j = 0; j < i - 1; j++) { /* 找到第 i 个节点的前一个节点 */
            p = p->next;
        }
        List temp = p->next;
        p->next = temp->next;
        free(temp);
    }
    ```

=== "Reverse"

    ```c
    void Reverse(List L) {
        List p = NULL;
        for (List q = L->next; q != NULL; ) {
            List temp = q->next;
            q->next = p;
            p = q;
            q = temp;
        }
        L->next = p;
    }
    ```

## 双向循环链表

数据结构如下定义：

```c
typedef struct node* List;
typedef struct node {
    int data;
    struct node *prev;
    struct node *next;
} Node;
```

有如下操作：

=== "CreateList"

    ```c
    List CreateList(int n) {
        List L = (List)malloc(sizeof(Node));
        L->prev = L;
        L->next = L;
        List p = L;
        for (int i = 0; i < n; i++) {
            List temp = (List)malloc(sizeof(Node));
            scanf("%d", &temp->data);
            temp->prev = p; /* temp 的前驱是 p */
            temp->next = p->next; /* temp 的后继是 p 的后继 */
            p->next->prev = temp; /* p 的后继的前驱是 temp */
            p->next = temp; /* p 的后继是 temp */
            p = temp;
        }
        return L;
    }
    ```

=== "Insert"

    ```c
    void Insert(int x, int i, List L) {
        List p = L;
        for (int j = 0; j < i - 1; j++) { /* 找到第 i 个节点的前一个节点 */
            p = p->next;
        }
        List temp = (List)malloc(sizeof(Node));
        temp->data = x;
        temp->prev = p;
        temp->next = p->next;
        p->next->prev = temp;
        p->next = temp;
    }
    ```

=== "Delete"

    ```c
    void Delete(int i, List L) {
        List p = L;
        for (int j = 0; j < i - 1; j++) { /* 找到第 i 个节点的前一个节点 */
            p = p->next;
        }
        List temp = p->next;
        p->next = temp->next;
        temp->next->prev = p;
        free(temp);
    }
    ```