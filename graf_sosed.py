n, g = [int(x) for x in input().split()]
d = {a + 1: [] for a in range(n)}
ch = 0
for i in range(g):
    a, b = input().split()
    d[int(a)].append(b)
    d[int(b)].append(a)
for i in sorted(d.keys()):
    ch += len(d[i])
    for j in d[i]:
        ch += len(d[int(j)]) - 1
    print(ch, end = ' ')
    ch = 0
