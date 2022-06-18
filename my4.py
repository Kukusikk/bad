
n, m  = input("Введите n и m:  ").split()

matrix = [ list(input()) for _ in range(int(n))]

for i in range(int(n)):
        for j in range(int(m)):
            if matrix[i][j] == 'S':
                current_coordinates=[i, j]

def have_empty_cell():
    for i in matrix:
        for j in i:
            if j=='.':
                return True

    return False

i=current_coordinates[0]
j=current_coordinates[1]

while have_empty_cell():
    if matrix[i+1][j]=='.':
        matrix[i+1][j]='D'
        i+=1
        continue

    if matrix[i-1][j]=='.':
        matrix[i-1][j]='U'
        i-=1
        continue

    if matrix[i][j+1]=='.':
        matrix[i][j+1]='R'
        j+=1
        continue

    if matrix[i][j-1]=='.':
        matrix[i][j-1]='L'
        j-=1
        continue

    if matrix[i][j]=='D':
        i-=1
        continue

    if matrix[i][j]=='U':
        i+=1
        continue

    if matrix[i][j]=='R':
        j-=1
        continue

    if matrix[i][j]=='L':
        j+=1
        continue

[print(*i, sep='') for i in matrix ]