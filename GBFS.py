from PriorityQueue import PQ
from time import perf_counter

def gbfs(rootNode, heur, timeout):
  open_list = PQ()
  closed_list = []
  search_path = []
  rootNode.hn = rootNode.h(heur)
  open_list.insert(rootNode.hn, rootNode)  # Add initial node
  start_time = perf_counter()   # Start the timer
  timedOut = False

  while(open_list.notEmpty()):
    elapsed_time = perf_counter()

    # if algorithm's runtime has exceeded the specified amount, stop execution
    if ((elapsed_time - start_time) >= timeout):
      timedOut = True
      return (None, None, None, None, None, None, timedOut)

    else:
      node = open_list.pop()[1]  # We don't care about the heuristic value returned

      # if node has not been visited yet, process it
      if node.state not in closed_list:
        closed_list.append(node.state)   # node is visited for the first time, add to closed list
        search_path.append(node)         # update search path

        # goal achieved, stop algorithm and return results
        if (node.isGoal(node.state)):
          moves, costs, sol_path = node.traceSolution([],[],[])
          totalCost = sum(costs)
          end_time = (elapsed_time - start_time)
          return (moves, costs, sol_path, search_path, totalCost, end_time, timedOut)   # Return final values

        # goal not achieved yet, generate next nodes and keep evaluating
        else:
          node.generateSuccessors()
          successors = node.successors

          for successor in successors:
            if successor not in closed_list:
              successor.hn = successor.h(heur)
              open_list.insert(successor.hn, successor)
