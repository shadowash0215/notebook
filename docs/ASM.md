# 汇编语言

## *3.9*

一般来说，三个 push+ 一个 call 表示程序在调用 main 函数，其之前的代码为 C 语言的初始化代码.  
OD 中 F2 为设置断点， F7 为跟踪进入.  
数据窗中 Ctrl+G 可以跟踪变量.  

有某些商用的对 exe 进行压缩的软件，如 Pecompact，VmProtect 可以把 exe 压缩为 exe ，压缩以后的 exe 也能双击运行.  
软件作者调用以下函数 sn  
sn = rsa(mac，私钥)  
软件检测 sn 是否正确  
rsa = (sn，公钥) == mac  
nop 指令指什么也不做，no operation，机器码为 0x90.  
alt+backspace 可将改坏的指令恢复原样.  
搜索时使用较长的串以获取想要的结果.  
用十六进制编辑工具如 010editor 或 QuickView 都可以对 password.exe 进行搜索并修改.  
010editor 中按 Ctrl+F 输入要查找的串(Type 要注意修改为 hex bytes).  
QV 打开 password.exe，按回车键可以在 ascii/hex/asm 三种模式中切换，asm 模式有两种: 16位/32位，按 F2 切换(查看最下方状态栏或寄存器字母数).  
F7 进行搜索，tab 键在 ascii/hex 间切换，左上角编辑内有粘贴.  
F3 可将改坏的内容变为原样，tab 键可从左侧机器语言切换到右侧汇编指令，输入汇编语言进行修改，alt+F9 保存修改，F1 可获取帮助.  
md5 加密算法(但已经被证明无法防止碰撞).

~~~
.data #编译指示语句，表示变量、数组定义从此处开始.汇编语言中单引号及双引号无区别，他们既可以引住单个字符，又可以引住多个字符;
#字符串末尾并没有隐含的'\0';定义数组和定义变量无区别.
result db 100 dup(0) #dup:duplicate
# == char result={0}
format db "%d"，0
prompt db "The result"，0

.code #编译指示语句，帮助编译器识别代码从此处开始   
main:       #标号
    mov eax，0
    mov ebx，1
next:
    add eax，ebx #eax = eax + ebx
    add ebx，1 
    cmp ebx，100 #cmp:compare
    jbe next #jbe:jump if below or equal
invoke wsprintf，offset result，offset format，eax #wsprintf 和 MessageboxA 是 Windows 操作系统下的函数 offset 为取地址.
# == wsprintf(&result[0]，&format[0]，eax); 将 eax 中的内容以 char 类型 format 数组的格式输出到 char 类型 result 数组中.
# == wsprintf(result，format，eax) result 中将包含"5050" "%d".
invoke MessageBoxA，0，offset result，offset prompt，0 #称为 API (Application Program Interface).
MessageboxA(0，format，prompt，0)
                #正文 标题
    ret #return
end main #指定程序的起始执行点即eip的初始值，end 后面的标号决定了程序刚开始运行时eip的值.
~~~

~~~
.386 #表示会用到32位的寄存器.
code segment use16 #相当于'{'，use16表示使用16位的地址.

assume cs:code
main:       
    mov eax，0
    mov ebx，1
next:
    add eax，ebx 
    add ebx，1 
    cmp ebx，100 
    jbe next 
code ends #相当于'}'
end main
~~~

Win+R 输入 command 打开 DOS 终端，进入 D 盘中的 MASM 目录中，masm name.asm 生成 name.obj，link name.obj 生成 name.exe.  
使用 td name.exe 进行 debug，按 Ctrl+R/在寄存器界面单击右键切换32位/16位的寄存器.  
cli 是一条特权指令，含义为 clear interrup，表示禁止硬件中断.  
Windows的用户程序是不允许执行该条指令的.  

~~~
#输入和输出，并判断是否为大写字母(getchar&putchar)
.386
code segment use16
assume cs:code
main:
    mov ah， 1
    int 21h #AL = getchar()，int 21h 是一个中断集，int:interrupt，指软件中断，ah = 1 表示调用该中断集中的1号子中断.
    cmp al， 'A'
    jb not_upper #jb:jump if below
    cmp al， 'Z'
    ja not_upper #ja:jump if above
is_upper:
    mov ah， 2
    mov dl， 'U'
    int 21h #putchar(DL)
    jmp exit
