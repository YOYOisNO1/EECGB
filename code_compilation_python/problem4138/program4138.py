    import io
    import sys
    import math
    
    
def rlist(t):
        return map(t, input().split())
    
    
def read_int_list():
        return rlist(int)
    
    
def write_list(lst, divider=" "):
        print divider.join(map(str, lst))
    
    
    class Graph(object):
    def __init__(self, vertices, edges):
            self.neighbours = [set() for _ in xrange(vertices)]
            self.size = vertices
            self.density = edges
            for _ in xrange(edges):
                v, u = read_int_list()
                self.neighbours[v-1].add(u-1)
                self.neighbours[u-1].add(v-1)
    
    def connected(self, vertex1, vertex2):
            return vertex2 in self.neighbours[vertex1]
    
        # True if vertex_set forms a full subgraph
    def check_full(self, vertex_set):
            for vertex1, vertex2 in vertex_set:
                if not self.connected(vertex1, vertex2):
                    return False
            return True
    
        # True if no edges between 2 sets
    def check_no_edges(self, set1, set2):
            for vertex1 in set1:
                for vertex2 in set2:
                    if self.connected(vertex1, vertex2):
                        return False
            return True
    
    def vertices_of_degree(self, degree):
            first_bad = -1
            ans = set()
            for i, vertex in enumerate(self.neighbours):
                if len(vertex) == degree:
                    ans.add(i)
                else:
                    first_bad = i
            return first_bad, ans
    
    n, m = read_int_list()
    graph = Graph(n, m)
    a_vertex, b_vertices = graph.vertices_of_degree(n-1)
    if a_vertex == -1:
        print "Yes"
        print "b"*n
    else:
        ab_vertices = graph.neighbours[a_vertex]
        ab_vertices.add(a_vertex)
        c_vertices = set(xrange(n))-ab_vertices
        a_vertices = ab_vertices - b_vertices
        if graph.check_full(a_vertices) and graph.check_full(c_vertices)\
                and graph.check_no_edges(a_vertices, c_vertices):
            print "Yes"
            ans = ""
            for i in xrange(n):
                if i in b_vertices:
                    ans += 'b'
                elif i in a_vertices:
                    ans += 'a'
                else:
                    ans += 'c'
            print ans
        else:
            print "No"