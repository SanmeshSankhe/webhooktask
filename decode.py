import numpy as np

file_path = "file.txt"

data = []
max_row, max_col = 0, 0

# Read the file line by line
with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split(":")
        if len(parts) == 2:
            position, char = parts
            row_col = position.replace("row=", "").replace("column=", "").split()
            row, col = int(row_col[0]), int(row_col[1])
            data.append((row, col, char.strip()))
            max_row = max(max_row, row)
            max_col = max(max_col, col)

matrix = np.full((max_row + 1, max_col + 1), " ", dtype=str)

for row, col, char in data:
    matrix[row, col] = char

for row in matrix:
    print(" ".join(row))