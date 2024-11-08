#Reverse a list from user input
lmt=int(input("Enter the limit"))
list=[]
print("Enter element in list")
for i in range(lmt):
    num=int(input())
    list.append(num)
print(list)
print("reversed list is")
list.reverse()
print(list)