def methodception(another):
    return another()


def add_two_numbers():
    return 35 + 77

print (methodception(add_two_numbers))

print (methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 474]
print (list(filter(lambda x: x != 13, my_list)))

print ((lambda x: x*3)(5))

def f(x):
    return x * 3

print (f(5))


def not_thirteen(x):
    return x != 13

print (list(filter(not_thirteen, my_list)))