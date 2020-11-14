from PriorityQueue import PQ
from time import perf_counter

""" Helper fn which returns index of el in a list or -1 if not found"""
def index(item, lst):
  states = [x.state for x in lst]
  try:
    return states.index(item)
  except:
    return -1

def aStar(rootNode, heur, timeout):
  open_list = PQ()
  closed_list = []  
  search_path = []  
  rootNode.fn = rootNode.hn = rootNode.h(heur)  # g(n) is 0 by default, so we only set f(n) & h(n)
  open_list.insert(rootNode.fn, rootNode)  # Add initial node
  start_time = perf_counter()     # Start the timer
  timedOut = False

  while(open_list.notEmpty()):
    elapsed_time = perf_counter()

    # if algorithm's runtime has exceeded the specified amount, stop execution
    if ((elapsed_time - start_time) >= timeout):
      timedOut = True
      return (None, None, None, None, None, None, timedOut)

    else:
      currCost, node = open_list.pop()     # get node and its g(n)
      clist_node_index = index(node.state, closed_list)     # get index of node in closed list or -1 if absent

      # node has been visited, but we must check if it now has a lower f(n) value
      if clist_node_index >= 0:
        if(node.fn < closed_list[clist_node_index].fn):
          del closed_list[clist_node_index]     # new f(n) < old f(n), so delete old node from cl
          open_list.insert(node.fn, node)
      
      else:
        closed_list.append(node)   # node is visited for the first time, add to closed list
        search_path.append(node)   # update search path

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
              successor.gn = currCost + successor.cost
              successor.fn = successor.gn + successor.hn
              open_list.insert(successor.fn, successor)
