def intToRoman(num: int) -> str:
    roman_dict_reverted = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    output = ""
    for i, val in enumerate(str(num)):
        if val == "0":
            continue
        else:



intToRoman(1042)
