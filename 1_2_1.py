name = 'Lada'
day = 'Monday'
print(f'Good day {name}! {day} is a perfect day to learn some python.')

print('Good day {}! {} is a perfect day to learn some python.'.format(name, day))

print('Good day {N}! {D} is a perfect day to learn some python.'.format(N=name, D=day))

print('Good day {0}! {1} is a perfect day to learn some python.'.format(name, day))

print('Good day %s! %s is a perfect day to learn some python' % (name, day))
