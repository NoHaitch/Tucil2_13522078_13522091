class Point:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self,otherPoint) -> bool:
        return (self.x == otherPoint.x) and (self.y==otherPoint.y)