# exercise 4.10.2

grid = [
        [".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", "0", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        [".", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
    ]

y = 0
while y < 6:
    for x in range(len(grid)):
        print(grid[x][y], end="")
    print("\n")
    y += 1