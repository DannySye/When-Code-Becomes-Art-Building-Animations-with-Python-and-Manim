from manim import *

class AxesGraphDemo(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 10],
            axis_config={"include_numbers": True}
        ).to_edge(DOWN)

        graph = axes.plot(lambda x: x**2, color=BLUE)
        graph_label = axes.get_graph_label(graph, label='x^2')

        self.play(Create(axes), run_time=2)
        self.play(Create(graph), Write(graph_label), run_time=5)
        self.wait(5)
