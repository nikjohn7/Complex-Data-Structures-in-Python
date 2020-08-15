'''
Maze Explorer
Welcome Ancient Ruins Explorer!

We’ve identified a mysterious chamber deep underground our excavation site. The artifacts held within this chamber would be a considerable addition to the local museum…

Unfortunately, the chamber lies at the heart of a twisted maze. We’re using a graph data structure to model the ruins. We’ll need your expertise to map out the chambers as we move through them.

With your help, we’ll find the optimal path to the chamber before our torch burns out.
'''


# import classes
from graph import Graph, build_graph
from vertex import Vertex

excavation_site=build_graph()
excavation_site.explore()