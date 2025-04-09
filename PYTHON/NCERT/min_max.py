# Initialize the list with zeros
l = [0, 0, 0, 0, 0]
for i in range(len(l)):
    l[i] = int(input("==> "))

big = l[0]
sml = l[0]

for i in range(len(l)):
    if l[i] > big:
        big = l[i]
    if l[i] < sml:
        sml = l[i]
print("Biggest :- ", big)
print("Smallest :- ", sml)
