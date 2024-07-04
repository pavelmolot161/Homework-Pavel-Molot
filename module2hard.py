

nums = list(range(3,21))
print(nums)
n = int(input("Введите число: "))
for i in range(1, n):
    if i > n / 2:
        break
    for j in range(i + 1, n):    # j = 1
        if n % (i + j) == 0:
            print('|',i,j, end=' |')










