#find the cube root of a number using guess and check method

#for a positive number
cube=int(input("Enter a positive integer: "))
for guess in range(cube+1):      #when the cube is 1 want to include the cube
    if guess**3==cube:
        print('cube root of',cube,'is',guess)


          

         
