from node import Node


class BinaryTree:

  def __init__(self):
    self.root = None
    self.aux = None
    
  def adicionar(self, value):
    node = Node(value)
    self.aux = node
    if self.root == None:
      self.root = node
    if value < self.root.value:
        if self.esquerda is None:
          self.esquerda = node
        else:
          self.esquerda.adicionar(value)
    elif value > self.root:
        if node.getDireita() is None:
          node.getDireita() = Node(value)
        else:
          node.getDireita().adicionar(value)
      
    else:
      self.root = value

  def encontra(self, aux):
    if self.aux == aux:
      return self
    node = self.esquerda if aux < self.aux else self.direita
    if node is not None:
      return node.encontra(aux)

  def PrintBT(self):
    if self.esquerda:
      self.esquerda.PrintBT()
    print(self.value),
    if self.direita:
      self.direita.PrintBT()
