coffee = 10

while coffee != 0:
    money = int(input("돈을 넣어 주세요 : "))
    if money == 300:
        print('커피를 줍니다')
        coffee = coffee - 1
    elif money > 300:
        money = money - 300
        print('거스름돈 %d원을 주고 커피를 줍니다.' %money)
        coffee = coffee - 1
    else:
        print('돈을 다시 돌려주고 커피를 주지 않습니다.')
        print('남은 커피의 양은 %d개 입니다' %coffee)
print('커피가 다 덜어졌습니다 판매를 중단 합니다')