#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
DiceRPG.py: Generate top quality passwords from dice rolls with Python DiceRPG script

https://github.com/rafal-dot/DiceRPG

Created on Sat Sep  20 19:26:10 2021
@author: Rafal Czeczotka <rafal dot czeczotka at gmail.com>

Copyright (c) 2020-2023 Rafal Czeczotka

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see
<https://www.gnu.org/licenses/>.
"""

from math import floor, ceil, log

# Characters set for machine-storred, human-retyped passwords. For suggestions for (i) handwritten passwords or
# (ii) passwords stored and processed entirely by machine, see the documentation
ALPHABET = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!@#$%&()/?"

ALPHABET_LEN = len(ALPHABET)
DICE_FACES = 6

while True:
    print(f"""
Please enter random dice rolls (string of digits from 1 to 6), 67 characters alphabet
bits of entropy -->             |49  |61  |73    |91           |128
password length -->             |8   |10  |12    |15           |21
dice rolls      -->    1        v2   v    v3     v   4         5
  +-->        12345678901234567890123456789012345678901234567890""")
    dice_rolls_string = input("Dice numbers: ")
    if dice_rolls_string == "":
        break
    number_of_rolls = len(dice_rolls_string)

    effective_password_len = floor(number_of_rolls * log(DICE_FACES) / log(ALPHABET_LEN))
    effective_number_of_rolls = ceil(effective_password_len * log(ALPHABET_LEN) / log(DICE_FACES))
    bits_of_entropy = ceil(effective_password_len * log(ALPHABET_LEN) / log(2))

    random_number = 0
    for dice_roll_char in dice_rolls_string:
        random_number = DICE_FACES * random_number + (int(dice_roll_char) % DICE_FACES)

    password = ""
    for _ in range(effective_password_len):
        password = ALPHABET[random_number % ALPHABET_LEN] + password
        random_number = random_number // ALPHABET_LEN

    print(f"\nRolls of dice: {number_of_rolls} (used: {effective_number_of_rolls})"
          f"   Entropy: {bits_of_entropy} bits"
          f"   Length of password ({ALPHABET_LEN} chars alphabet): {effective_password_len}")
    print(f"Password: \"{password}\"")
