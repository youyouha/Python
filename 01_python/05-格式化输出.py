age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 41609310126

print('今年我的年龄是%d' % age)
print('我的名字是%s' % name)
print('我的体重是%.2f公斤' % weight)
print('我的学号是%d' % stu_id)
# 我的学号是001    %06d 表示输出的整数显示6位数，不足以0不全，超出当前位数则原样输出
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)

# print('我的名字是%s,' % name + '今年%d岁了' % age)
print('我的名字是%s,今年%d岁了' % (name, age))
# 我的名字是x，我明年x岁了
print('我的名字是%s,明年%d岁了' % (name, age + 1))

# print('我的名字是%s,' % name + '今年%d岁了,' % age + '我的体重是%.2f公斤,' % weight + '我的学号是%.03d' % stu_id)
print('我的名字是%s,今年%d岁了,我的体重是%.2f公斤,我的学号是%03d' % (name, age, weight, stu_id))


