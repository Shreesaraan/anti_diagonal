def anti_diagonal(rows,columns,matrix):
    for x in range(row_size - 1):
        i = 0
        j = x
        while i < row_size:
            if 0 <= j < column_size:
                print(array[i][j], end=" ")
            else:
                print("0", end=" ")
            i += 1
            j -= 1
        print()

    for y in range(column_size):
        i = y
        j = column_size - 1
        while j >= 0:
            if 0 <= i < row_size:
                print(array[i][j], end=" ")
            else:
                print("0", end=" ")
            i += 1
            j -= 1
        print()


rows = int(input("Number of Rows : "))
columns = int(input("Number of Columns : "))
matrix = []
for i in range(row_size):
    array.append(list(map(int, input().split())))
anti_diagonal(rows,columns,matrix) 