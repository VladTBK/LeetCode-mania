from collections import Counter
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_dict = Counter(ransomNote)
        for c in ransomNote:
            if letter_dict[c] > 0:
                letter_dict[c] -= 1
            else:
                return False
        return True


sol = Solution()
