class Bfs:
  def __init__(self, graph):
      self.graph = graph
      self.visited = []
      self.path = []

  def bfs(self, start):
      queue = [start]
      self.visited.append(start)

      while queue:
          node = queue.pop(0)
          self.path.append(node.name)

          for neighbor in node.get_neighbors():
              if neighbor not in self.visited:
                  self.visited.append(neighbor)
                  queue.append(neighbor)

      return self.path
