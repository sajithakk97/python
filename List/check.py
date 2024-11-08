#Check if a number is in the list (from user input).
lmt=int(input("Enter the limit"))
list=[]
print("Enter element in list")
for i in range(lmt):
    num=int(input())
    list.append(num)
ele=int(input("Enter item to be search")) 
 
if ele in list:
    print("Element in list")

else:
    print("Not found") 