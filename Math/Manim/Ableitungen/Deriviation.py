from manimlib import *

class Deriviation(Scene):
    def construct(self):
        f = lambda x: x**3 - 3*x + 2
        x = 8
        y = 4
        deriveCcount = 2

        axes = Axes(x_range=[-x, x, x // 5 + 1], y_range=[-y, y, y // 5 + 1], height=6, width=10)

        axes.add_coordinate_labels(font_size=10, num_decimal_places=1)
        self.add(axes)

        graph = axes.get_graph(f, color=BLUE)
        self.play(ShowCreation(graph, run_time=1.5))

        def derivative(func, h=0.001):
            return lambda x: (func(x + h) - func(x)) / h

        colors = [YELLOW, GREEN, RED, ORANGE, PURPLE]  # List of colors for derivatives
        current_func = f
        for i in range(deriveCcount):
            current_func = derivative(current_func)
            graph = axes.get_graph(current_func, color=colors[i % len(colors)])
            self.play(ShowCreation(graph, run_time=1.5))
