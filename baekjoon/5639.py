from sys import stdin
read = stdin.readline
class BinaryTree:
    class Node:
        def __init__(self, value):
            self._value = value
            self._left = None
            self._right = None
    
    def __init__(self):
        self._root = None
    
    def push(self, value : int):
        node  = self._root
        parent = None
        while node != None:
            parent = node
            if value < node._value:
                node = node._left
            else:
                node = node._right
        node = self.Node(value)
        if parent:
            if value < node._value:
                parent._left = node
            else:
                parent._right = node
    
    def post_order(self):
        def print_child(node):
            if node == None:
                return
            print_child(node._left)
            print_child(node._right)
            print(node._value)
        print(self._root)

bt = BinaryTree()
val = read()
while True:
    try:
        val = int(input())
    except:
        break
    bt.push(val)
    print(val, 'i')
bt.post_order()
