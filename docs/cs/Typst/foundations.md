# Foundations

## Arguments

自定义函数也如内嵌函数一样可以接收可变长度的参数，以 `..sink` 形式指明参数接收器接收额外的参数. 接收器的值是 `arguments` 类型，其提供了一系列方法访问位置和命名参数.

而与参数接收相反，也可以通过运算符 `..spread` 进行参数传播，可传播类型包括参数，数组和字典.

参数的构造函数可以用于构造合适的可传播参数，行为类似 `let args(..sink) = sink`.

```
arguments(..any) -> arguments
```

- `at` 方法返回指定索引的位置参数，或指定键的命名参数. 如果键值是整数，则相当于先调用 `pos` 方法再调用 `array.at` 方法. 而如果键值是字符串，则相当于先调用 `named` 方法再调用 `dictionary.at` 方法.

    ```
    self.at(
        int/str,
        default: any,
    ) -> any
    ```

- `pos` 方法以数组形式返回捕捉的位置参数.

    ```
    self.pos() -> array
    ```

- `named` 方法以字典形式返回捕捉的命名参数.

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

- `len` 方法返回数组元素个数.

    ```
    self.len() -> int
    ```

- `first` 方法返回数组的第一个元素.

    ```
    self.first() -> any
    ```

- `last` 方法返回数组的最后一个元素.

    ```
    self.last() -> any
    ```

- `at` 方法返回指定索引的元素. 如果索引超过了数组范围，则返回默认值；若未指定默认值则出错.

    ```
    self.at(
        int,
        default: any,
    ) -> any
    ```

- `push` 方法将元素添加到数组末尾.

    ```
    self.push(any)
    ```

- `pop` 方法移除并返回数组的最后一个元素.

    ```
    self.pop() -> any
    ```

- `insert` 方法在指定索引处插入元素，并且将后续元素向后移动. 替换元素的话使用 `at` 方法.

    ```
    self.insert(
        int,
        any,
    )
    ```

- `remove` 方法移除指定索引的元素，并且返回该元素. 

    ```
    self.remove(
        int,
        default: any,
    ) -> any
    ```

- `slice` 方法提取数组的子数组. `end` 参数与 `count` 参数互斥.

    ```
    self.slice(
        start: int,
        end: none/int,
        count: int,
    ) -> array
    ```

- `contains` 方法检查数组是否包含指定元素，其也有专门的语法，比如可以用 `2 in (1, 2, 3)` 代替 `(1, 2, 3).contains(2)`.

    ```
    self.contains(any) -> bool
    ```

- `find` 方法用来查找符合条件的元素，如果找到则返回第一个匹配的元素，否则返回 `none`.

    ```
    self.find(function) -> any/none
    ```

    !!! example
        `#(1, 2, 3).find(calc.even)` 返回 `2`.

- `position` 方法用来查找符合条件的元素，如果找到则返回第一个匹配的索引，否则返回 `none`.

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

- `filter` 方法用来创建一个新数组，其中只包含符合条件的元素.

    ```
    self.filter(function) -> array
    ```

- `map` 方法用来创建一个新数组，其中的元素是原数组元素经过函数处理后的结果.

    ```
    self.map(function) -> array
    ```

- `enumerate` 方法用来创建一个新数组，其中的元素是原数组元素及其索引的数组，索引从 `start` 开始.

    ```
    self.enumerate(start: int) -> array
    ```

- `zip` 方法用来创建一个新数组，其中的元素是多个数组对应位置的元素的数组. 如果 `exact` 参数为 `true`，则强制所有数组长度相等，否则出错.

    ```
    array.zip(
        exact: bool,
        ..array,
    ) -> array
    ```

- `fold` 方法使用累加器和数组的元素折叠为一个值.

    ```
    self.fold(
        any,
        function,
    ) -> any
    ```

- `sum` 方法返回数组元素的和.

    ```
    self.sum(default: any) -> any
    ```

- `product` 方法返回数组元素的积.

    ```
    self.product(default: any) -> any
    ```

- `any` 方法检查数组是否有元素符合条件.

    ```
    self.any(function) -> bool
    ```

- `all` 方法检查数组是否所有元素都符合条件.

    ```
    self.all(function) -> bool
    ```

- `flatten` 方法将多维数组转换为一维数组.

    ```
    self.flatten() -> array
    ```

- `rev` 方法将数组元素反转.

    ```
    self.rev() -> array
    ```

- `split` 方法将数组在对应值处进行分割，得到多维数组.

    ```
    self.split(any) -> array
    ```

- `join` 方法将数组元素连接为一个元素.

    ```
    self.join(
        any/none,
        last: any,
    ) -> any
    ```

- `intersperse` 方法将某个元素插入到数组元素之间.

    ```
    self.intersperse(any) -> array
    ```

