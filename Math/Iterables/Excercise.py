from MathIterable import MathIterable
from math import sqrt

class Exercise(MathIterable):
    def calc_next(self, values):
        n = len(values) + 1
        # return 2**n / n
        # return sqrt(n**2 + 5) - n
        

if __name__ == "__main__":
    excercise = Exercise()
    for _ in range(10):
        print(next(excercise))