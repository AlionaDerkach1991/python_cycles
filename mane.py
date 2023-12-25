# All numbers of the range are displayed on the screen
a = int(input("Range from"))
b = int(input("Range up to"))
c = int(input("step"))
for i in range(a, b+1, c):
    print(int(i), end=' ')
