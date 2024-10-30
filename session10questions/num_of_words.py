#Count the words of a sentence  "Hello Its me","I have a beautiful smile","I can sing vwey well"

def count_words(S):
    """
        S is a string representing a sentence
        L is a sequence of characters between spaces
        returns how many words are the in S
    """
    
    L=S.split(' ')        #since the sentence inside S consists of many words combined as a sentence whwn we have to split the words of the sentence we can use split funtion
    return len(L)
print(count_words("Hello Its me"))
print(count_words("I have a beautiful smile"))
print(count_words("I can sing very well"))
