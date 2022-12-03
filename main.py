from binary_tree import BinaryTree

arvore1 = BinaryTree()

arvore1.adicionar(3)
arvore1.adicionar(2)
arvore1.adicionar(4)
arvore1.adicionar(5)
arvore1.adicionar(1)
arvore1.remove(4)
print("Pré ordem")
arvore1.imprimePre()
print("_______________")
print("Em ordem")
arvore1.imprimeEm()
print("_______________")
print("Pós ordem")
arvore1.imprimePos()

