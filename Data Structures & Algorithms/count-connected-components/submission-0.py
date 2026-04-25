class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)}
        visit = set()

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        
        def dfs(n):
            visit.add(n)
            for nei in adj_list[n]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
            return True        

        count = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        return count
        