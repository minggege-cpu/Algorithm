"""
        LL(1)算法及预测分析表的实现 并判断句子是否属于该文法描述的语言
"""

from copy import deepcopy


class LLOneAnalyzer(object):
    def __init__(self, start, overs, production):
        self.start = start
        self.overs = overs
        self.production = production
        self.nontermainals = production.keys()
        self.first = {nontermainal: {} for nontermainal in self.nontermainals}
        self.follow = {nontermainal: set() for nontermainal in self.nontermainals}
        self.get_first_follow()
        self.analyse_table = {nontermainal: {} for nontermainal in self.nontermainals}
        self.get_analyse_table()

    # 求first的函数
    def get_first(self, nontermainal):
        ret_dict = {}
        for right in self.production[nontermainal]:
            if (nontermainal, right) in self.first_first:
                ret_dict = self.first[nontermainal]
                continue
            if right != '':
                if right[0] in self.overs:
                    ret_dict.update({right[0]: right})
                else:
                    for sign in right:
                        if sign in self.nontermainals:
                            first_ = self.first[sign]
                            ret_dict.update({key: right for key in first_.keys()})
                            if '' not in first_.keys():
                                break
            else:
                ret_dict.update({'': ''})
        return ret_dict

        # 求first集和follow集

    def get_first_follow(self):
        # 求first第一轮，产生式右部首字符为终结符号
        self.first_first = set()
        for nontermainal in self.nontermainals:
            for right in self.production[nontermainal]:
                if right != '' and right[0] in self.overs:
                    self.first[nontermainal][right[0]] = right
                    self.first_first.add((nontermainal, right))
        # 求first第二轮
        while True:
            old_first = deepcopy(self.first)
            for nontermainal in self.nontermainals:
                self.first[nontermainal].update(self.get_first(nontermainal))
            if old_first == self.first:
                break
        # 起始符号follow集
        self.follow[self.start].add('#')
        # 循环直到follow集不再变化
        while True:
            old_follow = deepcopy(self.follow)
            for nontermainal in self.nontermainals:
                for right in self.production[nontermainal]:
                    for i, sign in enumerate(right):
                        if sign in self.overs:
                            continue
                        if i == len(right) - 1:
                            self.follow[sign] |= self.follow[nontermainal]
                        elif right[i + 1] in self.overs:
                            self.follow[sign].add(right[i + 1])
                        else:
                            next_set = {key for key in self.first[right[i + 1]].keys()}
                            next_set_without_null = {key for key in self.first[right[i + 1]].keys() if key != ''}
                            self.follow[sign] |= next_set_without_null
                            if '' in next_set:
                                self.follow[sign] |= self.follow[nontermainal]
            if old_follow == self.follow:
                break
        # 将follow集加入first集
        for nontermainal in self.nontermainals:
            if '' in self.first[nontermainal]:
                self.follow[nontermainal] -= {key for key in self.first[nontermainal].keys()}
                self.first[nontermainal][''] = self.follow[nontermainal]
        # print("first集", self.first)
        # print("follow集", self.follow)

    # 根据first集follow集生成分析表
    def get_analyse_table(self):
        # 对于first集中每一个产生式及对应的输入符号
        for nontermainal in self.nontermainals:
            for a, right in self.first[nontermainal].items():
                # 如果输入符号为终结符号，将终结符号、输入符号、产生式右部写入分析表
                if a != '':
                    self.analyse_table[nontermainal][a] = right
                # 如果输入符号是空串，将非终结符号的follow集中每一个符号在分析表中的值写为空串
                else:
                    for b in right:
                        self.analyse_table[nontermainal][b] = ''
        print("预测分析表", self.analyse_table)

    # ll(1)文法分析函数
    def analyse_llone(self):
        while True:
            print('分析栈：', self.stack, '  剩余串：', string[self.index:], end='')
            # 拿出分析栈栈顶符号分析
            x = self.stack.pop()
            # 如果是栈顶符号终结符号
            if x in self.overs:
                print('   产生式：', x, '匹配')
                # 如果和待分析的符号匹配，分析下一个符号
                if x == self.a:
                    self.index += 1
                    self.a = self.string[self.index]
                # 如果不匹配，返回False
                else:
                    print("   匹配失败")
                    return False
            # 如果栈顶符号是'#'
            elif x == '#':
                print('   接受')
                # 如果和待分析的符号匹配，返回True
                if x == self.a:
                    return True
                # 如果不匹配，返回False
                else:
                    print("   匹配失败")
                    return False
            # 如果是非终结符号，将产生式右部元素逆序压入分析栈
            elif self.a in self.analyse_table[x].keys():
                print('   产生式：', x, '➡', self.analyse_table[x][self.a])
                self.stack += list(reversed(self.analyse_table[x][self.a]))
            # 如果是未知符号，返回False
            else:
                print("   匹配失败")
                return False

    # ll(1)文法分析程序入口
    def analyse(self, string=''):
        self.string = string + '#'
        self.stack = ['#', self.start]
        self.index = 0
        self.a = self.string[self.index]
        if self.analyse_llone():
            print('OK  ', string)
        else:
            print('Fail', string)


if __name__ == "__main__":
    start = 'E'
    overs = ['i', '+', '*', '(', ')']
    production = {
        'E': ['TA', ],
        'A': ['+TA', ''],
        'T': ['FB', ],
        'B': ['*FB', ''],
        'F': ['i', '(E)'],

    }
    string_list = [
        'i+i*i',
        'i*a'
    ]
    llone_analyzer = LLOneAnalyzer(start=start, overs=overs, production=production)
    for string in string_list:
        llone_analyzer.analyse(string=string)



