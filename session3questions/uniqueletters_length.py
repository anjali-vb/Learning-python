s="abca"
seen='abc'
for char in (s):
 if char in seen:   #to ensure seen has only unique letters
  print(len(seen))
