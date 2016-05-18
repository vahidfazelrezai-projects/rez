import poseidon

def call(inp):
    return poseidon.call(inp)

if __name__ == '__main__':
    try:
        while True:
            inp = raw_input('> ')
            print call(inp) + '\n'
    except EOFError:
        print '\nbye'
