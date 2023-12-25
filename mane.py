# Потрібно порахувати суму чисел і середнє арифметичне у вказаному діапазоні

start = int(input("Start:"))
end = int(input("End:"))
sum = 0
count = 0
for i in range(start, end+1):
    sum += i
    count += 1
arithmetic_mean = sum/count
print("The sum of all number", sum)
print("Arithmetic mean of all numbers", arithmetic_mean)