def say_myself(name, old, sex):
    print('나의 이름은 %s 입니다' %name)
    print('나의 나이는 %d살 입니다' %old)
    if sex == 'man':
        print('나는 남자입니다')
    else:
        print('나는 여자입니다')

say_myself('김태영', 18, 'man')
say_myself('진자림', 21, 'girl')