# 22. Python Program to print duplicates from a list of integers
list=[4,5,4,3,2,3,2,1]
print("l=",list)
l1=[]
for i in list:
    if i not in l1:
        l1.append(i)
    else:
        print(i)



