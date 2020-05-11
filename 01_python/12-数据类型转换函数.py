# 1.float()  --将数据转换成浮点型
num1 = 1
str1 = '10'
print(float(num1))  #1.0
print(type(float(num1)))
print(float(str1))  #10.0
print(type(float(str1)))

# 2.str() --将数据转换成字符串型
print(type(str(num1)))  #str

# 3.tuple() --将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))  #(10, 20, 30)
print(type(tuple(list1)))  #tuple

# 4.list() --将一个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))  #[100, 200, 300]
print(type(list(t1))) #list

# 5.eval() --计算在字符串中的有效python表达式，并返回一个对象
#      也就是返回其本来的数据类型
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'
print(type(eval(str2))) #int
print(type(eval(str3))) #float
print(type(eval(str4))) #tuple
print(type(eval(str5))) #list
