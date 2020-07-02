class Node:
    def __init__(self, item=None):
        self.value = item
        self.next = None

class DeLinkList:
    def __init__(self, node=None):
        self.__head = node

    # 检测链表是否为空
    def is_empty(self):
        return self.__head is None

    # 从尾部添加元素
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return None
        cursor = self.__head
        while cursor.next != self.__head:
            cursor = cursor.next
        cursor.next = node
        node.next = self.__head

    # 从头部添加元素
    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return None
        cursor = self.__head
        while cursor.next != self.__head:
            cursor = cursor.next
        node.next = self.__head
        self.__head = node
        cursor.next = self.__head

    # 检测链表中元素个数
    def length(self):
        cursor = self.__head
        count = 0
        if self.is_empty():
            return count
        while True:
            count += 1
            if cursor.next == self.__head:
                break
            cursor = cursor.next
        return count

    # 打印链表中的数据
    def outPut(self):
        cursor = self.__head
        if self.is_empty():
            return None
        count = 1
        while count < 2:
            print(cursor.value, end=' ')
            if cursor.next == self.__head:
               count += 1
               print()
            cursor = cursor.next

#     查找链表中是否存在某元素
    def search(self, item):
        if self.is_empty():
            return False
        cursor = self.__head
        while True:
            if cursor.value == item:
                return True
            if cursor.next == self.__head:
                return False
            cursor = cursor.next

#     删除指定元素
    def remove(self, item):
        cursor = self.__head
        prev = None
        if self.is_empty():
            return None
        while True:
            if cursor.value == item:
                # 检测元素为头元素，且链表只有一个元素
                if self.length() == 1:
                    self.__head = None
                    return None
                # 检测结果为头节点，链表包含多个节点
                if self.__head == cursor:
                    while True:
                        if cursor.next == self.__head:
                            break
                        cursor = cursor.next
                    self.__head = self.__head.next
                    cursor.next = self.__head
                    return None
                # 要删除的元素为尾节点
                if cursor.next == self.__head:
                    prev.next = self.__head
                    return None
                # 要删除的元素为中间节点
                prev.next = cursor.next
            if cursor.next == self.__head:
                return None
            prev = cursor
            cursor = cursor.next

    # 指定位置插入元素
    def insert(self, pos, item):
        node = Node(item)
        cursor = self.__head
        prev = None
        count = 0
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            return None
        elif pos <= 0:
            return self.add(item)
        elif pos >= self.length():
            return self.append(item)
        else:
            while count != pos:
                count += 1
                prev = cursor
                cursor = cursor.next
            prev.next = node
            node.next = cursor


if __name__ == '__main__':
    ll = DeLinkList()
    print(ll.search(1))
    ll.add(100)
    print(ll.search(1))
    ll.add(1)
    print(ll.search(1))
    ll.append(1)
    ll.append(10)
    ll.append(100)
    ll.outPut()
    ll.remove(1)
    ll.outPut()
    ll.remove(100)
    ll.remove(100)
    ll.remove(1)
    ll.remove(10)
    print(ll.is_empty())
    ll.insert(0,5)
    ll.insert(0,5)
    ll.insert(1,4)
    ll.insert(1,3)
    ll.insert(1,2)
    ll.insert(1,1)
    ll.insert(5,1)
    ll.insert(7,1)
    # ll.remove(10)
    ll.outPut()
    print(ll.search(1))
    print(ll.length())
