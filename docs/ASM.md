# 汇编语言

## *3.9*

一般来说，三个 push+ 一个 call 表示程序在调用 main 函数,其之前的代码为 C 语言的初始化代码.  
OD 中 F2 为设置断点, F7 为跟踪进入.  
数据窗中 Ctrl+G 可以跟踪变量.  

有某些商用的对 exe 进行压缩的软件,如 Pecompact,VmProtect 可以把 exe 压缩为 exe ,压缩以后的 exe 也能双击运行.  
软件作者调用以下函数 sn  
sn = rsa(mac,私钥)  
软件检测 sn 是否正确  
rsa = (sn,公钥) == mac  
nop指令指什么也不做,no operation,机器码为 0x90.  
alt+backspace 可将改坏的指令恢复原样.  
搜索时使用较长的串以获取想要的结果.  
用十六进制编辑工具如 010editor 或 QuickView 都可以对 password.exe 进行搜索并修改.  
010editor 中按 Ctrl+F 输入要查找的串(Type 要注意修改为 hex bytes).  
QV 打开 password.exe,按回车键可以在 ascii/hex/asm 三种模式中切换,asm 模式有两种: 16位/32位,按 F2 切换(查看最下方状态栏或寄存器字母数).  
F7 进行搜索,tab 键在 ascii/hex 间切换,左上角编辑内有粘贴.  
F3 可将改坏的内容变为原样,tab 键可从左侧机器语言切换到右侧汇编指令,输入汇编语言进行修改,alt+F9 保存修改,F1 可获取帮助.  
md5 加密算法(但已经被证明无法防止碰撞).

~~~
.data #编译指示语句,表示变量、数组定义从此处开始.汇编语言中单引号及双引号无区别,他们既可以引住单个字符,又可以引住多个字符;
#字符串末尾并没有隐含的'\0';定义数组和定义变量无区别.
result db 100 dup(0) #dup:duplicate
# == char result={0}
format db "%d",0
prompt db "The result",0

.code #编译指示语句，帮助编译器识别代码从此处开始   
main:       #标号
    mov eax,0
    mov ebx,1
next:
    add eax,ebx #eax = eax + ebx
    add ebx,1 
    cmp ebx,100 #cmp:compare
    jbe next #jbe:jump if below or equal
invoke wsprintf,offset result,offset format,eax #wsprintf 和 MessageboxA 是 Windows 操作系统下的函数 offset 为取地址.
# == wsprintf(&result[0],&format[0],eax); 将 eax 中的内容以 char 类型 format 数组的格式输出到 char 类型 result 数组中.
# == wsprintf(result,format,eax) result 中将包含"5050" "%d".
invoke MessageBoxA,0,offset result,offset prompt,0 #称为 API (Application Program Interface).
MessageboxA(0,format,prompt,0)
                #正文 标题
    ret #return
end main #指定程序的起始执行点即eip的初始值,end 后面的标号决定了程序刚开始运行时eip的值.
~~~

~~~
.386 #表示会用到32位的寄存器.
code segment use16 #相当于'{',use16表示使用16位的地址.

assume cs:code
main:       
    mov eax,0
    mov ebx,1
next:
    add eax,ebx 
    add ebx,1 
    cmp ebx,100 
    jbe next 
code ends #相当于'}'
end main
~~~

Win+R 输入 command 打开 DOS 终端,进入 D 盘中的 MASM 目录中,masm name.asm 生成 name.obj,link name.obj 生成 name.exe.  
使用 td name.exe 进行 debug,按 Ctrl+R/在寄存器界面单击右键切换32位/16位的寄存器.  
cli 是一条特权指令,含义为 clear interrup,表示禁止硬件中断.  
Windows的用户程序是不允许执行该条指令的.  

~~~
#输入和输出,并判断是否为大写字母(getchar&putchar)
.386
code segment use16
assume cs:code
main:
    mov ah, 1
    int 21h #AL = getchar(),int 21h 是一个中断集,int:interrupt,指软件中断,ah = 1 表示调用该中断集中的1号子中断.
    cmp al, 'A'
    jb not_upper #jb:jump if below
    cmp al, 'Z'
    ja not_upper #ja:jump if above
is_upper:
    mov ah, 2
    mov dl, 'U'
    int 21h #putchar(DL)
    jmp exit
not_upper:
    mov ah, 2
    mov dl, 'O'
    int 21h
exit:
    move ah, 4Ch
    move al, 0
    int 21h #exit(0)
code ends
end main
~~~

## *3.16*  
 
