    import math
    
    sqrt = lambda s:s**0.5
    pi = math.pi
    
def distance(p1, p2):
    	(x1,y1) = p1
    	(x2,y2) = p2
    	return sqrt((x1-x2)**2 + (y1-y2)**2)
    	
def all_distances(p1, p2, p3):
    	return [distance(p,q) for p, q in [(p1,p2), (p2, p3), (p3, p1)]]
    	
def triangle_area(p1, p2, p3):
    	d1, d2, d3 = all_distances(p1, p2, p3)
    	s = (d1+d2+d3)/2 
    	area_sq = s*(s-d1)*(s-d2)*(s-d3)
    	return sqrt(area_sq)
    
def circle_radius(p1, p2, p3):
    	d1, d2, d3 = all_distances(p1, p2, p3)
    	area = triangle_area(p1, p2, p3)
    	return d1*d2*d3/(4*area)
    
def circle_fraction(p1, p2, r):
    	d = distance(p1, p2)
    	ratio = (d/2)/r
    	ratio = min(ratio,1)
    	ratio = max(ratio,-1)
    	# print(ratio)
    	angle = 2 * math.asin (ratio)
    	fraction = angle / (2*pi)
    	return fraction
    
def is_near_integer(x):
    	return abs(round(x)-x) < 1e-5
    
def smallest_denominator(frac1, frac2):
    	for denom in range(1,101):
    		num1 = denom * frac1
    		num2 = denom * frac2
    		if is_near_integer(num1) and is_near_integer(num2):
    			return denom
    	# print("No denom", frac1, frac2)
    
def smallest_num_sides(p1, p2, p3):
    	r = circle_radius(p1, p2, p3)
    	frac1 = circle_fraction(p1, p2, r)
    	frac2 = circle_fraction(p1, p3, r)
    	denom = smallest_denominator(frac1, frac2)
    	return denom
    
def polygon_area(num_sides, radius):
    	n = num_sides
    	r = radius
    	slice_sin = math.sin(2*pi/n)
    	return 1/2 * n * r * r * slice_sin
    
def smallest_polygon_area(p1, p2, p3):
    	n = smallest_num_sides(p1, p2, p3)
    	r = circle_radius(p1, p2, p3)
    	return polygon_area(n, r)
    
    f = smallest_polygon_area
    
    points = [(1,0), (0,0), (0,1)]
    
def string_to_tuple(s):
    	return tuple(map(eval,s.split()))
    
def read_tuple():
    	s=input()
    	return string_to_tuple(s)
    	
    p1=read_tuple()
    p2=read_tuple()
    p3=read_tuple()
    
    result = smallest_polygon_area(p1, p2, p3)
    print(result)
    
    # p1 = read_tuple()
    # print(p1)
    # print(smallest_num_sides(*points))
    
    # print(polygon_area(100, 1))
    
    # print( circle_fraction((1,0),(0,0),sqrt(2)/2))
    
    # print(smallest_denominator(2/5,1/3))