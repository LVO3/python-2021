def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

a = avg_numbers(1,1235,43141,14123,21321)
print(a)