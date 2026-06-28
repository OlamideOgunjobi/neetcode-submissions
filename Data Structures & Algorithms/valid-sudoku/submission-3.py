class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check horizontally
        # check vertically
        # check boxes
        

        hor = collections.defaultdict(set)
        vert = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".": continue
                
                if board[row][col] in hor[row] or board[row][col] in vert[col] or board[row][col] in box[(row // 3, col // 3)]:

                    return False

                hor[row].add(board[row][col])
                vert[col].add(board[row][col])
                box[(row // 3, col // 3)].add(board[row][col])
    

        return True
        