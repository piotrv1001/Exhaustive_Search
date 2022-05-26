def fileToGraph(filename):

    with open(filename, 'r') as f:

        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

        data = [line.split() for line in lines]

        nodes = int(data[0][0])
        
        output = [[int(x) for x in line] for line in data[1:]]

        return (output, nodes)