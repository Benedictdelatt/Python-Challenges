num = int(input("Enter a number: "))
print('Multiplication Table')
print('-' * len('Multiplication Table'))
for i in range(12):
       print(f'{num} * {i + 1} = {num * (i + 1)}')