from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output: List[List[int]] = []
        if numRows == 0:
            return output

        for i in range(1, numRows + 1):
            new_arr = [1] * i
            if i >= 3:
                for j, _ in enumerate(new_arr[1:-1]):
                    new_arr[j + 1] = output[i - 2][j] + output[i - 2][j + 1]
            output.append(new_arr)

        return output


sol = Solution()
print(sol.generate(10))
