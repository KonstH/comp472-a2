class PQ(): 
  def __init__(self): 
    self.queue = []

  # for checking if the queue is empty 
  def notEmpty(self): 
    return len(self.queue) > 0

  # insert element into queue, handles special cases where elements have same priority or same node with diff priorities
  # TODO: Re-write logic to be cleaner
  def insert(self, new_cost, new_node):
    if(len(self.queue) > 0):
      for i in range(len(self.queue)):
        (old_cost, old_node) = self.queue[i]
        if (new_node.equal(old_node)):
          if(new_cost >= old_cost):
            return
          else:
            del self.queue[i]
            self.queue.append((new_cost, new_node))
            return
      self.queue.append((new_cost, new_node))   
    else:
      self.queue.append((new_cost, new_node))
      
  # remove element with highest priority and return it
  def pop(self): 
    try: 
      min = 0
      for i in range(len(self.queue)):
        new, _ = self.queue[i]
        old, _ = self.queue[min]
        if new < old:
          min = i
      item = self.queue[min] 
      del self.queue[min] 
      return item
    except IndexError: 
      print()
      exit()
