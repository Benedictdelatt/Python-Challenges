first = int(input('Enter a number 1: '))

largest = first
smallest = first

for i in range(4):
    num = int(input(f'Enter your number {i + 2}: '))

    if num > largest:
      largest = num

    if num < smallest:
        smallest = num

print(f'The largest number is {largest}')
print(f'The smallest number is {smallest}') 