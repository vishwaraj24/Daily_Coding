num = [1, 1, 2, 4, 5, 6, 7]

n = int(input("Enter the number: "))

count = 0

for i in range(len(num)):
    if num[i] == n:
        count += 1

print("Count =", count)