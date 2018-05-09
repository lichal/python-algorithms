import copy

########################################################
# @author Cheng Li
# @project Spanning Trees
# @version April 12, 2018
########################################################

graphSet = {"A":[["B", 10], ["D", 5]], "B":[["A", 10], ["C", 5]], "C":[["B", 5], ["D", 15]], "D":[["C", 15], ["A", 5]]}

joinSet = [["A", "B"], ["C"], ["D"], ["E", "F"]]

graphTest = {"A" : [["B", 10], ["D", 5]], "B" : [["A", 10], ["C", 5]], "C" : [["B", 5], ["D", 15]], "D" : [["C", 15], ["A", 5]]}


########################################################
# Return a list of edges, in non-decreasing order.
########################################################
def edge_get(graph):
    unsortList = []
    edgeList = []
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
    # Remove the weight in the list of unsortList, and add it to
    # edgeList. 
    ###############################################################
    for edge in unsortList:
        # Checks any duplication. #
        checkDuplicate = [edge[2], edge[1]]
        if checkDuplicate not in edgeList:
            edgeList.append([edge[1],edge[2]])
    return edgeList

########################################################
# Takes in a list of sublists, and two vertex.
# Returns a list with the sublist combine.
########################################################
def list_join(lst, elt1, elt2):
    tempList = []
    # Loop the list #
    for item in lst:
        # Loop the lst again to find the sublist containing elt2 #
        for item2 in lst:
            # Onlt append if elt2 is not in the same sublist with elt1 #
            if elt2 in item2 and elt1 not in item2 and elt1 in item:
                tempList.append(item + item2)
        # Store the sub-list that don't need to merge into tempList #
        if elt1 not in item and elt2 not in item:
            tempList.append(item)
    return tempList

########################################################
# Takes in a graph to perform Kruskal's minimum spanning tree
# Return the spanning tree.
########################################################
def min_kruskal(graph):
    # Obtain all the edges of the graph, in non-decreasing order #
    sortedEdge = edge_get(graph)
    # Holds the spanning tree #
    tree = []
    # Holds a list of tree need to be connected #
    connection = []
    # First find the what vertex is in the graph that needs to be connected #
    for vertex in graph:
        connection.append([vertex])

    for edge in sortedEdge:
        # Place the edge into tree if its not in the tree already #
        if edge not in tree:
            connection = list_join(connection, edge[0], edge[1])
            tree.append(edge)
        # End the loop if all vertices are connected 
        # Since the Edge sets are in non-decreasing order, as long 
        # all vertices are connected the spanning tree is form.
        if len(connection) == 1:
            break
    return tree

########################################################
# Takes in a graph to perform Prim's minimum spanning tree
# Return the spanning tree. The algorithm will be perform
# assuming vertex "A" as the root.
########################################################
def min_prim(graph):
    # Obtain all the edges of the graph, in non-decreasing order #
    sortedEdge = edge_get(graph)
    # Holds the spanning tree #
    tree = []
    # Holds a list of tree need to be connected #
    connection = []
    # First find the what vertex is in the graph that needs to be connected #
    for vertex in graph:
        connection.append([vertex])
    # Find the first occurence of "A" in the edge.
    # It will be the first edge on the spanning tree
    for edge in sortedEdge:
        if "A" in edge:
            tree.append(edge)
            connection = list_join(connection, edge[0], edge[1])
            break
    # Number of possible edges #
    size = len(sortedEdge)
    count = 0
    # Loop to get edge #
    while count < size:
        edge = sortedEdge[count]
        # Append the edge into our tree only if one of it's vertex
        # is already added to the tree.
        # Also restart the count so we can search the who edge set again
        for vertex in connection[0]:
            # Ignore duplication of edges in the tree #
            if vertex in edge and edge not in tree:
                tree.append(edge)
                connection = list_join(connection, edge[0], edge[1])
                count = 0
        count += 1
        # If all vertices are connected, done. #
        if len(connection) == 1:
            break
    return tree

print()
print("Test edge_get")
print(edge_get(graphSet))
print()
print("Test list_join")
print(list_join(joinSet, "A", "E"))

print()
print("Test kruskal's spanning tree")
print(min_kruskal(graphTest))

print()
print("Test Prim's Spanning Tree")
print(min_prim(graphTest))


