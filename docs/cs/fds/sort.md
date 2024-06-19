# 排序

## 插入排序

```C
void insertSort(int *arr, int len) {
    int i, j, temp;
    for (i = 1; i < len; i++) {
        temp = arr[i];
        for (j = i; j > 0 && arr[j - 1] > temp; j--) {
            arr[j] = arr[j - 1];
        }
        arr[j] = temp;
    }
}
```

- 进行 $N - 1$ 次排序。
- 第 $i$ 次排序时，$0$ 到 $i - 1$ 位的元素已经有序，然后将第 $i$ 位的元素插入。
- 最坏情况为逆序，时间复杂度为 $O(N^2)$，最好情况为顺序，时间复杂度为 $O(N)$。

## 希尔排序

希尔排序是利用一个增量序列 $h_1 < h_2 < \cdots < h_t$ 进行分组排序，其中 $h_i$ 为整数，且 $h_1$ 为 1。

- 定义 $h_k$-sort 为将原数组隔 $h_k - 1$ 个元素分组，每组内部进行插入排序
- $k = t, t - 1, \cdots, 1$ 时，进行 $h_k$-sort，最终得到有序数组
    - $h_k$-sorted 的序列在 $h_{k - 1}$-sorted 后仍然是 $h_k$-sorted 的
- 希尔排序的时间复杂度与增量序列的选取有关
    - Shell's increments: $h_t = \lfloor N / 2 \rfloor, h_{k - 1} = \lfloor h_k / 2 \rfloor$
        - 最坏情况为 $O(N^2)$（只在 $1$-sort 时进行了排序）
    - Hibbard's increments: $h_k = 2^k - 1$
        - 最坏情况为 $O(N^{3/2})$
        - 平均情况为 $O(N^{5/4})$

使用 Shell's increments 的希尔排序：

```C
void shellSort(int *arr, int len) {
    int i, j, temp, h;
    for (h = len / 2; h > 0; h /= 2) {
        for (i = h; i < len; i++) {
            temp = arr[i];
            for (j = i; j >= h && arr[j - h] > temp; j -= h) {
                arr[j] = arr[j - h];
            }
            arr[j] = temp;
        }
    }
}
``` 

## 堆排序

堆排序是利用堆的性质进行排序的。

- 算法一：将数组构造成堆，然后依次取出堆顶元素
    - 时间复杂度为 $O(N \log N)$
    - 但空间消耗翻倍了
- 算法二：
    - 线性时间构造最大堆（从最后一个非叶子节点开始，依次进行下滤操作）
    - 将堆顶元素与最后一个元素交换（相当于删除最大元素），然后进行下滤操作
    - $N - 1$ 次删除后，得到有序数组
    - 平均比较次数为 $2N \log N - O(N \log \log N)$

```C
void PercDown(int *arr, int i, int len) {
    int temp = arr[i];
    int parent, child = 0;
    for(parent = i; parent * 2 + 1 < len; parent = child) {
        child = parent * 2 + 1;
        if (child != len - 1 && arr[child] < arr[child + 1]) {
            child++;
        }
        if (temp < arr[child]) {
            arr[parent] = arr[child];
        } else {
            break;
        }
    }
    arr[parent] = temp;
}

void HeapSort(int *arr, int len) {
    int i, temp;
    for (i = len / 2; i >= 0; i--) {
        PercDown(arr, i, len);
    }
    for (i = len - 1; i > 0; i--) {
        temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        PercDown(arr, 0, i);
    }
}
```

## 归并排序

归并排序是利用分治的思想进行排序的，关键在于将两个有序数组合并成一个有序数组的操作。
    - 复杂度为 $O(N \log N)$
    - 空间复杂度为 $O(N)$
