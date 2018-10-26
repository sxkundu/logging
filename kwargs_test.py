def greet_me( arg1, *args,  **kwargs ):
    print ("Test_arg1 {}".format(arg1))
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



def main():
    greet_me ( 'test1', 'arg', 1,2,3, name = " yasoob", int_test = 123 )

    kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
    some_kwargs(**kwargs)


if __name__ == '__main__':
    main()