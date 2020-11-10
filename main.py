from time import perf_counter
from UCS import ucs
from Node import Node
import numpy as np

# Reads input file and stores puzzles in a list
# Currently hardcoded to only accept 4x2 puzzles
with open('test.txt') as f:
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


# Solves each puzzle and outputs results/metrics in text file
puzzleCount = 0
for puzzle in puzzles:
  max_row = len(puzzle) - 1
  max_col = len(puzzle[1]) - 1
  rootNode = Node(puzzle, None, 0, max_row, max_col)

  print('\nPuzzle to solve:\n')
  print(np.matrix(puzzle))
  print('\nFinding solution with Uniform Cost Search....\n')

  solution, total_cost = ucs(rootNode)
  solution.reverse()    # Show solution moves in correct order

  file_name = str(puzzleCount) + '_ucs_solution.txt'
  f = open(file_name,'w')

  for move in solution:
    f.write((' '.join(str(tile) for tile in move)).replace('[', '').replace(']', '').replace(', ', ' '))
    f.write('\n')
  f.write(str(total_cost))
  
  print("Solution exported to " + file_name + "!\n")
  puzzleCount += 1
