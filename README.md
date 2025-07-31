# When Code Becomes Art: Building Animations with Python and Manim

This repository contains the code and resources for the presentation "When Code Becomes Art: Building Animations with Python and Manim," presented by Mwiine Daniel and Collins Mesue Asibong at PyCon Uganda 2025.

## About This Project

The goal of this project is to demonstrate how to use Python and the Manim library to create stunning mathematical animations. Manim is a powerful animation engine created by 3Blue1Brown for creating precise, code-driven animations, particularly for educational content, data visualization, and storytelling.

## Why Choose Manim?

* **Code-Driven Control:** Create precise and complex animations programmatically.
* **High-Quality Output:** Generate crisp, high-resolution videos.
* **LaTeX Support:** Seamlessly integrate mathematical equations and formulas.
* **3D Capabilities:** Create and animate in three-dimensional space.
* **Strong Community:** A large and active community for support and resources.

## Installation

### Prerequisites

* Python 3.8 or newer
* `pip` (Python package manager)
* A modern terminal (PowerShell, Bash, CMD, etc.)
* Git (for installing the development version of Manim)
* A code editor (e.g., VS Code, PyCharm)
* A LaTeX distribution (e.g., MiKTeX, MacTeX, TeX Live)

### Installation Steps

1.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install Manim:**
    ```bash
    pip install manim
    ```

3.  **Verify the installation:**
    ```bash
    manim --version
    ```

## Getting Started: Creating Animations

### Basic Syntax

The core of Manim is the `Scene` class. You create animations by defining a class that inherits from `Scene` and implementing the `construct` method.

**Hello, World!**

```python
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, World")
        self.play(Write(text))
        self.wait(3)
```

### Rendering a Scene

To render an animation, use the `manim` command in your terminal:

```bash
manim -pql your_script_name.py YourSceneName
```

* `-p`: Preview the animation when it's done rendering.
* `-q`: Render in a lower quality for faster previews.
* `l`: Use the lower quality setting.

For a better development experience, consider using the [Manim Sideview VS Code extension](https://marketplace.visualstudio.com/items?itemName=manim-is-a-heckin-good-engine.manim-sideview).

### Animation Examples

#### Simple Animation: Creating a Shape

```python
from manim import *

class BasicAnimation(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.wait(1)
```

#### Intermediate Animation: Transforming Shapes

```python
from manim import *

class TransformExample(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(circle))
        self.wait(2)
        self.play(Transform(circle, square))
        self.wait(1)
```

#### Complex Animation: Combining Text and Math

To use mathematical text, you need a LaTeX installation.

```python
from manim import *

class MathScene(Scene):
    def construct(self):
        eq = MathTex("e^{i\\pi} + 1 = 0")
        self.play(Write(eq))
        self.wait(2)
```python
from manim import *

class ComplexScene(Scene):
    def construct(self):
        title = Text("Visualizing Math")
        eq = MathTex("E=mc^2")
        self.play(Write(title))
        self.wait(1)
        self.play(Transform(title, eq))
        self.wait(2)
```

## Advanced Concepts

Manim offers many advanced features for more complex animations:

* **`ValueTracker`:** Animate changes in numerical values.
* **Updaters:** Make objects continuously update based on other objects or values.
* **Axes and Graphs:** Plot functions and data.
* **`ThreeDScene`:** Create animations in 3D space.
* **`add_sound()`:** Add audio to your animations.

## Resources

* **Official Documentation:** [docs.manim.community](https://docs.manim.community)
* **GitHub Repository:** [github.com/ManimCommunity/manim](https://github.com/ManimCommunity/manim)
* **Discord Community:** Join the [Manim Community Discord](https://www.manim.community/discord/) for help and discussion.

---
