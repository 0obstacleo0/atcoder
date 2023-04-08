h, w = map(int, input().split())
a = [input().split() for _ in range(h)]


def search(i, j, s):
    if a[i][j] in s:
        return

    if i == (h - 1) and j == (w - 1):
        global sum
        sum += 1
        return

    s.add(a[i][j])

    if i + 1 < h:
        search(i + 1, j, s)
    if j + 1 < w:
        search(i, j + 1, s)

    s.remove(a[i][j])


sum = 0
search(0, 0, set())
print(sum)
