class Solution:
    def parse_num(self, n: int) -> int:
        num_arr = [int(x) ** 2 for x in str(n)]
        acc = 0
        for val in num_arr:
            acc += val
        return acc

    def isHappy(self, n: int) -> bool:
        curr = self.parse_num(n)
        while True:
            if curr == 1:
                return True
            if curr >= (2**31 - 1) or curr <= 4:
                return False
            curr = self.parse_num(curr)


sol = Solution()
print(sol.isHappy(1111111))
