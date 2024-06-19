# 堆

## 二叉堆

二叉堆是完全二叉树(complete binary tree)，其节点编号按层序遍历是严格单调递增的。若高度为 $h$ 的二叉树有 $n$ 个节点，则 $2^h \leqslant n \leqslant 2^{h+1}-1$，即 $h = \lfloor \log_2 n \rfloor$。

二叉堆的存储一般用数组线性存储，`heap[0]` 不存储数据，`heap[1]` 是根节点，`heap[i]` 的左孩子是 `heap[2*i]`，右孩子是 `heap[2*i+1]`，父节点是 `heap[i/2]`。

数据结构定义如下：

```c
typedef struct HeapStruct {
    int *data;
    int size;
    int capacity;
} *Heap;
```

根据存储方式，二叉堆分为最大堆(max heap)和最小堆(min heap)。最大堆中，父节点的值大于等于两个子节点的值；最小堆中，父节点的值小于等于两个子节点的值。

下面是堆的一些基本操作(以最小堆为例)：

=== "Insert"

    ```c
    void Insert(int x, Heap H) {
        int i;
        if (H->size == H->capacity) {
            printf("Heap is full.\n");
            return;
        }
        for (i = ++H->size; H->data[i/2] > x; i /= 2) {
            H->data[i] = H->data[i/2];
        }
        H->data[i] = x;
    }
    ```
    
=== "PercolateUp"

    ```c
    void PercolateUp(int i, Heap H) {
        int temp = H->data[i];
        int index = 0;
        for (index = i; H->data[index/2] > temp && index > 1; index /= 2) {
            H->data[index] = H->data[index/2];
        }
        H->data[index] = temp;
    }
    ```

=== "PercolateDown"

    ```c
    void PercolateDown(int i, Heap H) {
        int temp = H->data[i];
        int parent, child = 0;
        for (parent = i; parent * 2 <= H->size; parent = child) {
            child = parent * 2;
            if (child != H->size && H->data[child + 1] < H->data[child]) {
                child++;
            }
            if (temp > H->data[child]) {
                H->data[parent] = H->data[child];
            } else {
                break;
            }
        }
        H->data[parent] = temp;
    }
    ```


=== "DeleteMin"

    ```c
    int DeleteMin(Heap H) {
        if (H->size == 0) {
            printf("Heap is empty.\n");
            return -1;
        }
        int min = H->data[1];
        H->data[1] = H->data[H->size--];
        PercolateDown(1, H);
        return min;
    }
    ```

=== "BuildHeap"

    ```c
    void BuildHeap(Heap H) {
        for (int i = H->size/2; i > 0; i--) {
            PercolateDown(i, H);
        }
    }
    ```