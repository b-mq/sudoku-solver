from math import floor

# 9x9 values in a sudoku
COUNT_NUMBERS = int(9)

sudoku = [  0,  1,  2,  3,  4,  5,  6,  7,  8,
            9, 10, 11, 12, 13, 14, 15, 16, 17,
           18, 19, 20, 21, 22, 23, 24, 25, 26,
           27, 28, 29, 30, 31, 32, 33, 34, 35,
           36, 37, 38, 39, 40, 41, 42, 43, 44,
           45, 46, 47, 48, 49, 50, 51, 52, 53,
           54, 55, 56, 57, 58, 59, 60, 61, 62,
           63, 64, 65, 66, 67, 68, 69, 70, 71,
           72, 73, 74, 75, 76, 77, 78, 79, 80
           ]

def get_row_index(index):
  return int(floor(index / COUNT_NUMBERS))

def get_column_index(index):
  return int(index % COUNT_NUMBERS)

def get_horizontal_slice_by(index, sudoku):
  row_index = get_row_index(index) * COUNT_NUMBERS
  values = sudoku[row_index : row_index + COUNT_NUMBERS]
  return values

def get_vertical_slice_by(index, sudoku):
  col = get_column_index(index)
  values = [sudoku[x * COUNT_NUMBERS + col] for x in range(0, COUNT_NUMBERS)]
  return values

def get_3x3_slice_by(array, index):
  col_start = floor(get_column_index(index) / 3) * 3
  row_start = floor(get_row_index(index) / 3) * 3
  start = row_start * COUNT_NUMBERS + col_start
  values = []
  for row in range(3):
    for col in range(3):
      i = start + COUNT_NUMBERS * row + col
      values.append(sudoku[i])
  return values
