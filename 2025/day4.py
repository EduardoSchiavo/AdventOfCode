with open('examples/example4.txt') as ifile:
    inp = ifile.read().splitlines()


GRID = {}
for i in range(len(inp)):
    for j in range(len(inp[0])):
        GRID[i,j] = inp[i][j]

print(inp)
print(GRID)
