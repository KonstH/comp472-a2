from time import perf_counter
from UCS import ucs
from Node import Node

puzzle = [[2,0,3,1],[5,6,7,4]]  # Simple puzzle for algorithm validation

max_row = len(puzzle) - 1
max_col = len(puzzle[1]) - 1

rootNode = Node(puzzle, None, 0, max_row, max_col)
ucs(rootNode)
