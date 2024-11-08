#Remove duplicates from a list while maintaining the original order:
# Given a list of integers, remove duplicates while keeping the first occurrence of each element
list=[1,6,3,9,11,6,31,19,4]
result=[]
for item in list:
    if item not in result:
        result.append(item)
print(result)