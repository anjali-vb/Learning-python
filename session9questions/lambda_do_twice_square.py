#what happens when you do twice of the lambda funtion in finding the square of the number


def do_twice(n,fn):            #here n is mapped to input and fn is mapped to anonymous lambda funtion
    """
        n is integer,returns square of the number
    """    

    return fn(fn(n))            #her lamda funtion is doing twice th operation once we got the result It is again doing the operation using lambda funtion ie the meaning of fn(fn(n))
print(do_twice(3,lambda x:x**2))         #eg)1
print(do_twice(-2,lambda x:x**2))        #eg)2
print(do_twice(10,lambda x:x**2))        #eg)3
