# coding: utf-8
class Node:
    def __init__(self, item=None):
        self.value = item
        self.lchild = None
        self.rchild = None


# 二叉树Binary tree
class BinaryTree:
    def __init__(self, item=None):
        self.__root = item

    # 检测二叉树中是否有元素
    def isEmpty(self):
        return self.__root is None

    # 向二叉树中添加元素
    def addNode(self, item):
        node = Node(item)
        if self.isEmpty():
            self.__root = node
            return None
        queue = [self.__root]
        while True:
            cursor = queue.pop(0)
            if cursor.lchild is None:
                cursor.lchild = node
                break
            else:
                queue.append(cursor.lchild)
            if cursor.rchild is None:
                cursor.rchild = node
                break
            else:
                queue.append(cursor.rchild)

    # 层级遍历
    def traverse(self):
        if self.isEmpty():
            return None
        queue = [self.__root]
        while queue:
            cursor = queue.pop(0)
            print(cursor.value, end=' ')
            if cursor.lchild is not None:
                queue.append(cursor.lchild)
            if cursor.rchild is not None:
                queue.append(cursor.rchild)
        print()

    # 先序遍历
    def preorderTraverse(self):
        if self.isEmpty():
            return None
        stack = [self.__root]
        while stack:
            cursor = stack.pop()
            print(cursor.value, end=' ')
            if cursor.rchild is not None:
                stack.append(cursor.rchild)
            if cursor.lchild is not None:
                stack.append(cursor.lchild)
        print()

    # 中序遍历
    def middleTraverse(self):
        if self.isEmpty():
            return None
        stack = [self.__root]
        while stack:
            cursor = stack.pop()
            if isinstance(cursor, Node):
                if cursor.rchild or cursor.lchild:
                    if cursor.rchild:
                        stack.append(cursor.rchild)
                    stack.append(cursor.value)
                    if cursor.lchild:
                        stack.append(cursor.lchild)
                else:
                    print(cursor.value, end=' ')
            else:
                print(cursor, end=' ')
        print()

    # 后续遍历
    def tailTraverse(self):
        if self.isEmpty():
            return None
        stack = [self.__root]
        while stack:
            cursor = stack.pop()
            if isinstance(cursor, Node):
                if cursor.lchild or cursor.rchild:
                    stack.append(cursor.value)
                    if cursor.rchild:
                        stack.append(cursor.rchild)
                    if cursor.lchild:
                        stack.append(cursor.lchild)
                else:
                    print(cursor.value, end=' ')
            else:
                print(cursor, end=' ')
        print()

if __name__ == '__main__':
    import random
    testList = [i for i in range(10)]
    random.shuffle(testList)               b
    binaryTree = BinaryTree()
    for item in testList:
        binaryTree.addNode(item)
    # binaryTree.addNode(1)
    # binaryTree.addNode(2)
    # binaryTree.addNode(3)
    # binaryTree.addNode(4)
    # binaryTree.addNode(5)
    # binaryTree.addNode(6)
    # binaryTree.addNode(7)
    # binaryTree.addNode(8)
    # binaryTree.addNode(9)
    binaryTree.traverse()
    binaryTree.preorderTraverse()
    binaryTree.middleTraverse()
    binaryTree.tailTraverse()

