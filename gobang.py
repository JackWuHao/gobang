import itertools
ROUND_SIZE=7 #棋盘大小
MAX_COUNT=5 #胜利条件
board=[]


#画棋盘
def initBorad():
    for i in range(ROUND_SIZE):
       row = [' □  '] * ROUND_SIZE
       board.append(row)


#在控制台输出棋盘的方法
def printBoard():
    for i in range(ROUND_SIZE):
        for j in range(ROUND_SIZE):
            print(board[j][i],end="")

        print()


#判断重复落子问题
def repeatBoad(x,y):
    #以（0,0为起点的）
    str = board[int(y)-1][int(x)-1]
    if str == ' ●  ':
        print("\t 棋子重复")
        return False
    else:
        return True


#判断胜负问题(以这个点为圆心，横向纵向斜线检测)
def sucess_failure(x,y):

     a=hengxian(x,y) #获取横线方向的结果
     if hengxian(x,y):
         return True
     elif zongxiang(x,y):
         return True
     elif duijiao(x,y):
         return True
     else:
         c = False
         if int(x) >= (int(y)):
             c = xiexian_down(x, y)
         else:
             c = xiexian_up(x, y)
         return c


     # # b=zongxiang(x,y)
     # c = False
     # if int(x) >=(int(y)):
     #     c = xiexian_down(x,y)
     # else:
     #     c= xiexian_up(x,y)
     # d = duijiao(x,y)
     # if a or b or c or d:
     #     return True
     # else:
     #     return False


#检测横线方向
def hengxian(x,y):
    hen_list =[]
    for i  in range(ROUND_SIZE):
        str = board[int(y)][int(i)]
        hen_list.append(str)
    max_count = max([len(list(v)) for k, v in itertools.groupby(hen_list) if k ==' ●  '])
    if max_count==MAX_COUNT:
        print("玩家胜利")
        return True
    else:
        return False


#检测纵向
def zongxiang(x,y):
    zong_list=[]
    for i in range(ROUND_SIZE):
        str = board[int(i)][int(x)]
        zong_list.append(str)

    max_count = max([len(list(v)) for k, v in itertools.groupby(zong_list) if k ==' ●  '])
    if max_count==MAX_COUNT:
        print("玩家胜利")
        return True
    else:
        return False

#向下斜线检测
def xiexian_down(x,y):
    xiexian_list=[]
    for i  in range(ROUND_SIZE):
        for j in range(ROUND_SIZE):
             if x>=y and (x-y ==(i-j)):
                 str = board[int(j)][int(i)]
                 xiexian_list.append(str)

    max_count = max([len(list(v)) for k, v in itertools.groupby(xiexian_list) if k ==' ●  '])
    if max_count==MAX_COUNT:
        print("玩家胜利")
        return True
    else:
        return False


def xiexian_up(x, y):
    xiexian_list = []
    for i in range(ROUND_SIZE):
        for j in range(ROUND_SIZE):
            if x <= y and (y - x == (j - i)):
                str = board[int(j)][int(i)]
                xiexian_list.append(str)

    max_count = max([len(list(v)) for k, v in itertools.groupby(xiexian_list) if k == ' ●  '])
    if max_count == MAX_COUNT:
        print("玩家胜利")
        return True
    else:
        return False


#对角检测
def duijiao(x,y):
    duijiao_list = []
    for i in range(ROUND_SIZE):
        for j in range(ROUND_SIZE):
            if  x+y == j+i:
                str = board[int(j)][int(i)]
                duijiao_list.append(str)

    max_count = max([len(list(v)) for k, v in itertools.groupby(duijiao_list) if k == ' ●  '])
    if max_count == MAX_COUNT:
        print("玩家胜利")
        return True
    else:
        return False


if __name__ == '__main__':
    initBorad()
    printBoard()
    inputStr = input("请输入你下棋的坐标，应以x,y的格式：\n")
    while inputStr != None:
        x_str, y_str = inputStr.split(sep=",")
        if repeatBoad(x_str,y_str):
            # 为对应的列表元素赋值' ●  '
            # ' ♥  '
            board[int(y_str) - 1][int(x_str) - 1] = ' ●  '
            printBoard()
            if sucess_failure(int(x_str) - 1, int(y_str) - 1): #判断胜负
                break
            else:
                inputStr = input("请继续输入你下棋的坐标，应以x,y的格式：\n")

        else:
            printBoard()
            inputStr = input("请重新输入你下棋的坐标，应以x,y的格式：\n")

