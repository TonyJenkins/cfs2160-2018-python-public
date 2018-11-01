sweets = int (input ('How many sweets are there?       '))
bag_size = int (input ('How many sweets fit in each bag? '))

full_bags = sweets // bag_size
left_over = sweets % bag_size

print ('You will get', full_bags, 'full bags.')
print ('There will be', left_over, 'sweets spare.')
