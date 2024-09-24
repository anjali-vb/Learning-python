#float to round conversion
x=5.9
y=float(x)
print(y)
print(type(y))

#float to int
x=6.2
y=int(x)
print(y)
print(type(y))

#int to float
x=7.2
y=float(7.2)
print(y)
print(type(y))

#(4+2)*6-1
x=(4+2)*6-1
print((4+2)*6-1)

#3+4
x=(3+4)
print(x)

##To find the perimeter and area of the circle and then increment radius by one
pi=355/113
radius=2.2
print(2*pi*radius)
print(pi*radius**2)
radius=radius+1    #here we are changing the bindings previous value may still stored in the memory but lost the handle for it.
print(2*pi*radius)
print(pi*radius**2)

#how can we find an integer is an even number eg:4,5
x=4
if x%2==0:
    print(x,'is an even number')
else:
        print(x,'is an odd number')
x=5
if x%2==0:
    print(x,'is an even number')
else:
        print(x,'is an odd number')



       
