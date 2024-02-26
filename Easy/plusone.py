def plusOne(self, digits: List[int]) -> List[int]:
    if not digits:
        return [1]
    big_num = 0
    reversed_digi = digits[::-1]
    for i, val in enumerate(reversed_digi):
        big_num += val * 10**i
    big_num += 1
    return [int(digit) for digit in str(big_num)]
