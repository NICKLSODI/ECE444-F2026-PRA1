def reversed(n):
    return int(str(n)[::-1])
    
def formatter(n):
    n = int(n)
    return bin(n), oct(n)