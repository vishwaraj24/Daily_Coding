# Count Frequency ⭐
# Given:

arr = [1, 2, 2, 3, 1, 2, 4]
new={}
for i in arr:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
print(new)
