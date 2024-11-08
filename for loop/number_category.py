#Write a program to categorize a number as "Small" if it's between 1-10, 
#   "Medium" if between 11-20, and "Large" for values greater than 20.
num=int(input("Enter a value:"))
if (num>=1 and num<=10):
    print("Small")
elif(num>10 and num<=20):
    print("Medium")
else:
    print("Large")