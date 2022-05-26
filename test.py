import TSP_BF
import TSP_DP
import fileHandler
import time
import numpy as np

def testTSP_BF(inputFiles):

    for pair in inputFiles:

        startTime = time.time()

        filename = pair[0]
        points = pair[1]

        graphInput = fileHandler.fileToGraph(filename)
        graph = graphInput[0]
        graph = graph[:points]
        #V = graphInput[1]
        V = points
        s = 0
        shortest_dist = TSP_BF.TSP_BF(graph, s, V)[0]
        shortest_sequence = TSP_BF.TSP_BF(graph,s, V)[1]
        shortest_dist_str = TSP_BF.printShortestPath(shortest_sequence, s)

        legitFilename = filename.replace("Lab6_files/", "")
        print(legitFilename + ", Points: " + str(points))
        print("Shortest distance: " + str(shortest_dist))
        print("Shortest path: " + shortest_dist_str)
        print("Execution time: ", end = "")
        executionTime = (time.time() - startTime) * 1000
        if executionTime > 1000:
            executionTime = executionTime / 1000
            print("{0:.2f} s".format(executionTime))
        else:
            print("{0:.2f} ms".format(executionTime))

        print()

def testTSP_DP(inputFiles):

    for pair in inputFiles:

        startTime = time.time()

        filename = pair[0]
        points = pair[1]

        graphInput = fileHandler.fileToGraph(filename)
        graph = graphInput[0]
        graph = graph[:points]
        #V = graphInput[1]
        #V = points
        #s = 0

        shortestPath, shortestDistance = TSP_DP.DP_TSP(graph)
        shortestPath = [x + 1 for x in shortestPath]
        shortestPath = ','.join([str(x) for x in shortestPath])

        legitFilename = filename.replace("Lab6_files/", "")
        print(legitFilename + ", Points: " + str(points))
        print("Shortest distance: ", str(shortestDistance))
        print("Shortest path: ", shortestPath)
        print("Execution time: ", end = "")
        executionTime = (time.time() - startTime) * 1000
        if executionTime > 1000:
            executionTime = executionTime / 1000
            print("{0:.2f} s".format(executionTime))
        else:
            print("{0:.2f} ms".format(executionTime))

        print()