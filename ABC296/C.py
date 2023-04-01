n, x = map(int, input().split())
a = list(map(int, input().split()))

a = set(list(a))

if x == 0:
    print("Yes")
    exit()

for i in a:
    if i - x in a:
        print("Yes")
        exit()
print("No")
