class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        precoursemap = {i:[] for i in range(numCourses)}
        visit = set()
        cycle = set()

        for crse, pre in prerequisites:
            precoursemap[crse].append(pre)

        output = []
        def dfs(crse):
            if crse in cycle:
                return False
            if crse in visit:
                return True
            
            cycle.add(crse)
            for pre in precoursemap[crse]:
                if not dfs(pre):
                    return False
            cycle.remove(crse)
            visit.add(crse)
            output.append(crse)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
                