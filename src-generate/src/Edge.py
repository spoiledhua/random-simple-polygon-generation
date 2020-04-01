# -----------------------------------------------------------------------------
#   Edge data type
# -----------------------------------------------------------------------------

from src.Math import intersect

import sys


class Edge:

    # constructs edge using start and end points ([x,y]) as arguments
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # checks if the two new edges created by the point are valid
    # (i.e. do not intersect the polygon)
    def valid(self, polygon, point):
        e1 = Edge(self.start, point)
        e2 = Edge(point, self.end)
        if not polygon.intersect(e1) and not polygon.intersect(e2):
            return True
        return False
