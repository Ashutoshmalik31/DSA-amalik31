class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visit or grid[row][col] != 1:
                        continue
                    q.append([row, col])
                    grid[row][col] = 2
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1



        # ROWS, COLS = len(grid), len(grid[0])
        # time, fresh = 0, 0
        # q = deque()
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             fresh += 1
        #         if grid[r][c] == 2:
        #             q.append([r,c])

        # directions = [[0,1],[0,-1],[1,0],[-1,0]]

        # while q and fresh > 0:
        #     for _ in range(len(q)):
        #         r,c = q.popleft()
        #         for dr, dc in directions:
        #             row, col = r + dr, c + dc
        #             if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
        #                 continue
        #             grid[row][col] = 2
        #             q.append([row, col])
        #             fresh -= 1
        #     time += 1
        # return time if fresh == 0 else -1

        