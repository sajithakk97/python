#Create a program that categorizes movie ratings:
#  "G" for all ages   ,  "PG" for 8 and above  ,  "PG-13" for 13 and above  ,  
# "R" for 17 and above
age=int(input("Enter age:"))
if age>=17:
    print("R,PG,PG-13 and R movies")
elif(age>=13):
    print("G,PG and PG-13  movies")
elif(age>=8):
    print("G and PG   movies")
else:
    print("G")
