# READING A FILE

# f = open('myfile.txt', 'r')
# # f = open('myfile2.txt', 'w')
# print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open('myfile.txt', 'w')
# f.write('Hello, world!')
# f.close()

with open('myfile.txt', 'a') as f:
    f.write("Hey I am inside with")

# APPEND A FILE

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()

