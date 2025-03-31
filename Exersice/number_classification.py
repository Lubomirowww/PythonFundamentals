data = list(map(int, input().split(' ')))


positive=[num for num in data if num  >=0]
negative=[num for num in data if num  <0]
even=[num for num in data if num %2 ==0]
odd=[num for num in data if num %2 !=0]

print(f'Positive: {positive}')
print(f'Negative: {negative}')
print(f'Even: {even}')
print(f'Odd: {odd}')

