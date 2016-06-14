import poseidon

def call(inp):
    return poseidon.call(inp)

if __name__ == '__main__':
    try:
        while True:
            inp = raw_input('> ')
            out = call(inp)
            if len(out) > 0:
                if out[-1] != '\n':
                    out += '\n'
            print out
    except EOFError:
        print '\nbye'
