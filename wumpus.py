from random import randint
import re

RAND_MAX = 20
RAND_MIN = 1


class Cave:
    _cave_rooms = {}
    cave_map = {1: [2, 5, 6], 2: [1, 3, 7], 3: [2, 4, 8], 4: [3, 5, 9], 5: [1, 4, 10],
                6: [1, 11, 12], 7: [3, 12, 13], 8: [4, 14, 15], 9: [4, 14, 15], 10: [5, 11, 15],
                11: [6, 10, 16], 12: [6, 7, 17], 13: [7, 8, 18], 14: [8, 9, 19], 15: [9, 10, 20],
                16: [11, 17, 20], 17: [12, 16, 18], 18: [13, 17, 19], 19: [14, 18, 20], 20: [15, 16, 19]}

    def __init__(self):
        for e in range(RAND_MIN, RAND_MAX+1):
            self._cave_rooms[e] = Room(self.cave_map[e])
        self._cave_rooms[randint(RAND_MIN, RAND_MAX)].pit = True
        self._cave_rooms[randint(RAND_MIN, RAND_MAX)].bats = True
        self._cave_rooms[randint(RAND_MIN, RAND_MAX)].bats = True
        self._cave_rooms[randint(RAND_MIN, RAND_MAX)].wumpus = True

    def visit_room(self, room):
        return self._cave_rooms[int(room)].get_room()


class Room:
    wumpus, pit, bats = False, False, False
    paths = {}

    def __init__(self, room_map):
        self.paths['1'] = room_map[0]
        self.paths['2'] = room_map[1]
        self.paths['3'] = room_map[2]

    def get_room(self):
        return self.wumpus, self.pit, self.bats


class Adventurer:
    arrows = 5
    current_room = 1

    def set_current_room(self, room):
        self.current_room = room


class PlayGame:
    _game_over, _game_win = False, False
    _game_cave = []
    _game_adventurer = Adventurer()
    _user_input = ""

    def __init__(self):
        self._game_cave = Cave()

    def start_game(self):
        print("         WELCOME TO HUNT THE WUMPUS\n" +
              "YOU MUST FIND THE WUMPUS IN HIS DARK AND DANGEROUS LAIR!\n" +
              "YOU ARE EQUIPPED WITH A BOW AND FIVE ARROWS.")
        while not self._game_over:
            self._game_turn()
        if self._game_win:
            print("YOU SLEW THE FOUL WUMPUS!!!!")

    def _game_turn(self):

        current_room = self._game_cave.visit_room(self._game_adventurer.current_room)
        print("YOU ARE IN ROOM : "+str(self._game_adventurer.current_room))

        if current_room[0]:
            self._encountered_wumpus()

        elif current_room[1]:
            self._encountered_pit()

        elif current_room[2]:
            self._encountered_bats()

        if not self._game_over:
            self._check_connected_rooms()
            self._user_input = input(": ")
            self._interpret_command()

    def _interpret_command(self):

        goto_schemes = ("GO", "GOTO", "GO TO", "G")
        shoot_schemes = ("SHOOT", "S")
        look_schemes = ("LOOK", "L")

        if self._user_input.upper().startswith(goto_schemes):
            room = re.search("\d+", self._user_input).group()
            self._go_to_room(int(room))

        elif self._user_input.upper().startswith(shoot_schemes):
            room = re.search("\d+", self._user_input).group()
            self._shoot_arrow(room)

        elif self._user_input.upper().startswith(look_schemes):
            self._look()

        else:
            print("SORRY I DIDN'T UNDERSTAND THAT")

    def _go_to_room(self, room):

        if room in self._game_cave.cave_map[self._game_adventurer.current_room]:
            self._game_adventurer.set_current_room(room)
        else:
            print("YOU CANT GET THERE FROM HERE")

    def _encountered_wumpus(self):
        print("YOU ARE DEVOURED BY THE EVIL WUMPUS")
        self._game_over = True

    def _encountered_bats(self):
        print("OH NO YOU WERE GRABBED BY THE SUPER BATS")
        self._game_adventurer.current_room = randint(RAND_MIN, RAND_MAX)

    def _encountered_pit(self):
        print("YOU STUMBLE DOWN A BOTTOMLESS PIT!!")
        self._game_over = True

    def _shoot_arrow(self, room):
        print("TWWANG YOU LOOSE AN ARROW FROM YOUR MIGHTY YEW BOW!!")
        if room in self._game_cave.cave_map[self._game_adventurer.current_room]:
            if self._game_cave._cave_rooms[room].wumpus:
                print("YOUR SWIFT ARROW PUNCTURES THE HEART OF THE STINKING BEAST!")
                self._game_win = True
                self._game_over = True
                return
        print("CRUNCH THE ARROW BREAKS AGAINST THE STONE WALL OF THE CAVE!")

    def _look(self):
        rooms = self._game_cave.cave_map[self._game_adventurer.current_room]
        print("YOU SEE PATHS TO ROOMS "+str(rooms[0])+", "+str(rooms[1])+" and "+str(rooms[2]))

    def _check_connected_rooms(self):
        rooms = self._game_cave.cave_map[self._game_adventurer.current_room]
        for e in rooms:
            if self._game_cave.visit_room(e)[0]:
                print("YOU SMELL THE FOUL STENCH OF THE WUMPUS!")
            if self._game_cave.visit_room(e)[1]:
                print("YOU HEAR A RUSH OF WIND WHISTLING FROM A NEARBY CAVE!")
            if self._game_cave.visit_room(e)[2]:
                print("YOU HEAR A LEATHERY FLAPPING NOISE!")


game = PlayGame()
game.start_game()
