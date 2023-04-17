# String loopage
for n in 'banana':
  print(n)

# Character manipulation
word = 'supercalifragilisticexpialidocious'
new_string = ''

for char in word:
  if char == 's':
    new_string += '$'
  else:
    new_string += char

print(new_string)

# Parsing
example = 'the quick brown fox'
words = example.split(' ')

for word in words:
  print(word)


# Validation
import re

email = 'john.doe@example.com'

if re.match(r"[^@]+@[^@]+\.[^@]+", email):
  print('Valid Email')
else:
  print('Invalid Email')