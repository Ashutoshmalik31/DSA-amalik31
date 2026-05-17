class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                    output += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                    output += 1
    
        return output
