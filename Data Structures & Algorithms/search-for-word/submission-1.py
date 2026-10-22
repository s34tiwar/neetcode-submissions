class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, i):
            # we matched the whole length 
            if i == len(word):
                return True
            # outside the board 
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # current cee; does not match the char we need 
            if board[r][c] != word[i]:
                return False
            # save char and mark cell as visited 
            temp = board[r][c]
            #Without the "#" line, the DFS could loop back and reuse the same cell multiple times.
            board[r][c] = '#'
            # try all four direction 
            found = (
                dfs(r+1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or 
                dfs(r, c +1, i + 1) or 
                dfs(r, c - 1, i + 1)
            )
            # backtrack 
            board[r][c] = temp
            return found 
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False