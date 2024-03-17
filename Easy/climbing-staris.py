# # recursive approach, but not approved by LeetCode because of extended time
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 1
#         if n <= -1:
#             return 0

#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


sol = Solution()
print(sol.climbStairs(0))