- `chunk` 方法将数组分割为多个大小相等的数组. 除了最后一个数组外，其它数组都有 `chunk-size` 个元素. 如果 `exact` 参数为 `true`，则在最后一个数组长度不足时将其丢弃，否则保留.

    ```
    self.chunk(
        int,
        exact: bool,
    ) -> array
    ```

- `windows` 方法返回数组上所有 `window-size` 大小的滑动窗口构成的数组.

    ```
    self.windows(int) -> array
    ```

- `sorted` 方法返回依据键函数排序的数组.

    ```
    self.sorted(key: function) -> array
    ```

- `dedup` 方法返回去重后的数组.

    ```
    self.dedup() -> array
    ```

- `to-dict` 方法将数组转换为字典，如果一个键值出现了多次，则取最后一个值.

    ```
    self.to-dict() -> dictionary
    ```

- `reduce` 方法将元素规约为一个值. 如果数组是空的，返回 `none`. 当数组至少有一个元素时，其与 `array.fold` 方法的行为类似，不过将第一个值作为累加器的初始值.

    ```
    self.reduce(function) -> any
    ```

## Assert

用于确保条件满足，如果未满足便会产生错误，文档中不产生任何输出.

可以使用 `assert.eq` 和 `assert.ne` 来测试两个值是否相等.

```
assert(
    bool,
    message: str
)
```

- `eq` 方法用于确保两个值相等.

    ```
    assert.eq(
        any,
        any,
        message: str
    )
    ```

- `ne` 方法用于确保两个值不等.

    ```
    assert.ne(
        any,
        any,
        message: str
    )
    ```

## Auto

支持 `auto` 值的参数会有智能的默认值或是上下文行为.

## Boolean

## Bytes

概念上其类似于一个元素都在 $0$ 和 $255$ 之间的整数数组，但表示更高效，可以使用 `for` 循环遍历.

可以作如下转换：

- 使用 `bytes` 的构造函数将一个字符串或整数数组转换为字节序列

- 借助 UTF-8 编码，使用 `str` 的构造函数将字节序列转换为字符串

- 使用 `array` 的构造函数将字节序列转换为整数数组

从文件读取数据时，可以自行决定是以字符串形式还是以字节序列加载.

构造函数用于将值转换为字节序列.

- 字符串会以 UTF-8 编码进行转换；

- $0$ 到 $255$ 之间的整数数组会被直接转换，专用的字节表示形式比数组表示形式高效的多，因此常被用于处理大型字节缓冲区.

```
bytes(str/bytes/array) -> bytes
```

- `len` 方法返回字节序列长度.

    ```
    self.len() -> int
    ```

- `at` 方法返回指定索引的元素. 如果索引超过了字节序列长度，则返回默认值；若未指定默认值则出错.

    ```
    self.at(
        int,
        default: any
    ) -> any
    ```

- `slice` 方法提取字节序列的切片. `end` 参数和 `count` 参数互斥.

    ```
    self.slice(
        start: int,
        end: none/int,
        count: int
    ) -> bytes
    ```

## Calculation

`calc` 是数值处理与运算模块，以下的定义都是 `calc` 模块的一部分，并不会默认导入. 此外 `calc` 模块还定义了一些数学常量.

- `abs` 方法返回数值的绝对值.

    ```
    calc.abs(int/float/length/angle/ratio/fraction/decimal) -> any
    ```

- `pow` 方法进行指数幂运算.

    ```
    calc.pow(
        int/float/decimal,
        int/float
    ) -> int/float/decimal
    ```

- `exp` 方法计算 $\mathrm{e}$ 的幂次.

    ```
    calc.exp(int/float) -> float
    ```

- `sqrt` 方法计算数值的平方根.

    ```
    calc.sqrt(int/float) -> float
    ```

- `root` 方法计算数值的 $n$ 次根. 如果数值为负，那么次数 $n$ 需要为奇数.

    ```
    calc.root(
        float,
        int
    ) -> float
    ```

- `sin` 方法计算角度的正弦值. 以下三角函数的参数若为整数或浮点类型，则作为弧度处理.

    ```
    calc.sin(int/float/angle) -> float
    ```

- `cos` 方法计算角度的余弦值.

    ```
    calc.cos(int/float/angle) -> float
    ```

- `tan` 方法计算角度的正切值.

    ```
    calc.tan(int/float/angle) -> float
    ```

- `asin` 方法计算数值的反正弦.

    ```
    calc.asin(int/float) -> angle
    ```

- `acos` 方法计算数值的反余弦.

    ```
    calc.acos(int/float) -> angle
    ```

- `atan` 方法计算数值的反正切.

    ```
    calc.atan(int/float) -> angle
    ```

