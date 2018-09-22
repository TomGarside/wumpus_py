class Room:
    wumpus, pit, bats = False, False, False
    paths = {}

    def __init__(self, room_map):
        self.paths['1'] = room_map[0]
        self.paths['2'] = room_map[1]
        self.paths['3'] = room_map[2]

    def get_room(self):
        return self.wumpus, self.pit, self.bats
