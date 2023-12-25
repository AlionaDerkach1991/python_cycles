# Print the number of numbers in multiples of 5
x1 = int(input("Range from:"))
x2 = int(input("Range up to:"))
x = x1 + 1
count = 0
for i in range(x1, x2+1, 1):
    if i % 5 == 0:
        count += 1
print(count, " numbers in multiples of 5")