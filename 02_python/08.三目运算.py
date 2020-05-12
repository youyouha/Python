#语法：
#  条件成立执行的表达式 if 条件 else 条件不成立执行的表达式

a = 1
b = 2
c = a if (a > b) else b
print(c)

#有两个变量比较大小 如果变量1大于变量2  执行 变量1 - 变量2；否则执行 变量2 - 变量1
num1 = int(input('请输入变量1：'))
num2 = int(input('请输入变量2：'))
result = (num1 - num2) if (num1 > num2) else (num2 - num1)

print(f'输出结果为{result}')