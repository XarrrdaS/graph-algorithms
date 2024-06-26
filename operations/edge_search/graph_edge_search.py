def search_edges_1_matrix(graph, start, end):
    edges = []
    for i in range(start, end+1):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                edges.append((i, j))
    return edges

def search_edges_2_list(graph, start, end):
    edges = []
    for i in range(start, end+1):
        for j in graph[i]:
            edges.append((i, j))
    return edges

def search_edges_3_table(graph, start, end):
    edges = []
    for i in range(start, end+1):
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                edges.append((i, j))
    return edges

def search(graph, representation):
    print('\n| Where program should look for edges |\n')
    while True:
        try:
            start = int(input('From:\n> '))
            end = int(input('To:\n> '))
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

    if start >= len(graph) or end >= len(graph):
        print("\nStart or end index is out of bounds.")
    else:
        if representation == 1:
            edges = search_edges_1_matrix(graph, start-1, end-1)
        elif representation == 2:
            edges = search_edges_2_list(graph, start-1, end-1)
        elif representation == 3:
            edges = search_edges_3_table(graph, start-1, end-1)
            
        if edges:
            print("\nEdge exists in the graph.")
        else:
            print("\nEdge does not exist in the graph.")