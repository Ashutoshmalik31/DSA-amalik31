class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for temp in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[temp]:
                res[stack[-1][1]] = temp - stack[-1][1]
                stack.pop() 
            stack.append([temperatures[temp], temp])       
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = [0] * (len(temperatures))
        # stack = []
        # for temp in range(len(temperatures)):
        #     while stack and stack[-1][0] < temperatures[temp]:
        #         res[stack[-1][1]] = temp - stack[-1][1]
        #         stack.pop()
        #     stack.append(temp)
        # return res