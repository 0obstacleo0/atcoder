n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = a + b
c.sort()
num = [i for i in range(1, len(c) + 1)]
dic = dict(zip(c, num))

ans = [[], []]
for i in a:
    ans[0].append(dic[i])
for i in b:
    ans[1].append(dic[i])

for i in ans:
    print(*i, sep=" ")
