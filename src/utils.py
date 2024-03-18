# Global Import Definition
import tkinter as tk
from tkinter import Tk, messagebox, Entry

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Slider

# Class Definition
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, otherPoint) -> bool:
        return (self.x == otherPoint.x) and (self.y == otherPoint.y)

# Global Function
def is_float(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False

# Get the mid point between two point
def mid_point(p1: Point, p2: Point) -> Point:
    midP = Point(((p1.x + p2.x) / 2), ((p1.y + p2.y) / 2))
    return midP

# used to calculate how many points in bfBezier
def calculate_amount_of_point(n: int) -> int:
    if n == 1:
        return 3
    else:
        return (calculate_amount_of_point(n - 1) * 2) - 1

# Debugging Tool
def print_list(lis: list[Point]) -> None:
    for i in lis:
        print(i)