not_upper:
    mov ah， 2
    mov dl， 'O'
    int 21h
exit:
    move ah， 4Ch
    move al， 0
    int 21h #exit(0)
code ends
end main
~~~

## *3.16*  
 
~~~
data segment
a db "ABC"
s db "Hello$World!"， 0Dh， 0Ah ，0 #函数经过编译后变为其首地址，数组经过编译后也变为其首地址.为防止与寄存器混淆，字母开头的十六进制数前需要加上0.
#                                offset s 称为 s 的偏移地址 = 其离 data 段首的距离 = 3 
#                   回车 换行     windows 中换到下一行行首需要回车和换行两个操.
#                   "\r""\n"     回车:光标回到行首;换行:光标移动到下一行同一列.
data ends

code segment 
assume cs:code，ds:data
main:
    mov ax，seg s # 或mov ax，data;seg s:取数组 s 的段地址.编译时会将 seg s 编译为 delta = (seg s - 首段段地址)，此处为0，，编译后即 mov ax，0.  
                 # 运行时操作系统即 dos 会对 delta 进行修正: delta += 首段的实际段地址，此过程被称为重定位(relocating).
                 # mov ax，seg s 编译后的机器语言为 B8 00 00，假定程序的首段地址为 1000h，则程序运行时机器语言变为 B8 00 10.
                 # 机器能知道此处需要修正是因为编译时生成了重定向表，对需要重定向的位置进行了标记，此标记被写在文件头中.                
    mov ds，ax # ds:数据段寄存器，只用来存储标号或变量的段地址，不能接受常数赋值，只接受另一个寄存器/变量赋值，另外还有 cs，ss，es 这三个段寄存器.
    mov bx，0
next:            # s[i] = *(s+i)
    mov dl，s[bx] # 编译后变成 mov dl，ds:[bx + 3];ds 指该数组元素的段地址(segment address)，该数组元素的偏移地址为 3，该元素的完整地址为 ds:bx + 3
    cmp dl，0
    je exit # je:jump if equal
    move ah，2
    int 21h
    add bx，1
    jmp next
exit:         # cs = seg exit = code 的段地址.
    mov ah，4Ch
    int 21h
code ends
end main
~~~

同一个段内每一个变量的段地址都是一样的，为段首地址取前四位，个位必须为0，偏移地址的变化范围为 0000h:FFFFh.段的最大长度为 10000h 字节即 64k;段和段可以重叠.
|物理地址|相对地址|
|:----:|:----:|
|12340h|00h|
|12341h|01h|
|…………|…………|
|12350h|33h|
|…………|…………|
|12398h|33h|
|…………|…………|
|12398h|55h|
|…………|…………|
|2233Fh|77h|
|…………|…………|
|2234Fh|99h|

16 位的 CPU 指其所有寄存器都是 16 位的宽度;ax，bx，cx，dx，si，di，bp，sp，cs，ds，es，ss，ip，FL.  
bx，bp，si，di 表示偏移地址，cs 管理 code 段，ds 管理 data 段，两者必须被赋值.  
标号最终会转化为其偏移地址.  
ip 是 指令指针(instruction pointer)，用来保存将要执行的指令的偏移地址，而 cs 则是用来保存将要执行的指令的段地址，于是 cs:ip 用来指向要执行的那条指令.  
FL 是标志(flag)寄存器，它里面的16个位分别代表不同的意义，其中有些 bit 表示指令执行以后的状态，有些则可以控制 CPU 的行为.  
如 FL 的第0位称为 CF 位，其用来存储当前指令的进位.
~~~ nasm
    mov ax，0FFFFh
    add ax，1 ; AX = 0 ， CF = 1
    jnc no_carry_flag ;jnc:jump if not carry flag
    jc has_carry_flag ;jc:jump if carry flag

    has_carry_flag:
~~~

