class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(1, len(edges)+1)}

        def dfs(src, target, visit):
            if src == target:
                return True

            visit.add(src)

            for nei in adj_list[src]:
                if nei not in visit:
                    if dfs(nei, target, visit):
                        return True
            return False
        
        for n1, n2 in edges:
            visit = set()
            if n1 in adj_list and n2 in adj_list and dfs(n1, n2, visit):
                return [n1,n2]

            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        return []
        