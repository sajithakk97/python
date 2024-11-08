#Write a program to determine the smallest of three numbers
a=int(input("first number\n"))
b=int(input("second number\n"))
c=int(input("third number\n"))
if(a<b and a<c):
    print(a,"is smallest")
elif(b<a and b<c):
    print(b,"is smallest")
else:
    print(c,"is smallest")