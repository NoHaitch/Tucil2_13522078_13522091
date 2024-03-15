from classes import *
def midPoint(p1:Point,p2:Point) -> Point:
    midP = Point(((p1.x+p2.x)/2),((p1.y+p2.y)/2))
    return midP

def printList(lis : list):
    for i in lis:
        print(i)

#used to calculate how many points in bfBezier
def pointCalculator(n: int) -> int:
    if(n==1):
        return 3
    else:
        return (pointCalculator(n-1)*2)-1
    