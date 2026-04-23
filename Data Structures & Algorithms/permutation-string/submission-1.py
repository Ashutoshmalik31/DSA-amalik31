class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s1) > len(s2):
        #     return False

        # s1count, s2count = [0] * 26, [0] * 26
        # matches = 0
        # for i in range(len(s1)):
        #     s1count[ord(s1[i]) - ord("a")] += 1
        #     s2count[ord(s2[i]) - ord("a")] += 1

        # for i in range(26):
        #     matches += (1 if s1count[i] == s2count[i] else 0)

        # l = 0
        # for r in range(len(s1), len(s2)):
        #     if matches == 26:
        #         return True
        #     index = ord(s2[r]) - ord("a")
        #     s2count[index] += 1
        #     if s2count[index] == s1count[index]:
        #         matches += 1
        #     elif s1count[index] +1 == s2count[index]:
        #         matches -= 1

        #     index = ord(s2[l]) - ord("a")
        #     s2count[index] -= 1
        #     if s2count[index] == s1count[index]:
        #         matches += 1
        #     elif s1count[index] - 1 == s2count[index]:
        #         matches -= 1
        #     l += 1

        # return matches == 26   


        if len(s1) > len(s2):
            return False

        freq_s1 = {}
        for i in range(len(s1)):
            freq_s1[s1[i]] = 1 + freq_s1.get(s1[i], 0)

        l = 0
        freq_s2 = {}
        for r in range(len(s2)):
            freq_s2[s2[r]] = 1 + freq_s2.get(s2[r], 0)
            if r - l + 1 > len(s1):
                freq_s2[s2[l]] -= 1
                if freq_s2[s2[l]] == 0:
                    del freq_s2[s2[l]]
                l += 1
            if freq_s1 == freq_s2:
                return True

        return freq_s1 == freq_s2
            