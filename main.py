import numpy as np
from time import perf_counter
from UCS import ucs
from Node import Node

puzzle = [[1,3,5,7],[2,4,6,0]]
max_row = len(puzzle) - 1
max_col = len(puzzle[1]) - 1

rootNode = Node(puzzle, None, 0, max_row, max_col)
ucs(rootNode)
