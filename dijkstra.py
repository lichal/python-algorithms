import copy
########################################################
# @author Cheng Li
# @project Dijkstra's Algorithm
# @version April 12, 2018
########################################################

graphSet = {"A":[["B", 10], ["D", 5]], "B":[["A", 10], ["C", 5]], "C":[["B", 5], ["D", 15]], "D":[["C", 15], ["A", 5]]}

graphSet2 = {"A":[["B",10],["D",5]],"B":[["A",10],["C",5]],"C":[["B",5],["D",15]],"D":[["C",15],["A",5]],"E": [["F",5]],"F" : [["E",5]]}

not_connected = {"A" : [["B", 5], ["C", 5]], "B" : [["A", 5], ["C", 5]], "C" : [["B", 5], ["A", 15]], "D" : [["E", 5]], "E" : [["D",5]]}

joinSet = [["A", "B"], ["C"], ["D"], ["E", "F"]]

graphTest = {"A" : [["B", 10], ["D", 5]], "B" : [["A", 10], ["C", 5]], "C" : [["B", 5], ["D", 15]], "D" : [["C", 15], ["A", 5]]}

########################################################
# Return sum of all the edge-weights plus 1.
# This value would be the weight that can't never be 
# reached.
########################################################
def infty(graph):
    unsortList = []
    edgeList = []
    sum = 0

    ###############################################################
    # Loop the graph and store the weight and edge set into a list.
    # Then the list is store into another list call unsortList
    # The list is stored in the following format
    # [weight, vertexA, vertexB]
    # The purpose is that so the list can be sorted on weight.
    ###############################################################
    for vertex in graph:
        for sets in graph[vertex]:
            unsortList.append([sets[1], vertex, sets[0]])
        # Sort the list #
        unsortList.sort()
    
    ###############################################################
    # Remove the weight in the list of unsortList, and add the weight 
    # to the sum, and append the edge into edgeList. 
    ###############################################################
    for edge in unsortList:
        # Checks any duplication. #
        checkDuplicate = [edge[2], edge[1]]
        # If the edge is not in the edgelist yet, add its weight to sum
        # and add the edge to edgelist.
        if checkDuplicate not in edgeList:
            edgeList.append([edge[1],edge[2]])
            sum += edge[0]
    return sum + 1

########################################################
# Initialize the dijkstra graph, and return the inital
# graph.
########################################################
def initial(graph):
    initialGraph = {}
    inf = infty(graph)
    #Assumming root will always be "A" #
    initialGraph["A"] = 0
    for vertex in graph:
        # For everything other than "A", set the color to equal inf #
        if vertex != "A":
            initialGraph[vertex] = inf
    return initialGraph

########################################################
# Inputting a colored graph and a list of vertices.
# Return the vertex that has the smallest value in the
# coloring.
########################################################
def find_min(color, queue):
    # Sort the color list in non-decreasing order #
    sortedColor = []
    for vertex in color:
        sortedColor.append([color[vertex], vertex])
        # Sort the list 
        sortedColor.sort()
    # Find the first occurence of any vertex of queue in the color 
    # So this will return the vertex with smallest color.
    for vertex in sortedColor:
        if vertex[1] in queue:
            return vertex[1]

########################################################
# Returns a vertex-coloring by dijkstra's algorithm
########################################################
def dijkstra(graph):
    # Initialize the graph #
    dGraph = initial(graph)
    # Initialize position to be "A" as mentioned #
    position = "A"
    # A check list that will hold all the vertices in graph 
    # the list will be empty if all vertices are checked.
    checkList = []
    # Append all vertices into checklist #
    for vertex in graph:
        checkList.append(vertex)
    # Continue looping until all vertices check #
    while len(checkList) != 0:
        for connect in graph[position]:
            # Update if weight for a walk to the desired vertex is 
            # greater than the old walk.
            if dGraph[connect[0]] > connect[1] + dGraph[position]:
                dGraph[connect[0]] = connect[1] + dGraph[position]
        # Remove the checked vertex from check list #
        checkList.remove(position)
        # Update position to the next vertex that has the smallest
        # coloring in the check list
        position = find_min(dGraph, checkList)
    return dGraph 

########################################################
# Checks if the graph is connected or not.
########################################################
def is_connected(graph):
    # The weight it takes to walk through whole graph + 1 #
    outofbound = infty(graph)
    # Proper vertex coloring a graph with dijkstra #
    dGraph = dijkstra(graph)
    # If any of the coloring is same as out of bound, 
    # this means the group is not connected.
    # (Vertex cannot be reached)
    for vertex in dGraph:
        if dGraph[vertex] >= outofbound:
            return False
    return True

print()
print("Test infty")
print(infty(graphSet))

print()
print("Initial Graph")
print(initial(graphSet))

print()
print("find min")
print(find_min({"B" : 10, "C" : 10, "D" : 15, "A": 0}, ["A", "D"]))
print(find_min({"A" : 0, "B" : 10, "C" : 10, "D" : 15}, ["B", "C", "D"]))

print()
print("Test dijkstra")
print(dijkstra(graphSet))
print(dijkstra(graphSet2))

print()
print("Connection")
print(is_connected(graphSet))
print(is_connected(not_connected))






