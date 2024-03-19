class Solution:
    def tribonacci(self, n: int) -> int:
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(1)
        if n == 0:
            return dp[0]
        if n == 1 or n == 2:
            return dp[1]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

        return dp[-1]
