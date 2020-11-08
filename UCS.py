from queue import PriorityQueue
import numpy as np

def ucs(rootNode):
  open_list = PriorityQueue()
  closed_list = set()   # set makes sure there's no duplicates
  open_list.put((0, rootNode))  # Add initial node and total cost of 0

  while(open_list):
    currCost, node = open_list.get()

    # if node has not been visited yet, go for it
    if node not in closed_list:
      closed_list.add(node)   # node is visited for the first time, add to closed list

      if (node.isGoal(node.state)):
        return print(np.matrix(node.state), currCost)
      else:
        node.generateSuccessors()
        successors = node.successors

        for successor in successors:
          if successor not in closed_list:
            new_cost = currCost + successor.cost
            open_list.put((new_cost, successor))
            