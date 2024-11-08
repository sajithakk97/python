# Create a list of strings from user input
lmt=int(input("Enter the limit"))
list=[]
print("Enter elements in list")
for i in range(lmt):
    item=input()
    list.append(item)
print(list)