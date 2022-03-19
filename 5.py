#5.Different ways to clear a list in Python
l1=[3,5,4,2,7]
print("l1=",l1)
l1.clear()
print("after clearing l1=",l1)
l2=['a','c']
print("l2=",l2)
for i in l2:
    l2.remove(i)
print("after removing values l2=", l2)
l3=[1,4,6,3,2]
print("l3=",l3)
for i in range (0,len(l3)-1):
        l3.pop(i)
print("l3=",l3)

l4=[3,4,5,7]
print("l4=",l4)
l4=[]
print("after assigning a empty set", l4)


