
Number_of_Results = 5

while 1:
    name = input ('Enter the student\'s name: ')

    if len (name) in range (2, 32):
        break
    else:
        print ('That does not look like a valid name!')

results = []

for count in range (Number_of_Results):
    while 1:
        try:
            result = int (input ('Enter result #' + str (count + 1) + ': '))
            if result in range (0, 101):
                results.append (result)
                break
            else:
                print ('Invalid. Try again.')
        except ValueError:
            print ('Please Enter an Integer!')

average_mark = sum (results) / Number_of_Results

print ()
print ('Final Mark for ' + name + ' is ' + str (average_mark) + '.')

if average_mark >= 70.0:
    print ('Cool Beans! ' + name + ' has a Distinction!')
elif average_mark >= 50.0:
    print ('Congratulations! ' + name + ' has passed!')
else:
    print ('Sadly, ' + name + ' has failed. What a pity.')

