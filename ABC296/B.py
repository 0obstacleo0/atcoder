h, w = 8, 8
grid = [["" for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if j == 0:
            grid[i][j] = "a" + str(8 - i)
        if j == 1:
            grid[i][j] = "b" + str(8 - i)
        if j == 2:
            grid[i][j] = "c" + str(8 - i)
        if j == 3:
            grid[i][j] = "d" + str(8 - i)
        if j == 4:
            grid[i][j] = "e" + str(8 - i)
        if j == 5:
            grid[i][j] = "f" + str(8 - i)
        if j == 6:
            grid[i][j] = "g" + str(8 - i)
        if j == 7:
            grid[i][j] = "h" + str(8 - i)

s = []
for _ in range(h):
    s.append(input())

row = 0
for i in s:
    if "*" in i:
        col = 0
        for j in i:
            if j == "*":
                print(grid[row][col])
                exit()
            col += 1
    row += 1
