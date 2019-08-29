# Graphs

Write a basic graph implementation.

## Challenge

Implement a graph with the following methods: add_vertex, add_edge, get_vertices, get_neighbors, and a custom __len__(). Provide comprehensive unit testing for each method.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API

## class Graph

- the main class for graph, off of which all of the main methods can be called. When instantiated, a private attribute of _vertices is created - which is an initially empty list.

Big O: Instantiation takes O(1) time and O(1) space.

### Graph's Methods

- add_vertex: this method takes in a value of any type, instantiates a new instance of the Vertex class with that value as the vertexes value, and adds that vertex to the vertices list on the graph. Then, the new Vertex is returned.

Big O: O(1) for both space and time

- add_edge: this method takes in two vertices and an optional weight integer. If the integer is not passed in, its default value is 0. This method then checks if the vertices are in the list and creates an Edge class instance holding the second vertex and the weight to append on the neighbors list of the first vertex.If both vertices are not in the graphs vertices list, None is returned.

Big O: O(1) for time and space

- get_vertices: this returns the graph's list of vertices if there are any in it, none if it is empty.

Big 0: O(1) for time and space

- get_neighbors: this returns a given vertex's list of neighbors if there are any, which will contain edge objects. If it is empty, get_neighbors returns None.

Big O: O(1) for time and space

- breadth_first: this traverses the graph and performs a passed in operation on each node encountered in breadth_first order.

Big O: without taking into consideration the passed in function, which will have its own complexity implications, the time complexity of this is O(n2), and space is O(n).

- depth_first: this traverses the graph and performs a passed in operation on each node encountered in depth_first order. 

Big O: without taking into the passed in function into consideration, the time complexity of this is O(n2), and space is O(n)

- _len_: this class has a custom len method which returns the length of self._vertices

Big O: O(1) for time and length - given that this uses the native length method on lists.


## class Edge

When instantiated, Edge takes in a vertex and a weight. If the weight is not otherwise passed in or set, it defaults to zero. The edge has a vertex property set to the vertex that is passed in, and a weight property set to the weight that is passed in or defaulting to zero. 

Big O: Instantiation has a big O(1) for both time and space

## class Vertex

When instantiated, vertex takes in a value of any type that is then set as the value of the vertex. Vertex also has a neighbors property that is instantiated as an empty list, and a seen property that is instantiated as False. Neighbors is referenced by add_edge and get_neighbors. Seen is referenced in the breadth traversal method.
