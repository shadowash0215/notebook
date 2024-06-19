# 栈和队列

## 栈

栈是一种后进先出的数据结构，只能在一端进行插入和删除操作，这一端称为栈顶，另一端称为栈底。

数据结构定义如下：

```C
typedef struct {
    int *data;
    int top;
    int size;
} Stack;
```

栈的基本操作：

=== "Create"

    ```C
    Stack Create(int size) {
        Stack S = (Stack)malloc(sizeof(Stack));
        S->data = (int *)malloc(sizeof(int) * size);
        S->top = -1;
        S->size = size;
        return S;
    }
    ```
=== "Push"

    ```C
    void Push(int x, Stack S) {
        if (S->top == S->size - 1) {
            printf("Stack is full.\n");
            return;
        }
        S->data[++S->top] = x;
    }
    ```
=== "Pop"

    ```C
    int Pop(Stack S) {
        if (S->top == -1) {
            printf("Stack is empty.\n");
            return -1;
        }
        return S->data[S->top--];
    }
    ```
    
## 队列

队列是一种先进先出的数据结构，只能在一端进行插入操作，在另一端进行删除操作，这一端称为队头，另一端称为队尾。

数据结构定义如下：

```C
typedef struct {
    int *data;
    int front;
    int rear;
    int size;
} Queue;
```

队列的基本操作：

=== "Create"

    ```C
    Queue Create(int size) {
        Queue Q = (Queue)malloc(sizeof(Queue));
        Q->data = (int *)malloc(sizeof(int) * size);
        Q->front = Q->rear = 0;
        Q->size = size;
        return Q;
    }
    ```

=== "Enqueue"

    ```C
    void Enqueue(int x, Queue Q) {
        if ((Q->rear + 1) % Q->size == Q->front) {
            printf("Queue is full.\n");
            return;
        }
        Q->data[Q->rear] = x;
        Q->rear = (Q->rear + 1) % Q->size;
    }
    ```

=== "Dequeue"

    ```C
    int Dequeue(Queue Q) {
        if (Q->front == Q->rear) {
            printf("Queue is empty.\n");
            return -1;
        }
        int x = Q->data[Q->front];
        Q->front = (Q->front + 1) % Q->size;
        return x;
    }
    ```

=== "IsEmpty"

    ```C
    int IsEmpty(Queue Q) {
        return Q->front == Q->rear;
    }
    ```