date 段和 code 段是连续的. `ds:[20] = cs:[0]`  
16位的 CPU 运行在实模式(real mode)下，用户代码拥有和操作系统一样的权限，可以执行任何指令，可以访问任何内存.32位的 CPU 除了可以继续运行在实模式下外，还可以运行在保护模式(protected mode)下.在保护模式下，用户代码的权限低于操作系统的权限，并不能执行任何指令，不能越权访问操作系统及其他进程占用的内存空间.  
32位的 CPU 中，cs，ds，es，ss 仍旧为16位的宽度，其他内存器都变成了32位，如 eax，ebx，ecx，edx，esi，edi，esp，ebp，eip，EFL.  
32位的 CPU 最多可以访问 4G ($2^{32}$)字节内存空间.  
实模式和保护模式下的段意义不同，例如当 ds = 8，esi  = 45678h 时，求 ds:esi 的物理地址.  
gdt 称为全局描述符表(global descriptor table)是一个数组，数组的每个元素都是8个字节.  
有一个寄存器叫 gdtr 会被赋值为 gdt 表的首地址.
~~~ text
设 gdt 表的首地址为 t:
t + 0 -> gdt[0]
t + 8 -> gdt[1]
t + 10h -> gdt[2]
t + 18h -> gdt[3]
~~~
把 ds 和 t 相加指向 gdt[1]，假定 gdt[1] 的8字节如下所示:  
~~~ text
00  01  02  03  04  05  06  07 ->下标  
FF, FF, 00, 00, 10, 93, 0F, 00 ->值  
~~~
段首地址取第2，3，4，7字节，此处为00100000h，于是 ds:45678h对应的物理地址为: 00100000h + 45678h = 00145678h.  
第0，1字节以及第6字节的低位用来定义段内的最大偏移地址，此处为 FFFFFh;第6字节的高位表.  
第5字节 93h 用来规定这是一个数据段，且可读可写，规定该段的访问权限是 ring 0. 93h = 1 _00_ 1 0011，权限由斜体部分决定.

## *3.23*

db, dw, dd, dq, dt  
08, 16, 32, 64, 80  
- db: char，b: byte;  
- dw: short int，w: word;  
- dd: long int or float，double words;  
- dq: __int64 or long long or double，q: quadruple words;  
- dt: long double，"%Lf".   

IEEE754 标准中单精度小数(即 float 类型的表示):  
0 *1000010 1* 1111110 11000000 00000000
1位符号位，8位指数位，23位尾数.偏置指数:a = (8位无符号数-127)，最终 *2^a，在二进制上表现为尾数小数点的移动.  
首先补一个1和小数点.1.11111101100000000000000->1111111.01100000000000000  

算术运算:  
add，sub 加减;mul，div 无符号数乘除;imul，idiv 有符号数乘除  
~~~
mov ax，0FFFFh
mov bx，0FFFFh
mul bx # dx:ax = ax * bx = 0FFFF 0001h = 4294836225，其中 dx = 0FFFFh，ax = 0001h，这里的冒号表示高16位和低16位的拼接.16位数的乘法默认被乘数为ax，且存放位置默认为 dx:ax.

mov ax，0FFFFh
mov bx，0FFFFh
imul bx # dx:ax = ax*bx = 0000 0001h
~~~
汇编语言的变量定义不区分符号数和无符号数.  
逻辑运算:and(&)，or(|)，xor(^)，not(~)，shl(<<)，shr(>>)， rol(_rotl())，ror(_rotr())    
shl:shift left; shr:shift right; rol:rotate left; ror:rotate right  
~~~
mov ah，10110110B # rol前 1011 0110
rol ah，1         # rol后 0110 1101，CF = 1
~~~

~~~
.386 # 接下来要用到32位寄存器，且偏移地址默认为32位.
data segment use16
a dd 56789ABCh
data ends
code segment use16
assume cs:code ds:data
main:
    mov ax，data # mov ax，seg a
    mov ds，ax   # 保证 ds 指向 data 段.
    mov eax，a   # 因为 a 需要用到段地址.
    mov cx，8
again:
    rol eax，4 # eax = 6789ABC5h
    mov edx，eax
    and edx，0Fh # edx = 5
    cmp edx，10
    jae is_alpha
    add dl，'0'
    jmp out_put
is_alpha:
    sub dl，10
    add dl，'A'
output:
    push eax
    mov ah，2
    int 21h
    pop eax
    dec cx # dec:自减;inc:自增
code ends
end main
~~~

## *3.30*  
1.直接寻址  

2.间接寻址(用寄存器，寄存器 + 常数来表示变量的偏移地址)  
cs，ds，es，ss 用来表示段地址;sp，bp，si，di 用来表示偏移地址.  
sp 和 ss 结合在一起构成 ss:sp 指向堆栈的顶端.
寄存器相加时只能以 b 开头和 i 结尾的寄存器相加.  
a. [bx]，[bp]，[si]，[di];  
b. [ax+2]，[bp-1]，[si+3]，[di-4];  
c. [bx+si];[bx+di]，[bp+si]，[bp+di];  
d. [bx+si+2]，[bx+di-2]，[bp+si+6]，[bp+di-6].  
  
