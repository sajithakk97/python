#Write a program that determines the grade of a student based on their percentage.
#Use the following grading scheme:

#A: 90-100
#B: 80-89 ,   C: 70-79,  D: 60-69,  F: below 60.
mark=int(input("Enter your mark:"))
if mark>=90 and mark<=100:
    print("A grade")
elif(mark>=80 and mark<90):
    print("B grade")
elif(mark>=70 and mark<80):
    print("C grade")
elif(mark>=60 and mark<70):
    print("D grade")
else:
    print("F grade")