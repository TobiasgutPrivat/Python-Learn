from manimlib import *

class Curves(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 10],
            y_range=[-2, 2, 0.5],
            width=10,
            height=6,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            y_axis_config={
                "include_tip": False,
            }
        )

        axes.add_coordinate_labels(
            font_size=10,
            num_decimal_places=1,
        )
        self.add(axes)

        # Create a dot
        dot = Dot(color=BLUE)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))

        # Create horizontal and vertical lines that are always redrawn
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        # Show the lines
        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )

        # Move the dot
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()

        # Keep dot at (1, 1) while scaling the axes
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.75).to_corner(UL),
            run_time=2,
        )
        self.wait()

        # Fade out everything
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))