- `atan2` 方法计算一个坐标的四象限反正切值，参数为 $(x, y)$.

    ```
    calc.atan2(
        int/float,
        int/float
    ) -> angle
    ```

- `sinh` 方法计算双曲角的双曲正弦值.

    ```
    calc.sinh(float) -> float
    ```

- `cosh` 方法计算双曲角的双曲余弦值.

    ```
    calc.cosh(float) -> float
    ```

- `tanh` 方法计算双曲角的双曲正切值.

    ```
    calc.tanh(float) -> float
    ```

- `log` 方法计算数值的对数. 如果没指定基底，则默认为 $10$.

    ```
    calc.log(
        int/float,
        base: float
    ) -> float
    ```

- `ln` 方法计算数值的自然对数.

    ```
    calc.ln(int/float) -> float
    ```

- `fact` 方法计算数值的阶乘.

    ```
    calc.fact(int) -> int
    ```

- `perm` 方法计算排列个数. 返回 $n$ 的 $k$ 排列个数.

    ```
    calc.perm(
        int,
        int
    ) -> int
    ```

- `binom` 方法计算二项式系数. 返回 $n$ 的 $k$ 组合个数.

    ```
    calc.binom(
        int,
        int
    ) -> int
    ```

- `gcd` 方法计算两个整数的最大公因数.

    ```
    calc.gcd(
        int,
        int
    ) -> int
    ```

- `lcm` 方法计算两个整数的最小公倍数.

    ```
    calc.lcm(
        int,
        int
    ) -> int
    ```

- `floor` 方法将数值向下取整为最近的整数，是整数则保持不变.

    ```
    calc.floor(int/float/decimal) -> int
    ```

- `ceil` 方法将数值向上取整为最近的整数，是整数则保持不变.

    ```
    calc.ceil(int/float/decimal) -> int
    ```

- `trunc` 方法返回数值的整数部分，是整数则保持不变.

    ```
    calc.trunc(int/float/decimal) -> int
    ```

- `fract` 方法返回数值的小数部分，是整数则返回 $0$.

    ```
    calc.fract(int/float/decimal) -> int/float/decimal
    ```

- `round` 方法将数值向远离 $0$ 的方向舍入到最接近的整数，可以指定保留位数. 如果保留位数为负，其绝对值将表示在小数点前要去除的整数位数. 该方法的返回值类型和参数类型一致.

    ```
    calc.round(
        int/float/decimal,
        digits: int,
    ) -> int/float/decimal
    ```

    !!! example
        
        ```
        #assert(calc.round(3) == 3)
        #assert(calc.round(3.14) == 3)
        #assert(calc.round(3.5) == 4.0)
        #assert(calc.round(3333.45, digits: -2) == 3300.0)
        #assert(calc.round(-48953.45, digits: -3) == -49000.0)
        ```

## Function

函数是从参数值到一个返回值的映射. 可以通过在函数名称后写入函数参数列表来调用函数，也可以在常规函数参数列表后向函数传递任意数量的后缀参数块. 此外还支持位置参数和命名参数.

某些函数与元素相关联，调用这些函数的时候便会创建对应的元素，被称为元素函数. 与普通函数不同，它们可以在 `set`, `show` 以及选择器中使用.

类似于模块，函数可以在自己的作用域中保留定义，但这目前只适用于内置函数.

可以使用 `let binding` 定义函数，在绑定名称后添加参数列表，参数列表可以包含必需的位置参数，带有默认值的命名参数，以及参数接收器.

函数绑定表达式的右侧是函数体. 函数体可以是块或任何其他的表达式，其定义了函数的返回值并且可以依赖于参数. 如果函数体是代码块，那么返回值是块内所有表达式结果的连接.

在函数体内使用 `return` 可以提前退出且可以选择指定返回值，如果没有指定返回值，那么函数会将 `return` 前的表达式结果连接作为返回值.

不返回任何有意义的值的函数会返回 `none` 作为代替，但这种函数的返回值类型是不指定的.

使用 `import` 可以从其他模块导入函数. 

也可以通过在参数列表后接 `=>` 和函数体来创建匿名函数，这种方式不需要绑定. 匿名函数主要应用于 `show`，但也适用于接受函数作为值的可设置属性.

Typst 中的所有函数都是纯函数，对于相同的参数总是返回相同的结果，函数无法记忆信息以在第二次调用时产生不同的值. 例外是像 `array.push(value)` 这样的内置方法，这些方法可以修改他们所调用的值.

- `with` 方法返回一个预先应用给定参数的新函数，可以认为是派生出的.

    ```
    self.with(..any) -> function
    ```

- `where` 方法返回一个选择器，其筛选属于此函数且字段值与给定参数值匹配的元素.

    ```
    self.where(..any) -> selector
    ```