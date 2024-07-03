
 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i <= 1:
        continue
    k = 1
    for j in range(2, i + 1):
        if i % j == 0:
            k = k + 1
    if k >= 3:
        not_primes.append(i)
    if k < 3:
        primes.append(i)
print("Primes: ", primes)               # Primes:  [2, 3, 5, 7, 11, 13]
print("Not Primes: ", not_primes)         # Not Primes:  [4, 6, 8, 9, 10, 12, 14, 15]






