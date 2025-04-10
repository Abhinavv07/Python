n = 5
for i in range(5):
    for j in range(5):
        if(i == j or i+j == n-1):
            print("*", end=' ')
        else:
            print(" ",end=' ')
    print()