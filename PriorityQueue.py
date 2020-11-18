""" Custom PriorityQueue class """

class PQ(): 
  def __init__(self): 
    self.queue = []

  # for checking if the queue is empty 
  def notEmpty(self): 
    return len(self.queue) > 0

  # insert element into queue, handles special cases where elements have same priority or same node with diff priorities
  def insert(self, new_priority, new_node):
    if(len(self.queue) > 0):
      for i in range(len(self.queue)):
        old_priority, old_node = self.queue[i]
        if (new_node.state == old_node.state):
          if(new_priority >= old_priority):
            return
          else:
            del self.queue[i]
            self.queue.append((new_priority, new_node))
            return
      self.queue.append((new_priority, new_node))   
    else:
      self.queue.append((new_priority, new_node))
      
  # remove element with highest priority and return it
  def pop(self): 
    try: 
      min = 0
      for i in range(len(self.queue)):
        new = self.queue[i][0]
        old = self.queue[min][0]
        if new < old:
          min = i
      item = self.queue[min] 
      del self.queue[min] 
      return item
    except IndexError: 
      print()
      exit()
