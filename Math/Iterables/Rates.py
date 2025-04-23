import math
import matplotlib.pyplot as plt
from MathIterable import MathIterable

class Rates(MathIterable):
    n = 1.0

    def calc_next(self, values: list):
        self.n *= 2
        result = (1 - 1 / self.n) ** self.n
        if result == 1:
            return None  # caused by rounding errors
        return result

if __name__ == "__main__":
    rates = Rates()
    for rate in rates:
        print(rate)

    print("Done at", rates.n, "with", rates.values[-2])

    # Plotting the convergence
    x_vals = [2 ** (i + 1) for i in range(len(rates.values))]  # n values used
    y_vals = rates.values
    target = [1 / math.e] * len(y_vals)  # reference line

    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label=r"$(1 - \frac{1}{n})^n$", marker='o')
    plt.axhline(1 / math.e, color='r', linestyle='--', label=r"$\frac{1}{e}$")
    plt.xscale('log')
    plt.xlabel("n (log scale)")
    plt.ylabel("Value")
    plt.title("Convergence of $(1 - 1/n)^n$ to $1/e$")
    plt.legend()
    plt.grid(True)
    plt.show()
