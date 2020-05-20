class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def preOrder(root):
    '''
    We shall solve this problem through recursion.
    In preOder traversal, print the value first and then traverse.
    '''

    if root:

        print(root.info)

        preOrder(root.left)

        preOrder(root.right)


if __name__ == "__main__":

    tree = BinarySearchTree()
    arr = [1, 2, 5, 3, 6, 4]

    for item in arr:
        tree.create(item)

    preOrder(tree.root)
