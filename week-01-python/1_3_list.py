# 목록 list, tuple
# 사전 dict
# 집합 set

# # list  []
# print("list")
# # print([1,2,3])
# # print(type([1,2,3]))
# list_a = [1,2,3]
# print(list_a)
# list_a.append(4)
# print(list_a)
#
# list_a.remove(2)
# print(list_a)
#
# list_a.clear()
# print(list_a)

# tuple (1,)
# 튜플을 변경할수 없다.

# print("tuple")
# print((1,2,3))
# print(type([1,2,3]))

# # dict {}
# # key & value
# dict_a = {
#         "apple" : "a type of truits" ,
#         "pen" : "a thing of writing"
# }
# print(dict_a)
# print(dict_a["apple"])
# dict_a["pen"] = "something to write"
# print(dict_a)

# set set([])
# 중복 자동 제거
set_a = set([1,2,3])
set_b = set([2,4,6])
print(set_a)
print(set_b)

# 교집합, 합집합, 차집합, 여집합
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
print(set_a)
