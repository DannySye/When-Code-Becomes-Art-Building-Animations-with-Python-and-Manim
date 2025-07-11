from manim import *

class WorkshopSlides(Scene):
    def construct(self):
        # Slide 1: Title Slide
        title = Text("Manim Workshop", font_size=72, gradient=(BLUE, GREEN))
        subtitle = Text("From Zero to Animation Hero in 45min", font_size=36)
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Slide 2: What is Manim?
        what_is = Text("What is Manim?", font_size=60)
        bullets = BulletedList(
            "Mathematical Animation Engine",
            "Created by 3Blue1Brown",
            "Python-based",
            "Produces publication-quality animations",
            height=4, width=8
        ).next_to(what_is, DOWN, buff=1)
        self.play(Write(what_is))
        self.play(Create(bullets))
        self.wait(3)
        self.play(FadeOut(what_is), FadeOut(bullets))

        # Slide 3: Advantages
        advantages = Text("Why Use Manim?", font_size=60)
        pros = BulletedList(
            "Precise mathematical animations",
            "Free and open-source",
            "Programmatic control",
            "Beautiful default styles",
            "Supports LaTeX",
            height=5, width=8
        ).next_to(advantages, DOWN, buff=1)
        self.play(Write(advantages))
        self.play(Create(pros))
        self.wait(3)
        self.play(FadeOut(advantages), FadeOut(pros))

        # Slide 4: Installation
        install = Text("Installation", font_size=60)
        steps = BulletedList(
            "Python 3.7+ required",
            "Run: pip install manim",
            "FFmpeg for video export",
            "LaTeX for text rendering",
            height=4, width=8
        ).next_to(install, DOWN, buff=1)
        self.play(Write(install))
        self.play(Create(steps))
        self.wait(3)
        self.play(FadeOut(install), FadeOut(steps))

        # Slide 5: Basic Syntax (Fixed Code Display)
        syntax = Text("Basic Structure", font_size=60)
        code_string = '''from manim import *

class MyAnimation(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait()'''
        
        code = Code(
            file_name=None,
            code=code_string,
            language="python",
            style="monokai",
            font="Monospace",
            line_spacing=0.5,
            insert_line_no=False
        ).scale(0.8).next_to(syntax, DOWN, buff=0.5)
        
        self.play(Write(syntax))
        self.play(FadeIn(code))
        self.wait(3)
        self.play(FadeOut(syntax), FadeOut(code))

        # Slide 6: Simple Animation Demo
        demo_title = Text("Simple Animation", font_size=60)
        self.play(Write(demo_title))
        self.wait(1)
        
        square = Square()
        circle = Circle()
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(BLUE, opacity=0.5))
        self.wait(2)
        self.play(FadeOut(demo_title), FadeOut(circle))

        # Slide 7: Complex Animation
        complex_title = Text("Complex Example", font_size=60)
        self.play(Write(complex_title))
        
        axes = Axes(x_range=[-3,3], y_range=[-3,3])
        graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        moving_dot = Dot(color=RED).move_to(axes.c2p(0,0))
        
        self.play(Create(axes), Create(graph))
        self.play(FadeIn(moving_dot))
        
        self.play(MoveAlongPath(moving_dot, graph, run_time=4, rate_func=linear))
        self.wait(2)
        self.play(FadeOut(complex_title), FadeOut(axes), FadeOut(graph), FadeOut(moving_dot))

        # Slide 8: Q&A
        qa = Text("Q&A Session", font_size=72, gradient=(RED, YELLOW))
        contact = Text("Contact: your@email.com", font_size=36)
        self.play(Write(qa))
        self.play(FadeIn(contact, shift=UP))
        self.wait(5)