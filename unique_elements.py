# Remove Duplicates
# Given a list, create a new list containing only unique elements.
num=[10,10,4,2,2,5,8,8,56]
n=[]
for i in num:
    if i not in n:
        n.append(i)
print(n)