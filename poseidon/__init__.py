# poseidon init


# import data structures
import list_structure as ls
import log_structure as lg
import graph_structure as gr

pos = {}
command = None
key = None
COMMANDS = ['add', 'remove', 'show', 'new', 'help']
DATATYPES = ['list']

# call handler
def call(inp):

    words = inp.split(' ')

    # [command, rest] = [words[0], words[1:]] if (words[0] in COMMANDS) else [command, words]

    command = words[0] if len(words) > 0 else None

    if not command:
        out = 'no command'

    elif command == 'add':
        # add [key] ...
        if len(words) < 2:
            out = 'syntax: add [key] ...'
        else:
            key = words[1]
            rest = ''.join(words[2:])
            pos[key].add(rest)
            out = 'added to ' + key

    elif command == 'remove':
        # remove [key] [index]
        if len(words) < 3:
            out = 'syntax: remove [key] [index]'
        else:
            key = words[1]
            try:
                index = int(words[2])
                pos[key].remove(index)
                out = 'removed from ' + key
            except ValueError:
                out = 'syntax: remove [key] [index] OR remove [index]'

    elif words[0] == 'show':
        # show [key]
        if len(words) < 2:
            out = 'syntax: show [key]'
        else:
            key = words[1]
            out = pos[key].read()

    elif words[0] == 'new':
        # new [datatype] [key]
        if len(words) < 3:
            out = 'syntax: new [datatype] [key]'
        else:
            datatype = words[1]
            key = words[2]
            if datatype not in DATATYPES:
                out = datatype + ' not supported. Supported datatypes:\n' + '\n'.join(DATATYPES)
            elif key in pos.keys():
                out = key + ' already exists'
            else:
                pos[key] = ls.List() # TODO: hardcoding type here
                out = 'new ' + datatype + ' ' + key + ' created'

    elif words[0] == 'help':
        # help
        out = 'Type command name to get syntax. Supported commands:\n' + '\n'.join(COMMANDS)



    # didn't match anything
    else:
        out = 'rez could not understand. Type help for help.'


    return out
