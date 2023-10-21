<style>
.center {
  width: auto;
  display: table;
  margin-left: auto;
  margin-right: auto;
}
</style>

# 组合逻辑电路

## 门电路

逻辑运算符：AND($A \cdot B$, $AB$), OR($A+B$), NOR($\overline{A}$, $A$', ~$A$).

门延迟(Gate Delay): 在实际的物理门电路中，如果多个输入的变化引起输出的变化，那么输出并不会立即发生改变. 输入变化与导致输出变化之间的时间差被称为门延迟，记作 $t_G$. 

逻辑表达方式：真值表(truth table)，逻辑函数(equation)，逻辑电路图(logic diagram)

## 布尔代数

!!! note "运算律"

    <div class="center">

    | Equation | Equation | name |
    |:-----------:|:----------:|:----------:|
    |$X + 0 = X$|$X \cdot 1 = X$|
    |$X + 1 = 1$|$X \cdot 0 = 0$|
    |$X + X = X$|$X \cdot X = X$|
    |$X + \overline{X} = 1$|$X \cdot \overline{X} = 0$|
    |$\overline{\overline{X}} = X$||
    |$X + Y = Y + X$|$XY = YX$|commutative|
    |$(X + Y) + Z = X + (Y + Z)$|$(XY)Z = X(YZ)$|associative|
    |$X(Y + Z) = XY + XZ$|$X + YZ = (X + Y)(X + Z)$|distributive|
    |$\overline{X + Y} = \overline{X} \cdot \overline{Y}$|$\overline{X \cdot Y} = \overline{X} + \overline{Y}$|DeMorgan's|
    |$X \cdot Y + \overline{X} \cdot Y = Y$|$(X + Y) \cdot (\overline{X} \cdot Y) = Y$|minimization|
    |$X + X \cdot Y = X$|$X \cdot (X + Y) = X$|absorption|
    |$X + \overline{X} \cdot Y = X + Y$|$X \cdot (\overline{X} + Y) = X \cdot Y$|simplification|
    |$X \cdot Y + \overline{X} \cdot Z + Y \cdot Z = X \cdot Y + \overline{X} \cdot Z$|$(X + Y) \cdot (\overline{X} + Z) \cdot (Y + Z) = (X + Y) \cdot (\overline{X} + Z)$|consensus|

    </div>

标准型(canonical form): 最小项的和(SOM)，最大项的积(POM).  
最大项(maxterm)和最小项(minterm): 由表达式中所有变量（或其否定）组成，最小项用“与”连接，最大项用“或”连接，对应指标(index)为使最小项输出逻辑 1，最大项输出逻辑 0 的二进制变量赋值方法. 同一指标下的最小项和最大项互反. 

标准乘积之和与标准和之乘积