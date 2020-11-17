"""
This file contains helper functions used in the main file
"""
import os
import shutil
import random
curr_dir = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))     # Store current directory path


"""
Function which captures puzzles from a given input file and returns them
as an array
"""
def getPuzzles(file_name):
  with open(file_name) as f:
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
    return puzzles


"""
Function which writes all the search/solution paths to appropriate files.
Also creates directories for them, to keep things neat and readable.
"""
def writeResults(sol_file_name, srch_file_name, search_results, timeout, algo):
  moves, costs, sol_path, srch_path, total_cost, end_time, timedOut = search_results    # unpacks results

  solutions_dir = curr_dir + '/solution_files/'
  search_dir = curr_dir + '/search_files/'

  # Creates directories for output files to keep things neat
  try:
    os.mkdir(solutions_dir)
    os.mkdir(search_dir)
  except OSError:
    pass   # folder already exists, ignore warning
  
  # Open files for writing
  sol_f = open(solutions_dir + sol_file_name, 'w')
  srch_f = open(search_dir + srch_file_name, 'w')

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
    if(algo == 'UCS'):
      for node in srch_path:
        srch_f.write('0 ')  # Write f(n) as 0
        srch_f.write(str(node.gn))  # Write g(n)
        srch_f.write(' 0 ')  # Write h(n) as 0
        srch_f.write(str(node.state).replace('[', '').replace(']', '').replace(', ', ' '))
        srch_f.write('\n')

    elif(algo == 'GBFS'):
      for node in srch_path:
        srch_f.write('0 0 ')  # Write f(n) and g(n) as 0
        srch_f.write(str(node.hn) + ' ')  # Write h(n)
        srch_f.write(str(node.state).replace('[', '').replace(']', '').replace(', ', ' '))
        srch_f.write('\n')
    
    elif(algo == 'A*'):
      for node in srch_path:
        srch_f.write(str(node.fn) + ' ')  # Write f(n)
        srch_f.write(str(node.gn) + ' ')  # Write g(n)
        srch_f.write(str(node.hn) + ' ')  # Write h(n)
        srch_f.write(str(node.state).replace('[', '').replace(']', '').replace(', ', ' '))
        srch_f.write('\n')

    sol_f.write(str(total_cost) + ' ')  # Write total cost
    sol_f.write(str(round(end_time, 1)))  # Write total computation time
    
    print('Solution exported to ' + sol_file_name + '!')
    print('Search path exported to ' + srch_file_name + '!\n')
    sol_f.close()
    srch_f.close()


"""
Function which generates 50 random/unique puzzles and exports them to a file
"""
def generate50Puzzles():
  puzzle_values = [0,1,2,3,4,5,6,7]
  puzzles = []

  while(len(puzzles) < 50):
    puzzle = random.sample(puzzle_values, len(puzzle_values))

    if(puzzle not in puzzles):
      puzzles.append(puzzle)

  # Export puzzles to file
  puzzles_file = open('50puzzles.txt', 'w')

  for puzzle in puzzles:
    puzzles_file.write(str(puzzle).replace('[', '').replace(']', '').replace(', ', ' ') + '\n')    # formatting


"""
Function which counts the total number of lines in all the files inside of the solution and search output directories
"""
def getTotalLines():
  solutions_dir = curr_dir + '/solution_files/'
  search_dir = curr_dir + '/search_files/'
  sols_total = 0
  search_total = 0
  no_sols = 0

  for filename in os.listdir(solutions_dir):
    with open(solutions_dir + filename) as f:
      sol_found = True
      for i, l in enumerate(f):
        if(i == 0 and 'solution' in l):
          sol_found = False
          no_sols += 1
          break
        else:
          pass
      if(sol_found):
        sols_total += i+1

  for filename in os.listdir(search_dir):
    with open(search_dir + filename) as f:
      sol_found = True
      for i, l in enumerate(f):
        if(i == 0):
          if('solution' in l):
            sol_found = False
            break
        else:
          pass
      if(sol_found):
        search_total += i+1
  
  return (search_total, sols_total, no_sols)

"""
Function which deletes the solution and search output directories along with their nested files
"""
def clearOldOutputs():
  solutions_dir = curr_dir + '/solution_files/'
  search_dir = curr_dir + '/search_files/'

  # Deletes directories for output files
  try:
    shutil.rmtree(solutions_dir)
    shutil.rmtree(search_dir)
  except OSError:
    pass   # ignore any errors


"""
Function which returns the index of the node in the closed list, or -1 if not found
"""
def index(item, lst):
  states = [x.state for x in lst]
  try:
    return states.index(item)
  except:
    return -1


"""
Function which returns the index of the specified value in a given list
"""
def find(arr, value):
  for row in range(2):
    for col in range(4):
      if arr[row][col] == value:
        return (row, col)