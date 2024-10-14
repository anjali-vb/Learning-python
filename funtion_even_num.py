#using funtion  write a code which returns True if d divides n eventually for (n,d)

def div_by(n,d):     #def =keyword ,div_by=name ,(n,d)=parameters
    """                                             
        n and d are integers >0                          
        returns True if d divides n eventually, otherwise False
    """
    if n%d==0:
      return True
    else:
      return False
print(div_by(10,3))
print(div_by(40,2))
print(div_by(30,10))



#the contents inside the Docstring contains all the definitions of the parameters
#Docstring starts at """ and ends by """
