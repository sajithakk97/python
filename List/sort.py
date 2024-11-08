#Sort a list from user input.
lmt=int(input("Enter the limit"))
list=[]
print("Enter element in list")
for i in range(lmt):
    num=int(input())
    list.append(num)
list.sort()
print(list)
list.sort(reverse=True)
print(list)