# 创建单向链表节点类
class Node:
    def __init__(self, item):
        self.value = item
        self.next = None


# 创建链表类
class LinkTable:
    def __init__(self, node=None):
        self.__header = node

    # 从头部添加元素
    def add(self, item):
        node = Node(item)
        if self.__header == None:
            self.__header = node
        else:
            cursor = self.__header
            self.__header = node
            self.__header.next = cursor

    # 从尾部添加元素
    def append(self, item):
        node = Node(item)
        if self.__header == None:
            self.__header = node
        else:
            cursor = self.__header
            while True:
                if cursor.next == None:
                    cursor.next = node
                    break
                cursor = cursor.next

    # 查看链表是否为空
    def is_empty(self):
        return self.__header == None

    # 查询链表元素个数
    def length(self):
        count = 0
        cursor = self.__header
        while cursor != None:
            count += 1
            cursor = cursor.next
        return count

    # 查询链表中是否存在指定元素
    def search(self, item):
        cursor = self.__header
        while cursor != None:
            if cursor.value == item:
                return True
            cursor = cursor.next
        return False

    # 删除链表中指定元素
    def remove(self, item):
        cursor = self.__header
        pre = None
        # 删除元素为链表的第一个元素
        if pre == None and cursor.value == item:
            self.__header = cursor.next
            return  None
        while cursor != None:
            if cursor.value == item:
                pre.next = cursor.next
                break
            pre = cursor
            cursor = cursor.next

    # 在指定位置添加元素
    def insert(self, pos, item):
        node = Node(item)
        cursor = self.__header
        pre = None
        if self.is_empty():
            self.__header = node
        elif pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            count = 0
            while cursor != None:
                count += 1
                pre = cursor
                cursor = cursor.next
                if count == pos:
                    pre.next = node
                    node.next = cursor
                    break

    # 输出链表中的元素
    def outPut(self):
        cursor = self.__header
        while cursor != None:
            print(cursor.value, end=' ')
            cursor = cursor.next
        print()
