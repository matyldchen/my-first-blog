print('Hello, Django girls!')
if 3 > 2:
    print('It works!')
    if 5 > 2:
        print('5 is indeed greater than 2')
    else:
        print('5 is not greater than 2')


def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

name="Sonja"
hi(3)
def hi(name):
    print('Hi ' + name + '!')

hi("Rachel")
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
