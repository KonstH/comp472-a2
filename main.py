from UCS import ucs
from GBFS import gbfs
from Astar import aStar
from Node import Node
from utils import getPuzzles, writeResults, generate50Puzzles
import numpy as np

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
      print('\nERROR: Please provide a valid heuristic!\nValid choices are: h0, h1 or h2')
      return
    print('\nFinding solution with Greedy Best First Search....\n')
    search_outputs = gbfs(rootNode, heur, timeout)
    sol_fname = str(puzzleCount) + '_gbfs-' + heur + '_solution.txt'
    srch_fname = str(puzzleCount) + '_gbfs-' + heur + '_search.txt'

  elif(algo == 'A*'):
    if (heur != 'h0' and heur != 'h1' and heur != 'h2'):
      print('\nERROR: Please provide a valid heuristic!\nValid choices are: h0, h1 or h2')
      return
    print('\nFinding solution with A* Search....\n')
    search_outputs = aStar(rootNode, heur, timeout)
    sol_fname = str(puzzleCount) + '_astar-' + heur + '_solution.txt'
    srch_fname = str(puzzleCount) + '_astar-' + heur + '_search.txt'
  
  else:
    print('\nERROR: Please provide a valid algorithm!\nValid choices are: UCS, GBFS or A*')
    return

  writeResults(sol_fname, srch_fname, search_outputs, timeout, algo)

# Reads input file and stores puzzles in a list (Currently hardcoded to only accept 4x2 puzzles)
puzzles = getPuzzles('input.txt')
puzzleCount = 0

# Solves each puzzle and outputs results/metrics in text file.
# The two last arguments passed to the solve function determine which algorithm and heuristic will be used.
# 
# Algorithm options: UCS, GBFS, A*
# Heuristic options: h0, h1, h2
#
# Note: If UCS is chosen, any heuristic value is accepted, as it's not required by the algorithm
for puzzle in puzzles:
  solve(puzzle, puzzleCount, 'A*', 'h1')
  puzzleCount += 1
