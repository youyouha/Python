'''
坐公交：
    如果有钱可以上车，没钱不能上车                ----判断是否有钱
        上车后若有空座则可以坐下，没有空座就站着   ----判断是否有空座
'''

money = 0
seat = 1

if money == 1:
    print('请上车')
    #判断是否能坐下
    if seat == 1:
        print('这有空座，坐下吧')
    else:
        print('就站着吧！')
else:
    print('朋友跟着跑吧')
