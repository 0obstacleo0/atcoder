n = int(input())
w = list(input().split())
words = ["and", "not", "that", "the", "you"]

for i in w:
    if i in words:
        print("Yes")
        exit()

print("No")
