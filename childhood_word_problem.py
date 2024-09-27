
for alyssa in range(11):       #checking all positive value sfor each
 for ben in range(11):
  for cindy in range(11):
    total=(alyssa + ben + cindy == 10)
    two_less=(ben == alyssa-2)         #for each value of alyssa check all possible values
    twice=(cindy == alyssa*2)
    if total and two_less and twice:        
       print(f"alyssa sold {alyssa} tickets")
       print(f"ben sold {ben} tickets")
       print(f"cindy sold {cindy} tickets")
