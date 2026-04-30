class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return None
        
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        area = 0

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1 or (r,c) in visit:
                return 0
            visit.add((r,c))
            return (1 + dfs(r+1, c) 
                    + dfs(r-1, c) 
                    + dfs(r, c+1)  
                    + dfs(r, c-1)) 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area, dfs(row, col))
        return area



        # if not grid:
        #     return None
        
        # rows = len(grid)
        # cols = len(grid[0])
        # visit = set()
        # area = 0

        # def dfs(r,c):
        #     if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visit:
        #         return 0
        #     visit.add((r,c))
        #     return(1 + dfs(r+1,c)
        #              + dfs(r-1,c)
        #              + dfs(r,c+1)
        #              + dfs(r,c-1))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             area = max(area, dfs(r,c))
        # return area 