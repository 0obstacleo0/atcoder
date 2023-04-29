n = int(input())
s = input()


if "x" in s:
    print("No")
    exit()

for i in s:
    if i == "o":
        print("Yes")
        exit()

print("No")
