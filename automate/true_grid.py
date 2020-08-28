# grid = [
#     [".", ".", ".", "1", "4", ".", ".", "2", "."],
#     [".", ".", "6", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", ".", ".", ".", "."],
#     [".", ".", "1", ".", ".", ".", ".", ".", "."],
#     [".", "6", "7", ".", ".", ".", ".", ".", "9"],
#     [".", ".", ".", ".", ".", ".", "8", "1", "."],
#     [".", "3", ".", ".", ".", ".", ".", ".", "6"],
#     [".", ".", ".", ".", ".", "7", ".", ".", "."],
#     [".", ".", ".", "5", ".", ".", ".", "7", "."],
# ]

grid = [
    [".", "4", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "1", ".", ".", "7", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "3", ".", ".", ".", "6", "."],
    [".", ".", ".", ".", ".", "6", ".", "9", "."],
    [".", ".", ".", ".", "1", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "8", ".", ".", ".", ".", "."],
]


def sudoku2(grid):
    l = len(grid)
    vertical = [set() for _ in range(l)]
    multi = [set() for _ in range(l)]
    for row in grid:
        for n in row:
            if n.isdigit():
                if row.index(n) in range(0:2)
                    multi[].add(n)
                if row.count(n) > 1:
                    return False
                elif n in vertical[row.index(n)]:
                    return False
                elif n not in vertical[row.index(n)]:
                    vertical[row.index(n)].add(n)

    return True


result = sudoku2(grid)
print(result)
