class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq_s1 = {}
        for s in range(len(s1)):
            freq_s1[s1[s]] = 1 + freq_s1.get(s1[s], 0)
        print(freq_s1)

        freq_s2 = {}
        l = 0
        for r in range(len(s2)):
            freq_s2[s2[r]] = 1 + freq_s2.get(s2[r], 0)
            while r - l + 1 > len(s1):
                freq_s2[s2[l]] -= 1
                if freq_s2[s2[l]] == 0:
                    del freq_s2[s2[l]]
                l += 1
            if freq_s1 == freq_s2:
                    return True
        
        return freq_s1 == freq_s2
        
        
        
        
        
        
        
        
        
        
        
        # if len(s1) > len(s2):
        #     return False

        # freq_s1 = {}
        # for i in range(len(s1)):
        #     freq_s1[s1[i]] = 1 + freq_s1.get(s1[i], 0)

        # l = 0
        # freq_s2 = {}
        # for r in range(len(s2)):
        #     freq_s2[s2[r]] = 1 + freq_s2.get(s2[r], 0)
        #     if r - l + 1 > len(s1):
        #         freq_s2[s2[l]] -= 1
        #         if freq_s2[s2[l]] == 0:
        #             del freq_s2[s2[l]]
        #         l += 1
        #     if freq_s1 == freq_s2:
        #         return True

        # return freq_s1 == freq_s2
            