from PriorityQueue import PQ
import numpy as np

def ucs(rootNode):
  open_list = PQ()
  closed_list = set()   # set makes sure there's no duplicates
  open_list.insert(0, rootNode)  # Add initial node and total cost of 0

  while(open_list.notEmpty()):
    totalCost, node = open_list.pop()

    # if node has not been visited yet, go for it
    if node not in closed_list:
      closed_list.add(node)   # node is visited for the first time, add to closed list
      if (node.isGoal(node.state)):
        moves, costs, path = node.traceSolution([],[],[])
        return (moves, costs, path, totalCost)   # Returns final solution
      else:
        node.generateSuccessors()
        successors = node.successors

        for successor in successors:
          if successor not in closed_list:
            new_cost = totalCost + successor.cost
            open_list.insert(new_cost, successor)
            