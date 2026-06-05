import random

random.random()         #随机生成一个[0，1)之间的小数

random.uniform(0, 100)      #生成0，100的随机小数

random.randint(0, 100)      #生成0，100的随机整数

random.randrange(0, 100,10) #生成从0，10，20，30，40，。。，90中的一个随机数

random.choice([1,2,3,4,5,6,7,8,9,'hello','row','weapon'])  #从中随机取出一个数字，里面可以是list,tuple,string等。

random.shuffle(['python','is','powerful'])   #将列表中的元素顺序打乱

random.sample(range(0,100),10) #从中随机抽取出10个元素作为一个片段返回

