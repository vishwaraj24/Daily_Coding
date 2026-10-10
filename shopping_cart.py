cart = [250, 120, 500, 80, 300]
total=0
for i in range(len(cart)):
    total+=cart[i]
print(total)
if total>1000:
    total=total-(total * 10/100)
print(total)
