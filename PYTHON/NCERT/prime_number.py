n = 3
isPrime = True
for i in range(2, n):
    if n <= 1:
        isPrime = False
    else:
        if n % i == 0:
            isPrime = False
            break
if isPrime:
    print("Prime")
else:
    print("Not Prime")
