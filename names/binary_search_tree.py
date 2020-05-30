from queue import Queue
from stack import Stack

from enum import Enum

class Order(Enum):
    pre_order = "pre order"
    post_order = "post order"
    in_order = "in order"

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value) 
        node = self
        while node is not None:
            if value >= node.value:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    return node.right
            elif value < node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    return node.left

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        while node is not None:
            if target > node.value:
                if node.right:
                    node = node.right
                else:
                    return False
            elif target < node.value:
                if node.left:
                    node = node.left
                else:
                    return False
            elif target == node.value:
                return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn, order=Order.in_order):
        if order == Order.pre_order:
            fn(self.value)

        if self.left:
            self.left.for_each(fn, order)

        if order == Order.in_order:
            fn(self.value)

        if self.right:
            self.right.for_each(fn, order)

        if order == Order.post_order:
            fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.for_each(print, Order.in_order)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while len(queue) > 0:
            current = queue.dequeue()
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
            print(current.value)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            current = stack.pop()
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        node.for_each(print, Order.pre_order)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        node.for_each(print, Order.post_order)
