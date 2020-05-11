num_to_flip = int(input('enter a number: '))

num_flipped = 0
if num_to_flip < 0:
    num_flipped = num_to_flip + (abs(num_to_flip) * 2)
else:
    num_flipped = num_to_flip - (num_to_flip * 2)
    
print('number flipped the hard way: ' + str(num_flipped))

num_flipped = num_to_flip * -1

print('number flipped the easy way: ' + str(num_flipped))

print(f'we turned the {num_to_flip} input into {num_flipped} output')


