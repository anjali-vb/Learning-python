#code to check i or u in a string
s="demo loops- fruit loops"
for char in(s):
 if char in 'iu':  #in is keyword used to directly check the alphabets
    print("There is an i or u")


#Another way which iterates through letters of s directly
s="demo loops- fruit loops"
for char in(s):
    if char=='i' or char=='u':
        print("There is an i or u")
    
