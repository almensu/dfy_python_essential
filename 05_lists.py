
lists = ['almensu', 33, 20180101, [2, 3, 'kk']]
nums = [3,55,77,5,6,89,70,34,44]

print(lists)
#
# print(lists[0])
# print(lists[-1])
#
# lists[0] = 'yanghoo'
# print(lists)
#

# lists.append(900)
# print(lists)

# lists.insert(0, 'Nanning')
# print(lists)
#
# # 直接删除
# del lists[0]
# print(lists)
#
# # pop 也是删除, 但有返回值 不填索引，默认最后一个删除
# poped = lists.pop()
# print(poped)
#
# # 直接删除 填对象
# lists.remove(33)
# print(lists)
#
# # 排序
# nums.sort()
# print(nums)
#
# # 倒序
# nums.sort(reverse=True)
# print(nums)
#
# # 临时性排序
# nums19 = sorted(nums)
# print(nums19)
#
# nums91 = sorted(nums, reverse=True)
# print(nums91)
#
# # 反转 镜像反转
nums.reverse()
print(nums)