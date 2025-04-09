n = int(input("Enter the value of n: "))
for i in range(5,(n+1) * 5,5):
    if (i % 2 ==0):
        print(i)
    else:
        print(i * -1)