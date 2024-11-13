class Dfs:

  def __init__(self, graph):
    self.graph = graph
    self.visited = []
    self.path = []

  def dfs(self, start):
    
    self.visited.append(start)
    
    self.path.append(start.name)
    
    for neighbor in start.neighbors:
      if neighbor.vertex not in self.visited:
        self.dfs(neighbor.vertex)
    return self.path