attendance = [1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
present=0
absent=0
for i in attendance:
    if i==1:
        present+=1
    else:
        absent+=1
print("No. of present numbers:",present)
print("No. of absent numbers:",absent)