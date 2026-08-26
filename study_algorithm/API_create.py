import streamlit as st

st.title("hello world")

st.header("这是一个一级标题")
st.subheader("llllll")

import math
def fun(x):
    if x == 2:
        return 1
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return 0
    return 1

t = int(input())
for i in range(t):
    n = int(input())
    res = []
    cur = 2
    while n:
        if fun(cur):
            while n % cur:
                res.append(cur)
                n //= cur
        cur += 1
    print(*res)
