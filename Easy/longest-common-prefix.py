class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        smallest = sorted(strs)
        char_list = [ch for ch in smallest[0]]
        if char_list == []:
            return output

        for i, ch in enumerate(char_list):
            ok = True
            for j in range(len(strs)):
                if strs[j][i] != ch:
                    ok = False

            if not ok:
                break
            output += ch
        return output
