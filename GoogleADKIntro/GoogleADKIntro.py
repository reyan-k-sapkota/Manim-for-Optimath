from manim import *

class GoogleADKIntro (Scene):
    def construct (self):
        text = Text ("<>", font_size=51, gradient= [RED, BLUE])
        self.add(text)
        self.wait(0.7)
        #self.play(text.animate.shift(LEFT*6))
        bracketOpen = Text("<", font_size=51, gradient= [RED, BLUE] ).next_to(text).shift(LEFT*7.5)
        text2 = Text(" Structural Engineering Code Compliance AI Agent", font_size=45, gradient=[RED, BLUE, PURPLE], font = "Times New Roman").next_to (bracketOpen)
        bracketClose = Text("/>", font_size=51, gradient= [RED, BLUE] ).next_to(text2)
        text_group = VGroup (bracketOpen, text2, bracketClose)
        self.play(ReplacementTransform(text, text_group), run_time = 1.5)
        self.play(text_group.animate.shift(UP*3))

        madeby = Text ("Made By: ", font_size=36, gradient= [PURPLE, BLUE]).next_to(text_group, DOWN*6)
        Name1 = Text ("- Rajwol Chapagain ", font_size=33, gradient= [RED, ORANGE, YELLOW]).next_to(text_group, DOWN*1).next_to(madeby, DOWN *1)
        Name2 = Text ("- Rohan Upadhyay ", font_size=33, gradient= [RED, ORANGE, YELLOW]).next_to(text_group, DOWN*1).next_to(Name1, DOWN *1)
        Name3 = Text ("- Reyan Kumar Sapkota ", font_size=33, gradient= [RED, ORANGE, YELLOW]).next_to(text_group, DOWN*1).next_to(Name2, DOWN *1)

        self.play (Write (madeby))
        self.play (Write (Name1), run_time = 0.7)
        self.play (Write (Name2), run_time = 0.7)
        self.play (Write (Name3), run_time = 0.7) 
        self.wait(0.6)

        group_3 = VGroup (madeby, Name1, Name2, Name3)
        self.play (FadeOut(group_3))
        
        self.play(text_group.animate.shift(DOWN*3))
        
        text_duplicate = Text ("<>", font_size=51, gradient= [RED, BLUE])
        self.play(Transform(text_group, text_duplicate), run_time = 1.5)
        self.wait(0.5)


