#write

f = open("새파일.txt", 'w')

for i in range(1, 11):
    data = '%dth line\n' %i
    f.write(data)

f.close()