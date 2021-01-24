学习笔记
===============================
PriorityQueue源码笔记

初始方法有多个重制，对应无输入以及输入容量以及比较函数的情况

grow方法使用copy方法将size乘2，以至达到所需最小容量

add()作为接口，调用offer方法

off方法处理size的变化，调用siftUP方法实现具体插入操作

siftUp

peek方法返回queue[0]

indexOf查找指定元素，时间复杂度为O(n)

remove方法，使用indexOf方法查找指定元素并使用removeAt方法删除

removeEq方法，删除第一个相等的元素

contains方法， 利用indexOf方法判断queue内是否包含指定元素

toArray方法，借用Arrays.copyOf方法返回array

removeAt方法， 使用siftDown和siftUp方法实现删除指定位置的元素

siftUp和siftDown方法，能看出queue的结构是由数组实现的二叉树结构，按照对比符的返回值操作数组元素的上移以及下移，得出上述的插入以及删除方法的时间复杂度皆为O（log n）


