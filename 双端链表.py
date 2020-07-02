# coding : utf-8
class Node:
    def __init__(self, item=None):
        self.value = item
        self.next = None
        self.prev = None


# 双端链表
class DoublyLinkList:
    def __init__(self, item=None):
        self.__head = None
        self.__tail = None

    # 检测链表是否为空
    def isEmpty(self):
        return self.__head is None

    # 从尾部添加元素
    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self.__head = node
            self.__tail = node
            return None
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node

    # 从链表头部添加元素
    def add(self, item):
        node = Node(item)
        if self.isEmpty():
            self.__head = node
            self.__tail = node
            return None
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    #  从头部开始遍历
    def traverseFromHead(self):
        cursor = self.__head
        while cursor is not None:
            print(cursor.value, end=' ')
            cursor = cursor.next
        print()

    # 从尾部开始遍历
    def traverseFromTail(self):
        cursor = self.__tail
        while cursor is not None:
            print(cursor.value, end=' ')
            cursor = cursor.prev
        print()

    # 返回链表长度
    def length(self):
        cursor = self.__head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.next
        return count

    # 从左侧开始查询链表中是否拥有某元素
    def lsearch(self, item):
        cursor = self.__head
        while cursor is not None:
            if cursor.value == item:
                return True
            cursor = cursor.next
        return False

# 从右侧开始查询链表中是否拥有某元素
    def rsearch(self, item):
        cursor = self.__tail
        while cursor is not None:
            if cursor.value == item:
                return True
            cursor = cursor.prev
        return False

    # 在链表指定位置插入元素
    def insert(self, pos, item):
        node = Node(item)
        cursor = self.__head
        prev = None
        count = 0
        if self.isEmpty():
            self.__head = node
            self.__tail = node
            return None
        elif pos <= 0:
            return self.add(item)
        elif pos >= self.length():
            return self.append(item)
        else:
            while count != pos:
                prev = cursor
                cursor = cursor.next
                count += 1
            node.prev = prev
            node.next = cursor
            prev.next = node
            cursor.prev = node

    # 删除链表中的指定元素
    def remove(self, item):
        cursor = self.__head
        while cursor is not None:
            if cursor.value == item:
                if self.length() == 1:
                    self.__head = None
                    self.__tail = None
                    return cursor.value
                elif cursor == self.__head:
                    self.__head = cursor.next
                    self.__head.prev = None
                    return cursor.value
                elif cursor == self.__tail:
                    self.__tail = cursor.prev
                    self.__tail.next = None
                    return  cursor.value
                else:
                    cursor.prev.next = cursor.next
                    cursor.next.prev = cursor.prev
                    return cursor.value
            cursor = cursor.next


if __name__ == '__main__':
    doublyLinkList = DoublyLinkList()
    doublyLinkList.append(1)
    doublyLinkList.append(2)
    doublyLinkList.append(3)
    doublyLinkList.append(4)
    doublyLinkList.append(5)
    doublyLinkList.add(0)
    doublyLinkList.insert(1,2)
    doublyLinkList.insert(0,0)
    doublyLinkList.insert(9,0)
    doublyLinkList.traverseFromHead()
    doublyLinkList.remove(0)
    doublyLinkList.remove(0)
    doublyLinkList.remove(0)
    doublyLinkList.remove(1)
    doublyLinkList.traverseFromHead()
    doublyLinkList.traverseFromTail()
    print('当前链表长度： %s' % (doublyLinkList.length()))
    print(doublyLinkList.lsearch(2))
    print(doublyLinkList.rsearch(-2))