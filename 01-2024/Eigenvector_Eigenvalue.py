from manim import *
import numpy as np
import random

class Vectors(VectorScene):
    def construct(self):

        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([-3,-2], color = YELLOW)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector = vector)

        vector2 = self.add_vector([2,2])
        self.write_vector_coordinates(vector = vector2)

class VectorsScalar(Scene):
    def construct(self):
        plane1 = NumberPlane(y_range = [-1, 5], background_line_style={"stroke_opacity": 0.7})
        plane1.add_coordinates()

        ##plane2 = Axes(x_range=[-5,5,1], y_range=[-4,4,1], x_length=10, y_length=7)
        ##plane2.add_coordinates()

        vect1 = Line(start = plane1.coords_to_point(0,0), end = plane1.coords_to_point(2,2), stroke_color = RED).add_tip()
        vect1_name = MathTex("\\vec{x}").next_to(vect1, RIGHT, buff=0.1).set_color(RED)

        vect2 = Line(start = plane1.coords_to_point(0,0), end = plane1.coords_to_point(4,4), stroke_color = YELLOW).add_tip()
        vect2_name = MathTex("\\lambda \\vec{x}").next_to(vect2, RIGHT, buff=0.1).set_color(YELLOW)
        
        text = Tex("Untuk", color=WHITE, font_size = 36)
        text2 = MathTex("\\lambda \\geq 1", font_size = 36)
        text2.next_to(text, RIGHT)

        group = VGroup(text,text2)
        group.next_to(vect2_name, DOWN, buff=0.1).set_color=(WHITE)


        stuff = VGroup(plane1, vect1, vect1_name, vect2, vect2_name)

        self.play(DrawBorderThenFill(plane1), run_time=2)
        self.wait()
        self.play(GrowFromPoint(vect1, point = vect1.get_start()), Write(vect1_name), run_time = 2)
        self.wait()
        self.play(GrowFromPoint(vect2, point = vect2.get_start()), Write(vect2_name), run_time = 2)
        self.wait()
        self.play(Write(group), run_time = 2)
        self.wait()

class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,show_coordinates=True,leave_ghost_vectors=False,show_basis_vectors=True)

    def construct(self):
        p1 = [0,0,0]
        p2 = [2,0,0]
        matrix = [[2,3],[0,1]]
        matrix_tex = MathTex("A = \\begin{bmatrix}  2 & 3 \\\ 0  & 1\\end{bmatrix}").to_edge(UL).add_background_rectangle()
        brace = BraceBetweenPoints(p1,p2)
        text = Tex("Vektor Eigen", font_size = 34).add_background_rectangle()
        text2 = Tex("Diregangkan sebesar 2",color=YELLOW, font_size = 34)
        text3= Tex("Nilai Eigen", color=YELLOW, font_size = 34)
        text4 = MathTex("\\lambda = 2", color=YELLOW, font_size = 34)

        text.next_to(text2,DOWN)
        text2.next_to(brace,DOWN)
        Group = VGroup(text,text2)
        Group2 = VGroup(text3,text4)
        Group2.next_to(brace,DOWN)

        text4.next_to(text3,RIGHT)
        ##unit_square = self.get_unit_square()
        ##text = always_redraw(lambda : Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center()))
        self.add_background_mobject(matrix_tex)  
        vector2 = self.add_vector([1,0])
        self.write_vector_coordinates(vector = vector2, color=YELLOW)
        self.apply_matrix(matrix)
        self.play(Create(brace))
        self.play(Write(Group), run_time=4)
        self.play(Unwrite(text2))
        self.play(Write(Group2))
        self.wait()


class Matrix2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,show_coordinates=True,leave_ghost_vectors=False,show_basis_vectors=True)

    def construct(self):
        p1 = [-3,1,0]
        p2 = [0,0,0]
        matrix = [[2,3],[0,1]]
        matrix_tex = MathTex("A = \\begin{bmatrix}  2 & 3 \\\ 0  & 1\\end{bmatrix}").to_edge(UL).add_background_rectangle()
        brace = BraceBetweenPoints(p1,p2)
        text = Tex("Vektor Eigen", font_size = 34).add_background_rectangle()
        text2 = Tex("Diregangkan sebesar 1",color=YELLOW, font_size = 34)
        text3= Tex("Nilai Eigen", color=YELLOW, font_size = 34)
        text4 = MathTex("\\lambda = 1", color=YELLOW, font_size = 34)

        text.next_to(text2,LEFT)
        text2.next_to(brace,DOWN)
        Group = VGroup(text,text2)
        Group2 = VGroup(text3,text4)
        Group2.next_to(brace,DOWN)

        text4.next_to(text3,RIGHT)
        ##unit_square = self.get_unit_square()
        ##text = always_redraw(lambda : Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center()))
        self.add_background_mobject(matrix_tex)  
        vector2 = self.add_vector([-3,1])
        self.write_vector_coordinates(vector = vector2, color=YELLOW)
        self.apply_matrix(matrix)
        self.play(Create(brace))
        self.play(Write(Group), run_time=4)
        self.play(Unwrite(text2))
        self.play(Write(Group2))
        self.wait()

class Matrix3(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self,show_coordinates=True,leave_ghost_vectors=True,show_basis_vectors=True)

    def construct(self):
        p1 = [-3,1,0]
        p2 = [0,0,0]
        matrix = [[2,3],[0,1]]
        matrix_tex = MathTex("A = \\begin{bmatrix}  2 & 3 \\\ 0  & 1\\end{bmatrix}").to_edge(UL).add_background_rectangle()
        brace = BraceBetweenPoints(p1,p2)
        text = Tex("Vektor Eigen", font_size = 34).add_background_rectangle()
        text2 = Tex("Diregangkan sebesar 1",color=YELLOW, font_size = 34)
        text3= Tex("Nilai Eigen", color=YELLOW, font_size = 34)
        text4 = MathTex("\\lambda = 1", color=YELLOW, font_size = 34)

        text.next_to(text2,LEFT)
        text2.next_to(brace,DOWN)
        Group = VGroup(text,text2)
        Group2 = VGroup(text3,text4)
        Group2.next_to(brace,DOWN)

        text4.next_to(text3,RIGHT)
        ##unit_square = self.get_unit_square()
        ##text = always_redraw(lambda : Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center()))
        self.add_background_mobject(matrix_tex)  
        vector2 = self.add_vector([1,1])
        self.write_vector_coordinates(vector = vector2, color=YELLOW)
        self.apply_matrix(matrix)
        self.play(Create(brace))
        self.play(Write(Group), run_time=4)
        self.play(Unwrite(text2))
        self.play(Write(Group2))
        self.wait()