# Проаналізуємо всі числа в заданому діапазоні:
#   Якщо число кратне 3, потрібно вивести слово "Fizz"
#   Якщо число кратне 5, потрібно вивести слово "Buzz"
#   Якщо число кратне 3 і 5, потрібно вивести "Fizz Buzz"
#   Якщо число не кратне ні 3, ні 5, потрібно вивести саме число.
x1 = int(input("Range from:"))
x2 = int(input("Range up to:"))
for i in range(x1, x2+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
