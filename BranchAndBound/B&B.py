import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy


class Node: # Create Node class
    def __init__(self, current, cost):
        self.current = current
        self.cost = cost


def redu(matrix): #Redux function 
    rowMin = np.amin(matrix, axis=1)
    rowMin[rowMin == infinite] = 0  #Determine the minium value of rows

    for i in range(COL):
        matrix[i, :] = np.subtract(
            matrix[i][:], rowMin[i])

    colMin = np.amin(matrix, axis=0)
    colMin[colMin == infinite] = 0  #Determine the minium value of columns

    for i in range(COL):
        matrix[:, i] = np.subtract(
            matrix[:, i], colMin[i])

    return rowMin, colMin


def BnB(adjList, visited):  #Create Breach and bound function 
    cont = 0
    for i in range(COL):
        if(((adjList[:, i] == 0).any() or (adjList[:, i] == infinite).all()) and ((adjList[i, :] == 0).any() or (adjList[i, :] == infinite).all())): #consult if exist a infinite value
            cont += 1
    if(cont == COL):
        return True
    else:
        return False


def bestN(matrix):  #Create the bestN fuction
    bestFn = 0
    ind = 0
    firstIt = True
    for node in matrix.values():
        if firstIt or node.cost < bestFn:
            ind += 1
            firstIt = False
            best = node
            bestFn = best.cost
    return best, ind


def printPath(visited): #Print function 
    path = []
    label = []
    for i in range(COL):
        path.append(visited[i])
    path.reverse()

    for i in range(len(path)):
        if path[i] == 0:
            label.append('A')#name the node A
        elif path[i] == 1:
            label.append('B')#name the node B
        elif path[i] == 2:
            label.append('C')#name the node C
        elif path[i] == 3:
            label.append('D')#name the node D
        elif path[i] == 4:
            label.append('E')#name the node E
    return label


def main(start):  #main

    matrix = {str(start): Node(start, 0)}
    first = True 
    bestList = []
    visited = np.array([0, 0, 0, 0]) #temporal matrix
    nodesL = [0, 1, 2, 3, 4]  #nodes of the matrix
    while True: #Meanwhile is the first node do:

        bestNode = bestN(matrix) #Call BestN function to extract the best Node
        minMax = redu(bestNode[0].current)#Declare the best node as the minmax to use the redux function
        if(first):
            b = np.sum(minMax[0] + minMax[1])
            index = 0
        else:
            b = bestNode[0].cost
            for i in range(len(bestList)):
                if (bestList[i].cost == bestNode[0].cost):
                    index = i

        visited = np.insert(visited, 0, nodesL[index])
        nodesL = (list(set(nodesL) - set(visited)))
        if(not nodesL):
            path = printPath(visited)
            return path   #Print path
        bestList = []
        for j in range(len(nodesL)):
            adjList = deepcopy(bestNode[0].current)
            adjList[visited[0], :] = infinite
            adjList[:, nodesL[j]] = infinite
            adjList[nodesL[j]][visited[0]] = infinite
            adjList[nodesL[j]][visited[1]] = infinite
            reduced = BnB(adjList, visited)

            if(reduced == True):
                cost = bestNode[0].current[visited[0]][nodesL[j]] + b
                bestList.append(
                    Node(adjList, cost, ))

            else:
                minMax = redu(adjList)
                bG = np.sum(minMax[0] + minMax[1])
                cost = bestNode[0].current[visited[0]][nodesL[j]] + b + bG
                bestList.append(
                    Node(adjList, cost))
        matrix = {}
        for bestL in bestList:
            matrix[str(bestL.current)] = bestL
        first = False


if __name__ == '__main__':

    G = nx.Graph()  #Create the graph
#ADD edges on graph
    G.add_edge("A", "B")
    G.add_edge("A", "C")
    G.add_edge("A", "D")
    G.add_edge("A", "E")
    G.add_edge("B", "C")
    G.add_edge("B", "D")
    G.add_edge("B", "E")
    G.add_edge("C", "D")
    G.add_edge("C", "E")
    G.add_edge("D", "E")
    G.add_edge("E", "D")
#Declare the position 
    pos = {'A': (1, 5), 'B': (3, 5), 'C': (0, 2), 'D': (4, 2), 'E': (2, 0)}
#Matrix 
    infinite = np.inf
    COL = 5
    ROW = 5
    refAdjList = np.array([[infinite, 20, 30, 10, 11],
                           [15, infinite, 16, 4, 2],
                           [3, 5, infinite, 2, 4],
                           [19, 6, 18, infinite, 3],
                           [16, 4, 7, 16, infinite]])

    path = main(refAdjList)

    esmall = []
    for i in range(len(path)-1):
        esmall.append((path[i], path[i+1]))

    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, width=6)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=10, alpha=0.9, edge_color="r", style="dashed"
    )

    # labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    plt.axis("off")
    plt.show()
