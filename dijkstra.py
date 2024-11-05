graph = {
    'a':{'b':3, 'c':4, 'd':7},
    'b':{'c':1, 'f':5},
    'c':{'f':6, 'd':2},
    'd':{'e':3, 'g':6},
    'e':{'g':3, 'h':4},
    'f':{'e':1, 'h':8},
    'g':{'h':2},
    'h':{'g':2}
}

def dijkstra(graph, start, goal):
    shortest_distance = {}  #records the cost to reach to that node. Going to be updated as we move along the graph
    track_predecessor = {}  #keep track of the path that has lead us to this node
    unseenNodes = graph  # to iterate through the entire graph
    infinity = 9999999 #infinity can basically be considered a very large number
    path = [ ] #going to trace out journey back to the source node optimal route

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node



