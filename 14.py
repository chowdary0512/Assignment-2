# 14.

n=int(input("enter the legnth of list"))

l=[]
for i in range(0,n):
    e=int(input("enter the element"))
    l.append(e)
print("l=",l)
for i in l:
    if i%2==1:
        print(i,"is a odd number")