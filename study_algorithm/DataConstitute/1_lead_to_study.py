"""
    数据结构于算法的代码机构导图:
        1.基本的数据类型如字典,元组,集合,字符串的一些python自带的一些函数.
            foundation_receive.py
        2.随机函数模块的复习:
            rand_module.py
        3.collection部分:
            Collections.py
        4.回溯/递归
            递归与回溯.py
        5. 哈希表算法:
            主要是求出给定元素的哈希值,然后可以根据哈希值对元素进行快速的查寻,但是可能会出现相同的哈希值,则需要用到常用的两种方式去解决
            Hash.py
        6.图的是实现和图的广度优先算法(利用队列) 和 深度优先算法(利用栈)
            Chaptet.py
        7. 查找类的算法:
            主要是使用二分查找  和   插值插值来进行  和  利用快速排序来进行查找(算法选择.py)
            search.py
        8.排序算法:
            主要是 快速排序算法(随机主元),快速排序(确定主元),归并排序
            sort_algorithm.py
        9.字符串的匹配算法:
            Rabin-Karp算法: 利用哈希表来进行查找,如果两个字符串的哈希值相同的话则进行,值的比较,如果值也相同则匹配成功
            KMP算法:在匹配前对模式进行处理,求出模式的next值,即匹配不成功后退的位置,从而避免了,不必要的重复比较
            Boyer-Moore算法:从模式的结尾向前进行比较,然后出现不匹配的结果,则有大致两个解决的方式,即坏字符 和 好后缀, 也可以只使用坏字符来进行匹配,
            虽然速度会比两中同时使用的慢,但是相比其他算法也快很多.
            string_algorithm.py
        10.贪心算法:
            通过查找局部最优解来尝试从中找到全局最优解的算法
            贪心.py

"""
from Collections import *
from rand_module import*
from Hash import*
from Chaptet import*
from search import*
from sort_algorithm import*
from string_agorithm import*
from 贪心 import*
