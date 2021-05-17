import linkedList

class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.height = 0

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        else:
            return node.height

    @staticmethod
    def get_balance(node):
        if not node:
            return 0
        left_height = 0 if node.left_child is None else (Node.get_height(node.left_child) + 1)
        right_height = 0 if node.right_child is None else (Node.get_height(node.right_child) + 1)
        return left_height - right_height

    def __str__(self):
        return str(None if not self else self.key)

    def __repr__(self):
        return str(self)


class BalancedBinarySearchTree:
    def __init__(self, bbst_type):
        self.__root = None
        self.__type = bbst_type
        self.__size = 0

    def insert(self, item):
        if self.__root is None:
            self.__root = Node(item)
            self.__size += 1
        else:
            self.__root = self._insert(item, self.__root)

    def _insert(self, item, cur_node):
        if item < cur_node.key:
            if cur_node.left_child is None:
                cur_node.left_child = Node(item)
                self.__size += 1
            else:
                cur_node.left_child = self._insert(item, cur_node.left_child)
        elif item > cur_node.key:
            if cur_node.right_child is None:
                cur_node.right_child = Node(item)
                self.__size += 1
            else:
                cur_node.right_child = self._insert(item, cur_node.right_child)
        else:
            print("Value already in tree")
            return cur_node

        cur_node.height = 1 + max(Node.get_height(cur_node.left_child),
                                  Node.get_height(cur_node.right_child))
        balance = Node.get_balance(cur_node)

        if balance > 1 and item < cur_node.left_child.key:
            return self.right_rotate(cur_node)

        if balance < -1 and item > cur_node.right_child.key:
            return self.left_rotate(cur_node)

        if balance > 1 and item > cur_node.left_child.key:
            cur_node.left_child = self.left_rotate(cur_node.left_child)
            return self.right_rotate(cur_node)

        if balance < -1 and item < cur_node.right_child.key:
            cur_node.right_child = self.right_rotate(cur_node.right_child)
            return self.left_rotate(cur_node)

        return cur_node

    @staticmethod
    def left_rotate(cur_node):

        right_node = cur_node.right_child
        left_subtree = right_node.left_child

        right_node.left_child = cur_node
        cur_node.right_child = left_subtree

        if cur_node.left_child is None and cur_node.right_child is None:
            cur_node.height = 0
        else:
            cur_node.height = 1 + max(Node.get_height(cur_node.left_child),
                                      Node.get_height(cur_node.right_child))
        if right_node.left_child is None and right_node.right_child is None:
            right_node.height = 0
        else:
            right_node.height = 1 + max(Node.get_height(right_node.left_child),
                                        Node.get_height(right_node.right_child))

        return right_node

    @staticmethod
    def right_rotate(cur_node):
        left_node = cur_node.left_child
        right_subtree = left_node.right_child

        left_node.right_child = cur_node
        cur_node.left_child = right_subtree

        if cur_node.left_child is None and cur_node.right_child is None:
            cur_node.height = 0
        else:
            cur_node.height = 1 + max(Node.get_height(cur_node.left_child),
                                      Node.get_height(cur_node.right_child))
        if left_node.left_child is None and left_node.right_child is None:
            left_node.height = 0
        else:
            left_node.height = 1 + max(Node.get_height(left_node.left_child),
                                       Node.get_height(left_node.right_child))

        return left_node

    def bst_print_asc(self):
        str_representation = self.__bst_print_asc(self.__root)
        print(str_representation)

    def __bst_print_asc(self, node, str_representation=""):
        if node is not None:
            str_representation += self.__bst_print_asc(node.left_child)
            str_representation += (str(node) + ' ')
            str_representation += self.__bst_print_asc(node.right_child)
        return str_representation

    def bst_print_desc(self):
        str_representation = self.__bst_print_desc(self.__root)
        print(str_representation)

    def __bst_print_desc(self, node, str_representation=""):
        if node is not None:
            str_representation += self.__bst_print_desc(node.right_child)
            str_representation += (str(node) + ' ')
            str_representation += self.__bst_print_desc(node.left_child)
        return str_representation

    def total_sum(self):
        return self.__total_sum(self.__root)

    def __total_sum(self, node):
        if node is None:
            return 0
        return node.key + self.__total_sum(node.left_child) + self.__total_sum(node.right_child)

    def count_left_nodes(self):
        counter = self._count_left_nodes(self.__root)
        return counter

    def _count_left_nodes(self, node, counter=0):
        if node is not None:
            counter += self._count_left_nodes(node.right_child)
            if node.left_child is not None:
                counter += 1
            counter += self._count_left_nodes(node.left_child)
        return counter

    def sum_right_keys(self):
        sum_of_keys = self._sum_right_keys(self.__root)
        return sum_of_keys

    def _sum_right_keys(self, node, sum_of_keys=0):
        if node is not None:
            sum_of_keys += self._sum_right_keys(node.right_child)
            if node.right_child is not None:
                sum_of_keys += node.right_child.key
            sum_of_keys += self._sum_right_keys(node.left_child)
        return sum_of_keys

    def includes(self, item):
        cur_node = self.__root
        while cur_node and cur_node.key != item:
            if cur_node.key > item:
                cur_node = cur_node.left_child
            else:
                cur_node = cur_node.right_child
        return cur_node is not None

    def find(self, item):
        cur_node = self.__root
        while cur_node and cur_node.key != item:
            if cur_node.key > item:
                cur_node = cur_node.left_child
            else:
                cur_node = cur_node.right_child
        return cur_node

    def find_second_largest(self):
        cur_node = self.__root
        parent = None
        while True:
            if cur_node.right_child is None:
                if cur_node.left_child is not None:
                    return cur_node.left_child
                else:
                    return parent
            parent = cur_node
            cur_node = cur_node.right_child

    def inorder_traversal(self):
        return self._inorder_traversal(self.__root)

    def _inorder_traversal(self, root):
        keys = list()
        if root is not None:
            keys = self._inorder_traversal(root.left_child)
            keys.append(root.key)
            keys = keys + self._inorder_traversal(root.right_child)
        return keys

    def insert_bbst(self, other):
        keys = other.inorder_traversal()
        for key in keys:
            self.insert(key)

    def contains_bbst(self, other):
        self_keys = self.inorder_traversal()
        other_keys = other.inorder_traversal()
        return set(other_keys).issubset(self_keys)

    def find_father(self, item):
        cur_node = self.__root
        parent = None
        while cur_node and cur_node.key != item:
            if cur_node.key > item:
                parent = cur_node
                cur_node = cur_node.left_child
            else:
                parent = cur_node
                cur_node = cur_node.right_child
        if cur_node is None:
            return -10 ** 4
        else:
            if parent is not None:
                return parent.key

    def find_middle(self):
        keys = self.inorder_traversal()
        average = (keys[0] + keys[-1]) / 2
        min_diff = (keys[0] - average) ** 2
        nearest = keys[0]
        for key in keys:
            if min_diff > (key - average) ** 2:
                min_diff = (key - average) ** 2
                nearest = key
        return nearest

    def equals_bbst(self, other):
        return self._equals_bbst(self.__root, other.__root)

    def _equals_bbst(self, first_node, second_node):
        if first_node is None and second_node is None:
            return first_node is second_node
        return first_node.key == second_node.key and \
               self._equals_bbst(first_node.left_child, second_node.left_child) and \
               self._equals_bbst(first_node.right_child, second_node.right_child)

    def same_data(self, other):
        self_data = self.__bbst_data(self.__root)
        print(self_data)
        other_data = other.__bbst_data(other.__root)
        print(other_data)
        return sorted(self_data) == sorted(other_data)

    def __bbst_data(self, node, data=None):
        if data is None:
            data = []
        if node is not None:
            data += self.__bbst_data(node.left_child)
            data.append(node.key)
            data += self.__bbst_data(node.right_child)
        return data

    def search_with_parent(self, item):
        cur_node = self.__root
        parent = None
        while cur_node and cur_node.key != item:
            if cur_node.key > item:
                parent = cur_node
                cur_node = cur_node.left_child
            else:
                parent = cur_node
                cur_node = cur_node.right_child
        return cur_node, parent

    def search(self, item):
        cur_node = self.__root
        while cur_node and cur_node.key != item:
            if cur_node.key > item:
                cur_node = cur_node.left_child
            else:
                cur_node = cur_node.right_child
        return cur_node

    def common_ancestor(self, item1, item2):
        node1 = self.search(item1)
        node2 = self.search(item2)
        if not node1 or not node2:
            raise ValueError("Node not in LinkedList")
        return self._common_ancestor(node1, node2)

    def _common_ancestor(self, node1, node2):

        while node1 != node2:
            if node1 == self.__root or node2 == self.__root:
                break
            _, node1 = self.search_with_parent(node1.key)
            _, node2 = self.search_with_parent(node2.key)
        return node1

    def is_balanced(self):
        return self._is_balanced(self.__root) != -1

    def _is_balanced(self, node):
        if node is None:
            return 0
        left = self._is_balanced(node.left_child)
        if left == -1:
            return -1

        right = self._is_balanced(node.right_child)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)

    def preorder_traversal(self, node):
        keys = list()
        if node is None:
            return keys
        keys.append(node.key)
        keys += self.preorder_traversal(node.left_child)
        keys += self.preorder_traversal(node.right_child)
        return keys

    def _add(self, item, cur_node):
        if cur_node is None:
            self.__root = Node(item)
            return
        if item < cur_node.key:
            if cur_node.left_child is None:
                cur_node.left_child = Node(item)
            else:
                cur_node.left_child = self._add(item, cur_node.left_child)
        elif item > cur_node.key:
            if cur_node.right_child is None:
                cur_node.right_child = Node(item)
            else:
                cur_node.right_child = self._add(item, cur_node.right_child)
        else:
            print("Value already in tree")
        return cur_node

    def copy_bbst(self):
        copy_bbst = BalancedBinarySearchTree(self.__type)
        copy_bbst.__root = self.__root
        return copy_bbst

    def delete_even(self):
        keys = [i for i in self.inorder_traversal() if i % 2 != 0]
        self.__root = None
        for key in keys:
            self.insert(key)

    def symmetrical_bbst(self):
        keys = [i for i in self.preorder_traversal(self.__root)]
        copy_bbst = BalancedBinarySearchTree(self.__type)
        for key in keys:
            copy_bbst._symmetrical_add(key, copy_bbst.__root)
        return copy_bbst

    def _symmetrical_add(self, item, cur_node):
        if cur_node is None:
            self.__root = Node(item)
            return
        if item > cur_node.key:
            if cur_node.left_child is None:
                cur_node.left_child = Node(item)
                cur_node.left_child.parent = cur_node
            else:
                cur_node.left_child = self._add(item, cur_node.left_child)
        elif item < cur_node.key:
            if cur_node.right_child is None:
                cur_node.right_child = Node(item)
                cur_node.right_child.parent = cur_node
            else:
                cur_node.right_child = self._add(item, cur_node.right_child)
        else:
            print("Value already in tree")
        return cur_node

    def bst_list(self):
        return self.__bst_list(self.__root, linkedList.SortedLinkedList(self.__type))

    def __bst_list(self, node, linked_list):
        if node is not None:
            linked_list.extend(self.__bbst_data(node.left_child))
            linked_list.add_item(node.key)
            linked_list.extend(self.__bbst_data(node.right_child))
        return linked_list

    def make_empty(self):
        self.__root = None
        self.__size = 0

    def size(self):
        return self._size(self.__root)

    def _size(self, node):
        if node is None:
            return 0
        return (1 if self.__root is not None else 0) + self._size(node.left_child) + self._size(node.right_child)

    def __eq__(self, other):
        return self.equals_bbst(other)

    def __ne__(self, other):
        return not self.equals_bbst(other)

    def __len__(self):
        return self.__size