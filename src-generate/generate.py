# -----------------------------------------------------------------------------
#   Randomly generate points in a [0,1) x [0,1) square and write to test.txt
# -----------------------------------------------------------------------------

import sys
import random

# prompt user to enter the number of vertices
n = int(input("Number of vertices: "))

f = open("test.txt", "w")
f.write("%i\n" % n)
for i in range(n):
    x = random.random()
    y = random.random()
    f.write("%f %f\n" % (x, y))
f.close()
