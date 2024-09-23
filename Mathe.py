def ggt(a,b):
    if a < b:
        return ggt(b,a)
    elif a % b == 0:
        return b
    else:
        return ggt(a - b, b)