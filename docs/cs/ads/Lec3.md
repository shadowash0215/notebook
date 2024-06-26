# 倒排索引

倒排索引是信息检索中最常用的数据结构之一，它是根据关键字来查找文档的数据结构。倒排索引当中包含了所有文档中的关键字，并且以链表的形式进行存储，每个关键字对应一个链表，链表中存储了包含这个关键字的文档的编号，出现的位置以及次数。

获取关键字可以使用 search tree 或者 hash table，二者各有利弊。search tree 查询速度较慢，但进行范围查询较为容易；hash table 查询速度较快，但是进行范围查询相对困难。

搜索的性能衡量指标有两个：**召回率**和**准确率**。召回率是指检索到的相关文档数与系统中所有相关文档数的比值，准确率是指检索到的相关文档数与检索到的文档总数的比值。

| |Relevant|Irrelevant|
|:---:|:---:|:---:|
|Retrieved|$R_R$|$I_R$|
|Not Retrieved|$R_N$|$I_N$|

Perscision = $\dfrac{R_R}{R_R+I_R}$

Recall = $\dfrac{R_R}{R_R+R_N}$