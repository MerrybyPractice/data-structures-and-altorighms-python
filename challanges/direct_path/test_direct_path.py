import pytest 
from data_structures.graph.graph import Graph
from challanges.direct_path.direct_path import direct_path

@pytest.fixture
def path_map(): 
  g = Graph()
  print(type(path_map.g))

  a = g.add_vertex('a')
  b = g.add_vertex("b")
  c = g.add_vertex("c")
  d = g.add_vertex("d")
  e = g.add_vertex("e") 
  f = g.add_vertex("f")

  g.add_edge(a, c, 1) 
  g.add_edge(c, a, 1)

  g.add_edge(b, c, 2) 
  g.add_edge(c, b, 2)

  g.add_edge(b, e, 3) 
  g.add_edge(e, b, 3)

  g.add_edge(c, d, 5)
  g.add_edge(d, c, 5) 

  g.add_edge(d, e, 4)
  g.add_edge(e, d, 4)

def test_direct_path(path_map): 

  lst = ['c', 'b', 'e']
  
  assert direct_path(grph, lst) == [True, 5]