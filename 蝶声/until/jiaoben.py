#！/user/bin/python
#-*-coding:utf-8-*-
with open (file=r"E:\蝶声\data\yong.txt",mode='r',encoding="utf-8") as f:
    t=f.read().split(';')

s=[]
for i in t:
    k=i.replace('\n','').split(',')
    s.append(tuple(k))
print(s)



