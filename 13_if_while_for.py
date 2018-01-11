# 第一题：利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# 我做的题1

# def get_grade(scores):
#     if scores >= 90:
#         return 'A'
#     elif scores >= 60 and scores <= 89:
#         return 'B'
#     else scores >= 0 and scores <= 60:
#         return 'C'

# 我做的题2
# score = int(input('输入你的分数：'))
# if score >= 90:
#     print('你的成绩为：A')
# elif score >= 60 and score <= 89:
#     print('你的成绩为：B')
# else score < 60:
#     print('你的成绩为：C')

# 老师做的
# score = int(input('输入你的分数：'))
# if score >= 90:
#     print('你的成绩为：A')
# elif score >= 60 and score <= 89:
#     print('你的成绩为：B')
# else:
#     print('你的成绩为：C')


# 第二题：for
#     创建一个名为favorite_places的字典。
#     在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1〜3个地方.
#     朋友指出一个名字(input)。遍历这个字典，并将输入名字及其喜欢的地方打印出来
#     还可以继续输入名字 如果输入q则退出
# #创建字典
# favorite_places = {'张三':['上海','北京','广州'],'李四':['九寨沟','张家界','鼓浪屿'],'东方耀':['长沙', '上海', '深圳']}

# favorite_places = {'张三':['上海','北京','广州'],
#                    '李四':['九寨沟','张家界','鼓浪屿'],
#                    '东方耀':['长沙', '上海', '深圳']
# }
#
# name_in = input('请输入你的名字 ：')
#
# while True:
#     if name_in == 'q':
#         break
#     else:
#         for name, places in favorite_places.items():
#             print(name, ':', places)
#         break


# 第三题：
# 99乘法表
#    用for循环打印99乘法表
#    用while
#    1x1 =1
#    1x2 = 2 2x2 = 4


# for x in range(1, 10):
#     for y in range(1, x+1):
#         print('{0}x{1}={2}'.format(x, y, x*y), end = '')
#         print('\n')


# 第四题：
# 1-100的和
#     1+2+3+4+...+100 = ?
#     range(1,101)

# result = 0
# for r in range(1, 101):
#     result += r
#     print(result)


# 第五题：
# 从键盘输入一个字符串，将小写字母全部转换成大写字母,
#     将字符串以列表的形式输出(如果字符串包含整数,转为整型)?

# str1 = input('输入小写字母：')
# dict1 = []
#
# for s in str1:
#     if str1.isdecimal():
#         dict1.append(int(s))
#     else:
#         dict1.append(str1.upper())
# print(dict1)

# 第六题：
# 随机输入8位以内的的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

nums = input('请随机输入8位以内的的正整数： ')
str1 = ''
if len(nums) <= 8:
    int1 = int(len(nums))
    print('它是', int1, '位数。')
    # 或者这样拼接
    print('它是{0}位数'.format(int1))

    # 方法一
    for char in list(reversed(nums)):
        str1 += char
    print(str1)

    # 方法二
    char_reversed = nums[::-1]
    print('逆序数字是：{0}'.format(char_reversed))

else:
    print('请输入8位以内的的正整数！！')









