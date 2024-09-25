#find the square root of a negative integer using guess and check method
guess=0
neg_flag=False
x=int (input("Enter an integer: "))
if x<0:
       neg_flag=True
while guess**2<x:
    guess=guess+1
if guess==x:
    print('square root','of',x,'is',guess)
else:
        print('x is not a perfect square')
if neg_flag:
    print('just checking....did you mean',-x, "?")
        

#find the square root of a negative integer using guess and check method
guess=0
neg_flag=False
x=int (input("Enter an integer: "))
if x<0:
       neg_flag=True
while guess**2<x:
    guess=guess+1
if guess**2==x:
    print('square root','of',x,'is',guess)
else:
        print('x is not a perfect square')
if neg_flag:
    print('just checking....did you mean',-x, "?")
        

       
       



        
    
