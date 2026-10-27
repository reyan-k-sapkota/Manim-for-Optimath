from manim import *

class ActivationFunctions(Scene):
    def construct(self):
        
        template = TexTemplate()

        title = MathTex(r"\mathbb{A}\text{ctivation}\ \mathbb{F}\text{unctions}\ ", tex_template = template).to_edge(UP, buff = 1.2)
        title.set_color_by_gradient(YELLOW, GOLD_A, RED_A)
        title.scale(1.7)
        
        initials = Text("@theoptimath", font="Yu Gothic UI", font_size=27)
        initials.set_opacity(0.4)
        initials.set_color_by_gradient(RED, ORANGE, YELLOW)
        initials.to_edge(DOWN, buff=1)

        self.add(title, initials)

        # Shared axes template        
        axes = Axes(
            x_range = [-5, 5, 1],
            y_range = [-0.5, 2, 1],
            x_length=7.2,
            y_length=5,
            axis_config={
                "color": GRAY_B,
                "include_tip":True,
                "stroke_width": 6,  
                "tip_length": 0.15,   # default ≈ 0.25; smaller = shorter arrow
                "tip_width": 0.2

            },
            x_axis_config={
                "include_ticks":False,
                "include_numbers": False,
                "font_size": 24, 
                
            },
            y_axis_config={
                "include_ticks": True,
                "include_numbers": True,
                "numbers_to_include": [1],
                "font_size":27,
            }
        ).shift(DOWN*0).scale(1.1)

        x_lbl = MathTex("z").next_to(axes.c2p(4.5,0), DOWN, buff=0.3).scale(1.2)
        y_lbl = MathTex(r"\sigma(z) ").next_to(axes, UP, buff=0.3).scale(1.2)

        self.add(axes, x_lbl, y_lbl) 

        #1. ReLu
        def ReLu(z):
            return np.maximum(0, z)

        graph_relu = axes.plot(
            ReLu,
            x_range=[-4, 2],
            color= ORANGE,
            stroke_width=5.2,
            use_smoothing=False
        )

        formula_relu = MathTex(r"\text{ReLU}(z) = \max(0, z)", font_size=63).next_to(axes, UP, buff=1.5).set_color_by_gradient(ORANGE)
        title_relu = MathTex(r"\mathbb{R}\text{eLu}\ ", tex_template = template).next_to(axes, DOWN, buff= 1.3).set_color_by_gradient(ORANGE).scale(1.5)
        self.play(FadeIn (formula_relu), Create(graph_relu), FadeIn(title_relu), run_time=1.5)
        self.wait(0.9)

        #2. Sigmoid
        def Sigmoid(z):
            return 1 / (1 + np.exp(-z))
        
        graph_sig = axes.plot(
            Sigmoid,
            x_range=[-5, 5],
            color= YELLOW,
            stroke_width=5.2,
            use_smoothing=False
        )

        formula_sig = MathTex(r"\sigma(z) = \frac{1}{1 + e^{-z}}", font_size=63).next_to(axes, UP, buff=1.5).set_color_by_gradient(YELLOW)
        title_sig = MathTex(r"\mathbb{S}\text{igmoid}}\ ", tex_template = template).next_to(axes, DOWN, buff= 1.3).set_color_by_gradient(YELLOW).scale(1.5)
        self.play(ReplacementTransform(formula_relu, formula_sig), FadeOut (graph_relu), Create(graph_sig), ReplacementTransform(title_relu, title_sig), run_time=1.5)
        self.wait(0.9)

        #3. Tanh
        def Tanh(z):
            return np.tanh(z)
        
        graph_tanh = axes.plot(
            Tanh,
            x_range=[-5, 5],
            color= RED,
            stroke_width=5.2,
            use_smoothing=False
        )

        formula_tanh = MathTex(r"\sigma(z) = \frac{e^{z} - e^{-z}}{e^z + e^{-z}}", font_size=63).next_to(axes, UP, buff=1.5).set_color_by_gradient(RED)        
        title_tanh = MathTex(r"\mathbb{T}\text{anh}}\ ", tex_template = template).next_to(axes, DOWN, buff= 1.3).set_color_by_gradient(RED).scale(1.5)        
        self.play(ReplacementTransform(formula_sig, formula_tanh), FadeOut (graph_sig), Create(graph_tanh), ReplacementTransform(title_sig, title_tanh), run_time=1.5)
        self.wait(0.9)

        #4. Hard Tanh
        def hard_tanh(z):
            return np.clip(z, -1, 1)
        
        graph_hardtanh = axes.plot(
            hard_tanh,
            x_range=[-5, 5],
            color= RED_B,
            stroke_width=5.2,
            use_smoothing=False
        )

        formula_hardtanh = MathTex(r"\mathrm{HardTanh}(z) = \begin{cases} \mathrm{max\_val} & \text{if } z > \mathrm{max\_val} \\ \mathrm{min\_val} & \text{if } z < \mathrm{min\_val} \\ z & \text{otherwise} \end{cases}"  
            ,font_size=42).next_to(axes, UP, buff=1.5).set_color_by_gradient(RED_B)
        title_hardtanh = MathTex(r"\mathbb{H}\text{ard}}\ \mathbb{T}\text{anh}}\ ", tex_template = template).next_to(axes, DOWN, buff= 1.3).set_color_by_gradient(RED_B).scale(1.5)        
        self.play(ReplacementTransform(formula_tanh, formula_hardtanh), FadeOut (graph_tanh), Create(graph_hardtanh), ReplacementTransform(title_tanh, title_hardtanh), run_time=1.5)
        self.wait(0.9)

        #5. Swish
        def swish(z):
            return z / (1 + np.exp(-z))
        
        graph_swish = axes.plot(
            swish,
            x_range=[-5, 2],
            color= BLUE,
            stroke_width=5.2,
            use_smoothing=False
        )

        formula_swish = MathTex(
            r"\text{Swish}(z) =  \frac{z}{1 + e^{-z}}",
            font_size=63
            ).next_to(axes, UP, buff=1.5).set_color_by_gradient(BLUE)
        title_swish = MathTex(r"\mathbb{S}\text{wish}}\ ", tex_template = template).next_to(axes, DOWN, buff= 1.3).set_color_by_gradient(BLUE).scale(1.5)        
        self.play(ReplacementTransform(formula_hardtanh, formula_swish), FadeOut (graph_hardtanh), Create(graph_swish), ReplacementTransform(title_hardtanh, title_swish), run_time=1.5)
        self.wait(0.9)

        #6. Leaky ReLU
        def leaky_relu(x, alpha=0.1):
            return alpha * x if x < 0 else x
        
        graph_leaky_relu = axes.plot(
            leaky_relu,
            x_range = [-5, 2],
            color= GREEN,
            stroke_width=5.2,
            use_smoothing=False
        )

        formula_leaky_relu = MathTex(
            r"\text{LeakyReLU}(z) = \begin{cases} \alpha z & \text{if } z < 0 \\ z & \text{if } z \geq 0 \end{cases}",
            font_size=51
            ).next_to(axes, UP, buff=1.5).set_color_by_gradient(GREEN)    
        title_leaky_relu = MathTex(r"\mathbb{L}\text{eaky}\ \mathbb{R}\text{eLU}\  ", tex_template = template).next_to(axes, DOWN, buff= 1.3).set_color_by_gradient(GREEN).scale(1.5)
        self.play(ReplacementTransform(formula_swish, formula_leaky_relu), FadeOut (graph_swish), Create(graph_leaky_relu), ReplacementTransform(title_swish, title_leaky_relu), run_time=1.5)
        self.wait(0.9)

        #7. GELU
        def gelu(x):
            return 0.5 * x * (1 + np.tanh(
                np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))
            ))
        
        graph_gelu = axes.plot(
            gelu,
            x_range = [-5, 2],
            color= "#00FFFF",
            stroke_width=5.2,
            use_smoothing=False
        )
        
        formula_gelu = MathTex(
            r"\text{GELU}(z) \approx 0.5z\left(1 + \tanh\left[\sqrt{\frac{2}{\pi}}\left(z + 0.044715z^3\right)\right]\right)",
            font_size=33
            ).next_to(axes, UP, buff=1.5).set_color_by_gradient("#00FFFF")        
        title_gelu = MathTex(r"\mathbb{G}\text{ELU}\ ", tex_template = template).next_to(axes, DOWN, buff= 1.3).set_color_by_gradient("#00FFFF").scale(1.5)
        self.play(ReplacementTransform(formula_leaky_relu, formula_gelu), FadeOut (graph_leaky_relu), Create(graph_gelu), ReplacementTransform(title_leaky_relu, title_gelu), run_time=1.5)
        self.wait(3)



        




        
        







