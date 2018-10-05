from random import randint
import re
from adventurer import Adventurer
from cave import Cave


class PlayGame:
    _game_over, _game_win = False, False
    _game_cave = []
    _game_adventurer = Adventurer()
    _user_input = ""
    _RAND_MAX = 20
    _RAND_MIN = 1

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
        quit_schemes = ("QUIT", "Q")

        if self._user_input.upper().startswith(goto_schemes):
            room = re.search("\d+", self._user_input).group()
            self._go_to_room(int(room))

        elif self._user_input.upper().startswith(shoot_schemes):
            room = re.search("\d+", self._user_input).group()
            self._shoot_arrow(int(room))

        elif self._user_input.upper().startswith(look_schemes):
            self._look()
        elif self._user_input.upper().startswith(quit_schemes):
            print("Goodbye....")
            self._game_over = True

        else:
            print("SORRY I DIDN'T UNDERSTAND THAT")

    def _go_to_room(self, room):

        if room in self._game_cave.cave_map[self._game_adventurer.current_room]:
            self._game_adventurer.set_current_room(room)
        else:
            print("YOU CANT GET THERE FROM HERE")

    def _shoot_arrow(self, room):
        print("TWWANG YOU LOOSE AN ARROW FROM YOUR MIGHTY YEW BOW!!")
        if room in self._game_cave.cave_map[self._game_adventurer.current_room]:
            if self._game_cave.visit_room(room)[0]:
                print("YOUR SWIFT ARROW PUNCTURES THE HEART OF THE STINKING BEAST!")
                self._game_win = True
                self._game_over = True
                return
        print("CRUNCH THE ARROW BREAKS AGAINST THE STONE WALL OF THE CAVE!")
        self._arrow_missed()

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

    def _arrow_missed(self):
        if randint(0, 3) != 3:
            print("You woke the Wumpus!")
            self._game_cave.wumpus_move()

    def _encountered_wumpus(self):
        print("YOU ARE DEVOURED BY THE EVIL WUMPUS")
        self._game_over = True

    def _encountered_bats(self):
        print("OH NO YOU WERE GRABBED BY THE SUPER BATS")
        self._game_adventurer.current_room = randint(self._RAND_MIN, self._RAND_MAX)

    def _encountered_pit(self):
        print("YOU STUMBLE DOWN A BOTTOMLESS PIT!!")
        self._game_over = True


game = PlayGame()
game.start_game()
