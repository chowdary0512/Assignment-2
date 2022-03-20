# 17. Python program to print positive numbers in a list
l1=[2,4,-3,0,22,-9]
print("l1=",l1)
l2=[]
for i in l1:
    if i>=0:
        l2.append(i)

print(" the positive numbers in a list are",l2)