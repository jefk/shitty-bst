
from random import shuffle

class ShittyBst:

  def __init__(self):
    self.root = None

  def insert(self, key, value):
    newnode = self._insert(self.root, key, value)
    if self.root == None:
      self.root = newnode

  def get(self, key):
    pass

  def in_order(self):
    self._in_order(self.root)

  def _insert(self, node, key, value):
    if node == None:
      return Node(key, value)

    if key < node.key:
      node.left = self._insert(node.left, key, value)
    elif key > node.key:
      node.right = self._insert(node.right, key, value)
    return node

  def _in_order(self, node):
    if node == None:
      return
    self._in_order(node.left)
    print node.key, node.value
    self._in_order(node.right)


class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None


if __name__ == '__main__':
  bst = ShittyBst()
  data = list(enumerate("this is a test dot split".split() ))
  shuffle(data)
  print data
  for i, val in data:
    bst.insert(i, val)

  bst.in_order()
