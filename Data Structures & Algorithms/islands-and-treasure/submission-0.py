class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()

        def addrooms(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == -1 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append([r,c])  
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])        

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addrooms(r + 1, c)
                addrooms(r - 1, c)
                addrooms(r, c + 1)
                addrooms(r, c - 1)
            dist += 1