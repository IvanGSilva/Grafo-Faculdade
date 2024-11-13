from edge import Edge
from vertix import Vertix

class Graph:
  def __init__ ( self ) :
    self.arad = Vertix ('Arad')
    self.zerind = Vertix ('Zerind')
    self.oradea = Vertix ('Oradea')
    self.sibiu = Vertix ('Sibiu')
    self.timisoara = Vertix ('Timisoara')
    self.lugoj = Vertix ('Lugoj')
    self.mehadia = Vertix ('Mehadia')
    self.dobreta = Vertix ('Dobreta')
    self.craiova = Vertix ('Craiova')
    self.rimnicu = Vertix ('Rimnicu')
    self.fagaras = Vertix ('Fagaras')
    self.pitesti = Vertix ('Pitesti')
    self.bucharest = Vertix ('Bucharest')
    self.giurgiu = Vertix ('Giurgiu')
    self.eforie = Vertix('Eforie')
    self.hirsova = Vertix('Hirsova')
    self.iasi = Vertix('Iasi')
    self.neamt = Vertix('Neamt')
    self.urziceni = Vertix('Urziceni')
    self.vaslui = Vertix('Vaslui')

    self.arad.add_neighbor(Edge (self.zerind, 75))
    self.arad.add_neighbor(Edge (self.sibiu, 140))
    self.arad.add_neighbor(Edge (self.timisoara, 118))
    
    self.zerind.add_neighbor(Edge (self.arad, 75))
    self.zerind.add_neighbor(Edge (self.oradea, 71))
    
    self.oradea.add_neighbor(Edge (self.zerind, 71))
    self.oradea.add_neighbor(Edge (self.sibiu, 151))
    
    self.sibiu.add_neighbor(Edge (self.oradea, 151))
    self.sibiu.add_neighbor(Edge (self.arad, 140))
    self.sibiu.add_neighbor(Edge (self.fagaras, 99))
    self.sibiu.add_neighbor(Edge (self.rimnicu, 80))
    
    self.timisoara.add_neighbor(Edge (self.arad, 118))
    self.timisoara.add_neighbor(Edge (self.lugoj, 111))
    
    self.lugoj.add_neighbor(Edge (self.timisoara, 111))
    self.lugoj.add_neighbor(Edge (self.mehadia, 70))
    
    self.mehadia.add_neighbor(Edge (self.lugoj, 70))
    self.mehadia.add_neighbor(Edge (self.dobreta, 75))
    
    self.dobreta.add_neighbor(Edge (self.mehadia, 75))
    self.dobreta.add_neighbor(Edge (self.craiova, 120))
    
    self.craiova.add_neighbor(Edge (self.dobreta, 120))
    self.craiova.add_neighbor(Edge (self.pitesti, 138))
    
    self.pitesti.add_neighbor(Edge (self.craiova, 138))
    self.pitesti.add_neighbor(Edge (self.bucharest, 101))
    
    self.rimnicu.add_neighbor(Edge (self.sibiu, 80))
    self.rimnicu.add_neighbor(Edge (self.pitesti, 97))
    
    self.fagaras.add_neighbor(Edge (self.sibiu, 99))
    self.fagaras.add_neighbor(Edge (self.bucharest, 211))
    
    self.bucharest.add_neighbor(Edge (self.fagaras, 211))
    self.bucharest.add_neighbor(Edge (self.pitesti, 101))
    self.bucharest.add_neighbor(Edge (self.giurgiu, 90))
    
    self.giurgiu.add_neighbor(Edge (self.bucharest, 90))
    self.giurgiu.add_neighbor(Edge (self.urziceni, 87))
    
    self.urziceni.add_neighbor(Edge (self.hirsova, 98))
    self.urziceni.add_neighbor(Edge (self.vaslui, 142))
    self.urziceni.add_neighbor(Edge (self.giurgiu, 87))
    
    self.vaslui.add_neighbor(Edge (self.urziceni, 142))
    self.vaslui.add_neighbor(Edge (self.iasi, 92))
    
    self.iasi.add_neighbor(Edge (self.neamt, 87))
    self.iasi.add_neighbor(Edge (self.vaslui, 92))
    
    self.neamt.add_neighbor(Edge (self.iasi, 87))
    self.neamt.add_neighbor(Edge (self.eforie, 70))
    
    self.eforie.add_neighbor(Edge (self.hirsova, 86))
    self.eforie.add_neighbor(Edge (self.neamt, 70))
    
    self.hirsova.add_neighbor(Edge (self.urziceni, 98))
    self.hirsova.add_neighbor(Edge (self.eforie, 86))
    self.hirsova.add_neighbor(Edge (self.iasi, 92))
    