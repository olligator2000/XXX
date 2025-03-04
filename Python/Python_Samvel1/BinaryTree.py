import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         if self.root is None:
#             self.root = TreeNode(key)
#         else:
#             self._insert(self.root, key)
#
#     def _insert(self, node, key):
#         if key < node.val:         # 5 < 10
#             if node.left is None:
#                 node.left = TreeNode(key)  # key = 5
#             else:
#                 self._insert(node.left, key)  # node.left = 6, key = 5
#         else:  # 50 > 10
#             if node.right is None:
#                 node.right = TreeNode(key)  # key = 50
#             else:
#                 self._insert(node.right, key)  # node.right = 20, key = 50
#
#     def search(self, key):
#         return self._search(self.root, key)
#
#     def _search(self, node, key):
#         if node is None or key == node.val:
#             return node
#         if key < node.val:
#             return self._search(node.left, key)
#         return self._search(node.right, key)
#
#     def preorder_traversal(self, node):
#         if node:
#             print(node.val, end=' ')
#             self.preorder_traversal(node.left)
#             self.preorder_traversal(node.right)
#
#     def inorder_traversal(self, node):
#         if node:
#             self.preorder_traversal(node.left)
#             print(node.val, end=' ')
#             self.preorder_traversal(node.right)
#
#     def postorder_traversal(self, node):
#         if node:
#             self.preorder_traversal(node.left)
#             self.preorder_traversal(node.right)
#             print(node.val, end=' ')
#
#     def delete(self, key):
#         return  self._delete(self.root, key)
#
#     def _delete(self, node, key):
#         if node is None:
#             return node
#
#         if key < node.val: # 6 < 10
#             node.left = self._delete(node.left, key)
#         elif key > node.val:  # 6 > 10
#             node.right = self._delete(node.right, key)
#         else:
#             if node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left
#
#             node.val = self._min_value_node(node.right).val   # 25
#
#             node.right = self._delete(node.right, node.val)    # 25
#
#         return node
#
#     def _min_value_node(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current
#
#
#
#
#
# def plot_tree(node, pos=None, level=0, h_shift=1.5, v_shift=1.5, parent_pos=None):
#     if node is None:
#         return
#     if pos is None:
#         pos = (0, 0)
#     x, y = pos
#     plt.text(x, y, str(node.val), ha='center', va='center',
#              bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
#     if parent_pos:
#         px, py = parent_pos
#         plt.plot([px, x], [py, y], 'k-')
#     if node.left:
#         plot_tree(node.left, pos=(x - h_shift / (level + 1), y - v_shift), level=level + 1, parent_pos=pos)
#     if node.right:
#         plot_tree(node.right, pos=(x + h_shift / (level + 1), y - v_shift), level=level + 1, parent_pos=pos)
#
# def visualize_tree(tree):
#     plt.figure(figsize=(12, 8))
#     plot_tree(tree.root)
#     plt.axis('off')
#     plt.show()
#
# b = BinarySearchTree()
#
# b.insert(10)
# b.insert(6)
# b.insert(20)
# b.insert(4)
# b.insert(5)
# b.insert(15)
# b.insert(30)
# b.insert(25)
# b.insert(8)
#
# print(b.search(8))   #8
# print(b.search(80))  #None
# print(b.search(30))  #30
# print(b.search(60))  #None
#
# print()
# b.preorder_traversal(b.root)
# print()
# b.inorder_traversal(b.root)
# print()
# b.postorder_traversal(b.root)
# print()
#
#
# b.delete(20)
# b.delete(6)
#
# visualize_tree(b)
#



import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            return self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                return self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
             return self._insert(node.right, key)

    def _find_max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def find_max_node(self):
        return self._find_max_node(self.root)

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_min_node(self):
        return self._find_min_node(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return self._count_leaves(node.left) + self._count_leaves(node.right)

    def count_leaves(self):
        return self._count_leaves(self.root)


def plot_tree(node, pos=None, level=0, h_shift=1.5, v_shift=1.5, parent_pos=None):
    if node is None:
        return
    if pos is None:
        pos = (0, 0)
    x, y = pos
    plt.text(x, y, str(node.val), ha='center', va='center',
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    if parent_pos:
        px, py = parent_pos
        plt.plot([px, x], [py, y], 'k-')
    if node.left:
        plot_tree(node.left, pos=(x - h_shift / (level + 1), y - v_shift), level=level + 1, parent_pos=pos)
    if node.right:
        plot_tree(node.right, pos=(x + h_shift / (level + 1), y - v_shift), level=level + 1, parent_pos=pos)

def visualize_tree(tree):
    plt.figure(figsize=(12, 8))
    plot_tree(tree.root)
    plt.axis('off')
    plt.show()

b = BinarySearchTree()
b.insert(10)
b.insert(20)
b.insert(30)
b.insert(40)
b.insert(50)
b.insert(5)
b.insert(9)
b.insert(45)
b.insert(23)
b.insert(32)
b.insert(1)
b.insert(7)
b.insert(90)


print(b.find_max_node().val)
print(b.find_min_node().val)

visualize_tree(b)









