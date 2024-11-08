age=int(input("Enter your age:"))
if age>=0 and age<13:
    print("Child")
elif age>=13 and age<20:
    print("Teen")
elif(age>=20 and age<=64):
    print("Adult")
else:
    print("Senior")