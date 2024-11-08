#Write a program that categorizes a person’s BMI:
#Underweight (BMI < 18.5),    Normal weight (BMI 18.5-24.9),  Overweight (BMI 25-29.9)
#   Obese (BMI 30 and above)
bmi=float(input("Enter BMI"))
if(bmi<18.5):
    print("Underweight")
elif(bmi>=18.5 and bmi<=24.9):
    print("Normal weight")
elif(bmi>=25 and bmi<=29.9):
    print("Overweight")
else:
    print("Obese")