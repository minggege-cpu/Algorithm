"""
    霍夫曼树  最优二叉树
"""


# 节点
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


# 面对对象的创建方式
class Huffman(object):

    def __init__(self, items=[]):
        while len(items)!=1:
            a, b = items[0], items[1]
            newvalue = a.value + b.value
            newnode = Node(value=newvalue)
            newnode.left, newnode.right = a, b
            items.remove(a)
            items.remove(b)
            items.append(newnode)
            items = sorted(items, key=lambda node: int(node.value))
            # 每次都要记得更新新的霍夫曼树的根节点
            self.root = newnode

    # 遍历
    def travel(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end='\t')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()


# 面向过程的创建方式
def create_huffman_tree(lists):
    while len(lists)>1:
        a, b = lists[0], lists[1]
        node = Node(value=int(a.value+b.value))
        node.left, node.right = a, b
        lists.remove(a)
        lists.remove(b)
        lists.append(node)
        lists = sorted(lists, key=lambda node: node.value)
    return lists


# 遍历
def scan(root):
    if root:
        queue = [root]
        while queue:
            current = queue.pop(0)
            print(current.value, end='\t')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


if __name__ == '__main__':
    ls = [Node(i) for i in range(1, 5)]
    huffman = Huffman(items=ls)
    huffman.travel()
    print('===================================')
    lssl = [Node(i) for i in range(1, 5)]
    root = create_huffman_tree(lssl)[0]
    scan(root)


