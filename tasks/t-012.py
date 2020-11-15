import sys

x1, y1, x2, y2, x3, y3, x4, y4 = sys.argv[1:]

# Make sure x1 is always smaller than x2
if x2 > x1:
    x1, x2 = x2, x1

if y2 > x1:
    x1, x2 = x2, x1

