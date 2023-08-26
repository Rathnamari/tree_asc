class tree:
  def _init_ (self,Data):
    self.right = None
    self.left = None
    self.node = Data
  def show(self):
    if self.left:
      self.left.show()
    print(self.node)
    if self.right:
      self.right.show()
  def insert(self,new_data):
    if new_data<self.node:
      if self.left is None:
        self.left = tree(new_data)
      else:
        self.left.insert(new_data)
    elif new_data>self.node:
      if self.right is None:
        self.right = tree(new_data)
      else:
        self.right.insert(new_data)

lin=tree(55)
lin.insert(25)
lin.insert(60)
lin.insert(45)
lin.insert(87)
lin.insert(26)
lin.insert(5)
lin.insert(33)
lin.show()
