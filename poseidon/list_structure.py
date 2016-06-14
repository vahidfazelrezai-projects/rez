# poseidon list data structure


class List():

    # initialize contents as an empty list
    def __init__(self):
        self.contents = []

    # add item to contents
    def add(self, item):
        self.contents.append(item)

    # remove first instance of item from contents
    def remove(self, index):
        self.contents.pop(index-1)

    # read contents according to given sort function
    def read(self):
        out = ''
        for i in range(1, len(self.contents)+1):
            out += str(i) + ': ' + self.contents[i-1] + '\n'            
        return out[:-1]


# call handler
def call(inp):
    return inp
