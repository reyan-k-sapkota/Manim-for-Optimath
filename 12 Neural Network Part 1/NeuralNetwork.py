from manim import *
import math


class Perceptron(Scene):
    def construct (self):
        template = TexTemplate()
        
        title = MathTex(r"\mathbb{N}\text{eural}\ \mathbb{N}\text{etworks}\ ", tex_template = template).to_edge(UP, buff = 1.2)
        title.set_color_by_gradient(YELLOW, GOLD_A, RED_A)
        title.scale(1.8)
        
        initials = Text("@theoptimath", font="Yu Gothic UI", font_size=27)
        initials.set_opacity(0.4)
        initials.set_color_by_gradient(RED, ORANGE, YELLOW)
        initials.to_edge(DOWN, buff=1.5)

        sub_title = MathTex(r"\text{Part 1: Forward Pass} \rightarrow", font_size=48)
        sub_title.set_color_by_gradient(BLUE, PURPLE_A, RED)
        sub_title.next_to(title, DOWN, buff=0.5)

        self.add (title, initials, sub_title)

        intro = MathTex(r"\text{a. Consider a simple neural net.}", font_size=45)
        intro.set_color_by_gradient(RED, PURPLE_A, YELLOW)
        intro.next_to(sub_title, DOWN, buff=0.75)

        #Perceptron Parameters
        x1, x2 = 1, 0.5 
        w1, w2 = 0.6, -0.4
        b = 0.2 #bias
        
        z = w1 * x1 + w2 * x2 + b
        def activation(x):
            return 1 / (1 + np.exp(-x))
        
        y_hat = activation (z)

        #Creating Input Neurons
        input_1 = Circle (radius = 0.5, color = PURPLE, stroke_width = 4).move_to(LEFT * 2.5 + UP * 1.5)
        input_2 = Circle (radius = 0.5, color = ORANGE, stroke_width = 4).next_to(input_1, DOWN*4)
        #input_label_1 = MathTex("x_1").next_to(input_1, LEFT, buff=0.3) 
        input_label_1 = MathTex("x_1", color = WHITE).move_to(input_1).scale(1)        
        #input_label_2 = MathTex("x_2").next_to(input_2, LEFT, buff=0.3)
        input_label_2 = MathTex("x_2", color = WHITE ).move_to(input_2).scale(1)

        input_value_1 = MathTex(
            "1.0", color=PURPLE
        ).move_to(input_1).scale(0.9)

        input_value_2 = MathTex(
            "0.5", color=ORANGE
        ).move_to(input_2).scale(0.9)
  
        input_group_1 = VGroup(input_1, input_label_1)
        input_group_2 = VGroup(input_2, input_label_2)

        input_text = MathTex (r"\text{Input Nodes", font_size = 45, color = YELLOW).next_to(input_1, UP*3)

        self.play(FadeIn(intro), run_time = 0.1)
        #self.play(FadeIn(input_text), FadeIn(input_group_1), FadeIn(input_group_2), run_time = 1)
        #self.play(FadeIn(input_group_2), run_time = 0.9) 

        
        #Drawing neuron lines
        output_1 = Circle (radius = 0.6, color = MAROON, stroke_width = 4.5).move_to(RIGHT * 0, DOWN*1.2)
        output_label_1 = MathTex(r"\sum").next_to(output_1, UP, buff=0.2).scale(0.75)
        output_value_1_initial = MathTex("?").move_to(output_1).scale(1.5)
        output_value_1 = DecimalNumber(
            z,
            num_decimal_places=2,
            color=GREEN,
            ).move_to(output_1).scale(0.9)
        
        output_group_without_value = VGroup(output_1, output_label_1)

        output_text = MathTex (r"\text{Output Node", font_size = 45, color = YELLOW).next_to(output_group_without_value, UP*2)
        
        arrow_1 = Arrow(start=input_1.get_right(), end=output_1.get_left() + UP * 0.2, color=PURPLE,buff=0, tip_length=0.21,max_tip_length_to_length_ratio=0.1)
        arrow_2 = Arrow(start=input_2.get_right(), end=output_1.get_left() + DOWN * 0.2, color=RED,buff=0, tip_length=0.21,max_tip_length_to_length_ratio=0.1)
        #Writing weights in neuron lines
        weight_1 = MathTex(
            "w_1",
            color=PURPLE
        ).scale(0.9).move_to(
            arrow_1.point_from_proportion(0.6) + UP * 0.45
        )

        weight_1_value = MathTex(
            "0.6",
            color=PURPLE
        ).scale(0.9).move_to(
            arrow_1.point_from_proportion(0.6) + UP * 0.45
        )

        weight_2 = MathTex(
            "w_2",
            color=RED
        ).scale(0.9).move_to(
            arrow_2.point_from_proportion(0.6) + DOWN * 0.45
        )

        weight_2_value = MathTex(
            "-0.4",
            color=RED
        ).scale(0.9).move_to(
            arrow_2.point_from_proportion(0.6) + DOWN * 0.45
        )
        
        arrow_1_group = VGroup(arrow_1, weight_1)
        arrow_2_group = VGroup(arrow_2, weight_2)

        self.play(FadeIn(input_text), FadeIn(input_group_1), FadeIn(input_group_2), run_time = 0.5)
        self.play(Create (arrow_1), run_time = 0.5)
        self.play(Create (arrow_2), run_time = 0.5)
        self.play(FadeIn (weight_1), FadeIn(weight_2), run_time = 0.5)
        self.play(Create(output_1), FadeIn (output_label_1), run_time = 0.9)
        #self.play(FadeIn(output_group_without_value), run_time = 0.9)
        self.play(FadeIn(output_value_1_initial), run_time = 0.5)
        

        #self.play(FadeIn(weight_1, weight_2), run_time=1)

        #Writing Bias
        bias_label = MathTex(r"bias",
            color= YELLOW
        ).next_to(output_1, DOWN, buff=1.2).scale(0.9)

        
        bias_value = MathTex(r"0.2",
            color= YELLOW
        ).next_to(output_1, DOWN, buff=1.2).scale(0.9)

        bias_box = SurroundingRectangle(
            bias_label,
            color=YELLOW,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=2
        )

        bias_group = VGroup(bias_label, bias_box)

        #arrow_bias = Arrow(start=bias_box.get_top(), end=output_1.get_bottom(), color=YELLOW,buff=0, tip_length=0.45,max_tip_length_to_length_ratio=0.15)
        arrow_bias = DashedVMobject(
            Arrow(start=bias_box.get_top(), end=output_1.get_bottom(),color=YELLOW,buff=0,tip_length=0.2,max_tip_length_to_length_ratio=0.15),
            num_dashes=5
            )



        # Animation
        self.play(FadeIn(bias_label), Create(bias_box), run_time=1)
        self.play(Create(arrow_bias),run_time=0.5)

        #Calculating value of z and showing the steps
        # Step 1
        z_new = MathTex(r"z").move_to(LEFT * 2.25 + DOWN * 2.7).scale(1.2)

        #self.play(TransformFromCopy(output_label_1, z_new), run_time = 1)
        equal_after_z_new = MathTex(r"=").next_to(z_new, RIGHT*0.5).scale(0.9)
        w1_new = MathTex(r"w_1", color = PURPLE).next_to(equal_after_z_new, RIGHT*0.5).scale(0.9)
        x1_new = MathTex(r"x_1", color = WHITE).next_to(w1_new, RIGHT*0.5).scale(0.9)
        plus_after_x1_new = MathTex(r"+", color = RED).next_to(x1_new, RIGHT*0.5).scale(0.9) 
        w2_new = MathTex(r"w_2", color = ORANGE).next_to(plus_after_x1_new, RIGHT*0.5).scale(0.9)
        x2_new = MathTex(r"x_2", color = WHITE).next_to(w2_new, RIGHT*0.5).scale(0.9)
        plus_after_x2_new = MathTex(r"+", color = RED).next_to(x2_new, RIGHT*0.5).scale(0.9)
        bias_new = MathTex(r"b",color= YELLOW).next_to(plus_after_x2_new, RIGHT*0.5).scale(0.9)

        output_highlight = output_1.copy().scale(1.2)
        output_highlight.set_fill(MAROON, opacity=0.3)
        output_highlight.set_stroke(MAROON, width=3)
        
        input1_highlight = input_1.copy().scale(1.2)
        input1_highlight.set_fill(PURPLE, opacity=0.3)
        input1_highlight.set_stroke(PURPLE, width=3)

        arrow1_highlight = arrow_1_group.copy()
        arrow1_highlight.set_stroke(PURPLE, width=5)
        arrow1_highlight.scale(1.12)

        input2_highlight = input_2.copy().scale(1.2)
        input2_highlight.set_fill(ORANGE, opacity=0.3)
        input2_highlight.set_stroke(ORANGE, width=3)

        arrow2_highlight = arrow_2_group.copy()
        arrow2_highlight.set_stroke(ORANGE, width=5)
        arrow2_highlight.scale(1.12)

        bias_highlight = bias_group.copy().scale(1.2)
        bias_highlight.set_fill (YELLOW, opacity = 0.3)
        bias_highlight.set_stroke (YELLOW, width = 3)

        calc_z = MathTex(r"\text{b. Calculating weighted sum}", font_size=45)
        calc_z.set_color_by_gradient(RED, PURPLE_A, YELLOW)
        calc_z.next_to(sub_title, DOWN, buff=0.75)

        
        self.play(ReplacementTransform(intro, calc_z), run_time =0.5)
        self.wait(0.5)

        self.play(GrowFromCenter(output_highlight), run_time=0.3)
        self.play(TransformFromCopy(output_1, z_new), Create(equal_after_z_new), FadeOut(output_highlight),run_time=0.9)

        self.play(FadeIn(arrow1_highlight), GrowFromCenter (input1_highlight), run_time=0.3)
        self.play(TransformFromCopy(arrow_1_group, w1_new), TransformFromCopy(input_1, x1_new), Create(plus_after_x1_new), FadeOut(input1_highlight), FadeOut(arrow1_highlight), run_time = 0.9)


        self.play(FadeIn(arrow2_highlight), GrowFromCenter (input2_highlight), run_time=0.3)
        self.play(TransformFromCopy(arrow_2_group, w2_new), TransformFromCopy(input_2, x2_new), Create(plus_after_x2_new), FadeOut(input2_highlight), FadeOut(arrow2_highlight), run_time = 0.9)

        self.play(FadeIn(bias_highlight), run_time=0.3)
        self.play(TransformFromCopy(bias_group, bias_new), FadeOut(bias_highlight), run_time = 0.9)

        step1_equation = VGroup(z_new, equal_after_z_new, w1_new, x1_new, plus_after_x1_new, w2_new, x2_new, plus_after_x2_new, bias_new)

        assume_text = MathTex(r"\text{c. Assume initial weights and biases}", font_size=45)
        assume_text.set_color_by_gradient(RED, PURPLE_A, YELLOW)
        assume_text.next_to(sub_title, DOWN, buff=0.75)

        self.play(ReplacementTransform(calc_z, assume_text), run_time =0.3)
        self.wait(0.5)
        
        self.play(ReplacementTransform(input_label_1, input_value_1), ReplacementTransform(input_label_2, input_value_2), 
                  ReplacementTransform(weight_1, weight_1_value), ReplacementTransform(weight_2, weight_2_value),
                  ReplacementTransform(bias_label, bias_value),
                  run_time =0.3)
        self.wait(0.5)

        #Substituting the values
        subs_text = MathTex(r"\text{d. Substituting weights and biases}", font_size=45)
        subs_text.set_color_by_gradient(RED, PURPLE_A, YELLOW)
        subs_text.next_to(sub_title, DOWN, buff=0.75)

        self.play(ReplacementTransform(assume_text, subs_text), run_time =0.3)
        self.wait(0.5)

        
        z_new_sub = MathTex(r"z").move_to(LEFT * 2.7 + DOWN * 2.7).scale(1.2)
        equal_after_z_new_sub = MathTex(r"=").next_to(z_new_sub, RIGHT*0.5).scale(0.9)
        w1_new_sub = MathTex(r"0.6", color = PURPLE).next_to(equal_after_z_new_sub, RIGHT*0.5).scale(0.9)
        multiply_after_w1_new_sub = MathTex(r"*").next_to(w1_new_sub, RIGHT*0.5).scale(0.9)
        x1_new_sub = MathTex(r"1", color = PURPLE).next_to(multiply_after_w1_new_sub, RIGHT*0.5).scale(0.9)
        plus_after_x1_new_sub = MathTex(r"+", color = RED).next_to(x1_new_sub, RIGHT*0.5).scale(0.9) 
        w2_new_sub = MathTex(r"(-0.4)", color = ORANGE).next_to(plus_after_x1_new_sub, RIGHT*0.5).scale(0.9)
        multiply_after_w2_new_sub = MathTex(r"*").next_to(w2_new_sub, RIGHT*0.5).scale(0.9)
        x2_new_sub = MathTex(r"0.5", color = ORANGE).next_to(multiply_after_w2_new_sub, RIGHT*0.5).scale(0.9)
        plus_after_x2_new_sub = MathTex(r"+", color = RED).next_to(x2_new_sub, RIGHT*0.5).scale(0.9)
        bias_new_sub = MathTex(r"0.2",color= YELLOW).next_to(plus_after_x2_new_sub, RIGHT*0.5).scale(0.9)

        step2_equation = VGroup(z_new_sub, equal_after_z_new_sub, 
                                w1_new_sub, multiply_after_w1_new_sub, x1_new_sub, 
                                plus_after_x1_new_sub, 
                                w2_new_sub, multiply_after_w2_new_sub, x2_new_sub,
                                plus_after_x2_new_sub, bias_new_sub
                        )
    
        self.play(ReplacementTransform(step1_equation, step2_equation), run_time = 0.9)
        self.wait(1)
        
        step3_eq = MathTex(
            rf"z = 0.6",
            color = "#00FFFF"
        ).move_to(LEFT * 0 + DOWN * 3.4).scale(1.2)
        
        step3_box = SurroundingRectangle(
            step3_eq,
            color=YELLOW,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=2
        )

        step3_equation = VGroup(step3_eq, step3_box)

        self.play(ReplacementTransform(step2_equation, step3_equation), run_time = 0.9)
        self.wait(0.5)

        output_value_1_final = MathTex("0.6", color = MAROON).move_to(output_1).scale(0.9)

        self.play(ReplacementTransform(step3_equation, output_value_1_final), FadeOut(output_value_1_initial), run_time = 1)

        #Applying activation function

        activation_text = MathTex(r"\text{e. Activation using Sigmoid function}", font_size=45)
        activation_text.set_color_by_gradient(RED, PURPLE_A, YELLOW)
        activation_text.next_to(sub_title, DOWN, buff=0.75)

        self.play(ReplacementTransform(subs_text, activation_text), run_time =0.3)
        self.wait(0.5)

        
        #Creating Activated output eurons
      
        
        arrow3_start = output_1.get_center() + 1.6*(RIGHT * output_1.radius)
        arrow_3 = Arrow(start=arrow3_start, end=arrow3_start+RIGHT,  # Temporary endpoint, 
                    color=RED, buff=0, tip_length=0.36,max_tip_length_to_length_ratio=0.3).set_length(1.6)
        
        output2_label = MathTex(r"\hat{y}", color = WHITE ).scale(0.9).next_to(arrow_3.get_end(), RIGHT, buff=0.2)
        output2_text = MathTex (r"\text{Output }(\hat{y})", font_size = 45, color = YELLOW).next_to(output2_label, UP*5)
        
        act_function = MathTex(
            r"\sigma(z)",
            color=RED
        ).scale(0.9).move_to(
            arrow_3.point_from_proportion(0.6) + UP * 0.45
        )
        arrow_3_group = VGroup(arrow_3, act_function)

        self.play(FadeIn (arrow_3_group), run_time =0.75)
        self.play(FadeIn(output2_text), FadeIn(output2_label), run_time = 0.9)
        #self.play(FadeIn(output2_label), run_time = 0.5)
        self.wait(0.5)

        #Calcuting y = sigma(z)
        y_calc = MathTex(r"\hat{y}").move_to(LEFT * 2.25 + DOWN * 2.7).scale(0.9)
        equals_to_after_y = MathTex(r"=").next_to(y_calc, RIGHT*0.5).scale(0.9)
        sigmoid = MathTex(
             r"\sigma(",
             "z",
             r") = \frac{1}{1 + e^{-",
             "z",
             "}", color = RED
            ).next_to(equals_to_after_y, RIGHT*0.5).scale(1)
        final_answer = MathTex(r"\hat{y} = 0.6456", color = '#00FFFF').move_to(LEFT * 0 + DOWN * 2.7).scale(0.9)
        
        self.play(TransformFromCopy(output2_label, y_calc), FadeIn(equals_to_after_y), run_time = 1)
        self.play(TransformFromCopy(arrow_3_group,sigmoid), run_time = 0.9)
        

        z_value_1 = output_value_1_final.copy().move_to(sigmoid[1]).scale(0.6)
        z_value_2 = output_value_1_final.copy().move_to(sigmoid[3]).scale(0.6)
        
        self.play(Transform(sigmoid[1], z_value_1),Transform(sigmoid[3], z_value_2),run_time=0.75)
        self.wait(0.5)
        self.play(ReplacementTransform(sigmoid, final_answer), FadeOut(y_calc), FadeOut(equals_to_after_y), run_time = 0.9)
        self.wait(0.5)

        output2_answer = MathTex("0.6456", color = "#00FFFF" ).scale(0.9).next_to(arrow_3.get_end(), RIGHT, buff=0.2)
        self.play(ReplacementTransform(final_answer, output2_answer), FadeOut(output2_label), run_time = 1)
        

        #Finding Loss
        loss_text = MathTex(r"\text{f. Finding Loss}", font_size=45)
        loss_text.set_color_by_gradient(RED, PURPLE_A, YELLOW)
        loss_text.next_to(sub_title, DOWN, buff=0.75)

        self.play(ReplacementTransform(activation_text, loss_text), run_time =0.3)
        self.wait(0.5)

        mse_loss= MathTex(r"Loss = (y_{\text{true}} - \hat{y})^2", color = RED_C).scale(1).move_to(LEFT * 0 + DOWN * 2.7).scale(0.9)
        

        self.play (TransformFromCopy(final_answer, mse_loss), run_time = 1)
        self.wait(1)
        #self.play(Create(mse_box), run_time = 0.75)

        show_ytrue= MathTex(r" y_{\text{true}} = 1", color = GREEN).scale(1).next_to(mse_loss, DOWN*1)
        self.play(FadeIn(show_ytrue), run_time = 0.5)
        self.wait(0.5)

        mse_loss_calc = MathTex(r"Loss = (1-0.6456)^2", color = RED_C).scale(1).move_to(LEFT * 0 + DOWN * 2.7).scale(0.9)
        self.play(FadeOut(show_ytrue), ReplacementTransform(mse_loss, mse_loss_calc), run_time = 1)

        mse_loss_ans = MathTex(r"Loss = 0.12556", color = RED_C).scale(1).move_to(LEFT * 0 + DOWN * 2.7).scale(0.9)
        self.play(ReplacementTransform(mse_loss_calc, mse_loss_ans), run_time = 1)
        mse_box = SurroundingRectangle( mse_loss_ans,color=YELLOW, buff=0.2,  corner_radius=0.1,stroke_width=2)
        self.play(Create(mse_box), run_time= 1)

        #Teasing backProp
        
        BP_text = MathTex(r"\text{g. Minimizing Loss}", font_size=45)
        BP_text.set_color_by_gradient(RED, PURPLE_A, YELLOW)
        BP_text.next_to(sub_title, DOWN, buff=0.75)

        self.play(ReplacementTransform(loss_text, BP_text), run_time =0.3)
        self.wait(0.5)

        teaser1 = MathTex (r"\text{This loss is minimized through Backpropagation}", font_size = 36).next_to(mse_box, DOWN * 1)
        teaser1.set_color_by_gradient(RED, PURPLE_A, YELLOW)

        #teaser2 = MathTex (r"\text{Stay Tuned for}", font_size = 45).next_to(teaser1, DOWN * 1, buff=0.75)
        #teaser2.set_color_by_gradient(BLUE, PURPLE_A, RED)

        
        teaser3 = MathTex (r"\text{Part 2: Backpropagation} \leftarrow", font_size = 48).next_to(teaser1, DOWN * 2)
        teaser3.set_color_by_gradient(BLUE, PURPLE_A, RED)
        teaser3_box = SurroundingRectangle(teaser3,color=PURPLE, buff=0.2,  corner_radius=0.1,stroke_width=2)

        self.play(FadeIn(teaser1), run_time = 1)
        #self.play(FadeIn(teaser2), FadeIn(teaser3), run_time = 1)
        self.play(FadeIn(teaser3), run_time = 1)
        self.play(Create (teaser3_box), run_time = 1)
        self.play(
            teaser3_box.animate.set_fill(PURPLE, opacity=0.15),
            run_time=1
        )


        self.wait(1)
        

       