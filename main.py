from time import perf_counter
from UCS import ucs
from GBFS import gbfs
from Node import Node
import numpy as np

# Reads input file and stores puzzles in a list
# Currently hardcoded to only accept 4x2 puzzles
with open('input.txt') as f:
  puzzles = []
  for line in f:
    line = line.split()
    puzzle = [[],[]]
    count = 0
    if line:
      for i in line:
        num = int(i)
        if count < 4:
          puzzle[0].append(num)
        else:
          puzzle[1].append(num)
        count += 1
      puzzles.append(puzzle)


def solve(puzzle, puzzleCount, algo, heur):
  max_row = len(puzzle) - 1
  max_col = len(puzzle[1]) - 1
  rootNode = Node(puzzle, None, 0, 0, max_row, max_col)

  print('\nPuzzle to solve:\n')
  print(np.matrix(puzzle))

  timeout = 60  # Maximum time the algorithm should run for
  if(algo == 'UCS'):
    print('\nFinding solution with Uniform Cost Search....\n')
    moves, costs, sol_path, srch_path, total_cost, end_time, timedOut = ucs(rootNode, timeout)
    sol_fname = str(puzzleCount) + '_ucs_solution.txt'
    srch_fname = str(puzzleCount) + '_ucs_search.txt'

  elif(algo == 'GBFS'):
    if (heur != 'h0' and heur != 'h1' and heur != 'h2'):
      print('Please provide a valid heuristic!\nYour choices are: h0, h1 or h2')
      return
    print('\nFinding solution with Greedy Best First Search....\n')
    moves, costs, sol_path, srch_path, total_cost, end_time, timedOut = gbfs(rootNode, heur, timeout)
    sol_fname = str(puzzleCount) + '_gbfs_solution.txt'
    srch_fname = str(puzzleCount) + '_gbfs_search.txt'

  sol_f = open(sol_fname,'w')
  srch_f = open(srch_fname,'w')

  if(timedOut):
    print('Search exceeded {} seconds! Execution halted.\n'.format(timeout))
    sol_f.write('no solution')
    srch_f.write('no solution')
    return
  else:
    moves.reverse()    # Show solution moves in correct order
    costs.reverse()    # Show solution moves in correct order
    sol_path.reverse()    # Show solution moves in correct order
    i = 0 

    # Export solution path to solution file
    for state in sol_path:
      sol_f.write(str(moves[i]) + ' ')  # Write the tile moved
      sol_f.write(str(costs[i]) + ' ')  # Write how much the move cost
      sol_f.write((' '.join(str(tile) for tile in state)).replace('[', '').replace(']', '').replace(', ', ' '))   # Write the state of the board after the move
      sol_f.write('\n')
      i += 1
    
    # Export search path to search file
    for node in srch_path:
      srch_f.write('0 0 0 ')  # Write f(n), g(n), h(n) as 0 for the UCS algorithm
      srch_f.write(str(node).replace('[', '').replace(']', '').replace(', ', ' '))
      srch_f.write('\n')

    sol_f.write(str(total_cost) + ' ')  # Write total cost
    sol_f.write(str(round(end_time, 1)))  # Write total computation time
    
    print('Solution exported to ' + sol_fname + '!')
    print('Search path exported to ' + srch_fname + '!\n')
    sol_f.close()
    srch_f.close()
  

# Solves each puzzle and outputs results/metrics in text file
puzzleCount = 0
for puzzle in puzzles:
  solve(puzzle, puzzleCount, 'GBFS', 'h1')
  puzzleCount += 1