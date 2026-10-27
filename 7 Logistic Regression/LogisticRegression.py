from manim import *
import math
import numpy as np

#These values are from a sample logistic regression model trained in LogisticRegression.ipynb
x_data = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
y_data = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

params_history = [(0.2, 2.0), (0.37093111784713956, 2.3533504824337896),
 (0.46167973201012275, 2.8011695159093613),
 (0.6644445590027857, 3.7799408060859),
 (0.8674826452157667, 4.507537761704537),
 (0.9552111555074958, 4.7189080591494275),
 (1.1021704506400496, 4.9230260078094705),
 (1.2212899284113063, 4.9825836691188545),
 (1.3221732132379092, 4.996633097661072),
 (1.3676392195089757, 4.998593203039079),
 (1.4509462352001232, 4.999773339217859),
 (1.526151091009864, 4.999963796394556),
 (1.5612836923484028, 4.999983756727942),
 (1.6274312773601138, 4.999993646856658),
 (1.6889115432373145, 4.999994851964338),
 (1.7181479020570876, 4.999994952665452),
 (1.7739999542563776, 4.999994995469546),
 (1.8267715174131502, 4.999994999607902),
 (1.8768680549862136, 4.999994999964284),
 (1.901017680936534, 4.999994999985933),
 (1.9476944287536877, 4.999995000009248),
 (1.9924051177353739, 4.999995000000921),
 (2.014087800160502, 4.99999499999426),
 (2.056219013537874, 4.999994999997591),
 (2.0968333342436414, 4.999994999997591),
 (2.116614612989331, 4.999994999997591),
 (2.155200854507044, 4.999995000007583),
 (2.1925742708516656, 4.999995000000921),
 (2.210836297588758, 4.99999499999426),
 (2.246564744682433, 4.999995000002587),
 (2.281296654907749, 4.999994999999256),
 (2.3151015112209623, 4.999994999999256),
 (2.331675908724961, 4.999995000000921),
 (2.364204224964927, 4.999995000005085),
 (2.3959484321901754, 4.999994999994259),
 (2.411541478314549, 4.99999499999759),
 (2.4421968882028406, 4.999995000000088),
 (2.472178309928585, 4.9999949999975914),
 (2.486928006947475, 4.999994999993429),
 (2.51596701749559, 4.999995000001755),
 (2.5444188746465364, 4.999994999994261),
 (2.558433997826603, 4.999995000005919),
 (2.586060045671545, 4.999995000008417),
 (2.613168765487472, 4.999994999990932),
 (2.639784330965766, 4.999995000003422),
 (2.652914233918246, 4.9999949999942634),
 (2.678831475968057, 4.999994999993431),
 (2.7043084549388747, 4.999995000001757),
 (2.7168877014473787, 4.999994999990933),
 (2.741738713740038, 4.999994999995096),
 (2.766193562649932, 4.999995000001755),
 (2.7782773479517737, 4.999995000002588),
 (2.8021669277877854, 4.999995000000925),
 (2.8256975528393675, 4.999994999990099),
 (2.848882505147387, 4.9999950000034215),
 (2.860349283925889, 4.9999949999992594),
 (2.8830388978661188, 4.999995000005089),
 (2.905412683196284, 4.999995000000093),
 (2.9164845241552046, 4.999995000003424),
 (2.938404538065997, 4.999994999998428)]

loss_history = [0.5245677773813024,
 0.4541553549737598,
 0.40293737553072423,
 0.28012170993314006,
 0.19334655284059607,
 0.17024248003793835,
 0.1442795036223951,
 0.12927496616030304,
 0.11871374998281733,
 0.1144320269648847,
 0.10723502022905611,
 0.10136687808496352,
 0.09880588756319605,
 0.09426334158715774,
 0.09033797896540387,
 0.08856271129844759,
 0.08532191623581716,
 0.08242815386503095,
 0.07981986591520346,
 0.07860764241396226,
 0.0763427965674828,
 0.07426446263246063,
 0.07328690192664469,
 0.0714411567611404,
 0.06972576479748918,
 0.06891192200912537,
 0.0673633761221408,
 0.06591054028336149,
 0.06521676849038735,
 0.06388887982391635,
 0.0626339599591681,
 0.06144507444529499,
 0.060873482907095725,
 0.0597726119354365,
 0.058724129413682914,
 0.0582181616173193,
 0.05724031126919656,
 0.05630495218251478,
 0.055852191161270756,
 0.05497466661634244,
 0.05413224363993361,
 0.05372342391877879,
 0.052929159821564195,
 0.05216434409135111,
 0.051427083688610487,
 0.051068242985551585,
 0.050369138575750885,
 0.049693569715197214,
 0.04936417833243369,
 0.048721379673445406,
 0.04809890040581945,
 0.04779493078515013,
 0.047200880253866234,
 0.04662453799973108,
 0.04606499588882937,
 0.04579125949718092,
 0.0452553589057672,
 0.0447342661477757,
 0.04447905178195053,
 0.0439788717130715]

