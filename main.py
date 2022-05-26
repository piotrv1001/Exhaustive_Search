import test

if __name__ == "__main__":
 
    testInput = [("g4.txt", 4), ("g13.txt", 4), ("g13.txt", 9), ("g13.txt", 10), ("g13.txt", 11)]
    testInput = [("Lab6_files/" + filename, points) for (filename, points) in testInput]

    #test.testTSP_BF(testInput)
    
    test.testTSP_DP(testInput)