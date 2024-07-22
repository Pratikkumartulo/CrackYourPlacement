class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def CountNeighbour(i, j, board):
            count = 0
            item = board[i][j]
            for k in [[1,0],[0,1],[0,-1],[-1,0],[1,1],[-1,1],[-1,-1],[1,-1]]:
                a = k[0]
                b = k[1]
                ni, nj = i + a, j + b
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if board[ni][nj] == 1:
                        count += 1
            if item==1 and count<2:
                return 0
            if item==1 and (count==2 or count==3):
                return 1
            if item==1 and count>3:
                return 0
            if item==0 and count==3:
                return 1
        next_state = [[CountNeighbour(i, j, board) for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if next_state[i][j]==None:
                    next_state[i][j]=0
                board[i][j] = next_state[i][j]