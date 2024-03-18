from utils import *
import time

# Build Bezier Curve using Brute Force algorithm
def bfBezier(start_point: Point, mid_point: Point, end_point: Point, desire_iteration: int) -> tuple[list[Point], int]:
    start_time = time.time()
    amount_of_point = calculate_amount_of_point(desire_iteration)
    tVals : list[int] = [i / (amount_of_point - 1) for i in range(amount_of_point)]
    result : list[Point] = []
    for t in tVals:
        newX = ((1 - t) ** 2 * start_point.x) + (2 * (1 - t) * t * mid_point.x) + (t**2 * end_point.x)
        newY = ((1 - t) ** 2 * start_point.y) + (2 * (1 - t) * t * mid_point.y) + (t**2 * end_point.y)
        newPoint = Point(newX, newY)
        result.append(newPoint)
    end_time = time.time()
    execution_time = end_time - start_time
    return [result, execution_time]