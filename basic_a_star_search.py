class Graph:
    def __init__(self, adjacency_list, heuristic_list):
        self.adjacency_list = adjacency_list
        self.heuristic_list = heuristic_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def get_heuristic(self, n):
        return self.heuristic_list[n]

    def algorithm(self, start, stop):
        open_list = set(start)
        closed_list = set()

        distance = {}
        distance[start] = 0

        mapping = {}
        mapping[start] = start

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or distance[v] + self.get_heuristic(v) < distance[n] + self.get_heuristic(n):
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop:
                reconstruct_path = []

                while mapping[n] != n:
                    reconstruct_path.append(n)
                    n = mapping[n]

                reconstruct_path.append(start)

                reconstruct_path.reverse()

                print('Path found: {}'.format(reconstruct_path))
                return reconstruct_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    mapping[m] = n
                    distance[m] = distance[n] + weight

                else:
                    if distance[m] > distance[n] + weight:
                        distance[m] = distance[n] + weight
                        mapping[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


def main():
    node_list = []
    adjacency_list = {}
    heuristic_list = {}

    number_of_nodes = int(input("Number of Nodes (INT) >> "))
    print("-------------------------------------------------")

    i = 0
    while i < number_of_nodes:
        node = input("Node %d (CHAR) >> " % (i+1))
        node_list.append(node)

        manhattan_heuristic = int(input("Heuristic Value of %c (INT) >> " % node))
        heuristic_list[node] = manhattan_heuristic

        number_of_neighbors = int(input("Number of Neighbors %c (INT) >> " % node))

        j = 0
        neighbor_list = []

        while j < number_of_neighbors:
            n_cost = []

            print("Details of Neighbor %d of Node %c" % (j+1, node))
            neighbor = input("Neighbor (CHAR) >> ")
            cost = int(input("Cost (INT) >> "))

            n_cost.append(neighbor)
            n_cost.append(cost)
            neighbor_list.append(n_cost)
            j += 1

        adjacency_list[node] = neighbor_list
        i += 1
        print("-------------------------------------------------")

    i = 0
    print("This is your Adjacency List:")
    print("{")
    while i < number_of_nodes:
        print("   '%c': " % node_list[i], end='')
        print(adjacency_list[node_list[i]])
        i += 1
    print("}")
    print("-------------------------------------------------")

    i = 0
    print("This is your Heuristic Value List:")
    print("{")
    while i < number_of_nodes:
        print("   '%c': " % node_list[i], end='')
        print(heuristic_list[node_list[i]])
        i += 1
    print("}")
    print("-------------------------------------------------")

    a_star = Graph(adjacency_list, heuristic_list)

    source = input("Source >> ")
    destination = input("Destination >> ")

    result = a_star.algorithm(source, destination)
    print("-------------------------------------------------")

    if result is not None:
        i = 0
        total_cost = 0
        print("This is your Traversed Path Cost:")
        print("{")
        while result[i] != destination:
            if result[i] in adjacency_list.keys():
                j = 0

                while j < len(adjacency_list[result[i]]):
                    if result[i+1] == adjacency_list[result[i]][j][0]:
                        total_cost += adjacency_list[result[i]][j][1]
                        print("   '%c to %c': %d" % (result[i], result[i+1], adjacency_list[result[i]][j][1]))
                        break
                    j += 1
            i += 1
        print("}")
        print("So, the minimum cost from Node %c to Node %c is %d." % (result[0], result[len(result)-1], total_cost))


main()
