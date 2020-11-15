from PriorityQueue import PQ
from time import perf_counter
from utils import index

def ucs(rootNode, timeout):
  open_list = PQ()
  closed_list = []
  open_list.insert(0, rootNode)  # Add initial node with g(n) of 0
  start_time = perf_counter()    # Start the timer
  timedOut = False

  while(open_list.notEmpty()):
    elapsed_time = perf_counter()

    # if algorithm's runtime has exceeded the specified amount, stop execution
    if ((elapsed_time - start_time) >= timeout):
      timedOut = True
      return (None, None, None, None, None, None, timedOut)

    else:
      currCost, node = open_list.pop()   # get node and its g(n)
      clist_node_index = index(node.state, closed_list)

      # if node has not been visited yet, process it
      if clist_node_index < 0:
        closed_list.append(node)   # node is visited for the first time, add to closed list

        # goal achieved, stop algorithm and return results
        if (node.isGoal(node.state)):
          moves, costs, sol_path = node.traceSolution([],[],[])
          totalCost = sum(costs)
          end_time = (elapsed_time - start_time)
          return (moves, costs, sol_path, closed_list, totalCost, end_time, timedOut)   # Return final values

        # goal not achieved yet, generate next nodes and keep evaluating
        else:
          node.generateSuccessors()
          successors = node.successors

          for successor in successors:
            if successor not in closed_list:
              successor.gn = currCost + successor.cost
              open_list.insert(successor.gn, successor)
