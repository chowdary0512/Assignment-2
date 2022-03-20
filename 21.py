# 21. Python – Remove empty List from List
l=[1,5,6,[],[3,5],5,[6],[]]
print("l=",l)
print("after removing empty list l=",[i for i in l if i])
l1=[3,5,[],[5],6,[]]
print("l1=",l1)
print("after removing empty list l1=",[i for i in l1 if i!=[]])
l3=[5,9,[0],[],4,[],'']
print("l3=",l3)
print("after using filter l3=",list(filter(lambda i:i!=[] ,l3)))
