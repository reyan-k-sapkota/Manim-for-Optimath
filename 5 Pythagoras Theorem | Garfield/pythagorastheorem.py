from manim import *
import numpy as np

class PythagorasTheorem(Scene):
    def construct (self):
        intro = Text("Pythagoras Theorem", font_size = 51, font = "Comic Sans MS").to_edge(UP)
        intro2 = Text("Garfield's Proof", font_size = 45, font = "Comic Sans MS").next_to(intro, DOWN)
        intro.set_color_by_gradient(RED, PURPLE_A, BLUE)
        intro2.set_color_by_gradient(RED, PURPLE_A, BLUE)
        

        initials = Text("@liberative.musings", font="Yu Gothic UI", font_size=27)
        initials.set_opacity(0.4)
        initials.set_color_by_gradient(RED, ORANGE, YELLOW)
        initials.to_edge(DOWN, buff=1)

        self.add (intro, intro2, initials)

        vertices = [
            np.array([-2, -2, 0]),
            np.array([4, -2, 0]),
            np.array([-2, 2, 0]),
        ]

        triangle = Polygon(*vertices, color = ORANGE, stroke_width = 9).move_to(UP*1)
        
        #self.play (Create (triangle), run_time = 1)
        triangle.set_fill(RED, opacity=0.3)

        A, B, C = vertices

        mid_AB = (A+B)/2
        mid_BC = (B+C)/2
        mid_AC = (A+C)/2

        label_b = Tex("b", font_size = 81).move_to(mid_AB + DOWN * 0.6 + UP*1+ LEFT*1.2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        label_c = Tex("c", font_size = 81).move_to(mid_BC + UP*1.25).set_color_by_gradient(RED, PURPLE_A, BLUE)
        label_a = Tex("a", font_size = 81).move_to(mid_AC + LEFT * 1.5+ UP*1).set_color_by_gradient(RED, PURPLE_A, BLUE)

        triangle_group = VGroup (triangle, label_a, label_b, label_c)

        #self.play(Write(label_a), Write(label_b), Write(label_c))
        self.add(triangle_group.shift(RIGHT*0.5))

        a_squared = MathTex ("a^2", font_size = 75).move_to(DOWN * 3 + LEFT*1.5).set_color_by_gradient(RED, PURPLE_A, BLUE)
        plus = MathTex("+", font_size = 75).next_to(a_squared, RIGHT, buff=0.2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        b_squared = MathTex ("b^2", font_size = 75).next_to(plus, RIGHT, buff=0.2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        equal = MathTex("=", font_size = 75).next_to(b_squared, RIGHT, buff=0.2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        c_squared = MathTex ("c^2", font_size = 75).next_to(equal, RIGHT, buff=0.2).set_color_by_gradient(RED, PURPLE_A, BLUE)

        group = VGroup (a_squared, plus, b_squared, equal, c_squared)


        self.play (TransformFromCopy(label_a, a_squared), Write (plus), run_time = 0.7)
        self.play (TransformFromCopy(label_b, b_squared), Write (equal), run_time = 0.7)
        self.play (TransformFromCopy(label_c, c_squared), run_time = 0.7)

        question = Text ("Proof?", font_size = 51, color = RED).move_to(DOWN*4.5).set_color_by_gradient(RED, PURPLE_A, BLUE)
        self.play (Write(question))
        
        self.play (FadeOut (group), FadeOut (question))

        self.play(triangle_group.animate.shift(DOWN * 3).scale(0.7), run_time=2)

        new_triangle = triangle_group.copy()
        self.play(new_triangle.animate.rotate(270*DEGREES).shift(UP*4.10+LEFT*0.77), run_time=2)

        vertex_initial  = triangle_group[0].get_vertices()
        vertex_final = new_triangle[0].get_vertices()

        connector_line = Line(
            vertex_initial[1],  # third point of original
            vertex_final[2],   # second point of rotated
            color=WHITE, 
            stroke_width = 9,
        )
        print("Original vertex C:", vertex_initial[2])
        print("Rotated vertex B:", vertex_final[2])

        self.play(Create(connector_line), run_time = 1)
        #self.wait()

        vertices_new = [
            vertex_initial[1],  
            vertex_final[2],
            vertex_final[1]
        ]

        area = Polygon(*vertices_new, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)

        self.play(Create(area), run_time = 1.5)

        all_three_triangles = VGroup (triangle_group, new_triangle, connector_line, area)

        self.play(all_three_triangles.animate.scale(0.9).shift(UP*2), run_time = 1)


        vertex_triangle_old_new  = triangle_group[0].get_vertices()
        vertex_triangle_new_new = new_triangle[0].get_vertices()

        vertices_for_trapezoidal_area = [
            vertex_triangle_old_new[0], 
            vertex_triangle_old_new[1], 
            vertex_triangle_new_new[2],
            vertex_triangle_new_new[0]
        ]

        vertices_for_triangle1_area = [
            vertex_triangle_old_new[0], 
            vertex_triangle_old_new[1], 
            vertex_triangle_old_new[2], 
        ]

        vertices_for_triangle2_area = [
            vertex_triangle_new_new[0], 
            vertex_triangle_new_new[1], 
            vertex_triangle_new_new[2], 
        ]

        vertices_for_triangle3_area = [
            vertex_triangle_old_new[1],  
            vertex_triangle_new_new[2],
            vertex_triangle_new_new[1]
        ]

        trapezoidal_area = Polygon(*vertices_for_trapezoidal_area, fill_color=BLUE, fill_opacity=0.6, stroke_width = 0)
        
        self.play (Create(trapezoidal_area), run_time = 1)
        self.wait(0.6)

        
        trapezoidal_area_mini_copy = trapezoidal_area.copy().scale(0.2).shift(DOWN*5+LEFT*2.5)
        equals_sign = Text ("=").next_to(trapezoidal_area_mini_copy)

        self.play(ReplacementTransform(trapezoidal_area, trapezoidal_area_mini_copy), Write (equals_sign))


        triangle_1_area_new = Polygon(*vertices_for_triangle1_area, fill_color=ORANGE, fill_opacity=0.6, stroke_width = 0)
        triangle_1_area_new_copy = triangle_1_area_new.copy().scale(0.2).next_to(equals_sign)

        plus_sign1 = Text ("+").next_to(triangle_1_area_new_copy)

        triangle_2_area_new = Polygon(*vertices_for_triangle2_area, fill_color=ORANGE, fill_opacity=0.6, stroke_width = 0)
        triangle_2_area_new_copy = triangle_2_area_new.copy().scale(0.2).next_to(plus_sign1)
        
        plus_sign2 = Text ("+").next_to(triangle_2_area_new_copy)

        triangle_3_area_new = Polygon(*vertices_for_triangle3_area, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)
        triangle_3_area_new_copy = triangle_3_area_new.copy().scale(0.2).next_to(plus_sign2)

        self.play(ClockwiseTransform(triangle_1_area_new, triangle_1_area_new_copy), Write(plus_sign1))
        self.play(CounterclockwiseTransform(triangle_2_area_new, triangle_2_area_new_copy), Write(plus_sign2))
        self.play(ReplacementTransform(triangle_3_area_new, triangle_3_area_new_copy))




        area_exp_trap = MathTex(r"(a + b) \cdot \frac{a + b}{2}").shift(DOWN*5+LEFT*2.5).set_color_by_gradient(RED, PURPLE_A, BLUE)
        
        equals_sign1 = Text ("=").next_to(area_exp_trap).set_color_by_gradient(RED, PURPLE_A, BLUE)
        
        trapezoidal_area_dim = Polygon(*vertices_for_trapezoidal_area, fill_color=BLUE, fill_opacity=0.6, stroke_width = 0)
        self.play(TransformFromCopy(trapezoidal_area_mini_copy, trapezoidal_area_dim))
        self.play(ReplacementTransform(trapezoidal_area_dim, area_exp_trap), Create(equals_sign1))

        area_exp_triangle1 = MathTex(r"\frac{a \cdot b}{2}").next_to(equals_sign1).set_color_by_gradient(RED, PURPLE_A, BLUE)
        plus_sign_new = Text ("+").next_to(area_exp_triangle1).set_color_by_gradient(RED, PURPLE_A, BLUE)
        triangle_1_area_dim = Polygon(*vertices_for_triangle1_area, fill_color=BLUE, fill_opacity=0.6, stroke_width = 0)
        self.play(TransformFromCopy(triangle_1_area_new_copy, triangle_1_area_dim))
        self.play(ReplacementTransform(triangle_1_area_dim, area_exp_triangle1), Create(plus_sign_new))

        
        area_exp_triangle2 = MathTex(r"\frac{a \cdot b}{2}").next_to(plus_sign_new).set_color_by_gradient(RED, PURPLE_A, BLUE)
        plus_sign_new1 = Text ("+").next_to(area_exp_triangle2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        triangle_2_area_dim = Polygon(*vertices_for_triangle2_area, fill_color=BLUE, fill_opacity=0.6, stroke_width = 0)
        self.play(TransformFromCopy(triangle_2_area_new_copy, triangle_2_area_dim))        
        self.play(ReplacementTransform(triangle_2_area_dim, area_exp_triangle2), Create(plus_sign_new1))

        area_exp_triangle3 = MathTex(r"\frac{c \cdot c}{2}").next_to(plus_sign_new1).set_color_by_gradient(RED, PURPLE_A, BLUE)
        triangle_3_area_dim = Polygon(*vertices_for_triangle3_area, fill_color=BLUE, fill_opacity=0.6, stroke_width = 0)
        self.play(TransformFromCopy(triangle_3_area_new_copy, triangle_3_area_dim)) 
        self.play(ReplacementTransform(triangle_3_area_dim, area_exp_triangle3))

        
        area_exp_trap_1 = MathTex(r"\frac{(a + b)^2}{2}").shift(DOWN*5+LEFT*2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        area_exp_triangle12_1 = MathTex(r"a \cdot b").next_to(equals_sign1).set_color_by_gradient(RED, PURPLE_A, BLUE)
        area_exp_triangle3_1 = MathTex(r"\frac {c^2}{2}").next_to(plus_sign_new1).set_color_by_gradient(RED, PURPLE_A, BLUE)

        self.play(ReplacementTransform(area_exp_trap, area_exp_trap_1))
        group_steps = VGroup (area_exp_triangle1, plus_sign_new, area_exp_triangle2)
        self.play(ReplacementTransform(group_steps, area_exp_triangle12_1))
        self.play(ReplacementTransform(area_exp_triangle3, area_exp_triangle3_1))
        self.play( plus_sign_new1.animate.shift(LEFT*1.5), area_exp_triangle3_1.animate.shift(LEFT*1.5))

        area_exp_trap_2 = MathTex(r"\frac{a^2 + 2ab + b^2}{2}").shift(DOWN*5+LEFT*2.25).set_color_by_gradient(RED, PURPLE_A, BLUE)
        self.play(ReplacementTransform(area_exp_trap_1, area_exp_trap_2))

        area_exp_trap_3 = MathTex (r"\frac{a^2}{2} + ab + \frac{b^2}{2}").shift(DOWN*5+LEFT*2.25).set_color_by_gradient(RED, PURPLE_A, BLUE)
        self.play(ReplacementTransform(area_exp_trap_2, area_exp_trap_3))

        area_exp_trap_4 = MathTex(r"\frac{a^2}{2} + \frac{b^2}{2}").shift(DOWN*5+ LEFT*1).set_color_by_gradient(RED, PURPLE_A, BLUE)
        self.wait(0.75)
        equals_sign1.shift(RIGHT*1)
        area_exp_second_last = MathTex(r"\frac {c^2}{2}").next_to(equals_sign1).set_color_by_gradient(RED, PURPLE_A, BLUE)
        
        steps_group = VGroup (area_exp_triangle12_1, area_exp_triangle3_1, plus_sign_new1)
        
        
        self.play(ReplacementTransform(area_exp_trap_3, area_exp_trap_4), ReplacementTransform(steps_group, area_exp_second_last))
        
        
        

        final_conclusion = MathTex(r"a^2 + b^2 = c^2").shift(DOWN*5).set_color_by_gradient(RED, PURPLE_A, BLUE)
        final_steps_group = VGroup (area_exp_trap_4, equals_sign1, area_exp_second_last)
        self.wait(0.75)
        self.play(ReplacementTransform(final_steps_group, final_conclusion))

        box = SurroundingRectangle(final_conclusion, buff=0.2).set_color_by_gradient(PURPLE_A)
        proved = Tex ("Proved").next_to(final_conclusion).shift(DOWN*1).set_color_by_gradient(RED, PURPLE_A, BLUE)

        self.play(Create(box), run_time = 1)
        self.play(Write (proved), run_time = 1)

        
        

        
        #self.play(TransformFromCopy(triangle_1_area_new_copy, triangle_1_area_new_dim))

        



        
        

        
        self.wait()
        




        
        


        
        
        