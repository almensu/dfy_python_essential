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


for x in range(1, 10):
    for y in range(1, x+1):
        print('{0}x{1}={2}'.format(x, y, x*y), end = '')
        print('\n')

