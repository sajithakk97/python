#Reverse a list without using the reverse() method:
#  Given a list of integers, reverse the list and print the result
lmt=int(input("Enter the limit"))
list=[]
print("Enter element in list")
for i in range(lmt):
    num=int(input())
    list.append(num)
print("List after reverse without function is")
for i in range(len(list)):
    print(list[len(list)-1-i])