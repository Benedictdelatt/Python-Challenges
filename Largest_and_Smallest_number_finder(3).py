numbers = []

for i in range(5):
 num = int(input('Enter a number: '))
 numbers.append(num)
print(f'Numbers entered: {numbers}')


largest  = smallest = numbers[0]

for num in numbers:
  if num > largest:
   largest = num
  if num < smallest:
    smallest = num

print(f'The largest value is {largest}')
print(f'The smallest value is {smallest}')
 