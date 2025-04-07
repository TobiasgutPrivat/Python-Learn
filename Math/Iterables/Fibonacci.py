from MathIterable import MathIterable

class Fibonacci(MathIterable):
    def calc_next(self, values):
        if len(values) < 2:
            return 1
        return values[-1] + values[-2]

if __name__ == "__main__":
    fib = Fibonacci()
    for _ in range(10):
        print(next(fib))

