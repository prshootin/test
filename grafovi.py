# ALGORITMI

def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend([i for i in graph[vertex] if i not in visited])
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend([i for i in graph[vertex] if i not in list(visited)])

    return visited


def get_Susjed(m, node):
    susjedi = []
    
    for ix, dist in enumerate(m[node]):
        if dist != 0:
            susjedi.append(ix)
    
    return susjedi

def dijkstra(matrica, pocetniCvor):
    not_visited = [x for x in range(0, len(matrica))]
    shortest_paths = {}
    prev_nodes = {}
    for node in not_visited:
        shortest_paths[node] = float("inf")
    shortest_paths[pocetniCvor] = 0
    while not_visited:
        curr_node = None
        for node in not_visited:
            if curr_node == None:
                curr_node = node
            elif shortest_paths[node] < shortest_paths[curr_node]:
                curr_node = node

        susjedi = get_Susjed(matrica, curr_node)

        for h in susjedi:
            temp = shortest_paths[curr_node] + matrica[curr_node][h]
            if temp < shortest_paths[h]:
                shortest_paths[h] = temp
        not_visited.remove(curr_node)

    return shortest_paths


def top_sort(g):
    visited = set()
    stack = []
    for vertex in g:
        if vertex not in visited:
            dfs(g, vertex, visited, stack)
    print(stack[::-1])


def floyd_warshall(G):
    udaljenost = list(map(lambda i: list(map(lambda j: j, i)), G))


    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                udaljenost[i][j] = min(udaljenost[i][j], udaljenost[i][k] + udaljenost[k][j])

