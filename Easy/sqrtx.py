def mySqrt(self, x: int) -> int:
    checker = 1

    while 1:
        if checker * checker > x:
            for i in range(int(checker * 0.5), checker):
                if i * i > x:
                    return i - 1
        checker += checker
