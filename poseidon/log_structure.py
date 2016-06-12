# poseidon log structure


class Log():

    # initialize contents as an empty list
    def __init__(self):
        self.contents = []

    def __str__(self):
        return str(self.contents)

    # append item to contents
    def log(self, item):
        self.contents.append(item)

    # read all contents
    def read(self):
        return self.contents


# call handler
def call(inp):
    return inp