汇编语言的多数指令要求两个操作数等宽，只要有一方的宽度已知，另一方的宽度必须与其一致.若两者均不明确，则需给一方加上宽度的限制.常数在汇编语言中没有明确的宽度.如:  
~~~
mov ds:[di]，0 #两者宽度均不明确，编译会报错.
正确的写法为:
mov byte ptr ds:[di]，0
翻译为 C 语言:
*(char *)(ds:di) = 0; #ptr 是 pointer 的缩写.
mov word ptr ds:[di]，0
翻译为 C 语言:
*(short int *)(ds:di) = 0
mov dword ptr ds:[di]，0
翻译为 C 语言:
*(long int *)(ds:di) = 0
或:
mov al，0
mov ds:[di]，al
~~~
注意宽度修饰不能用于常数，只能作用于变量.  

在程序中引用某个变量时， 该变量的段地址必须用段寄存器表示， 不能用常数表示;  
偏移地址既可以用直接寻址即常数， 又可以用间接寻址即[]中含有寄存器表示.
~~~
struct st
{
    char name[8];
    short int score;
}a[10];
# 假定 ds = seg a， bx = offset a. 现在要将 a[2].score 赋值给 ax.
mov si，20
mov ax，ds:[bx+si+8] # ax = a[2].score
# bx 是数组首元素的地址， si 是 a[0] 到 a[2] 的距离， 8是 name 数组的长度.
~~~
在原程序中引用变量:
~~~
data segment
abc db 1，2，3，4
xyz dw 789Ah，0BCDEh，9876h
asd dd 12345678h，56789ABCh
data ends

code segment 
assume cs:code，ds:data
main:
    mov ax，data
    mov ds，ax
    # 形式 1
    mov ah，abc[1] 
    mov ah，[abc+1]
    # 形式 2
    mov bx，offset abc 
    mov ah，[bx+1] 
    # 形式 3
    mov bx，1
    mov ah，abc[bx]
    mov ah，[abc+bx]
    # 形式 4
    mov bx，offset abc
    mov si，1
    mov ah，[bx+si]


code ends
end main
~~~
assume 的作用就是告诉编译器在引用某个变量或标号的段地址替换成对应的段寄存器， 但他并不会对段寄存器进行赋值.  
assume cs:code，ds:data 是编译指示语句(directive)，编译后不会产生机器码，但会消失.  
~~~
data segment
a db 'a'
end datas

code1 segment
assume cs:code1，ds:data
main:
    je far_away
next:
    mov dl，[a]
    mov al，2
    int 21h
code1 ends
    je next
code2 segment
assume cs:code2
    je next
code2 ends
end main
~~~
段寄存器优先级: ds>ss>es>cs. 当同一个段名和多个段寄存器建立了关联时，遵循如上的优先级顺序.  

Bochs 虚拟机及其内置调试器 Soft-ICE 介绍:  
Bochs 下载解压缩后，bochs\bochsdbg.exe 双击 -> Load -> dos.bxrc -> Start -> Continue (解释执行)  
常规的断点即软件断点(software breakpoint)会把设了断点的指令的首字节改成 0CCh 这个机器码，该机器码对应的指令是 int 3.当调试器执行到 int 3 时会自动断住，即 int 3 相当于一个断点.  
TD 只支持软件断点，不支持硬件断点.Soft-ICE 既支持软件断点，又支持硬件断点(hardware breakpoint).其中硬件断点有 3 种类型:  
bpmb 地址 r:当地址处的变量值被读取时断住;  
bpmb 地址 w:当地址处的变量值被写入时断住;  
bpmb 地址 x:当地址处的指令被执行时断住.  
80386 以上的 CPU 在硬件上支持硬件断点功能，当调试器设置硬件断点，它会把断点地址保存到寄存器 dr0，dr1，dr2，dr3中，再把断点的条件保存到 dr6 及 dr7 中.硬件断点的个数最多 4 个.硬件断点不会修改变量或指令的内容. 
~~~
# 检测设置软件断点会将指令首字节改为 0CCh.
code segment 
assume cs:code
main:
    cx，10
