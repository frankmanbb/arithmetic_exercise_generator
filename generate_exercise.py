import random
from datetime import datetime
random.seed(datetime.now())

numbers = 76  # number of equations to generate.
first_op_range = (0, 10)  # first operands range in [0, 10]
second_op_range = (0, 10)  # second operands range in [0, 100]
operators = ['+', '-']  # set which operator to use, supports any  ['+', '-', 'x']


numbers = numbers // 2 * 2  # Make it even so each line can contain two equations.

rand_num = numbers * 2


generate_nums = []
file = open("numbers.txt", 'w')
for i in range(numbers):
  a = random.randint(*first_op_range)
  b = random.randint(*second_op_range)
  sign = random.choice(operators)
  if sign == '-':
    if a < b:
      a, b = b, a
  str_val = '{}\t{}\t{}\t=\t\t\t'.format(a, sign, b)
  if i % 2 == 0:
    str_val += '\t'
  else:
    str_val += '\n'
  print(str_val)
  file.write(str_val)
file.close()
