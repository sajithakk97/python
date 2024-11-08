#Count occurrences of each element in a list:
# Given a list of strings, count how many times each string appears.
from collections import Counter
list=['apple','rose','yellow','rose','white','yellow']
for item in list:
    count_list=Counter(list)
print(dict(count_list))

#........second way......
count={}
for i in list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)