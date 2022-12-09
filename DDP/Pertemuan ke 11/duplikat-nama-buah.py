buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

print('='*60)

print(f'Array not Duplicated: {buah}')

# Defining duplication function
def myDupe(args):

    for i in range(0,len(args)):
        args.append(args[0])
        args.append(args.pop(0))


print('-'*65)

# Duplicating Array using myDupe Function
myDupe(buah)

print(f'Array has been Duplicated: {buah}')

print('='*60)