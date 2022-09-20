# -*- coding: utf-8 -*-

# Imports
import json
import math


"""_summary_
Function for reading JSON file and converting string data to tupel
"""
def readGraphData(path):
    
    # read graph data from JSON
    file = open(path)
    data = json.load(file)
    file.close()
    
    # Read relevant data
    numberOfNodes = data["graph"]["nodesNumber"]
    numberOfEdges = data["graph"]["edgesNumber"]
    edges = data["graph"]["edges"]
    nodes = data["graph"]["properties"]["viewLayout"]["nodesValues"]
    
    nodeList = []
    
    # Convert node to tupel
    for i in range(len(nodes)):
        nodeList.append(tuple(map(float, nodes[str(i)].strip("()").split(','))))
    
    return edges, nodeList, numberOfEdges, numberOfNodes


"""_summary_
Calculates the distance between two nodes
"""
def calculateEdgeLength(node1, node2):
    return math.dist(node1._position, node2._position)


def findNodeById(id, nodeList):
    for node in nodeList:
        if (node._id == id):
            return node


"""_summary_
Function used to specific node object in node grid
"""
def findNodeByPosition(nodeList, x, y, z):
    for node in nodeList:
        if node._position[0] == x and node._position[1] == y and node._position[2] == z: 
            return node
        

def findConnection(startNode, endNode):
    for edge in startNode._nodeEdgeList:
        if (startNode._id == edge._start._id or startNode._id == edge._end._id) and (endNode._id == edge._start._id or endNode._id == edge._end._id):
            return edge
        

def findOtherEdgeEnd(node, edge):
    if (edge._start._id == node._id):
        return edge._end
    elif (edge._end._id == node._id):
        return edge._start


def calculatePressureDelta(node):
    delta = []
    
    for i in range(len(node._nextPressureVector)):
        if node._currentPressureVector[i] < node._nextPressureVector[i]:
            delta.append("-")
        elif node._currentPressureVector[i] > node._nextPressureVector[i]:
            delta.append("+")
        else:
            delta.append("=")
            
    return delta


def calculateConductivityDelta(edge):
    
    if edge._conductivity[1] < edge._conductivity[0]:
        return "-"
    elif edge._conductivity[1] > edge._conductivity[0]:
        return "+"
    else:
        return "="