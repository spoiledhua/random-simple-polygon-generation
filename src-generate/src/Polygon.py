# -----------------------------------------------------------------------------
#   Polygon data type
# -----------------------------------------------------------------------------

from src.Edge import Edge
from src.Math import pnt2line, intersect

import sys


class Polygon:

    # polygon is constructed from a list of vertices (in cw order)
    def __init__(self, vertices):
        self.vertices = vertices
        # edges are found and added as a parameter (type list)
        edges = []
        for i in range(len(vertices)-1):
            e = Edge(vertices[i], vertices[i+1])
            edges.append(e)
        edges.append(Edge(vertices[-1], vertices[0]))
        self.edges = edges

    # checks whether polygon intersects with a query edge
    def intersect(self, query_edge):
        for edge in self.edges:
            # if the query edge and polygon edge don't share a vertex
            if edge.start != query_edge.start and edge.start != query_edge.end:
                if edge.end != query_edge.start and edge.end != query_edge.end:
                    # return true if polygon edge intersects with query edge
                    if intersect(edge.start, edge.end, query_edge.start, query_edge.end):
                        return True
        return False

    # find closest point from pointlist and return the point and the removing edge
    def findClosest(self, pointlist):
        min_dist = float("inf")
        remEdge = None
        closestPoint = None
        for i in range(len(self.edges)):
            e = self.edges[i]
            for point in pointlist:
                # find point to line distance between the point and the removing
                # edge and potentially update nearest point
                curr_dist = pnt2line(point, e.start, e.end)
                # if the two new edges created by the point are valid
                if curr_dist < min_dist:
                    if e.valid(self, point):
                        min_dist = curr_dist
                        remEdge = e
                        closestPoint = point
        return remEdge, closestPoint
