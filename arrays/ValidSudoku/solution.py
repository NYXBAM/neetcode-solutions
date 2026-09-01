def isValidSudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = {}
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            box_key = (r // 3, c // 3)
            if val == ".":
                continue
            if val in cols[c] or val in rows[r] or val in boxes.get(box_key, set()):
                return False

            rows[r].add(val)
            cols[c].add(val)
            if box_key not in boxes:
                boxes[box_key] = set()
            boxes[box_key].add(val)
    return True


board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(isValidSudoku(board))
