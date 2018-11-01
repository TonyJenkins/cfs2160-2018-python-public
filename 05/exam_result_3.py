Number_of_Results = 5

name = input ('Enter the student\'s name: ')

results = []

for count in range (Number_of_Results):
    while 1:
        result = int (input ('Enter result #' + str (count + 1) + ': '))
        if result in range (0, 101):
            results.append (result)
            break
        else:
            print ('Invalid. Try again.')

average_mark = sum (results) / Number_of_Results

print ()
print ('Final Mark for ' + name + ' is ' + str (average_mark) + '.')

if average_mark >= 70.0:
    print ('Cool Beans! ' + name + ' has a Distinction!')
elif average_mark >= 50.0:
    print ('Congratulations! ' + name + ' has passed!')
else:
    print ('Sadly, ' + name + ' has failed. What a pity.')