next:
    mov ah，2 # 此处设一个软件断点
    mov dl，'A'
    int 21h
    mov al，byte ptr [next] # 编译时会转为 mov al，byte ptr code:[next]，
                           # 再根据 assume 转为 mov al，byte ptr cs:[next]
    cmp al，0CCh
    je done
    sub cx，1
    cmp cx，0
    jnz next
done:
    mov al，4Ch
    int 21h
code ends
end main
~~~

## *4.6* 
用 winimage 打开 dos.img 这个硬盘镜像可以实现虚拟机内外文件的交换.  
找到 bochs\dos.img 双击   
bochs\bochsdbg.exe 双击启动 bochs  
Load -> dos.bxrc -> Start

复制 addr.c 到 bochs\tc 中; cd\tc  
tc:  
按 Alt + F 选择菜单 file -> load -> addr.c  
按 Alt + C 选择菜单 compile -> build all  
按 Alt + F 选择菜单 file -> quit  
td addr
用汇编语言控制文本方式下整个屏幕的输出：  
(x,y) 坐标对应的显卡偏移地址 = (y * 80 + x) * 2，显卡段地址固定为 0B800h.  
~~~
0000:0000 ~ 0000:FFFF
1000:0000 ~ 1000:FFFF
……
9000:0000 ~ 9000:FFFF # dos 及用户程序占用这块内存，长度为 640 KB

A000:0000 ~ A000:FFFF
B000:0000 ~ B000:7FFF
B800:0000 ~ B800:7FFF # 映射到显卡内存

C000:0000 ~ C000:FFFF
……
F000:0000 ~ F000:FFFF # 映射到 ROM(Read-Only-Memory)
~~~
映射是在电脑启动时执行 ROM 中 POST 代码过程中完成的; ROM 中还包括了 BIOS 代码，如 int 10h 及 int 16h 中断集就定义在 BIOS 中.  
~~~
code segment
assume cs:code
main:
    mov ax, 0B800h
    mov es, ax
    mov di, 0
    mov al, 'A'
    mov ah, 71h # 白色背景，蓝色前景
    mov cx, 2000
again:
    mov word ptr es:[di], ax # ax = 7141h
    add di, 2
    sub cx, 1
    jnz again
end:
    mov ah, 1
    int 21h # 等待键盘敲键
    mov ah, 4Ch
    int 21h
code ends
end main
~~~
~~~
# C 中的实现
#include<stdio.h>
int main()
{
    unsigned char far *p;
    int i;
    p = (unsigned char far)
}
~~~
A000:0000 是图形模式 (graphics mode) 下的显卡地址.  
~~~
mov ah, 0
mov al, 13h
int 10h # 把显卡切换到 320 * 200 * 256 色图形模式
# al = 12h 表示 640 * 480 * 16 色图形模式
# al = 3h 表示
~~~
(x, y) 坐标对应的显卡偏移地址 = y * 320 + x.  

## *4.13*  
~~~
again:
    mov ds:[di], ax
    mov bx, 800h
wait_wait:
    mov dx, 0    
wait_a_while:
    sub ds, 1
    jnz wait_a_while  
    sub bx, 1
    jnz wait_wait

    mov word ptr ds:[di], 0020h
    add di, 2
    sub cx, 1
    jnz again
    mov ah, 1
~~~

键盘输入除了可以调用 int 21h/ah = 01h 外，还可以调用 int 16h/ah = 00h 属于 BIOS 中断. 
int 21h/ah = 01h 不能读取上下左右方向键也不能读取 PgUp PgDn Home End Insert Del F1~F12 这些键.
~~~
again:
    mov ah, 1
    int 16h # 检测键盘缓冲区是否为空，若为空，则返回 ZF = 1，否则返回 ZF = 0
    jz no_key
has_key:
    mov ah, 0
    int 16h # ax = 所敲键的编码，此处从键盘缓冲中读取一个键，根据所敲的键执行不同的分支
no_key:
    jmp again    
~~~

~~~
draw:
    mov ax, [y]
    mov bp, 80
    mul bp # dx:ax = ax * bp
    add ax, [x]
    add ax, ax # 或 shl ax, 1
    mov bx, ax
    mov es:[bx], 1720h
check_key: # 刷新屏幕画面
    mov ah, 1
    int 16h
    jnz has_key
    jmp check_key
