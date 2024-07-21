class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def findWord(i,j,word,idx):
            if (idx==len(word)):
                return True
            if (i<0 or j<0 or i>=len(board) or j>=len(board[i]) or board[i][j]=="$"):
                return False
            if board[i][j]!=word[idx]:
                return False
            temp = board[i][j]
            board[i][j]="$"
            direc =[[1,0],[-1,0],[0,1],[0,-1]]
            for k in direc:
                i_=i+k[0]
                j_=j+k[1]
                if findWord(i_,j_,word,idx+1):
                    return True
            board[i][j]=temp
            return False
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j]==word[0] and findWord(i,j,word,0)):
                    return True
        return False