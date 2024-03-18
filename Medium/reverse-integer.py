class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0:
            x = abs(x)
            is_neg = True

        rev_arr = [int(i) for i in str(x)][::-1]
        order = len(rev_arr) - 1
        output = 0
        for i, val in enumerate(rev_arr):
            if val != 0:
                output += val * 10 ** (order - i)
        if output >= 2**31 - 1:
            return 0
        return output if not is_neg else -output


sol = Solution()
print(sol.reverse(123))
