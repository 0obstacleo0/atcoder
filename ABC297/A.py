n, d = map(int, input().split())
t = list(map(int, input().split()))

lt = -1
for i in range(n):
    if i == 0:
        continue
    if t[i] - t[i - 1] <= d:
        lt = t[i]
        print(lt)
        exit()

print(lt)
