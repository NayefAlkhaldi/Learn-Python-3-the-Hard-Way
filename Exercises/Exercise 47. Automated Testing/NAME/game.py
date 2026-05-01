class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def delete_paths(self, *paths):
        for path in paths:
            self.paths.pop(path)
        
    
    def reset(self):
        self.paths = {}