from manim import *

class ThreeDSphereDemo(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE).shift(OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.add(axes, sphere)
        self.play(Rotate(sphere, angle=PI, axis=UP), run_time=10)
        self.wait(5)
