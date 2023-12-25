# Analyze the numbers in this range according to the rule:
# if a number is a multiple of 7, it should be displayed
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
x = x1 + 1
while x < x2:
    x += 1
    if x % 7 == 0:
        print(int(x), "- multiple of 7")
