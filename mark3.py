marks = [90, 25, 67, 45, 88]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print('%d번 학생 축하드립니다. 합격입니다.' %(number + 1))