~~~
data segment
a db "ABC"
s db "Hello$World!", 0Dh, 0Ah ,0 #函数经过编译后变为其首地址,数组经过编译后也变为其首地址.为防止与寄存器混淆,字母开头的十六进制数前需要加上0.
#                                offset s 称为 s 的偏移地址 = 其离 data 段首的距离 = 3 
#                   回车 换行     windows 中换到下一行行首需要回车和换行两个操.
#                   "\r""\n"     回车:光标回到行首;换行:光标移动到下一行同一列.
data ends

code segment 
assume cs:code,ds:data
main:
    mov ax,seg s #或mov ax,data;seg s:取数组 s 的段地址.
    mon ds,ax #ds:数据段寄存器,只用来存储标号或变量的段地址,不能接受常数赋值,只接受另一个寄存器/变量赋值,另外还有 cs,ss,es 这三个段寄存器.
    mov bx,0
next:            #s[i] = *(s+i)
    mov dl,s[bx] #编译后变成 mov dl,ds:[bx + 3];ds 指该数组元素的段地址(segment address),该数组元素的偏移地址为 3,该元素的完整地址为 ds:bx + 3
    cmp dl,0
    je exit #je:jump if equal
    move ah,2
    int 21h
    add bx,1
    jmp next
exit:         # cs = seg exit = code 的段地址.
    mov ah,4Ch
    int 21h
code ends
end main
~~~

同一个段内每一个变量的段地址都是一样的，为段首地址取前四位,个位必须为0,偏移地址的变化范围为 0000h:FFFFh.段的最大长度为 10000h 字节即 64k;段和段可以重叠.
|物理地址|相对地址|
|:----|----:|
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

16 位的 CPU 指其所有寄存器都是 16 位的宽度;ax,bx,cx,dx,si,di,bp,sp,cs,ds,es,ss,ip,FL.  
bx,bp,si,di 表示偏移地址,cs 管理 code 段,ds 管理 data 段,两者必须被赋值.  
标号最终会转化为其偏移地址.  
ip 是 指令指针(instruction pointer),用来保存将要执行的指令的偏移地址,而 cs 则是用来保存将要执行的指令的段地址,于是 cs:ip 用来指向要执行的那条指令.  
FL 是标志(flag)寄存器,它里面的16个位分别代表不同的意义,其中有些 bit 表示指令执行以后的状态,有些则可以控制 CPU 的行为.  
如 FL 的第0位称为 CF 位,其用来存储当前指令的进位.
~~~
mov ax,0FFFFh
add ax,1 # AX = 0 , CF = 1
jnc no_carry_flag #jnc:jump if not carry flag
jc has_carry_flag #jc:jump if carry flag

has_carry_flag:
~~~

date 段和 code 段是连续的. `ds:[20] = cs:[0]`  
16位的 CPU 运行在实模式(real mode)下,用户代码拥有和操作系统一样的权限,可以执行任何指令,可以访问任何内存.32位的 CPU 除了可以继续运行在实模式下外,还可以运行在保护模式(protected mode)下.在保护模式下,用户代码的权限低于操作系统的权限,并不能执行任何指令,不能越权访问操作系统及其他进程占用的内存空间.  
32位的 CPU 中,cs,ds,es,ss 仍旧为16位的宽度,其他内存器都变成了32位,如 eax,ebx,ecx,edx,esi,edi,esp,ebp,eip,EFL.  
32位的 CPU 最多可以访问 4G ($2^{32}$)字节内存空间.  
实模式和保护模式下的段意义不同,例如当 ds = 8,esi  = 45678h 时,求 ds:esi 的物理地址.  
gdt 称为全局描述符表(global descriptor table)是一个数组,数组的每个元素都是8个字节.  
有一个寄存器叫 gdtr 会被赋值为 gdt 表的首地址.
~~~
#设 gdt 表的首地址为 t:
t + 0 -> gdt[0]
t + 8 -> gdt[1]
t + 10h -> gdt[2]
t + 18h -> gdt[3]
~~~
把 ds 和 t 相加指向 `gdt[1]`,假定 `gdt[1]` 的8字节如下所示:  
~~~
0  1  2  3  4  5  6  7 #下标  
FF,FF,00,00,10,93,0F,00 #值  
~~~
段首地址取第2,3,4,7字节,此处为00100000h,于是 ds:45678h对应的物理地址为: 00100000h + 45678h = 00145678h.  
第0,1字节以及第6字节的低位用来定义段内的最大偏移地址,此处为 FFFFFh;第6字节的高位表.  
第5字节 93h 用来规定这是一个数据段,且可读可写,规定该段的访问权限是 ring 0. 93h = 1 _00_ 1 0011,权限由斜体部分决定.