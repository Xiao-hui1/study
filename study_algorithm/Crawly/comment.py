import re, csv, requests

with open("bilibili_comment.txt",'r',encoding='utf-8') as f:
    content = f.read()

aid = re.findall('"aid":(.*?),', content, re.S)
bvid = re.findall('"bvid":"(.*?)",', content, re.S)
cid = re.findall('"cid":(.*?),', content, re.S)
title = re.findall('"title":"(.*?)"', content, re.S)

res = []
for a in range(len(title)):
    t = {"aid": aid[a], "bvid": bvid[a], "cid": cid[a], "title": title[a]}
    res.append(t)

with open("res_comment.csv",'w',encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['aid', 'bvid', 'cid', 'title'])
    writer.writeheader()
    writer.writerows(res)
