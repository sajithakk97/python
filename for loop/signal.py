#Create a program that assigns a traffic light signal ("Stop", "Get Ready", "Go")
#  based on a color input (Red, Yellow, Green).
signal=input("Enter a color\n")
if(signal=='Red'):
    print("Stop")
elif(signal=='Yellow'):
    print("Get ready")
elif(signal=="Green"):
    print("Go")
else:
    print("enter a valid color")