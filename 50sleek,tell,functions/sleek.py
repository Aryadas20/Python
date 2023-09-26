with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  print(type(f))
  f.seek(10)

  # Read the next 5 bytes
  print(f.tell()) # kahan tak seek kiay hua hai
  data = f.read(5)
  print(data)