has_key
    cmp ax, 4800h
    je is_up
    cmp ax, 5000h
    je is_up
    cmp ax, 4B00h
    je is_up
    cmp ax, 4800h
    je is_up
    jmp exit
is_up:
    cmp [y], 0
    je check_key
    dec [y]
    jmp draw
~~~
push ax / push word ptr ds:[bx]  
push eax / push dword ptr ds:[bx]
push ah 或 push al 是错误的用法，因为 push 的操作数只能是 16 位或 32 位  
pop ax / pop word ptr ds:[bx]  
pop eax / pop dword ptr ds:[bx]  
程序开始运行时，dos 会对以下寄存器做初始化赋值：  
cs = code ip = offset main ss = stk sp = 200h ds = es = psp 段地址  
psp 是程序段前缀(program segment prefix) 它是一个长度为 100h 字节的内存块，位于当前程序首段的前面，psp 由操作系统分配给当前程序，里面存放了与该 exe 相关的一些信息如命令行参数  
~~~
int main(int argc, char*argv[])
{

}
main.exe 123 xyz
argv[0]  [1] [2]
~~~
~~~
data segment
abc dw 1234,5678h
data ends

code segment
assume cs:code, ds:data, ss:stk
main:
    mov ax, data

stk segment stack # 堆栈段只能定义一个
db 200h dup('S') # 或写成 dw 100h dup('0') 为了分配空间而写了一个无名数组
stk ends # 程序刚开始运行时 ss = stk, sp = 200h
end main
~~~
当源程序没有定义堆栈段时，ss = 首段的段地址 = 1000h， sp = 0  
es: extra segment 附加段  
## *4.20*
<table class="fl-table" style="margin-top: 0.6em">
<tr>
    <td class="fl-table-node"></td>
    <td class="fl-table-node"></td>
    <td class="fl-table-node"></td>
    <td class="fl-table-node"></td>
    <td class="fl-table-node">OF</td>
    <td class="fl-table-node">DF</td>
    <td class="fl-table-node">IF</td>
    <td class="fl-table-node">TF</td>
    <td class="fl-table-node fl-affected">SF</td>
    <td class="fl-table-node fl-affected">ZF</td>
    <td class="fl-table-node"></td>
    <td class="fl-table-node fl-affected">AF</td>
    <td class="fl-table-node"></td>
    <td class="fl-table-node fl-affected">PF</td>
    <td class="fl-table-node"></td>
    <td class="fl-table-node fl-affected">CF</td>
</tr>
</table>
CF: 进位标志(carry flag)  
~~~
mov ah, 0FFh
add ah, 1 # ah = 0, CF = 1, 产生了进位
add ah, 2 # ah = 2, CF = 0
sub ah, 3 # ah = 0FFh, CF = 1, 产生了错位
~~~
移位指令也会影响 CF 的值，最后移出去的那一位会自动保存到 CF 中
~~~
mov ah, 10110110B
shr ah, 2 # 该语法要求源代码最前面加 .386，并且每个段定义时 segment 后跟 use16
mov cl, 2
shr ah, cl # 右移 2 位，CF = 1
~~~
与 CF 相关的两条跳转指令：  
jc：有进位则跳；jnc：无进位则跳  
adc：带进位加；clc: CF = 0; stc: CF = 1  
  
ZF: 零标志(zero flag)
~~~
    sub ax, ax # ax =  0, ZF = 1
    add ax, 1 # ax = 1, ZF = 0
    add ax, 0FFh # ax = 0, ZF = 1, CF = 1
    jz is_zero # 会进行跳转，因为当前 ZF == 1
~~~
与 jz 相反的指令是 jnz，jnz 是根据 ZF == 0 作出跳转
jz \equiv je; jnz \equiv jne
~~~
cmp ax, ax # cmp 指令内部做了减法，会影响 ZF 的状态
jz/je is_equal 会跳转到 is_equal
~~~
~~~
int ax = 0x1234, bx = 0x1234, cx;
cx = 1;
if (ax != bx) cx = 0;
# 注意 mov 指令不影响任何标志位
    mov ax, 1234h
    mov bx, 1234h
    sub ax, bx # ZF = 1
    mov bx = 1 # 此 mov 不影响 sub 指令产生的 ZF 状态
    jz is_zero
    mov bx = 0
    is_zero:

~~~
  
