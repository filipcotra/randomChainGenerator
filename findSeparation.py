contactsByAASep = {};

def findSeparation(nodePar, particleSet):
    # Defining sets to contain particles with identified and unidentified
    # shortest paths from the starting node. Initially, all particles other
    # than the source node particle are in the unidentified set.
    visited_separation = {};
    unvisited_separation = {};
    # Populating the unidentified sets.
    for par in particleSet:
        unvisited_separation[par] = float('infinity');
    # Adding source node to visited dictionaries with separation 0;
    visited_separation[nodePar] = 0;
    unvisited_separation.pop(nodePar);
    # Implementing Dijkstra's algorithm to calculate separation. Starting at the
    # source node particle.
    currentNode = nodePar;
    while (len(unvisited_separation) != 0):
        currNeighbours = currentNode.getContacts();
        for neighbour in currNeighbours:
            if neighbour in visited_separation.keys():
                continue;
            # Reassigning tentative separation.
            currSeparation = visited_separation[currentNode];
            tentativeSeparation = currSeparation + 1;
            if tentativeSeparation < unvisited_separation[neighbour]:
                # If the new tentative separation is less than the assigned separation,
                # reassign the tentative separation in the dictionary. Because of how
                # this works, it will always be in the unvisited set - We are always
                # taking the shortest separation so tentativeDistance will never be smaller
                # than the separation in the dictionary for a visited node.
                unvisited_separation[neighbour] = tentativeSeparation;
        # Once we loop through all the neighbours, choose the closest unvisited particle
        # as the new current node. Then put it in the visited dictionary and remove it
        # from unvisited. If the smallest tentative separation in the unvisited set is
        # infinity, end the loop.
        sortedUnvisited = sorted(unvisited_separation, key = unvisited_separation.get, reverse = False);
        closestPar = sortedUnvisited[0];
        # Should never happen.
        if unvisited_separation[closestPar] == float('infinity'):
            break;
        currentNode = closestPar;
        visited_separation[currentNode] = unvisited_separation[currentNode];
        unvisited_separation.pop(currentNode);
    return visited_separation;