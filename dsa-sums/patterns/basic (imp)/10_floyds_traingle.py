n = int(input("Enter the number of rows : "))
        
numb = 1
        
for i in range(1 , n+1):
    for j in range(i):
        print(numb , end=" ")
        numb=numb+1
    print()