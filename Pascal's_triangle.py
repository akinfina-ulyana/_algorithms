N = 7
p = []

for i in range(3):
    row = [1] * (i+1)
    print(row)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = p[i-1][j-1] + p[i-1][j]

    p.append(row)

for line in p:
    print(line)