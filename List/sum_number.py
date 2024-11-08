#Sum of numbers from user input
lmt=int(input("Enter the limit"))
list=[]
print("Enter element in list")
sum=0
for i in range(lmt):
    num=int(input())
    list.append(num)
    sum+=list[i]
print(f"Sum of number in list is {sum}",)