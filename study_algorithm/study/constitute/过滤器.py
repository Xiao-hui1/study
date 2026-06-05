#从列表中过滤出满足条件的值

#使用filter函数加内联函数 lambda

num = [1,3,5,8,4,6,3,56,26,23,67,267,84,145]

#过滤出列表中为偶数的值
even_num = filter(lambda x: x % 2 == 0, num)        #filter(function, iterable)当 function为 None是会将 iterable 中布尔值为 False 值过滤掉
print(list(even_num))

st =['world','weapon','legislation','peculiar','illusion','frame','margin']

#输出满足条件长度的字符串

val_str = filter(lambda word: len(word) > 5, st)
print(val_str)


#----------------------------------------------------------------------


""" 

        主要key 可以为一个元组,在元组中第一个元素为主要关键字,第二个为次要关键字....., 
        如果要设置主要关键字为降序排序,次要关键字为升序排序可以:
                    res = sorted(data, key=lambda x: (x[0],-x[0]), reverse=True)
                    使用 - 负好来进行操作
        
"""
#sorted(iterable,key=None,reverse=True)函数的用法  iterable :迭代的数据，key：用什么数据中的什么作为迭代的依据 ，reverse：为true是为降序(默认为升序)
val = [1,3,5,8,4,6,3,56,26,23,67,267,84,145]

s = sorted(val)
print(s)

s = sorted(val,reverse=True)
print(s)
#-------------------------------------------------------------------
#按照字符串的长度排序
st =['world','weapon','legislation','peculiar','illusion','frame','margin']

st_val = sorted(st,key = len)
print(st_val)

#按照字符串的最后一个字符排序
st =['world','weapon','legislation','peculiar','illusion','frame','margin']
val_str = sorted(st,key = lambda x: x[-1])
print(val_str)


student_dict = [
    {'name':'luca','grade':78},
    {'name':'last','grade':98},
    {'name':'Alice','grade':38},
    {'name':'Bob','grade':71},
]
#按照学生的成绩进行排序

ch = "sgafefgegsfds"
flag = ch.startswith("sga")    #判断字符串是否以sga开头，endswith()判断是否以子串结尾

student_dict = sorted(student_dict,key = lambda x: x['grade'])
print(student_dict)