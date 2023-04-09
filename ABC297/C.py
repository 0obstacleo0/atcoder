h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if j == (w - 1):
            continue
        if s[i][j] == "T" and s[i][j + 1] == "T":
            s[i][j] = "P"
            s[i][j + 1] = "C"

for i in range(h):
    print(*s[i], sep="")
