#find the cube root of a number using guess and check method

#for negative number
cube=int(input("Enter an integer: "))
for guess in range(abs(cube)+1):    #assume It as positive so weused absolute
    if guess**3==abs(cube):
        if cube<0:                     #to check to verify It is negative
            guess=-guess            # here dealing with negative cube here
            print('cube root of',cube,'is',guess)
        

          

         
