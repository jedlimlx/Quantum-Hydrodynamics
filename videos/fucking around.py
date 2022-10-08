import math

import numpy as np
from manim import *
config.frame_width = 32
config.frame_height = 18
class Still(Scene):
    def construct(self):
        rectangle = Rectangle(height = 20.0, width = 32.0, color=BLUE_D)
        rectangle.set_fill(BLUE_D, opacity=1)
        rectangle.shift(10*DOWN)
        water_circle = Circle(radius = 2.0, color=BLUE_D)
        water_circle.set_fill(BLUE_D, opacity=1)
        water_circle.shift(11*UP)
        water_circle.set_z(5)
        water_ellipse = Ellipse(width = 4.0, height = 3.5, color=BLUE_D)
        water_ellipse.set_fill(BLUE_D, opacity=1)
        water_ellipse.set_z(5)
        water_ellipse_2 = Ellipse(width=4.0, height=3.5, color=BLUE_D)
        water_ellipse_2.shift(3.5*DOWN)
        water_ellipse_2.set_fill(BLUE_D, opacity=1)
        water_ellipse_2.set_z(5)
        air_ellipse = Ellipse(width = 5.0, height= 3.0, color=BLACK)
        air_ellipse.shift(2*UP)
        air_ellipse.set_fill(BLACK, opacity=1)
        air_ellipse.set_z(3)
        air_ellipse_2 = Ellipse(width = 5.0, height= 3.0, color=BLACK)
        air_ellipse_2.set_fill(BLACK, opacity=1)
        air_ellipse_2.set_z(3)
        air_arrow_1 = Arrow(start = [2.1, -0.5, 0], end=[2.6, 1, 0])
        air_arrow_2 = Arrow(start = [-2.1, -0.5, 0], end=[-2.6, 1, 0])
        air_text_1 = Text("air")
        air_text_2 = Text("air")
        air_text_1.shift(1.5*UP+2.6*RIGHT)
        air_text_2.shift(1.5*UP+2.6*LEFT)
        air_path = Line(start = [0, 0, 0], end = [0, 2, 0])
        water_path = Line(start = [0, 0, 0], end = [0, -2, 0])
        self.add(rectangle)
        self.add(air_ellipse)
        self.add(water_circle)
        self.play(Transform(water_circle, water_ellipse), Transform(air_ellipse, air_ellipse_2))
        self.play(FadeIn(air_arrow_1), FadeIn(air_arrow_2), FadeIn(air_text_1), FadeIn(air_text_2))
        self.wait(1)
        self.play(FadeOut(air_arrow_1), FadeOut(air_arrow_2), FadeOut(air_text_1), FadeOut(air_text_2))
        self.play(MoveAlongPath(air_ellipse, air_path), MoveAlongPath(water_circle, water_path))
        self.wait(1)
