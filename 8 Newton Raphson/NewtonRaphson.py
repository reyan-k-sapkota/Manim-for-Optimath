from manim import *
import math

class NewtonRaphson(MovingCameraScene):
    def construct (self):
        template = TexTemplate()
        
        title = MathTex(r"\mathbb{N}\text{ewton}\ \mathbb{R}\text{aphson}\ \mathbb{M}\text{ethod}\ ", tex_template = template).to_edge(UP, buff = 1.5)
        title.set_color_by_gradient(YELLOW, GOLD_A, RED_A)
        title.scale(1.2)
        
        initials = Text("@liberative.musings", font="Yu Gothic UI", font_size=27)
        initials.set_opacity(0.4)
        initials.set_color_by_gradient(RED, ORANGE, YELLOW)
        initials.to_edge(DOWN, buff=1)

        equation = MathTex(r"f(x)={x^2-4x}",font_size=36)
        equation.set_color_by_gradient(ORANGE, PURPLE_A, RED)
        equation.next_to(title, DOWN)

        real_root = MathTex(r"\text{Actual Non-Zero Root, } x=4 ", font_size=33)
        real_root.set_color_by_gradient(MAROON, PURPLE_A, RED)
        real_root.next_to(equation, DOWN, buff=0.3)
        box_real_root = SurroundingRectangle(real_root, corner_radius=0.15, buff=0.15, color=PURPLE_C, stroke_width=2).set_color_by_gradient("ORANGE")
        real_root_group = VGroup(real_root, box_real_root)

        self.add (title, initials, equation, real_root, box_real_root)

        def f(x):
            return x**2 - 4*x 

        def df(x):
            return 2*x - 4
        
        #Defining Axes
        axes = Axes(
            x_range = [-2, 9, 1],
            y_range = [-5, 14, 1],
            x_length=7.2,
            y_length=7.2,
            axis_config={
                "color":BLUE,
                "include_tip":True,
                "stroke_width": 3,  
                "tip_length": 0.15,   # default ≈ 0.25; smaller = shorter arrow
                "tip_width": 0.2

            },
            x_axis_config={
                "include_ticks": False,
                "include_numbers": True,
                "font_size": 24, 
                
            },
            y_axis_config={
                "include_ticks": False,
                "include_numbers": True,
                "font_size":24,
                
            }
        )
        axes.x_axis.add_tip(at_start=True)
        axes.y_axis.add_tip(at_start=True)

        x_lbl = MathTex("x").next_to(axes.c2p(9, 0), RIGHT, buff=0.15).scale(0.75)
        y_lbl = MathTex("f(x)").next_to(axes.c2p(0, 14), UP, buff=0.15).scale(0.75)
        
        graph = axes.plot(
            f,
            x_range=[-2, 6.3],
            color="#FF0000",
            stroke_width=3.6,
            use_smoothing=False
        )

        self.add(axes, x_lbl, y_lbl, graph)
        self.wait(0.5)

        root_dot = Dot(axes.c2p(4, 0), color=BLUE, radius=0.09)
        self.play(ReplacementTransform(real_root.copy(), root_dot), run_time = 1.5)
        

        #Initial Guess
        x0 = 6

        step1_text = MathTex(r"\text{Initial Guess}").scale(0.6).set_color_by_gradient(ORANGE, YELLOW, RED)
        step1_value = MathTex(r"x_0 = 6").scale(0.6).set_color_by_gradient(ORANGE, YELLOW, RED)
        step1 = VGroup(step1_text, step1_value).arrange(DOWN).shift(UP*2.5)
        step1_value_box = SurroundingRectangle(step1, corner_radius=0.15, buff=0.15, color="#00FFFF", stroke_width=2)
        
        self.play (Create(step1), Create(step1_value_box), run_time = 1)
        self.wait(0.72)

        step1_total = VGroup(step1, step1_value_box)

        initialguess_dot = Dot(axes.c2p(x0, 0), color=ORANGE, radius=0.07)
        self.play(Transform(step1_total, initialguess_dot))
        self.wait(0.72)


        #Iteration 1
        xs = [x0]
        for _ in range(3):
            x0 = x0 - f(x0) / df(x0)
            xs.append(x0)
        
        # Scene coordinates
        x_n = xs[0]
        x_next = xs[1]

        # Coordinates (these are numpy arrays, not Mobjects)
        pt_xn    = axes.c2p(x_n, 0)           # point on x-axis
        pt_curve = axes.c2p(x_n, f(x_n))      # point on curve
        pt_next  = axes.c2p(x_next, 0)        # next guess on x-axis
        
        # Mobjects (these are the visual dots)
        dot_x     = Dot(pt_xn,    color=RED, radius=0.08)
        dot_curve = Dot(pt_curve, color=ORANGE, radius=0.08)
        dot_next  = Dot(pt_next,  color=PINK, radius=0.08)


        # Dashed line uses the COORDINATES
        v_line = DashedLine(pt_xn, pt_curve, color=YELLOW, stroke_width=1.5)

        self.play(
            Create(v_line),
            FadeIn(dot_curve),            
            run_time=0.9
        )
        self.wait(0.72)

        # Tangent line 
        slope = df(x_n)
        dx = abs(x_n - x_next)
        tan_p1 = axes.c2p(x_n - dx, f(x_n) - slope * dx)
        tan_p2 = axes.c2p(x_n + dx * 0.18, f(x_n) + slope * dx * 0.18)
        tangent = Line(tan_p1, tan_p2, color=YELLOW, stroke_width=1.5)

        tangent_point_text = MathTex(r"(6, 12)", font_size = 27,color=ORANGE).next_to(dot_curve, RIGHT, buff=0.15)
        tangent_text = MathTex(r"\text{Draw a tangent at } (6, 12)", font_size = 27, color=GOLD_C).next_to(dot_curve, LEFT, buff=0.15)

        self.play(Write(tangent_point_text), run_time=0.9)
        self.play(Write(tangent_text), run_time=0.9)
        self.play(Create(tangent), run_time=1.3)       
        self.play(FadeOut(tangent_text), FadeOut(tangent_point_text), run_time=0.6)

        #Next guess (tangent meets x-axis) 
        dot_next = Dot(pt_next, color=PINK, radius=0.08)
        x1_var = MathTex(f"x_{1}", color="#00FFFF")
        x1_val = MathTex(f"= {x_next:.4f}", color="#00FFFF")
        x1 = VGroup(x1_var, x1_val).arrange(RIGHT, buff=0.05).shift(UP*2.5).scale(0.6)
        
        self.play(
            FadeIn(dot_next),
            run_time=0.9
        )

        self.play (ReplacementTransform(dot_next.copy(), x1), run_time = 1.2)
        self.wait(0.72)


        #Changing Axes and Graph for better visibility
        axes1 = Axes(
            x_range = [-2, 9, 1],
            y_range = [-5, 14, 1],
            x_length=7.2,
            y_length=7.2,
            axis_config={
                "color":BLUE,
                "include_tip":True,
                "include_numbers": True,
                "stroke_width": 3,  
                "tip_length": 0.15,   # default ≈ 0.25; smaller = shorter arrow
                "tip_width": 0.2

            },
            x_axis_config={
                "include_ticks": False,
                "font_size": 18, 
                
            },
            y_axis_config={
                "include_ticks": False,
                "font_size":18,
            }
        )
        
        axes1.x_axis.add_tip(at_start=True)
        axes1.y_axis.add_tip(at_start=True)

        graph1 = axes1.plot(
            f,
            x_range=[-2, 6.3],
            color="#FF0000",
            stroke_width=2.7
        )
        
        self.camera.frame.save_state()
        
        #root_dot.scale(0.7)
        root_dot1 = Dot(axes1.c2p(4, 0), color=BLUE, radius=0.06)
        
        #initialguess_dot.scale(0.7)
        initialguess_dot1 = Dot(axes1.c2p(6, 0), color=ORANGE, radius=0.06)
        
        pt_next1  = axes1.c2p(x_next, 0)
        dot_next1 = Dot(pt_next1, color=PINK, radius=0.06)
        #dot_next.scale(0.7)

        #self.play(self.camera.frame.animate.scale(0.6).move_to(axes.c2p(x_next, 2)), run_time = 1)
        
        self.play(self.camera.frame.animate.scale(0.3).move_to(axes.c2p(4.05, 2)), run_time = 1)
        
        root_dot_last = Dot(axes1.c2p(4, 0), color=BLUE, radius=0.03)
        self.play(ReplacementTransform(axes, axes1),
            ReplacementTransform(graph, graph1), 
            ReplacementTransform(root_dot, root_dot1),
            ReplacementTransform(initialguess_dot, initialguess_dot1),
            ReplacementTransform(dot_next, dot_next1), 
            ReplacementTransform(root_dot1, root_dot_last),            
            run_time=1)
        

        #Next iteration

        # Scene coordinates
        x_n = xs[1]
        x_next = xs[2]

        # Coordinates (these are numpy arrays, not Mobjects)
        pt_xn2    = axes1.c2p(x_n, 0)           # point on x-axis
        pt_curve2 = axes1.c2p(x_n, f(x_n))      # point on curve
        pt_next2  = axes1.c2p(x_next, 0)        # next guess on x-axis
        
        # Mobjects (these are the visual dots)
        dot_x2     = Dot(pt_xn2,    color=RED, radius=0.06)
        dot_curve2 = Dot(pt_curve2, color=ORANGE, radius=0.06)
        dot_next2  = Dot(pt_next2,  color=PINK, radius=0.06)


        # Dashed line uses the COORDINATES
        v_line2 = DashedLine(pt_xn2, pt_curve2, color=YELLOW, stroke_width=1.5)

        self.play(
            Create(v_line2),
            FadeIn(dot_curve2),            
            run_time=0.9
        )
        self.wait(0.72)


        
        # Tangent line 
        slope = df(x_n)
        dx = abs(x_n - x_next)
        tan_p1 = axes1.c2p(x_n - dx, f(x_n) - slope * dx)
        tan_p2 = axes1.c2p(x_n + dx * 0.18, f(x_n) + slope * dx * 0.18)
        tangent = Line(tan_p1, tan_p2, color=YELLOW, stroke_width=1.5)

        self.play(Create(tangent), run_time=1.3)

        #Next guess (tangent meets x-axis) 
        dot_next2 = Dot(pt_next2, color=PINK, radius=0.03)
        x2_var = MathTex(f"x_{2}", color=RED)
        x2_val = MathTex(f"= {x_next:.4f}", color=RED)
        x2 = VGroup(x2_var, x2_val).arrange(RIGHT, buff=0.05).shift(UP*2).scale(0.6)
        
        self.play(
            FadeIn(dot_next2),
            run_time=0.9
        )

        self.play (ReplacementTransform(dot_next2.copy(), x2), Restore(self.camera.frame), run_time = 1)
        self.wait(0.72)

        error_text = MathTex(r"\text{Error} = 0.05", font_size=30).set_color_by_gradient(ORANGE, YELLOW, RED)
        error_box = SurroundingRectangle(error_text, corner_radius=0.15, buff=0.15, color="#00FFFF", stroke_width=2)
        error = VGroup(error_text, error_box).shift(UP*1.5)

        self.play(
            ReplacementTransform(x2.copy(), real_root_group), run_time = 1)
        
        self.play(
            ReplacementTransform (real_root_group.copy(), error), run_time = 1)
        
        self.wait(0.72)
        
        msg_text = MathTex(r"\text{Continue similarly for better approximation} ", font_size=33).set_color_by_gradient(ORANGE, YELLOW, RED)
        msg_box = SurroundingRectangle(msg_text, corner_radius=0.15, buff=0.15, color=YELLOW, stroke_width=2)
        msg= VGroup(msg_text, msg_box).shift(DOWN*4.5)

        values_group = VGroup(x1, x2, error)

        self.play(
            ReplacementTransform(values_group, msg), run_time = 1.5
        )

        self.wait(2)

        
