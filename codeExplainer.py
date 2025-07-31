from manim import *

class CodeExplainer(Scene):
    def construct(self):
        # Create a code block from file
        code = Code(
            file_name="code_example.py",  # create this file manually
            language="python",
            background="window",
            font="Monospace",
        ).scale(0.7)

        self.play(FadeIn(code), run_time=3)
        self.wait(1)

        self.play(code.animate.set_color_by_line(start_line=2, end_line=2, color=YELLOW), run_time=1)
        self.wait(1)

        self.play(code.animate.set_color_by_line(start_line=3, end_line=3, color=GREEN), run_time=1)
        self.wait(2)

        explanation = Tex("Function that adds two numbers").next_to(code, DOWN)
        self.play(Write(explanation), run_time=2)
        self.wait(5)
