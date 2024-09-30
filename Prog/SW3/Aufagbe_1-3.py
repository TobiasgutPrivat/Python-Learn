def printStarts(lines: int):
    mid: int =  int(lines/2)
    for i in range(lines):
        print("* " * (mid - abs(i - mid) + 1))

printStarts(11)