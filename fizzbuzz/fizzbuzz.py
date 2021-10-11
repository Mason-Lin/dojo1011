def result(num):
    if isinstance(num, float):
        raise NotImplementedError("float is not supported")
    if num % 15 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)
