from collections import defaultdict
import collections


# works but long time
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest: list[list[str]] = [[] for _ in range(len(s))]
        for i in range(len(s)):
            seen_chars = [s[i]]
            longest[i].append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in seen_chars:
                    seen_chars.append(s[j])
                    longest[i] += s[j]
                else:
                    break
        max_len = 0
        for arr in longest:
            if len(arr) >= max_len:
                max_len = len(arr)
        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
