

class ogGrammar(object):
    def __init__(self, start, overs, production):
        self.start = start                          # 开始符号
        self.overs = overs                          # 终结符号
        self.production = production                # 产生式
        self.nontermainals = production.keys()      # 产生式左部集合
        # FirstVT集
        self.FirstVT = {nontermainal: [] for nontermainal in self.nontermainals}
        # LastVt集
        self.LastVT = {nontermainal: [] for nontermainal in self.nontermainals}
        self.get_firstVT()
        self.get_lastVT()

    # 运用递归的方法获取非终结字符的FirstVT集
    def getFirstVt(self, nontermainal):
        l = []
        if nontermainal in memo1:
            return memo1[nontermainal]
        # 产生式右部
        right = self.production[nontermainal]
        for r in right:
            # 右部第一个字符为终结字符
            if r[0] in self.overs:
                # 直接加入列表
                l.append(r[0])
                continue
            # 右部串长度大于一并且第一个字符为非终结字符第二个字符为终结字符
            elif len(r) > 1 and r[0] not in self.overs and r[1] in self.overs:
                # 第二个字符直接加入列表
                l.append(r[1])
                # 首字符不等于当前字符
                if r[0] != nontermainal:
                    # 递归计算
                    l += self.getFirstVt(r[0])
                # 添加备忘录的方式  也是跳出递归循环的条件
                if r[0] in memo1:
                    return memo1[r[0]] + l
                else:
                    # 加入到备忘录
                    memo1[r[0]] = l
            elif r[0] not in self.overs:
                if r[0] != nontermainal:
                    l += self.getFirstVt(r[0])
                if r[0] in memo1:
                    return memo1[r[0]] + l
                else:
                    memo1[r[0]] = l

        return list(set(l))

    def getLastVt(self, nontermainal):
        l = []
        if nontermainal in memo2:
            return memo2[nontermainal]
        right = self.production[nontermainal]
        for r in right:
            if r[-1] in self.overs:
                l.append(r[-1])
                continue
            elif len(r) > 1 and r[-1] not in self.overs and r[-2] in self.overs:
                l.append(r[-2])
                if r[-1] != nontermainal:
                    l += self.getLastVt(r[-1])
                if r[-1] in memo2:
                    return memo2[r[-1]] + l
                else:
                    # 加入到备忘录
                    memo2[r[-1]] = l
            elif r[-1] not in self.overs:
                if r[-1] != nontermainal:
                    l += self.getLastVt(r[-1])
                if r[-1] in memo2:
                    return memo2[r[-1]] + l
                else:
                    # 加入到备忘录
                    memo2[r[-1]] = l
        return list(set(l))

    def get_firstVT(self):
        # 第一轮求FirstVT 产生式右部为终结字符的情况
        # 循环所有产生式左部
        for nontermainal in self.nontermainals:
            # 循环所有产生式右部
            for right in self.production[nontermainal]:
                # 产生式右部第一个字符串为终结字符直接加入
                if right != '' and right[0] in self.overs:
                    self.FirstVT[nontermainal].append(right[0])
                elif right != '' and right[0] not in self.overs:
                    # 第一个字符为非终结符并且第二个字符为终结字符
                    if len(right) > 1 and right[1] in self.overs:
                        self.FirstVT[nontermainal].append(right[1])
                        l = self.getFirstVt(right[0])
                        # 追加
                        self.FirstVT[nontermainal] += l
                        # 去重
                        self.FirstVT[nontermainal] = list(set(self.FirstVT[nontermainal]))
                    # 产生式右部第一个字符为非终结符  第二个没有或者为非终结符
                    else:
                        l = self.getFirstVt(right[0])
                        self.FirstVT[nontermainal] += l
                        self.FirstVT[nontermainal] = list(set(self.FirstVT[nontermainal]))

    def get_lastVT(self):
        for nontermainal in self.nontermainals:
            for right in self.production[nontermainal]:
                if right != '' and right[-1] in self.overs:
                    self.LastVT[nontermainal].append(right[-1])
                elif right != '' and right[-1] not in self.overs:
                    if len(right) > 1 and right[-2] in self.overs:
                        self.LastVT[nontermainal].append(right[-2])
                        l = self.getLastVt(nontermainal)
                        self.LastVT[nontermainal] += l
                        self.LastVT[nontermainal] = list(set(self.LastVT[nontermainal]))
                    # elif len(right) == 1:
                    else:
                        l = self.getLastVt(nontermainal)
                        self.LastVT[nontermainal] += l
                        self.LastVT[nontermainal] = list(set(self.LastVT[nontermainal]))


if __name__ == "__main__":
    memo1 = {}
    memo2 = {}
    start = 'E'
    overs = ['+', '*', '^', '(', ')', 'i']
    production = {
        'E': ['E+T', 'T'],
        'T': ['T*F', 'F'],
        'F': ['P^F', 'P'],
        'P': ['(E)', 'i'],
        'G': ['E']
    }
    og = ogGrammar(start=start, overs=overs, production=production)
    print('FirstVT集：', og.FirstVT)
    print('LastVT集：', og.LastVT)
# if __name__ == "__main__":
#     memo1 = {}
#     memo2 = {}
#     start = 'S'
#     overs = ['(', ')', 'a', 'b', 'c']
#     production = {
#         'S': ['(A)', 'a', 'b'],
#         'A': ['AcS', 'S'],
#
#     }
#     og = ogGrammar(start=start, overs=overs, production=production)
#     print('FirstVT集：', og.FirstVT)
#     print('LastVT集：', og.LastVT)
