#suppose we want to add odd numbers between 2 and 8 using foe loop write a code usong funtion

def sum_odd(a,b):
    """
       a and b are integers greater than 0
       returns sum of the odd numbers inbetween them
    """
    sum_of_odds=0
    for i in range(a,b+1):    #b+1 is used beacuse to include b also        
      if i%2==1:              #number will be even number If It gives remainder 1 when divided by 2
       sum_of_odds+=i
    return sum_of_odds
print(sum_odd(2,4))
    
