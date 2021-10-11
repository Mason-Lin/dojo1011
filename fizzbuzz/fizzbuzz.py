def result(num):
    if num % 3 == 0:
        if num % 5 == 0:
            return "fizzbuzz"
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)
