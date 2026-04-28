class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        freq_t = {}
        for chr in t:
            freq_t[chr] = 1 +  freq_t.get(chr, 0)
        
        have, need = 0, len(freq_t)
        freq_s = {}
        length = len(s) + 1
        l = 0
        res = [-1, -1]
        for r in range(len(s)):
            freq_s[s[r]] = 1 + freq_s.get(s[r], 0) 
            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < length:
                    res = [l, r]
                    length = r - l + 1
                freq_s[s[l]] -= 1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if length != len(s) + 1 else ""




        # if len(t) > len(s):
        #     return ""

        # freq_t, freq_s = {}, {}
        # for i in range(len(t)):
        #     freq_t[t[i]] = 1 + freq_t.get(t[i], 0)

        # have, need = 0, len(freq_t)

        # l = 0
        # length = float('inf')
        # res = [-1,-1]
        # for r in range(len(s)):
        #     freq_s[s[r]] = 1 + freq_s.get(s[r], 0)
        #     if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
        #         have += 1
        #     while have == need:
        #         if r - l + 1 < length:
        #             res = [l,r]
        #             length = r - l + 1

        #         freq_s[s[l]] -= 1
        #         if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
        #             have -= 1
        #         l += 1
        # l, r = res
        # return s[l:r+1] if length != float("inf") else ""
        
        