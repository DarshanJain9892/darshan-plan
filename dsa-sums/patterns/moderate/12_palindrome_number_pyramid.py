n = int(input("Enter the number of rows : "))

for i in range(n , 1 ,-1):
    for j in range(i-1):
        print(" " , end="")
        for k in range(n-j):
            print(j , end="")
        print()