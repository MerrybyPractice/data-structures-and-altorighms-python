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
  
  one_two_edge = one.neghibors[0]

  assert one_two_edge.vertex == two
  assert one_two_edge.weight == 7
  assert len(two.neghibors) == 0

def test_get_neghiboring_vertices(): 
  g = Graph() 

  one = g.add_vertex('1')
  two = g.add_vertex('2') 
  three = g.add_vertex('3') 
  g.add_edge(one, two, 34) 
  g.add_edge(one, three, 17) 

  neghibors = g.get_neghibors(one)

  assert neghibors[0].vertex.value == '2' 
  assert neghibors[0].weight == 34

  assert neghibors[1].vertex.value == '3' 
  assert neghibors[1].weight == 17  

def test_looping(): 
  g = Graph()

  one = g.add_vertex('one')
  g.add_edge(one, one)

  neghibors = g.get_neghibors(one)

  assert neghibors[0].vertex.value == 'one'
  assert neghibors[0].weight == 0

  vrtxs = g.get_vertices()

  assert [vrtx.value for vrtx in vrtxs] == ['one']

def test_breadth_first(): 
  g = Graph() 

  one = g.add_vertex('1')
  two = g.add_vertex('2') 
  three = g.add_vertex('3') 
  g.add_edge(one, two, 34) 
  g.add_edge(one, three, 17)

  operate = []
  def operation(current): 
    operate.append(current.value)
  g.breadth_first(one, operation)
  assert operate == ['1', '2', '3']

def test_depth_first(): 
  g = Graph() 

  one = g.add_vertex('1')
  two = g.add_vertex('2') 
  three = g.add_vertex('3') 
  four = g.add_vertex('4')
  
  g.add_edge(one, two, 34) 
  g.add_edge(one, three, 17)
  g.add_edge(two, four, 78)

  operate = []
  def operation(current): 
    operate.append(current.value)
  g.depth_first(one, operation)
  assert operate == ['1', '3', '2', '4']
  

