#Alyssa,ben and Cindy are selling tickets.Ben sells two less than Alyssa,Cindy sells twice than Alyssa.totally there are 10 tickets.Howmany did each sold?

for alyssa in range(11):               #checking all positive value sfor each
 for ben in range(11):
  for cindy in range(11):
    total=(alyssa + ben + cindy == 10)
    two_less=(ben == alyssa-2)         #for each value of alyssa check all possible values
    twice=(cindy == alyssa*2)
    if total and two_less and twice:   #on the light of existing conditions we can print the number of tickets each sold      
       print(f"alyssa sold {alyssa} tickets")
       print(f"ben sold {ben} tickets")
       print(f"cindy sold {cindy} tickets")
