from time import perf_counter
from UCS import ucs
from GBFS import gbfs
from Node import Node
import numpy as np
from utils import getPuzzles, writeResults, generate50Puzzles

def solve(puzzle, puzzleCount, algo, heur):
  max_row = len(puzzle) - 1
  max_col = len(puzzle[1]) - 1
  rootNode = Node(puzzle, None, 0, 0, max_row, max_col)

  print('\nPuzzle to solve:\n')
  print(np.matrix(puzzle))

  timeout = 60  # Maximum time the algorithm should run for
  if(algo == 'UCS'):
    print('\nFinding solution with Uniform Cost Search....\n')
    search_outputs = ucs(rootNode, timeout)
    sol_fname = str(puzzleCount) + '_ucs_solution.txt'
    srch_fname = str(puzzleCount) + '_ucs_search.txt'

  elif(algo == 'GBFS'):
    if (heur != 'h0' and heur != 'h1' and heur != 'h2'):
      print('Please provide a valid heuristic!\nYour choices are: h0, h1 or h2')
      return
    print('\nFinding solution with Greedy Best First Search....\n')
    search_outputs = gbfs(rootNode, heur, timeout)
    sol_fname = str(puzzleCount) + '_gbfs_solution.txt'
    srch_fname = str(puzzleCount) + '_gbfs_search.txt'

  writeResults(sol_fname, srch_fname, search_outputs, timeout)  

# Reads input file and stores puzzles in a list
# Currently hardcoded to only accept 4x2 puzzles
puzzles = getPuzzles('input.txt')

# Solves each puzzle and outputs results/metrics in text file
puzzleCount = 0
for puzzle in puzzles:
  solve(puzzle, puzzleCount, 'GBFS', 'h1')
  puzzleCount += 1