import random

characters = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890'
print('welcome to the pypassword generator')
n_chars=int(input('how much length of Password?\n'))
password=""
for char in range(n_chars):
   random_char=  random.choice(characters)
   password += random_char
print(password)