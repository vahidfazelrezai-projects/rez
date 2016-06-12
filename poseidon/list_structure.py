# poseidon list data structure


class List():

    # initialize contents as an empty list
    def __init__(self):
        self.contents = []

    # add item to contents
    def add(self, item):
        self.contents.append(item)

    # remove first instance of item from contents
    def remove(self, item):
        self.contents.remove(item) # TODO PROBABLY INCORRECT SYNTAX

    # read contents according to given sort function
    def read(self, sort_fn=lambda x: x):
        sorted_list = sorted(self.contents, key=sort_fn) # TODO PROBABLY INCORRECT SYNTAX
        out = ''
        for i in range(1, len(sorted_list)+1):
            out += str(i) + ': ' + sorted_list[i-1] + '\n'
        return out


# call handler
def call(inp):
    return inp
