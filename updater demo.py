from manim import *

class UpdaterDemo(Scene):
    def construct(self):
        dot = Dot().shift(LEFT * 4)
        number_line = NumberLine(x_range=[-4, 4], length=8).to_edge(DOWN)

        self.add(number_line, dot)

        def update_dot(mob, dt):
            mob.shift(RIGHT * dt)

        dot.add_updater(update_dot)
        self.wait(10)
        dot.remove_updater(update_dot)
        self.wait(5)
