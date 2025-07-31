from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(circle))
        self.wait(2)
        self.play(Transform(circle, square))
        self.wait(2)