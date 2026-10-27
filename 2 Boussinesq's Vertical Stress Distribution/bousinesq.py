from manim import *
import numpy as np

class Bousinesq (Scene):
    def construct(self):
        text = Text("Bousinessq's Vertical Stress Distribution in Horizontal Plane", font_size = 25, font = 'Yu Gothic UI')
        text.set_color_by_gradient(RED, ORANGE, YELLOW)
        self.play (Write (text), run_time = 3)
        #self.play (ShrinkToCenter(text))

        START = (-5,0,0)
        END =   (5,0,0)
        line = Line(START,END)
        self.play(ReplacementTransform(text, line))
        self.play(line.animate.shift(UP*2))

        ground_label = Text("GroundLevel", font_size=20)
        ground_label.next_to(line, RIGHT)
        self.play(Write(ground_label))

        load_arrow = Arrow(
            start=UP * 3, 
            end=UP * 2, 
            color=RED, 
            stroke_width=6,  # Thickness of the arrow
            buff=0  # No buffer, so it touches the endpoints exactly
        )

        load_label = MathTex("P").next_to(load_arrow, UP)

        self.play (Create (load_arrow))
        self.play (Create(load_label))

        #compressed_surface = line.copy().shift(DOWN * 0.2)
        group = VGroup(line, load_arrow, load_label, ground_label)
        START1= (-5, 2, 0)
        END1 = (5, 2, 0) 
        dotted_line = DashedLine(START1, END1, color=GRAY, dash_length=0.1, dashed_ratio=0.5)
        self.play(group.animate.shift(DOWN*0.3), FadeIn(dotted_line))

        #self.play(Transform(line, compressed_surface), run_time=0.5)

        new_ground_label = Text("Final GL", font_size=20)
        new_ground_label.next_to(line, RIGHT)
        self.play(ReplacementTransform(ground_label, new_ground_label))

        old_ground_label = Text("Initial GL", font_size=20)
        old_ground_label.next_to(dotted_line, RIGHT)
        self.play(Write(old_ground_label))

        #y_max = max(line.get_start()[1], line.get_end()[2])

        axes = Axes(
            x_range = [-5, 5, 1],
            y_range = [0, 50, 1],
            x_length=10,
            y_length=4,
            axis_config={
                "color":RED,
                "include_tip":False,
            }
        )
        
        x_label = axes.get_x_axis_label("x")
        
        self.play(Create(axes))
        self.play(Create(x_label))
        #self.play(Create(y_label))

        z_depth = Text("Depth, z=2m", font_size=20)
        z_depth.next_to(axes, RIGHT)
        self.play(Write(z_depth))

        freq = ValueTracker(1)
        
        def Bousinesq(x):
            P = 100*freq.get_value()
            a = 1+pow(x/2, 2)
            IB = (1.5/np.pi)*(1/pow(a,2.5))
            stress = IB*(P/4)
            return stress
        
        graph = always_redraw(lambda: axes.plot(
            lambda x: Bousinesq(x),
            color=YELLOW
        ))

        freq_label = always_redraw(
            lambda: MathTex(f"= {100* freq.get_value():.1f}")
            .next_to(load_label, RIGHT)
        )

        self.play(Create(graph))
        self.play (Create (freq_label))

        # Animate the change in frequency
        self.play(freq.animate.set_value(2), run_time=4)



        






       


        
