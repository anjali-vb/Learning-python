#convert negative integer to binary

#here we can do It by setting a flag and taking absolute value to convert neg of a number to positive and do the calculations

num=-19
if num <0:
    is_neg=True          #setting a neg flag
    num=abs(num)         #taking absolute of the neg number for smooth calculations
else:
        neg_flag=False   #if the number is>0 then the negative flag will be False for this question
result=' '              #saving the result in an empty string for smooth calculations 
if num==0:
     result=0
while num>0:
     result=str(num%2)+result   #last binary bit take the remainder of number by by 2(num%2=remainder)
     num==num//2               #If we then divide the integer by 2 (num//2) now take the quotient,then all the bits gets shifted to the right keep doing successive divisionsand take each quotients as the next bits untill the quotient becomes less than 1
if neg_flag:
    result='-'+result           #after all the calculations we are adding the negative sign along with the result
    print(result)
           
