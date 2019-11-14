# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


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
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can't go right any more
        while self.right is not None:
            self = self.right

        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # visit each node exactly one time
        # go left until you cant anymore, then go back and go right
        # somewhere in here call cb(node)
        pass

   # DAY 2 Project -----------------------

   # Print all the values in order from low to high
   # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)

print(bst)

bst.insert(2)
print(bst)
bst.insert(3)
print(bst)
bst.insert(7)
print(bst)
bst.insert(6)
print(bst)
bst.insert(8)
print(bst)
bst.insert(10)
print(bst)
print("4 right: ", bst.right.right.right.right)
print("get_max: ", bst.get_max())
