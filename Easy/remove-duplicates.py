nums = [1, 1, 2, 2]


def removeDuplicates(nums) -> int:
    discoverd = [0 for _ in range(len(nums))]
    for idx, num in enumerate(nums):
        if num not in discoverd:
            discoverd[idx] = num
        else:
            discoverd[idx] = "_"
    under_count = 0
    for idx, val in enumerate(discoverd):
        if val == "_":
            discoverd.remove("_")
            under_count += 1
    discoverd += ["_" for _ in range(under_count)]

    return len(nums) - under_count, discoverd


print(removeDuplicates(nums))
