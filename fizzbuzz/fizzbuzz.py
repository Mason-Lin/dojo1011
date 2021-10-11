def result(num):
    if num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return 'buzz'
    else:
        return str(num)