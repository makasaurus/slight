class subset:
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.parent[slice(index.start + self.start, index.stop + self.start)]
        return self.parent[index + self.start]
    def __delitem__(self, key):
        #not sure how this is implemented
        return self.parent.remove(key)

    def __setitem__(self, index, value):
        self.parent[index + self.start] = value

    def __init__(self, parent, start, end):
        self.parent = parent
        self.start = start
        self.end = end

