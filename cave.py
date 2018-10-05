
from random import randint
from room import Room


class Cave:

    _RAND_MAX = 20
    _RAND_MIN = 1
    _wumpus_room = 0

    _cave_rooms = {}
    cave_map = {1: [2, 5, 6], 2: [1, 3, 7], 3: [2, 4, 8], 4: [3, 5, 9], 5: [1, 4, 10],
                6: [1, 11, 12], 7: [3, 12, 13], 8: [4, 14, 15], 9: [4, 14, 15], 10: [5, 11, 15],
                11: [6, 10, 16], 12: [6, 7, 17], 13: [7, 8, 18], 14: [8, 9, 19], 15: [9, 10, 20],
                16: [11, 17, 20], 17: [12, 16, 18], 18: [13, 17, 19], 19: [14, 18, 20], 20: [15, 16, 19]}

    def __init__(self):
        for e in range(self._RAND_MIN, self._RAND_MAX+1):
            self._cave_rooms[e] = Room(self.cave_map[e])
        self._cave_rooms[randint(self._RAND_MIN, self._RAND_MAX)].pit = True
        self._cave_rooms[randint(self._RAND_MIN, self._RAND_MAX)].bats = True
        self._cave_rooms[randint(self._RAND_MIN, self._RAND_MAX)].bats = True
        self._wumpus_room = randint(self._RAND_MIN, self._RAND_MAX)
        self._cave_rooms[self._wumpus_room].wumpus = True

    def visit_room(self, room):
        return self._cave_rooms[int(room)].get_room()

    def wumpus_move(self):
        self._cave_rooms[self._wumpus_room].wumpus = False
        self._wumpus_room = randint(self._RAND_MIN, self._RAND_MAX)
        self._cave_rooms[self._wumpus_room].wumpus = True


