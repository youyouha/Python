#导入随机数模块
import random

#1.出拳
# 1.玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布\n'))
# 2.电脑
#使用随机函数模块
computer =random.randint(0,2)

# 2.判断输赢
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 3)) or ((player == 3) and (computer == 0)):
    print(f'您出的是{player},电脑出的是{computer}--玩家获胜')
elif player == computer:
    print(f'您出的是{player},电脑出的是{computer}--平局，别走再来一局')
else:
    print(f'您出的是{player},电脑出的是{computer}--电脑获胜')
