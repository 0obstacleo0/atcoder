n = int(input())
a = list(map(int, input().split()))

status = [False for _ in range(n)]
for i in range(1, n + 1):
    if status[i - 1] is False:
        status[a[i - 1] - 1] = True

ans = []
for i in range(1, n + 1):
    if status[i - 1] is False:
        ans.append(i)
print(len(ans))
print(*ans, sep=" ")
