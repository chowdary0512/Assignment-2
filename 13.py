# 13. Python program to print even numbers in a list
n=int(input("enter the legnth of list"))

l=[]
for i in range(0,n):
    e=int(input("enter the element"))
    l.append(e)
print("l=",l)
for i in l:
    if i%2==0:
        print(i,"is a even number")
