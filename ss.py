#학생 점수 판별 프로그램

scores = [90, 25, 43, 71, 60]
number = 0
for score in scores:

    number = number + 1
    
    if score >= 60:
        print('%d번 학생은 합격입니다' %number)
    else:
        print('%d번 학생은 불합격입니다' %number)
