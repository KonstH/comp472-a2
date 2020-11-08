class Node:
  def __init__(self, state, parent, cost, max_row, max_col):
    self.state = state
    self.parent = parent
    self.successors = []
    self.cost = cost
    self.max_row = max_row
    self.max_col = max_col
    self.emptyPos = self.find(0)

  def find(self, value):
    for row in range(self.max_row + 1):
      for col in range(self.max_col + 1):
        if self.state[row][col] == value:
          return (row, col)
  
  def isCorner(self, coord):
    (row, col) = coord

    if row == 0 and col == 0:
      return 'tl'
    elif row == self.max_row and col == self.max_col:
      return 'br'
    elif row == self.max_row and col == 0:
      return 'bl'
    elif row == 0 and col == self.max_col:
      return 'tr'
    return None

  def generateSuccessors(self):
    empty = self.emptyPos
    self.move_up(empty)
    self.move_down(empty)
    self.move_left(empty)
    self.move_right(empty)

    if(self.isCorner(empty) != None):
      self.wrap_left(empty)
      self.wrap_right(empty)
      self.diag_downleft(empty)
      self.diag_downright(empty)
      self.diag_upleft(empty)
      self.diag_upright(empty)
      self.diag_opposite(empty, self.isCorner(empty))

      if(self.max_row > 2):
        self.wrap_up(empty)
        self.wrap_down(empty)
        
  # Regular moves: Cost = 1
  def move_up(self, emptyTile):
    row, col = emptyTile

    if(row-1 >= 0):
      targetTile = (row-1, col)
      self.swap_and_add_child(emptyTile, targetTile, 1)

  def move_down(self, emptyTile):
    (row, col) = emptyTile

    if(row+1 <= self.max_row):
      targetTile = (row+1, col)
      self.swap_and_add_child(emptyTile, targetTile, 1)

  def move_left(self, emptyTile):
    (row, col) = emptyTile

    if(col-1 >= 0):
      targetTile = (row, col-1)
      self.swap_and_add_child(emptyTile, targetTile, 1)

  def move_right(self, emptyTile):
    (row, col) = emptyTile

    if(col+1 <= self.max_col):
      targetTile = (row, col+1)
      self.swap_and_add_child(emptyTile, targetTile, 1)


  # Wrap moves: Cost = 2
  def wrap_left(self, emptyTile):
    (row, _) = emptyTile
    targetTile = (row, 0)
    self.swap_and_add_child(emptyTile, targetTile, 2)
    
  def wrap_right(self, emptyTile):
    (row, _) = emptyTile
    targetTile = (row, self.max_col)
    self.swap_and_add_child(emptyTile, targetTile, 2)    

  def wrap_up(self, emptyTile):
    (_, col) = emptyTile
    targetTile = (0, col)
    self.swap_and_add_child(emptyTile, targetTile, 2)    

  def wrap_down(self, emptyTile):
    (_, col) = emptyTile
    targetTile = (self.max_row, col)
    self.swap_and_add_child(emptyTile, targetTile, 2)   


  # Diagonal moves: Cost = 3
  def diag_downleft(self, emptyTile):
    (row, col) = emptyTile

    if(row + 1 <= self.max_row and col - 1 >= 0):
      targetTile = (row+1, col-1)
      self.swap_and_add_child(emptyTile, targetTile, 3)


  def diag_downright(self, emptyTile):
    (row, col) = emptyTile

    if(row + 1 <= self.max_row and col + 1 <= self.max_col):
      targetTile = (row+1, col+1)
      self.swap_and_add_child(emptyTile, targetTile, 3)


  def diag_upleft(self, emptyTile):
    (row, col) = emptyTile
    
    if(row - 1 >=0 and col - 1 >= 0):
      targetTile = (row-1, col-1)
      self.swap_and_add_child(emptyTile, targetTile, 3)

  def diag_upright(self, emptyTile):
    (row, col) = emptyTile
    
    if(row - 1 >=0 and col + 1 <= self.max_col):
      targetTile = (row+1, col-1)
      self.swap_and_add_child(emptyTile, targetTile, 3)

  def diag_opposite(self, emptyTile, cornerPos):
    if(cornerPos == 'tl'):
      targetTile = (self.max_row, self.max_col)
    elif(cornerPos == 'tr'):
      targetTile = (self.max_row, 0)
    elif(cornerPos == 'bl'):
      targetTile = (0, self.max_col)
    else:
      targetTile = (0, 0)
    self.swap_and_add_child(emptyTile, targetTile, 3)

  def swap_and_add_child(self, emptyTile, targetTile, move_cost):
    new_state = self.state.copy()
    t_row, t_col = targetTile
    e_row, e_col = emptyTile
    value_target = self.state[t_row][t_col]
    new_state[e_row][e_col] = value_target
    new_state[t_row][t_col] = 0
    child = Node(new_state, self, move_cost, self.max_row, self.max_col)
    self.successors.append(child)

  def isGoal(self, state):
    goal1 = [['1','2','3','4'],['5','6','7','0']]
    goal2 = [['1','3','5','7'],['2','4','6','0']]

    if(state == goal1 or state == goal2):
      return True
    return False

  # # Applies heuristic to node
  # def apply_heuristic(self, h):
  #   if h == 'h0':
  #     return self.h0()
  #   elif h == 'h1':
  #     return self.h1()
  #   elif h == 'h2':
  #     return self.h2()
  #   else:
  #     print('invalid heuristic')

  # # Heuristic 0 logic
  # def h0(self):
  #   return 0

  # # Heuristic 1 logic
  # def h1(self):
  #   return 0

  # # Heuristic 2 logic
  # def h2(self):
  #   return 0
