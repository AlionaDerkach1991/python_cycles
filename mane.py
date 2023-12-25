# Print all numbers in the range in reverse order
a = int(input("Range from:"))  # Write a bigger value
b = int(input("Range up to:"))  # Write a smaller value
c = int(input("Step:"))
for i in range(a, b-1, -c):
    print(int(i), end=' ')
