from manim import *

class Reinmann_Sum(Scene):
    def construct(self):
        text = Text('Reimann Sums', gradient=(RED, ORANGE))
        self.play (Write(text), run_time = 2)

        integral = MathTex(r"\int_{\pi/3}^{\pi} sin(x) \, dx = 1.5", font_size = 30 )
        integral.set_color_by_gradient(RED, ORANGE)
        
        self.play (ReplacementTransform(text, integral))
        
        self.play (integral.animate.shift(UP*3))
        #self.play (integral.animate.shift(LEFT*5))
        text2 = Text('a. Finding area by Reimann Rectangle Sum Method', gradient = (RED, ORANGE), font_size =25)
        text3 = Text('Notice how the value of area converges on increasing the number of reinmann rectangles', gradient = (RED, ORANGE), font_size =25)
        
        
    
        self.play (Write (text2), run_time = 2)
        self.play (text2.animate.shift(UP*2))
        
        self.play (Write (text3), run_time = 2)

        self.play (Transform(text2, integral))
        self.play (Transform (text3, integral))
        
        

        
        #step_1 = MathTex(r"= \left[ -cos(x) \right]_{\pi/3}^{\pi}")
        #step_1.set_color_by_gradient(RED, ORANGE)
        #step_1.next_to(integral, RIGHT)
        #self.play(Write(step_1))
        

        #step_2 = MathTex (r"= -[cos({\pi})-cos({\pi/3})]")
        #step_2.set_color_by_gradient(RED, ORANGE)
        #step_2.next_to(step_1, RIGHT)
        #self.play(Write(step_2))
        

        
        #step_3 = MathTex (r"= -[-1-1/2]")
        #step_3.set_color_by_gradient(RED, ORANGE)
        #step_3.next_to(step_2, DOWN)
        #self.play(Write(step_3))
        

        
        #step_4 = MathTex (r"= 3/2")
        #step_4.set_color_by_gradient(RED, ORANGE)
        #step_4.next_to(step_3, DOWN)
        #self.play(Write(step_4))
        #self.wait(1)

        #target_answer = step_4
        #target_answer.next_to(integral, RIGHT, buff=0.2)

        # Step 4: Animate moving answer into place
        #self.play(Transform(step_4, target_answer, path_arc=PI / 2))
        #self.wait(2)

        #all_steps = VGroup(integral, step_1, step_2, step_3)


        #self.play(ShrinkToCenter(all_steps))

        
        axes = Axes( 
            x_range=[0, 4 * PI, PI],  # Covers the interval from 0 to 4\pi
            y_range=[-1.5, 1.5, 0.5],
            axis_config = {"color":BLUE},
            tips= True
        ).add_coordinates()
        
        axes. get_axis_labels(x_label = "x", y_label = "f(x)")

        axes.x_axis.numbers.set_opacity(0)
        axes.x_axis.ticks.set_opacity(0)


        axes.x_axis.add_labels({
            0: MathTex("0"),
            PI: MathTex(r"\pi"),
            2 * PI: MathTex(r"2\pi"),
            3 * PI: MathTex(r"3\pi"),
            4 * PI: MathTex(r"4\pi")
        })

        axes.set_color([RED, ORANGE])


        def func(x):
            return np.sin(x)
        

        sin_curve = axes.plot(func, color=BLUE)
        
        self.play (DrawBorderThenFill(axes))
        self.play(Create(sin_curve.set_color ([RED, BLUE])), run_time = 3)
        summation = MathTex(r"\sum_{i=1}^{n} sin(x) \, \Delta x", font_size = 30).to_edge(DOWN)
        integral.set_color_by_gradient(RED, ORANGE)
        self.play(Write (summation))

        area = axes.get_area(
            sin_curve,
            x_range=(PI/3, PI),
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )
        
        area.set_color_by_gradient(RED, ORANGE)

        rects = axes.get_riemann_rectangles(
            sin_curve,
            x_range=[PI/3, PI],
            dx=0.3,
            color=(TEAL, BLUE_B),
            input_sample_type="right",
        )

        

        self.play (Create (area))
        self.play (Create(rects))

        num_rectangles = len(rects)
        area_value = Text(f"Area", gradient = [RED, ORANGE], font_size = 30).to_edge(UR)

        rect_count_text = Text(f"Number of Rectangles: {num_rectangles}", gradient = [RED, ORANGE], font_size = 20).to_edge (UR)
        self.play (Create(rect_count_text))
        #self.play (Create(rect_count_text))

        for new_dx in [0.3, 0.2, 0.1, 0.05, 0.025]:
            new_rectangles = axes.get_riemann_rectangles(
                sin_curve,
                x_range=[PI/3, PI],
                dx=new_dx,
                stroke_width=0.25,
                fill_opacity=0.75,
                color=(PURPLE, ORANGE)
            )
            
            num_rectangles1 = len(new_rectangles)
            sum_of_areas = sum(func(PI/3 + i * new_dx) * new_dx for i in range(num_rectangles1))
            #area_text = MathTex(f"\\text{{Sum of Areas}} \\approx {sum_of_areas:.2f}", font_size = 25).to_edge(UR)
            ans = MathTex(f"= {sum_of_areas:.2f}", font_size = 25).next_to(summation, RIGHT)
            integral.set_color_by_gradient(RED, ORANGE)
            
            rect_count_text1 = Text(f"Number of Rectangles: {num_rectangles1}", gradient = [RED, ORANGE], font_size = 20).to_edge(UR)
            self.play(Transform(rects, new_rectangles))
            self.play(Transform(rect_count_text, rect_count_text1))
            self.play(Transform(area_value, ans))
            self.wait(1)
        
       