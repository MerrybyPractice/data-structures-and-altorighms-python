from data_structures.graph.graph import Graph, Vertex
import pytest

def test_graph_exsits(): 
  assert Graph
  assert Vertex

def test_add_single_vertex(): 
  g = Graph()
  one = g.add_vertex('1')

  assert isinstance(one, Vertex) 
  assert one.value == '1'

def test_add_many_vertices(): 
  g = Graph() 
  one = g.add_vertex('1') 
  two = g.add_vertex('2')
  three = g.add_vertex('3') 

  assert one.value == '1'
  assert two.value == '2' 
  assert three.value == '3'

def test_get_single(): 
  g = Graph()
  one = g.add_vertex('1')
  vertex = g.get_vertices() 
  assert len(vertex) == 1
  assert [vert.value for vert in vertex] == ['1']

def test_get_multiple(): 
  g = Graph() 
  g.add_vertex('1')
  g.add_vertex('2')
  g.add_vertex('3')

  vertices = g.get_vertices()
  assert len(vertices) == 3
  assert {vert.value for vert in vertices} == set(['1','2','3'])  

def test_len(): 
  g = Graph()

  g.add_vertex('1')
  g.add_vertex('2')

  assert len(g) == 2

def test_empty(): 
  g = Graph()

  assert g.get_vertices() == None

def test_add_edge(): 
  g = Graph() 

  one = g.add_vertex('1')
  two = g.add_vertex('2')
  g.add_edge(one, two, 7) 

  assert True

@pytest.mark.skip('not ready')
def test_get_neghiboring_vertices(): 
  g = Graph() 

  one = g.add_vertex('1')
  two = g.add_vertex('2') 
  three = g.add_vertex('3') 
  g.add_edge(one, two, 34) 
  g.add_edge(three, one, 17) 

  assert neghibors[0].vertex.value == '2' 
  assert neghibors[0].weight == 34

  assert neghibors[1].vertex.value == '1' 
  assert neghibors[1].weight == 17  



