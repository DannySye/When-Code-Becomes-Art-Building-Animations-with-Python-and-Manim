from manim import *

class GraphFunctions(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 2*PI], y_range=[-1.5, 1.5], axis_config={"include_numbers": True})
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=GREEN)
        sin_label = axes.get_graph_label(sin_graph, label="\\sin x")
        cos_label = axes.get_graph_label(cos_graph, label="\\cos x")

        self.play(Create(axes), run_time=2)
        self.play(Create(sin_graph), Write(sin_label), run_time=4)
        self.wait(2)
        self.play(Transform(sin_graph, cos_graph), Transform(sin_label, cos_label), run_time=4)
        self.wait(5)
