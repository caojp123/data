# 栈
# class Stack:
#     def __init__(self):
#         self.__stack = []
#
#     # 添加元素
#     def append(self, item):
#         self.__stack.append(item)
#
#     # 弹出元素
#     def pop(self):
#         if self.__stack:
#             return self.__stack.pop()
#         else:
#             return None
# if __name__ == '__main__':
#     stack = Stack()
#     stack.append(1)
#     stack.append(2)
#     stack.append(3)
#     print(stack.pop())
#     stack.append(4)
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())

# # 队列
# class Queue:
#     def __init__(self):
#         self.__queue = []
#
#     # 向队列中添加元素
#     def append(self, item):
#         self.__queue.append(item)
#
#     # 获取队列中的元素
#     def pop(self):
#         if self.__queue:
#             return self.__queue.pop(0)
#         else:
#             return None
# if __name__ == '__main__':
#     queue = Queue()
#     queue.append(1)
#     queue.append(2)
#     queue.append(3)
#     queue.append(4)
#     print(queue.pop())
#     queue.append(5)
#     print(queue.pop())
#     print(queue.pop())
#     print(queue.pop())
#     print(queue.pop())

# class DoublyQueue:
#     def __init__(self):
#         self.__dq = []
#
#     # 头部添加
#     def headAdd(self, item):
#         self.__dq.insert(0, item)
#
#     # 尾部添加元素
#     def tailAdd(self, item):
#         self.__dq.append(item)
#
#     # 头部获取
#     def headPop(self):
#         if self.__dq:
#             return self.__dq.pop(0)
#         else:
#             return None
#
#     # 从尾部获取元素
#     def tailPop(self):
#         if self.__dq:
#             return self.__dq.pop()
#         else:
#             return None
#
# if __name__ == '__main__':
#        doublyQueue = DoublyQueue()
#        doublyQueue.headAdd(1)
#        doublyQueue.headAdd(2)
#        doublyQueue.tailAdd(3)
#        while True:
#            count = doublyQueue.headPop()
#            if count:
#                print(count, end=' ')
#            else:
#                break
