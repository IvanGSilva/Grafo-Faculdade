class Vertix:

  def __init__(self, name):
    self.name = name
    self.visited = False
    self.neighbors = []

  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)

  def display_neighbors(self):
    for neighbor in self.neighbors:
      print(neighbor.name, neighbor.weight)

  def get_neighbors(self):
    return [edge.vertex for edge in self.neighbors]
