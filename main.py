from UCS import ucs
from GBFS import gbfs
from Astar import aStar
from Node import Node
from utils import getPuzzles, writeResults, clearOldOutputs
import numpy as np
import argparse

# Sets up the arguments that can be passed in the terminal
parser = argparse.ArgumentParser(description="Solve the Chi-Puzzle(s) using different algorithms and heuristics")
parser.add_argument('-f', '--filename', type=str, default='50puzzles.txt', metavar='', help="Name of input file (default: input.txt)")
parser.add_argument('-t', '--timeout', type=int, default=60, metavar='', help="Timeout for algorithms (default: 60)")
group = parser.add_mutually_exclusive_group()
group.add_argument('-del', '--delete', action="store_true", help="Delete outputs from previous run (default: False)")
args = parser.parse_args()

"""
Function which solves the given puzzles using the provided algorithm and heuristic
"""
def solve(puzzle, puzzleCount, algo, heur, timeout):
  max_row = len(puzzle) - 1
  max_col = len(puzzle[1]) - 1
  rootNode = Node(puzzle, None, 0, 0, max_row, max_col)

  print('\nPuzzle to solve:\n')
  print(np.matrix(puzzle))

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

# Reads input file and stores puzzles in a list (Only works for 2x4 puzzles)
# Default file: 50puzzles.txt (you can pass another file as an argument or using the -f flag in the terminal)
puzzles = getPuzzles(args.filename)

# If -del flag is passed, old output folders and their contents are deleted
if(args.delete):
  clearOldOutputs()

# Solves each puzzle and outputs results/metrics in text file.
# The third and fourth arguments passed to the solve function determine which algorithm and heuristic will be used.
# 
# Algorithm options: UCS, GBFS, A*
# Heuristic options: h0, h1, h2
#
# Note: If UCS is chosen, any heuristic value is accepted, as it's not required by the algorithm
for i, puzzle in enumerate(puzzles):
  solve(puzzle, i, 'UCS', None, args.timeout)
  solve(puzzle, i, 'GBFS', 'h1', args.timeout)
  solve(puzzle, i, 'GBFS', 'h2', args.timeout)
  solve(puzzle, i, 'A*', 'h1', args.timeout)
  solve(puzzle, i, 'A*', 'h2', args.timeout)