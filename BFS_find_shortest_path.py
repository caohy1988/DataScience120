# BFS to Count the Shortest Path in Graph
# Author: Haiyuan Cao
# Date: Oct. 5, 2016

import Queue
from collections import defaultdict
def bfs(graph, start):
    visited = set()
    queue = Queue.Queue()
    queue.put(start)
    cost = list()
    while not queue.empty():
        connected = list()
        current = queue.get(0)
        if isinstance(current, list) and len(current) > 0:
            current = current[0]
            if graph.has_key(current):
                connected = graph[current]
        else:
            if graph.has_key(current):
                connected = graph[current]
        if len(connected) > 0:
            if isinstance(connected, list):
                for each in connected:
                    if each != start and each not in visited:
                        visited.add(each)
                        queue.put(each)
                        cost[each] = cost[current] + 1
                    else:
                        if each != start and each not in visited:
                            visited.add(each)
                            queue.put(each)
                            cost[each] = cost[current] + 1
    return cost
