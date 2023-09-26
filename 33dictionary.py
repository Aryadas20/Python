dic = {344: "Human being", 575: "Object", 383: "randomly", "Arya": "Avneet"}
# print(dic[383])
# print(dic['Arya'])
# print(dic.get(344))
# print(dic.keys())

# for key in dic.keys():
#   print(f"The value corresponding to the {key} is {dic[key]}")

print(dic.items())
for key, Value in dic.items():
  print(f"The value corresponding to the {key} is {Value}")