import random

slices = random.randint(4, 8)

print('Hello there')
print('I\'m a pizza package')
print(f'Once I had a {slices} slices of pizza')
print('and then HE started to eat them one by one')

for i in reversed(range(slices)):
    print(f'he continues eat and there was only {i} of them left')

print('Once I was devastated there is no more reason to keep me in the fridge')
print('Fast-forward 3 hours and now I\'m here in a *cking trashcan... ')

print('But life is goin on, there is plenty of friends here...')