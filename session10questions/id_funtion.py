# use id funtion to check that Its the same object in memory

L=[4,5,6]
print("memory location of list=",id(L))                  #id funtion =It is used to check that Its the same object in memory
L.append(8)
print("memory location of list after appending=",id(L))
L=[ ]
print("memory location of list after clearing=",id(L))
