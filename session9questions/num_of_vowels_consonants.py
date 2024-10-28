#write a funtion which returns a tuple wher first element is the  number of vowels in a string s and the second element is the number of consonants in s

def num_of_chars(s):
    """
       s is a sequence of lower case letters
       returns a tuple wher first element is the number of vowels and the second element is the number of consonants
    """
    vowels="aeiou"          #any one of the required char count is saved in a variable for easy calculation
    (v,c)=(0,0)             #required tuple is initiated
    for char in s:
     if char in vowels:
        v+=1                #number of vowels is counted
     else:
        c+=1                #number of consonants is counted
    return(v,c)  
print(num_of_chars("abcd"))
print(num_of_chars("computer science"))
print(num_of_chars("information technology"))
        
