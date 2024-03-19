## Works, but lacks time becouse for in python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        acc = 1.0
        if n == 0:
            return acc
        elif n > 0:
            for _ in range(n):
                acc *= x
        else:
            for _ in range(abs(n)):
                acc /= x

        return acc


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n > 0:
            acc = x * self.myPow(x, n - 1)
            return acc
        else:
            acc = 1 / (x * self.myPow(x, abs(n) - 1))
            return acc


sol = Solution2()
print(sol.myPow(2, -1))
