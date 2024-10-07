#convert negative integer to binary

#here we can do It by setting a flag and taking absolute value to convert neg of a number to positive and do the calculations

num=-19            #number is saved in a variable called num
result=' '         #the last result we want to obtain is saved as an empty string
if num <0:         #here if the number is less than zero that is if number is neg nummber the flag we are setting will be true
    is_neg=True    #here flag value is_neg(flag name) is true for negative number
    num=abs(num)   #first we are doing calculations by taking the absolute value of the negative number for the smooth calculations and It is at the last step we are adding a neg sign to the result
else:              #else the flag value will be false
    is_neg=False   #flag value will false
if num==0:         #If the number is equal to zero result will be zero      
    result=0       #the result will be zero
while num>0:                  #here we are iterating using while loop when the number is greater than zero that is her we are taking positive part of the number for smooth calculation then after calculation we are adding negative sign
    result=str(num%2)+result  #to get the last binary bit divide the number by 2(num%2)
    num=num//2                #If we then divide the integer by 2 (num//2) now take the quotient,then all the bits gets shifted to the right keep doing successive divisionsand take each quotients as the next bits untill the quotient becomes less than           
if is_neg:                    #here in this problem we have already true neg flag value so for this value,
    result="-"+result         #we had done calculations by taking the positive value of the number so at last before printing the result we are adding a neg sign to the answer since the number here belongs to negative so the result should also neg
else:
    is_neg=False              #for positive numbers
print(result)
    
