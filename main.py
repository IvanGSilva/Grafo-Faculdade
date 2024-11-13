from gbfSearch import GBFSearch
from graph import Graph
from dfs import Dfs
from bfs import Bfs


graph = Graph()
gbf_search = GBFSearch(graph)

dfsPath = Dfs(graph).dfs(graph.arad)

bfsPath = Bfs(graph).bfs(graph.arad)

print(dfsPath)
print("\n"
  "--------------------------------------------------------\n"
  "\n")
print(bfsPath)

print("\n"
  "--------------------------------------------------------\n"
  "\n")

start_vertex = graph.arad
goal_vertex = graph.bucharest

path = gbf_search.greedy_bfs(start_vertex, goal_vertex)

if path:
    print("Caminho encontrado:", path)
else:
    print("Objetivo não encontrado.")