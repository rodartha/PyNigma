"""
Rotor.py
Author: Colin Page
colin.w.page1@gmail.com

This file holds the Rotor class which defines the functionality
of a single Enigma Rotor
"""


class Rotor():

    def __init__(self, rotor_num, start_pos):
        self.rotor_num = rotor_num
        self.pos = start_pos

        if self.rotor_num == 1:
            self.letter_map = MAP_ONE
            self.back_map = BACK_ONE
        elif self.rotor_num == 2:
            self.letter_map = MAP_TWO
            self.back_map = BACK_TWO
        elif self.rotor_num == 3:
            self.letter_map = MAP_THREE
            self.back_map = BACK_THREE
        elif self.rotor_num == 4:
            self.letter_map = MAP_FOUR
            self.back_map = BACK_FOUR
        else:
            self.letter_map = MAP_FIVE
            self.back_map = BACK_FIVE

    def run_letter(letter, forward_pass):
        if forward_pass:
            map_pos = (letter + self.pos) % 26

            return self.letter_map[map_pos]
        else:
            output = self.back_map[letter] - self.pos
            if output < 0:
                output += 26

            return output % 26
