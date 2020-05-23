# Fibonacci Series - Python Project

n = int(input("Enter How Many Elements you want in the Fibonacci series = "))

a = 0
b = 1

print ("Fibonacci Series with",n,"elements -: ")
print (a,end="")
print (","+str(b),end="")

while n>2:
    c=a+b
    a=b
    b=c
    print (","+str(c),end="")
    n-=1
