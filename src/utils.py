# Global Import Definition
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Class Definition
class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self, otherPoint) -> bool:
        return (self.x == otherPoint.x) and (self.y == otherPoint.y)
    
def midPoint(p1: Point, p2: Point) -> Point:
    midP = Point(((p1.x+p2.x) /2),((p1.y+p2.y)/2))
    return midP

def printList(lis : list):
    for i in lis:
        print(i)

def partition(points, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if points[i].x <= points[begin].x:
            pivot += 1
            points[i], points[pivot] = points[pivot], points[i]
    points[pivot], points[begin] = points[begin], points[pivot]
    return pivot

def quicksort(points, begin=0, end=None):
    if end is None:
        end = len(points) - 1
    def _quicksort(points, begin, end):
        if begin >= end:
            return
        pivot = partition(points, begin, end)
        _quicksort(points, begin, pivot-1)
        _quicksort(points, pivot+1, end)
    return _quicksort(points, begin, end)

#used to calculate how many points in bfBezier
def pointCalculator(n: int) -> int:
    if(n == 1):
        return 3
    else:
        return (pointCalculator(n-1)*2)-1
    
def binary_search(points, value):
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

def split_array(points, value):
    index = binary_search(points, value)
    left = points[:index]
    right = points[index:]
    return left, right
