    import math
    import sys
    
    class Coordinate:
    
  def __init__(self, x, y):
        self.x = x
        self.y = y
    
  def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)
    
  def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    class Polygon:
    
  def __init__(self, vertices):
        self.vertices = vertices # Tuple of Coordinate objects
    
  def point_in_polygon(self, point, count_border):
        """
        Takes in a Coordinate and returns True if this point is within this
        polygon, False otherwise. The count_border flag indicates whether we count the
        point inside the polygon if it is on the border.
        Taken from
        http://stackoverflow.com/questions/217578/point-in-polygon-aka-hit-test
        """
        if count_border:
          edges = self.get_edges()
          for e in edges:
            if point_on_line_segment(e[0], e[1], point):
              return True
        j = len(self.vertices) - 1
        c = False
        for i in range(len(self.vertices)):
          if ( ((self.vertices[i].y > point.y) != (self.vertices[j].y > point.y)) \
              and (point.x < (self.vertices[j].x - self.vertices[i].x) * \
              (point.y - self.vertices[i].y) / (self.vertices[j].y - \
              self.vertices[i].y) + self.vertices[i].x) ):
            c = not c
          j = i
    
        return c
    
  def get_edges(self):
        return [(self.vertices[0], self.vertices[1]),
                (self.vertices[1], self.vertices[2]),
                (self.vertices[2], self.vertices[3]),
                (self.vertices[3], self.vertices[0])]
    
    
def ccw(a, b, c):
      return (c.y-a.y) * (b.x-a.x) > (b.y-a.y) * (c.x-a.x)
    
def line_intersection(a, b, c, d):
      return ccw(a,c,d) != ccw(b,c,d) and ccw(a,b,c) != ccw(a,b,d)
    
    
def point_on_line_segment(a, b, c):
      """
      a and b are Coordinates defining the line segment, c is the point to be
      tested, returns True if c is on the line segment.
      Taken from
      http://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
      """
      epsilon = .0000001
      cross_product = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)
      if abs(cross_product) > epsilon:
        return False   # (or != 0 if using integers)
    
      dot_product = (c.x - a.x) * (b.x - a.x) + (c.y - a.y)*(b.y - a.y)
      if dot_product < 0:
        return False
    
      squared_length_ba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
      if dot_product > squared_length_ba:
        return False
    
      return True
    
    
    coords = map(int, input().split())
    a = Coordinate(coords[0], coords[1])
    b = Coordinate(coords[2], coords[3])
    c = Coordinate(coords[4], coords[5])
    d = Coordinate(coords[6], coords[7])
    square_a = Polygon((a, b, c, d))
    
    coords = map(int, input().split())
    e = Coordinate(coords[0], coords[1])
    f = Coordinate(coords[2], coords[3])
    g = Coordinate(coords[4], coords[5])
    h = Coordinate(coords[6], coords[7])
    
    square_b = Polygon((e, f, g, h))
    for p in square_a.vertices:
      if square_b.point_in_polygon(p, True):
        print("YES")
        sys.exit(0)
    for p in square_b.vertices:
      if square_a.point_in_polygon(p, True):
        print("YES")
        sys.exit(0)
    
    for i in range(len(square_a.vertices)):
      for j in range(len(square_b.vertices)):
        if square_a.vertices[i] == square_b.vertices[j]:
          print("YES")
          sys.exit(0)
        if line_intersection(square_a.vertices[i], square_a.vertices[(i + 1) % 4],
            square_b.vertices[j], square_b.vertices[(j + 1) % 4]):
          print("YES")
          sys.exit(0)
    print("NO")