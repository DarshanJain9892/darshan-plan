n = int(input("Enter the number of rows : "))

for i in range(1, n + 1):
    # Inner loop for characters
    for j in range(i):
        # Convert ASCII to character (65 is 'A')
        print(chr(65 + j), end=" ")
    print()