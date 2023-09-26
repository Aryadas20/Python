listA = ['a', 'b', 'c', 'd', 'e']
# print(listA)
#  print(type(listA))
# print(listA[0])
# print(listA[1])
# print(listA[2])
# print(listA[3])

# print(listA[-3])  # negative index
# print(listA[len(listA)-3])  # positive index

# if 7 in listA:
#     print("yes")
# else:
#     print("No")



# print(listA[:])
print(listA)
print(listA[1:-1])
print(listA[1:4:1])


lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst) 
