n=[0,1,2,3,0]
zero=[]
res=[]
for i in n:
    if i ==0:
        zero.append(i)
    else:
        res.append(i)
result=res+zero
print(result)
