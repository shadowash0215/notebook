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
.data ;编译指示语句,表示变量、数组定义从此处开始.汇编语言中单引号及双引号无区别,他们既可以引住单个字符,又可以引住多个字符;
;字符串末尾并没有隐含的'\0';定义数组和定义变量无区别.
result db 100 dup(0) ;dup:duplicate
; == char result={0}
format db "%d",0
prompt db "The result",0

.code ;编译指示语句，帮助编译器识别代码从此处开始   
main:       ;标号
    mov eax,0
    mov ebx,1
next:
    add eax,ebx ;eax = eax + ebx
    add ebx,1 
    cmp ebx,100 ;cmp:compare
    jbe next ;jbe:jump if below or equal
invoke wsprintf,offset result,offset format,eax ;wsprintf 和 MessageboxA 是 Windows 操作系统下的函数 offset 为取地址.
wsprintf(&result[0],&format[0],eax); ;将 eax 中的内容以 char 类型 format 数组的格式输出到 char 类型 result 数组中.
wsprintf(result,format,eax) ;result 中将包含"5050" "%d".
invoke MessageBoxA,0,offset result,offset prompt,0 ;称为 API (Application Program Interface).
MessageboxA(0,format,prompt,0)
                ;正文 标题
    ret ;return
end main ;指定程序的起始执行点即eip的初始值,end 后面的标号决定了程序刚开始运行时eip的值.
~~~

~~~
.386 ;表示会用到32位的寄存器.
code segment use16 ;相当于'{',use16表示使用16位的地址.

assume cs:code
main:       
    mov eax,0
    mov ebx,1
next:
    add eax,ebx 
    add ebx,1 
    cmp ebx,100 
    jbe next 
code ends ;相当于'}'
end main
~~~

Win+R 输入 command 打开 DOS 终端,进入 D 盘中的 MASM 目录中,masm name.asm 生成 name.obj,link name.obj 生成 name.exe.  
使用 td name.exe 进行 debug,按 Ctrl+R/在寄存器界面单击右键切换32位/16位的寄存器.  
cli 是一条特权指令,含义为 clear interrup,表示禁止硬件中断.  
Windows的用户程序是不允许执行该条指令的.  

~~~
;输入和输出,并判断是否为大写字母(getchar&putchar)
.386
code segment use16
assume cs:code
main:
    mov ah, 1
    int 21h ;AL = getchar(),int 21h 是一个中断集,int:interrupt,指软件中断,ah = 1 表示调用该中断集中的1号子中断.
    cmp al, 'A'
    jb not_upper ;jb:jump if below
    cmp al, 'Z'
    ja not_upper ;ja:jump if above
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
    int 21h ;exit(0)
code ends
end main
~~~