    class graph:
        # initialize graph
    def __init__(self, gdict=None):
            if gdict is None:
                gdict = dict()
            self.gdict = gdict
    
        # get edges
    def edges(self):
            return self.find_edges()
    
        # find edges
    def find_edges(self):
            edges = []
            for node in self.gdict:
                for nxNode in self.gdict[node]:
                    if {nxNode, node} not in edges:
                        edges.append({node, nxNode})
            return edges
    
        # Get verticies
    def get_vertices(self):
            return list(self.gdict.keys())
    
        # add vertix
    def add_vertix(self, node):
            if node not in self.gdict:
                self.gdict[node] = []
    
        # add edge
    def add_edge(self, node1, node2):
            # edge = set(edge)
            if node1 in self.gdict:
                self.gdict[node1].append(node2)
            else:
                self.gdict[node1] = [node2]
    
            if node2 in self.gdict:
                self.gdict[node2].append(node1)
            else:
                self.gdict[node2] = [node1]
    
    def dfsUtil(self, v, visit):
    
            visit[v] = True
            print(v)
    
            for i in self.gdict[v]:
                if visit[i] == False:
                    self.dfsUtil(i, visit)
            self.topsort.append(v)
    
            # dfs for graph
    
    def dfs(self):
            node_len = len(self.gdict)
            visit = [False] * (node_len)
            self.cnt, self.topsort = 0, []
    
            for i in range(node_len):
                if visit[i] == False:
                    self.dfsUtil(i, visit)
                    self.cnt += 1
    
    
def inp():
        return map(int, input().split())
    
    
    from copy import *
    
    n, m = inp()
    student = graph()
    for i in range(m):
        a, b = inp()
        student.add_edge(a, b)
    
    dic = deepcopy(student.gdict)
    for i, j in dic:
        l = len(j)
        if l > :
    
    print(student.gdict)