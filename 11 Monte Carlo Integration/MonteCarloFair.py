from manim import *
import numpy as np

class MonteCarloFair(Scene):
    def construct(self):

        #STEP 1: Title and initials
        template = TexTemplate()
        title = MathTex(r"\mathbb{M}\text{onte}\ \mathbb{C}\text{arlo}\ \mathbb{M}\text{ethod}\ ", tex_template = template).to_edge(UP, buff = 0.9)
        title.set_color_by_gradient(YELLOW, GOLD_A, RED_A)
        title.scale(1.5)

        equation = MathTex(r" A = \int_{1}^{5} \ln(1+x)\, dx",font_size=42)
        equation.set_color_by_gradient(ORANGE, PURPLE_A, RED)
        equation.next_to(title, DOWN, buff = 0.5)

        box_equation = SurroundingRectangle(equation, corner_radius=0.15, buff=0.15, color=PURPLE_C, stroke_width=2).set_color_by_gradient("ORANGE")
        equation_group = VGroup(equation, box_equation)

        real_area = MathTex(rf"A_{{\text{{actual}}}} = 5.3642", font_size=33)
        real_area.set_color_by_gradient(MAROON, PURPLE_A, RED)
        real_area.next_to(equation_group, DOWN, buff=0.3)
        
        initials = Text("@theoptimath", font="Yu Gothic UI", font_size=24)
        initials.set_opacity(0.5)
        initials.set_color_by_gradient(RED, ORANGE, YELLOW)
        initials.to_edge(DOWN, buff=1)

        self.add(title, equation_group, real_area, initials)

        #STEP 2: Axes and curve
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 3, 0.5],
            x_length=6.5,
            y_length=5,
            axis_config={
                "color": WHITE,
                "include_tip":True,
                "stroke_width": 3,  
                "tip_length": 0.15,   # default ≈ 0.25; smaller = shorter arrow
                "tip_width": 0.2
            },
            x_axis_config={
                "numbers_to_include": [0, 1, 2, 3, 4, 5, 6, 7],
            },
            y_axis_config={
                "numbers_to_include": [0, 0.5, 1, 1.5, 2, 2.5],
            },
            
        ).shift(UP * 1.5, RIGHT*0.3)
        x_lbl = MathTex("x").next_to(axes.c2p(8, 0), RIGHT, buff=0.15).scale(0.9)
        y_lbl = MathTex("f(x)").next_to(axes.c2p(0, 3), UP, buff=0.15).scale(0.9)

        curve = axes.plot(
            lambda x: np.log(1 + x),
            x_range=[0, 7],
            color=BLUE_B,
            stroke_width=5,
        )
        
        curve_label = axes.get_graph_label(
            curve,
            label=MathTex(r"f(x)=\ln(1+x)"),
            x_val=7,
            direction=UR,
            buff=0.3,
        )

        self.add(axes, x_lbl, y_lbl)
        self.play(Create(curve), run_time = 1)
        self.play(FadeIn(curve_label), run_time = 1)

        #STEP 3: Area under the curve and bounding rectangle
        area = axes.get_area(curve, x_range=[1, 5], color=YELLOW, opacity=0.3)
        
        # Vertical boundary lines at x=2 and x=5 make the bounds crystal clear
        x2_line = axes.get_vertical_line(
            axes.c2p(1, np.log(1 + 1)), color=YELLOW, line_func=Line
        )
        
        x5_line = axes.get_vertical_line(
            axes.c2p(5, np.log(1 + 5)), color=YELLOW, line_func=Line
        )
        self.play(Create(x2_line), Create(x5_line), run_time=1)
        self.play(TransformFromCopy(equation_group,area), run_time=1)

        # Bounding rectangle corners in graph coordinates
        x_min, x_max = 1, 5
        y_max = np.log(1 + x_max)  # ln(6) ≈ 1.79
        
        bounding_box = Polygon(
            axes.c2p(x_min, 0),
            axes.c2p(x_max, 0),
            axes.c2p(x_max, y_max),
            axes.c2p(x_min, y_max),
            color=RED,
            stroke_width=4,
            fill_opacity=0,          # keep the inside see-through
            stroke_opacity=0.9,
        )
        
        box_label = MathTex(
            r"\text{Bounding Box}", font_size=33,color=RED).next_to(bounding_box, UP, buff=0.25)
        
        self.play(Create(bounding_box))
        self.play(Write(box_label))

        #STEP4:
        x_min, x_max = 1, 5
        y_max = np.log(1 + x_max)
        box_area = (x_max - x_min) * y_max   # ≈ 7.17

        Abox = MathTex(rf"A_{{\text{{box}}}} \approx {box_area:.2f}", font_size=39, color=ORANGE).next_to(axes, DOWN, buff=0.39)
        self.wait(1)
        self.play(TransformFromCopy(bounding_box, Abox), FadeOut(curve_label), run_time=1)

        #STEP 5
        # ============================================================
        # STEP 5: MONTE CARLO COUNTERS
        # ============================================================

        total_points = 450
        batch_size = 10

        green_tracker = ValueTracker(0)
        red_tracker = ValueTracker(0)
        total_tracker = ValueTracker(0)

        # ------------------------------------------------------------
        # 5.1: GREEN COUNTER
        # ------------------------------------------------------------
        green_label = MathTex(
            r"N_{\text{green}} =",
            font_size=39,
            color=GREEN
        )


        green_number = DecimalNumber(0,
                num_decimal_places=0,
                font_size=39,
                color=GREEN
            )
        
        green_number.add_updater(
            lambda m: m.set_value(green_tracker.get_value())
        )

        green_counter = VGroup(
            green_label,
            green_number
        ).arrange(RIGHT, buff=0.1)

        # ------------------------------------------------------------
        # 5.2: RED COUNTER
        # ------------------------------------------------------------

        red_label = MathTex(
            r"N_{\text{red}} =",
            font_size=39,
            color=RED
        )


        red_number = DecimalNumber(0,
                    num_decimal_places=0,
                    font_size=39,
                    color=RED
                )
        red_number.add_updater(
            lambda m: m.set_value(red_tracker.get_value())
        )

        red_counter = VGroup(
            red_label,
            red_number
        ).arrange(RIGHT, buff=0.1)

        counters = VGroup(
            green_counter,
            red_counter
        ).arrange(RIGHT,buff=0.9).next_to(Abox, DOWN, buff=0.35)

        self.play(Write(counters), run_time=1)

        # ============================================================
        # # STEP 6: MONTE CARLO APPROXIMATION EQUATION
        # # ============================================================
        
        approx_value = DecimalNumber(0,num_decimal_places=4,font_size=35,color=YELLOW)
        approx_value.add_updater(lambda m: m.set_value((green_tracker.get_value() /max(total_tracker.get_value(), 1))* box_area))
        
        approx_equation = MathTex(
            r"A_{\text{approx}} = "
            r"\frac{N_{\text{green}}}"
            r"{N_{\text{green}}+N_{\text{red}}}"
            r"\times A_{\text{box}} \approx",
            font_size=35
        ).set_color_by_gradient(MAROON, PURPLE_A, RED)

        
        
        approx_group = VGroup(approx_equation,
        approx_value).arrange(RIGHT, buff=0.15)
        
        approx_group.next_to(counters, DOWN, buff=0.7)
        
        self.play(FadeIn(approx_equation), FadeIn(approx_value))

        # ============================================================
        # STEP 7: MONTE CARLO RANDOM POINT GENERATION
        # ============================================================

           # Lists to store the generated points
        green_points = VGroup()
        red_points = VGroup()

        # Generate random points uniformly within the bounding box
        np.random.seed(42)  # For reproducible results

        random_x = np.random.uniform(1, 5, total_points)
        random_y = np.random.uniform(0, np.log(6), total_points)

        box_label2 = MathTex(
            r"\text{Random points fall in here}", font_size=33,color=RED).next_to(bounding_box, UP, buff=0.25)
        self.play(ReplacementTransform (box_label, box_label2), run_time = 1)
        self.wait(1)

        # Process points in batches
        for start in range(0, total_points, batch_size):

            batch_green = VGroup()
            batch_red = VGroup()

            green_count = 0
            red_count = 0

            for i in range(start, min(start + batch_size, total_points)):

                x = random_x[i]
                y = random_y[i]

                # Transform graph coordinates into scene coordinates
                point = Dot(
                    axes.c2p(x, y),
                    radius=0.035
                )

                # Classify the point
                if y <= np.log(1 + x):
                    point.set_color(GREEN)
                    batch_green.add(point)
                    green_points.add(point)
                    green_count += 1

                else:
                    point.set_color(RED)
                    batch_red.add(point)
                    red_points.add(point)
                    red_count += 1

            # Animate the current batch
            self.play(
                LaggedStart(
                    *[FadeIn(p, scale=0.5) for p in batch_green],
                    *[FadeIn(p, scale=0.5) for p in batch_red],
                    lag_ratio=0.05
                ),
                green_tracker.animate.increment_value(green_count),
                red_tracker.animate.increment_value(red_count),
                total_tracker.animate.increment_value(
                    len(batch_green) + len(batch_red)
                ),
                run_time=0.3
            )
        
        self.wait(1)
        
        final_approx = (green_tracker.get_value() / total_tracker.get_value()) * box_area
        error_value = abs(5.3642 - final_approx)
        error = MathTex(rf"\text{{Error}} = {error_value:.4f}",font_size=36, color = MAROON)
        
        box_error = SurroundingRectangle(error, corner_radius=0.15, buff=0.15, color=PURPLE_C, stroke_width=2).set_color_by_gradient("ORANGE")
        error_box = VGroup(error, box_error).next_to(approx_group, DOWN, buff = 1)


        self.play(TransformFromCopy(real_area, error_box), run_time = 1)
        

        # Ensure all updater animations finish cleanly
      



        self.wait(2)
        

