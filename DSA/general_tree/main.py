class TreeNode:
  def __init__(self, data):
    self.data = data
    self.child =[]
    self.parent = None

  def add_child(self, child):
    child.parent=self
    self.child.append(child)

  def Print_Tree(self):
    print(self.data)
    if self.child:
      for ch in self.child:
        ch.Print_Tree()
  

  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level+=1
      p = p.parent
    return level
Electronic = TreeNode("Electronic")

Laptop = TreeNode("Laptop")
Laptop.add_child(TreeNode("Dell"))
Laptop.add_child(TreeNode("Mac"))
Laptop.add_child(TreeNode("Hp"))

Phone = TreeNode("Phone")
Phone.add_child(TreeNode("iphone"))
Phone.add_child(TreeNode("Vivo"))
Phone.add_child(TreeNode("Samsung"))

TV = TreeNode("TV")
TV.add_child(TreeNode("LED"))
TV.add_child(TreeNode("LCD"))

Electronic.add_child(Laptop)
Electronic.add_child(Phone)
Electronic.add_child(TV)

Electronic.Print_Tree()

print(TV.child[0].get_level())
