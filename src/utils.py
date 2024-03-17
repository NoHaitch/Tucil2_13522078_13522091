# Global Import Definition
import tkinter as tk
from tkinter import Tk, messagebox, Entry

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

# Partition for Quicksort
def partition(points : list[Point], begin: int, end: int) -> int:
    pivot = begin
    for i in range(begin + 1, end + 1):
        if points[i].x <= points[begin].x:
            pivot += 1
            points[i], points[pivot] = points[pivot], points[i]
    points[pivot], points[begin] = points[begin], points[pivot]
    return pivot

# Quicksort for points
def quicksort(points : list[Point], begin : int = 0, end : int = None) -> None:
    if end is None:
        end = len(points) - 1

    def _quicksort(points : list[Point], begin: int, end: int) -> None:
        if begin >= end:
            return
        pivot = partition(points, begin, end)
        _quicksort(points, begin, pivot - 1)
        _quicksort(points, pivot + 1, end)

    return _quicksort(points, begin, end)

# used to calculate how many points in bfBezier
def calculate_amount_of_point(n: int) -> int:
    if n == 1:
        return 3
    else:
        return (calculate_amount_of_point(n - 1) * 2) - 1

# Binary search for points
def binary_search(points : list[Point], value : Point) -> int:
    low = 0
    high = len(points) - 1

    while low <= high:
        mid = (low + high) // 2
        if points[mid].x < value.x:
            low = mid + 1
        elif points[mid].x > value.x:
            high = mid - 1
        else:
            if points[mid].y < value.y:
                low = mid + 1
            elif points[mid].y > value.y:
                high = mid - 1
            else:
                return mid
    return low

# Split an array at value
def split_array(points : list[Point], value : Point) -> tuple[list[Point], list[Point]]:
    index = binary_search(points, value)
    left = points[:index]
    right = points[index:]
    return left, right

# Debugging Tool
def print_list(lis: list[Point]) -> None:
    for i in lis:
        print(i)
