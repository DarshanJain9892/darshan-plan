# Input
n = int(input("Enter the number of rows: "))

# Outer loop for rows
for i in range(n):
    # Print leading spaces
    for j in range(i):
        print(" ", end=" ")
    # Print stars
    for k in range(n - i):
        print("*", end=" ")
    print()
