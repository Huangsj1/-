'''
常量文件
'''

# 难度
EASY = 1
MIDDLE = 2
HARD = 3

# 最大/小值
MAX_VAL = 9999999
MIN_VAL = -9999999

# alpha_beta的最大深度(搜索的层数是MAX_DEPTH-1)
# MAX_DEPTH = 4

# IDA迭代加深的alpha-beta (局面越好,速度越快)
# 搜索深度由MAX_DEPTH和MAX_TIME共同决定
MAX_DEPTH_EASY = 2
MAX_DEPTH_MIDDLE = 3
MAX_DEPTH_HARD = 6      # 最多搜6层,由时间决定深度
MAX_TIME = 0.3      # 倒数第二层的时间不能超过该时间,否则最后一层会过长

# 棋子类型
NULL = 0
KING = 1
CHE = 2
MA = 3
PAO = 4
XIANG = 5
SHI = 6
ZU = 7

TYPE_MAP = {0: "NULL", 1: "KING", 2: "CHE", 3: "MA", 4: "PAO", 5: "XIANG", 6: "SHI", 7: "ZU"}
TYPE_MAP_SHOW = {0: " ", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "G", 7: "Z"}

# 选手棋子颜色（电脑为黑）
BLACK = 0
RED = 1

COLOR_MAP = {0: "B", 1: "R"}

# 初始时棋盘
# init_board = [
#     [NULL, NULL, NULL, NULL, KING, NULL, NULL, NULL, NULL],
#     [NULL, NULL, NULL, CHE, NULL, NULL, NULL, NULL, NULL],
#     [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
#     [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
#     [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
#     [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
#     [CHE, NULL, NULL, NULL, NULL, NULL, ZU, NULL, ZU],
#     [NULL, NULL, NULL, NULL, NULL, NULL, MA, NULL, PAO],
#     [NULL, NULL, NULL, NULL, SHI, NULL, NULL, NULL, NULL],
#     [NULL, NULL, NULL, NULL, KING, SHI, NULL, NULL, NULL],
# ]
init_board = [
    [CHE, MA, XIANG, SHI, KING, SHI, XIANG, MA, CHE],
    [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
    [NULL, PAO, NULL, NULL, NULL, NULL, NULL, PAO, NULL],
    [ZU, NULL, ZU, NULL, ZU, NULL, ZU, NULL, ZU],
    [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
    [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
    [ZU, NULL, ZU, NULL, ZU, NULL, ZU, NULL, ZU],
    [NULL, PAO, NULL, NULL, NULL, NULL, NULL, PAO, NULL],
    [NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL],
    [CHE, MA, XIANG, SHI, KING, SHI, XIANG, MA, CHE],
]


# 以下棋子子力和棋子位置都被用来棋局评估
# 棋子子力
base_value = [0, 0, 500, 300, 300, 200, 200, 100]
# base_value = [0, 0, 500, 300, 300, 200, 200, 100]
# 棋子机动性(可以移动到空位置就有机动性)
mobile_value = [0, 0, 6, 12, 6, 1, 1, 15]
# 棋子位置
pos_value = [
    [   # NULL
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ], 
    [   # KING
        [0, 0, 0, 1, 5, 1, 0, 0, 0],
        [0, 0, 0, -8, -8, -8, 0, 0, 0],
        [0, 0, 0, -9, -9, -9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    [   # CHE
        [ -6, 6, 4, 12, 0, 12, 4, 6, -6],
        [ 5, 8, 6, 12, 0, 12, 6, 8, 5],
        [ -2, 8, 4, 12, 12, 12, 4, 8, -2],
        [ 4, 9, 4, 12, 14, 12, 4, 9, 4],
        [ 8, 12, 12, 14, 15, 14, 12, 12, 8],
        [ 8, 11, 11, 14, 15, 14, 11, 11, 8],
        [ 6, 13, 13, 16, 16, 16, 13, 13, 6],
        [ 6, 8, 7, 14, 16, 14, 7, 8, 6],
        [ 6, 12, 9, 16, 33, 16, 9, 12, 6],
        [ 6, 8, 7, 13, 14, 13, 7, 8, 6],
    ],
    [   # MA
        [ 0, -3, 2, 0, 2, 0, 2, -3, 0],
        [ -3, 2, 4, 5, -10, 5, 4, 2, -3],
        [ 5, 4, 6, 7, 4, 7, 6, 4, 5],
        [ 4, 6, 10, 7, 10, 7, 10, 6, 4],
        [ 2, 10, 13, 14, 15, 14, 13, 10, 2],
        [ 2, 12, 11, 15, 16, 15, 11, 12, 2],
        [ 5, 20, 12, 19, 12, 19, 12, 20, 5],
        [ 4, 10, 11, 15, 11, 15, 11, 10, 4],
        [ 2, 8, 15, 9, 6, 9, 15, 8, 2],
        [ 2, 2, 2, 8, 2, 8, 2, 2, 2],
    ],
    [   # PAO
        [ 0, 0, 1, 3, 3, 3, 1, 0, 0],
        [ 0, 1, 2, 2, 2, 2, 2, 1, 0],
        [ 1, 0, 4, 3, 5, 3, 4, 0, 1],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ -1, 0, 3, 0, 4, 0, 3, 0, -1],
        [ 0, 0, 0, 0, 4, 0, 0, 0, 0],
        [ 0, 3, 3, 2, 4, 2, 3, 3, 0],
        [ 1, 1, 0, -5, -4, -5, 0, 1, 1],
        [ 2, 2, 0, -4, -7, -4, 0, 2, 2],
        [ 4, 4, 0, -5, -6, -5, 0, 4, 4],
    ],
    [   # XIANG
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ -2, 0, 0, 0, 3, 0, 0, 0, -2],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    [   # SHI
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ],
    [   # ZU
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [ -2, 0, -2, 0, 6, 0, -2, 0, -2],
        [ 3, 0, 4, 0, 7, 0, 4, 0, 3],
        [ 10, 18, 22, 35, 40, 35, 22, 18, 10],
        [ 20, 27, 30, 40, 42, 40, 30, 27, 20],
        [ 20, 30, 45, 55, 55, 55, 45, 30, 20],
        [ 20, 30, 50, 65, 70, 65, 50, 30, 20],
        [ 0, 0, 0, 2, 4, 2, 0, 0, 0],
    ]
]

if __name__ == "__main__":
    for k in range(8):
        for i in range(10):
            for j in range(9):
                print(pos_value[k][i][j], end=', ')
            print()
        print()