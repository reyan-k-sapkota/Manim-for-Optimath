from manim import *

class PythagorasTheoremEinstein(Scene):
    def construct(self):
        #text = Text("Integration Bee")
        #self.play(Write (text))

        intro = Text("Pythagoras Theorem", font_size = 51, font = "Comic Sans MS").to_edge(UP)
        intro2 = Text("Einstein's Proof", font_size = 45, font = "Comic Sans MS").next_to(intro, DOWN)
        intro.set_color_by_gradient(RED, PURPLE_A, BLUE)
        intro2.set_color_by_gradient(RED, PURPLE_A, BLUE)

        initials = Text("@liberative.musings", font="Yu Gothic UI", font_size=27)
        initials.set_opacity(0.4)
        initials.set_color_by_gradient(RED, ORANGE, YELLOW)
        initials.to_edge(DOWN, buff=1)

        self.add (intro, intro2, initials)

        vertices = [
            np.array([-2, 0, 0]),
            np.array([3, 0, 0]),
            np.array([-2, 4, 0]),
        ]

        triangle = Polygon(*vertices, color = PURPLE_C, stroke_width = 9)

        triangle.set_fill(DARK_BLUE, opacity=0.3)

        A, B, C = vertices

        line_AC = Polygon (C, A, color = PURPLE_C)
        line_BC = Polygon (A, B, color = PURPLE_C)
        line_AB = Polygon (C, B, color = PURPLE_C)
        

        mid_AB = (A+B)/2
        mid_BC = (B+C)/2
        mid_AC = (A+C)/2

        #label_a = Text("a", font_size = 51).move_to(mid_AB+ DOWN * 0.6 + LEFT*0.3 ).set_color_by_gradient(RED, PURPLE_A, BLUE)
        #label_c = Text("c", font_size = 51).move_to(mid_BC + RIGHT*0.9).set_color_by_gradient(RED, PURPLE_A, BLUE)
        #label_b = Text("b", font_size = 51).move_to(mid_AC + LEFT*0.7).set_color_by_gradient(RED, PURPLE_A, BLUE)

        label_A = Text("A", font_size = 51, color = BLUE_C).move_to(C + UP*0.5)
        label_C = Text("C", font_size = 51, color = BLUE_C).move_to(A + LEFT*0.5)
        label_B = Text("B", font_size = 51, color = BLUE_C).move_to(B + RIGHT*0.5)

        triangle_group = VGroup (triangle, line_AC, line_BC, line_AB, label_A, label_B, label_C)

        self.add(triangle_group)

        #plus, RIGHT, buff=0.2

        b_squared = MathTex ("AC^2", font_size = 63).move_to(DOWN * 2 + LEFT*2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        plus = MathTex("+", font_size = 63).next_to(b_squared, RIGHT, buff=0.2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        a_squared = MathTex ("BC^2", font_size = 63).next_to(plus, RIGHT, buff=0.2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        equal = MathTex("=", font_size = 63).next_to(a_squared, RIGHT, buff=0.2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        c_squared = MathTex ("AB^2", font_size = 63).next_to(equal, RIGHT, buff=0.2).set_color_by_gradient(RED, PURPLE_A, BLUE)

        group = VGroup (a_squared, plus, b_squared, equal, c_squared)

        #line_ACNew = Polygon (C, A, color = PURPLE_C, stroke_width = 12)
        #line_BCNew = Polygon (A, B, color = PURPLE_C, stroke_width = 12)
        #line_ABNew = Polygon (C, B, color = PURPLE_C, stroke_width = 12)

        #Transform (line_AC, line_ACNew)
        #Transform (line_BC, line_BCNew),
        #Transform (line_AB, line_ABNew),

        self.play (TransformFromCopy(line_AC, b_squared),  Write (plus), run_time = 0.7)
        self.play (TransformFromCopy(line_BC, a_squared),  Write (equal), run_time = 0.7)
        self.play (TransformFromCopy(line_AB, c_squared),  run_time = 0.7)

        question = Text ("Proof?", font_size = 63, color = RED).move_to(DOWN*3.6).set_color_by_gradient(RED, PURPLE_A, BLUE)
        self.play (Write(question))
        
        self.play (FadeOut (group), FadeOut (question))

        perpendicular = Line (start = ([-2, 0 ,0]), end = ([-0.048, 2.439, 0]), color = RED)

        intersection = np.array([-0.048, 2.439, 0])
        size = 0.3  # size of the small square
        right_angle = Polygon(
            intersection ,
            np.array([0.195, 2.243, 0]),
            np.array([0, 2, 0]),
            np.array([-0.243, 2.196, 0]),
            color=RED
        )
        label_D = Text("D", font_size = 51, color = BLUE_C).move_to(intersection + RIGHT*0.5 + UP *0.5)
        triangles_group2 = VGroup (triangle_group, right_angle, label_D, perpendicular)

        self.play (Create(perpendicular), run_time = 1)
        self.play (Create (right_angle), Write(label_D), triangles_group2.animate.scale(0.7).shift(UP))
        

        
        #self.play(triangles_group2.animate.scale(0.7).shift(UP))

        vertices_ABC = triangles_group2[0][0].get_vertices()
        vertices_DC_start = triangles_group2[3].get_start()
        vertices_DC_end = triangles_group2[3].get_end()
        

        vertices_all = [
            vertices_ABC[0], 
            vertices_ABC[1], 
            vertices_ABC[2],
            vertices_DC_start,
            vertices_DC_end,
        ]

        #print(vertices_ADC)

        vertices_ACB = [
            vertices_ABC[2],
            vertices_ABC[0],
            vertices_ABC[1],
        ]

        
        vertices_ACD = [
            vertices_ABC[2],
            vertices_ABC[0],
            vertices_DC_end,
        ]

        vertices_CDB = [
            vertices_ABC[0],
            vertices_DC_end,
            vertices_ABC[1],
        ]

        line_CB_new = Line (start = vertices_ACB[1], end= vertices_ACB[2], color = GOLD, stroke_width = 9)
        line_DB_new = Line (start = vertices_CDB[1], end = vertices_CDB[2], color = BLUE, stroke_width = 9)

        line_AB_new = Line (start = vertices_ACB [0], end = vertices_ACB[2], color = GOLD, stroke_width = 9)
        line_CB_new_s = Line (start = vertices_ACB[1], end= vertices_ACB[2], color = BLUE, stroke_width = 9)

        line_AC_new = Line (start = vertices_ACB [0], end  =vertices_ACB[1], color = GOLD, stroke_width = 9)
        line_AD_new = Line (start = vertices_ACB [0], end  =vertices_CDB[1], color = GREEN, stroke_width = 9)
        
        line_AB_new1 = Line (start = vertices_ACB [0], end = vertices_ACB[2], color = GOLD, stroke_width = 9)
        line_AC_new_s = Line (start = vertices_ACB [0], end  =vertices_ACB[1], color = GREEN, stroke_width = 9)

        triangle_ACB = Polygon (*vertices_ACB, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)
        triangle_ACD = Polygon (*vertices_ACD, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)
        triangle_CDB = Polygon (*vertices_CDB, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)


        #langauge = Text("By Geometry,", font_size=45, color = RED, font = "Comic Sans MS").next_to(triangles_group2, DOWN*1.5)
        #self.play (Write (langauge), run_time = 1)

        #math_expression = MathTex(r"\triangle ABC \sim \triangle ACD \sim \triangle CDB").next_to(langauge, DOWN*1.5)

        triangle_ACB_exp = MathTex(r"\triangle ABC", font_size = 45).next_to(triangles_group2, DOWN *3.6).shift (LEFT*1.8).set_color_by_gradient(RED, PURPLE_A, BLUE)
        sim1 = MathTex(r"\sim").next_to (triangle_ACB_exp).set_color_by_gradient(RED, PURPLE_A, BLUE)
        triangle_ACD_exp = MathTex(r"\triangle ACD", font_size = 45).next_to(sim1).set_color_by_gradient(RED, PURPLE_A, BLUE)
        

        self.play (Create(triangle_ACB), run_time = 1)
        self.play(ReplacementTransform(triangle_ACB, triangle_ACB_exp), Write (sim1))
        self.play (Create(triangle_ACD), run_time = 1)
        self.play(ReplacementTransform(triangle_ACD, triangle_ACD_exp))
        #self.play (Write(sim2))

        #self.play(ReplacementTransform(triangle_CDB, triangle_CDB_exp))

        Exp_group1 = VGroup (triangle_ACB_exp, triangle_ACD_exp, sim1)

      
        AC1 = MathTex ("AC", font_size = 45, color = GOLD).next_to (Exp_group1, DOWN*3.6 + LEFT*1.2)
        slash = Text("/", color=WHITE).next_to (AC1)
        AD = MathTex ("AD", font_size = 45, color = GREEN).next_to (slash)

        equals_sim = MathTex ("=", font_size = 45, color = WHITE).next_to(AD)

        self.play(ReplacementTransform (line_AC_new, AC1))
        self.play(Write (slash))
        self.play (ReplacementTransform (line_AD_new, AD))
        self.play(Write (equals_sim))

        AB = MathTex ("AB", font_size = 45, color = GOLD).next_to(equals_sim)
        slash2 = Text("/", color=WHITE).next_to (AB)
        AC2 = MathTex ("AC", font_size = 45, color = GREEN).next_to (slash2)

        self.play(ReplacementTransform (line_AB_new, AB))
        self.play(Write (slash2))
        self.play (ReplacementTransform (line_AC_new_s, AC2))

        sim_exp1_group = VGroup (AC1, slash, AD, equals_sim, AB, slash2, AC2)
        #self.play(FadeOut(sim_exp1_group))

        final_exp_1 = MathTex (r"AC^2 = AD \cdot AB ", color = GOLD).next_to(Exp_group1, DOWN*2.1).shift(LEFT*0.2)

        eqn1_name = MathTex(r"--(1)", font_size=45, color = GOLD)
        eqn1_name.next_to(final_exp_1, RIGHT)

    
        self.play (FadeTransform(sim_exp1_group, final_exp_1), run_time =1)
        self.play ( Create (eqn1_name))
        
        triangle_ACB2_exp = MathTex(r"\triangle ABC", font_size = 45).next_to(final_exp_1, DOWN *4.5).shift (LEFT*1.2).set_color_by_gradient(RED, PURPLE_A, BLUE)
        sim2 = MathTex(r"\sim").next_to (triangle_ACB2_exp).set_color_by_gradient(RED, PURPLE_A, BLUE)
        triangle_CDB_exp = MathTex(r"\triangle CDB", font_size = 45).next_to(sim2).set_color_by_gradient(RED, PURPLE_A, BLUE)

        triangle_ACB_again = Polygon (*vertices_ACB, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)
        self.play (Create(triangle_ACB_again), run_time = 1)
        self.play(ReplacementTransform(triangle_ACB_again, triangle_ACB2_exp), Write (sim2))
        self.play (Create(triangle_CDB), run_time = 1)
        self.play(ReplacementTransform(triangle_CDB, triangle_CDB_exp))

        Exp_group2 = VGroup (triangle_ACB2_exp, triangle_CDB_exp, sim2)

        CB1 = MathTex ("CB", font_size = 45, color = GOLD).next_to (Exp_group2, DOWN*3.6).shift(LEFT*1.5)
        slash3 = MathTex("/", color=WHITE).next_to (CB1)
        DB = MathTex ("DB", font_size = 45, color = BLUE).next_to (slash3)
        equals_sim2 = MathTex ("=", font_size = 45, color = WHITE).next_to(DB)

        self.play(ReplacementTransform (line_CB_new, CB1))
        self.play(Write (slash3))
        self.play (ReplacementTransform (line_DB_new, DB))
        self.play(Write (equals_sim2))

        AB = MathTex ("AB", font_size = 45, color = GOLD).next_to (equals_sim2)
        slash4 = MathTex("/", color=WHITE).next_to (AB)
        CB = MathTex ("CB", font_size = 45, color = BLUE).next_to (slash4)

        self.play(ReplacementTransform (line_AB_new1, AB))
        self.play(Write (slash4))
        self.play (ReplacementTransform (line_CB_new_s, CB))

        self.wait()

        sim_exp2_group = VGroup (CB1, slash3, DB, equals_sim2, AB, slash4, CB)
        #self.play(FadeOut(sim_exp1_group))

        final_exp_2 = MathTex (r"CB^2 = DB \cdot AB", color = BLUE_C ).next_to(Exp_group2, DOWN*2.1).shift(LEFT*0.2)

        eqn2_name = MathTex(r"--(2)", font_size=45, color = BLUE_C)  
        eqn2_name.next_to(final_exp_2, RIGHT)

    
        self.play (FadeTransform(sim_exp2_group, final_exp_2), run_time =1)
        self.play ( Create (eqn2_name))

        final_equation1 = VGroup (final_exp_1, eqn1_name)
        final_equation2 = VGroup (final_exp_2, eqn2_name)

        final_combined_equations = VGroup (final_equation1, final_equation2)

        self.play (FadeOut (Exp_group1), FadeOut(Exp_group2))
        #self.play(final_equation1.animate.shift(UP*0.9))
        #self.play (final_equation2.animate.next_to(final_equation1, DOWN*1))
        #self.wait()

        steps1 = MathTex (r"AC^2 + CB^2 = AD \cdot AB + DB \cdot AB", font_size = 45).set_color_by_gradient(RED, PURPLE_C, BLUE)
        steps2 = MathTex (r"AC^2 + CB^2 = AB \cdot (AD + DB)", font_size = 45).set_color_by_gradient(RED, PURPLE_C, BLUE)
        steps3 = MathTex (r"AC^2 + CB^2 = AB \cdot AB", font_size = 45).set_color_by_gradient(RED, PURPLE_C, BLUE)
        steps4 = MathTex (r"AC^2 + CB^2 = AB^2", font_size =45).set_color_by_gradient(RED, PURPLE_C, BLUE)

        adding_lang = Text ("Adding eqn (1) and eqn (2)", font_size = 36, font = "Comic Sans MS" ).next_to(final_equation2, DOWN*1.5).set_color_by_gradient(RED, PURPLE_A, BLUE)
        self.play (Create (adding_lang))
        self.play (FadeOut (adding_lang))

        self.play (ReplacementTransform(final_combined_equations, steps1))
        self.wait(0.7)
        self.play (ReplacementTransform(steps1, steps2))
        self.wait(0.7)
        self.play (ReplacementTransform(steps2, steps3))
        self.wait(0.7)
        self.play (ReplacementTransform(steps3, steps4))
        self.wait(0.7)

        self.play (steps4.animate.shift (DOWN*2.4).scale (1.2), triangles_group2.animate.shift(DOWN*1.8).scale (1.2))
        box = SurroundingRectangle(steps4, buff=0.2).set_color_by_gradient(PURPLE_A)
        proved = Tex ("Proved.").next_to(steps4).shift(DOWN*1 + LEFT*0.3).set_color_by_gradient(RED, PURPLE_A, BLUE)

        self.play(Create(box), run_time = 1)
        self.play(Write (proved), run_time = 1)

        self.wait()
        

        





        

        

        #self.play(FadeOut(Exp_group))
        
        #triangle_ACB = Polygon (*vertices_ACB, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)
        #triangle_ACB_small = Polygon (*vertices_ACB, stroke_width = 7, color = ORANGE).scale(0.7).shift(DOWN*4+LEFT*2.5)
        
        #vertices_ACB_small = triangle_ACB_small.get_vertices()
        #label_ACBSmall_C = Text("C", font_size = 24, color = PURPLE).move_to(vertices_ACB_small[1] + LEFT*0.5)
        #label_ACBSmall_A = Text("A", font_size = 24, color = PURPLE).move_to(vertices_ACB_small[0] + LEFT*0.5)
        #label_ACBSmall_B = Text("B", font_size = 24, color = PURPLE).move_to(vertices_ACB_small[2] + RIGHT*0.3)
        #self.play (ReplacementTransform(triangle_ACB, triangle_ACB_small))
        #self.play(Write (label_ACBSmall_A), Write(label_ACBSmall_C), Write (label_ACBSmall_B))

        #triangle_ACD = Polygon (*vertices_ACD, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)
        #triangle_CDB = Polygon (*vertices_CDB, fill_color=PURPLE_A, fill_opacity=0.6, stroke_width = 0)
        
        #triangle_ACD_small = Polygon (*vertices_ACD, stroke_width = 7, color = ORANGE).scale(0.7).next_to(triangle_ACB_small, RIGHT * 1.8)
        #vertices_ACD_small = triangle_ACD_small.get_vertices()
        #print(vertices_ACD_small)
        #triangle_CDB_small = Polygon (*vertices_CDB, stroke_width = 7, color = ORANGE).scale(0.7).next_to(triangle_ACD_small, RIGHT * 1.8)
        #vertices_CDB_small = triangle_CDB_small.get_vertices()
        #print(vertices_CDB_small)

        #CD_vector = vertices_ACD_small [2] - vertices_ACD_small [0]
        #CD_vector_2 = vertices_CDB_small [1] - vertices_CDB_small[0]

        #angle1 = np.arctan2(CD_vector[1], CD_vector[0]) 
        #angle2 = np.arctan2(CD_vector_2[1], CD_vector_2[0])                                                  
                                                                  



        #self.play (ReplacementTransform(triangle_ACD, triangle_ACD_small))
        #label_ACDSmall_C = Text("C", font_size = 24, color = PURPLE).move_to(vertices_ACD_small[0] + LEFT*0.5)
        #label_ACDSmall_A = Text("A", font_size = 24, color = PURPLE).move_to(vertices_ACD_small[1] + LEFT*0.5)
        #label_ACDSmall_D = Text("D", font_size = 24, color = PURPLE).move_to(vertices_ACD_small[2] + RIGHT*0.3)
        #triangle_ACD_smallGroup = VGroup(triangle_ACD_small, label_ACDSmall_C, label_ACDSmall_D, label_ACDSmall_A)
        #self.play(Write (label_ACDSmall_A), Write(label_ACDSmall_C), Write (label_ACDSmall_D))


        #self.play (ReplacementTransform(triangle_CDB, triangle_CDB_small))
        #label_CDBSmall_C = Text("C", font_size = 24, color = PURPLE).move_to(vertices_CDB_small[0] + LEFT*0.5)
        #label_CDBSmall_D = Text("D", font_size = 24, color = PURPLE).move_to(vertices_CDB_small[1] + LEFT*0.5)
        #label_CDBSmall_B = Text("B", font_size = 24, color = PURPLE).move_to(vertices_CDB_small[2] + RIGHT*0.3)
        #triangle_CDB_smallGroup = VGroup(triangle_CDB_small, label_CDBSmall_C, label_CDBSmall_D, label_CDBSmall_B)
        #self.play(Write (label_CDBSmall_C), Write(label_CDBSmall_D), Write (label_CDBSmall_B))


        #self.play(Rotate(triangle_ACD_small, -angle1, about_point=vertices_ACD_small[0]))
        #self.play(Rotate(triangle_CDB_small, -angle2, about_point=vertices_CDB_small[1]))
        #self.play(triangle_CDB_small.animate.next_to(triangle_ACD_small, RIGHT* 2.7), run_time = 0.3)
        #self.play(triangle_CDB_small.animate.shift(DOWN*0.24), run_time = 0.3)
         
        #triangle_ACB__area_mini_copy = triangle_ACB.copy().scale(0.3).shift(DOWN*5+LEFT*2.5)
        #similar_sign = MathTex(r"\sim").next_to(triangle_ACB__area_mini_copy)

        #self.play(ReplacementTransform(triangle_ACB, triangle_ACB__area_mini_copy), Write (similar_sign))

        #triangle_ACD__area_mini_copy = triangle_ACD.copy().scale(0.3).next_to(similar_sign).shift(RIGHT*0.5)
        #similar_sign2 = MathTex(r"\sim").next_to(triangle_ACD__area_mini_copy)
        
        #self.play(ReplacementTransform(triangle_ACD, triangle_ACD__area_mini_copy))
        #self.play(Write (similar_sign2))

        #triangle_CDB__area_mini_copy = triangle_CDB.copy().scale(0.3).next_to(similar_sign2).shift(RIGHT*0.5)

        #self.play(ReplacementTransform(triangle_CDB, triangle_CDB__area_mini_copy))


        















        