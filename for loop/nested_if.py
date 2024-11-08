#Use a nested if-else to determine if a number is divisible by both 2 and 3, 
# only by 2, only by 3, or by neither.
num=int(input("enter a number"))
if (num%2==0):
    if(num%3==0):
        print(num,"is divisible by both 2 and 3")
    else:
        print(num,"is divisible by 2 not by 3")
else:
    if(num %3==0):
        print(num,"is divisible by 3")
    else:
        print(num,"is neighther divisible by 2 nor 3")