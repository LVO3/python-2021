def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

c = add_many(1,2,34,5,6,657,7,846,4)
print(c)