# 12. Python program to find N largest elements from a list

n=int(input("enter the legnth of list"))

l=[]
for i in range(n):
    e=int(input("enter the element"))
    l.append(e)
print("l=",l)
l.sort()
print("the nth largest number is",l[n-1])

