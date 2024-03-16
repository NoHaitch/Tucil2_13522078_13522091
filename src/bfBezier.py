from utils import *

def bfBezier3Point(sp: Point, mp: Point, ep: Point, desiredIteration: int):
    nPoint = pointCalculator(desiredIteration)
    tVals = [i/(nPoint - 1)for i in range(nPoint)]
    result = []
    for t in tVals:
        newX = (1-t)**2 * sp.x + 2 * (1-t) * t * mp.x+t**2 * ep.x
        newY = (1-t)**2 * sp.y + 2 * (1-t) * t * mp.y+t**2 * ep.y
        newPoint = Point(newX,newY)
        result.append(newPoint)
    return result