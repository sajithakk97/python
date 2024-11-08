#Create a program that checks if a year is a leap year
year=int(input("Enter a year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap year")
        else:
            print("Not leap")
    else:
        print("Leap year")
    
else:
    print("Not Leap year")


