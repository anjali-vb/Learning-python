#Make a list comprehension exmaple

a=[e**2 for e in range(6)]          #eg of an ist comprehension pattern
print(a)
b=[e**2 for e in range(8)if e%2==0]     #here comprehension funtion is applied only for the even numbers in the range
print(b)
c=[e**2 for e in range(8)if e%2!=0]     #here comprehension funtion is only applied for the odd numbers in the range
print(c)
d=[e+2 for e in range(10)if e%2==0]
print(d)
f=[e-1 for e in range(10)if e%2==0]
print(f)

