from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for a in range(1, n):
    b = 1
    while a * b < n:
        dic[a * b] += 1
        b += 1

result = 0
for k, v in dic.items():
    cd = n - k
    if cd in dic:
        result += v * dic[cd]

print(result)
