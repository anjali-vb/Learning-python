#Sample question

L1=['re']
L2=['mi']
L3=['do']
L4=L1+L2

print("L4 is",L4)
L5=L3.append(L4)     #some funtions mutate the list and dont return anything
print(L5)
L6=L1.append(L3)
print(L6)
