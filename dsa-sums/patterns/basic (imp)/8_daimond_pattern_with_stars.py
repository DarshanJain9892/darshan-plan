n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # Spaces
    for j in range(n - i):
        print(" ", end="")
    # Stars (2*i - 1)
    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n, 0, -1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars (2*i - 1)
    for k in range(2 * i - 1):
        print("*", end="")
    print()