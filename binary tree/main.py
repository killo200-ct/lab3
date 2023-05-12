import csv


class Node:
    def init(self, test):
        self.test = test

        self.left = None
        self.right = None


class BinarySearchTree:
    def init(self):

        self.root = None

    def insert(self, test):
        new_node = Node(test)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if new_node.test.test_num < current.test.test_num:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, test_num):
        if self.root is None:
            return None
        else:
            current = self.root
            while current is not None:
                if test_num == current.test.test_num:
                    return current.test
                elif test_num < current.test.test_num:
                    current = current.left
                else:
                    current = current.right
            return None

    def remove(self, test_num):
        if self.root is None:
            return False
        elif self.root.test.test_num == test_num:
            if self.root.left is None:
                self.root = self.root.right
            elif self.root.right is None:
                self.root = self.root.left
            else:
                successor = self._find_successor(self.root.right)
                self.root.test = successor.test
                self._remove_node(self.root.right, successor)
            return True
        else:
            parent = None
            current = self.root
            while current is not None:
                if test_num == current.test.test_num:
                    if current.left is None:
                        if parent.left == current:
                            parent.left = current.right
                        else:
                            parent.right = current.right
                    elif current.right is None:
                        if parent.left == current:
                            parent.left = current.left
                        else:
                            parent.right = current.left
                    else:
                        successor = self._find_successor(current.right)
                        current.test = successor.test
                        self._remove_node(current.right, successor)
                    return True
                elif test_num < current.test.test_num:
                    parent = current
                    current = current.left
                else:
                    parent = current
                    current = current.right
            return False

    def _find_successor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _remove_node(self, node, to_remove):
        if node == to_remove:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                successor = self._find_successor(node.right)
                node.test = successor.test
                self._remove_node(node.right, successor)
        elif to_remove.test.test_num < node.test.test_num:
            self._remove_node(node.left, to_remove)
        else:
            self._remove_node(node.right, to_remove)

    def traverse_preorder(self, node, tests):
        if node is not None:
            tests.append(node.test)
            self.traverse_preorder(node.left, tests)
            self.traverse_preorder(node.right, tests)

    def traverse_postorder(self, node, tests):
        if node is not None:
            self.traverse_postorder(node.left, tests)
            self.traverse_postorder(node.right, tests)
            tests.append(node.test)

    def traverse_inorder(self, node, tests):
        if node is not None:
            self.traverse_in

        order(node.left, tests)
        tests.append(node.test)
        self.traverse_inorder(node.right, tests)

    bst = BinarySearchTree()

    with open('tests.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
    next(reader)  # skipping the header row
    for row in reader:
        test = Test(int(row[0]), row[1], float(row[2]), float(row[3]))
        bst.insert(test)

    preorder_tests = []
    bst.traverse_preorder(bst.root, preorder_tests)
    print("Preorder traversal:", [test.test_num for test in preorder_tests])

    postorder_tests = []
    bst.traverse_postorder(bst.root, postorder_tests)
    print("Postorder traversal:", [test.test_num for test in postorder_tests])

    inorder_tests = []
    bst.traverse_inorder(bst.root, inorder_tests)
    print("Inorder traversal:", [test.test_num for test in inorder_tests])

    searched_test = bst.search(1001)
    if searched_test is not None:
        print(f"Test {searched_test.test_num} found with result {searched_test.result}.")
    else:
        print("Test not found.")

    removed = bst.remove(1003)
    if removed:
        print("Test removed.")
    else:
        print("Test not found.")

    inorder_tests = []
    bst.traverse_inorder(bst.root, inorder_tests)
    print("Inorder traversal after removing a node:", [test.test_num for test in inorder_tests])
