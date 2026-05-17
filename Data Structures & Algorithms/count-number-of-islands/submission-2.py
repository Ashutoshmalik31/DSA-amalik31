class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        island = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    ro = r + dr
                    co = c + dc
                    if ro in range(ROWS) and co in range(COLS) and grid[ro][co] == "1" and (ro, co) not in visit: 
                        q.append((ro,co))
                        visit.add((ro,co))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row, col)
                    island += 1
        return island











        # if not grid:
        #     return None

        # rows = len(grid)
        # cols = len(grid[0])
        # visit = set()
        # islands = 0
       
        # def bfs(r,c):
        #     q = deque()
        #     visit.add((r,c))
        #     q.append((r,c))
        #     while q:
        #         r, c = q.popleft()
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr, dc in directions:
        #             row, col = r + dr, c + dc
        #             if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visit:
        #                 q.append((row, col))
        #                 visit.add((row,col))        

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visit:
        #             bfs(r,c)
        #             islands += 1
        # return islands










        # if not grid:
        #     return None

        # rows = len(grid)
        # cols = len(grid[0])
        # visit = set()
        # islands = 0

        # def bfs(r,c):
        #     q = deque()
        #     visit.add((r,c))
        #     q.append((r,c))
        #     while q:
        #         row, col = q.popleft()
        #         directions = [[1,0],[-1,0],[0,1],[0,-1]]
        #         for dr, dc in directions:
        #             r_new, c_new = row+dr, col+dc
        #             if (r_new in range(rows) and c_new in range(cols)
        #                 and grid[r_new][c_new] == "1" and (r_new,c_new) not in visit):
        #                 q.append((r_new,c_new))
        #                 visit.add((r_new,c_new)) 
                        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visit:
        #             bfs(r,c)
        #             islands += 1
        # return islands

        