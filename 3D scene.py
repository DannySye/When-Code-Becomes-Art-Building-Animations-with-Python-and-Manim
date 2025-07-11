from manim import *

class Calculus3DVisualization(ThreeDScene):
    def construct(self):
        # === Setup 3D camera ===
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()
        self.add(axes)

        # === Define math formulas and place them in 3D space ===
        # Stokes' Theorem
        formula1 = MathTex(
            r"\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_{S} (\nabla \times \mathbf{F}) \cdot d\mathbf{S}",
            font_size=40
        ).move_to([0, 2.5, 0]).rotate(-PI / 2, axis=RIGHT)

        # Divergence Theorem
        formula2 = MathTex(
            r"\iiint_V (\nabla \cdot \mathbf{F}) \, dV = \iint_{\partial V} \mathbf{F} \cdot d\mathbf{S}",
            font_size=40
        ).move_to([0, -2.5, 0]).rotate(-PI / 2, axis=RIGHT)

        # Gradient example
        formula3 = MathTex(
            r"\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right)",
            font_size=40
        ).move_to([-4.5, 0, 0]).rotate(-PI / 2, axis=RIGHT)

        # Laplacian
        formula4 = MathTex(
            r"\Delta f = \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}",
            font_size=40
        ).move_to([4.5, 0, 0]).rotate(-PI / 2, axis=RIGHT)

        # Add all to the scene
        self.add(formula1, formula2, formula3, formula4)

        # === Define 3D Surfaces ===
        surface1 = Surface(
            lambda u, v: [u, v, np.sin(u**2 + v**2)],
            u_range=[-1.5, 1.5],
            v_range=[-1.5, 1.5],
            resolution=(20, 20),
            fill_opacity=0.5,
            checkerboard_colors=[BLUE_D, BLUE_E],
        ).shift(OUT * 0.5)

        surface2 = Surface(
            lambda u, v: [u, v, np.cos(u) * np.sin(v)],
            u_range=[-PI, PI],
            v_range=[-PI, PI],
            resolution=(20, 20),
            fill_opacity=0.5,
            checkerboard_colors=[GREEN_D, GREEN_E],
        ).shift(IN * 0.5)

        self.play(Create(surface1), run_time=3)
        self.play(FadeIn(formula1), run_time=2)

        self.play(Transform(surface1, surface2), run_time=3)
        self.play(FadeIn(formula2), run_time=2)

        # === Add vector field illustration (simplified) ===
        vectors = VGroup()
        for x in np.linspace(-2, 2, 4):
            for y in np.linspace(-2, 2, 4):
                start = np.array([x, y, 0])
                end = np.array([x, y, 0.5])
                arrow = Arrow3D(start, end, color=YELLOW)
                vectors.add(arrow)

        self.play(Create(vectors), run_time=3)
        self.play(FadeIn(formula3), FadeIn(formula4), run_time=2)

        self.wait(2)
