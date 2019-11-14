import sys
import random
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"<Value: {self.value}. Left: {self.left}. Right: {self.right}>"

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
        elif value < self.value and self.left is not None:
            self.left.insert(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)
        # < go left
        # >= go right

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value and self.left is None:
            return False
        elif target >= self.value and self.right is None:
            return False
        elif target < self.value and self.left is not None:
            self = self.left
            return self.contains(target)
        elif target >= self.value and self.right is not None:
            self = self.right
            return self.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        # Go right until you can't go right any more
        while self.right is not None:
            self = self.right

        return self.value

        # Alternative one-liner recursive solution
        # return self.right.get_max() if self.right else self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # visit each node exactly one time
        # go left until you cant anymore, then go back to the first branch and go right, then go up to the next branch and repeat

        # somewhere in here call cb(node)

        if self.left is not None:
            prev = self
            self = self.left
            self.for_each(cb)
            self = prev
        if self.right is not None:
            prev = self
            self = self.right
            self.for_each(cb)
            self = prev

        return cb(self.value)

        # Alternative cleaner solution
        # cb(self.value)

        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)
   # DAY 2 Project -----------------------

   # Print all the values in order from low to high
   # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        self.queue = Queue()
        self.queue.enqueue(node)
        
        while self.queue.len() > 0:
            node = self.queue.dequeue()
            if node.left:
                self.queue.enqueue(node.left)
            if node.right:
                self.queue.enqueue(node.right)
            print(node.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make stack
        self.stack = Stack()
        self.stack.push(node)
        while self.stack.len() > 0:
            node = self.stack.pop()
            if node.left:
                self.stack.push(node.left)
            if node.right:
                self.stack.push(node.right)
            print(node.value)

        


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)


    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)


def add_two(node):
    return node.value + 2


arr = []


def cb(x):
    return arr.append(x)


# v1 = random.randint(1, 101)
# v2 = random.randint(1, 101)
# v3 = random.randint(1, 101)
# v4 = random.randint(1, 101)
# v5 = random.randint(1, 101)

# bst = BinarySearchTree(5)


# bst.insert(v1)
# bst.insert(v2)
# bst.insert(v3)
# bst.insert(v4)
# bst.insert(v5)


# bst.for_each(cb)
# print(bst)

# print(bst.contains(6))
# print("arr: ", arr)


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print("in order")
bst.in_order_print(bst)

print("post order")
bst.post_order_dft(bst)

print("bft print")
bst.bft_print(bst)

print("dft_print")
bst.dft_print(bst)