def my_method(arg1, arg2):
    return arg1 * arg2

print (my_method(10, 20))


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)



what_are_kwargs(10,20,30,name='Jose', location='UK')