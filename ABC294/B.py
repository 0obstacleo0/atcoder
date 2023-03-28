import string

h, w = map(int, input().split())
a = [list(input().split()) for _ in range(h)]

# abc辞書
alpha = list(string.ascii_uppercase)
number = [i for i in range(1, len(alpha) + 1)]
dic = dict(zip(number, alpha))

ans = []
for i in range(h):
    row = ""
    for j in range(w):
        if a[i][j] == "0":
            row += "."
        else:
            row += dic[int(a[i][j])]
    ans.append(row)

for i in range(h):
    print(ans[i])
