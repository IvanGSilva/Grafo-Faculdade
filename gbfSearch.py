import heapq

class GBFSearch:

    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.path = []
        self.frontier = []

    def heuristic(self, start, goal):
        return abs(ord(start.name[0]) - ord(goal.name[0]))

    def greedy_bfs(self, start, goal):
        heapq.heappush(self.frontier, (0, start))

        while self.frontier:
            current_heuristic, current_node = heapq.heappop(self.frontier)

            if current_node == goal:
                self.path.append(current_node.name)
                return self.path

            if current_node not in self.visited:
                self.visited.append(current_node)
                self.path.append(current_node.name)

                for neighbor in current_node.get_neighbors():
                    if neighbor not in self.visited:
                        h = self.heuristic(neighbor, goal)
                        heapq.heappush(self.frontier, (h, neighbor))

        return None
