true = [[101, 102, 104, 107, 111, 0, 0, 0, 0, 0], 
[0, 105, 108, 112, 0, 0, 0, 0, 0, 0], 
[106, 109, 113, 0, 0, 0, 0, 0, 0, 0], 
[110, 114, 103, 0, 0, 0, 0, 0, 0, 0], [115, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 215], [0, 0, 0, 0, 0, 0, 0, 0, 214, 210], [0, 0, 0, 0, 0, 0, 0, 213, 209, 206], [0, 0, 0, 0, 0, 0, 212, 208, 205, 203], [0, 0, 0, 0, 0, 211, 207, 204, 202, 201]]


p1 = [101, 102, 103, 104, 105, 106, 107,
      108, 109, 110, 111, 112, 113, 114, 115]
p2 = [201, 202, 203, 204, 205, 206, 207,
      208, 209, 210, 211, 212, 213, 214, 215]

false = {101: (0, 0), 102: (2, 3), 103: (0, 1), 104: (2, 0), 105: (1, 1), 106: (0, 2), 107: (3, 0), 108: (2, 1), 109: (1, 2), 110: (0, 3), 111: (4, 0), 112: (3, 1), 113: (2, 2), 114: (1, 3), 115: (0, 4), 201: (9, 9), 202: (8, 9), 203: (9, 8), 204: (7, 9), 205: (8, 8), 206: (9, 7), 207: (6, 9), 208: (7, 8), 209: (8, 7), 210: (9, 6), 211: (5, 9), 212: (6, 8), 213: (7, 7), 214: (8, 6), 215: (9, 5)}

for i in p1:
    x, y = false[i]
    if true[y][x] == i:
        print(i, True)
    else:
        print(i, False)

print('')
for i in p2:
    x, y = false[i]
    # print(i)
    # print([false[i]])
    # print(true[y][x])
    if true[y][x] == i:
        print(i, True)
    else:
        print(i, False)
    # print('')

# Jumlah langkah = 1

x = [[], []]
print(x)
x[0].append(3)
print(x)