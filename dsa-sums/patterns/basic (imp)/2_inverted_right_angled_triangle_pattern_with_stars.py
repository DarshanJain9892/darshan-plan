# Input
n = int(input("Enter the number of rows: "))

# Loop from n down to 1
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()