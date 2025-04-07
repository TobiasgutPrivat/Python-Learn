from MathIterable import MathIterable

class Factorial(MathIterable):
    def calc_next(self, values):
        if len(values) == 0:
            return 1
        return values[-1] * (len(values) + 1)
    
if __name__ == "__main__":
    fak = Factorial()
    for _ in range(10):
        print(next(fak))