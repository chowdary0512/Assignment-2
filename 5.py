#5.Different ways to clear a list in Python
l1=[3,5,4,2,7]
print("l1=",l1)
l1.clear()
print("after clearing l1=",l1)
l2=['a','c']
print("l2=",l2)
for i in l2:
    l2.remove('a')
    l2.remove('c')
print("after removing values l2=", l2)
l3=[4]
print("l3=",l3)
l3.pop(0)
print("after popping the values l3=",l3)

l4=[3,4,5,7]
print("l4=",l4)
l4=[]
print("after assigning a empty set l4", l4)

l5=[3,4,5,7]
print("l5=",l5)
l5 *=0
print("after assigning to list to 0 l5=", l5)

l6=[3,5,1,7]
print("l6=",l6)
del l6[:]
print("after deleting a list l6=",l6)



