n, q = map(int, input().split())

status = [0] * n
ans = []

for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        status[x - 1] += 1
    elif c == 2:
        status[x - 1] += 2
    else:
        if status[x - 1] >= 2:
            ans.append("Yes")
        else:
            ans.append("No")

for i in ans:
    print(i)
