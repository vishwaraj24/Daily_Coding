numbers = {10, 20, 30, 40}
num = int(input("Enter a number to remove: "))
if num in numbers:
    numbers.remove(num)
    print(numbers)
else:
    print("Number not found")