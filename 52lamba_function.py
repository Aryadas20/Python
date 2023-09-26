# def double(x):
#     return x*2


def apple(fx, value):
    return 6 + fx(value)


double = lambda X:X*2
cube  = lambda X:X*3
avg = lambda x, y, z: (x + y+z) /3

print(double(5))

print(apple(lambda x: x * x * x, 2)) 