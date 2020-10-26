#defining the function "recur_factorial()" which will calculate teh factorial of given input of int datatype by user.
def recur_factorial(n):
    """Function to return the factorial
    of a number using recursion"""
#below condition will be true then the output will be number i.e, 1.
    if n == 0:
        return 1.
#below condition will be true then the output will be number i.e, 1.
    if n == 1:
        return n
#otherwise if the number is greater than 1 then the following recursive formula will be used.
    else:
        return n*recur_factorial(n-1)   
#storing the given input by user in a variable.
 n=int(input("enter the number = "))
 print(recur_factorial(n))
#end of code.
