largest = float('-inf')
smallest = float('inf')

for i in range(5):
    num = float(input(f"Enter your number {i + 1}: "))
    if num > largest:
        largest = int(num)
    
    if num < smallest:
        smallest = int(num)


print(f'The largest value is {largest}')
print(f'the smallest value is {smallest}')