def lengthOfLastWord(s: str) -> int:
    test = s.split()
    return len(test[-1])


s = "Hello World!"
print(lengthOfLastWord(s))