class Bounce(Scene):
    def construct(self):
        rectangle = Rectangle(height = 20.0, width = 32.0, color=BLUE_D)
        rectangle.set_fill(BLUE_D, opacity=1)
        rectangle.shift(10 * DOWN)
        water_circle = Circle(radius = 2.0, color=BLUE_D)
        water_circle.set_fill(BLUE_D, opacity=1)
        water_circle.shift(3 * UP)
        water_circle.set_z(5)
        water_circle_2 = Circle(radius=2.0, color=BLUE_D)
        water_circle_2.set_fill(BLUE_D, opacity=1)
        water_circle_2.shift(3 * UP)
        water_circle_2.set_z(5)
        water_ellipse = Ellipse(width = 4.0, height = 3.5, color=BLUE_D)
        water_ellipse.set_fill(BLUE_D, opacity=1)
        water_ellipse.set_z(5)
        water_ellipse.shift(UP)
        air_ellipse = Ellipse(width = 5.0, height= 3.0, color=BLACK)
        air_ellipse.shift(2*UP)
        air_ellipse.set_fill(BLACK, opacity=1)
        air_ellipse.set_z(3)
        air_path = Line(start=[0, 2, 0], end=[0, 0.5, 0])
        air_path_2 = Line(start = [0, 0.5, 0], end = [0, 2, 0])
        water_body_path = Line(start=[0, -10, 0], end=[0, -9.5, 0])
        water_body_path_2 = Line(start=[0, -9.5, 0], end=[0, -10, 0])
        air_arrow_1 = Arrow(start=[2.1, 0, 0], end=[2.6, 1.5, 0])
        air_arrow_2 = Arrow(start=[-2.1, 0, 0], end=[-2.6, 1.5, 0])
        air_text_1 = Text("air")
        air_text_2 = Text("air")
        air_text_1.shift(2 * UP + 2.6 * RIGHT)
        air_text_2.shift(2 * UP + 2.6 * LEFT)
        air_arrow_3 = Arrow(end=[1.1, 0.5, 0], start=[3.1, 1, 0])
        air_arrow_4 = Arrow(end=[-1.1, 0.5, 0], start=[-3.1, 1, 0])
        air_text_3 = Text("air")
        air_text_4 = Text("air")
        air_text_3.shift(1.5 * UP + 3.6 * RIGHT)
        air_text_4.shift(1.5 * UP + 3.6 * LEFT)
        force_arrow = Arrow(start=[0, 1, 0], end=[0, 4, 0])
        force_text = Text("Force by air on droplet")
        force_text.shift(4.5*UP)
        self.add(rectangle)
        self.add(air_ellipse)
        self.add(water_circle)
        self.play(Transform(water_circle, water_ellipse), MoveAlongPath(air_ellipse, air_path),
                  MoveAlongPath(rectangle, water_body_path))
        self.play(FadeIn(air_arrow_1), FadeIn(air_arrow_2), FadeIn(air_text_1), FadeIn(air_text_2), FadeIn(force_arrow),
                  FadeIn(force_text))
        self.wait(0.5)
        self.play(FadeOut(air_arrow_1), FadeOut(air_arrow_2), FadeOut(air_text_1), FadeOut(air_text_2),
                  FadeOut(force_arrow), FadeOut(force_text))
        self.play(MoveAlongPath(air_ellipse, air_path_2), Transform(water_circle, water_circle_2),
                  MoveAlongPath(rectangle, water_body_path_2))
        self.play(FadeIn(air_arrow_3), FadeIn(air_arrow_4), FadeIn(air_text_3), FadeIn(air_text_4))
        self.wait(0.5)
        self.play(FadeOut(air_arrow_3), FadeOut(air_arrow_4), FadeOut(air_text_3), FadeOut(air_text_4))
