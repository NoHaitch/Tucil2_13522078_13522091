from utils import *
import time

# Build Bezier Curve using Divide and Conquer algorithm
def dcBezier(control_points: list[Point], desire_iteration: int, num_of_CP: int) -> [list[list[Point]],int]:
    result : list[list[Point]] = []
    for iteration in range(1, desire_iteration + 1):
        if iteration == desire_iteration:
            start_time = time.time()
        result.append(intermediary_Bezier(control_points, iteration, num_of_CP))
    end_time = time.time()
    execution_time = end_time - start_time
    return [result,execution_time]

def intermediary_Bezier(control_points: list[Point], desire_iteration: int, num_of_CP: int) -> list[Point]:
    result : list[Point] = [control_points[0]]
    dcBuilder(control_points, result, 0, desire_iteration, num_of_CP)
    result.append(control_points[-1])
    return result

def dcBuilder(control_points: list[Point], container: list, counter: int, desire_iteration: int, num_of_CP: int) -> None:
    if counter < desire_iteration:
        leftPoints= [control_points[0]]
        rightPoints = [control_points[-1]]
        midpoint = make_mid_point(control_points, num_of_CP, leftPoints,rightPoints)
        counter += 1

        dcBuilder(leftPoints, container, counter, desire_iteration, num_of_CP)
        container.append(midpoint)
        dcBuilder(rightPoints, container, counter, desire_iteration, num_of_CP)

def make_mid_point(control_points: list[Point], num_of_CP: int, useful_midpoints_a: list[Point],useful_midpoints_b: list[Point]) -> Point:
    if num_of_CP == 2:
        real_midpoint = mid_point(control_points[0], control_points[1])
        useful_midpoints_a.append(real_midpoint)
        useful_midpoints_b.insert(0,real_midpoint)
        return real_midpoint
    
    else:
        points_between = []
        for i in range(num_of_CP - 1):
            points_between.append(mid_point(control_points[i], control_points[i + 1]))

        useful_midpoints_a.append(points_between[0])
        useful_midpoints_b.insert(0,points_between[-1])
        num_of_CP -= 1
        return make_mid_point(points_between, num_of_CP, useful_midpoints_a,useful_midpoints_b)
