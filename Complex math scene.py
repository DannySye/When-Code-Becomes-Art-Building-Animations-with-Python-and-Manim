from manim import *

class ComplexScene(Scene):
    def construct(self):
        title = Text("Visualizing Math").scale(1.5)
        eq = MathTex("E=mc^2").scale(1.2)
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(Transform(title, eq))
        self.wait(2)