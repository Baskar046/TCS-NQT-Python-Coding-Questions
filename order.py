"""
Move Zeros to End

Description: Given an integer array, move all zeros to the end while preserving the order of non-zero elements.

Input: n (number of elements), then array of size n.

Output: Modified array.
"""


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
