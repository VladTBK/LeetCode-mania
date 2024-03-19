class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0

        while i < length:
            if flowerbed[i] == 0:

                next_ = flowerbed[i + 1] if i < length - 1 else 0

                if next_ == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
                if n == 0:
                    return True
            else:
                i += 2

        return n <= 0
