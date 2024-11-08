num=int(input("Enter a value"))
if(num > 0):
    if(num%2==0):
        print(num,"is even number")
    else:
        print(num,"is odd number")
elif(num<0):
    print(num,"is negative number")
else:
    print("number is zero")
