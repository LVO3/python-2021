#positive.py
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([-1, -3, 2, 0, -5, 6]))


#함수를 사용해서 더욱더 간단하게 만들기
#filter1.py
def sositive(x):
    return x > 0

print(list(filter(sositive, [-1, -3, 2, 0, -5, 6])))