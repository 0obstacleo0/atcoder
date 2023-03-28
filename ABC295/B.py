r, c = map(int, input().split())
b = [input() for _ in range(r)]

pos = [[False for _ in range(c)] for _ in range(r)]

# 爆発箇所をマーキング
for i in range(r):
    for j in range(c):
        if str.isdigit(b[i][j]):
            num = int(b[i][j])
            for k in range(r):
                for l in range(c):
                    if abs(i - k) + abs(j - l) <= num:
                        pos[k][l] = True

for i in range(r):
    for j in range(c):
        if pos[i][j]:
            b[i] = b[i][:j] + "." + b[i][j + 1 :]

for i in range(r):
    print(b[i])
