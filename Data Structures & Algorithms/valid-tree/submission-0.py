class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        if not n:
            return False
        
        adjmap = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adjmap[n1].append(n2)
            adjmap[n2].append(n1)
        
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adjmap[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
