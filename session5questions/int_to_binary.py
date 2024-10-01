#Convert the positive integer into binary

num=1507
result=' '                  #we are creating an empty string for the calculations
if num==0:
    result=0                #when the number is 0 result will be also 0 
while num>0:                #when the number is >0
 result=str(num%2)+result   #to get the last binary bit divide the number by 2(num%2)
 num=num//2                 #If we then divide the integer by 2 (num//2) now take the quotient,then all the bits gets shifted to the right keep doing successive divisionsand take each quotients as the next bits untill the quotient becomes less than 1
 print(result)
