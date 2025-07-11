from manim import *
import subprocess

class AnimatedIntro(Scene):
    def construct(self):
        # Set white background
        self.camera.background_color = WHITE
        
        # Color palette
        DARK_BLUE = "#003366"
        PYTHON_BLUE = "#0066CC"
        VIBRANT_ORANGE = "#FF6600"
        RICH_PURPLE = "#663399"
        DARK_GREEN = "#008000"
        GOLD = "#FFD700"  # New color for third person
        
        # Main title
        title = Text("WHEN CODE BECOMES ART:",
                   font_size=50,
                   color=DARK_BLUE,
                   weight=BOLD).set_stroke(BLACK, 1.5)
        
        # Subtitle
        subtitle = MarkupText(
            'Building Animations with <span fgcolor="{}">Python</span> &amp; '
            '<span fgcolor="{}">Manim</span>\n'
            'Presented by: '.format(
                PYTHON_BLUE, DARK_GREEN),
            font_size=24,
            color=BLACK
        ).next_to(title, DOWN, buff=0.4)
        
        # Position title group
        title_group = VGroup(title, subtitle).to_edge(UP, buff=1.0)
        
        # Load images with error handling
        try:
            your_photo = ImageMobject(r"C:\Users\mwiin\OneDrive\Imágenes\daniel-pycon.jpg")
            pycon_logo = ImageMobject(r"C:\Users\mwiin\OneDrive\Imágenes\pyconUganda.png")
            collins_photo = ImageMobject(r"C:\Users\mwiin\OneDrive\Imágenes\collins.jpg")  # Add path for Collins' photo
            
            # Constrain image sizes
            max_height = 2.5  # Reduced size to fit three images
            for img in [your_photo, pycon_logo, collins_photo]:
                img.height = max_height
        except:
            # Fallback shapes if images not found
            your_photo = Rectangle(height=2.5, width=2.5, fill_color=PYTHON_BLUE, fill_opacity=0.8)
            pycon_logo = Rectangle(height=2.5, width=2.5, fill_color=VIBRANT_ORANGE, fill_opacity=0.8)
            collins_photo = Rectangle(height=2.5, width=2.5, fill_color=GOLD, fill_opacity=0.8)
        
        # Position images in a row with adjusted spacing
        images = Group(your_photo, collins_photo, pycon_logo).arrange(RIGHT, buff=0.8)
        images.next_to(title_group, DOWN, buff=0.8)
        
        # Add frames
        photo_frame = SurroundingRectangle(your_photo, color=DARK_BLUE, stroke_width=2)
        logo_frame = SurroundingRectangle(pycon_logo, color=VIBRANT_ORANGE, stroke_width=2)
        collins_frame = SurroundingRectangle(collins_photo, color=GOLD, stroke_width=2)
        
        # Labels
        name_label = Text("Mwiine Daniel", font_size=18, color=DARK_BLUE).next_to(your_photo, DOWN, buff=0.15)
        event_label = Text("PyCon Uganda 2025", font_size=18, color=VIBRANT_ORANGE).next_to(pycon_logo, DOWN, buff=0.15)
        collins_label = Text("Eng. Collins Mesue Asibong", font_size=18, color=DARK_BLUE).next_to(collins_photo, DOWN, buff=0.15)
        
        # Animation sequence
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(0.5)
        
        # Animate images appearing one by one
        self.play(FadeIn(your_photo))
        self.play(Create(photo_frame))
        self.play(Write(name_label))

        self.play(FadeIn(collins_photo))
        self.play(Create(collins_frame))
        self.play(Write(collins_label))
        
        self.play(FadeIn(pycon_logo))
        self.play(Create(logo_frame))
        self.play(Write(event_label))
        
        self.wait(3)

    def on_finish(self):
        """Called automatically when rendering completes"""
        video_path = self.renderer.file_writer.movie_file_path
        audio_path = r"C:\Users\mwiin\OneDrive\Imágenes\test-audio.mp3"
        
        # Output file with audio
        output_path = video_path.replace(".mp4", "_with_audio.mp4")
        
        # FFmpeg command to merge audio and video
        cmd = [
            'ffmpeg',
            '-y',
            '-i', video_path,
            '-i', audio_path,
            '-shortest',
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-map', '0:v:0',
            '-map', '1:a:0',
            output_path
        ]
        
        subprocess.run(cmd, check=True)
        print(f"Video with audio created at: {output_path}")