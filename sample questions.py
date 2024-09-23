#print numbers from 0 to 5
for n in range(5):
    print(n)
#if start=6,end=4 find the sum using running sum method
mysum = 0
start = 3
end = 5
for i in range(start, end):
    mysum += i
print(mysum)

mysum = 0
start = 2
end = 3
for i in range(start, end):
    mysum += i
print(mysum)

#code that loops over a range and prints howmany even numbers and odd numbers are in that range
num=0
for i in range(5):
    i+=1
    print(i)
    if i%2==0:
        print ("even number")
    else:
        print("odd number")

    
