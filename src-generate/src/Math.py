# -----------------------------------------------------------------------------
#   Miscellaneous math tools
#   1. Point to line distance calculator
#   2. Intersection checker
#   3. Quickhull algorithm
# -----------------------------------------------------------------------------
import math


# ------------------------------------------------------------------------------
#                       1. Point to line distance calculator
#           (source: http://www.fundza.com/vectors/point2line/index.html)
# ------------------------------------------------------------------------------

# Given a line with coordinates 'start' and 'end' and the
# coordinates of a point 'pnt' the proc returns the shortest
# distance from pnt to the line and the coordinates of the
# nearest point on the line.
#
# 1  Convert the line segment to a vector ('line_vec').
# 2  Create a vector connecting start to pnt ('pnt_vec').
# 3  Find the length of the line vector ('line_len').
# 4  Convert line_vec to a unit vector ('line_unitvec').
# 5  Scale pnt_vec by line_len ('pnt_vec_scaled').
# 6  Get the dot product of line_unitvec and pnt_vec_scaled ('t').
# 7  Ensure t is in the range 0 to 1.
# 8  Use t to get the nearest location on the line to the end
#    of vector pnt_vec_scaled ('nearest').
# 9  Calculate the distance from nearest to pnt_vec_scaled.
# 10 Translate nearest back to the start/end line.
# Malcolm Kesson 16 Dec 2012

def dot(v, w):
    x, y = v
    X, Y = w
    return x*X + y*Y


def length(v):
    x, y = v
    return math.sqrt(x*x + y*y)


def vector(b, e):
    x, y = b
    X, Y = e
    return (X-x, Y-y)


def unit(v):
    x, y = v
    mag = length(v)
    return (x/mag, y/mag)


def distance(p0, p1):
    return length(vector(p0, p1))


def scale(v, sc):
    x, y = v
    return (x * sc, y * sc)


def add(v, w):
    x, y = v
    X, Y = w
    return (x+X, y+Y)


def pnt2line(pnt, start, end):
    line_vec = vector(start, end)
    pnt_vec = vector(start, pnt)
    line_len = length(line_vec)
    line_unitvec = unit(line_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0/line_len)
    t = dot(line_unitvec, pnt_vec_scaled)
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    nearest = scale(line_vec, t)
    dist = distance(nearest, pnt_vec)
    return dist


# ------------------------------------------------------------------------------
#                              2. Intersection checker
# (source: https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
#     ?fbclid=IwAR0y8Gh7g07QIPL965uqMbQWUU8i1z0U0q_HNm21167VnUWV-1m6m42nGwA)
# ------------------------------------------------------------------------------

# simple CCW implementation
def ccw_x(a, b, c):
    return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])


# Return true if line segments AB and CD intersect
def intersect(a, b, c, d):
    return ccw_x(a, c, d) != ccw_x(b, c, d) and ccw_x(a, b, c) != ccw_x(a, b, d)

# ------------------------------------------------------------------------------
#                              3. Quickhull algorithm
#                               (copied from jaehok A1)
# ------------------------------------------------------------------------------


# simple ccw algorithm
def ccw_qh(x_A, y_A, x_B, y_B, x_C, y_C):
    return (x_B - x_A)*(y_C - y_A) - (x_C - x_A)*(y_B - y_A)


def quickhull(points):
    def quickhull_rec(x_A, y_A, x_B, y_B, points):
        # find furthest point in points from AB
        furthest = []
        maxdist = 0
        new_points = []
        for point in points:
            if ccw_qh(x_A, y_A, x_B, y_B, point[0], point[1]) > 0:
                new_points.append(point)
                if ccw_qh(x_A, y_A, x_B, y_B, point[0], point[1]) > maxdist:
                    maxdist = ccw_qh(x_A, y_A, x_B, y_B, point[0], point[1])
                    furthest = point
        if maxdist == 0:
            convex_hull.append([x_A, y_A])
            return
        quickhull_rec(x_A, y_A, furthest[0], furthest[1], new_points)
        quickhull_rec(furthest[0], furthest[1], x_B, y_B, new_points)
    # initialize convex hull and points list
    convex_hull = []
    minval = float("inf")
    maxval = float("-inf")
    y_min = -1
    y_max = -1

    for point in points:
        if point[0] > maxval:
            maxval = point[0]
            y_max = point[1]
        if point[0] < minval:
            minval = point[0]
            y_min = point[1]

    # find horizontal max and min points
    set1 = []
    set2 = []
    for point in points:
        ccw_val = ccw_qh(minval, y_min, maxval, y_max, point[0], point[1])
        if ccw_val > 0:
            set1.append(point)
        elif ccw_val < 0:
            set2.append(point)

    quickhull_rec(minval, y_min, maxval, y_max, set1)
    quickhull_rec(maxval, y_max, minval, y_min, set2)

    return convex_hull
