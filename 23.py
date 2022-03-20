#23. Python Program to print remove duplicates from a list

l=[5,8,4,3,5,8]
print("l=",l)
l1=set(l)
print("l1=",list(l1))

l=[4,5,4,3,2,3,2,1]
print("l=",l)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)