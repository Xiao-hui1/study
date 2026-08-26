import re, csv

content = '我的微博账号:133\n553463，你记住了哦'

acount = re.findall('账号:(.*?)，',content, re.S)

se = re.search('账号:(.*?)，',content, re.S)
print(acount)
print(se)
print(se.group())
print(se.group(1))

data = [{'name': 'zhangsan', 'age': 18, 'salary': 100000},{'name':'lisi', 'age':17,'salary': 10054}]

with open('result.csv','w') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'salary'])
    #写入一个包含字典的列表，每一个字典对应CSV的一行。这些字典的Key必须和fieldnames相同。字典可以是普通的无序字典，
    #所以不需要关心字典里面Key的顺序，但是不能存在fieldnames里面没有的Key，也不能缺少fieldnames里面已有的Key
    writer.writeheader()
    writer.writerows(data)
    writer.writerow({'name': 'pc', 'age': 18, 'salary': 101008})


with open('result.csv','r') as f:
    writer = csv.DictReader(f)  #读取csv文件，以字典的形式存储
    for row in writer:
        print(row)