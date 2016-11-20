import math

class points_in_space:
    def __init__(self, lat = 0, lon = 0):
        self.lat, self.lon  = lat, lon
       
class two_points:
    def __init__(self, a, b):
        self.a, self.b = a, b
    def dist(a, b):
        return math.sqrt(((a.lat - b.lat)**2)*(a.lon - b.lon)**2)     

point_a = points_in_space(6.0, 7.5) 
point_b = points_in_space(2.4, 16.3)


points_list = two_points(point_a, point_b)

#def dist(a, b):
    #return math.sqrt(((a.lat - b.lat)**2)*(a.lon - b.lon)**2)

print points_list.dist