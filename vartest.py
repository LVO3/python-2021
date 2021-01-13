#vartest.py
a = 1
def vartest(a):
    a += 1
    return a

vartest(a)
print(a)

b = vartest(11)
print(b)