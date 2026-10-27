from manim import *
import numpy as np
import math

# Configure aspect ratio (9:16)
config.frame_width = 9  # Width in Manim units
config.frame_height = 16  # Height in Manim units

# Set output resolution (e.g., 1080x1920 pixels)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60

class VerticalPlane(Scene):
    def construct (self):
        #words = Text ("Manim first test text")
        #self.play (Write (words))

        

        axes = Axes(
            x_range = [0, 15, 0.5],
            y_range = [0, 0.5, 0.05],
            x_length=7,
            y_length=5,
            axis_config={
                "color":RED,
                "include_tip":True,
                "stroke_width": 5,  # Thicker axes

            },
            x_axis_config={
                "include_ticks": False,
            },
            y_axis_config={
                "include_ticks": False, 
                "include_tip":True,
                "stroke_width":5
            }
        )
        x_label = Text("x").set_color(ORANGE).scale(1.1)
        y_label = Text("P(X)").set_color(ORANGE).scale(1.1)
        labels = axes.get_axis_labels(x_label, y_label)

        text = Text ("Poisson's Distribution", font_size = 51, font = "Comic Sans MS")
        text.set_color_by_gradient(RED, PURPLE_C, BLUE)

        initials = Text("@liberative.musings", font="Yu Gothic UI", font_size=36)
        initials.set_opacity(0.4)
        initials.set_color_by_gradient(RED, ORANGE, YELLOW)
        initials.to_edge(DOWN, buff=1)

        equation = MathTex(r"\mathbf{P(X = x) = \frac{e^{-\lambda} \lambda^{x}}{x!}}", font_size = 66 )
        equation.set_color_by_gradient(RED, PURPLE_C, BLUE)
        equation.next_to(axes, UP, buff=2)

        text.next_to(equation, UP, buff = 0.5)

        self.add (equation, axes, labels, text, initials)

        mean = ValueTracker(1)

        def func(x, m):
            a = np.exp(-m)
            b = math.pow(m, x)
            c = math.factorial(int(x))
            y = a*b/c
            return y
        
        def func2(x):
            return np.cos(x)
        
        def get_points():
            f = mean.get_value()
            return [axes.c2p(x, func(x, f)) for x in range(15)]
            

        # Curve that redraws based on current mean
        curve = always_redraw(lambda:
            VMobject(color=PURPLE).set_points_smoothly(get_points()).set_stroke(width=9)
        )

        # Dots that redraw based on current mean
        dots = always_redraw(lambda:
            VGroup(*[Dot(point=p, radius=0.04, color=WHITE) for p in get_points()])
        )

        last_displayed_value = [None]  # store last displayed to avoid flicker
        def get_label_text():
            val = mean.get_value()
            # Round to nearest 0.2
            rounded_val = round(val * 5) / 5  # 1/0.2 = 5
            # Only update if different to avoid excessive redraws
            if rounded_val != last_displayed_value[0]:
                last_displayed_value[0] = rounded_val
            return f"Mean (\\lambda) = {rounded_val:.1f}"

        mean_label = always_redraw(lambda:
           MathTex(f"\\mathbf{{{get_label_text()}}}", font_size = 51).next_to(axes, DOWN*6).set_color_by_gradient(RED, PURPLE, BLUE)
        )

       

        self.add(curve, dots, mean_label)

        #self.wait(1)

        # Animate mean from 1 to 10 in steps of 1
        for val in range(2, 15):
            self.play(mean.animate.set_value(val), run_time=1)
            self.wait(0.3)

        self.wait(2)
        
        #m = 2
        #points = [
        #    axes.c2p(x, func(x, m))
        #    for x in range(10)
        #]

        # Create a smooth curve through the points
        #curve = VMobject(color=ORANGE)
        #curve.set_points_smoothly(points)

        # Optionally add dots to show actual discrete points
        #dots = VGroup(*[Dot(point=p, radius=0.04, color=WHITE) for p in points])

        #self.play(Create(curve), FadeIn(dots))
        #self.wait(2)






