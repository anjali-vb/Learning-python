#Alyssa,ben and Cindy are selling tickets.Ben sells two less than Alyssa,Cindy sells twice than Alyssa.totally there are 10 tickets.Howmany did each sold?

#solve it by using one loop over one variable(most efficient way)

for Alyssa in range(11):          #here alyssa is defined and replace loop with direct equations for other people
    Ben=Alyssa-2
    Cindy=2*Alyssa
    if Ben+Cindy+Alyssa==10:      #apply the given condition so we can print the number of tickets each one get
     print(f"Alyssa sold {Alyssa} tickets")
     print(f"Ben sold {Ben} tickets")
     print(f"Cindy sold {Cindy} tickets")
    
    
        
    
