num=[78,54,17,5,65,20,1]
low=0
high=len(num)-1
mid=low+high//2
key=int(input("Enter the key you want to find:"))
if key==mid:
    print("Key found at index :",mid)
elif(key>mid):
    high=mid-1
    print("Key found at ",high)
elif(key<mid):
    low=mid+1
    print("Key found at ",low)
else:
    print("Number not found")