for i in range(15):
    print(" ".join(["." if abs(j - i) < 2 else "x" for j in range(15)]))