#Use conditional statements to classify a temperature input: "Cold" for below 0°C,
#     "Cool" for 0-15°C, "Warm" for 16-30°C, and "Hot" for above 30°C.
temp=int(input("Enter a temperature value:"))
if(temp<0):
    print("Cold")
elif(temp>=0 and temp<=15):
    print("Cool")
elif(temp>=16 and temp<=30):
    print("Warm")
else:
    print("Hot")