class Interaction(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-PI*4, PI*4],
            y_range=[0, 18],
            x_length=32,
            y_length=18
        )
        surface = ax.plot(lambda x: 1 if x == 0 else np.sin(x)/x*3 + 9, color=BLUE_D)
        area = ax.get_area(surface, x_range=[-PI*4, PI*4], color=(BLUE_D, BLUE_D), opacity=1)
        surface_3 = ax.plot(lambda x: 1 if x == 0 else np.sin(x)/x*3 + 9, color=BLUE_D)
        area_3 = ax.get_area(surface, x_range=[-PI*4, PI*4], color=(BLUE_D, BLUE_D), opacity=1)
        self.add(surface, area)
        surface_2 = ax.plot(lambda x: 1 if x == 0 else np.sin(x)/x*3 + 9.5, color=BLUE_D)
        area_2 = ax.get_area(surface_2, x_range=[-PI*4, PI*4], color=(BLUE_D, BLUE_D), opacity=1)
        air_ellipse = Ellipse(height=1, width=1.5, color=BLACK)
        air_ellipse.shift(1.25*RIGHT + 3.75*UP)
        air_ellipse.set_fill(BLACK, opacity=1)
        water_circle = Circle(radius=0.5, color=BLUE_D)
        water_circle.shift(10*UP + 1*RIGHT)
        water_circle.set_fill(BLUE_D, opacity=1)
        water_circle_2 = Circle(radius=0.5, color=BLUE_D)
        water_circle_2.set_fill(BLUE_D, opacity=1)
        water_circle_2.shift(3*RIGHT + 5.5*UP)
        water_ellipse = Ellipse(height=0.75, width=1, color=BLUE_D)
        water_ellipse.shift(RIGHT*1.25 + 3.25*UP)
        water_ellipse.set_fill(BLUE_D, opacity=1)
        air_path = Line([1.25, 5.75, 0], [1.25, 3.25, 0])
        air_path_2 = Line([1.25, 3.25, 0], [3, 5, 0])
        water_ellipse.rotate(-PI/6)
        air_ellipse.rotate(-PI/6)
        air_ellipse.z_index = 1
        water_ellipse.z_index = 2
        water_circle.z_index = 2
        force_arrow = Arrow(start = [1.25, 3.25, 0], end=[3, 5, 0])
        force_text = Text("Force by air on droplet")
        force_text.shift(3.5 * RIGHT + 5.5 * UP)
        force_arrow.z_index = 3
        self.add(water_circle)
        self.play(Transform(surface, surface_2), Transform(area, area_2), MoveAlongPath(air_ellipse, air_path),
                  Transform(water_circle, water_ellipse))
        self.play(FadeIn(force_text), FadeIn(force_arrow))
        self.wait(1)
        self.play(FadeOut(force_arrow), FadeOut(force_text))
        self.play(Transform(surface, surface_3), Transform(area, area_3), MoveAlongPath(air_ellipse, air_path_2),
                  Transform(water_circle, water_circle_2))