class LogisticRegression(Scene):
    def construct(self):
        template = TexTemplate()
        
        title = MathTex(r"\mathbb{L}\text{ogistic}\ \mathbb{R}\text{egression}\ ", tex_template = template).to_edge(UP, buff = 1.5)
        title.set_color_by_gradient(RED, PURPLE_A, BLUE)
        title.scale(1.5)
        
        initials = Text("@liberative.musings", font="Yu Gothic UI", font_size=27)
        initials.set_opacity(0.4)
        initials.set_color_by_gradient(RED, ORANGE, YELLOW)
        initials.to_edge(DOWN, buff=1)

        equation = MathTex(r"P(x)=\frac{1}{1+e^{-k(x-b)}}",font_size=45)
        equation.set_color_by_gradient(ORANGE, PURPLE_A, RED)
        equation.next_to(title, DOWN, buff=0.5)

        self.add (title, initials, equation)

        axes = Axes(
            x_range = [0, 11.5, 1],
            y_range = [0, 1.2, 0.2],
            x_length=6.5,
            y_length=6,
            axis_config={
                "color":WHITE,
                "include_tip":True,
                "stroke_width": 3,  
                "tip_length": 0.15,   # default ≈ 0.25; smaller = shorter arrow
                "tip_width": 0.2

            },
            x_axis_config={
                "include_ticks": True,
                "include_numbers": True,
                "font_size": 24, 
                
            },
            y_axis_config={
                "include_ticks": True,
                "include_numbers": True,
                "numbers_to_include": [0, 0.2, 0.4, 0.6, 0.8, 1],
                "font_size":24,
            }
        ).shift(DOWN*1)

        x_lbl = MathTex("Features(X)").next_to(axes.c2p(6, 0), DOWN, buff=0.75)
        y_lbl = MathTex("P(X)").next_to(axes.c2p(0, 1.2), UP, buff=0.3).scale(0.75)
        

        self.play(Create(axes, lag_ratio=0.1), Write(x_lbl), Write(y_lbl), run_time = 1.5)

        def func(k, x0, x):
            L = 1
            y = L/(1 + math.exp(-k*(x-x0)))
            return y
        
        #graph = axes.plot(lambda x: func(0.2, 2, x), color=RED)
        #self.play(Create(graph), run_time = 3)
        #self.wait(2)

        # ---- DATA POINTS ----#
        dots = VGroup()
        for x, y in zip(x_data, y_data):
            color = BLUE_D if y == 0 else ORANGE
            dot = Dot(axes.c2p(x, y), color=color, radius=0.09)
            dots.add(dot)
        
        self.play(FadeIn(dots), run_time=1.2)
        

        # ---- INITIAL CURVE ----
        curve = axes.plot(
            lambda x: func(*params_history[0], x),
            x_range=[0, 11.5],
            color="#FF0000",
            stroke_width=4.5
        )
        

        # PARAMS ----
        
        k_lbl = MathTex("k=", font_size=36, color = "#00FFFF" )
        k_num = DecimalNumber(params_history[0][0], num_decimal_places=3, font_size=36, color = "#FF00FF" )
        k_grp = VGroup(k_lbl, k_num).arrange(RIGHT, buff=0.1)
        
        x0_lbl = MathTex(r"b=", font_size=36, color = "#00FFFF")
        x0_num = DecimalNumber(params_history[0][1], num_decimal_places=3, font_size=36, color = "#FF00FF")
        x0_grp = VGroup(x0_lbl, x0_num).arrange(RIGHT, buff=0.1).next_to(k_grp, RIGHT, buff = 1.5)
        
        params = VGroup(k_grp, x0_grp)
        params.next_to(equation, DOWN, buff=0.4)

        # Loss display
        loss_lbl = MathTex(r"\text{Binary CE Loss }(\mathcal{L})=", font_size=36, color = "#00FFFF")
        loss_num = DecimalNumber(loss_history[0], num_decimal_places=5, font_size=36, color=YELLOW)
        loss_grp = VGroup(loss_lbl, loss_num).arrange(RIGHT, buff=0.1)
        loss_grp.next_to(params, DOWN, buff=0.45)

        loss_box = always_redraw(lambda: SurroundingRectangle(
            loss_grp,
            corner_radius=0.15,
            buff=0.15,
            color=PURPLE_C,
            stroke_width=2
        ))
        
        #self.play(Write(equation), run_time=1)
        self.play(Create(curve), FadeIn(params, loss_grp), Create(loss_box), run_time=1.5)
        self.wait (0.75)
        

        # ---- FITTING ANIMATION ----
        for i in range(1, len(params_history)):
            new_curve = axes.plot(
                lambda x, i=i: func(*params_history[i], x),
                x_range=[0, 11.5],
                color="#FF0000",
                stroke_width=4.5
            )
            self.play(
                Transform(curve, new_curve),
                k_num.animate.set_value(params_history[i][0]),
                x0_num.animate.set_value(params_history[i][1]),
                loss_num.animate.set_value(loss_history[i]),
                run_time=0.10,
                rate_func=linear
            )
        

        # ---- CLOSING: k and b converge below Loss ----
        final_k = MathTex(f"k = {params_history[-1][0]:.3f}", font_size=33, color="#FF00FF")
        final_x0 = MathTex(f"b = {params_history[-1][1]:.3f}", font_size=33, color="#FF00FF")
        final_params = VGroup(final_k, final_x0).arrange(DOWN, buff=0.1)
        optimized = MathTex(r"\text{Optimized Parameters}", font_size=36, color=YELLOW).next_to(loss_grp, DOWN, buff=0.6)
        final_params.next_to(optimized, DOWN, buff=0.3)
        
        self.play (Write (optimized), run_time=0.75)

        self.play(
            ReplacementTransform(k_grp, final_k),
            ReplacementTransform(x0_grp, final_x0),
            run_time=1.2
        )

        box = SurroundingRectangle(final_params, buff=0.15).set_color_by_gradient("ORANGE")
        self.play(Create(box), run_time=1)
        
        self.wait(1.5)



        
        