SF: 符号标志(sign flag)，其实就是运算结果的最高位
mov ah, 7Fh
add ah, 1 # ah = 80h = <u>1</u>000 0000B, SF = 1
sub ah, 1 # ah = 7Fh = 0111 1111B, SF = 0
jns positive # 会发生跳转，因为 SF == 0
与 jns 相反的指令为 js，js 是根据 SF == 1 作出跳转

OF:溢出标志(overflow flag)
~~~
    mov ah, 7Fh
    add ah, 1 # ah = 80h, OF = 1, ZF = 0, CF = 0, SF = 1
    mov ah, 80h
    add ah, 0FFh # ah = 7Fh, OF = 1, ZF = 0, CF = 1, SF = 0
    mov ah, 80h
    sub ah, 1 # ah = 7Fh, OF = 1, ZF = 0, CF =0, SF = 0
~~~
OF 也有两条相关的指令：jo, jno  
正负相加永不溢出
左移也会造成溢出  
~~~
    mov ah, 81h # ah = 1000 0001B
    shl ah, 1 # ah = 0000 0010B, OF = 1, CF = 1
~~~
左移导致的溢出只考虑移动 1 位，取移位后的数的最高位（即原数据的次高位）和 CF （即原数据的最高位进行）异或运算得到 OF

PF (Parity flag)奇偶标志
~~~
    mov ah, 4
    add ah, 1 # ah = 0000 0101B PF = 1 表示有偶数个 1
    mov ax, 0101h
    add ax, 0004h # ax = 0105h = 0000 0001 0000 0101B PF = 1; PF 只统计低八位中 1 的个数
~~~
PF 有两条相关指令：jp (PF == 1 则跳)；jnp (PF == 0 则跳)
其中 jp 也可以写作 jpe (jump if parity even), jnp 也可以写作 jpo (jump if parity odd)
假定要发送字符 'C' = 0<u>100 0011</u>B，现假定低 7 位为数据位，最高位为校验位，那么校验位的计算方法有 2 种：  
1. 奇校验：数据位 + 校验位合起来，1 的个数必须是奇数；
2. 偶校验：数据位 + 校验位合起来，1 的个数必须是偶数。  
现采用偶校验来发送 'C' ，那么校验位必须是 1，即实际发送的 8 位二进制值为 <u>1</u>100 0011，对方接受这 8 位值并保存在寄存器 al 中，接下来可以执行以下代码来验证 al 中的值是否有错：  
~~~
    or al, al # 故意产生运算，迫使 CPU 统计 al 中 1 的个数 
    jnp error # if (PF == 0) goto error;
good:

error:
 
~~~
~~~
or al, al
jz iszero

cmp al, 0
je iszero
~~~
前者效率更高

AF (Auxiliary Flag) 辅助进位标志 
低 4 位向高 4 位产生进位或借位，例如：
~~~
mov ah, 1Fh # 0001 1111
add ah, 1 # ah = 20h, AF = 1
~~~
AF 和 BCD (Binary Coded Decimal)码有关
~~~
mov al, 29h #分钟
add al, 08 # 过了 8 分钟，31h
daa # decimal adjust for addition 加法的十进制调整
# 这条指令会根据 AF = 1 或 (al & 0Fh) > 9，做以下运算:
# al = al + 6 使得 al = 37h 而实际上 29 + 8 = 37
# 若 CF = 1 或 al & 0F0h > 90h，则 al += 60h
~~~ 

## *5.11*  
设有以下定义
x dd 3.14
y dq 5.67
现在执行  
1. fld x
2. fld y
浮点状态寄存器的第 11 位至第 13 位保存了当前指针处的物理编号

除法溢出

## *5.17*  
代码复制：需要知道代码块的起始地址和代码块的长度
```nasm
main:
    push cs
    pop ds
    push cs
    pop es
    cld
    mov ah, 2
    mov dl, 'A'
    int 21h
    mov si, offset begin_flag
    mov di, 1000h
    mov cx, offset end_flag - offset begin_flag ; 可计算的常数
    rep  movsb
    mov cx, offset begin_flag - offset main 
    mov di, offset main ; 毁去之前调用过的代码
    mov bx, 1000h
    jmp bx
begin_flag:
    jmp next 
    ;因为是标号而不敢冒险，故留下了 3 个字节，
    ;进一步扫描发现 next 就在下面，但仍留下了 nop
next:
    mov al, 0
    rep stosb

```
