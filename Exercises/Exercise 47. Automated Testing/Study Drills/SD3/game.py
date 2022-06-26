class Room(object):
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)
    
    def remove_paths(self, paths):
        self.paths.pop(paths)
    
    def correct_paths(self, death_room):
        available_paths = []
        for key, value in self.paths.items():
            if value != death_room:
                available_paths.append(key)
        if len(available_paths) <= 0:
            return None

        return available_paths