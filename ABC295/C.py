from collections import Counter

n = map(int, input())
a = list(map(int, input().split()))

ans = 0
for i in Counter(a).values():
    ans += i // 2

print(ans)
