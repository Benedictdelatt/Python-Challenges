'''count_odd = 0
count_even = 0

for i in range(10):
 num = int(input(f'Enter a number {i + 1}: '))
 
 if num % 2 == 0:
  count_even += 1
 elif num % 2 != 0:
    count_odd += 1 
 
print(f'Number of even number is {count_even}')
print(f'Number of odd numbers is {count_odd}')'''


first_name = ["Benedict"]
last_name = ["Lawoe"]

for a_first_name,a_last_name in zip(first_name, last_name):
    print(a_first_name, a_last_name)