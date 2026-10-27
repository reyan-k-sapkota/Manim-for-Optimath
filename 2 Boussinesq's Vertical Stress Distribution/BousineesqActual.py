from manim import *
import numpy as np



class New_Vertical (Scene):
    def construct(self):
        
        #formula = MathTex (r"\sigma_z =\frac{3Q}{2 \pi (1+(\frac{r}{z})^2)^5/2}")
        #self.play (Create (formula), run_time = 2)
        text = Text("Boussinesq's Vertical Stress Distribution in soil along a Horizontal Plane ", font_size = 29, font = 'Bahnschrift', weight=ULTRABOLD)
        text.set_color_by_gradient(RED, ORANGE, YELLOW)
        
        self.play (Write(text), run_time = 2)

        START = (-5,0,0)
        END =   (5,0,0)
        line_d = DashedLine(START,END, color=GRAY, dash_length=0.1, dashed_ratio=0.5)
        line = Line(START,END, color = LIGHT_BROWN)
        self.play(ReplacementTransform(text, line))
        self.play(line.animate.shift(UP*2))

        ground_label = Text("Initial GL", font_size=20)
        ground_label.next_to(line, RIGHT)
        self.play(Write(ground_label))

        load_arrow = Arrow(
            start=UP * 3, 
            end=UP * 2, 
            color=RED, 
            stroke_width=6, 
            buff=0  
        )

        load_label = Text("Q", font_size=25).next_to(load_arrow, UP)
        load_label.set_color_by_gradient(RED, ORANGE, YELLOW)


        #self.play (Create (load_arrow))
        #self.play (Create(load_label))

        #group = VGroup(line, load_arrow, load_label, ground_label)
        START1= (-5, 2, 0)
        END1 = (5, 2, 0) 
        dotted_line = DashedLine(START1, END1, color=GRAY, dash_length=0.1, dashed_ratio=0.5)

        

        old_ground_label = Text("Initial GL", font_size=20)
        old_ground_label.next_to(dotted_line, RIGHT)

        new_ground_label = Text("Final GL", font_size=20)
        new_ground_label.next_to(line, LEFT)


        

        axes = Axes(
            x_range = [-5, 5, 1],
            y_range = [0, 50, 1],
            x_length=10,
            y_length=4,
            axis_config={
                "color":RED,
                "include_tip":False,
            },
            y_axis_config={"include_ticks": False}
        )

        axes.x_axis.add_labels({
            -5: '-5',
            -4: '-4',
            -3: '-3',
            -2: '-2',
            -1: '-1',
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5'
        })
        
        x_label = Text("Radial distance (m)", font_size=20)
        x_label.next_to(axes.x_axis, DOWN)

        freq = ValueTracker(1)

        def Bousinesq(x):
            P = 100*freq.get_value()
            a = 1+pow(x/2, 2)
            IB = (1.5/np.pi)*(1/pow(a,2.5))
            stress = IB*(P/4)
            return stress
        
        graph = always_redraw(lambda: axes.plot(
            lambda x: Bousinesq(x),
            color=ORANGE,
        ))

        freq_label = always_redraw(
            lambda: MathTex(f"= {100* freq.get_value():.1f} kN", font_size = 25)
            .next_to(load_label, RIGHT)
        )

        dot = always_redraw(lambda: 
            Dot(axes.c2p(0, Bousinesq(0)), color=RED)
        )

        y_value_label = always_redraw(lambda: 
            MathTex(f"\\sigma = {Bousinesq(0):.1f} kN/m^2")
            .scale(0.5)
            .next_to(dot, RIGHT, buff=0.2)
        )


        def get_shift():
            return DOWN * (0.2 * (freq.get_value() - 1))
        
        START = (-5,2,0)
        END =   (5,2,0)
        line_new = Line(START,END, color = LIGHT_BROWN)

        ground_group = VGroup(line_new, load_arrow, load_label, freq_label, new_ground_label)

        dynamic_group = always_redraw(lambda:
            ground_group.copy().shift(get_shift())
        )

        height_arrow = DoubleArrow(
            start=axes.c2p(5.5, 0),
            end=axes.c2p(5.5, 50),
            buff=0.05,
            stroke_width = 1,
            color=YELLOW,
            tip_shape=ArrowTriangleTip
        )
        height_arrow.tip.scale(0.5)
        height_arrow.start_tip.scale(0.5)

        
        height_label = MathTex("z = 2.0m").scale(0.7)
        height_label.next_to(height_arrow, RIGHT, buff=0.1)

        self.play(Create(dynamic_group), run_time = 3)
        self.play(
                  Transform (line, dotted_line),
                  Create(axes),
                  Create(x_label),
                Create(graph),
                Create(dot),
                Create(y_value_label)
            )
        self.play (Create(height_arrow), Create(height_label))
        

        self.play(freq.animate.set_value(2), run_time=4)
        self.play(freq.animate.set_value(3), run_time=5)
        self.play(freq.animate.set_value(2), run_time=4)


        


