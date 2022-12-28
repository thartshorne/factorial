# hello
import sys


def recur_factorial(n):
    def recur_factorial(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a 
if __name__ == '__main__':
    arg = sys.argv
    print(recur_factorial(int(arg[1])))
