from gbfSearch import GBFSearch
from aStar import AStar
from graph import Graph
from dfs import Dfs
from bfs import Bfs


graph = Graph()
gbf_search = GBFSearch(graph)
a_star_search = AStar(graph)

dfsPath = Dfs(graph).dfs(graph.arad)

bfsPath = Bfs(graph).bfs(graph.arad)

print("Depth Firist Search",dfsPath)
print("\n"
  "--------------------------------------------------------\n"
  "\n")

print("Bredth Firist Path",bfsPath)
print("\n"
  "--------------------------------------------------------\n"
  "\n")

start_vertex = graph.arad
goal_vertex = graph.bucharest

path = gbf_search.greedy_bfs(start_vertex, goal_vertex)

if path:
    print("Caminho encontrado por Greedy-Best-Firist-Search:", path)
else:
    print("Objetivo não encontrado.")

print("\n"
  "--------------------------------------------------------\n"
  "\n")

path = a_star_search.a_star(start_vertex, goal_vertex)

if path:
    print("Caminho encontrado por A-Star:", path)
else:
    print("Objetivo não encontrado.")