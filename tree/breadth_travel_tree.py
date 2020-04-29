
class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem       # 值
        self.lchild = None      # 左子树
        self.rchild = None      # 右子树


class Tree(object):
    """
        二叉树
        完成了插入和广度遍历
    """
    def __init__(self):
        self.root = None        # 根节点

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:                    # 代表树的节点
            cur_node = queue.pop(0)     # 弹出第一个节点
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):       # 广度遍历 也称层次遍历
        if self.root is None:       # 为空直接return
            return
        queue = [self.root]         # 从根节点开始循环
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:     # 左子树不为空，将左子树加入循环列表
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:     # 右子树不为空，将右子树加入循环列表
                queue.append(cur_node.rchild)


if __name__ == "__main__":
    t = Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.breadth_travel()
