
#----------------------------
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


#----------------------------
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

#----------------------------
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


#----------------------------
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


#----------------------------
# 第四题：
# 1-100的和
#     1+2+3+4+...+100 = ?
#     range(1,101)

# result = 0
# for r in range(1, 101):
#     result += r
#     print(result)


#----------------------------
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


#----------------------------
# 第六题：
# 随机输入8位以内的的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

# nums = input('请随机输入8位以内的的正整数： ')
# str1 = ''
# if len(nums) <= 8:
#     int1 = int(len(nums))
#     print('它是', int1, '位数。')
#     # 或者这样拼接
#     print('它是{0}位数'.format(int1))
#
#     # 方法一
#     for char in list(reversed(nums)):
#         str1 += char
#     print(str1)
#
#     # 方法二
#     char_reversed = nums[::-1]
#     print('逆序数字是：{0}'.format(char_reversed))
#
# else:
#     print('请输入8位以内的的正整数！！')


#----------------------------
# 第七题：
# 一球从n米(自己输入)高度自由落下，每次落地后反跳回原高度的一半；
#     再落下，求它在第10次落地时，共经过多少米？



#----------------------------
# 第八题：
# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# str = input('请输入一段文字：')
#
# letter = 0
# space = 0
# numeric = 0
# other = 0
#
# for char in str:
#     if char.isalpha():
#         letter += 1
#     elif char.isspace():
#         space += 1
#     elif char.isnumeric():
#         numeric += 1
#     else:
#         other += 1
#
# print('输入的字符串中，字母{0}个，空格{1}个，数字{2}个，其他字符{3}个'.format(letter, space, numeric, other))


#----------------------------
# 第九题：
# names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven',
# 'Joe','Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']
# 找出上述名字中长度大于4的名字,组成列表打印出来.
# 过滤掉长度大于5的字符串列表，并将剩下的转换成大写字母.

# names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven',
# 'Joe','Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']
#
# names4 = []
# names5 = []
#
# for n in names:
#     if len(n) > 4:
#         names4.append(n)
#
# for n in names:
#     if len(n) <= 5:
#         # n = n.upper()
#         names5.append(n.upper())
#
#
# print('长度大于4的名字: ', names4)
# print('剩下的转换成大写字母: ', names5)



#----------------------------
# 第十一题：
# 打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，
# 其各位数字立方和等于该数本身。
# 例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。


# n = 153
#
# print(n//100)
# print(n%100//10)
# print(n%100%10)

# 未完成


#----------------------------
# 第十二题：
# 打印菱形       *




# ----------------------------
# 第十三题：
# 一个5位数，判断它是不是回文数。即12321是回文数，
# 个位与万位相同，十位与千位相同。
#
# ge = wan
# shi = qian
# bai = range(0, 10)
#
# for i in range(0, 99999):
#     if i == str(ge) + str(shi) + str(bai) + str(qian) + str(wan):
#         print(i)
#
#
#
# 老师的方法
#
# nums = input('输入5位数')
# if nums[0] == nums[4] and nums[1] == nums[3]:
#     print('这是回文数')
# else:
#     print('这不是')
#
#
# 我的方法
# nums5 = []
# huiwenshu = []
#
# nums = list(range(100000))
# for i in nums:
#     if len(str(i)) == 5:
#         nums5.append(i)
#     else:
#         pass
#
# for i in nums5:
#     # if i[0] == i[4] and i[1] == i[3]:
#     if str(i) == str(i)[::-1]:
#         huiwenshu.append(i)
#     else:
#         pass
#
# print(huiwenshu)
# 我的方法
#
#
# 我的调试
# nums = ['12322', '12321', '32123']
# shouji = []
#
# for i in nums:
#     if str(i) == str(i[::-1]):
#         shouji.append(i)
#     else:
#         print('bu是回文数')
#
# print(shouji)
# 我的调试


# ----------------------------
# 第十四题：
# 求一个3*3矩阵对角线元素之和
#     m [0][0]1    m [0][2-0=2]  3
#     m [1][1]5    m [1][2-1=1]  5
#     m [2][2]9    m [2][2-2=0]  7


# ----------------------------
# 第十五题：
# 题目：有四个数字：1、2、3、4，能组成多少个互不
#     相同且无重复数字的三位数？各是多少？
#     123 213 143 234 431
#     程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
#     组成所有的排列后再去 掉不满足条件的排列。(用列表推导式)

#
# for a in range(1, 5):
#     for b in range(1, 5):
#         for c in range(1, 5):
#             if a != b and b != c and a != c:
#                 print(a * 100 + b * 10 + c)



# ----------------------------
# 第十六题：
# 将列表用for循环添加到一个字典中names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven',
# 'Joe','Alice','Sherry','Eva']

names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven',
'Joe','Alice','Sherry','Eva']

# dict1 = {}
#
# i = 0
#
# for name in names:
#     dict1[i] = name
#     i += 1
# print(dict1)

# print({key:value for key, value in enumerate(names)})



# ----------------------------
# 第十七题：
# 设一组账号和密码不少于两个
#     通过输入账号和密码，如果输入正确则显示登录成功
#     若账号或者密码错误则显示登录失败，最多可以输入三次

users ={'张三':'123456','李四':'654321'}

for i in range(3):
    name = input('请输入账号：')
    pwd = input('请输入密码：')
    if name in users.keys():
        if pwd == users[name]:
            print('登录成功！')
            break
        else:
            if i == 2:
                print('你的账户已被冻结！')
                break
            print('密码错误')
    else:
        if i == 2:
            print('你的账户已被冻结！')

        print('你的帐号错误！')

