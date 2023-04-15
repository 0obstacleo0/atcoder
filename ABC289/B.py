n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []
temp = []

for i in range(1, n + 1):
    temp.append(i)

    if i not in a:
        while len(temp) > 0:
            ans.append(temp.pop())

print(*ans)
