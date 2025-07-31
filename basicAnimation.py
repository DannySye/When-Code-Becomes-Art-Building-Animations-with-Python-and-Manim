from manim import *

class BasicAnimation(Scene):
    def construct(self):
        square = Square()
        self.wait(2)
        self.play(Create(square))
        self.wait(2)