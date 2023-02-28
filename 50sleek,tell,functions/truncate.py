with open('file.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

with open('file.txt', 'r') as f:
  print(f.read())