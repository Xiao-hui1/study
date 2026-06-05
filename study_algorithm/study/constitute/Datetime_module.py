from datetime import *
"""
        
        date: 表示一个理想的日期
        time：表示一天的中的时间，包含时、分、秒、微秒
        datetime: 是date 和 time 的组合体，同时包含日期和时间信息
        timedelta: 表示两个时间点之间的时间间隔，常用时间的加减运算
        tzinfo: 一个抽象基类，用于处理时区信息
"""

now = datetime.now()
print(f"{now}",now.year, now.month, now.day) #输出当前的日期时间：2026-04-09 16:53:42.478138

today = date.today()
print(today.year, today.month, today.day) #输出当前的日期：2026-04-09

tomorrow = today + timedelta(days = 1)
#计算明天的此时

past = now - timedelta(hours = 1, minutes = 30)
#计算一小时30分钟前的时间

diff = tomorrow - past
#计算两个时间的差值


# 1. 格式化: datetime 对象 -> 字符串
formatted_str = now.strftime("%Y年%m月%d日 %H:%M")
print("格式化后:", formatted_str) # 例如: 2026年04月08日 21:32

# 2. 解析: 字符串 -> datetime 对象
date_string = "2025-12-25 10:30:00"
parsed_dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("解析后:", parsed_dt) # 输出: 2025-12-25 10:30:00
