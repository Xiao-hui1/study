import requests
from multiprocessing.dummy import Pool
# source = requests.get('https://www.bilibili.com/video/BV14P546xEDp/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=12fdd9ff94cdbbc5ff6b43fc00b6f9b6').content.decode()
#
# print(source)

data = {'name': 'pc', 'password': '123456'}
html_formdata = requests.post('http://exercise.kingname.info/exercise_requests_post', data = data).content.decode()
#使用formdata 的形式获取网页数据

print(html_formdata)
print('-'*64)
html_json = requests.post('http://exercise.kingname.info/exercise_requests_post', json = data).content.decode()
print(html_json)


#使用多线程的技术，让代码同时计算很多个数的平方，就需要使用multiprocessing.dummy来实现
def calc_power2(a):
    return a * a

pool = Pool(3)
origin_num = [x for x in range(1, 11)]

result = pool.map(calc_power2, origin_num)
'''
    #线程池的map()方法接收两个参数，第1个参数是函数名，第2个参数是一个列表。注意：第1个参数仅仅是函数的名字，是不能带括号的。
    # 第2个参数是一个可迭代的对象，这个可迭代对象里面的每一个元素都会被函数clac_power2()接收来作为参数。
    # 除了列表以外，元组、集合或者字典都可以作为map()的第2个参数
'''

print(result)