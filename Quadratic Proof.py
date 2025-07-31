from manim import *

class QuadraticFormulaProof(Scene):
    def construct(self):
        # Title
        title = Tex("Quadratic Formula:").to_edge(UP)
        formula = MathTex(
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
        ).next_to(title, DOWN)

        self.play(Write(title), run_time=2)
        self.play(Write(formula), run_time=3)
        self.wait(1)

        # Plot the quadratic function: f(x) = ax^2 + bx + c
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 10],
            axis_config={"include_numbers": True},
            tips=False
        ).scale(0.8).to_edge(DOWN)

        graph = axes.plot(lambda x: x**2 - 2*x - 3, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="x^2 - 2x - 3")

        self.play(Create(axes), run_time=2)
        self.play(Create(graph), Write(graph_label), run_time=3)
        self.wait(1)

        # Show the roots using the formula
        root1_dot = Dot(axes.c2p(-1, 0), color=RED)
        root2_dot = Dot(axes.c2p(3, 0), color=RED)
        root1_label = MathTex("x_1 = -1").next_to(root1_dot, DOWN)
        root2_label = MathTex("x_2 = 3").next_to(root2_dot, DOWN)

        self.play(FadeIn(root1_dot), FadeIn(root2_dot), run_time=1)
        self.play(Write(root1_label), Write(root2_label), run_time=2)
        self.wait(2)

        # Emphasize discriminant
        disc = MathTex("b^2 - 4ac > 0").to_corner(DR)
        self.play(Write(disc), run_time=2)
        self.wait(5)
