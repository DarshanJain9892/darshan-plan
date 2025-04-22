# Ask user for number of rows
n = int(input("Enter the number of rows: "))

# Outer loop for rows
for i in range(1, n + 1):
    # Inner loop for columns (stars)
    for j in range(i):
        print("*", end=" ")
    # Move to the next line after each row
    print()