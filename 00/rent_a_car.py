print ('Hello, who are you? ')
name = input ()

print ('What year were you born?')
year = int (input ())

age_this_year = 2017 - year

print ('Good to meet you, ' + name + '.')
print ('This year you will be ' + str (age_this_year) + ' years old.')

if age_this_year >= 21:
    print ('So you can rent the car.')
else:
    print ('Sorry, you are too young to rent.')