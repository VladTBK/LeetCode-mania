class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        idx = 0
        done_first = False
        done_second = False
        while not done_first or not done_second:
            try:
                merged += word1[idx]
            except IndexError:
                done_first = True
            try:
                merged += word2[idx]
            except IndexError:
                done_second = True
            idx += 1
        return merged


sol = Solution()
print(sol.mergeAlternately("abcd", "pq"))
