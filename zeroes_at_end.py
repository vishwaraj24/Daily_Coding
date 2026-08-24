# Move Zeros to End
arr=[1, 0, 3, 0, 5, 0]
new=[]
count=0
for i in arr:
    if i!=0:
        new.append(i)
    else:
        count+=1
for i in range(count):
    new.append(0)
print(new)