class Hill(Scene):
    def construct(self):
        hill = Polygon([-16, -18, 0], [0, 0, 0], [16, -18, 0], fill_color=BLUE_E, fill_opacity=1, stroke_color=BLUE_E).round_corners()
        ball = Circle(radius=1, stroke_color=BLUE_C, fill_color=BLUE_C, fill_opacity=1)
        upPath = Line([-8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [-4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        downPath = Line([-4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [-8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        hill_text = Text("Hill")
        ball_text = Text("Ball")
        energy_text = Text("Insufficient energy to go over hill")
        energy_arrow = Arrow(start=[-4, 1, 0], end=[-4, -3.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        energy_text.shift(4 * LEFT + 1.5 * UP)
        hill_text.shift(8 * DOWN)
        ball_text.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        ball.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        self.add(hill, hill_text)
        self.play(FadeIn(ball), FadeIn(ball_text))
        self.play(MoveAlongPath(ball, upPath), MoveAlongPath(ball_text, upPath))
        self.play(FadeIn(energy_arrow), FadeIn(energy_text))
        self.wait(1)
        self.play(FadeOut(energy_text), FadeOut(energy_arrow))
        self.play(MoveAlongPath(ball, downPath), MoveAlongPath(ball_text, downPath))

class Electron(Scene):
    def construct(self):
        barrier = Polygon([-16, -18, 0], [0, 0, 0], [16, -18, 0], fill_color=BLUE_E, fill_opacity=1, stroke_color=BLUE_E).round_corners()
        electron = Circle(radius=1, stroke_color=BLUE_C, fill_color=BLUE_C, fill_opacity=1)
        upPath = Line([-8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [-4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        downPath = Line([-4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [-8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        barrier_text = Text("Potential Barrier")
        electron_text = Text("Electron", font_size = 32)
        energy_text = Text("Insufficient energy to go over potential barrier")
        energy_arrow = Arrow(start=[-4, 1, 0], end=[-4, -3.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        energy_text.shift(4 * LEFT + 1.5 * UP)
        barrier_text.shift(8 * DOWN)
        electron_text.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        electron.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        self.add(barrier, barrier_text)
        self.play(FadeIn(electron), FadeIn(electron_text))
        self.play(MoveAlongPath(electron, upPath), MoveAlongPath(electron_text, upPath))
        self.play(FadeIn(energy_arrow), FadeIn(energy_text))
        self.wait(1)
        self.play(FadeOut(energy_text), FadeOut(energy_arrow))
        self.play(MoveAlongPath(electron, downPath), MoveAlongPath(electron_text, downPath))

class Tunneling(Scene):
    def construct(self):
        barrier = Polygon([-16, -18, 0], [0, 0, 0], [16, -18, 0], fill_color=BLUE_E, fill_opacity=1, stroke_color=BLUE_E).round_corners()
        electron = Circle(radius=1, stroke_color=BLUE_C, fill_color=BLUE_C, fill_opacity=1)
        electron2 = Circle(radius=1, stroke_color=BLUE_C, fill_color=BLUE_C, fill_opacity=1)
        upPath = Line([-8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [-4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        downPath = Line([4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        barrier_text = Text("Potential Barrier")
        electron_text = Text("Electron", font_size = 32)
        electron_text2 = Text("Electron", font_size=32)
        tunnel_text = Text("Tunnels through the potential barrier")
        tunnel_arrow = Arrow(start=[4, 1, 0], end=[4, -3.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        tunnel_text.shift(4 * RIGHT + 1.5 * UP)
        barrier_text.shift(8 * DOWN)
        electron_text.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        electron.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        electron2.shift(4 * RIGHT + (-4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5) * UP)
        electron_text2.shift(4 * RIGHT + (-4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5) * UP)
        self.add(barrier, barrier_text)
        self.play(FadeIn(electron), FadeIn(electron_text))
        self.play(MoveAlongPath(electron, upPath), MoveAlongPath(electron_text, upPath))
        self.play(FadeOut(electron_text), FadeOut(electron), FadeIn(electron2), FadeIn(electron_text2))
        self.play(FadeIn(tunnel_arrow), FadeIn(tunnel_text))
        self.wait(1)
        self.play(FadeOut(tunnel_text), FadeOut(tunnel_arrow))
        self.play(MoveAlongPath(electron2, downPath), MoveAlongPath(electron_text2, downPath))

class Wall(Scene):
    def construct(self):
        # hill = Polygon([-16, -18, 0], [0, 0, 0], [16, -18, 0], fill_color=BLUE_E, fill_opacity=1,
        #                stroke_color=BLUE_E).round_corners()
        # ball = Circle(radius=1, stroke_color=BLUE_C, fill_color=BLUE_C, fill_opacity=1)
        # upPath = Line([-8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [-4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        # downPath = Line([-4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [-8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        # hill_text = Text("Hill")
        # ball_text = Text("Ball")
        # energy_text = Text("Insufficient energy to go over hill")
        # energy_arrow = Arrow(start=[-4, 1, 0], end=[-4, -3.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        # energy_text.shift(4 * LEFT + 1.5 * UP)
        # hill_text.shift(8 * DOWN)
        # ball_text.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        # ball.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        # self.add(hill)
        # self.wait(12)
        # self.add(hill_text)
        # self.play(FadeIn(ball), FadeIn(ball_text))
        # self.play(MoveAlongPath(ball, upPath), MoveAlongPath(ball_text, upPath))
        # self.play(FadeIn(energy_arrow), FadeIn(energy_text))
        # self.wait(4)
        # self.play(FadeOut(energy_text), FadeOut(energy_arrow))
        # self.play(MoveAlongPath(ball, downPath), MoveAlongPath(ball_text, downPath))
        # self.wait(3)
        # self.play(FadeOut(hill),FadeOut(hill_text), FadeOut(ball_text), FadeOut(ball))
        # barrier = Polygon([-16, -18, 0], [0, 0, 0], [16, -18, 0], fill_color=BLUE_E, fill_opacity=1,
        #                   stroke_color=BLUE_E).round_corners()
        # electron = Circle(radius=1, stroke_color=BLUE_C, fill_color=BLUE_C, fill_opacity=1)
        # electron2 = Circle(radius=1, stroke_color=BLUE_C, fill_color=BLUE_C, fill_opacity=1)
        # upPath = Line([-8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [-4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        # downPath = Line([4, -4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0], [8, -9 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        # barrier_text = Text("Potential Barrier")
        # electron_text = Text("Electron", font_size=32)
        # electron_text2 = Text("Electron", font_size=32)
        # tunnel_text = Text("Tunnels through the potential barrier")
        # tunnel_arrow = Arrow(start=[4, 1, 0], end=[4, -3.5 + (1 ** 2 + 1.125 ** 2) ** 0.5, 0])
        # tunnel_text.shift(4 * RIGHT + 1.5 * UP)
        # barrier_text.shift(8 * DOWN)
        # electron_text.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        # electron.shift(8 * LEFT + (9 - (1 ** 2 + 1.125 ** 2) ** 0.5) * DOWN)
        # electron2.shift(4 * RIGHT + (-4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5) * UP)
        # electron_text2.shift(4 * RIGHT + (-4.5 + (1 ** 2 + 1.125 ** 2) ** 0.5) * UP)
        # self.add(barrier, barrier_text)
        # self.play(FadeIn(electron), FadeIn(electron_text))
        # self.play(MoveAlongPath(electron, upPath), MoveAlongPath(electron_text, upPath))
        # self.play(FadeOut(electron_text), FadeOut(electron), FadeIn(electron2), FadeIn(electron_text2))
        # self.play(FadeIn(tunnel_arrow), FadeIn(tunnel_text))
        # self.wait(1)
        # self.play(FadeOut(tunnel_text), FadeOut(tunnel_arrow))
        # self.play(MoveAlongPath(electron2, downPath), MoveAlongPath(electron_text2, downPath))
        # self.wait(4)
        # self.play(FadeOut(barrier), FadeOut(barrier_text), FadeOut(electron_text2), FadeOut(electron2))
        ax = Axes(
            x_range=[-PI/2, 11*PI/2],
            y_range=[-9, 9],
            x_length=32,
            y_length=18
        )
        path = ax.plot(lambda x:np.sin(x)+1.5, x_range=[PI/2, 3*PI/2])
        path2 = ax.plot(lambda x: np.sin(x) + 1.5, x_range=[3 * PI / 2, 5 * PI / 2])
        path3 = ax.plot(lambda x: np.sin(2*x-PI/2) + 1.5, x_range=[5 * PI / 2, 6 * PI / 2])
        path4 = ParametricFunction(lambda x: np.array((-x - 4*PI/2, np.sin(2*-x-PI/2) + 1.5, 0)),
                                   t_range=[-6 * PI / 2, -5 * PI / 2])
        path5 = ParametricFunction(lambda x: np.array((-x - 4*PI/2, np.sin(-x) + 1.5, 0)),
                                   t_range=[-5 * PI / 2, -3 * PI / 2])
        path6 = ParametricFunction(lambda x: np.array((-x - 4*PI/2, np.sin(-x) + 1.5, 0)),
                                   t_range=[-3 * PI / 2, -PI / 2])
        path7 = ParametricFunction(lambda x: np.array((-x - 4 * PI / 2, np.sin(-x) + 1.5, 0)),
                                   t_range=[-PI / 2, PI / 2])
        path8 = ParametricFunction(lambda x: np.array((-x - 4 * PI / 2, np.sin(-x) + 1.5, 0)),
                                   t_range=[PI / 2, 3 * PI / 2])
        path9 = ax.plot(lambda x:np.sin(x)+1.5, x_range=[5*PI/2, 7*PI/2])
        path10 = ax.plot(lambda x: np.sin(x) + 1.5, x_range=[7 * PI / 2, 9 * PI / 2])
        path11 = ax.plot(lambda x:np.sin(x)+1.5, x_range=[9*PI/2, 11*PI/2])
        path12 = ax.plot(lambda x: np.sin(x) + 1.5, x_range=[11 * PI / 2, 13 * PI / 2])
        wall = Rectangle(width=2, height=6, color=WHITE, fill_color=WHITE, fill_opacity=1)
        wall_text = Text("Wall", color=BLACK)
        wall.shift(6*DOWN + 7*RIGHT)
        wall_text.shift(6*DOWN + 7*RIGHT)
        water_ellipse = Ellipse(width = 4.0, height = 3.5, color=BLUE_D)
        water_ellipse.set_fill(BLUE_D, opacity=1)
        air_ellipse = Ellipse(width = 5.0, height= 4.0, color=BLACK)
        air_ellipse.set_fill(BLACK, opacity=1)
        rectangle = Rectangle(height=20.0, width=32.0, color=BLUE_D)
        rectangle.set_fill(BLUE_D, opacity=1)
        droplet_text = Text("Droplet", color=WHITE)
        water_ellipse.z_index = 2
        air_ellipse.z_index = 1
        rectangle.z_index = 0
        wall.z_index = 1
        wall_text.z_index = 3
        droplet_text.z_index = 3
        upPath = Line([0, -10, 0], [0, -9.5, 0])
        downPath = Line([0, -9.5, 0], [0, -10, 0])
        self.add(wall, wall_text)
        self.play(Create(droplet_text))
        self.play(MoveAlongPath(water_ellipse, path), MoveAlongPath(air_ellipse, path), MoveAlongPath(droplet_text, path),
                  MoveAlongPath(rectangle, upPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path2), MoveAlongPath(air_ellipse, path2), MoveAlongPath(droplet_text, path2),
                  MoveAlongPath(rectangle, downPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path3), MoveAlongPath(air_ellipse, path3), MoveAlongPath(droplet_text, path3),
                  MoveAlongPath(rectangle, upPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path4), MoveAlongPath(air_ellipse, path4), MoveAlongPath(droplet_text, path4),
                  MoveAlongPath(rectangle, downPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path5), MoveAlongPath(air_ellipse, path5), MoveAlongPath(droplet_text, path5),
                  MoveAlongPath(rectangle, upPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path6), MoveAlongPath(air_ellipse, path6), MoveAlongPath(droplet_text, path6),
                  MoveAlongPath(rectangle, downPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path7), MoveAlongPath(air_ellipse, path7), MoveAlongPath(droplet_text, path7),
                  MoveAlongPath(rectangle, upPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path8), MoveAlongPath(air_ellipse, path8), MoveAlongPath(droplet_text, path8),
                  MoveAlongPath(rectangle, downPath), rate_func=linear)
        self.play(FadeOut(water_ellipse, droplet_text))
        self.play(MoveAlongPath(water_ellipse, path), MoveAlongPath(air_ellipse, path), MoveAlongPath(droplet_text, path),
                  MoveAlongPath(rectangle, upPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path2), MoveAlongPath(air_ellipse, path2), MoveAlongPath(droplet_text, path2),
                  MoveAlongPath(rectangle, downPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path9), MoveAlongPath(air_ellipse, path9), MoveAlongPath(droplet_text, path9),
                  MoveAlongPath(rectangle, upPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path10), MoveAlongPath(air_ellipse, path10), MoveAlongPath(droplet_text, path10),
                  MoveAlongPath(rectangle, downPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path11), MoveAlongPath(air_ellipse, path11), MoveAlongPath(droplet_text, path11),
                  MoveAlongPath(rectangle, upPath), rate_func=linear)
        self.play(MoveAlongPath(water_ellipse, path12), MoveAlongPath(air_ellipse, path12), MoveAlongPath(droplet_text, path12),
                  MoveAlongPath(rectangle, downPath), rate_func=linear)
        self.wait(3)
        self.play(Create(Tex("P(tunnel)=e^{-kw}")))
        self.wait(3)