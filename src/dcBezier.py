from utils import *


def dcBezier(controlPoints : list[Point], desiredIteration : int,numofCP : int):
    result = [controlPoints[0]]
    dcBuilder(controlPoints,result,0,desiredIteration,numofCP)
    result.append(controlPoints[-1])
    return result


def dcBuilder(controlPoints:list[Point],container:list,counter:int, desiredIteration : int,numofCP:int):
    if(counter < desiredIteration):
        usefulMidpoints = [controlPoints[0],controlPoints[-1]]
        midPoint = makeMidPoint(controlPoints,numofCP,usefulMidpoints)
        quicksort(usefulMidpoints)
        leftPoints, rightPoints = split_array(usefulMidpoints,midPoint)
        leftPoints.append(midPoint)
        counter += 1
        dcBuilder(leftPoints,container,counter,desiredIteration,numofCP)
        container.append(midPoint)
        dcBuilder(rightPoints,container,counter,desiredIteration,numofCP)

def makeMidPoint(controlPoints:list[Point],numofCP:int,usefulMidpoints:list[Point]):
    if numofCP == 2:
        realMP = midPoint(controlPoints[0],controlPoints[1])
        usefulMidpoints.append(realMP)
        return realMP
    else:
        pointAntara = []
        for i in range(numofCP-1):
            pointAntara.append(midPoint(controlPoints[i],controlPoints[i+1]))
        usefulMidpoints.append(pointAntara[0])
        usefulMidpoints.append(pointAntara[-1])
        numofCP -= 1
        return makeMidPoint(pointAntara,numofCP,usefulMidpoints)

#ceritanya main
pointTest = [
    Point(0, 0),
    Point(1, 3),
    Point(4, 0),
    Point(7,6)
]
printList(dcBezier(pointTest,5,4))