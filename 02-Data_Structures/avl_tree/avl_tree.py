"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    def max_depth(self):
        if not self:
            return 0
        left_depth = -1
        right_depth = -1
        if self.node.left:
            left_depth = self.node.left.max_depth()
        if self.node.right:
            right_depth = self.node.right.max_depth()

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        if not self.node:
            return 0
        self.height = self.max_depth()
    

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        balance = self.balance
        if self.node.right and self.node.left:
            balance = self.node.left.max_depth() - self.node.right.max_depth()
        elif self

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        if not self.node:
            return
        self.node.right = self.node
        self.node = self.node.left

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        if not self.node:
            return
        self.node.left = self.node
        self.node = self.node.right

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        tree_hgt = self.max_depth()
        if tree_hgt > 1 and self.node.key <self.node.left.node.key:
            self.right_rotate()
        elif tree_hgt < -1 and self.node.key > self.node.right.node.key
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        pass
