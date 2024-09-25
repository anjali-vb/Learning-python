#To find the perimeter and area of the circle and then increment radius by one
pi=355/113
radius=2.2
print(2*pi*radius)
print(pi*radius**2)
radius=radius+1    #here we are changing the bindings previous value may still stored in the memory but lost the handle for it.
print(2*pi*radius)
print(pi*radius**2)
