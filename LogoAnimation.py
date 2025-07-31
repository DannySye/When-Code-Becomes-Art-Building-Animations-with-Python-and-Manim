from manim import *

class PythonLogoAnimation(Scene):
    def construct(self):
        # Upper "snake" body - yellow
        upper = RoundedRectangle(
            height=2, width=2.5, corner_radius=0.5,
            color=YELLOW, fill_opacity=1
        ).shift(UP + LEFT * 1.2)

        # Lower "snake" body - blue
        lower = RoundedRectangle(
            height=2, width=2.5, corner_radius=0.5,
            color=BLUE, fill_opacity=1
        ).shift(DOWN + RIGHT * 1.2)

        # Eye circles
        eye1 = Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(upper.get_center() + LEFT*0.6 + UP*0.4)
        eye2 = Circle(radius=0.1, color=WHITE, fill_opacity=1).move_to(lower.get_center() + RIGHT*0.6 + DOWN*0.4)

        # Python text
        py_text = Text("Python", font_size=42, weight=BOLD).next_to(lower, DOWN, buff=0.5)

        # Animations
        self.play(DrawBorderThenFill(upper), run_time=2)
        self.play(DrawBorderThenFill(lower), run_time=2)
        self.wait(0.5)

        self.play(FadeIn(eye1), FadeIn(eye2), run_time=1)
        self.play(Write(py_text), run_time=2)

        self.wait(5)
