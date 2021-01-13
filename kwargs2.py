def introduceEnglishName(**kwargs):
    for key, value in kwargs.items():
        if 'ant' in kwargs.keys():
            print("주인님 오셨군요. 오늘 기분이 어떠세요?")
        else: print("{0} is {1}".format(key, value))

introduceEnglishName(Myname = 'Chris!!')
introduceEnglishName(ant = 'Chirs!!')