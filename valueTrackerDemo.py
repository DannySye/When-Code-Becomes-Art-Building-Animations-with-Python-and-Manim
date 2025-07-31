from manim import *

class ValueTrackerDemo(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        number = always_redraw(lambda: DecimalNumber(tracker.get_value()).to_edge(UP))
        
        self.add(number)
        self.play(tracker.animate.set_value(10), run_time=10, rate_func=linear)
        self.wait(5)
