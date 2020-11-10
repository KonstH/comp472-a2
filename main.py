from time import perf_counter
from UCS import ucs
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


def solve(puzzle, puzzleCount):
  max_row = len(puzzle) - 1
  max_col = len(puzzle[1]) - 1
  rootNode = Node(puzzle, None, 0, 0, max_row, max_col)

  print('\nPuzzle to solve:\n')
  print(np.matrix(puzzle))
  print('\nFinding solution with Uniform Cost Search....\n')

  moves, costs, path, total_cost, end_time, timedOut = ucs(rootNode, 60)

  file_name = str(puzzleCount) + '_ucs_solution.txt'
  f = open(file_name,'w')

  if(timedOut):
    print('Timed Out!\n')
    f.write('no solution')
    return
  else:
    moves.reverse()    # Show solution moves in correct order
    costs.reverse()    # Show solution moves in correct order
    path.reverse()    # Show solution moves in correct order
    i = 0 

    for state in path:
      f.write(str(moves[i]) + ' ')  # Write the tile moved
      f.write(str(costs[i]) + ' ')  # Write how much the move cost
      f.write((' '.join(str(tile) for tile in state)).replace('[', '').replace(']', '').replace(', ', ' '))   # Write the state of the board after the move
      f.write('\n')
      i += 1

    f.write(str(total_cost) + ' ')  # Write total cost
    f.write(str(round(end_time, 1)))  # Write total computation time
    
    print("Solution exported to " + file_name + "!\n")
  

# Solves each puzzle and outputs results/metrics in text file
puzzleCount = 0
for puzzle in puzzles:
  solve(puzzle, puzzleCount)
  puzzleCount += 1