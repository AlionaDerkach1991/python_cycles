# Print all the numbers in multiples of 7
x1 = int(input("Range from:"))
x2 = int(input("Range up to:"))
x = x1 + 1
for i in range(x1, x2+1, 1):
    if i % 7 == 0:
        print(int(i), end=' ')
