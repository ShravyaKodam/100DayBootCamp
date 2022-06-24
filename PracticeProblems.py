# Python Program for Sum of squares of first n natural numbers
#
# Python Program for How to check if a given number is Fibonacci number?
number=int(input("Enter the number: "))
num=0
for i in range(1,number+1):
    square=i**2
    num=square+num
print(num)


numberFab=int(input("Enter the number to know the fibonacci number: "))
numberFabtoString=str(numberFab)
fabNumber=numberFabtoString[-1:]
fabNumbertoInt=int(fabNumber)
if numberFab==fabNumbertoInt:
    print("Fibonacci Number")
else:
    print("Not a Fibonacci Number")

num = int(input("Enter how many terms: "))
n1=0
n2=1
count=0

if num<0:
    print("Invalid Input")
elif num==1:
    print("Fibonacci: ")
    print(n1)
else:
    print("Fibonacci: ")
    while count<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count += 1
