class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict: dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for c in s:
            if c not in valid_dict:
                stack.append(c)
            else:
                if stack:
                    if stack[-1] != valid_dict[c]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True


sol = Solution()

print(sol.isValid("()[]}{"))
