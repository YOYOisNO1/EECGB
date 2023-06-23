def program3484():
    graph = {'A':[['B',2],['D',1]],
    		'B':[['A',2],['D',2]],
    		'C':[['D',3]],
    		'D':[['A',1],['B',2]]}
    connect_to = 'C'
    incoming_nodes = graph[connect_to]
    minimum_weight = [incoming_nodes
    print(incoming_nodes)