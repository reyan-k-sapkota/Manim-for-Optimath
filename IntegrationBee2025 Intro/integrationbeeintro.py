from manim import *


class BeeIntro (Scene):
    def construct (self):
        integral = MathTex(
            r"\int_0^{\infty} \frac{\tanh(x)}{x \cosh(2x)} \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)

        integral_2 = MathTex(
            r"\int x(1 - x)^{2025} \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)

        integral_3 = MathTex(
            r"\int \sin\left(\sqrt{x}\right) \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)

        integral_4 = MathTex(
            r"\int \cosh^{-1} x  dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)

        integral_5 = MathTex(
            r"\int_0^{\infty} x^3 e^{-x^2} \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)

        integral_l_1 = MathTex(
            r"\int_0^2 \left\lfloor x^2 - x + 1 \right\rfloor \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)

        integral_l_2 = MathTex(
            r"\int \frac{\csc^2 x - 2025}{\cos^{2025} x} \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)

        integral_l_3 = MathTex(
            r"\int_0^{1} \sqrt{x + \sqrt{x + \sqrt{x + \cdots}}} \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)

        integral_l_4 = MathTex(
            r"\int \frac{\sin^2 x - \cos^2 x}{1 - 2\sin^2 x \cos^2 x} \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)
        
        integral_l_5 = MathTex(
            r"\int \frac{x + 2082}{(x - 2025)^2} \, dx"
        ).set_color_by_gradient(RED, BLUE, PURPLE)


        integral.scale(1.5)  # Optional: scale it up
        integral_2.scale(1.5)  # Optional: scale it up
        integral_3.scale(1.5)  # Optional: scale it up
        integral_4.scale(1.5)  # Optional: scale it up
        integral_5.scale(1.5)  # Optional: scale it up

        integral_l_1.scale(1.5)  # Optional: scale it up
        integral_l_2.scale(1.5)  # Optional: scale it up
        integral_l_3.scale(1.2)  # Optional: scale it up
        integral_l_4.scale(1.2)  # Optional: scale it up
        integral_l_5.scale(1.5)  # Optional: scale it up

        


        self.add (integral_l_5)