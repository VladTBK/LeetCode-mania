def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


addBinary("hi", "mom")
