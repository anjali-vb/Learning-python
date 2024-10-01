#print the number of unique letters in the string -abca
s="abca"
seen=' ' #first save the unique letters in a variable
count=0
for char in (s):
  if char not in seen:   #in -keyword used to ensure seen has only unique letters
   seen=seen+char
   count+=1
print(count)
