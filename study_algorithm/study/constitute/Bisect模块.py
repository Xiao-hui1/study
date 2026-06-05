import bisect as bs
data = [1,12, 34, 65, 66, 76, 86, 95]
pos = bs.bisect_left(data, 25)    #返回在data数组中25应该插入的位置，左边的都 < 25

pos = bs.bisect_right(data, 25)  #返回在data数组中25应该插入的位置，左边的都 <= 25

bs.insort_left(data, 25)    #在data数组中插入25，左边的都 < 25
bs.insort_right(data, 25)   #同理

