class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for c in preMap[crs]:
                if not dfs(c):
                    return False
            preMap[crs] = []
            visit.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
        
        
        
        # precoursemap = {i: [] for i in range(numCourses)}
        # visit = set()
        
        # for crs,pre in prerequisites:
        #     precoursemap[crs].append(pre)
        
        # def dfs(crs):
        #     if crs in visit:
        #         return False
        #     if precoursemap[crs] == []:
        #         return True
            
        #     visit.add(crs)
        #     for pre in precoursemap.get(crs):
        #         if not dfs(pre):
        #             return False
        #     visit.remove(crs)
        #     precoursemap[crs] = []
        #     return True
        
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True

        