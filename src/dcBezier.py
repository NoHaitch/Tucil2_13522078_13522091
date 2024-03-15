from classes import *
from utils import *

#dc = divide and conquer
#sp = start point, mp : middle point, ep = end point, ip = inner point
def dcBezier(sp: Point, mp: Point, ep:Point,desiredIteration : int):
    result = []
    dcBuilder(sp,mp,ep,result,0,desiredIteration)
    return result


def dcBuilder(sp:Point,ip:Point,ep:Point,container:list,counter:int, desiredIteration : int):
    if(counter < desiredIteration):
        mp1 = midPoint(sp,ip)
        mp2 = midPoint(ip,ep)
        mp3 = midPoint(mp1,mp2)
        counter += 1
        dcBuilder(sp,mp1,mp3,container,counter,desiredIteration)
        container.append(mp3)
        dcBuilder(mp3,mp2,ep,container,counter,desiredIteration)

#main ceritanya
p1 = Point(0,0)
p2 = Point(4,10)
p3 = Point(8,0)
test = dcBezier(p1,p2,p3,5)
printList(test)