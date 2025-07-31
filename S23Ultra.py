from manim import *

class SamsungS23UltraAnimation(Scene):
    def construct(self):
        # Set a background color
        self.camera.background_color = "#1C1C1C"

        # 1. Animate the Samsung Logo
        logo = Text("SAMSUNG", font_size=48, weight=BOLD).set_color(WHITE)
        self.play(Write(logo), run_time=2)
        self.wait(0.5)

        # 2. Transition to the Phone Body
        phone_body = RoundedRectangle(
            width=4.5, 
            height=8, 
            corner_radius=0.6, 
            color="#2E2E2E", 
            fill_opacity=1
        )
        
        # Position the phone body relative to the logo, then move the logo away
        phone_body.next_to(logo, DOWN, buff=1.5)
        self.play(FadeOut(logo), Create(phone_body), run_time=1.5)
        self.wait(0.5)

        # 3. Animate the Cameras
        # Main camera lenses
        cam1 = Circle(radius=0.4, color=BLACK, fill_opacity=1).set_stroke(color="#555555", width=3)
        cam2 = Circle(radius=0.4, color=BLACK, fill_opacity=1).set_stroke(color="#555555", width=3)
        cam3 = Circle(radius=0.4, color=BLACK, fill_opacity=1).set_stroke(color="#555555", width=3)
        
        # Smaller sensors
        sensor1 = Circle(radius=0.15, color=BLACK, fill_opacity=1).set_stroke(color="#555555", width=2)
        sensor2 = Circle(radius=0.1, color=BLACK, fill_opacity=1).set_stroke(color="#555555", width=2)

        # Group and position the cameras
        cameras = VGroup(cam1, cam2, cam3).arrange(DOWN, buff=0.2)
        sensors = VGroup(sensor1, sensor2).arrange(DOWN, buff=0.3)
        
        camera_system = VGroup(cameras, sensors).arrange(RIGHT, buff=0.4)
        camera_system.move_to(phone_body.get_center() + UP * 1.5)

        self.play(LaggedStart(*[GrowFromCenter(cam) for cam in camera_system], lag_ratio=0.2), run_time=2)
        self.wait(0.5)
        
        # 4. Add other details (e.g., Flash)
        flash = Circle(radius=0.12, color="#E0E0E0", fill_opacity=1).set_stroke(color=BLACK, width=2)
        flash.next_to(sensors, DOWN, buff=0.4)
        
        self.play(FadeIn(flash, scale=0.5), run_time=1)
        self.wait(0.5)

        # 5. Animate the S-Pen
        s_pen_body = RoundedRectangle(width=0.3, height=5, corner_radius=0.1, color="#333333", fill_opacity=1)
        s_pen_tip = Triangle(color="#AAAAAA", fill_opacity=1).scale(0.1).rotate(PI)
        s_pen_button = Rectangle(width=0.05, height=0.5, color="#555555", fill_opacity=1)

        s_pen_tip.next_to(s_pen_body, DOWN, buff=-0.05)
        s_pen_button.move_to(s_pen_body.get_center() + UP*1.5)
        
        s_pen = VGroup(s_pen_body, s_pen_tip, s_pen_button)
        s_pen.next_to(phone_body, RIGHT, buff=0.5)
        
        self.play(Create(s_pen), run_time=1.5)
        self.wait(2)