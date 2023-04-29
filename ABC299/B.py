n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

max = 0
max_pos = -1
if t in c:
    for i in range(n):
        if c[i] == t:
            if r[i] > max:
                max = r[i]
                max_pos = i
else:
    for i in range(n):
        if c[i] == c[0]:
            if r[i] > max:
                max = r[i]
                max_pos = i

print(max_pos + 1)
