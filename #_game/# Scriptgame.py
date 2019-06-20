# 面向对象设计，XO小游戏
import random


class game:

    # 初始化游戏
    def __init__(self):
        self.name = "XO小游戏"
        self.pie = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# 设置随机数决定哪一方先走

    def random_gamer(self, seed):
        try:
            num = random.randrange(int(seed))
        except:
            seed = input('输入错误，请重新输入：')
            return self.random_gamer(seed)
        if num % 2 == 0:
            return 1
        else:
            return -1

    # 判断输入是否在0-2之间

    def boolean_xy(self, x, y):
        if (x > 2 or x < 0) or (y < 0 or y > 2):
            x, y = input('输入有误，请重新输入：').split(',')
            return self.boolean_xy(int(x), int(y))
        return x, y

    # 判断输入是否为整数

    def boolean_input(self, x, y):
        try:
            return int(x), int(y)
        except:
            x, y = input('输入有误，请重新输入：').split(',')
            return self.boolean_input(x, y)

    # 设置落子
    def location(self, x, y, loc):
        x1, y1 = self.boolean_input(x, y)
        x, y = self.boolean_xy(x1, y1)
        if loc == 1:
            self.pie[x][y] = 'O'
        else:
            self.pie[x][y] = 'X'

    # 返回落子方
    def set_xy(self, num):
        if num == 1:
            return 'X'
        else:
            return 'Y'

    # 绘制棋盘
    def print_pie(self):
        for i in self.pie:
            print("%s  %s  %s" % (i[0], i[1], i[2]))

    def define(self, string):
        if string == 'O':
            return 1
        elif string == 'X':
            return -1
        else:
            return 0

    # 判断这个地方有没有子
    def bealean_exit(self, x, y):
        x, y = int(x), int(y)
        if self.pie[x][y] != 0:
            try:
                x, y = input('这个位置上已经落子了，请重新输入：').split(',')
                return self.bealean_exit(x, y)
            except:
                x, y = input('输入有误，请重新输入：').split(',')
                return self.bealean_exit(x, y)
        return x, y

    # 游戏规则，行或者列都为同一方获胜，组成对角线也获胜
    def game_rule(self):
        pie = self.pie

        sum3 = 0  # 判断左斜是否满足获胜条件
        sum4 = 0  # 判断右协是否满足获胜条件
        for i in range(len(pie)):
            sum1 = 0  # 判断行是否满足获胜条件
            sum2 = 0  # 判断列是否满足获胜条件
            for j in range(len(pie[i])):
                # print(pie[i][j])
                sum1 += self.define(pie[i][j])
                sum2 += self.define(pie[j][i])
                if i == j:
                    sum3 += self.define(pie[i][j])
                if i == abs(j-2):
                    sum4 += self.define(pie[i][j])
                if abs(sum1) == 3:
                    print('%s获胜' % (self.set_xy(sum1/3)))
                    return True
                if abs(sum2) == 3:
                    print('%s获胜' % (self.set_xy(sum2/3)))
                    return True
                if abs(sum3) == 3:
                    print('%s获胜' % (self.set_xy(sum1/3)))
                    return True
                if abs(sum4) == 3:
                    print('%s获胜' % (self.set_xy(sum1/3)))
                    return True

    # 游戏结束
    def boolean_end(self, flag):
        if flag == ('Y' or 'y'):
            self.pie = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            return self.start_game()
        elif flag == ('N' or 'n'):
            print('游戏结束，欢迎下次再来')
            return True
        else:
            return self.boolean_end(input('输入有误，请重新输入'))

    # 主程序，运行游戏
    def start_game(self):
        print('欢迎来到XO小游戏')
        self.print_pie()
        print('*'*30)
        seed = input('输入一个种子，决定谁先落子：')
        gamer = self.random_gamer(seed)
        self.set_xy(gamer)
        print('第1次落子')

        def boolean():
            try:
                x, y = input('请%s先落子(横纵坐标在0到2之间：)' %
                             self.set_xy(gamer)).split(',')
                return x, y
            except:
                return boolean()
        x, y = boolean()
        self.location(x, y, gamer)
        self.print_pie()
        for i in range(1, 9):
            print('第%d次落子' % i)
            gamer = -gamer
            x, y = input('请%s方落子(横纵坐标在0到2之间：)' % self.set_xy(gamer)).split(',')
            x, y = self.bealean_exit(x, y)
            self.location(x, y, gamer)
            self.print_pie()
            if self.game_rule():
                if self.boolean_end(input('游戏结束，选择Y再来一局，N结束：')):
                    break
        return True


if __name__ == "__main__":
    g = game()
    g.start_game()
