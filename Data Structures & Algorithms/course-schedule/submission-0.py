class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        precoursemap = {i: [] for i in range(numCourses)}
        visit = set()
        
        for crs,pre in prerequisites:
            precoursemap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if precoursemap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in precoursemap.get(crs):
                if not dfs(pre):
                    return False
            visit.remove(crs)
            precoursemap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

        