class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict_normal = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        sum = 0
        idx = 0
        while idx < len(s):
            chars = ""
            if idx != len(s) - 1:
                chars = s[idx] + s[idx + 1]
            if chars in roman_dict_normal:
                sum += roman_dict_normal[chars]
                idx += 1
            else:
                sum += roman_dict_normal[s[idx]]
            idx += 1
        return sum
