from PriorityQueue import PQ
import numpy as np
from time import perf_counter

def gbfs(rootNode, heur, timeout):
  open_list = PQ()
  closed_list = []  # keeps track of search path
  open_list.insert(rootNode.h(heur), rootNode)  # Add initial node
  start_time = perf_counter()
  timedOut = False

  while(open_list.notEmpty()):
    elapsed_time = perf_counter()
    
    if ((elapsed_time - start_time) >= timeout):
      timedOut = True
      return (None, None, None, None, None, None, timedOut)

    else:
      _ , node = open_list.pop() # we don't care about the heuristic value returned

      # if node has not been visited yet, go for it
      if node.state not in closed_list:
        closed_list.append(node.state)   # node is visited for the first time, add to closed list
        if (node.isGoal(node.state)):
          moves, costs, sol_path = node.traceSolution([],[],[])
          totalCost = sum(costs)
          end_time = (elapsed_time - start_time)
          return (moves, costs, sol_path, closed_list, totalCost, end_time, timedOut)   # Returns final solution
        else:
          node.generateSuccessors()
          successors = node.successors

          for successor in successors:
            if successor not in closed_list:
              open_list.insert(successor.h(heur), successor)
            