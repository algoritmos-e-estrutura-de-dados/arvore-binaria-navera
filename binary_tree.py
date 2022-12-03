from node import Node


class BinaryTree:

  def __init__(self):
    self.root = None
    self.aux = None
    
  def adicionar(self, value):
    node = Node(value)
    aux = self.root
    n = 0
    while(n < 1):
      if self.root == None:
        self.root = node
        break
      if aux.esquerda == None:
        if value < aux.value:
          aux.setEsquerda(node)
          break
      if aux.direita == None:
        if value > aux.value:
          aux.setDireita(node)
          break
      if value < aux.value:
        aux = aux.esquerda
      if value > aux.value:
        aux = aux.direita
      
    
  def remover(self, value, controle):
      if controle.value == value:
         controle.value = None
      if controle.esquerda is not None:
        self.remover(value, controle.esquerda)
      if controle.direita is not None:
        self.remover(value, controle.direita)
      

  def remove(self,value):
    self.remover(value, self.root)
    

  def PrintPre(self, aux):
    if aux is not None:
      if aux.value is not None:
        print(aux.value)
      self.PrintPre(aux.esquerda)
      self.PrintPre(aux.direita)

  def imprimePre(self):
    self.PrintPre(self.root)

  def PrintEm(self, aux):
    if aux is not None:  
      self.PrintEm(aux.esquerda)
      if aux.value is not None:
        print(aux.value)
      self.PrintEm(aux.direita)

  def imprimeEm(self):
    self.PrintEm(self.root)

  def PrintPos(self, aux):
    if aux is not None:
      self.PrintPos(aux.esquerda)
      self.PrintPos(aux.direita)
      if aux.value is not None:
        print(aux.value)

  def imprimePos(self):
    self.PrintPos(self.root)