#Append i that comes in the range of index length of L which is a list to that list Itself


L=[1,2,3,4]
for i in range(len(L)):       #will append the integers that have the same index length of L
    L.append(i)
print(L)
