# Input
n = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end=" ")
    # Print stars
    for k in range(i):
        print("*", end=" ")
    print()
