#user input list  creation
lmt=int(input("Enter limit"))
list1=[]
list2=[21,22]
for i in range(1,lmt+1):
    list1.append(i)
print(list1)
#      ..........insertion.........
list1.insert(2,45)
print("list after insertion is",list1)
#..........append.......
list1.append(8)
print("list after append",list1)
#.........extend......
list2.extend(list1)
print("Extended list is ",list2)
#.....slicing......
list3=['apple',"orange","grapes"]
print("slicing operation of list")
print(list3[:])
print(list3[1:2])
print(list3[2])
print(list3[-3:-1])
print(list3[-3:])


