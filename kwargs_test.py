def greet_me(arg1, *args, **kwargs):
    print("Test_arg1 {}".format(arg1))
    if args is not None:
        for num in args:
            print(num)
    if kwargs is not None:
        print(kwargs)
        print(type(kwargs))
        for key, value in kwargs.items():
            print("The value of {} is {}".format(key, value))


def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def coroutine_test():
    while True:
        received = yield
        print("Reveived {}".format(received))
        processed_value = received + 5
        yield processed_value


def main():
    # greet_me ( 'test1', 'arg', 1,2,3, name = " yasoob", int_test = 123 )

    # kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
    # some_kwargs(**kwargs)

    # for i in countdown(5):
    #    print (i)
    s = coroutine_test()
    next(s)
    # s.send('abc')
    x = s.send(123)
    print(x)
    s.close()


if __name__ == '__main__':
    main()
