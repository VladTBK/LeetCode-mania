hs = "leetcode"
nd = "sad"


def strStr(haystack: str, needle: str) -> int:
    n = len(needle)
    for i in range(len(haystack)):
        if haystack[i : n + i] == needle:
            return i
    return -1


print(strStr(hs, nd))
