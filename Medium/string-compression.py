# Bad compiling on leetcode but this is the answer
from collections import defaultdict
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        counter: dict[str, int] = defaultdict(int)
        for c in chars:
            counter[c] += 1
        s = ""
        for key, val in counter.items():
            s += key
            s += str(val)
        return len(s)


sol = Solution()
print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))
