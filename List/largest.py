#Find the largest number in a list (from user input).
lmt=int(input("Enter the limit"))
list=[]
print("Enter element in list")
for i in range(lmt):
    num=int(input())
    list.append(num)
large=list[0]
for i in list:
    if i>large:
        large=i
print("largest element in list is",large)