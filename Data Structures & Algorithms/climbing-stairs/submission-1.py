class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for _ in range(n):
            tmp = one
            one = one + two
            two = tmp

        return tmp