```C
void mergeSort(int *arr, int N) {
    int *tmp = malloc(sizeof(int) * N);
    if (tmp != NULL) {
        mergeSortHelper(arr, tmp, 0, N - 1);
        free(tmp);
    } else {
        printf("No space for tmp array!\N");
    }
}

void mergeSortHelper(int *arr, int *tmp, int left, int right) {
    if (left < right) {
        int center = (left + right) / 2;
        mergeSortHelper(arr, tmp, left, center);
        mergeSortHelper(arr, tmp, center + 1, right);
        merge(arr, tmp, left, center + 1, right);
    }
}

void merge(int *arr, int *tmp, int leftPos, int rightPos, int rightEnd) {
    int leftEnd = rightPos - 1;
    int tmpPos = leftPos
    int numElements = rightEnd - leftPos + 1;
    while (leftPos <= leftEnd && rightPos <= rightEnd)
        if (arr[leftPos] <= arr[rightPos])
            tmp[tmpPos++] = arr[leftPos++];
        else
            tmp[tmpPos++] = arr[rightPos++];
    while (leftPos <= leftEnd)
        tmp[tmpPos++] = arr[leftPos++];
    while (rightPos <= rightEnd)
        tmp[tmpPos++] = arr[rightPos++];
    for (int i = 0; i < numElements; ++i, rightEnd--)
        arr[rightEnd] = tmp[rightEnd];
}
```

## 快速排序

- 已知的实际运行最快的排序算法
- 选择一个基准元素（枢轴 pivot），将数组分成两个子数组，左边的元素都小于等于基准元素，右边的元素都大于等于基准元素，然后对两个子数组进行快排、合并
- 选取 pivot
    - 错误方法：选取第一个元素
        - 最坏情况为逆序，时间复杂度为 $O(N^2)$
    - 随机选取 pivot
        - 期望时间复杂度为 $O(N \log N)$
        - 但随机数生成也有时间消耗
    - 三数中值分割法：选取左端、中间、右端三个元素，将中间元素作为 pivot
- 当子数组长度小于某个值时，使用插入排序
- 时间复杂度
    - 最坏情况为逆序，时间复杂度为 $O(N^2)$
    - 平均情况为 $O(N \log N)$
    - 最优情况为 $O(N \log N)$

```C
void quickSort(int *arr, int len) {
    quickSortHelper(arr, 0, len - 1);
}

void quickSortHelper(int *arr, int left, int right) {
    if (left + cutoff < right) {
        int pivot = median3(arr, left, right);
        int i = left, j = right - 1;
        while (1) {
            while (arr[++i] < pivot) {}
            while (arr[--j] > pivot) {}
            if (i < j) {
                swap(&arr[i], &arr[j]);
            } else {
                break;
            }
        }
        swap(&arr[i], &arr[right - 1]);
        quickSortHelper(arr, left, i - 1);
        quickSortHelper(arr, i + 1, right);
    } else {
        insertSort(arr + left, right - left + 1);
    }
}

int median3(int *arr, int left, int right) {
    int center = (left + right) / 2;
    if (arr[left] > arr[center]) {
        swap(&arr[left], &arr[center]);
    }
    if (arr[left] > arr[right]) {
        swap(&arr[left], &arr[right]);
    }
    if (arr[center] > arr[right]) {
        swap(&arr[center], &arr[right]);
    }
    swap(&arr[center], &arr[right - 1]);
    return arr[right - 1];
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

## 桶排序

- 如果输入数据都小于 $M$，则可以用一个大小为 $M$ 的数组来记录某个值出现了多少次，这个数组称为桶（bucket）
- 桶排序的时间复杂度为 $O(N)$，但是需要额外的空间

```C
void bucketSort(int *arr, int len) {
    int *bucket = malloc(sizeof(int) * len);
    if (bucket != NULL) {
        for (int i = 0; i < len; i++) {
            bucket[i] = 0;
        }
        for (int i = 0; i < len; i++) {
            bucket[arr[i]]++;
        }
        for (int i = 0, j = 0; i < len; i++) {
            while (bucket[i] > 0) {
                arr[j++] = i;
                bucket[i]--;
            }
        }
        free(bucket);
    } else {
        printf("No space for bucket!\n");
    }
}
```

## 基数排序

- 从低位（LSD，Least Significant Digit）到高位（MSB），对每一位进行进行排序
- 每一位的排序可以使用桶排序
- 时间复杂度为 $O(P(N + B))$，其中 $P$ 为位数，$B$ 为桶的个数

## 杂项

- 只依靠比较实现的排序，必然存在时间复杂度为 $\Omega(N \log N)$ 的最坏情况
- 稳定性：如果两个元素的大小相等，排序后两个元素的相对位置是否发生变化
    - 归并排序、插入排序、冒泡排序、桶排序、基数排序是稳定的
    - 堆排序、快速排序、希尔排序、选择排序是不稳定的  