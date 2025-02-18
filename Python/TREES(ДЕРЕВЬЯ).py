# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None  # Левый дочерний узел
#         self.right = None  # Правый дочерний узел
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         if self.root is None:
#             self.root = TreeNode(value)
#         else:
#             self._insert_recursively(self.root, value)
#
#     def _insert_recursively(self, node, value):
#         if value < node.value:  # Сравнение строк идет по лексикографическому порядку
#             if node.left is None:
#                 node.left = TreeNode(value)
#             else:
#                 self._insert_recursively(node.left, value)
#         else:
#             if node.right is None:
#                 node.right = TreeNode(value)
#             else:
#                 self._insert_recursively(node.right, value)
#
#     def inorder_traversal(self, node):
#         if node:
#             self.inorder_traversal(node.left)
#             print(node.value, end=' ')
#             self.inorder_traversal(node.right)
#
# # Пример использования
#
# binary_tree = BinaryTree()
# binary_tree.insert("apple")
# binary_tree.insert("banana")
# binary_tree.insert("cherry")
# binary_tree.insert("date")
# binary_tree.insert("fig")
# binary_tree.insert("grape")
#
# print("Inorder traversal of the binary tree:")
# binary_tree.inorder_traversal(binary_tree.root)


############################################################################


# import matplotlib.pyplot as plt
#
# class TreeNode:
#     def __init__(self, key):
#         self.val = key
#         self.left = None
#         self.right = None
#
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
#             self.inorder_traversal(node.left)
#             print(node.val, end=' ')
#             self.inorder_traversal(node.right)
#
#     def postorder_traversal(self, node):
#         if node:
#             self.postorder_traversal(node.left)
#             self.postorder_traversal(node.right)
#             print(node.val, end=' ')
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
# visualize_tree(b)


############################################################################ 1
# Реализовать метод для нахождения максимального значения в дереве. Реализуйте метод для поиска максимального значения в
# бинарном дереве поиска. Этот метод должен быть частью класса BinarySearchTree

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:         # 5 < 10
            if node.left is None:
                node.left = TreeNode(key)  # key = 5
            else:
                self._insert(node.left, key)  # node.left = 6, key = 5
        else:  # 50 > 10
            if node.right is None:
                node.right = TreeNode(key)  # key = 50
            else:
                self._insert(node.right, key)  # node.right = 20, key = 50

    def search_max(self):
        if self.root is None:
            return None  # Дерево пустое
        return self._search_max(self.root)


    def _search_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current.val


b = BinarySearchTree()

b.insert(10)
b.insert(6)
b.insert(20)
b.insert(4)
b.insert(5)
b.insert(15)
b.insert(30)
b.insert(25)
b.insert(8)

max_value = b.find_max()
print(f"Максимальное значение в BST: {max_value}")