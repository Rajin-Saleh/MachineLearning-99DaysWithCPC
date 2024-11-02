def para(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


para(arg1=1, arg2="hello", arg3=True, arg4=["1", 2, "test"])


def greeter(person="person", greet="hello", weekday="any day"):
    print(f"{person} {greet}")
    print(f"It is {weekday}")


greeter("Bob", weekday="Tuesday")
