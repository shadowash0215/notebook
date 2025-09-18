# Foundations

## Arguments

自定义函数也如内嵌函数一样可以接收可变长度的参数，以 `..sink` 形式指明参数接收器接收额外的参数. 接收器的值是 `arguments` 类型，其提供了一系列方法访问位置和命名参数.

而与参数接收相反，也可以通过运算符 `..spread` 进行参数传播，可传播类型包括参数，数组和字典.

参数的构造函数可以用于构造合适的可传播参数，行为类似 `let args(..sink) = sink`.

```
arguments(..any) -> arguments
```

- `at` 函数返回指定索引的位置参数，或指定键的命名参数. 如果键值是整数，则相当于先调用 `pos` 函数再调用 `array.at` 函数. 而如果键值是字符串，则相当于先调用 `named` 函数再调用 `dictionary.at` 函数.

    ```
    self.at(
        int/str,
        default: any,
    ) -> any
    ```

- `pos` 函数以数组形式返回捕捉的位置参数.

    ```
    self.pos() -> array
    ```

- `named` 函数以字典形式返回捕捉的命名参数.

    ```
    self.named() -> dictionary
    ```

!!! example
    对于
    ```
    #let args = arguments(stroke: red, inset: 1em, [Body])
    ```
    而言，`args.pos()` 返回 `([Body],)`，`args.named()` 返回 `(stroke: rgb("#ff4136"), inset: 1em)`.

## Array

数组是一种有序的集合，其元素可以是任意类型. 索引从零开始，负索引从数组末尾回绕. 

长度为 1 的数组需要一个尾逗号，以消除与括号运算符的歧义.

数组的构造函数可以将值转换为数组，不过该函数意图在于将集合类的值转换为数组，对于独立的值，可以直接使用数组的语法.

```
array(bytes/array/version) -> array
```

- `len` 函数返回数组元素个数.

    ```
    self.len() -> int
    ```

- `first` 函数返回数组的第一个元素.

    ```
    self.first() -> any
    ```

- `last` 函数返回数组的最后一个元素.

    ```
    self.last() -> any
    ```

- `at` 函数返回指定索引的元素. 如果索引超过了数组范围，则返回默认值.

    ```
    self.at(
        int,
        default: any,
    ) -> any
    ```

- `push` 函数将元素添加到数组末尾.

    ```
    self.push(any)
    ```

- `pop` 函数移除并返回数组的最后一个元素.

    ```
    self.pop() -> any
    ```

- `insert` 函数在指定索引处插入元素，并且将后续元素向后移动. 替换元素的话使用 `at` 函数.

    ```
    self.insert(
        int,
        any,
    )
    ```

- `remove` 函数移除指定索引的元素，并且返回该元素. 

    ```
    self.remove(
        int,
        default: any,
    ) -> any
    ```

- `slice` 函数提取数组的子数组. `end` 参数与 `count` 参数互斥.

    ```
    self.slice(
        int,
        none/int,
        count: int,
    ) -> array
    ```

- `contains` 函数检查数组是否包含指定元素，其也有专门的语法，比如可以用 `2 in (1, 2, 3)` 代替 `(1, 2, 3).contains(2)`.

    ```
    self.contains(any) -> bool
    ```

- `find` 函数用来查找符合条件的元素，如果找到则返回第一个匹配的元素，否则返回 `none`.

    ```
    self.find(function) -> any/none
    ```

    !!! example
        `#(1, 2, 3).find(calc.even)` 返回 `2`.

- `position` 函数用来查找符合条件的元素，如果找到则返回第一个匹配的索引，否则返回 `none`.

    ```
    self.position(function) -> int/none
    ```

- `range` 创建一个整数数组，其范围从 `start` 到 `end`，步长为 `step`. 只传入一个参数的话，其作为 `end` 参数，`start` 参数默认为 0，`step` 参数默认为 1. 传入两个参数的话，第一个参数作为 `start` 参数，第二个参数作为 `end` 参数，`step` 参数默认为 1.

    ```
    array.range(
        int,
        int,
        step: int,
    ) -> array
    ```

- `filter` 函数用来创建一个新数组，其中只包含符合条件的元素.

    ```
    self.filter(function) -> array
    ```

- `map` 函数用来创建一个新数组，其中的元素是原数组元素经过函数处理后的结果.

    ```
    self.map(function) -> array
    ```

- `enumerate` 函数用来创建一个新数组，其中的元素是原数组元素及其索引的数组，索引从 `start` 开始.

    ```
    self.enumerate(start: int) -> array
    ```

- `zip` 函数用来创建一个新数组，其中的元素是多个数组对应位置的元素的数组. 如果 `exact` 参数为 `true`，则强制所有数组长度相等，否则出错.

    ```
    array.zip(
        exact: bool,
        ..array,
    ) -> array
    ```

- `fold` 函数使用累加器和数组的元素折叠为一个值.

    ```
    self.fold(
        any,
        function,
    ) -> any
    ```

- `sum` 函数返回数组元素的和.

    ```
    self.sum(default: any) -> any
    ```

- `product` 函数返回数组元素的积.

    ```
    self.product(default: any) -> any
    ```

- `any` 函数检查数组是否有元素符合条件.

    ```
    self.any(function) -> bool
    ```

- `all` 函数检查数组是否所有元素都符合条件.

    ```
    self.all(function) -> bool
    ```

- `flatten` 函数将多维数组转换为一维数组.

    ```
    self.flatten() -> array
    ```

- `rev` 函数将数组元素反转.

    ```
    self.rev() -> array
    ```

- `split` 函数将数组在对应值处进行分割，得到多维数组.

    ```
    self.split(any) -> array
    ```

- `join` 函数将数组元素连接为一个元素.

    ```
    self.join(
        any/none,
        last: any,
    ) -> any
    ```

- `intersperse` 函数将某个元素插入到数组元素之间.

    ```
    self.intersperse(any) -> array
    ```

- `chunk` 函数将数组分割为多个大小相等的数组. 除了最后一个数组外，其它数组都有 `chunk-size` 个元素. 如果 `exact` 参数为 `true`，则在最后一个数组长度不足时将其丢弃，否则保留.

    ```
    self.chunk(
        int,
        exact: bool,
    ) -> array
    ```

- `windows` 函数返回数组上所有 `window-size` 大小的滑动窗口构成的数组.

    ```
    self.windows(int) -> array
    ```

- `sorted` 函数返回依据键函数排序的数组.

    ```
    self.sorted(key: function) -> array
    ```

- `dedup` 函数返回去重后的数组.

    ```
    self.dedup() -> array
    ```

- `to-dict` 函数将数组转换为字典，如果一个键值出现了多次，则取最后一个值.

    ```
    self.to-dict() -> dictionary
    ```

- `reduce` 函数将元素规约为一个值. 如果数组是空的，返回 `none`. 当数组至少有一个元素时，其与 `array.fold` 函数的行为类似，不过将第一个值作为累加器的初始值.

    ```
    self.reduce(function) -> any
    ```