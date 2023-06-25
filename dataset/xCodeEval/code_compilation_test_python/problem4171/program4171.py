    n = int(input())
    
    like = dict((i, set()) for i in range(1, n + 1))
    dislike = dict((i, set()) for i in range(1, n + 1))
    
    k = int(input())
    for person1, person2 in (map(int, input().split()) for i in range(k)):
        like[person1].add(person2)
        like[person2].add(person1)
    
    m = int(input())
    for person1, person2 in (map(int, input().split()) for i in range(m)):
        dislike[person1].add(person2)
        dislike[person2].add(person1)
    
def find_solutions():
        for root in range(1, n + 1):
            graph_follow = set([root])
            graph = set()
            graph_likes = set()
            graph_dislikes = set()
    
            while graph_follow:
                for follow in graph_follow:
                    graph.add(follow)
                    graph_likes |= like[follow]
                    graph_dislikes |= dislike[follow]
                graph_follow = (graph_likes - graph_dislikes) - graph
    
            yield len(graph - graph_dislikes)
    
    print max(find_solutions())