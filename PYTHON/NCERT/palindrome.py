n = int(input("Enter number : "))
og = n
reverse_num = 0
while n > 0:
    digit = n % 10
    reverse_num = reverse_num * 10 + digit
    n //= 10
if (reverse_num == og):
    print("palindrome")
else:
    print("Not palindrome")
