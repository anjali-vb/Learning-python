#Make the words of a sentence in sorted order

def sort_words(S):
    """
        S is a string representing a sentence
        Returns a list containing all the words in S but sorted in alphabetical order.
    """
   
    L=S.split(' ')      #At first we have to slit the words of the sentence
    L.sort()            #then the words of the sentence are sorted
    return L
S="look at this photograph"
print(sort_words(S))
print(sort_words("this is very beautiful"))                   #eg
print(sort_words("sunflower has beautiful yellow colour"))    #eg   
