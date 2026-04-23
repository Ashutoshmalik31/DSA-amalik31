class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs, key=len)
        res = ""

        for i in range(len(shortest_word)):
            ch = shortest_word[i]
            for word in strs:
                if word[i] != ch:
                    return res
            res += ch

        return res