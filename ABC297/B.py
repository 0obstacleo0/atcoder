s = input()
b_pos = []
k_pos = -1
r_pos = []

ans = "No"

for i in range(len(s)):
    if s[i] == "B":
        b_pos.append(i)
    elif s[i] == "R":
        r_pos.append(i)
    elif s[i] == "K":
        k_pos = i

if (b_pos[0] % 2 + b_pos[1] % 2) != 1:
    print(ans)
    exit()
if r_pos[0] < k_pos and k_pos < r_pos[1]:
    ans = "Yes"

print(ans)
