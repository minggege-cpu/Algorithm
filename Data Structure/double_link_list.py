"""
        使用python实现双向链表
        is_empty：判断是否为空
        length： 获取链表长度
        travel：便利链表
        add：从头部添加
        append：从尾部添加
        insert：指定位置添加
        remove：删除
        search:查询是否存在
"""


class Node(object):
    """结点"""
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """获取链表长度"""
        """ cur 游标 用来移动遍历节点 """
        cur = self.__head
        """ 游标移动次数 即代表链表长度"""
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表 """
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def add(self, item):
        """ 从头部添加 """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
            node.next.prev = node

    def append(self, item):
        """ 从尾部添加 """
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        指定位置添加
        pos  位置参数   从零开始
        """
        if pos > self.length()-1:
            self.append(item)
        elif pos <= 0:
            self.add(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count != pos:
                cur = cur.next
                count += 1
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除指定的元素"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 删除的元素为头节点
                if cur == self.__head:
                    # 链表长度为一的情况
                    if cur.next:
                        cur.next.prev = None
                        self.__head = cur.next
                    else:
                        self.__head = None
                    return
                cur.prev.next = cur.next
                # 需要判断删除的是否为尾节点
                if cur.next:
                    cur.next.prev = cur.prev
                return
            else:
                cur = cur.next

    def search(self, item):
        """查找元素"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


node = Node(300)
dl = DoubleLinkList(node)
dl.add(1)
dl.add(2)
dl.append(3)
dl.insert(2, 1000)
dl.remove(3)
dl.travel()




