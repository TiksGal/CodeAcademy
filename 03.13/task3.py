# Create a class Sudoku that takes a string as an argument. The string will contain the numbers of a regular 9x9 sudoku board left to right and top to bottom, with zeros filling up the empty cells.
# Attributes
# An instance of the class Sudoku will have one attribute:
#     board: a list representing the board, with sublits for each row, with the numbers as integers. Empty cell represented with 0.
# Methods
# An instance of the class Sudoku wil have three methods:
#     get_row(n): will return the row in position n.
#     get_col(n): will return the column in position n.
#     get_sqr([n, m]): will return the square in position n if only one argument is given, and the square to which the cell in position (n, m) belongs to if two arguments are given.
#     game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
# game.board ➞ [
#   [4, 1, 7, 9, 5, 0, 0, 3, 0],
#   [0, 0, 0, 0, 0, 0, 7, 0, 0],
#   [0, 6, 0, 0, 0, 7, 0, 0, 0],
#   [0, 5, 0, 0, 0, 9, 1, 0, 6],
#   [8, 0, 0, 6, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 3, 4, 0, 0],
#   [9, 0, 0, 0, 0, 5, 0, 0, 0],
#   [0, 0, 0, 4, 3, 0, 0, 0, 0],
#   [2, 0, 0, 7, 0, 1, 5, 8, 0]
# ]
# game.get_row(0) ➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
# game.get_col(8) ➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
# game.get_sqr(1) ➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
# game.get_sqr(1, 8) ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
# game.get_sqr(8, 3) ➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]

# class Sudoku:
#     def __init__(self, board_string):
#         self.board = [[int(board_string[row * 9 + col]) for col in range(9)] for row in range(9)]
        
#     def get_row(self, row_index):
#         return self.board[row_index]
        
#     def get_col(self, col_index):
#         return [row[col_index] for row in self.board]
    
#     def get_sqr(self, row_index, col_index=None):
#         if col_index is None:
#             row_index, col_index = row_index // 3 * 3, row_index % 3 * 3
#         else:
#             row_index, col_index = row_index // 3 * 3, col_index // 3 * 3
            
#         return [self.board[row][col] for row in range(row_index, row_index + 3) for col in range(col_index, col_index + 3)]

# game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
# print("My board", game.board)
# print(game.get_row(0))
# print(game.get_col(8))
# print(game.get_sqr(1))
# print(game.get_sqr(1, 8))
# print(game.get_sqr(8, 3))

