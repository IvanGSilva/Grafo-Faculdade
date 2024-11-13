import heapq

class AStar:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.path = []
        self.frontier = []

    def heuristic(self, start, goal):
        return abs(ord(start.name[0]) - ord(goal.name[0]))

    def a_star(self, start, goal):
        heapq.heappush(self.frontier, (0 + self.heuristic(start, goal), 0, start))
        g_costs = {start: 0}
        parent_map = {start: None}

        while self.frontier:
            _, g, current_node = heapq.heappop(self.frontier)
            print(f"Explorando: {current_node.name} com "
                  f"f(n) = {g + self.heuristic(current_node, goal)}")
            if current_node == goal:
                while current_node:
                    self.path.insert(0, current_node.name)
                    current_node = parent_map[current_node]
                return self.path

            for neighbor in current_node.get_neighbors():
                if neighbor not in self.visited:
                    tentative_g = g + self.get_edge_weight(current_node, neighbor)

                    if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                        g_costs[neighbor] = tentative_g
                        f_cost = tentative_g + self.heuristic(neighbor, goal)

                        heapq.heappush(self.frontier, (f_cost, tentative_g, neighbor))

                        parent_map[neighbor] = current_node

            self.visited.append(current_node)

        return None

    def get_edge_weight(self, from_vertex, to_vertex):
        for edge in from_vertex.neighbors:
            if edge.vertex == to_vertex:
                return edge.weight
        return float('inf')
