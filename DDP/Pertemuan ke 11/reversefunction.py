buah = ['manggis', 'mangga', 'jambu', 'markisa', 'sirsak']

print('='*60)

print(f'Array not reverse: {buah}')

# defining my reverse method function
def myReverse(args):

    for i in range(-len(args), 0):
        args.insert(0, args.pop(i))


print('-'*65)

# reverse function that i created
myReverse(buah)

print(f'Array has been reversed: {buah}')

print('='*60)