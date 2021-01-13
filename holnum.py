numbers = [1, 2, 3, 4, 5]
result = []
for number in numbers:
    if number % 2 == 0: continue
    else: result.append(2 * number)
print(result)

#same
numbers = [1, 2, 3, 4, 5]
result = [number * 2 for number in numbers if number % 2 == 1]
print(result)