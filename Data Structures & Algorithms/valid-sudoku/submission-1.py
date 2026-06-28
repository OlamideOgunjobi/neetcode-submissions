class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cond = []
        

        # checking for row and column validity
        for row in range(len(board)):
            row_vals = []
            col_vals = []
            for col in range(len(board)):

                if board[row][col].isnumeric():
                    if board[row][col] in row_vals:
                        return False
                    row_vals.append(board[row][col])

                if board[col][row].isnumeric():
                    if board[col][row] in col_vals:
                        return False
                    col_vals.append(board[col][row])

                
                

            # if list(set(row_vals)).sort() != row_vals.sort() or list(set(col_vals)).sort() != col_vals.sort():
            #     return False


        # box_vals = []
        # box_row = 0
        # # checking for sub-box validity
        # for box_index in range(0, 9, 3):
        #     for i in range(3):
        #         for col in range(box_index, box_index+3):
        #             for row in range(box_row, box_row+3):
        #                 if board[row][col].isnumeric():
        #                     if board[row][col] in box_vals:
        #                         return False
        #                 box_vals.append(board[row][col])      
        #                 box_row -= 2

        #         box_vals = []
        #         box_row += 3
        #     box_row = 0

        box_vals = []
        # the following is to iterate the sudoku
        for box_col in range(0, 9, 3):
            for box_row in range(0, 9, 3):

                # the following is to iterate each box
                for col in range(box_col, box_col+3):
                    for row in range(box_row, box_row+3):
                        if board[row][col].isnumeric():
                            if board[row][col] in box_vals:
                                return False
                            box_vals.append(board[row][col]) 

                # at the end of each box iteration reset the array
                box_vals = []
                    



        # if 0 in cond:
        #     return False

        return True