n = int(input())
s = input()

tmp = ""
ans = True
for i in s:
    if tmp == i:
        ans = False
    tmp = i

if ans:
    print("Yes")
else:
    print("No")
