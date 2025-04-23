from MathIterable import MathIterable

class Rates(MathIterable):
    n = 1.0

    def calc_next(self, values: list):
        self.n *= 2
        result = (1-1/self.n)**self.n
        if result == 1:
            return None # this is caused by rounding errors
        return result

if __name__ == "__main__":
    rates = Rates()
    for rate in rates:
        print(rate)

    print("Done at", rates.n,"with", rates.values[-2])