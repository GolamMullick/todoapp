rows = input("Enter number of rows ")
rows = int (rows)

k = 8
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()
