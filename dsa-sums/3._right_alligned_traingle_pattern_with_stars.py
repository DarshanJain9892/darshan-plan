# Input
n = int(input("Enter the number of rows: "))

# Outer loop for rows
for i in range(1, n + 1):
    # Print spaces first
    for j in range(n - i):
        print(" ", end=" ")
    # Print stars
    for k in range(i):
        print("*", end=" ")
    print()
