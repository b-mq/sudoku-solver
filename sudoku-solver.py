#!/usr/bin/python3

# 9x9 values in a sudoku
COUNT_NUMBERS = int(9)

"""
a sudoku of indices, columns and rows

colum       0   1   2   3   4   5   6   7   8   | row
________________________________________________|_____
sudoku = [  0,  1,  2,  3,  4,  5,  6,  7,  8,  |  0
            9, 10, 11, 12, 13, 14, 15, 16, 17,  |  1
           18, 19, 20, 21, 22, 23, 24, 25, 26,  |  2
           27, 28, 29, 30, 31, 32, 33, 34, 35,  |  3
           36, 37, 38, 39, 40, 41, 42, 43, 44,  |  4
           45, 46, 47, 48, 49, 50, 51, 52, 53,  |  5
           54, 55, 56, 57, 58, 59, 60, 61, 62,  |  6
           63, 64, 65, 66, 67, 68, 69, 70, 71,  |  7
           72, 73, 74, 75, 76, 77, 78, 79, 80   |  8
         ]
"""

# the sudoku puzzle | 0 == unset
sudoku = [  5, 3, 0, 0, 7, 0, 0, 0, 0,
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9  ]


# returns the row and column number of given index
def get_row_column_from_index(index):
  row = index // COUNT_NUMBERS
  column = index - (row * COUNT_NUMBERS)
  return row, column

# returns the index given by row and column
def get_index_from_row_column(row, column):
  return row * COUNT_NUMBERS + column

# returns the row number index at index of sudoku
def get_row_index(index):
  return index // COUNT_NUMBERS

# returns the column number index at index of sudoku
def get_column_index(index):
  return int(index % COUNT_NUMBERS)

# returns a horizontal subset of the sudoku at index position (row)
def get_horizontal_slice_by(index, sudoku=sudoku):
  row_index = get_row_index(index) * COUNT_NUMBERS
  values = sudoku[row_index : row_index + COUNT_NUMBERS]
  return values

# returns a vertical subset of the sudoku at index position (column)
def get_vertical_slice_by(index, sudoku=sudoku):
  col = get_column_index(index)
  values = [sudoku[x * COUNT_NUMBERS + col] for x in range(COUNT_NUMBERS)]
  return values

# returns a 3x3 subset of the sudoku at index position
def get_3x3_slice_by(index, sudoku=sudoku):
  col_start = (get_column_index(index) // 3) * 3
  row_start = (get_row_index(index) // 3) * 3
  start = row_start * COUNT_NUMBERS + col_start
  values = []
  for row in range(3):
    for col in range(3):
      i = start + (COUNT_NUMBERS * row) + col
      values.append(sudoku[i])
  return values

# def is_possible(row, column, number, sudoku=sudoku):
  # check row
  for i in range(9):
    if sudoku[row * COUNT_NUMBERS + i] == number:
      return False
  # check column
  for i in range(9):
    if sudoku[column + COUNT_NUMBERS * i] == number:
      return False
  # check 3x3 area
  col0 = (column//3)*3
  row0 = (row//3)*3
  for r in range(3):
    for c in range(3):
      if sudoku[(row0 + r) * COUNT_NUMBERS + (col0 + c)] == number:
        return False
  return True

# checks if it's possible to put given number into sudoku at given index
def is_possible(index, number, sudoku=sudoku):
  if number in get_horizontal_slice_by(index, sudoku):
    return False
  elif number in get_vertical_slice_by(index, sudoku):
    return False
  elif number in get_3x3_slice_by(index, sudoku):
    return False
  else:
    return True

# print sudoku visually as 9x9 grid
def print_sudoku(sudoku=sudoku, ending=""):
  for i,value in enumerate(sudoku):
    val = f"{value:<2}"
    # horizontal separator
    if i!=0 and not (i/9)%3:
      print(f"\n{'– '*16}\n{val}", end=" ")
    # print row
    elif not i%9:
      print(f"\n{val}", end=" ")
    # print 3x3 seperator
    elif not i%3:
      print(f"|{val:>4}", end=" ")
    # just print value
    else:
      print(f"{val}", end=" ")
  print(f"\n{ending}")

# solve sudoku puzzle via backtracking and recursion
def solve(sudoku=sudoku):
  for row in range(COUNT_NUMBERS):
    for column in range(COUNT_NUMBERS):
      index = get_index_from_row_column(row, column)
      if sudoku[index] == 0:
        for n in range(1, 10):
          if is_possible(index=index, number=n, sudoku=sudoku):
            sudoku[index] = n
            solve(sudoku=sudoku)
            sudoku[index] = 0
        return
  print_sudoku(sudoku)

# the main function
if __name__ == "__main__":
  solve(sudoku)