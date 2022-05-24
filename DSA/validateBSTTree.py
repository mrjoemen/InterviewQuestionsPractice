"""

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

--

https://leetcode.com/problems/validate-binary-search-tree/submissions/


"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root)

    def isValidBSTHelper(self, root, minimum=float('-inf'), maximum=float('inf')):
        #This method works because whenever we call the recursion, it passes the current value as something to compare for the next cycle
        # whether if the value that is going to be used as a max or a min will depend if it's going to the right or left tree
        if root == None:
            return True

        if root.val <= minimum or root.val >= maximum:
            print(f"{minimum} <= {root.val} < {maximum}")
            return False
        
        print(f"{minimum} <= {root.val} < {maximum}")
            
        
        return self.isValidBSTHelper(root.right, root.val, maximum) and self.isValidBSTHelper(root.left, minimum, root.val)
